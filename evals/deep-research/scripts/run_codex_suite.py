#!/usr/bin/env python3
"""Run the selected Deep Research prompts in fresh, isolated Codex CLI sessions.

This runner reads the manifest, visible prompt bodies, explicitly selected skill
files and named packet only. It never reads the hidden rubric. Human scoring
remains separate.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVAL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = EVAL_ROOT.parents[1]
QUOTA_RE = re.compile(
    r"usage limit|rate limit|quota.{0,30}(exceed|exhaust)|"
    r"(exceed|exhaust).{0,30}(limit|quota)|weekly limit|free.?tier.{0,20}limit",
    re.IGNORECASE,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def expected_skill_version() -> str:
    master = (REPO_ROOT / "deep-research-domain-council" / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r'(?m)^  version: "([^"]+)"$', master)
    if not match:
        raise ValueError("Active skill version is missing from master SKILL.md")
    return match.group(1)


def read_prompt_bodies() -> dict[str, str]:
    text = (EVAL_ROOT / "prompts.md").read_text(encoding="utf-8")
    headings = list(re.finditer(r"(?m)^## (CP-[A-Z]+-\d+|LIVE-[A-Z]+-\d+)\s*$", text))
    prompts: dict[str, str] = {}
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        prompts[match.group(1)] = text[match.end():end].strip()
    return prompts


def task_input(task: dict[str, Any], prompt: str) -> tuple[str, list[str], list[str], list[str]]:
    supplied_skill_files: list[str] = []
    skill_parts: list[str] = []
    skills_root = (REPO_ROOT / "skills").resolve()
    for relative in task.get("skill_files", ["skills/deep-research-council/SKILL.md"]):
        skill_path = (REPO_ROOT / relative).resolve()
        if skills_root not in skill_path.parents or skill_path.suffix.lower() != ".md":
            raise ValueError(f"Skill file is outside the skills allowlist: {relative}")
        if not skill_path.is_file():
            raise FileNotFoundError(f"Selected skill file is missing: {relative}")
        supplied_skill_files.append(skill_path.relative_to(REPO_ROOT).as_posix())
        skill_parts.append(f"\n\n--- Trusted selected skill file: {supplied_skill_files[-1]} ---\n{skill_path.read_text(encoding='utf-8')}")

    packet = task.get("packet")
    text_parts = [
        "Follow the selected skill instructions embedded below. Do not try to read them from repository paths; their full contents are supplied here. Then answer the user's task.\n",
        *skill_parts,
        f"\n\n--- User task ---\n{prompt}",
    ]
    if not packet:
        return "".join(text_parts), [], [], supplied_skill_files

    packet_dir = (EVAL_ROOT / packet).resolve()
    if EVAL_ROOT.resolve() not in packet_dir.parents:
        raise ValueError(f"Packet path escapes evaluation root: {packet}")

    images: list[str] = []
    supplied_files: list[str] = []
    for path in sorted(p for p in packet_dir.rglob("*") if p.is_file()):
        suffix = path.suffix.lower()
        rel = path.relative_to(packet_dir).as_posix()
        supplied_files.append(rel)
        if suffix in {".png", ".jpg", ".jpeg", ".webp"}:
            images.append(str(path))
            continue
        if suffix not in {".md", ".txt", ".csv", ".json", ".html", ".xml"}:
            continue
        content = path.read_text(encoding="utf-8-sig")
        text_parts.append(f"\n\n--- Untrusted allowed packet file: {rel} ---\n{content}")
    return "".join(text_parts), images, supplied_files, supplied_skill_files


def parse_trace(stdout: str) -> dict[str, Any]:
    answer = ""
    input_tokens = cached_tokens = output_tokens = 0
    web_calls = search_actions = 0
    action_log: list[dict[str, Any]] = []
    event_count = 0
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_count += 1
        if event.get("type") == "turn.completed":
            usage = event.get("usage", {})
            input_tokens += int(usage.get("input_tokens", 0) or 0)
            cached_tokens += int(usage.get("cached_input_tokens", 0) or 0)
            output_tokens += int(usage.get("output_tokens", 0) or 0)
        if event.get("type") != "item.completed":
            continue
        item = event.get("item", {})
        if item.get("type") == "agent_message":
            answer = item.get("text", answer)
        elif item.get("type") == "web_search":
            web_calls += 1
            action = item.get("action", {})
            action_type = action.get("type", "unknown")
            if action_type in {"search", "search_query", "search_queries"}:
                search_actions += 1
            action_log.append({
                "action": action_type,
                "query": action.get("query") or action.get("queries") or item.get("query"),
                "url": action.get("url", item.get("url")),
            })
    return {
        "answer": answer,
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "output_tokens": output_tokens,
        "web_search_tool_calls": web_calls,
        "search_actions": search_actions,
        "search_log": action_log,
        "json_events": event_count,
    }


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Output directory under evals/deep-research/runs")
    parser.add_argument("--task-ids", nargs="*", help="Optional task IDs; omit to run the whole manifest")
    parser.add_argument("--task-timeout-seconds", type=int, default=900)
    parser.add_argument("--max-web-calls", type=int, default=48, help="Stop before the next task after this many web tool calls")
    parser.add_argument("--max-input-tokens", type=int, default=1_700_000, help="Checkpoint ceiling checked between tasks")
    parser.add_argument("--max-output-tokens", type=int, default=40_000, help="Checkpoint ceiling checked between tasks")
    parser.add_argument("--force", action="store_true", help="Rerun tasks that already have a completed task.json")
    args = parser.parse_args()

    codex = shutil.which("codex")
    if not codex:
        parser.error("Codex CLI was not found on PATH")

    manifest = json.loads((EVAL_ROOT / "manifest.json").read_text(encoding="utf-8"))
    prompts = read_prompt_bodies()
    all_tasks = manifest["tasks"]
    selected_ids = set(args.task_ids or [task["id"] for task in all_tasks])
    unknown = selected_ids - {task["id"] for task in all_tasks}
    if unknown:
        parser.error(f"Unknown task IDs: {', '.join(sorted(unknown))}")
    tasks = [task for task in all_tasks if task["id"] in selected_ids]

    run_dir = (EVAL_ROOT / args.run_dir).resolve()
    runs_root = (EVAL_ROOT / "runs").resolve()
    if runs_root not in run_dir.parents:
        parser.error("--run-dir must resolve beneath evals/deep-research/runs")
    run_dir.mkdir(parents=True, exist_ok=True)

    execution_path = run_dir / "execution.json"
    execution: dict[str, Any] = {
        "started_at": utc_now(),
        "codex_cli": subprocess.run([codex, "--version"], capture_output=True, text=True, check=False).stdout.strip(),
        "skill_version_expected": expected_skill_version(),
        "suite_version": manifest["suite_version"],
        "selected_task_ids": [task["id"] for task in tasks],
        "caps": {
            "max_web_calls": args.max_web_calls,
            "max_input_tokens_checked_between_tasks": args.max_input_tokens,
            "max_output_tokens_checked_between_tasks": args.max_output_tokens,
            "task_timeout_seconds": args.task_timeout_seconds,
        },
        "status": "in_progress",
        "completed_task_ids": [],
        "remaining_task_ids": [task["id"] for task in tasks],
        "totals": {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "web_search_tool_calls": 0, "search_actions": 0},
        "tasks": [],
    }
    if execution_path.exists() and not args.force:
        previous = json.loads(execution_path.read_text(encoding="utf-8"))
        by_id = {record["task_id"]: record for record in previous.get("tasks", [])}
        execution["tasks"] = [by_id[task["id"]] for task in tasks if task["id"] in by_id]
        execution["completed_task_ids"] = [
            record["task_id"] for record in execution["tasks"] if record.get("status") == "completed"
        ]
        execution["totals"] = previous.get("totals", execution["totals"])
        if not args.force:
            tasks = [task for task in tasks if task["id"] not in set(execution["completed_task_ids"])]
        execution["remaining_task_ids"] = [task["id"] for task in tasks]

    temp_root = Path(tempfile.gettempdir()).resolve()
    stopped_reason = ""
    for task in tasks:
        totals = execution["totals"]
        if totals["web_search_tool_calls"] >= args.max_web_calls:
            stopped_reason = "web tool-call ceiling reached; checkpoint before the next task"
            break
        if totals["input_tokens"] >= args.max_input_tokens or totals["output_tokens"] >= args.max_output_tokens:
            stopped_reason = "token ceiling reached; checkpoint before the next task"
            break

        task_id = task["id"]
        prompt = prompts.get(task.get("prompt_heading", task_id))
        if not prompt:
            raise ValueError(f"Prompt body missing for {task_id}")
        combined_prompt, images, supplied_files, supplied_skill_files = task_input(task, prompt)
        artifact_dir = run_dir / task_id
        artifact_dir.mkdir(parents=True, exist_ok=True)
        task_started_at = utc_now()
        task_started = time.monotonic()
        stdout = ""
        stderr = ""
        status = "failed"
        exit_code: int | None = None
        timeout_error = ""

        with tempfile.TemporaryDirectory(prefix="codex-dr-", dir=str(temp_root)) as work:
            work_dir = Path(work).resolve()
            if temp_root not in work_dir.parents:
                raise RuntimeError("Temporary task directory escaped the system temp root")
            command = [codex, "exec", "--json", "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only", "--cd", str(work_dir)]
            if task.get("track") == "closed-packet":
                command.extend(["--config", "mcp_servers.depup.enabled=false"])
            for image in images:
                command.extend(["--image", image])
            command.append("-")
            try:
                result = subprocess.run(
                    command,
                    input=combined_prompt,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=args.task_timeout_seconds,
                    cwd=str(work_dir),
                    check=False,
                )
                stdout, stderr, exit_code = result.stdout, result.stderr, result.returncode
            except subprocess.TimeoutExpired as exc:
                timeout_error = f"task timed out after {args.task_timeout_seconds} seconds"
                stdout = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
                stderr = exc.stderr.decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")

        parsed = parse_trace(stdout)
        if parsed["answer"]:
            status = "completed"
            (artifact_dir / "answer.md").write_text(parsed["answer"].rstrip() + "\n", encoding="utf-8")
        (artifact_dir / "trace.jsonl").write_text(stdout, encoding="utf-8")
        (artifact_dir / "stderr.log").write_text(stderr, encoding="utf-8")
        task_record = {
            "task_id": task_id,
            "track": task.get("track"),
            "status": status,
            "started_at": task_started_at,
            "finished_at": utc_now(),
            "wall_time_seconds": round(time.monotonic() - task_started, 2),
            "exit_code": exit_code,
            "timeout_error": timeout_error,
            "answer_artifact": f"{task_id}/answer.md" if parsed["answer"] else "",
            "skill_files_supplied": supplied_skill_files,
            "packet_files_supplied": supplied_files,
            **{key: parsed[key] for key in ("input_tokens", "cached_input_tokens", "output_tokens", "web_search_tool_calls", "search_actions", "search_log", "json_events")},
            "tool_failures_or_unavailable": [line for line in stderr.splitlines() if "error" in line.lower() or "failed" in line.lower()],
        }
        save_json(artifact_dir / "task.json", task_record)
        execution["tasks"] = [record for record in execution["tasks"] if record["task_id"] != task_id]
        execution["tasks"].append(task_record)
        if status == "completed":
            execution["completed_task_ids"].append(task_id)
        for key in execution["totals"]:
            execution["totals"][key] += parsed[key]
        completed_set = set(execution["completed_task_ids"])
        execution["remaining_task_ids"] = [task["id"] for task in all_tasks if task["id"] in selected_ids and task["id"] not in completed_set]
        save_json(execution_path, execution)
        print(
            f"{task_id}: {status}; input={parsed['input_tokens']}; output={parsed['output_tokens']}; "
            f"web_calls={parsed['web_search_tool_calls']}; search_actions={parsed['search_actions']}",
            flush=True,
        )

        failure_events = []
        for line in stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") in {"error", "turn.failed", "item.failed"}:
                failure_events.append(json.dumps(event, ensure_ascii=False))
        if QUOTA_RE.search(stderr) or QUOTA_RE.search("\n".join(failure_events)):
            stopped_reason = "host usage/quota limit reported; saved checkpoint and stopped"
            break
        if totals["web_search_tool_calls"] > args.max_web_calls or totals["input_tokens"] > args.max_input_tokens or totals["output_tokens"] > args.max_output_tokens:
            stopped_reason = "run ceiling exceeded; saved checkpoint and stopped before next task"
            break

    completed_set = set(execution["completed_task_ids"])
    execution["remaining_task_ids"] = [task["id"] for task in all_tasks if task["id"] in selected_ids and task["id"] not in completed_set]
    execution["status"] = "complete" if not execution["remaining_task_ids"] else "partial"
    execution["stop_reason"] = stopped_reason
    execution["finished_at"] = utc_now()
    save_json(execution_path, execution)
    print(f"RUN {execution['status']}: {len(execution['completed_task_ids'])}/{len(selected_ids)} completed; {stopped_reason or 'all selected tasks produced answers'}", flush=True)
    return 0 if execution["status"] == "complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
