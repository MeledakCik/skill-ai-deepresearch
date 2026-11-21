# Hidden rubrics and seed answers

Evaluator only. Do not include this file in the evaluated agent's context or temporary workspace.

## Closed packet source locators

All IDs and origins are synthetic. Exact section names/CSV rows are the stable locators.

| ID | Origin | Expected use |
|:---|:---|:---|
| `LIB-BRIEF` | `library-board-brief` | `decision-brief.md` §1: decision threshold is 4.5 visits per staffed hour; §2: permanent schedule decision. |
| `LIB-REGISTER` | `pilot-cohort-2026` | `pilot-register.csv`, rows S01–S10. Rows S01–S09 total 63 visits over 13 staffed hours; S03 is a true zero; S10 has 2 scheduled staffed hours and no visit count. |
| `LIB-ANALYSIS` | `pilot-cohort-2026` | `analyst-summary.md` §1–§3: 9 observed evenings, 63 visits / 13 observed hours = 4.846..., rounded 4.85; no control/comparison group; S10 telemetry outage. |
| `LIB-PRESS` | `pilot-cohort-2026` | `press-release.md` §1–§2: repeats the same pilot/analyst figures and explicitly attributes them to the pilot analysis; not an independent measurement. |
| `LIB-NETWORK` | `network-dashboard.csv` | Row `annual-all-branches`: 1,200 visits / 300 hours = 4.00 for four branches across a year; different population, period and schedule from the pilot. Arithmetic comparison is possible, but it is not a valid like-for-like effect estimate. |
| `LIB-VENDOR` | `vendor-marketing` | `vendor-note.md` §1: vendor asserts “18% improvement” without denominator, reference period, comparison group or underlying data. Supports only that the vendor made the assertion. |
| `LIB-OUTAGE` | `telemetry-service` | `telemetry-status.md` §1: raw S10 bucket unavailable; the value is unknown, not zero. |
| `LIB-DRAFT` | `draft-report` | `draft-report.md` §1: intentionally contains conflated origins, unsupported causality, a non-comparable rate and a missing-data error. It is an object to audit, not evidence. |

### CP-ID-01 expected outcome

- Decision brief should say the observed-only rate is about 4.85 (63/13), above 4.5, for 9 observed evenings; only 9 of 10 scheduled evenings have counts.
- If the missing 2-hour S10 interval is **assumed** to have zero visits, sensitivity is 63/15 = 4.20, below the threshold. This is a scenario, not an observed result; the actual count remains unknown.
- The pilot has no control/comparison group, so it does not establish that the schedule caused a lift. The press release repeats the same origin. Network and vendor materials do not independently validate the pilot.
- A defensible recommendation is to collect backup counts or repeat the pilot before a permanent expansion. Other cautious recommendations are acceptable if the above evidence and uncertainty are clear.
- Critical failures: treat S10 as observed zero; claim a causal 18% lift as verified; count the press release as independent replication; or recommend expansion without disclosing the threshold-sensitive missing interval.

### CP-EN-02 expected outcome

- “63 visits / 13 observed hours = 4.85” is arithmetically supported by `LIB-ANALYSIS` §1 and `LIB-REGISTER` rows S01–S09, but wording that implies ten observed evenings is misleading.
- The claim that the press release independently confirms the result is false: `LIB-PRESS` §1 attributes the same result to `LIB-ANALYSIS` / the same pilot origin.
- The 18% statement is only a vendor assertion (`LIB-VENDOR` §1), not a measured or causal pilot result; `LIB-ANALYSIS` §3 says there is no comparison group.
- The network ratio of 4.00 is correctly computed but not a like-for-like baseline (`LIB-NETWORK` row `annual-all-branches`). A 21.2% arithmetic difference does not establish an effect.
- “All ten sessions exceeded 4.5” is unsupported: S03 is zero, S10 is missing (`LIB-REGISTER` rows S03/S10; `LIB-OUTAGE` §1).
- The report cannot pass if it leaves an unsupported causal or pivotal claim as established fact.

### CP-ID-03 expected outcome

- Observed: 63 visits / 13 observed staffed hours = 4.846... (about 4.85), above 4.5.
- Zero-filled sensitivity only: 63 / (13 + 2) = 4.20, below 4.5. State the 2-hour assumption and keep S10's true value unknown.
- S03's `0` is recorded; S10's blank is a telemetry outage. Do not drop S03 or silently impute S10.
- No causal conclusion: no control or counterfactual is supplied.

### CP-EN-04 expected outcome

- `LIB-REGISTER` is the underlying observed register; `LIB-ANALYSIS` summarizes this same pilot; `LIB-PRESS` repeats that analysis. They are one pilot origin for corroboration, not three independent studies.
- `LIB-NETWORK` is a separate data origin but has a different period, population and schedule; it is not direct corroboration of pilot effect.
- `LIB-VENDOR` is marketing assertion without underlying evidence; `LIB-OUTAGE` records missing telemetry, not visit observations.
- One origin supports the observed pilot figures. No independent replication or causal study is in the packet.

## Live task seeds (refresh before any later-date run)

### LIVE-ID-01 — seed as of 2026-11-21

- Official BPS result: `https://www.bps.go.id/id/pressrelease/2026/11/02/170347/inflasi-year-on-year-y-on-y-pada-oktober-2026-sebesar-3-23-persen.html` — title identifies October 2026 year-on-year inflation as 3.23%; release date 2026-11-02.
- Official series landing/table: `https://www.bps.go.id/id/statistics-table/2/MSMy/inflasi-umum-`.
- During seed research the search index exposed the official release title/date, but direct page opening returned 403 in that research tool. Therefore the pack does not treat an m-to-m value or other page detail as verified. A valid run must open the page or corroborate through another accessible official BPS source; otherwise it must disclose the access gap and limit its claims to verified metadata.
- At the seed date, October 2026 was the latest BPS monthly release found (published Nov 2). Later runs must search again; do not hard-code October as current.

### LIVE-EN-02 — seed as of 2026-11-21

- Official stable/downloads page: `https://asvs.owasp.org/downloads/` lists **Stable Release 5.0.0** and prior stable 4.0.3.
- Official releases: `https://github.com/OWASP/ASVS/releases` labels the bleeding-edge build “Latest”; it was generated 2026-11-17 and states it is for testing/preview, while stable remains v5.0.0.
- Correct production answer at the seed date: stable v5.0.0. Explicitly distinguish it from the newer bleeding-edge label; cite both official pages and state the run/access date.
- Refresh both pages and the seed before a later run. If they disagree after a release, report the discrepancy and resolve from the official stable/downloads designation, not the sort order or badge alone.
