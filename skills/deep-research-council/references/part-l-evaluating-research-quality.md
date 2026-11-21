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

## L5. Evaluate the research report and the retrieval separately

Use two complementary test sets. A **closed evidence packet** makes answers reproducible and exposes whether the agent preserves conflicts, source origins and limits. A small **live-search set** checks source discovery, current facts and actual citation links. Include Bahasa Indonesia and English tasks when those are real use cases. Keep expected facts tied to opened source passages and date the packet.

Grade each run on separate, inspectable dimensions:

| Dimension | Observable check |
|:---|:---|
| Evidence retrieval | Was the decisive source found, opened and matched to the right population, period and measure? |
| Claim support | Does the exact cited passage support the attached sentence, including its numbers and strength? |
| Independent coverage | Do independent origins corroborate the pivotal claim, or do reports trace to one dataset? |
| Analysis | Are comparisons commensurate? Are counterevidence, uncertainty and causal limits handled? |
| Task coverage | Does the report answer the decision and every material sub-question? |
| Delivery and cost | Are the required format and checks complete? Record tokens or searches when available, otherwise label the proxy. |

Build a small, versioned set around failures the skill must survive: conflicting denominators, reports that repeat one origin, a changed fact, an unsupported citation, a blocked source, a missing result and a premature causal claim. Add a task only with its evidence locator and an acceptance rule. Run the same brief, model, tools and effort before and after a change. Have a blind human check a sample. A judge model is a diagnostic aid, not ground truth. Deep research benchmarks distinguish fixed-answer browsing from report-level analysis and presentation; expert-derived, fine-grained criteria are easier to inspect than one broad score. [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) · [DeepResearch Bench](https://arxiv.org/abs/2506.11763) · [BrowseComp](https://openai.com/index/browsecomp/)

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
