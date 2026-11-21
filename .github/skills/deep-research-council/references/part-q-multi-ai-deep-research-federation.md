# PART Q — MULTI-AI DEEP RESEARCH FEDERATION (Make Every Research AI Strengthen the Others)

Research hosts can differ in available tools, data access, source ranking, context and failure modes, but their reports may still rely on the same underlying sources. Federation helps only when it explores distinct evidence or resolves a consequential uncertainty; agent agreement alone is not corroboration.

## Q1. The Roster (Strengths to Exploit, ⚠ features change often)

Treat this roster as discovery hints, not a current ranking or a durable statement of capability. Before routing a real task, verify the host's currently available search/connectors, file access, model selection, limits, privacy rules and output/citation behavior from first-party documentation and the actual authorized account. Record the check date; if a capability is not exposed or cannot be verified, mark it unknown. Do not infer a user's access, plan or quota from public marketing pages, and do not route confidential data to an unapproved provider. Benchmark results are task- and setup-specific; do not turn them into a universal vendor ranking.

| Platform | Potential fit to verify at run time | Pre-use check |
|:---|:---|:---|
| ChatGPT Deep Research (OpenAI) | Cited web research and supplied/connected source support, if enabled | Confirm the actual model, source access and citation locators |
| Gemini Deep Research (Google) | Plan-led web research and Workspace context, if enabled | Confirm account access, export path and primary-source coverage |
| Claude Research (Anthropic) | Parallel research lanes and connected work sources, if enabled | Confirm integrations and inspect lane/source overlap |
| Microsoft 365 Copilot Researcher | Research over organizational records the tenant permits | Confirm permissions and which repositories were searched |
| Perplexity (Deep Research / Pro search) ⚠ | Public-web discovery or source leads, if currently available | Verify pivotal claims at primary sources |
| Grok DeepSearch (xAI) ⚠ | Public-discussion discovery, including X only if available | Treat posts as leads unless they resolve to primary evidence |
| DeepSeek (search + thinking) / Qwen / Kimi ⚠ | Additional-language discovery or comparison lane, if available | Verify current search access, costs and every citation |
| Domain tools (Elicit, Consensus, Semantic Scholar, scite) ⚠ | Specialized scholarly indexes and citation context | Check coverage, indexing dates and study-level evidence |
| This skill's own agent (any harness) | Orchestration: brief, assign, merge, verify and report | Verify each upstream claim; do not count agreement as proof |

## Q2. Four Collaboration Patterns

| Pattern | How | When |
|:---|:---|:---|
| **1. Split (divide RQs)** | Each AI gets a distinct RQ and evidence boundary matched to its verified tools | Broad questions with independent parts; may reduce elapsed time or expand coverage, usually at higher aggregate usage |
| **2. Mirror (same brief, independent runs)** | 2-3 AIs get the identical brief; compare claims, definitions, sources and gaps | High-stakes decisions; use disagreement to target checks and treat matching independent evidence as corroboration, not an automatic confidence increase |
| **3. Relay (sequential)** | AI-1 maps the field → AI-2 checks only verified gaps → AI-3 reviews the draft if risk warrants it | Unknown territory; pass forward evidence IDs to avoid repeated searches |
| **4. Cross-examine (adversarial)** | Give a reviewer the report and evidence trail, then ask it to check linchpins and counterevidence | High-stakes, ambiguous or explicitly adversarial reviews |

### Q2.1 Delegation gate

Start with one researcher. Split only when there are at least two genuinely independent questions with distinct evidence targets, or when breadth/context limits justify parallel retrieval. Keep sequential work with one owner when subquestions depend on shared evolving state. Mirror runs are an expensive uncertainty check, reserved for pivotal/high-stakes questions where independent discovery could change the verdict; agreement is never a vote. Cross-examine a completed report when the risk, ambiguity or user request warrants it. Do not make all three patterns a default for every Deep task.

Before creating workers, record the shared goal, fixed user criteria, assigned RQ and evidence boundary for each worker, expected handoff, aggregate token/tool budget, and a stop condition. Assign non-overlapping lanes first. If a worker discovers a dependency or useful new lead in another lane, report it to the lead rather than launching an unbounded search. The lead should request another lane only for an unresolved, decision-changing gap.

## Q3. The Universal Research Brief (paste into any deep-research AI)

Every AI gets the same structured brief so results are comparable and mergeable:

```markdown
# Research brief — <title> (as of <date>)
Purpose / decision: <what the reader will do with this>
Core question: <one sentence>
Your sub-questions: RQ<n>: <...>   (only the ones assigned to this AI)
Scope: <geography, period, population, technology>
Out of scope: <...>
Source standard: prefer primary sources (official data, filings, peer-reviewed, official docs); include publication dates; languages: <EN + ID + ...>
Assignment boundary: <unique RQ, evidence/source types to pursue, out-of-lane topics to hand back>
Must include for every claim: source title, publisher, date, URL, and a short locator (section/page/quote ≤15 words)
Mark confidence per finding: Very high / High / Moderate / Low / Speculative, with one line why
List contradictions you found and sources that disagree
List what you could NOT find
Output format: Research Packet (see below)
```

## Q4. The Research Packet (shared exchange format)

Every AI returns, or is asked to convert its report into, this format. It lets the orchestrator merge results without re-reading whole reports.

