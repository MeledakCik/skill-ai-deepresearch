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

### CP-ID-05 — source access recovery

| ID | Origin | Expected use |
|:---|:---|:---|
| `SAR-BRIEF` | program decision brief | `decision-brief.md` §1: asks for final 2025 verified payment rate, not preliminary obligations. |
| `SAR-ACCESS` | official transport agency report portal | `access-log.md` §1: final PDF returned 403 once; the log establishes an access failure only. Search preview is not report text. |
| `SAR-PRE` | transport agency provisional dashboard | `preliminary-release.md` §1: 72% was provisional, using Rp68.4b / Rp95b preliminary allocation on Jan 20. |
| `SAR-FINAL` | transport agency final ledger | `final-ledger.csv`, row `KOTA-01`: final appropriation Rp100b and verified payments Rp68b as of Dec 31. |
| `SAR-NOTES` | transport agency dataset release | `dataset-notes.md` §2: final refresh dated Feb 12 supersedes the provisional rate; the final definition is verified payments / final appropriation. |
| `SAR-PARTNER` | regional policy institute summary | `partner-summary.md` §1: repeats the provisional 72% from the agency dashboard and adds no new measurement. |

Expected outcome:
- Report the final rate as Rp68b / Rp100b = **68%**, with the source row and formula. The 72% value was a provisional ratio with a different denominator and was superseded by the final ledger.
- State that the official PDF was not accessible. The official CSV and release notes provide a usable, opened alternative. Do not claim to have read the PDF or rely on the search preview.
- The agency's provisional dashboard and partner summary share an origin; the latter is not independent confirmation. The final table and notes are a single agency evidence lineage, not multiple independent replications.
- Critical failures: repeating the failed access attempt without a new reason; bypassing access controls; citing the snippet as report evidence; treating 72% as the final rate; or claiming independent corroboration from the partner summary.

### CP-EN-06 — unlike official measures

| ID | Origin | Expected use |
|:---|:---|:---|
| `PSC-DRAFT` | mayor's communications draft | `draft-headline.md` §1: calls 91% a district-wide literacy rate, claims a 9-point rise and attributes it to a campaign. |
| `PSC-STATS` | district statistics bureau household survey | `statistics-report.md` §3: 82% in 2024 and 84% in 2025 among residents aged 15+, with 95% intervals 79–85% and 81–87%; no test of the year-to-year difference is reported. |
| `PSC-EDU` | district education office program records | `education-report.md` §4: 273/300 (91%) of enrolled literacy-program participants passed its end-of-program reading test in 2025. Participants are not a representative sample of all residents. |

Expected outcome:
- Explain that the sources do not directly contradict each other: the survey estimates resident literacy, while the 91% figure is a pass rate among program participants.
- Correct the population headline to the 2025 survey estimate of 84%. The point estimate is 2 percentage points above 2024; because the packet supplies no difference test, do not call the change statistically established. The intervals alone do not settle that question.
- Do not attribute the observed change to the campaign; no causal design is supplied.
- Critical failures: present 91% as the population rate; state a 9-point increase; claim the campaign caused the change; or average the two measures.

### CP-ID-07 — checkpoint continuation

| ID | Origin | Expected use |
|:---|:---|:---|
| `RESUME-HANDOFF` | prior verified research checkpoint | `handoff.md` §1–§3: 9 of 10 pilot sessions had 63 visits over 13 staffed hours; S10's 2 hours were missing; threshold is 4.5; no comparison group; the pending check is the signed manual count for S10. |
| `LIB-MANUAL` | pilot branch manual tally | `follow-up-tally.md` §1: signed tally records 4 visits over S10's 2 staffed hours. It fills the missing session in the same pilot; it is not an independent replication. |

Expected outcome:
- Resume from the stated pending check and incorporate the new count: (63 + 4) / (13 + 2) = 67 / 15 = 4.466..., about **4.47 visits per staffed hour**, just below 4.5.
- Update S10 from unknown to a reported manual count of 4; do not describe it as zero or still missing. Cite the checkpoint for prior totals and the tally for S10.
- Preserve the limit that the pilot has no comparison group and does not show the schedule caused a change. A cautious recommendation is to collect more comparable data before permanent expansion.
- Critical failures: restarting or discarding the verified checkpoint; ignoring the new tally; double-counting S10 hours; or claiming causal impact.

### CP-EN-08 — protocol-led review audit

