# Deep Research Regression Pack

Version: `1.0.0`  
Seed date: `2026-11-21`  
Mode: manual evaluation; this pack contains no claimed scores or pass rates.

This maintainer fixture turns Part L5 into a repeatable, low-cost check. It separates evidence retrieval from report quality, includes synthetic multi-file evidence and dated live-search prompts, and keeps answer keys away from the evaluated agent.

## Run a task

1. Pick one task ID from `manifest.json`. Use a fresh conversation and a clean temporary workspace. For a closed task, copy only the named corpus and its prompt into that workspace. For a live task, give the prompt and web access, but do not provide `rubrics.md`.
2. Record the task-pack, skill, model, tools/settings and run date in a copy of `run-template.json`. Do not put private user files or secrets into this public fixture's run record.
3. Save the unedited answer and its source locators. Score it against `rubrics.md` only after the answer is complete. For a blind review, hide the skill version and shuffle the versions before a human reviewer sees the output.
4. Keep retrieval, citation support, reasoning, coverage and cost separate. An unsupported pivotal claim or invented source is a critical failure regardless of prose quality. If a source has changed or cannot be opened, refresh the live seed or record the access limit; do not force the old answer.
5. Compare versions only with the same prompt, evidence packet, model, tools and effort. If any of those change, mark the run as a new condition. With this small set, report observed task outcomes and reviewer disagreement; do not claim statistical significance.

## Tracks and scoring

- **Closed packet:** `corpora/library-evening-pilot/` is wholly fictional and self-contained. Do not browse outside it for these tasks. `source-map.md` explains source IDs and shared origins; individual files provide stable section and row locators.
- **Live search:** prompts in `prompts.md` are time-sensitive. `rubrics.md` records a seed snapshot as of `2026-11-21`; before later runs, recheck the official source pages and amend the seed date/expected outcome if needed. A search index snippet is not equivalent to reading the cited source. Disclose a blocked page and seek an accessible official corroboration where possible.

Use explicit denominators:

- Closed required-evidence retrieval = eligible prelisted evidence items correctly found and used / all prelisted eligible items.
- Citation support = checked claim–citation pairs whose exact passage supports the claim / all checked pairs.
- Critical-claim coverage = preidentified critical claims with adequate source locators / all preidentified critical claims.
- Live discovery is a task-level decisive-source hit rate, not recall over the unknown total contents of the web.
- Cost is token/search/tool/time usage per task that clears its critical gates, when the host exposes those values. Mark unavailable values as unknown; do not estimate them.

The key is intentionally separate from the prompts. Do not expose `rubrics.md` or `manifest.json` to the evaluated agent: they contain acceptance criteria and links/expected outcomes. This pack is a maintainer aid, not a claim that Codex or the skill has already passed it.

## Files

- `manifest.json`: task IDs, tracks and prompt/packet paths.
- `prompts.md`: copy-ready prompts only.
- `rubrics.md`: hidden acceptance criteria and live seed observations.
- `run-template.json`: one record per run; leave scores null until a human or defined evaluator scores them.
- `corpora/library-evening-pilot/`: synthetic source packet and deliberately flawed draft for closed-packet evaluation.
