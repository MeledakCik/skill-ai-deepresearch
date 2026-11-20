"""Offline regression tests. Run with python -B -m unittest discover -s evals."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


SKILL_SCRIPTS = Path(__file__).resolve().parents[1] / "skills/usage-limit-recovery/scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import checkpoint


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = Path(folder.name) / "task notes" / "resume.json"

    def run_cli(self, command, *args):
        return subprocess.run([sys.executable, str(SKILL_SCRIPTS / "checkpoint.py"),
                               command, str(self.path), *args], capture_output=True, text=True)

    def save_partial(self):
        result = self.run_cli("save", "--goal", "Antrian café", "--verified", "Queue opens",
                              "--pending", "Confirm receipt", "--unverified", "Send timed out",
                              "--next", "Read receipt for order 42")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_resume_then_complete(self):
        self.save_partial()
        partial = json.loads(self.run_cli("read").stdout)
        self.assertEqual(partial["goal"], "Antrian café")
        self.assertEqual(partial["unverified"], ["Send timed out"])
        self.assertEqual(partial["next"], "Read receipt for order 42")
        result = self.run_cli("save", "--goal", partial["goal"], "--verified", "Queue opens",
                              "--verified", "Receipt for order 42 confirmed", "--complete")
        self.assertEqual(result.returncode, 0, result.stderr)
        final = json.loads(self.run_cli("read").stdout)
        self.assertEqual(len(final["verified"]), 2)
        self.assertEqual((final["pending"], final["unverified"], final["next"]), ([], [], None))

    def test_failed_replacement_preserves_previous_snapshot(self):
        self.save_partial()
        original = self.path.read_bytes()
        updated = checkpoint.read_checkpoint(self.path)
        updated["next"] = "Inspect the destination"
        with patch.object(checkpoint.os, "replace", side_effect=OSError("write interrupted")):
            with self.assertRaises(OSError):
                checkpoint.save_checkpoint(self.path, updated)
        self.assertEqual(self.path.read_bytes(), original)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_invalid_completion_preserves_partial(self):
        self.save_partial()
        original = self.path.read_bytes()
        for fields in ([], ["--verified", "Page opens", "--pending", "Check receipt"],
                       ["--verified", "Page opens", "--unverified", "Send timed out"]):
            with self.subTest(fields=fields):
                result = self.run_cli("save", "--goal", "Queue", "--complete", *fields)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(self.path.read_bytes(), original)

    def test_missing_and_unrecognized_checkpoint(self):
        self.assertNotEqual(self.run_cli("read").returncode, 0)
        self.path.parent.mkdir()
        for original in ("unrelated note", "{}", '{"format": "usage-limit-recovery/1"}'):
            with self.subTest(original=original):
                self.path.write_text(original, encoding="utf-8")
                result = self.run_cli("save", "--goal", "Queue", "--next", "Open page")
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(self.path.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
