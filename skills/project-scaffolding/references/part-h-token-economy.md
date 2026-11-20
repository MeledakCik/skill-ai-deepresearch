# PART H — TOKEN ECONOMY (Stop Wasting Context and Money)

Many agents burn tokens on the same few mistakes: re-reading files, dumping huge tool outputs, rewriting whole files, verbose narration, and picking a bigger model or higher effort than the task needs. Cost is roughly:

$$\text{Cost} \approx \sum_{\text{turns}} \big(\text{input}_t \cdot p_{in} + \text{cached}_t \cdot p_{cache} + \text{output}_t \cdot p_{out}\big) + \text{tool fees}$$

Repeated large inputs can dominate an agent loop. Use the host's reported usage and billing categories when available. In the formula above, input means uncached input.

## H1. The Ten Biggest Token Leaks (and the Fix)

| # | Leak | Fix |
|:---|:---|:---|
| 1 | Reading whole large files to find one function | `grep -n` / symbol search first, then read only the line range |
| 2 | Re-reading a file you just edited to "verify" | Trust the edit tool's success; re-read only if a later step depends on exact content |
| 3 | Dumping full command output | Use the runner's quiet flags or retain its exit status and first actionable error when filtering logs. |
| 4 | Rewriting whole files for small changes | Diff/patch edits; diff ≤ ~20% of file |
| 5 | Narrating every step ("Now I will…", "Great, that worked!") | Silent tool calls; report only results and decisions |
| 6 | Restating the user's request and the plan at length | One-line plan; the work is the answer |
| 7 | Serial tool calls that could be batched | Parallel independent calls in one turn |
| 8 | Using the biggest model / max effort for trivial steps | Route by task (D2); small model for search, summarization, formatting |
| 9 | Sub-agents returning full transcripts | Sub-agents return structured summaries (≤ 300-500 tokens) with file paths and line refs |
| 10 | Pasting web pages / PDFs into context | Extract only the needed passages; store notes, not pages (A4) |

## H2. Context Hygiene

- **Budget the window:** keep working context well below the model's limit; quality often degrades long before the hard limit.
- **Stable prefix first:** system prompt, skill text, project rules, then volatile content. Stable prefixes are what prompt caching can reuse.
- **Compact proactively:** at natural milestones, summarize decisions, file paths, open TODOs; drop raw logs.
- **Externalize memory:** write `notes.md` / `claim_ledger.md` / `TODO.md` to disk and read back the part you need, instead of carrying everything in context.
- **Lazy skill loading** (C1): frontmatter idle, body on demand, references only when needed. Keep `SKILL.md` lean and move rarely used detail to `references/*.md`.
- **Limit MCP/tool surface:** every enabled tool's schema costs tokens on every turn. Disable unused servers.

## H3. Prompt Caching (Provider Features, ⚠ verify current pricing)

- Anthropic: explicit cache breakpoints (`cache_control`); cached reads are billed at a small fraction of normal input price, cache writes at a premium; short TTL by default with a longer option.
- OpenAI: automatic caching of repeated prompt prefixes above a minimum length; cached input billed at a discount.
- Google Gemini: implicit and explicit context caching with storage cost.
- **Rule:** put long, unchanging material (skill, docs, codebase map) at the start and never edit it mid-session; small edits early in the prompt invalidate everything after them.

## H4. Output Discipline

- Answer length proportional to question difficulty.
- Code: return only changed hunks or the new file, never both; no commented-out alternatives.
- Reports: tables for comparisons; no repeated summaries at start and end.
- Structured outputs (JSON schema) for machine-consumed results; avoids retries from malformed output.
- Set explicit max output where the harness allows it.

## H5. Reasoning Budget

- Thinking tokens are output tokens (usually the most expensive kind). Use low/medium effort for mechanical work, high only for genuinely hard reasoning (D2).
- Do the hard thinking once, write the decision down, then execute cheaply. Do not re-derive the same plan each turn.
- For research, more searches usually beat more thinking when facts are missing.

## H6. Harness-Specific Tips (⚠ features change; verify in current docs)

