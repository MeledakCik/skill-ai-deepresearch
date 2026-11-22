# Manual score — v17.27.0, suite 1.15.0

- **Execution:** 19/19 selected tasks completed. The run is complete; the input ceiling is exceeded.
- **Critical gates:** 18/19 passed. Closed-packet tasks: 16/16 pass with zero web calls. Live tasks: LIVE-ID-01 and LIVE-EN-02 pass; LIVE-ID-03 fails citation fidelity.
- **LIVE-ID-01:** After BPS release/catalog opens failed, the answer leaves the requested month, release date and y-on-y figure unverified. It uses four web calls, exactly the Quick limit.
- **LIVE-EN-02:** Names stable OWASP ASVS 5.0.0 and distinguishes the newer Bleeding Edge build using opened official OWASP/GitHub pages.
- **LIVE-ID-03:** Adds separate iOS, macOS and web readiness rows, marks all team access unconfirmed, and explicitly sets production feasibility unresolved and schedule conditional. It still cites release, compatibility and distribution pages surfaced in results without individually opening them; critical gate fails.
- **Measured usage:** 1,758,072 input tokens (1,435,520 cached), 23,815 output tokens, and 15 web calls (4 search actions). The 1,700,000 input ceiling was checked between tasks and exceeded by **58,072** during the final task. Output and web-call ceilings were not exceeded. The run completed all tasks, so status remains `complete`; `budget_status` is `exceeded`.
- **Reliability and efficiency:** LIVE-ID-03 logged five stream retries and consumed 1,025,198 input tokens. Do not claim a token-efficiency gain; the suite includes a critical citation failure and this run is not a matched efficiency comparison.
- **Follow-up:** v17.28.0 clarifies that search/related-link appearances do not count as opened sources and requires a claim-to-source ledger. Its local unit/integrity checks pass; fresh live/full behavioral validation is deferred until usage resets because the primary five-hour window showed 91% used at 22 November 2026, 22:27 WIB.
