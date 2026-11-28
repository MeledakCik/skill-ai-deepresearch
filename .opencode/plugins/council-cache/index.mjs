import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../../../", import.meta.url));
const script = fileURLToPath(new URL("../../../scripts/host_cache_guard.py", import.meta.url));

function guard(phase, payload) {
  const input = JSON.stringify(payload);
  if (Buffer.byteLength(input) > 2 * 1024 * 1024) return Promise.resolve({});
  return new Promise((resolve) => {
    const proc = spawn(process.platform === "win32" ? "python" : "python3",
      ["-I", "-S", script, "opencode", phase], { cwd: root, stdio: ["pipe", "pipe", "ignore"], timeout: 5000, windowsHide: true });
    let result = "";
    proc.stdout.setEncoding("utf8").on("data", (chunk) => { result += chunk; });
    proc.on("error", () => resolve({}));
    proc.stdin.on("error", () => resolve({}));
    proc.on("close", (code) => {
      try { resolve(code === 0 ? JSON.parse(result) : {}); }
      catch { resolve({}); }
    });
    proc.stdin.end(input);
  });
}

export default {
  id: "council-cache",
  async setup(ctx) {
    const reset = (event) => guard("reset", { session_id: event.sessionID }).then(() => {});
    await ctx.session.hook("prompt", reset);
    await ctx.session.hook("compaction", reset);
    await ctx.tool.hook("execute.after", async (event) => {
      if (event.status !== "completed" || event.codemode || !["read", "bash"].includes(event.tool)) return;
      const result = event.result;
      if (typeof result?.content !== "string" || result.content.length < 1024 || result.metadata?.truncated) return;
      if (result.output !== undefined && result.output !== result.content) return;
      const reply = await guard("read", { session_id: event.sessionID, agent_id: event.agent,
        cwd: root, tool_name: event.tool, tool_input: event.input, tool_response: { content: result.content } });
      if (typeof reply.content === "string") {
        event.result = { ...result, content: reply.content };
        if (result.output !== undefined) event.result.output = reply.content;
      }
    });
  },
};