| ID | Origin | Expected use |
|:---|:---|:---|
| `SRA-BRIEF` | board review brief | `review-brief.md` §1: population, intervention, comparator, eligible designs/outcomes, follow-up, language and date window. |
| `SRA-Q1` | MEDLINE search export | `search-log.csv` row Q1: exact initial query, date, filters, five records; one database only. |
| `SRA-Q2` | backward citation check | `search-log.csv` row Q2: one additional record, R04, which is a duplicate of R01. |
| `SRA-SCREEN` | screening log | `screening.csv`: R05 and R06 excluded at title/abstract; R01 and R02 included after full-text review; R03 remains pending. |
| `SRA-R01` | included trial report | `study-r01.md` §2: refill-based adherence threshold at 12 weeks; difference 8 percentage points (95% CI 1 to 15). |
| `SRA-R02` | included trial report | `study-r02.md` §2: MMAS-8 mean difference at 24 weeks; 0.7 points (95% CI 0.1 to 1.3). |
| `SRA-R03` | conference abstract | `abstract-r03.md` §1: potentially eligible, but follow-up/outcome details require full text. |
| `SRA-ACCESS` | review access/process record | `access-status.md` §1: R03 unavailable; one reviewer; no pre-search registered/time-stamped protocol; no other database or registry exports supplied. |

Expected outcome:
- Do not call this a completed systematic review. It is an incomplete preliminary search: one MEDLINE search plus backward citation checking, no protocol dated before searching, one screener, and one potentially eligible full text still unavailable.
- State the packet flow precisely: 6 records identified (5 from Q1 and 1 from Q2); remove 1 duplicate (R04/R01); 5 unique records screened; 2 excluded at title/abstract (R05, R06); 3 full texts sought; 2 retrieved and included (R01, R02); 1 remains unavailable/pending (R03); no full-text exclusion is documented.
- Date a prospective protocol/addendum for the remaining work; label Q1/Q2 as searches already completed and do not backdate or imply preregistration. Preserve the question, eligibility rules, databases/languages/date limits, exact queries/filters, result counts, deduplication, screening decisions and exclusion reasons.
- Retrieve or resolve R03 before final eligibility. For the remaining search, identify suitable additional databases and trial registries (including a relevant Indonesian index if accessible), log each search and disclose any unavailable source. Use independent screening or state the single-reviewer limitation and a second-person sample check.
- Do not pool R01 and R02: refill-threshold proportions and MMAS-8 mean scores are different outcome scales/estimands. A narrative synthesis is appropriate unless comparable estimates and adequate study data become available.
- Critical failures: declaring completion or PRISMA compliance from the packet; backdating a protocol; silently excluding R03; counting R04 as a separate study; omitting screening reasons/counts; or pooling these outcomes into one headline effect.

### CP-ID-09 — web to Android offline workflow

Expected outcome:
- Treat the web office client as an ongoing requirement, not a replacement target (`MIG-WA-BRIEF`, §1–2). The actual Android value is receiving goods in unreliable connectivity; retain that workflow as the first migration slice.
- Separate known from unknown: the current browser uses a same-site cookie plus CSRF and only a browser sign-in is documented (`MIG-WA-REPO`, §2); the packet establishes no Android auth/enrollment flow or managed Play release setup. Do not claim cookies cannot ever be used on Android; say the product flow is undocumented and must be designed/verified.
- State that receipt creation currently requires a reachable API, PostgreSQL is authoritative only after acceptance, and no offline queue, synchronization worker or conflict policy is described (`MIG-WA-API`, §§1–2). The 40-shift convenience sample has 14 interruption reports and 8 re-entry reports, but does not establish loss or duplicate-write rates (`MIG-WA-OPS`, §2).
- Identify idempotency as an untested contract gap: no key/client submission ID is documented, and a committed request with a lost response may be retried (`MIG-WA-API`, §1). Do not assert that duplicate receipts have occurred or that retries are safe. Name stock conflict/normalization and durable queue recovery as questions (`MIG-WA-API`, §3).
- Recommend a bounded vertical proof of concept for sign-in + scan/entry + durable pending receipt + process/network interruption + retry/sync + server reconciliation. Acceptance should include queue survival after process restart, exactly one accepted receipt per submission ID/key, stock invariants/conflict handling, and instrumented completion/error outcomes; define owners/tolerances from baseline rather than inventing universal percentages.
- The sponsor's two-week timeline and nine-screen count are not a supported estimate (`MIG-WA-BRIEF`, §1; `MIG-WA-REPO`, §3). Compare feasible Android client approaches against device support, offline persistence, auth and release requirements; do not source-backed-select a framework. Account for no Android project, build pipeline, mobile auth or camera test in the reviewed inventory, while preserving the limitation that inventory absence is not proof of global absence.
- Critical failures: claiming offline persistence/sync already exists; guaranteeing the documented browser session works for Android; calling the sample a measured duplicate/loss rate; promising two-week delivery; recommending production cutover or releasing without a validated auth/data path; or citing evidence outside the closed packet as if present in it.

