"""Black-box checks using the native registrations and separately extracted ZIPs."""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

from scripts import sync


class HostGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.base = Path(cls.temp.name)
        for host in ("claude", "gemini", "copilot", "opencode"):
            sync.make_platform_zip(host, cls.base)
            with zipfile.ZipFile(cls.base / f"{sync.ROOT.name}-{host}.zip") as z:
                z.extractall(cls.base / host)

    def run_hook(self, host, phase, event):
        root = self.base / host
        files = {"claude": ".claude-plugin/hooks.json", "gemini": "hooks/hooks.json",
                 "copilot": ".github/hooks/council-cache.json"}
        conf = json.loads((root / files[host]).read_text(encoding="utf-8"))["hooks"]
        keys = {"claude": ("PostToolUse", "UserPromptSubmit", "PreCompact"),
                "gemini": ("AfterTool", "BeforeAgent", "PreCompress"),
                "copilot": ("postToolUse", "userPromptSubmitted", "preCompact")}
        name = keys[host][phase]
        registration = conf[name][0]
        if host == "copilot":
            cmd = registration["powershell" if os.name == "nt" else "bash"]
        else:
            cmd = registration["hooks"][0]["command"]
            cmd = cmd.replace("\x24{CLAUDE_PLUGIN_ROOT}", str(root)).replace("\x24{extensionPath}", str(root))
        env = dict(os.environ, LOCALAPPDATA=str(self.base / "state"))
        result = subprocess.run(cmd, shell=True, input=json.dumps(event), encoding="utf-8",
                                capture_output=True, cwd=root, env=env, timeout=8, check=True)
        return json.loads(result.stdout)

    def test_native_read_shapes_and_reset(self):
        for host in ("claude", "gemini", "copilot"):
            with self.subTest(host=host):
                root = self.base / host
                rel = "skills/deep-research-council/SKILL.md"
                path = str(root / (".github" if host == "copilot" else "") / rel)
                text = Path(path).read_text(encoding="utf-8").rstrip("\n")
                n = len(text.splitlines())
                if host == "claude":
                    event = dict(session_id="s", tool_name="Read", tool_input={"file_path": path},
                                 tool_response={"type": "text", "file": {"filePath": path, "content": text,
                                                "startLine": 1, "numLines": n, "totalLines": n}})
                elif host == "gemini":
                    event = dict(session_id="s", tool_name="read_file", tool_input={"file_path": path},
                                 tool_response={"llmContent": [{"text": text}]})
                else:
                    numbered = "\n".join(f"{i}. {v}" for i, v in enumerate(text.splitlines(), 1))
                    event = dict(sessionId="s", toolName="view", toolArgs=json.dumps({"path": path}),
                                 toolResult={"resultType": "success", "textResultForLlm": numbered})
                self.assertEqual(self.run_hook(host, 0, event), {})
                duplicate = self.run_hook(host, 0, event)
                if host == "claude":
                    file = duplicate["hookSpecificOutput"]["updatedToolOutput"]["file"]
                    self.assertEqual(file["numLines"], 1)
                    self.assertEqual(file["filePath"], path)
                    self.assertIn("already returned", file["content"])
                elif host == "gemini":
                    self.assertEqual(duplicate["decision"], "deny")
                    self.assertIn("already returned", duplicate["reason"])
                else:
                    self.assertIn("already returned", duplicate["modifiedResult"]["textResultForLlm"])
                    self.assertEqual(duplicate["modifiedResult"]["resultType"], "success")
                for boundary in (1, 2):
                    self.run_hook(host, boundary, event)
                    self.assertEqual(self.run_hook(host, 0, event), {})
                if host == "claude":
                    mirrored = str(sync.ROOT / ".claude/skills/deep-research-council/SKILL.md")
                    reply = {"type": "text", "file": {**event["tool_response"]["file"], "filePath": mirrored}}
                    mirror = {**event, "tool_input": {"file_path": mirrored}, "tool_response": reply}
                    self.assertIn("hookSpecificOutput", self.run_hook(host, 0, mirror))
                    reply["file"]["content"] += "changed"
                    self.assertEqual(self.run_hook(host, 0, mirror), {})
                args = {"file_path": path, "limit": 2}
                self.assertEqual(self.run_hook(host, 0, dict(event, tool_input=args, toolArgs=args)), {})
                failed = dict(event, tool_response={"error": "failed"}, toolResult={"resultType": "failure"})
                self.assertEqual(self.run_hook(host, 0, failed), {})

    def test_opencode_v2_registration(self):
        root = self.base / "opencode"
        script = """
            import assert from 'node:assert/strict';
            import fs from 'node:fs';
            import guard from './.opencode/plugins/council-cache/index.mjs';
            const hooks = {};
            const register = async (name, fn) => { hooks[name] = fn; };
            await guard.setup({tool:{hook:register},session:{hook:register}});
            const path = '.opencode/skills/deep-research-council/SKILL.md';
            const content = fs.readFileSync(path,'utf8');
            const fresh = () => ({sessionID:'s',agent:'a',status:'completed',tool:'bash',
                input:{command:'cat '+path},result:{content}});
            await hooks.prompt({sessionID:'s'});
            const first=fresh(); await hooks['execute.after'](first); assert.equal(first.result.content,content);
            const repeat=fresh(); await hooks['execute.after'](repeat); assert.match(repeat.result.content,/already returned/);
            await hooks.compaction({sessionID:'s'});
            const next=fresh(); await hooks['execute.after'](next); assert.equal(next.result.content,content);
        """
        subprocess.run(["node", "--input-type=module", "-e", script], cwd=root, check=True, timeout=20,
                       env=dict(os.environ, LOCALAPPDATA=str(self.base / "state")))
