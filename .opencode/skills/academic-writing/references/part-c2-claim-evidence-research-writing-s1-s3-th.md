## C2. Claim-Evidence Research Writing & S1-S3 Thesis Engine (`jin-s13/ai-research-writing-skill`)

- Every major claim traces to code/logs/tables/verified metadata, with a confidence label.
- **6-journey state machine:**
  1. Story (`paper_story.md`): thesis, gap, boundaries, claims to avoid.
  2. Claim-Evidence Map (`claim_evidence_map.md`): claim → section/table/figure/script/log + confidence.
  3. Verified BibTeX (`references.bib`): each entry checked against DOI/Crossref/arXiv/Semantic Scholar; SOTA matrix ≥5 works (`Author & Year | Method | Dataset | Metric | Gap`); `[TODO:CITE]` instead of hallucinating.
  4. Deterministic figures: method diagrams (TikZ/SVG) vs result plots produced by scripts from real CSV/JSON.
  5. Skeptical reviewer loop: hostile ICML/NeurIPS/promotor critique (B4 pass 3).
  6. Build gate (`build_check.md`): zero TODO, citations locked, LaTeX log clean, venue format.
- **Indonesian S1-S3 (Bab I-V):**
  - No cliché openings ("Di era globalisasi / revolusi industri 4.0..."). Open Bab I with the concrete phenomenon and its measured anomaly.
  - Bab I: inverted pyramid; $RQ_1..RQ_n$ mapped 1:1 to *Tujuan*.
  - Bab II: SOTA matrix built with A1 S4.2 citation chasing + *Kerangka Pemikiran*.
  - Bab III: formal methodology (DSR, CRISP-DM, NDLC, RUP), math, power/effect size, $O(n)$ bounds.
  - Bab IV: black-box + white-box testing (cyclomatic $V(G)=E-N+2P$), p50/p95/p99 with causal explanation, ablation.
  - Bab V: numbered answers to each RQ.
  - Lab report: Times New Roman 12 pt; margins top/left 4 cm, bottom/right 3 cm; correct cover year; legible enlarged screenshots.
