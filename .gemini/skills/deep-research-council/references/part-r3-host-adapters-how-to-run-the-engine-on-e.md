## R3. Host Adapters: How to Run the Engine on Each AI

| Host | Turn on / use | Engine notes |
|:---|:---|:---|
| **ChatGPT** | Deep research mode (or agent mode / web search for lighter runs); Custom GPT or Project with this skill | Deep research mode already browses for a long time: put the full brief from stage 1 in the first message so its own planner follows it. In normal chat with search, run lanes (R2) |
| **Gemini app / Gemini CLI** | Deep Research for long runs; Gem with this skill; Gemini CLI loads the skill natively | When Gemini shows its plan, edit it to match stage 2 (add the recency sweep, the mirror pass and primary-source requirements) before starting |
| **Claude (claude.ai, Claude Code)** | Research mode / web search; skill loads natively; sub-agents in Claude Code | Use real sub-agents for stage 4 and a separate verifier sub-agent for stage 10 |
| **Microsoft 365 Copilot** | Researcher agent | Internal-data sweep (stage 8) is its strength; add the brief's source standard so web sources are primary |
| **Perplexity** | Deep Research / Pro search; Space instructions with this skill | Strong at stage 3; push it through stages 5-10 by asking explicitly for primary sources, recency and contradictions |
| **Grok** | DeepSearch / DeeperSearch; custom instructions | Strong at stage 7; require T1/T2 confirmation for anything first seen on social media |
| **DeepSeek** | Search + DeepThink (thinking) | Matches stage 6 natively; ask for dates and URLs on every claim |
| **Codex / coding agents** | Web search tool if enabled; skill loads natively | Same engine; notes on disk (stage 11) |
| **API models** | Provider web-search tool or a search MCP | Without a search tool, say research is limited to model knowledge |
