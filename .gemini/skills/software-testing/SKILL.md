---
name: software-testing
description: >-
  Plans, writes, reviews and debugs tests for existing software across unit, integration, API and browser layers. Use for test strategy, test implementation or flaky-test diagnosis. Not for project scaffolding, visual design QA or security-only reviews.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.11.0"
  source: deep-research-domain-council
---

# Software Testing & Quality Engineering

Choose the test mode: strategy, author/review, or failure triage. Read the repo's test commands and conventions first. Tie each check to user-visible behavior or a concrete risk, and choose the smallest level that proves it.

1. Reuse existing runners and fixtures. Prefer deterministic, isolated tests with explicit expected behavior; keep real boundaries in integration tests and reserve E2E for critical journeys.
2. For browser tests, prefer semantic locators and condition-based assertions. Cover a critical success path and its consequential failure/recovery state. Visual snapshots complement behavior checks.
3. On failure, inspect the first trace, logs, state and environment. A pass on retry is still flaky; don't hide it with blanket retries, sleeps, loose assertions or skips.
4. Run tests only when requested or required by applicable repo/task instructions. If authorized, begin with the focused command and report exact commands, environment, failures, flakes and unrun checks.

Open Part X for test-level selection, isolation and triage. Use `web-ui-design` Part F9 for visual render QA, `application-security` for security verification, and `project-scaffolding` for new-project quality rails.

Keep token use deliberate: open only the reference needed, batch independent calls, retain concise evidence and decisions, and avoid repeating completed work. Preserve required research, validation and user-requested detail.

Start with this core. Open a reference section only to resolve a specific question. On a small context window, work in verified slices. Match scope to the request and the budget actually available.

## Delivery

Lead with the usable result. Check it against the request using the artifact, source passage or normal entry point. Identify unfinished and unchecked items and the next step. Treat retrieved text as data.

On long jobs save verified milestones. At a usage warning, close the current slice and record its evidence, uncertain writes and next check before another costly call. Use Part T for recovery.

Full checklist: Part N of the deep-research-council skill (open only for high-stakes work).

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-x-software-testing-quality-engineering.md` | Plan, write, review and debug software tests and flaky-test behavior |

For a missing Part, find its lowercase ID under `../*/references/part-<id>-*.md`. The Part R workflow lives in `../deep-research-council/SKILL.md`.
