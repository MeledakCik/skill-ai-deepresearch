# Partial evaluation notes

- Evaluated skill: `17.13.0`; task pack: `1.2.0`; Codex CLI: `0.171.0-alpha.13`; model: `gpt-6.2-astra`.
- Completed: `2 / 10` tasks (CP-ID-01 and CP-EN-02). Six remaining closed-packet tasks and two live-search tasks were not run.
- Recorded successful-call usage: 111,726 input tokens (97,024 cached input, included in the input total) plus 3,310 output tokens. CP-ID-01 used 23,257 input+output tokens; CP-EN-02 used 91,779. These are separate task costs, not a matched efficiency comparison.
- The first CP-ID-01 attempt could not read the temporary prompt file because the workspace service was unavailable. An inline retry completed; usage for the failed attempt is unknown.
- CP-EN-02 emitted a non-fatal expired-credential warning from MCP startup/shutdown. It had no external search requirement and returned the closed-packet answer.
- The maintainer spot-checked both answers against the hidden acceptance rubric after generation. The review was not blind, and metric numerators/denominators were not formally scored.
- No numeric token cap was declared before this exploratory run. The run stopped after CP-EN-02's 89,793 input tokens; there was no observed Codex session/weekly/free-tier quota denial. Remaining quota is unknown.
- This artifact is a partial checkpoint only. Do not report a full-suite pass rate, baseline comparison or statistical result from it.
