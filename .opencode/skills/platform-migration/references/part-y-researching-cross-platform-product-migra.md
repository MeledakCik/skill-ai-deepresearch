# PART Y — RESEARCHING CROSS-PLATFORM PRODUCT MIGRATIONS

Use for a product that already exists and may move between web, Android, iOS/iPadOS, Windows desktop, macOS or a mix of them. This is a feasibility and planning method; it does not assume the user wants code rewritten. Pair it with the `platform-migration` skill. For implementation, inspect the real repository and use the skill for the chosen target platform.

## Y1. Establish the actual migration

Name the source product and platform, destination platform(s), supported OS/browser versions, user groups, critical workflows, release/distribution channel, constraints, and what “successful migration” means. If the user did not specify a detail, ask only when it could reverse the recommendation; otherwise record a bounded assumption and show how it affects the decision.

Inspect supplied code, architecture documents, analytics, API contracts, screenshots or support reports before describing the current product. Inventory workflows and their states—not just pages: sign-in, first use, primary task, data changes, offline/retry, permissions, success, failure, account/data export, and support. Mark each fact as observed, inferred or unknown, and attach a file path, source locator or owner for verification.

For a repository, inspect the actual entry points, modules, package manifests, build/release path and dependency graph. Trace who owns each important data entity, which clients/services read or write it, how identity/session state is issued and renewed, and where state lives (server, browser storage, local database, files, queued/offline edits). Capture external consumers, schema/API versions, test coverage and runtime evidence if supplied. Do not infer usage or reliability from filenames alone; name what needs a query, log or owner confirmation.

Do not equate “web” with a responsive site or “app” with a native client. Identify whether the source is a public website, authenticated web app, PWA, packaged desktop app, or native client, and whether the target needs browser access, store distribution, background work, hardware access, offline use, managed deployment or a platform-specific experience.

## Y2. Build the capability and evidence matrix

For each workflow or capability, capture the current behavior and target requirement. Use these disposition labels:

| Label | Meaning |
|:---|:---|
| **Share** | The same domain rule, API contract, schema or content can remain authoritative across platforms; verify compatibility and ownership. |
| **Adapt** | The outcome stays the same but interaction, persistence, navigation, permissions or lifecycle must change. |
| **Native** | A target-specific API or convention is required; name the exact capability and minimum supported version. |
| **Replace / retire** | The feature has a justified target equivalent or no longer belongs in scope; record user and data impact. |
| **Unknown** | Current evidence is insufficient; define the smallest check or prototype that can resolve it. |

Include identity and session renewal; data ownership, import/export and migration; offline/sync/conflict behavior; notifications and deep links; background tasks and process restart; files, camera, location, biometrics or other hardware; payments and permissions; accessibility and input modes; telemetry/support; build, signing, updates and distribution. For important capabilities, record the current owner, upstream/downstream dependencies, data classification, failure behavior, and migration consequence. Do not turn missing evidence into a negative capability claim.

For every consequential compatibility or policy claim, record the first-party source, exact page/section/API, platform and version, date checked, supported/limited behavior, and any test still needed. Prefer current official platform and standards documentation. Search only the destination versions and capabilities in scope. Trace copied summaries to the original source and count shared origins once. Treat search snippets and framework marketing matrices as leads, not proof.

## Y3. Compare migration paths against constraints

Consider only plausible options for the product: retain and adapt the current client; add a browser-installable or packaged web route; use a host/container for selected workflows; share a domain core with platform-specific clients; use a multi-target framework; or rebuild a target client natively. These are option classes, not defaults. For each, compare the user's criteria: workflow and platform fit, offline/data behavior, performance, accessibility, security/privacy, device integration, release rules, team skills, maintenance, transition risk and cost.

Separate code reuse from product parity. A shared component can still behave poorly with touch, keyboard, screen readers, window resizing or OS lifecycle. Reuse domain rules and stable contracts where the evidence supports it; adapt the interaction and state ownership to the destination. Do not choose a technology before the target capabilities and operating constraints are known.

Estimate work from the discovered workstreams: critical workflows, interfaces/integrations, target-specific capabilities, data and identity transition, test/release support, and the period when old and new clients coexist. Use repository evidence, historical delivery data supplied by the team, or measured spike results. Separate effort from calendar time and ongoing dual-run cost. When there is no reference class or prototype, give conditional ranges only if their assumptions can be stated; otherwise report the unknowns and the next sizing check. Explain confidence with its evidence, not an invented probability. Do not derive effort from screen counts or framework claims.

## Y4. Verify the riskiest assumption before committing

Choose one vertical workflow that exercises the hardest uncertain boundary—not a “hello world” screen. Define a small prototype or investigation that includes the actual API/auth path and relevant state, persistence, device capability, offline/retry, accessibility, performance or distribution constraint. Set observable acceptance criteria before the spike, such as state surviving process recreation, a deep link opening the correct record, old and new clients safely reading the same API version, data reconciliations matching, or a supported browser/OS completing the task with keyboard and assistive technology. Keep any production write or deployment outside a research spike unless separately authorized.

