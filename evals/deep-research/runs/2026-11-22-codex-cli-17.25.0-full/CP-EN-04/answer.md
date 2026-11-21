**One independent origin supports the pilot’s observed rate.** The October 2026 pilot register records 63 visits in 13 staffed hours across nine evenings, or **4.85 visits per observed staffed hour**. That exceeds the board’s 4.5 threshold for the observed hours. S10’s two hours have no visit count, so the full ten-evening rate is unknown. (`LIB-REGISTER` rows S01–S10; `LIB-BRIEF` §1; `LIB-OUTAGE` §1)

| Packet item and locator | Evidence and lineage |
|---|---|
| `LIB-REGISTER` rows S01–S09, S10 | Primary pilot observations. S01–S09 supply the visits and hours. S10 records the outage and leaves visits blank. |
| `LIB-ANALYSIS` §§1–3 | Calculates the rate from the register, explains the missing interval, and documents the lack of a control group or comparable pre-pilot evening series. |
| `LIB-PRESS` §§1–2 | Explicitly attributes its figures to the analyst summary. Its causal wording adds no measurement. |
| `LIB-OUTAGE` §1 | Primary incident evidence from the telemetry service. It confirms the S10 counter failure and absence of a backup tally. |
| `LIB-NETWORK` row `annual-all-branches` | Independent operational data for a different population, period, and schedule. Its 4.00 rate covers all staffed hours at four branches in 2025 (1,200 visits / 300 hours). |
| `LIB-VENDOR` §1 | The promotional 18% claim has no verifiable underlying data, denominator, comparison group, or study citation. |
| `LIB-BRIEF` §§1–2 | Establishes the board’s threshold and decision question. It supplies no visit measurements. |
| `LIB-DRAFT` §1, claims 1–4 | Contains the assertions under audit and supplies no original evidence. |
| `source-map.md`, “Provenance graph” | Documents the chain `pilot-register.csv` → `analyst-summary.md` → `press-release.md`. |

**Audit of `LIB-DRAFT` §1**

1. **Claim 1.** The count and hours are correct for the nine observed evenings. The pilot design cannot establish a causal increase, and the vendor gives no evidence for 18%. (`LIB-REGISTER` rows S01–S10; `LIB-ANALYSIS` §3; `LIB-VENDOR` §1)
2. **Claim 2.** The release identifies the analyst summary as its source, ruling out independent replication. (`LIB-PRESS` §§1–2)
3. **Claim 3.** The 21.2% arithmetic is correct using the unrounded rates. The different populations, periods, and schedules prevent that difference from establishing pilot outperformance. (`LIB-REGISTER` rows S01–S09; `LIB-NETWORK` row `annual-all-branches`)
4. **Claim 4.** Six observed sessions met the threshold. S02, S03, and S05 fell below it at 4, 0, and 4 visits per hour, respectively. S10 is unknown. (`LIB-BRIEF` §1; `LIB-REGISTER` rows S01–S10; `LIB-OUTAGE` §1)
