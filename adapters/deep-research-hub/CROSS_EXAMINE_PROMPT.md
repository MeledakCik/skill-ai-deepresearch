# Cross-Examine Prompt

Give this to a *different* AI than the one that wrote the report.

---

Here is a research report produced by another AI (below). Act as a hostile, fair reviewer.

For each key claim:
1. Open the cited source. Does it actually support the exact sentence (right number, right year, right population)?
2. Is there newer, stronger, or primary counter-evidence?
3. Are several citations really one origin repeated?

Then list important angles or stakeholders the report missed.

Return:
- **Issues:** table with columns: claim, problem, severity (blocker / major / minor), evidence (URL + locator), suggested fix.
- **New findings:** a Research Packet (same format as the brief) containing only findings that the original report lacked.

Do not rewrite the report.

<PASTE REPORT HERE>