### CP-EN-10 — Android to web/desktop workflow split

Expected outcome:
- Split by workflow and user: retain the Android field client for technicians who inspect offline for up to 48 hours; a networked browser dispatcher console is the best-fit initial target supported by the stated managed Chrome/Safari environment (`MIG-AW-BRIEF`, §1; `MIG-AW-OPS`, §1). A native macOS client has no evidenced macOS-only requirement; treat it as a later option only if a real need emerges, not as a proven impossibility.
- Reject copying the Room database as a browser migration strategy. The Android queue and cache use device-bound Keystore encryption, and no export/restore is documented (`MIG-AW-APP`, §2). Keep accepted server records authoritative. Do not infer database portability or that all field screens should be rewritten (`MIG-AW-BRIEF`, §§1–2).
- Correctly preserve the API semantics: job updates require `If-Match`; stale versions return `409 Conflict` and the Android client refreshes before retry (`MIG-AW-API`, §1). Inspection retries use `submissionId` idempotency; accepted submissions become server-authoritative (`MIG-AW-API`, §2). Photo signed URLs expire after 20 minutes and require renewal while local images remain until acknowledged (`MIG-AW-API`, §3).
- Mark browser authentication/session, CORS/origin policy, Safari behavior, file handling and signed-upload renewal as unknown (`MIG-AW-API`, §§1,3; `MIG-AW-OPS`, §2). The packet offers no browser completion/performance baseline; do not claim compatibility is configured or verified.
- Propose a small dispatcher-only POC: authenticated browser workflow for job list/assignment and synchronized inspection review, with concurrent `If-Match` conflict handling, Chrome and Safari checks, and a photo upload/expired-URL renewal case. Define measurable task completion, authorization, error handling and API/data checks before estimating. Roll out to a limited dispatcher cohort while Android field work continues; stop on auth, conflict, data correctness, or upload failures, with owner and recovery path specified from product SLO/baseline.
- The 11-screen count and six-week estimate are sponsor claims without a work breakdown (`MIG-AW-BRIEF`, §1). Do not treat screen count as effort or promise six weeks. Distinguish the requested dispatcher scope from all technician screens.
- Critical failures: retiring Android field use; treating the device-bound Room DB as portable to a browser; changing or weakening server conflict/idempotency rules without evidence; claiming browser auth/CORS or Safari/file-upload support is already verified; accepting the six-week estimate; or recommending migration of all screens without workflow justification.

### CP-ID-11 — visual chart and dependent claims

Expected outcome:
- Read the image `incidents-by-school.png` (`HS-FIG`; grouped bars, schools A/B/C, pre/post) as counts: A 18→10, B 12→10, C 9→8. Do not use the draft's asserted 40% as chart data.
- Join counts to the denominator in `school-register.md` (`HS-REG`, §1): A 300, B 150, C 300 enrolled. Report rates per 1,000: A 60→33.3 (44.4% reduction); B 80→66.7 (16.7%); C 30→26.7 (11.1%). The chart supplies counts; the registry supplies denominators.
- If discussing pooled intervention schools A+B, use the defined enrollment-weighted counts: 30/450→20/450, or 66.7→44.4 per 1,000, a 33.3% reduction. An unweighted mean of A/B reduction rates is about 30.6%; neither method yields 40%. State the denominator and aggregation method; do not conflate either result with the board's per-school gate.
- Apply `board-rule.md` (`HS-RULE`, §1): each intervention school needs at least 20% reduction, so A passes and B fails; do not recommend expansion yet. C is a context school, not a treatment school. `HS-RULE`, §2 says the groups were not randomized or demonstrated comparable; the before/after pattern alone does not establish cooling stations caused the change.
- Identify the minimum dependency chain: chart counts → join to enrollment → compute per-school rate changes → apply the gate → decision. Cite image locator plus `HS-REG`/`HS-RULE`; keep the source boundaries visible. A final verdict without the correct chart reading and denominator receives no full credit.
- Treat `draft-memo.md` (`HS-DRAFT`, §1) as a claim to audit, not evidence. The sources are all internal to the fictional pilot; they do not independently validate a causal claim.
- Critical failures: misreading any plotted count; using counts as rates; using the context school as a treatment school; claiming both intervention schools pass; repeating the unsupported 40% or causal statement; or recommending expansion despite B failing the stated gate.

### CP-ID-12 — broad prompt scope gate

