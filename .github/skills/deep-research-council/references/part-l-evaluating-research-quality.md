# PART L — EVALUATING RESEARCH QUALITY (How Labs Grade Research Agents)

## L1. Rubric-Based Judging

Inspect the cited passages in a separate pass. Use task-specific, observable criteria rather than relying on a single overall score. Record critical factual or citation failures separately from coverage and presentation. A weighted average cannot erase a false pivotal claim or a citation that does not support it.

| Criterion | Question |
|:---|:---|
| Factual accuracy | Do claims match the cited sources? |
| Citation accuracy | Does each citation actually support its sentence? |
| Completeness | Are all RQs and requested aspects covered? |
| Source quality | Primary/T1 sources used where available, not SEO pages? |
| Tool efficiency | Reasonable number of searches for the tier; no loops? |
| Calibration | Confidence matches evidence? |
| Usefulness | Can the reader act on it? |

Do not treat uncalibrated score thresholds as a quality guarantee. Before using an automated judge for release decisions, compare its judgments with a small, blinded expert-reviewed sample. Report the disagreement and revise the rubric before scaling.

## L2. Golden Questions

Keep a small set (5-20) of questions with known, verified answers from your domain. After changing the skill, prompts, or model, rerun them and compare. A small, carefully chosen set catches big regressions early; grow it when new failure types appear.

## L3. Human Spot Checks

Automated judging misses subtle failures (e.g., preferring SEO pages over authoritative but less-ranked sources). For D/X work, a human reviews a sample of sources and the BLUF before the report is used for a real decision.

## L4. Failure Taxonomy (Log These)

| Failure | Symptom | Fix |
|:---|:---|:---|
| Under-search | A pivotal question rests on one unexamined origin | Trace the measurement, seek an independent challenge and qualify the conclusion if evidence stays sparse |
| Over-search | Retrieval continues after the decision and counterchecks are settled | Recheck the pivotal uncertainty and stop when the next search cannot change the answer |
| Echo chamber | All sources share one origin | Origin counting (A0 law 4) |
| Citation drift | Citation near but not supporting the claim | Citation inspection (A1 S7.1) |
| Stale facts | Old prices/versions | "As of" dates; volatile-fact gate (E9) |
| Delegation confusion | Sub-agents duplicate work | Structured delegation briefs (J3) |
| Pretty but empty | Polished format, thin evidence | Rubric L1 before formatting |

## L5. Evaluate research retrieval and reports separately

Use two complementary tracks. A **closed evidence packet** makes evaluation reproducible and reveals whether the agent preserves conflicts, source origins and limits. A **live-search set** checks source discovery, current facts and working citations. Keep the tracks' scores separate: an answer can reason well from supplied files while failing to find the right web evidence, or retrieve good sources and then misstate them.

### Build a small, versioned task set

- Stratify only across dimensions that matter to this skill: Bahasa Indonesia and English when used; supplied files and live web; fact checks and report-level synthesis; stable and time-sensitive facts. Include a compact set of failure cases such as a false premise, conflicting denominators, duplicated reports from one origin, a blocked source, a missing result, unsupported citations and a causal claim without an identifying design.
- For closed packets, freeze the task's eligible files and date. Include relevant evidence plus realistic distractors or noise when useful. Record each required evidence item, its source origin and exact locator (page, section, table, row or timestamp), expected claims, material caveats and the acceptance rule. If OCR, a chart or another extraction step is uncertain, record that limitation instead of treating a guessed value as ground truth.
- For live tasks, date the prompt and reference answer, store exact query-log entries and URLs actually opened, and recheck time-sensitive facts at evaluation time. Do not grade a changed fact against stale ground truth. A web search has a bounded, unknown source universe, so report task-level hits and failures; do not label them global retrieval recall.
- Before a multi-task run, declare a practical budget: task order, maximum measured tokens or spend when available, wall time, tool calls, and a small reserve for scoring and delivery. If the host exposes a quota or reset window, record its wording and value; otherwise leave it unknown. Start with a representative, high-information task and inspect its actual usage before scheduling more. Do not assume tasks have equal cost.
- After each task, save the unedited answer, source locators, settings, measured usage, failures and completion status. Stop before the next expensive call when the declared cap is reached, the host reports a quota/rate limit, or the remaining budget cannot cover review and delivery. A failed setup attempt is a failure, not a completed task; record it and retry only through a bounded, materially different recovery path.
- On a stop, write a checkpoint with the original conditions, completed and remaining task IDs, verified outcomes, unavailable measures, stop reason, and the exact next action/retry condition. Use Part T for quota recovery. Resume from that checkpoint with unfinished tasks only; do not rerun completed tasks unless a replicate was planned. If model, tools, effort, prompt or packet changes, record a new run condition rather than pooling it with the earlier one.
- Report a partial run as `completed / planned`; score only completed tasks and label the rest untested. Never present a partial denominator as a full-suite pass rate. Keep per-task cost visible, mark unexposed limits and costs unknown, and do not infer token use from answer length.
- For every run, record the task-pack version, skill/prompt version, model, tools, effort or relevant settings, date, task status, source locators and any unavailable tools. For Standard/Deep research tasks, preserve the compact search log as an artifact. Keep the same setup for before/after comparisons; if a model or tool changes, mark that as a separate factor rather than attributing the difference to the skill.

