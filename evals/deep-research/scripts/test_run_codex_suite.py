#!/usr/bin/env python3
"""Focused unit checks for Codex trace parsing and version discovery."""

from __future__ import annotations

import json
import os
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

from run_codex_suite import (
    budget_report,
    expected_skill_version,
    parse_trace,
    resolve_codex,
    run_ceiling_stop_reason,
    task_input,
    windows_app_codex_path,
)


class ParseTraceTests(unittest.TestCase):
    def test_captures_queries_array_url_and_usage(self) -> None:
        events = [
            {
                "type": "item.completed",
                "item": {
                    "type": "web_search",
                    "query": "outer query",
                    "action": {"type": "search", "queries": ["q1", "q2"]},
                },
            },
            {
                "type": "item.completed",
                "item": {"type": "web_search", "action": {"type": "open", "url": "https://example.test/source"}},
            },
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Done."}},
            {
                "type": "turn.completed",
                "usage": {"input_tokens": 12, "cached_input_tokens": 3, "output_tokens": 4},
            },
        ]

        parsed = parse_trace("\n".join(json.dumps(event) for event in events))

        self.assertEqual(parsed["answer"], "Done.")
        self.assertEqual(parsed["input_tokens"], 12)
        self.assertEqual(parsed["cached_input_tokens"], 3)
        self.assertEqual(parsed["output_tokens"], 4)
        self.assertEqual(parsed["web_search_tool_calls"], 2)
        self.assertEqual(parsed["search_actions"], 1)
        self.assertEqual(parsed["search_log"][0]["query"], ["q1", "q2"])
        self.assertEqual(parsed["search_log"][1]["url"], "https://example.test/source")

    def test_active_skill_version_is_read_from_master(self) -> None:
        self.assertRegex(expected_skill_version(), r"^\d+\.\d+\.\d+$")

    def test_allowlisted_skill_is_embedded_without_repository_access(self) -> None:
        combined, images, packet_files, skill_files = task_input(
            {"packet": None, "skill_files": ["skills/platform-migration/SKILL.md"]},
            "Choose a migration route.",
        )

        self.assertEqual(images, [])
        self.assertEqual(packet_files, [])
        self.assertEqual(skill_files, ["skills/platform-migration/SKILL.md"])
        self.assertIn("Trusted selected skill file", combined)
        self.assertIn("delivery-readiness row", combined)
        self.assertIn("Choose a migration route.", combined)
        self.assertIn("Do not try to read them from repository paths", combined)

    def test_explicit_codex_path_resolves_without_path_entry(self) -> None:
        expected = str(Path(__file__).resolve())
        with patch("run_codex_suite.shutil.which", return_value=None):
            self.assertEqual(os.path.normcase(resolve_codex(expected)), os.path.normcase(expected))

    def test_codex_cli_path_environment_variable_is_supported(self) -> None:
        expected = str(Path(__file__).resolve())
        with patch.dict(os.environ, {"CODEX_CLI_PATH": expected}), patch(
            "run_codex_suite.shutil.which", return_value=None
        ):
            self.assertEqual(os.path.normcase(resolve_codex()), os.path.normcase(expected))

    @unittest.skipUnless(os.name == "nt", "Windows app-package discovery is Windows-only")
    def test_windows_app_fallback_works_when_codex_is_not_on_path(self) -> None:
        expected = windows_app_codex_path()
        if not expected:
            self.skipTest("Codex Store app package is not installed on this host")
        real_which = shutil.which
        with patch(
            "run_codex_suite.shutil.which",
            side_effect=lambda name: None if name == "codex" else real_which(name),
        ):
            self.assertEqual(
                os.path.normcase(resolve_codex()),
                os.path.normcase(str(Path(expected).resolve())),
            )


class BudgetReportTests(unittest.TestCase):
    def test_final_task_overrun_is_recorded_as_complete_not_checkpointed(self) -> None:
        report = budget_report(
            {"input_tokens": 110, "output_tokens": 8, "web_search_tool_calls": 2},
            {"max_input_tokens": 100, "max_output_tokens": 20, "max_web_calls": 4},
        )

        self.assertEqual(report["status"], "exceeded")
        self.assertEqual(report["overages"]["input_tokens"], 10)
        self.assertEqual(
            run_ceiling_stop_reason(report, []),
            "run ceiling exceeded during the final task; all selected tasks completed and the overrun is recorded",
        )

    def test_mid_run_overrun_retains_checkpoint_reason(self) -> None:
        report = budget_report(
            {"input_tokens": 101, "output_tokens": 8, "web_search_tool_calls": 2},
            {"max_input_tokens": 100, "max_output_tokens": 20, "max_web_calls": 4},
        )

        self.assertEqual(
            run_ceiling_stop_reason(report, ["LIVE-ID-03"]),
            "run ceiling exceeded after a completed task; checkpoint saved before the next task",
        )

    def test_exact_ceiling_is_reached_but_not_overrun(self) -> None:
        report = budget_report(
            {"input_tokens": 100, "output_tokens": 8, "web_search_tool_calls": 2},
            {"max_input_tokens": 100, "max_output_tokens": 20, "max_web_calls": 4},
        )

        self.assertEqual(report["status"], "ceiling_reached")
        self.assertEqual(run_ceiling_stop_reason(report, ["LIVE-ID-03"]), "")


if __name__ == "__main__":
    unittest.main()
