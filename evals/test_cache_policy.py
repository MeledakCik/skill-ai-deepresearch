"""Exercise the shipped hook command and the policy actually loaded by each skill."""

import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts import sync


class CachePolicyTests(unittest.TestCase):
    def test_policy_is_in_every_distributed_entry_point(self):
        for base in ["skills", *sync.NATIVE_DIRS]:
            for name in sync.SKILLS:
                with self.subTest(base=base, skill=name):
                    body = (sync.ROOT / base / name / "SKILL.md").read_text(encoding="utf-8")
                    self.assertEqual(body.count(sync.CACHE_POLICY), 1)
                    self.assertLess(body.index(sync.CACHE_POLICY), body.index(sync.SKILLS[name]["core"]))

    def setUp(self):
        manifest = json.loads((sync.ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        self.hooks = json.loads((sync.ROOT / manifest["hooks"]).read_text(encoding="utf-8"))["hooks"]
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.env = dict(os.environ, PLUGIN_ROOT=str(sync.ROOT), PLUGIN_DATA=self.temp.name)
        self.file = sync.ROOT / "skills/deep-research-council/SKILL.md"
        self.body = self.file.read_text(encoding="utf-8")
        self.event = dict(hook_event_name="PostToolUse", session_id="session", turn_id="turn", agent_id="agent",
                          tool_name="Bash", cwd=str(sync.ROOT), tool_input={"command": f'cat "{self.file}"'},
                          tool_response=self.body)

    def invoke(self, **changes):
        event = {**self.event, **changes}
        cmd = self.hooks[event["hook_event_name"]][0]["hooks"][0]["command"]
        run = subprocess.run(cmd, shell=True, input=json.dumps(event), capture_output=True, encoding="utf-8",
                             env=self.env, check=True, timeout=8)
        return json.loads(run.stdout) if run.stdout else None

    def test_first_pass_duplicate_elided_and_files_still_verifiable(self):
        self.assertIsNone(self.invoke())
        duplicate = self.invoke(tool_input={"command": f'Get-Content -Raw -LiteralPath "{self.file}"'},
                                tool_response=self.body.replace("\n", "\r\n") + "\r\n")
        self.assertIs(duplicate["continue"], False)
        self.assertLess(len(duplicate["stopReason"]), 200)
        for changed in [self.body + "new content", self.body[:6000],
                        {"exit_code": 1, "output": self.body}, {"exit_code": 0, "output": self.body, "stderr": "error"}]:
            self.assertIsNone(self.invoke(tool_response=changed))
        for command in [f'Get-Content "{self.file}" -TotalCount 10', f'cat "{self.file}" | head',
                        'python run_tests.py', 'cat user-project/private.md']:
            self.assertIsNone(self.invoke(tool_input={"command": command}))

    def test_turn_session_compaction_and_concurrency(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: self.invoke(), range(2)))
        self.assertEqual(sum(r is None for r in results), 1)
        for scope in [dict(turn_id="next"), dict(session_id="another"), dict(agent_id="sibling"), dict(turn_id=None)]:
            self.assertIsNone(self.invoke(**scope))
        self.assertIsNone(self.invoke(hook_event_name="PostCompact"))
        self.assertIsNone(self.invoke())
        self.assertIsNotNone(self.invoke(session_id="another"))

    def test_small_reads_and_unwritable_state_pass(self):
        self.assertIsNone(self.invoke(tool_response="short result"))
        self.assertEqual(list(Path(self.temp.name).iterdir()), [])
        self.env["PLUGIN_DATA"] = str(self.file)
        self.assertIsNone(self.invoke())
