# Universal Research Brief

Paste this into any deep-research AI (ChatGPT Deep Research, Gemini Deep Research, Claude Research, Copilot Researcher, Perplexity, Grok DeepSearch, DeepSeek, ...). Fill the <...> parts. Give every AI the same brief so results can be compared and merged.

---

# Research brief — <title> (as of <YYYY-MM-DD>)
Brief ID: <short-id>
Purpose / decision: <what the reader will do with this>
Core question: <one sentence>
Your sub-questions:
- RQ1: <...>
- RQ2: <...>
Scope: <geography, period, population, technology>
Out of scope: <...>
Source standard: prefer primary sources (official data, regulatory filings, peer-reviewed studies, official documentation). Include the publication date of every source. Languages: <English, Bahasa Indonesia, ...>.
For every claim give: source title, publisher/author, date, URL, and a short locator (section, table, page, or a quote of at most 15 words).
Mark confidence per finding (Very high / High / Moderate / Low / Speculative) with one line explaining why.
List contradictions between sources and explain the likely reason.
List what you could NOT find or verify.

Return your result in this exact format:

## Research Packet
producer: <platform + model + mode>   run_date: <YYYY-MM-DD>   brief_id: <short-id>

### Findings
| id | RQ | claim | confidence | sources (ids) | notes |
|:---|:---|:---|:---|:---|:---|

### Sources
| id | title | publisher/author | date | url | tier (T1 primary .. T4 weak) | locator |
|:---|:---|:---|:---|:---|:---|:---|

### Contradictions
| topic | says A (source) | says B (source) | likely reason |
|:---|:---|:---|:---|

### Gaps
- <...>
