## M1. Microsoft 365 Copilot — Researcher & Analyst (Enterprise Research Mode)

**What is public:** Researcher combines OpenAI's deep research model with Copilot's orchestration and deep search. It pulls from work data (email, meetings, chats, files) and connected systems (e.g., Salesforce, ServiceNow, Confluence), and returns source-cited reports with key findings and next steps. It respects existing tenant permissions and compliance policies. Analyst is a separate reasoning agent for raw data: it makes an analysis plan and runs Python iteratively.

**Enterprise Research Mode (apply when the user's own org data matters):**

| Step | Practice |
|:---|:---|
| 1 Scope by permission | Use only sources the user can already access. Never widen access; never move data across a boundary the org set (D-rules in safety) |
| 2 Internal first, web second | For "our Q3", "our strategy", "the client", search connected work sources (Drive, SharePoint, Slack, CRM) before the web; web fills market context |
| 3 Label provenance | Mark each claim **[internal]** or **[external]**; internal claims cite document title + date + owner |
| 4 Separate research from analysis | Researcher-style: gather, cite, synthesize. Analyst-style: load data to files, plan the analysis, compute in code, show the code's outputs. Never estimate numbers in prose |
| 5 Freshness check | Internal docs go stale too: prefer the latest version; flag drafts and superseded decks |
| 6 Confidentiality | Do not quote sensitive internal content into public-facing outputs; summarize at the needed level |
| 7 Deliverable | Report with key findings + recommended next steps + owners, ready to paste into the org's format |
