# PART J — FRONTIER LAB RESEARCH PLAYBOOKS (From Public Engineering Write-ups)

What the major labs have *publicly* described about how their deep-research systems work, turned into habits you can apply. Nothing here claims insider knowledge; each item traces to the lab's own publication (see Sources at the end of this part).

## J1. OpenAI — Deep Research (ChatGPT + API)

| Practice | How to apply |
|:---|:---|
| Reasoning model trained end-to-end with RL on browsing + Python tasks | Treat browsing as reasoning, not lookup: decide each next query from what the last page taught you |
| Pivot as information arrives | Explicit pivot checkpoints after every 5-10 sources (A1 S4.6) |
| Clarify → rewrite → research pipeline (cookbook: Triage → Clarifier → Instruction Builder → Research agent) | Use S0/S1 to settle scope before retrieval. Keep a short follow-up tied to its active decision. |
| Cited, analyst-grade report with a summary of reasoning | BLUF + per-RQ sections + methodology (A1 S6) |
| BrowseComp-style persistence (hard-to-find facts) | When a fact is hard to find, change *strategy*, not just wording: different source type, language, time period, entity name, or reverse-search from the answer's likely properties |

**BrowseComp lesson:** the hard part is *locating* an obscure fact, and verifying it is comparatively easy. So enumerate the constraints the answer must satisfy, search on the most selective constraint first, then verify the candidate against all the others.

## J2. Google — Gemini Deep Research

| Practice | How to apply |
|:---|:---|
| Prompt → personalized multi-point research plan the user can refine | Show the plan (A1 S2.6); invite edits when the user is present |
| Planner decides which sub-tasks run in parallel vs sequentially | Mark RQ dependencies; batch independent ones |
| Iterative reasoning: at each step, ground on everything gathered so far, then decide the next move | Re-read the claim ledger (not the raw pages) before each new search batch |
| Asynchronous task manager with shared planner/worker state for graceful recovery | Persist notes to disk (A4) so a failure does not mean restarting; resume from the ledger |
| Draws on web + user's own files/workspace when allowed | Vector C (local/internal) is a first-class source, not an afterthought |
| Synthesizes once "enough information has been gathered" | Saturation stopping rule (A2) |

## J3. Anthropic — Claude Research (Multi-Agent, Orchestrator-Worker)

| Practice | How to apply |
|:---|:---|
| Lead agent plans and delegates to parallel subagents with their own context windows; a separate citation pass at the end | A3 roles; Verifier/citation pass is mandatory for D/X |
| Multi-agent shines on breadth-first queries with independent directions | Use sub-agents only when RQs are truly independent; keep shared-state tasks (e.g., one codebase change) single-agent |
| Token usage explained most of the performance variance; multi-agent costs far more tokens than chat | Multi-agent is a spending decision: use it when task value justifies it (D2, H7) |
| Vague delegation ("research X") made subagents duplicate work or misread the task | Every delegation includes objective, output format, tools/sources to use, explicit boundaries, and what *not* to cover |
| Scale effort to complexity (simple fact = 1 agent, few calls; comparison = a few subagents; complex = many subagents with clearly divided scopes) | A1 S0 budget tiers; never spawn many agents for a simple question |
| Early failure modes: too many subagents, endless searching for nonexistent sources, agents distracting each other | Hard caps per tier; "source may not exist" stop rule after N failed strategies; sub-agents report only at the end |
| Start wide, then narrow | Broad short queries first, then targeted ones (A1 S3) |
| Evaluate with rubric-based LLM judging plus human review | Part L |

## J4. DeepSeek — Reasoning + Agentic Search

| Practice | How to apply |
|:---|:---|
| Reasoning integrated into tool use, trained on large-scale synthesized agentic tasks | Think *between* tool calls: after each result, state what changed and what to do next, in one or two lines |
| "Search while thinking" API mode: the model searches, opens pages, finds text in pages and checks facts over several reasoning steps | Verify inside the loop, not only at the end: check a key fact the moment you find it |
| Efficiency-first engineering (e.g., sparse attention for long context) | Prefer cheap, long-context passes for reading and expensive reasoning only for synthesis (H5) |

## J5. Cross-Lab Consensus (What Everyone Converged On)

1. **Plan first, visibly.** All four systems start by decomposing the question into a plan.
2. **Iterate: search → read → reason → decide the next step.** None of them does one big search and then writes.
3. **Parallelize independent threads; serialize dependent ones.**
4. **Persist state** so long tasks survive failures and context limits.
5. **Ground every claim in a source and run a dedicated citation check.**
6. **Spend tokens where they buy accuracy.** More search and more parallel exploration usually beat longer monologue reasoning when facts are missing. Open research (e.g., "search more, think less" studies) points the same way.
7. **Evaluate with rubrics, not vibes.**
