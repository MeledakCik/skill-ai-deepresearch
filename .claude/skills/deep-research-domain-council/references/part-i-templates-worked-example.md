# PART I — TEMPLATES & WORKED EXAMPLE

## I1. `source_log.md`

```markdown
| ID | Title | Author / Publisher | Date | URL | Tier | Origin of | Accessed | Relevance |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| S1 | Statistik E-Commerce 2025 | BPS | 2026-03 | https://... | T1 | origin | 2026-11-18 | Market size baseline for RQ1 |
| S2 | "E-commerce grows 20%" | News site | 2026-04 | https://... | T2 | copy of S1 | 2026-11-18 | Not independent; cite S1 instead |
```

## I2. `contradictions.md`

```markdown
| Topic | Source A says | Source B says | Likely reason | Resolution |
|:---|:---|:---|:---|:---|
| Market size 2025 | S1: Rp X T (GMV) | S5: Rp Y T (revenue) | GMV vs revenue definitions | Report both, explain definitions |
```

## I3. ACH Matrix Example

| Evidence | H1: Demand fell | H2: Competitor took share | H3: Measurement changed |
|:---|:---|:---|:---|
| Category search volume flat (S3) | I | C | N |
| Competitor launched cheaper plan same month (S4) | N | C | N |
| Analytics tag migrated that week (S7) | N | N | C |
| Support tickets about tracking (S8) | N | N | C |
| **Inconsistencies** | **1** | **0** | **0** |

Reading: H1 is weakest. H2 and H3 both survive, so the linchpin is S7: verify the tag migration date before concluding. Report both until resolved.

## I4. Research Plan Example (Shown to User)

```
Core question: Should we build our store on Platform A or Platform B for the Indonesian market in 2027?
1. Define criteria with you: cost at 1K/10K orders/month, local payment support (QRIS, VA, e-wallets), shipping integrations, admin language, lock-in.
2. Pull official pricing pages and fee schedules for both (T1), dated.
3. Check payment-gateway docs for QRIS / virtual account support (T1).
4. Find independent merchant experiences in Indonesian forums and reviews (T3, used for failure modes only).
5. Disconfirmation: search known outages, fee changes, migration complaints.
6. Build cost model at 3 volumes; sensitivity to fee changes.
7. ACH on "A better / B better / depends on volume".
Deliverable: 2-page brief + cost table + sources. Est. 20-30 sources (S tier).
```

## I5. Report Skeleton

```markdown
# <Title> (as of <date>)
## Bottom line
## Executive summary
## 1. <RQ1>
## 2. <RQ2>
## Key findings (ranked)
## Confidence & limitations
## Methodology
## Sources
## Follow-up questions
```