### Score observable evidence and outcomes

| Dimension | Observable check |
|:---|:---|
| Required-evidence retrieval | In a closed packet, what share of prelisted eligible evidence items was found, opened and used correctly? State the denominator. In live search, did the run find the decisive independent source for each task? |
| Citation fidelity | Does the exact cited passage support the attached claim's value, population, period, unit and strength? Distinguish broken links, wrong locators and nearby-but-irrelevant passages. |
| Material-claim coverage | What share of checked material claims has adequate evidence? State how claims were selected and the denominator; do not equate citation count with coverage. |
| Source independence | Do reports trace to independent data origins, or repeat the same press release, study or dataset? Count shared origins once. |
| Analysis | Are measures commensurate? Are contradictions, missing evidence, uncertainty, alternatives, bias and causal limits handled? |
| Task and delivery | Does the result answer the decision and material sub-questions, follow the requested language/format, and disclose what could not be verified? |
| Efficiency and reliability | Record tokens, searches/tool calls, latency, failures, recovery and the compact query log when available. Otherwise label the proxy. Judge whether queries tested distinct uncertainties and found useful evidence; raw query count alone is not efficiency. Compare cost per task that passes its quality gates, not cost per URL or raw answer. |

For a within-task token diagnostic, optionally report measured input + output tokens per predeclared pivotal claim that passes citation and factual checks. Keep the accepted-claim count visible; this ratio is descriptive, not a quality score. Compare only matched prompt, packet, model, tools and settings. A run with a critical failure is not an efficiency improvement, even if it is shorter. If token usage is unavailable, mark it unknown instead of estimating from answer length.

For critical claims, report factual support and citation support separately from completeness and presentation. A fabricated source or unsupported pivotal claim is a critical failure; presentation or a weighted average cannot hide it. Define acceptance criteria before grading and set thresholds for the task's risk, not as universal constants. If forecasts have resolved outcomes and a suitable reference class, assess calibration on those forecasts; do not convert ordinary research confidence into unsupported probabilities.

### Compare versions without overclaiming

Run the same prompts, packets, model, tools and effort before and after a skill change. Repeat only a small, risk-selected subset when stochastic variation could change the conclusion; preserve individual runs and summarize the spread rather than presenting one lucky run as stable. Blind a domain-capable human to the version for a sample of evidence and reports. Compare automated judgments with those reviews, record disagreements and revise the rubric; use a judge model for triage, not as ground truth. For small samples, describe observed cases and uncertainty without claiming statistical significance.

Keep the suite small enough to run regularly. Add a task only when it captures a distinct failure, and keep its source locator and acceptance rule with it. Benchmarks offer useful dimensions, not universal quality thresholds: DeepResearch Bench II uses expert-derived rubrics for information recall, analysis and presentation; DR³-Eval tests multi-file reports against supportive material, distractors and noise. These motivate separate retrieval/report checks and realistic document packets, but results across benchmarks or different model/tool setups are not directly interchangeable. For a manually runnable maintainer pack, see `evals/deep-research/README.md`; give the evaluated agent only the prompt and allowed packet, never the hidden acceptance criteria. [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) · [DR³-Eval](https://arxiv.org/abs/2604.14683) · [DeepResearch Bench](https://arxiv.org/abs/2506.11763) · [BrowseComp](https://openai.com/index/browsecomp/)

## Sources for Parts J-L

- OpenAI, "Introducing deep research": https://openai.com/index/introducing-deep-research/
- OpenAI, "BrowseComp": https://openai.com/index/browsecomp/
- OpenAI Cookbook, "Deep Research API Agents": https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api_agents
- Google, "Gemini Deep Research" overview: https://gemini.google/overview/deep-research/
- Anthropic Engineering, "How we built our multi-agent research system": https://www.anthropic.com/engineering/multi-agent-research-system
- DeepSeek-AI, "DeepSeek-V3.2" technical report: https://arxiv.org/abs/2512.02556
- DeepSeek API docs, "Web Tools": https://api-docs.deepseek.com/guides/web_tools.md
- OPPO AI Agent Team, "Search More, Think Less": https://arxiv.org/abs/2602.22675
- Yue et al., "DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports": https://arxiv.org/abs/2601.08536
- Xie et al., "DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation": https://arxiv.org/abs/2604.14683
