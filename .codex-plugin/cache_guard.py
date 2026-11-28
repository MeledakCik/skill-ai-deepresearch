"""Keep repeated full skill-file output out of a Codex turn. No model or network calls."""

import hashlib
import json
import os
import re
import sqlite3
import sys
import time
from contextlib import closing
from pathlib import Path


SKILLS = Path(__file__).resolve().parent.parent / "skills"
MIN_BYTES = 4096
MAX_EVENT_BYTES = 2 * 1024 * 1024
READ = re.compile(
    r"""(?:cat(?:\s+--)?|Get-Content(?:\s+-(?:Raw|(?:Literal)?Path|Encoding\s+utf-?8))*)\s+"""
    r"""(?:"([^"\r\n]+)"|'([^'\r\n]+)'|([^\s'"]+))""", re.IGNORECASE,
)
SKILL_PATH = re.compile(r"(?:^|/)skills/([a-z0-9_-]+)/((?:SKILL|references/part-[a-z0-9-]+)\.md)$", re.IGNORECASE)
NOTICE = "This complete skill file was already returned in this turn. Reuse it, or read the specific heading or range needed."


def digest(*parts):
    return hashlib.sha256(json.dumps(parts, ensure_ascii=True).encode("ascii")).hexdigest()


def matching_read(event, skills):
    """Only elide text proven equal to a shipped document. Other shell output passes."""
    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict) or not isinstance(tool_input.get("command"), str):
        return None
    command = tool_input["command"].strip()
    if any(char in command for char in "|;&<>*$\x60?\r\n"):
        return None
    read = READ.fullmatch(command)
    if not read:
        return None
    path = next(value for value in read.groups() if value is not None)
    location = (Path(event.get("cwd") or ".") / path).as_posix().replace("\\", "/")
    rel = SKILL_PATH.search(location)
    if not rel:
        return None
    response = event.get("tool_response")
    if isinstance(response, dict):
        if response.get("exit_code") != 0 or response.get("stderr") or response.get("session_id") is not None:
            return None
        response = response.get("output")
    if not isinstance(response, str) or len(response.encode("utf-8")) < MIN_BYTES:
        return None
    source = (skills / rel[1] / rel[2]).resolve()
    if skills not in source.parents or not source.is_file():
        return None
    body = source.read_text(encoding="utf-8")
    if response.replace("\r\n", "\n") not in (body, body + "\n", body.removesuffix("\n")):
        return None
    return digest(source.relative_to(skills).as_posix(), body)


def decision(event, data, skills=SKILLS):
    if not isinstance(event, dict) or not data or not event.get("session_id"):
        return None
    kind = event.get("hook_event_name")
    session = digest(event["session_id"])
    db = Path(data) / "skill-read-hashes.sqlite3"
    if kind == "PostCompact":
        if db.is_file():
            with closing(sqlite3.connect(db, timeout=0.25)) as conn, conn:
                conn.execute("DELETE FROM seen WHERE session = ?", (session,))
        return None
    if kind != "PostToolUse" or event.get("tool_name") != "Bash" or not event.get("turn_id"):
        return None
    fingerprint = matching_read(event, skills)
    if not fingerprint:
        return None
    turn = digest(event["turn_id"], event.get("agent_id"))
    db.parent.mkdir(parents=True, exist_ok=True)
    now = int(time.time())
    with closing(sqlite3.connect(db, timeout=0.25)) as conn, conn:
        conn.execute("CREATE TABLE IF NOT EXISTS seen (session TEXT, turn TEXT, item TEXT, at INTEGER, PRIMARY KEY(session, turn, item))")
        conn.execute("DELETE FROM seen WHERE at < ?", (now - 86400,))
        first = conn.execute("INSERT OR IGNORE INTO seen VALUES (?, ?, ?, ?)", (session, turn, fingerprint, now)).rowcount
    if first:
        return None
    return {"continue": False, "stopReason": NOTICE}


def main():
    raw = sys.stdin.buffer.read(MAX_EVENT_BYTES + 1)
    if len(raw) > MAX_EVENT_BYTES:
        return
    try:
        result = decision(json.loads(raw), os.environ.get("PLUGIN_DATA"))
    except (ValueError, OSError, sqlite3.Error, TypeError):
        return  # Missing metadata, an unavailable store or an unfamiliar payload leaves the result intact.
    if result:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
