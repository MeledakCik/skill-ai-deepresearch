"""Native after-tool adapters for large, complete reads of this package's Markdown."""

import copy
import json
import os
import re
import runpy
import sqlite3
import sys
from pathlib import Path

CORE = runpy.run_path(str(Path(__file__).with_name("cache_guard.py")))
ROOT = Path(__file__).resolve().parent.parent
NOTICE = CORE["NOTICE"]
SKILL_DIR = {"claude": ("skills",), "gemini": ("skills", ".gemini/skills"),
             "copilot": (".github/skills",), "opencode": (".opencode/skills",)}


def complete_text(value, expected):
    if not isinstance(value, str):
        return False
    value = value.replace("\r\n", "\n")
    if value in (expected, expected + "\n", expected.removesuffix("\n")):
        return True
    # Some native readers prefix every line with its number. Verify each line.
    lines = value.splitlines()
    original = expected.splitlines()
    if len(lines) != len(original):
        return False
    for index, (line, source) in enumerate(zip(lines, original), start=1):
        match = re.fullmatch(r"\s*(\d+)(?:\t|: |\. |\.  |\| )(.*)", line)
        if not match or int(match[1]) != index or match[2] != source:
            return False
    return True


def observed_read(host, event):
    name = event.get("tool_name") or event.get("toolName")
    args = event.get("tool_input", event.get("toolArgs"))
    result = event.get("tool_response", event.get("toolResult"))
    if host == "copilot" and isinstance(args, str):
        args = json.loads(args)
    if not isinstance(args, dict) or not isinstance(result, dict):
        return None
    if any(result.get(key) for key in ("error", "stderr", "interrupted", "isImage", "backgroundTaskId", "persistedOutputPath")):
        return None
    if any(key in args for key in ("offset", "limit", "pages", "view_range", "start_line", "end_line")):
        return None

    if host == "claude" and name == "Read":
        file = result.get("file")
        if result.get("type") != "text" or not isinstance(file, dict) or file.get("startLine") != 1:
            return None
        if file.get("numLines") != file.get("totalLines") or file.get("filePath") != args.get("file_path"):
            return None
        return args.get("file_path"), file.get("content")
    if host == "gemini" and name == "read_file":
        value = result.get("llmContent")
        if isinstance(value, list) and len(value) == 1 and isinstance(value[0], dict):
            value = value[0].get("text") if set(value[0]) == {"text"} else None
        return args.get("file_path") or args.get("absolute_path"), value
    if host == "copilot" and result.get("resultType") != "success":
        return None
    if host == "copilot" and name == "view":
        return args.get("path"), result.get("textResultForLlm")
    if host == "opencode" and name == "read":
        return args.get("filePath"), result.get("content")
    if (host, name) not in (("claude", "Bash"), ("copilot", "bash"), ("copilot", "powershell"), ("opencode", "bash")):
        return None
    cmd = args.get("command")
    if not isinstance(cmd, str) or any(c in cmd for c in "|;&<>*$\x60?\r\n"):
        return None
    match = CORE["READ"].fullmatch(cmd.strip())
    if match:
        return next(v for v in match.groups() if v is not None), result.get("stdout", result.get("textResultForLlm", result.get("content")))


def adapt(host, phase, event, data, root=ROOT):
    if not isinstance(event, dict):
        return {}
    session = event.get("session_id") or event.get("sessionId")
    if not isinstance(session, str) or not session:
        return {}
    scope = CORE["digest"](host, str(root), session)
    if phase == "reset":
        CORE["decision"]({"hook_event_name": "PostCompact", "session_id": scope}, data)
        return {}
    if phase != "read":
        return {}
    item = observed_read(host, event)
    if not item or not all(isinstance(x, str) and x for x in item):
        return {}
    path, text = item
    if len(text.encode("utf-8")) < CORE["MIN_BYTES"]:
        return {}
    candidate = (Path(event.get("cwd") or root) / path).resolve()
    relative = CORE["SKILL_PATH"].search(candidate.as_posix())
    if not relative:
        return {}
    # Native agents also open project mirrors of an installed skill. Verify that exact shipped edition.
    source = None
    roots = [root / folder for folder in SKILL_DIR[host]]
    roots.sort(key=lambda folder: folder not in candidate.parents)
    for skills in roots:
        copy_path = (skills / relative[1] / relative[2]).resolve()
        if skills in copy_path.parents and copy_path.is_file():
            source = copy_path
            break
    if source is None:
        return {}
    body = source.read_text(encoding="utf-8")
    if host == "opencode" and text.startswith("<path>"):
        framed = re.fullmatch(r"<path>([^\r\n]+)</path>\n<type>file</type>\n<content>\n(.*?)\n\n\(End of file - total (\d+) lines\)\n</content>\s*", text.replace("\r\n", "\n"), re.S)
        if not framed or Path(framed[1]).resolve() != candidate or int(framed[3]) != len(body.splitlines()):
            return {}
        text = framed[2]
    if not complete_text(text, body):
        return {}
    # Hosts reset session state at the turn and compaction boundaries.
    normalized = dict(hook_event_name="PostToolUse", tool_name="Bash", session_id=scope,
                      agent_id=event.get("agent_id", event.get("agentId")), turn_id=event.get("turn_id") or "current",
                      tool_input={"command": f'cat "{source}"'}, tool_response=body)
    if not CORE["decision"](normalized, data, skills):
        return {}
    if host == "claude":
        replacement = copy.deepcopy(event["tool_response"])
        if event["tool_name"] == "Read":
            replacement["file"].update(content=NOTICE, numLines=1, startLine=1, totalLines=1)
        else:
            replacement["stdout"] = NOTICE
        return {"hookSpecificOutput": {"hookEventName": "PostToolUse", "updatedToolOutput": replacement}}
    if host == "gemini":
        return {"decision": "deny", "reason": NOTICE}
    if host == "opencode":
        return {"content": NOTICE}
    return {"modifiedResult": {"resultType": "success", "textResultForLlm": NOTICE}}


def main():
    raw = sys.stdin.buffer.read(CORE["MAX_EVENT_BYTES"] + 1)
    result = {}
    if len(sys.argv) == 3 and sys.argv[1] in SKILL_DIR and len(raw) <= CORE["MAX_EVENT_BYTES"]:
        try:
            cache = Path(os.environ.get("LOCALAPPDATA") or os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
            result = adapt(sys.argv[1], sys.argv[2], json.loads(raw), cache / "deep-research-domain-council" / "hooks")
        except (ValueError, TypeError, OSError, RuntimeError, sqlite3.Error):
            pass  # Tool errors, constrained environments and unknown result shapes keep their output.
    print(json.dumps(result))


if __name__ == "__main__":
    main()
