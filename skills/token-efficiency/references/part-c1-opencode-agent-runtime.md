## C1. OpenCode / Agent Runtime (`opencode.ai/docs`)

- **3-level lazy discovery:**
  - L1 (~100 tokens idle): frontmatter only. `name` 1-64 lowercase alnum/hyphen, matching the directory; valid keys `name`, `description`, `license`, `compatibility`, `metadata`.
  - L2 (on demand): full `SKILL.md` from `.opencode/skills/<name>/`, `~/.config/opencode/skills/<name>/`, `.claude/skills/<name>/`, `.agents/skills/<name>/`.
  - L3 (need-to-know): `AGENTS.md` / `CLAUDE.md` / `opencode.json` load `@rules/...` only when required. Disable unused MCP servers globally (`my-mcp*: deny`), enable per agent.
- **Agents:** Plan (read-only), Build (surgical edits), Explore (parallel glob/grep/lsp).
- **Permissions:** `allow` (immediate), `ask` (destructive mutations), `deny` (blocked).
