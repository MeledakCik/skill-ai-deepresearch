# Deep Research Hub (Part Q)

Tools for running several deep-research AIs on one question so they check and complete each other.

| File | Use |
|:---|:---|
| `BRIEF_TEMPLATE.md` | Same brief for every AI (ChatGPT, Gemini, Claude, Copilot, Perplexity, Grok, DeepSeek, ...) |
| `RELAY_PROMPT.md` | Send one AI's packet to another to go deeper on gaps and weak findings |
| `CROSS_EXAMINE_PROMPT.md` | Have a different AI hunt for errors in a report |
| `MERGE_PROMPT.md` | Give all packets to the orchestrator to merge and write the final report |
| `research_packet.schema.json` | JSON format for packets |
| `merge_packets.py` | Quick merge of JSON packets into `merge_report.md` (agreement and origin counts) |

## Typical flow (Deep tier)

1. Write the brief once (`BRIEF_TEMPLATE.md`).
2. **Split:** give each AI the RQs it is best at (see SKILL.md Part Q1).
3. **Mirror:** give the 2-3 most important RQs to two or three AIs at once.
4. Collect Research Packets; run `RELAY_PROMPT.md` on the gaps.
5. Merge with `MERGE_PROMPT.md` (or `python merge_packets.py *.json` first).
6. **Cross-examine** the final draft with an AI that did not write it.
7. Record each AI's results in `federation_log.md` to improve routing next time.

Agreement between AIs is a signal, not proof. They can repeat the same wrong source, so linchpin claims are always checked against the primary source.
