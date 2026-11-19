# PART Q — MULTI-AI DEEP RESEARCH FEDERATION (Make Every Research AI Strengthen the Others)

No single deep-research product is best at everything. Each searches a different slice of the web, ranks sources differently, and makes different mistakes. Used together with a shared protocol, they cover each other's blind spots: one finds what another missed, and claims that survive independent runs earn more trust. This part turns several research AIs into one team.

## Q1. The Roster (Strengths to Exploit, ⚠ features change often)

| Platform | Use it for | Watch out for |
|:---|:---|:---|
| ChatGPT Deep Research (OpenAI) | Long cited reports, hard-to-find facts (strong BrowseComp record), file + connector inputs | Long run times; verify that citations support the exact sentence |
| Gemini Deep Research (Google) | Editable research plan up front, broad web coverage, Google Workspace context, export to Docs | Breadth can outrun depth; check primary sources |
| Claude Research (Anthropic) | Multi-agent breadth on independent sub-questions, connected work tools (Drive, Gmail, integrations) | Ask explicitly for primary sources and dates |
| Microsoft 365 Copilot Researcher | Questions that depend on the org's own email, meetings, files, CRM | Only sees what your tenant permissions allow |
| Perplexity (Deep Research / Pro search) ⚠ | Fast first sweep, quick source lists to seed deeper runs | Short answers; verify depth |
| Grok DeepSearch (xAI) ⚠ | Very recent public discussion and news on X | Social posts are T4 unless they lead to a primary source |
| DeepSeek (search + thinking) / Qwen / Kimi ⚠ | Chinese-language sources, cost-efficient runs, second opinion | Check citations and dates carefully |
| Domain tools (Elicit, Consensus, Semantic Scholar, scite) ⚠ | Academic literature, citation context, study design | Coverage limited to indexed papers |
| This skill's own agent (any harness) | Orchestrator: brief, split, merge, verify, write | Must not trust any single upstream report |

## Q2. Four Collaboration Patterns

| Pattern | How | When |
|:---|:---|:---|
| **1. Split (divide RQs)** | Each AI gets different RQs matched to its strengths (Copilot: internal data; Grok: last-week discourse; ChatGPT/Gemini/Claude: core literature) | Broad questions with independent parts; saves time and tokens |
| **2. Mirror (same brief, independent runs)** | 2-3 AIs get the identical brief; results are compared claim by claim | High-stakes decisions; agreement across independent runs raises confidence, disagreement shows where to dig |
| **3. Relay (sequential)** | AI-1 maps the field and sources → AI-2 goes deep on the gaps AI-1 lists → AI-3 red-teams the combined draft | Unknown territory; each stage builds on the last |
| **4. Cross-examine (adversarial)** | Give AI-B the report of AI-A and ask it to find errors, missing evidence and counter-evidence | Before shipping any D/X-tier report |

Default for Deep tier: **Split + Mirror on the 2-3 linchpin RQs + Cross-examine the final draft.**

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
| id | title | publisher/author | date | url | tier | locator |
|:---|:---|:---|:---|:---|:---|:---|
| S1 | ... | ... | 2026-09 | https://... | T1 | Table 3 |

### Contradictions
| topic | says A (source) | says B (source) | likely reason |

### Gaps
- <what could not be found or verified>
```

Machine-readable version: `adapters/deep-research-hub/research_packet.schema.json`.

## Q5. Merge Protocol (Orchestrator)

1. **Normalize:** convert every report into a Research Packet (ask the producing AI to do it, or extract it yourself).
2. **De-duplicate sources by origin**, not by URL (A0 law 4). Two AIs citing the same press release = one origin.
3. **Align claims:** group findings that state the same thing (same entity, metric, period, definition).
4. **Score agreement:**

| Situation | Effect on confidence |
|:---|:---|
| Same claim, ≥2 AIs, **different** origins | Raise one level (max Very high) |
| Same claim, ≥2 AIs, **same** single origin | No change: it is one source repeated |
| Claim from one AI only | Keep its level; verify linchpins yourself |
| AIs disagree | Open a contradiction; resolve with primary source; if unresolved, report both |
| Claim's cited source does not support it on re-check | Drop or downgrade, whichever AI produced it |

5. **Verify linchpins yourself** by opening the primary sources (Part N). Agreement between AIs is a signal, not proof: they can share the same wrong source.
6. **Fill gaps:** union of all "Gaps" lists becomes the next relay round, sent to the AI best suited for each gap.
7. **Write once** in the A1 S6 report shape, crediting which runs contributed (methodology section).

## Q6. Credit and Calibration Log (Making the Team Better Over Time)

Keep `federation_log.md` per project:

| run | platform | RQs | claims kept | claims dropped (why) | unique valuable finds | citation errors |
|:---|:---|:---|:---|:---|:---|:---|

After 3-5 projects, the log shows which platform is reliable for which kind of question. Route future RQs accordingly. This is how the AIs "benefit each other": every run improves the routing and verification of the next.

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
