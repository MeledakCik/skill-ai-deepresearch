# Manual score — v17.26.0, suite 1.14.0

- **Execution:** 19/19 tasks completed in fresh Codex CLI sessions with the exact selected skill files embedded. Final run status is `complete`; no remaining task IDs.
- **Critical gates:** 17/19 passed. All 16 closed-packet tasks passed, used zero web calls, and retained the required evidence/decision constraints. LIVE-EN-02 passed. LIVE-ID-01 failed citation fidelity; LIVE-ID-03 failed per-target readiness/citation requirements.
- **LIVE-ID-01:** Exactly four web calls met the Quick ceiling. The BPS release returned an access error, then the answer cited an opened AllStats search page whose title/query concerned another subject. The CPI figure therefore remained unverified but was still presented as confirmed.
- **LIVE-ID-03:** The answer correctly marked target access unconfirmed and delayed scheduling until a POC. It did not provide separate team-access/status values per target or explicitly mark production feasibility unresolved; one pivotal stability URL was cited without being opened.
- **LIVE-EN-02:** Stable ASVS 5.0.0 and the newer Bleeding Edge label were distinguished using official sources.
- **Measured usage:** 1,141,499 input tokens (897,792 cached), 22,132 output tokens, 16 web-search calls and 4 search actions. These totals are for this complete run only; no efficiency gain is claimed because two critical gates failed and conditions differ from the earlier run.
- **Reliability:** The first resume attempt stopped at startup on an explicit limit; after the reported retry window, the same checkpoint resumed without rerunning completed tasks. The Windows AppX CLI resolver succeeded. Depup OAuth was expired, but live searches completed through the native web tool.
- **Conclusion:** Full execution, not a clean skill release pass. Tighten the opened-source allowlist and per-target migration readiness schema before the next release test.
