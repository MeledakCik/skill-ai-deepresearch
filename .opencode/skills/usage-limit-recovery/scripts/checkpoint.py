"""Save or read one task's local recovery note. Requires Python 3.8+."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile


FORMAT = "usage-limit-recovery/1"
LIST_FIELDS = ("verified", "pending", "unverified")


def nonempty(text):
    if not text.strip():
        raise argparse.ArgumentTypeError("provide a nonempty note")
    return text.strip()


def validate(note):
    if not isinstance(note, dict) or note.get("format") != FORMAT:
        raise ValueError("unrecognized checkpoint format")
    if not isinstance(note.get("goal"), str) or not note["goal"].strip():
        raise ValueError("missing or invalid goal")
    for field in LIST_FIELDS:
        items = note.get(field)
        if not isinstance(items, list) or not all(isinstance(s, str) and s.strip() for s in items):
            raise ValueError(f"invalid {field} list")
    if "next" in note and note["next"] is None:
        if note["pending"] or note["unverified"] or not note["verified"]:
            raise ValueError("completion requires verified work and no pending or unchecked items")
    elif not isinstance(note.get("next"), str) or not note["next"].strip():
        raise ValueError("a partial checkpoint needs a next action")


def read_checkpoint(path):
    with path.open(encoding="utf-8") as stream:
        note = json.load(stream)
    validate(note)
    return note


def save_checkpoint(path, note):
    validate(note)
    if path.is_symlink():
        raise ValueError("choose a regular task file")
    if path.exists():
        read_checkpoint(path)  # Only replace a recognized checkpoint.
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, encoding="utf-8",
                                         prefix=".checkpoint-", suffix=".tmp", delete=False) as stream:
            temp_path = Path(stream.name)
            json.dump(note, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    save = commands.add_parser("save", help="replace the complete snapshot for one task")
    read = commands.add_parser("read", help="print a validated snapshot as JSON")
    for command in (save, read):
        command.add_argument("path", type=Path)
    save.add_argument("--goal", type=nonempty, required=True)
    for field in LIST_FIELDS:
        save.add_argument(f"--{field}", type=nonempty, action="append", default=[])
    outcome = save.add_mutually_exclusive_group(required=True)
    outcome.add_argument("--next", type=nonempty, help="first unmet check on resume")
    outcome.add_argument("--complete", action="store_true", help="all requested outcomes were verified")
    args = parser.parse_args()
    try:
        if args.command == "read":
            print(json.dumps(read_checkpoint(args.path), indent=2, ensure_ascii=True))
        else:
            note = {"format": FORMAT, "goal": args.goal, "next": args.next}
            note.update({key: getattr(args, key) for key in LIST_FIELDS})
            save_checkpoint(args.path, note)
            print("Checkpoint saved.")
    except (OSError, ValueError) as error:
        print(f"Checkpoint {args.command} failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
