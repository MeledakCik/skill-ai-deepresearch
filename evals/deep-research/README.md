# Deep Research Regression Pack

Version: `1.3.0` · Seed date: `2026-11-21` · Mode: manual evaluation; no scores or pass rates are claimed.

This maintainer fixture turns Part L5 into a repeatable, low-cost check. Its 10 tasks comprise eight synthetic closed-packet cases and two dated live-search prompts. It separates evidence retrieval from report quality and keeps answer keys away from the evaluated agent. Closed cases cover official-source fallback, unlike measures, checkpoint continuation and a protocol-led review audit.

## Run a task

1. Pick task IDs from `manifest.json`; order a small, representative first slice before deciding whether to continue. Use a fresh conversation and a clean temporary workspace. For a closed task, copy only the named corpus and its prompt into that workspace. For a live task, give the prompt and web access, but do not provide `rubrics.md`.
2. Before the first call, set practical caps for tokens or spend (when exposed), wall time and tool calls, plus a reserve for scoring and delivery. Treat each task's cost as unknown until measured. If quota/reset information is not exposed, record it as unknown; do not guess.
3. Record the task-pack, skill, model, tools/settings, run date, declared budget and task order in a copy of `run-template.json`. For live or reproducibility runs, preserve materially distinct queries and filters in `search_log`, with tool/index, date, language, exposed result count, opened source IDs and query purpose/outcome. Leave it empty when no search was run. Do not put private user files, credentials or unrelated raw transcripts into the run record.
4. Save the unedited answer, source locators, actual usage and failure/recovery notes immediately after each task. Score it against `rubrics.md` only after the answer is complete. For a blind review, hide the skill version and shuffle the versions before a human reviewer sees the output.
5. Stop before the next expensive call when a cap is reached, the host reports a quota/rate limit, or the remaining budget cannot cover review and delivery. Save a checkpoint with completed and remaining task IDs, verified outcomes, unknowns, stop reason and exact next action. Resume unfinished tasks only; completed tasks are rerun only for a predeclared replicate. A changed model, tool, effort, prompt or packet is a separate condition.
6. Use run statuses `planned`, `in_progress`, `partial` or `complete`; task statuses are `not_started`, `in_progress`, `completed` or `blocked`. Mark the run `partial` when interrupted or voluntarily stopped. Report `completed / planned`, score completed tasks only, and do not call it a full-suite pass rate. Keep retrieval, citation support, reasoning, coverage and cost separate. An unsupported pivotal claim or invented source is a critical failure regardless of prose quality. If a source has changed or cannot be opened, refresh the live seed or record the access limit; do not force the old answer.
7. Compare versions only with the same prompt, evidence packet, model, tools and effort. If any of those change, mark the run as a new condition. With this small set, report observed task outcomes and reviewer disagreement; do not claim statistical significance.

## Tracks and scoring

- **Closed packet:** `corpora/library-evening-pilot/` is wholly fictional and self-contained. Do not browse outside it for these tasks. `source-map.md` explains source IDs and shared origins; individual files provide stable section and row locators.
- **Live search:** prompts in `prompts.md` are time-sensitive. `rubrics.md` records a seed snapshot as of `2026-11-21`; before later runs, recheck the official source pages and amend the seed date/expected outcome if needed. A search index snippet is not equivalent to reading the cited source. Disclose a blocked page and seek an accessible official corroboration where possible.

Use explicit denominators:

- Closed required-evidence retrieval = eligible prelisted evidence items correctly found and used / all prelisted eligible items.
- Citation support = checked claim–citation pairs whose exact passage supports the claim / all checked pairs.
- Critical-claim coverage = preidentified critical claims with adequate source locators / all preidentified critical claims.
- Live discovery is a task-level decisive-source hit rate, not recall over the unknown total contents of the web.
- Cost is token/search/tool/time usage per task that clears its critical gates, when the host exposes those values. Mark unavailable values as unknown; do not estimate them.
- Optional token-efficiency diagnostic = measured input + output tokens / predeclared pivotal claims that passed factual and citation checks. Report the accepted-claim count beside the ratio. Do not compute it when the count is zero, do not use it as a quality score, and do not call a run more efficient if it failed a critical gate.
- Compare that diagnostic only across matched prompt, packet, model, tools and settings. Keep costs per task visible; a pooled ratio across unlike tasks can conceal an expensive or weak case.

The answer key is intentionally separate from the prompts. Do not expose `rubrics.md` to the evaluated agent. `manifest.json` is an operator index; share only the selected prompt and allowed packet with the agent. This pack is a maintainer aid, not a claim that Codex or the skill has already passed it.

## Files

- `manifest.json`: task IDs, tracks and prompt/packet paths.
- `prompts.md`: copy-ready prompts only.
- `rubrics.md`: hidden acceptance criteria and live seed observations.
- `run-template.json`: one record per run, with budget, status and resumable task IDs; leave scores null until a human or defined evaluator scores them.
- `runs/`: optional durable run records and answer artifacts; preserve partial runs with their original pack and skill versions so they can be resumed without repeating completed tasks.
- `corpora/library-evening-pilot/`: synthetic source packet and deliberately flawed draft for closed-packet evaluation.
- `corpora/source-access-recovery/`: synthetic official-source access failure with an official final data alternative.
- `corpora/primary-source-conflict/`: synthetic official measures with different populations, constructs and uncertainty.
- `corpora/research-resume/`: a verified checkpoint plus a later source that resolves the pending missing-data question.
- `corpora/systematic-review-audit/`: synthetic search export, duplicate, screening decisions, two eligible studies and one unavailable full text.