Make acceptance checks measurable from a supplied baseline: critical-task completion, auth/session continuity, API error and latency behavior, persisted or queued state after process/browser restart, and data invariants. For data transfer, select checks suited to the entity: source/target counts, key uniqueness, referential integrity, critical aggregate totals, and sampled field-level differences. Record exclusions and accepted transformations. Set tolerances with the product/data owner based on impact; do not invent a universal percentage. A matching row count alone does not establish matching data.

If the prototype fails, revise the option comparison before promising a schedule. If no running prototype is possible, name the unavailable evidence and keep estimates conditional. A feasibility report should distinguish documented support, repository facts, measured prototype results and unresolved assumptions.

## Y5. Plan safe coexistence and rollout

Create a phase table for each important entity or workflow: authoritative writer, readers, API/schema version, sync/conflict rule, validation check, and recovery path. Keep changes backward-compatible when possible; when a breaking API change is required, state how old clients are supported or retired. Assign one authoritative writer per entity and phase unless an explicit conflict-resolution design supports concurrent writes. Do not recommend dual writes without idempotency, retry/order semantics, reconciliation and a failure plan.

For a migration that needs staged rollout, make the table actionable. For each applicable phase—preflight, coexistence/canary, cutover and retirement—name the audience or traffic slice, current and target writer, validation evidence, stop threshold, decision owner and recovery action. Choose thresholds from existing service objectives, user impact and the supplied baseline; when none exist, propose a measurement and label its threshold as needing owner approval.

Define identity/session continuity, data migration direction, backups/exports, monitoring, support ownership, rollout cohorts and rollback limits. Distinguish traffic rollback from data rollback: after the new system accepts writes, routing users to the old client does not return those writes or make stale data current. Define the recovery path for new transactions (replay, reverse sync, restore, forward-fix or another evidenced strategy), the responsible decision owner, and the observable stop/rollback thresholds. Mark the point of no return, such as deleting old schemas or ending synchronization. Set launch gates for critical workflows, data correctness, accessibility, security/privacy, performance and the selected distribution channel. Publishing approval is separate from technical feasibility.

Phased migration can lower cutover risk when components can coexist and traffic or workflows can be routed safely; it adds transition complexity and dual-running cost. A complete replacement may be simpler for a small system, a hard platform boundary, or a required fast retirement. Compare both only when they are viable; do not make “incremental” or “rewrite” the automatic answer.

Deliver a short recommendation with: current-state inventory, target scope, capability matrix, compared options and decision criteria, proof-of-concept result or open check, phased plan and gates, data/rollback risks, and the evidence date. For a quick question, return only the smallest matrix and key decision. Keep unstated assumptions visible instead of inflating the report.

## Y6. Direction-specific checks

- **Web → mobile:** distinguish responsive web/PWA needs from store-distributed app needs. Check navigation and touch ergonomics, app links, device permissions, offline storage/sync, background limits, notification consent, and whether the web session/data model survives application lifecycle changes.
- **Android or iOS → web:** inspect browser API support for the required versions; redesign for URLs, refresh/back behavior, browser storage, multi-tab state, permissions, file/device APIs, offline caching and browser accessibility. Do not promise native background or hardware parity without evidence.
- **Web/mobile → desktop or macOS:** include keyboard and pointer behavior, window resizing and multi-window state, file/system integration, update/signing/distribution, sandbox and privacy boundaries. Distinguish a hosted web experience from a packaged desktop application and from a native macOS client.
- **Android ↔ Apple platforms, or desktop ↔ mobile:** preserve task outcomes and data contracts while validating each platform's navigation, lifecycle, interaction conventions, notifications and release requirements. Check whether local state, pending offline writes, account recovery and device permissions have equivalent owners and recovery paths. Similar screenshots do not prove equivalent behavior.

## Y7. Official starting points (recheck before use)

These are entry points, not a fixed compatibility verdict. Verify the exact current version and follow links to the relevant API or policy for the user's target:

- Android architecture and lifecycle: [Guide to app architecture](https://developer.android.com/topic/architecture) · [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
- Android local/network state and conflict handling: [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first)
- Apple platform differences: [App design and UI](https://developer.apple.com/documentation/technologyoverviews/app-design-and-ui) · [Interface fundamentals](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals) · [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
- Windows framework and distribution decisions: [Plan your Windows app](https://learn.microsoft.com/en-us/windows/apps/get-started/plan-your-app)
- API compatibility during client coexistence: [API design in Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/api-design)
- Incremental replacement and when it may not fit: [Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
- State-aware migration cutover and rollback: [AWS Prescriptive Guidance: Cutover stage](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html)
- Web feature support: [MDN compatibility tables and Browser Compatibility Data](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Page_structures/Compatibility_tables); open the relevant specification and browser-vendor documentation for the feature being evaluated.

Cloud-provider migration patterns are examples, not requirements for a client-platform migration. Apply them only when their assumptions (routing layer, data stores, ability to coexist, and rollback authority) match the system being studied.