```markdown
## Research Packet
producer: <platform + model + mode>   run_date: <YYYY-MM-DD>   brief_id: <id>

### Findings
| id | RQ | claim | confidence | sources (ids) | notes |
|:---|:---|:---|:---|:---|:---|
| F1 | RQ1 | ... | High | S1, S3 | ... |

### Sources
| id | title | publisher/author | date | url | publication role | data_origin_id | tier | locator |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| S1 | ... | ... | 2026-09 | https://... | origin | D1 | T1 | Table 3 |

### Lane contribution
Assigned RQs: RQ1
Verified unique evidence IDs: F1
Overlap with shared ledger: <source/claim IDs or none>
Unresolved decision-changing gaps: <...>

### Contradictions
| topic | says A (source) | says B (source) | likely reason |

### Gaps
- <what could not be found or verified>
```

Use publication role to distinguish an original source from analysis, summary or repost. Add a `data_origin_id` when the underlying measurement can be traced; if the lineage is unclear, mark it unknown rather than guessing.

Machine-readable version: `adapters/deep-research-hub/research_packet.schema.json`.

## Q5. Merge Protocol (Orchestrator)

1. **Normalize:** convert every report into a Research Packet (ask the producing AI to do it, or extract it yourself).
2. **De-duplicate sources by origin**, not by URL (A0 law 4). Two AIs citing the same press release = one origin. Preserve both publication lineage and underlying data lineage.
3. **Align claims:** group findings that state the same thing (same entity, metric, period, definition). Compare each worker's assignment to its actual sources and claims.
4. **Separate contribution from repetition:** identify verified evidence or contradiction resolution that only one lane found, shared evidence found by several lanes, and unusable/unsupported output. Agent agreement over a shared origin adds no independent evidence.
5. **Score agreement:**

| Situation | Effect on confidence |
|:---|:---|
| Same claim, independent runs and **distinct, supporting** origins | Treat as corroboration after checking the claims, definitions and source passages. Reassess the evidence; do not raise a label mechanically. |
| Same claim, ≥2 AIs, **same** single origin | One origin repeated; it adds no independent evidence. |
| Claim from one AI only | Treat as unverified until its linchpin evidence is checked. |
| AIs disagree | Open a contradiction; resolve with primary source; if unresolved, report both |
| Claim's cited source does not support it on re-check | Drop or downgrade, whichever AI produced it |

6. **Verify linchpins yourself** by opening the primary sources (Part N). Agreement between AIs is a signal, not proof: they can share the same wrong source.
7. **Fill gaps selectively:** merge the "Gaps" lists, remove duplicates and assign only unresolved gaps likely to change the answer. Do not repeat completed searches.
8. **Write once** in the A1 S6 report shape, crediting which runs contributed (methodology section).

## Q6. Credit and Calibration Log (Making the Team Better Over Time)

Keep `federation_log.md` per project:

| run | platform/model | assigned RQs | claims kept/dropped | unique verified finds | duplicated/unusable returns | input+output tokens | tool calls | wall time | citation errors |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|

After 3-5 projects, the log can show which tools helped on which task types and at what measured cost. Treat this as a small, setup-specific routing history, not a permanent provider ranking. Route future RQs accordingly and refresh volatile capabilities at use time.

## Q7. Hand-off Prompts

**Relay, stage 2 (deepen):**
> "Here is a Research Packet from a previous run. Do not repeat its findings. Go deep on its Gaps and on findings marked Moderate or lower. Find primary sources that confirm or refute them. Return a new Research Packet."

**Cross-examine:**
> "Here is a research report produced by another AI. Act as a hostile reviewer. For each key claim: does the cited source actually support it? Is there newer or stronger counter-evidence? What important angle is missing? Return a list of issues with severity, evidence and URL, then a Research Packet of any new findings."

**Merge (to the orchestrator):**
> "Here are N Research Packets from different AIs on the same brief. Apply the merge protocol: de-duplicate by origin, align claims, score agreement, list contradictions, list remaining gaps. Then write the final report in the standard shape, with a methodology section naming which runs contributed what."

## Q8. Rules That Keep the Federation Honest

- No AI's output is accepted as ground truth, including this skill's own drafts.
- Never paste one AI's unverified claims into another as fact; label them as "claims to check".
- Respect each platform's terms of service and data policies; do not move confidential work data into a platform not approved for it (M1).
- Report which platforms were used, so the reader can judge.
- Cost control: Mirror runs multiply cost and time. Use them only for linchpin RQs or high-stakes work.
- Log each worker's assignment, actual tool/source trail, verified unique evidence contribution, duplicated or unusable contribution, and failures. Count lead, workers, retries, merge and citation verification in the aggregate cost whenever the host exposes them; mark hidden usage unknown.
- Stop delegation when the next worker is expected only to repeat settled evidence, when remaining work is dependent rather than parallel, or when the aggregate budget cannot cover synthesis and citation checks. Report what extra coverage cost; do not claim efficiency from shorter wall time alone.
- Compare orchestration policies on matched tasks, tools, models and total aggregate budgets before claiming a quality or efficiency gain. A multi-agent run given more tokens than its single-agent baseline cannot establish that delegation itself caused the improvement.

These are conditional controls, not a claim that parallelism is inherently wasteful. Anthropic's published system report describes high task-specific token overhead for its multi-agent research setup, while the Argus preprint identifies duplicated evidence and diminishing returns in parallel rollouts. Treat both as reasons to measure marginal contribution in the user's own setup, not as universal cost ratios. [Anthropic Research system](https://www.anthropic.com/research/multi-agent-research-system) · [Argus preprint](https://arxiv.org/abs/2605.16217)