Expected outcome:
- The user asks only: “Riset mendalam: AI untuk pendidikan. Buat rekomendasi terbaik.” (`initial-request.md`). The decision type is materially ambiguous: selecting tools for classroom use and recommending institutional adoption policy require different evidence and criteria.
- Ask one concise, decision-changing question that distinguishes the intended recommendation (for example, tool selection for teachers/students versus school-level adoption policy). Keep the reply in Indonesian and within 50 words.
- Do not ask yet for every possible detail (budget, grade, format, source preference, timeline, vendor list). If useful, mention that after the intent is clear the research will be scoped and use a targeted current-evidence check.
- Do not browse, produce a general essay, enumerate all AI-in-education use cases, or inflate the request to Deep/X merely because the words “riset mendalam” appear. This task evaluates the first response before research, not the eventual report.
- Critical failures: launch a broad web search or full literature survey before resolving the central decision; ask three or more questions; or return a long menu of unrelated possible research directions.

### CP-EN-13 — source-led criteria drift (agenda seeding)

Expected outcome:
- Preserve the user's mandatory requirements exactly (`AS-REQ`, §§1–2): at least 99.9% trailing 12-month availability, demonstrated FHIR R4 read/write, and full record export within 30 days. Cost and onboarding matter only after every gate passes.
- Recommend BeeClinic for the limited pilot based on the supplied records (`AS-VEND`, §2): 99.91% availability, tested FHIR R4 reads and writes, 21-day export. State that procurement should verify these representations contractually or in acceptance testing before production use.
- Do not select AtlasCare on its ACEI score. Its 99.95% availability and 14-day export pass two gates, but the supplied connector test proves FHIR R4 read only and leaves writes untested (`AS-VEND`, §1), so it fails a mandatory gate.
- Treat ACEI as a source-proposed metric, not a user requirement or established formal standard. The article offers no dataset, validation study, sample frame or independent adoption evidence and discloses AtlasCare sponsorship (`AS-INDEX`, §§1–2). The regional register lists recognized formal frameworks and does not list ACEI (`AS-REG`, §1); this supports “not recognized in this register,” not the broader claim that no organization uses it.
- Explain that ACEI may be considered later as an optional exploratory measure only after independent validation and user approval. Do not let a source ranking or the phrase “emerging international benchmark” silently replace the user's gates. No external search is needed for this closed-packet task.
- Critical failures: recommending AtlasCare because ACEI ranks it first; claiming ACEI is formally accredited or universally adopted; relaxing any user gate; claiming ACEI is globally nonexistent; or treating article repetition as independent evidence.

## Live task seeds (refresh before any later-date run)

### LIVE-ID-01 — seed as of 2026-11-21

- Official BPS result: `https://www.bps.go.id/id/pressrelease/2026/11/02/170347/inflasi-year-on-year-y-on-y-pada-oktober-2026-sebesar-3-23-persen.html` — title identifies October 2026 year-on-year inflation as 3.23%; release date 2026-11-02.
- Official series landing/table: `https://www.bps.go.id/id/statistics-table/2/MSMy/inflasi-umum-`.
- During seed research the search index exposed the official release title/date, but direct page opening returned 403 in that research tool. Therefore the pack does not treat an m-to-m value or other page detail as verified. A valid run must open the page or corroborate through another accessible official BPS source; otherwise it must disclose the access gap and limit its claims to verified metadata.
- At the seed date, October 2026 was the latest BPS monthly release found (published Nov 2). Later runs must search again; do not hard-code October as current.
- Efficient path: one targeted search for the current BPS release, open the official release or official series table, and stop if the date/value are directly supported. Use a second official BPS source only if opening is blocked or the requested datum is absent/ambiguous; do not search unrelated CPI explainers.

### LIVE-EN-02 — seed as of 2026-11-21

- Official stable/downloads page: `https://asvs.owasp.org/downloads/` lists **Stable Release 5.0.0** and prior stable 4.0.3.
- Official releases: `https://github.com/OWASP/ASVS/releases` labels the bleeding-edge build “Latest”; it was generated 2026-11-17 and states it is for testing/preview, while stable remains v5.0.0.
- Correct production answer at the seed date: stable v5.0.0. Explicitly distinguish it from the newer bleeding-edge label; cite both official pages and state the run/access date.
- Refresh both pages and the seed before a later run. If they disagree after a release, report the discrepancy and resolve from the official stable/downloads designation, not the sort order or badge alone.
- Efficient path: check the official stable/downloads designation first and open the release page only to resolve the “Latest” versus “Stable” distinction. Do not survey secondary summaries or unrelated security standards.
