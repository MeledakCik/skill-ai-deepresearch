# Merge Prompt (orchestrator)

Give this, with all Research Packets, to the AI that will write the final report (ideally one running the deep-research-domain-council skill).

---

Below are <N> Research Packets from different AIs answering the same brief (<brief_id>). Merge them:

1. De-duplicate sources by ORIGIN, not URL. Several articles repeating one press release or dataset count as one origin.
2. Group findings that state the same thing (same entity, metric, period, definition).
3. Score agreement:
   - Same claim from 2+ AIs with different origins: raise confidence one level.
   - Same claim from 2+ AIs but one shared origin: no change.
   - Claim from one AI only: keep its level; verify it if it is a linchpin.
   - AIs disagree: record a contradiction and resolve it with the primary source, or report both sides.
4. Re-open the primary source for every linchpin claim before keeping it.
5. Combine all Gaps lists; mark which gaps remain.
6. Write the final report: Bottom line, Executive summary (cited), one section per RQ, ranked key findings, confidence & limitations, methodology (which AI runs contributed what), sources, follow-up questions.

Also output a federation log row for each AI: claims kept, claims dropped (why), unique valuable finds, citation errors.

<PASTE ALL RESEARCH PACKETS HERE>
