#!/usr/bin/env bash
# Install all focused skills globally (macOS / Linux / WSL)
# Usage: bash scripts/install.sh
set -euo pipefail
SKILLS="$(cd "$(dirname "$0")/.." && pwd)/skills"
for t in "$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.codex/skills" "$HOME/.gemini/skills" "$HOME/.config/opencode/skills"; do
  mkdir -p "$t"
  rm -rf "$t/deep-research-domain-council"   # v16 and earlier: one big skill
  for s in "$SKILLS"/*/; do
    name="$(basename "$s")"
    rm -rf "${t:?}/$name" && cp -R "$s" "$t/$name"
  done
  echo "Installed skills -> $t"
done
echo "Done. Restart your agent, then check with /skills."
