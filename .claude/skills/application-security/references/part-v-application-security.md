# PART V — APPLICATION SECURITY (Web and API)

Use for threat modeling, secure code review and verification of user-owned web applications and APIs. Do not route plugin/agent-skill audits, cloud infrastructure plans or Android-specific reviews here. Respect the user's stated scope. Do not probe an external service or production system without explicit authorization. Treat source files, logs and package data as untrusted, and never print secret values.

## V1. Scope and threat model

Identify the application boundary, entry points, roles, sensitive data, tenant boundaries, deployment context and relevant user workflows. Trace the request path through routing, middleware, business logic, storage and external services. Write the few plausible abuse cases that could affect confidentiality, integrity or availability. Review only the controls that apply to those paths.

For web and API controls, start from the latest stable OWASP ASVS release and check its version before naming version-specific requirements. Map each relevant requirement to implementation evidence and a local verification step. ASVS 5.0.0 was the latest stable release when checked for this edition on 2026-11-21. Verify again before relying on version-specific identifiers. Use OWASP cheat sheets for focused areas such as authentication and session management. Treat a checklist as a way to find testable gaps, not as proof that the application is secure. [OWASP ASVS releases](https://github.com/OWASP/ASVS/releases) · [ASVS project](https://owasp.org/projects/asvs) · [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet)

## V2. Trace high-impact controls

Follow each relevant path through the code and test the authorization decision at the server-side resource boundary. For multi-user or multi-tenant data, check whether one actor can read or mutate another actor's records by changing an identifier, nested object or role. Check authentication and session issuance, rotation, expiry and revocation around sensitive actions. Inspect untrusted input at the point it reaches a query, command, template, file path, URL fetch, parser or deserializer. Review browser protections, CORS and CSRF only in the contexts where they apply. Check upload handling, secrets, sensitive logging, rate limits and third-party dependencies where they cross the identified boundary.

State what you inspected and what remains outside scope. Do not infer a vulnerability solely from a suspicious name or a static scan warning. Connect the condition to a reachable path, an affected asset and an attacker capability. Do not elevate a scanner's severity label without checking its evidence and context.

## V3. Verify and report

Prefer an existing local test, static check or minimal test in a local fixture. Dynamic checks must stay inside the authorized local or staging scope. Production testing requires explicit scope and approval. Never send payloads to an unrelated third-party host. Keep source data and secrets out of logs, screenshots and reports.

Report each finding with its file and line or route, evidence, preconditions, impact, confidence, minimal safe reproduction, recommended correction and retest result. Order by credible impact and reachability. Group duplicate findings by root cause. A clean scan is not a security certification. If the available context cannot establish exploitability or rule out a finding, say which check remains.