| Harness | Tips |
|:---|:---|
| Claude Code | Keep `CLAUDE.md` short and factual; use `/compact` at milestones and `/clear` between unrelated tasks; prefer sub-agents for broad searches so raw results stay out of the main context; disable unused MCP servers |
| OpenCode | Per-agent tool permissions; disable MCP globally and enable per agent (C1); short `AGENTS.md`; Plan agent read-only for exploration |
| Cursor / Windsurf / Cline / Roo | Scope context with explicit file mentions instead of whole-repo; keep rules files small; prefer apply-diff edit modes; avoid auto-including huge folders (`node_modules`, `dist`, lockfiles) via ignore files |
| OpenAI Codex / Responses API | Reuse `previous_response_id` or cached prefixes instead of resending history; pick reasoning effort per call; use cheaper `-mini` variants for retrieval and summarization |
| Any API loop | Truncate tool results server-side; cap retries; log tokens per turn to find the expensive step |

## H7. Token Budget Table (Guideline per Task)

| Task | Target total tokens | Notes |
|:---|:---|:---|
| Simple Q&A | < 2K | No tools or one search |
| Bug fix in known file | 5-20K | grep → read range → patch → targeted test |
| Feature across 3-5 files | 20-80K | Plan once, batch reads, diffs only |
| S-tier research report | 30-100K | Notes on disk; pages never pasted whole |
| D/X-tier research | 100K-1M+ | Sub-agents with compact summaries; lead holds only the ledger |

## H8. Token Waste Audit (Run After Expensive Sessions)

1. Which turn had the largest input? What made it large?
2. How many file reads were repeats?
3. How many tool outputs exceeded 2K tokens? Could they have been filtered?
4. Was effort/model higher than the task required?
5. Was any output thrown away (rewritten drafts, failed full-file rewrites)?
Write the answers into project notes so the next session avoids them.


## H9. Model-Class Profiles (Pro vs Standard vs Small)

The same skill must stay cheap on a frontier model and still work on a small one. Detect the class from the model name or the harness; when unsure, use **Standard**.

| Class | Examples (⚠ names change) | Load | Starting scope | Effort / thinking | Output |
|:---|:---|:---|:---|:---|:---|
| **Pro / frontier** (largest tier) | e.g. Claude Opus 5.5 / Fable 5.2, GPT-6 Astra, Gemini 4 Argon (see D4) | Core + the 1-2 references the task needs | Deep / Exhaustive (sub-agents allowed) | Default medium; high/xhigh only for hard reasoning; max only per Part P/D rules | As long as the task needs, no padding |
| **Standard** (mid tier) | e.g. Claude Sonnet 5.5, Gemini Flash-class, GPT mini-class, DeepSeek V4 | Core + at most 1 reference; prefer reading a single section of it | Standard | Low-medium; spend on searching, not on long thinking | Compact: BLUF + findings table + sources |
| **Small / free / local** (smallest tier) | e.g. Claude Haiku 5.5, Gemini 4 Hydrogen, small open models | Lite prompt only (`adapters/*/INSTRUCTIONS-lite.md` or the core's short rules); never load references in full | Quick (1-5 sources) | Lowest; no sub-agents | Short; one table max; say when a bigger model would do better |

**Rules for every class**
1. Load references lazily: read the table of contents in the core, open one reference, and within it read only the needed section (grep for the heading) when the harness allows partial reads.
2. Never paste whole web pages or files; extract the needed lines (Part H1).
3. Re-use earlier conclusions instead of re-deriving them each turn.
4. Escalate class only when the cheaper one fails a check (Part N), not pre-emptively.
5. For a deep question on a constrained host, work through pivotal claims one at a time. Carry forward checked evidence and identify what remains open if the available budget runs out.

## H10. Compacting research without losing the evidence

Keep an origin index (source ID, URL, date, exact locator, shared dataset or announcement) and one short row per claim (finding, population/period/units, supporting IDs, counterevidence, confidence reason, open question). Reuse both between turns. Search by the missing field before opening another source. An extra link to an indexed origin can supply a missing detail even though it adds no independent confirmation.

After an expensive pass, compare input/output tokens on the same task and model if counts are available. Otherwise record bytes retained or calls repeated and name the proxy. In both runs, verify that a reader can still locate the pivotal measurement, distinguish duplicated origins and explain the strongest contrary evidence. Restore any lost locator or caveat before accepting a smaller prompt.
