#!/usr/bin/env python3
"""Focused unit checks for Codex trace parsing and version discovery."""

from __future__ import annotations

import json
import unittest

from run_codex_suite import expected_skill_version, parse_trace, task_input


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


if __name__ == "__main__":
    unittest.main()
