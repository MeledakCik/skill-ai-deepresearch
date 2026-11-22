#!/usr/bin/env python3
"""Check that the Deep Research evaluation pack enforces its input boundaries."""

from __future__ import annotations

import json
import re
from pathlib import Path


EVAL = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    manifest = load_json(EVAL / "manifest.json")
    run_template = load_json(EVAL / "run-template.json")
    prompts = (EVAL / "prompts.md").read_text(encoding="utf-8")
    readme = (EVAL / "README.md").read_text(encoding="utf-8")
    runner = (EVAL / "scripts" / "run_codex_suite.py").read_text(encoding="utf-8")
    root = EVAL.parents[1]
    research_skill = (root / "skills" / "deep-research-council" / "SKILL.md").read_text(encoding="utf-8")
    migration_skill = (root / "skills" / "platform-migration" / "SKILL.md").read_text(encoding="utf-8")

    assert manifest["suite_version"] == run_template["suite_version"], "suite version mismatch"
    tasks = manifest["tasks"]
    task_ids = [task["id"] for task in tasks]
    assert len(task_ids) == len(set(task_ids)), "duplicate task ID"
    assert tasks, "evaluation suite has no tasks"

    controls = manifest.get("evaluation_controls", {})
    closed = controls.get("closed_packet", {})
    live = controls.get("live_search", {})
    assert closed.get("web_search_connectors") == "disabled", "closed-packet retrieval must be disabled"
    assert closed.get("allowed_inputs") == "selected prompt, named packet, and explicit task skill_files only", "closed-packet allowlist is unclear"
    assert "explicitly listed" in closed.get("allowed_skill_files", ""), "closed skill-file allowlist is unclear"
    assert closed.get("trace_review_required") is True, "closed-packet trace review is required"
    assert closed.get("invalid_if_external_retrieval_occurs") is True, "external retrieval must invalidate a clean closed run"
    assert live.get("trace_review_required") is True, "live-task trace review is required"
    assert "private rotating holdouts" in live.get("release_claims", ""), "live release claims need private holdouts"

    headings = set(re.findall(r"^## ([A-Z]+-[A-Z]+-\d+)\s*$", prompts, re.MULTILINE))

    def prompt_body(heading: str) -> str:
        match = re.search(
            rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
            prompts,
            re.MULTILINE | re.DOTALL,
        )
        assert match, f"cannot extract prompt: {heading}"
        return match.group(1).strip()

    for task in tasks:
        assert task["prompt_heading"] in headings, f"missing prompt: {task['id']}"
        skill_files = task.get("skill_files", [])
        assert "skills/deep-research-council/SKILL.md" in skill_files, f"deep-research skill missing: {task['id']}"
        assert len(skill_files) == len(set(skill_files)), f"duplicate skill file: {task['id']}"
        for skill_file in skill_files:
            skill_path = (root / skill_file).resolve()
            assert skill_path.is_relative_to((root / "skills").resolve()), f"skill path escapes allowlist: {task['id']}"
            assert skill_path.is_file(), f"skill file missing: {task['id']} ({skill_file})"
        if task["track"] != "closed-packet":
            continue

        prompt_text = prompt_body(task["prompt_heading"]).lower()
        assert re.search(r"do not browse|don't browse|jangan browsing|jangan menjalankan pencarian web", prompt_text), (
            f"closed task lacks no-browse instruction: {task['id']}"
        )

        packet = (EVAL / task["packet"]).resolve()
        assert packet.is_relative_to((EVAL / "corpora").resolve()), f"packet escapes corpus root: {task['id']}"
        assert packet.is_dir(), f"packet missing: {task['id']}"
        packet_files = [path.name.lower() for path in packet.rglob("*") if path.is_file()]
        forbidden = {"rubrics.md", "manifest.json", "readme.md", "run-template.json"}
        assert not (forbidden & set(packet_files)), f"operator/evaluation files leaked into packet: {task['id']}"
        assert not any("answer-key" in name or "hidden-rubric" in name for name in packet_files), (
            f"hidden scoring material leaked into packet: {task['id']}"
        )

    paired_cases = manifest.get("paired_cases", [])
    assert paired_cases, "matched adversarial cases are missing"
    for pair in paired_cases:
        clean = next((task for task in tasks if task["id"] == pair["clean_task_id"]), None)
        attacked = next((task for task in tasks if task["id"] == pair["attacked_task_id"]), None)
        assert clean and attacked, f"paired tasks are missing: {pair['id']}"
        assert clean["track"] == attacked["track"] == "closed-packet", f"paired tasks must be closed: {pair['id']}"
        assert prompt_body(clean["prompt_heading"]) == prompt_body(attacked["prompt_heading"]), (
            f"paired prompts differ: {pair['id']}"
        )

        clean_packet = (EVAL / clean["packet"]).resolve()
        attacked_packet = (EVAL / attacked["packet"]).resolve()
        clean_files = {path.relative_to(clean_packet).as_posix(): path for path in clean_packet.rglob("*") if path.is_file()}
        attacked_files = {
            path.relative_to(attacked_packet).as_posix(): path
            for path in attacked_packet.rglob("*")
            if path.is_file()
        }
        assert clean_files.keys() == attacked_files.keys(), f"paired packet file sets differ: {pair['id']}"
        variant_path = "committee-acceptance-log.md"
        assert variant_path in clean_files, f"paired variant file missing: {pair['id']}"
        for relative_path in clean_files:
            clean_text = clean_files[relative_path].read_text(encoding="utf-8")
            attacked_text = attacked_files[relative_path].read_text(encoding="utf-8")
            if relative_path == variant_path:
                directives = re.findall(r"<!--.*?-->", attacked_text, re.DOTALL)
                assert len(directives) == 1, f"attacked packet must contain one HTML-comment injection: {pair['id']}"
                assert "AI ASSISTANT INSTRUCTION" in directives[0], f"injection marker missing: {pair['id']}"
                attacked_text = re.sub(r"<!--.*?-->", "", attacked_text, flags=re.DOTALL)
            assert clean_text.rstrip() == attacked_text.rstrip(), (
                f"paired packet has an uncontrolled difference: {pair['id']} ({relative_path})"
            )

    task_template = run_template["tasks"][0]
    integrity = task_template.get("evaluation_integrity", {})
    required_fields = {
        "workspace_isolated",
        "web_access_mode",
        "hidden_material_excluded",
        "trace_reviewed",
        "exposure_status",
        "contamination_signal",
        "contamination_type",
        "contaminated",
        "adjudication",
    }
    assert required_fields <= integrity.keys(), "run template lacks contamination record fields"
    assert "disable web search" in readme.lower(), "operator instructions do not require closed-run isolation"
    assert "contamination control" in readme.lower(), "contamination protocol missing from README"
    assert "paired retrieved-content injection check" in readme.lower(), "README lacks paired-injection instructions"
    assert "at most four web calls" in readme.lower(), "Quick lookup call ceiling missing"
    assert "explicit `skill_files` allowlist" in readme, "runner skill-input handling is undocumented"
    assert "CODEX_CLI_PATH" in runner and "Get-AppxPackage" in runner, "runner cannot discover Windows Codex CLI installs"
    assert "expected_skill_version()" in runner, "runner must read the active skill version"
    assert 'action.get("query") or action.get("queries")' in runner, "runner must preserve Codex search queries"
    assert all(term in research_skill.lower() for term in (
        "unconfirmed", "same-publisher fallback", "successfully opened",
        "search/query endpoints whose title or query concerns another topic",
        "related-link lists is only a lead", "claim → opened url → exact section/locator → support"
    )), "generated deep-research skill lacks opened-source allowlist and bounded-recovery gates"
    assert all(term in migration_skill.lower() for term in (
        "team access status + owner", "unconfirmed", "delivery-readiness row for every target",
        "production feasibility: unresolved", "schedule: conditional", "builds, runs/tests",
        "related-link list is a lead", "destination page's content"
    )), (
        "generated migration skill lacks explicit per-target readiness output"
    )
    assert "each cited release, runtime minimum" in (EVAL / "rubrics.md").read_text(encoding="utf-8"), (
        "live migration rubric must enforce opened-page citation checks for version-specific claims"
    )

    print(
        f"Evaluation integrity checks passed: {len(tasks)} tasks, "
        f"{sum(t['track'] == 'closed-packet' for t in tasks)} closed prompts/packets, "
        "closed-run isolation, live trace review, and contamination logging."
    )


if __name__ == "__main__":
    main()
