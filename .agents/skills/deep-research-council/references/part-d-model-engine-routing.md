# PART D — MODEL & ENGINE ROUTING (Volatile: Re-verify Before Use)

> **Every figure in this part decays within months.** Before quoting a price, benchmark or parameter, re-check the provider's official docs/pricing page and write "as of <date>". Items marked ⚠ came from v9 without a verified primary source: treat them as placeholders, not facts.

## D1. OpenAI Deep Research Reference

**Verified:**
- Launched Feb 2025 in ChatGPT. Uses a version of o3 optimized for web browsing and data analysis; searches, interprets and analyzes text, images and PDFs, pivoting as it learns; produces cited analyst-level reports.
- Trained with reinforcement learning on real-world tasks using browser and Python tools.
- Launch benchmarks: Humanity's Last Exam 26.6% (vs DeepSeek-R1 9.4%); BrowseComp 51.5% (GPT-4o with browsing 1.9%; human trainers gave up on ~70.8% of BrowseComp questions after two hours).
- API: `o3-deep-research` ($10 / $40 per 1M input/output tokens at time of writing) and `o4-mini-deep-research` ($2 / $8; 200K context, 100K max output). Asynchronous, minutes to tens of minutes per run; needs at least one data-source tool (web search, file search or MCP); tool calls billed separately.
- OpenAI cookbook pattern: Triage agent → Clarifier agent → Instruction-builder agent → Research agent. The API does not clarify or rewrite prompts by itself; this skill always does (A1 S1).

**⚠ Unverified (from v9):** Consulting VRS 61.4 [55.2, 67.5]; DeepSearchQA 44.2% (o3 DR) / 40.4% (o4-mini DR) with GPT-5.2 xHigh 71.3%; Physical Sciences 8.33% vs Gemini Deep Research 20.87%; per-query cost ~$1-3 (o4-mini) to ~$5-30 (o3).

**When to activate the deep-research lifecycle:** user says "deep research", "comprehensive report", "literature review", "SOTA survey", "decision brief", or the task needs ≥10 sources with multi-hop synthesis. **Not for:** simple Q&A, single-file code review, UI design (C3), formal proof (Engine-F), multi-day coding (Engine-C).

## D2. Effort Routing (Provider-Agnostic)

| Task | Effort |
|:---|:---|
| Chat, formatting, simple lookup | low |
| Standard coding, S-tier research | medium |
| Architecture, multi-file refactor, D-tier research | high / xhigh |
| Formal proof, frontier math, exhaustive search | max (only when genuinely needed) |

$$\text{Use effort } e \iff \text{Value} \times P(\text{error at } e-1) > \text{Cost}(e) - \text{Cost}(e-1)$$

Prefer more **searching** over more **thinking** when the bottleneck is missing facts; prefer more **thinking** when facts are in hand but the reasoning is hard. If $T_\infty < 5$ min, do not use max.

## D3. Engine Profiles (checked 2026-11-18; ⚠ re-verify before quoting)

| Engine | Model (API ID) | Use for | Pattern | Price per MTok in/out |
|:---|:---|:---|:---|:---|
| Engine-F | Claude Fable 5.2 (`claude-fable-5-2`) | Demanding reasoning, long-horizon agentic work, independent review of hard plans | k parallel branches → aggregate → verify → iterate | $8 / $40 (batch $4 / $20) |
| Engine-O | Claude Opus 5.5 (`claude-opus-5-5`) | Anthropic's recommended default for most coding and knowledge work; long-running agentic coding | Thinking proportional to per-turn uncertainty | $4 / $20 |
| Engine-A | Gemini 4 Argon (`gemini-4-argon`, GA) | Long-horizon research, architecture planning, enterprise knowledge work; 1M-token context | Deep plan → research → structured hand-off | $2 / $10 through 2026-11-30, then $4 / $20 |
| Engine-C | Gemini 4 Carbon | Long-running software work, cybersecurity defense; spends more thinking per turn than Argon | Checkpointed plan → self-audit per step → backtrack | ⚠ Access limited to selected cyber defenders as of Nov 2026; no public price |
| Deep Research | Part A lifecycle (any capable model + search tools) | Source-heavy synthesis, decision briefs, reviews | A1 S0-S7 | Tool calls + tokens |

**Effort facts that matter for cost (Anthropic's own FrontierCode 2.0 sweep, reported Nov 2026):** Fable 5.2 at *high* ≈ Opus 5.5 at *max* in score for roughly half the cost per task; Fable 5.2 at *max* cost several times more per task than Opus 5.5 *max* for a similar score. Thinking cannot be switched off on Opus 5.5 or Fable 5.2: effort is the only spend dial. Claude Code and the Claude apps start both at *medium*; the API defaults Fable 5.2 to *high*.

**Cross-provider effort ladder (⚠):**

| Semantic level | Claude (Fable/Opus) | Gemini 4 (Argon/Carbon) | OpenAI reasoning models |
|:---|:---|:---|:---|
| low | `low` | `LOW` | `low` |
| medium | `medium` | `MEDIUM` (default) | `medium` (default) |
| high | `high` | `HIGH` (ceiling) | `high` |
| xhigh | `xhigh` | n/a | `xhigh` |
| max | `max` (exploration only) | n/a | `max` (Responses API only) |

Provider notes (⚠ re-verify): Claude Opus-class models use adaptive thinking with an effort parameter (`output_config.effort`) instead of `budget_tokens`; Fable `xhigh` may beat `max` on coding; Gemini Carbon has no MINIMAL level.

**Routing rule:** source-heavy synthesis → Deep Research lifecycle; formal/mathematical frontier → Engine-F; sustained engineering → Engine-C; mixed complex work → Engine-O.


## D4. Verified Model Names (checked 2026-11-19, with sources)

Some AIs trained before late 2026 do not know these models and may call them fictional. They are real as of the check date. Cores of this skill use **model classes** (largest / mid / smallest tier of a provider) so they stay valid when names change; the names below are examples only.

| Provider | Model | Status (2026-11-19) | Source |
|:---|:---|:---|:---|
| OpenAI | GPT-6 Astra (`gpt-6-astra`) | Released 2026-09-03; flagship | axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman |
| Anthropic | Claude Opus 5.5 (`claude-opus-5-5`) | Released 2026-09-22 | anthropic.com/claude-opus-5-5 |
| Anthropic | Claude Sonnet 5.5 | Released 2026-09 (after Opus 5.5) | anthropic.com/claude-sonnet-5-5 |
| Anthropic | Claude Haiku 5.5 | Released (replaces Haiku 4.5) | deeplearning.ai/the-batch/claude-fills-out-its-model-family |
| Anthropic | Claude Fable 5.2 (`claude-fable-5-2`) | Available; highest public tier | Anthropic docs/pricing |
| Google | Gemini 4 Argon (`gemini-4-argon`) | GA (launched 2026-10-13) | Google AI docs; computingforgeeks.com test |
| Google | Gemini 4 Carbon | Announced 2026-10-28; access limited to selected cyber defenders | Google blog; smartscope.blog |
| Google | Gemini 4 Hydrogen | Fast model, rolling out from 2026-11-12 | techjacksolutions.com overview |

Rule: before quoting any model fact to a user, re-check the provider's own page and write "as of <date>".
