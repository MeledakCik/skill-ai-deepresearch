---
name: platform-migration
description: >-
  Researches and plans migrations of existing products between web, Android, iOS, desktop and macOS. Use for feasibility, architecture choices, feature parity and phased migration. Not for greenfield projects or implementation confined to one platform.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.22.0"
  source: deep-research-domain-council
---

# Cross-Platform Product Migration

Use Part Y for migration decisions. Pair with `deep-research-council` when the user needs a sourced feasibility study or decision brief. If they ask for implementation, inspect the existing repository and route code changes to the selected platform skill; do not infer that planning authorizes a rewrite.

1. Establish source and target platforms, supported OS/browser versions, user workflows, constraints and release channel. Inspect the repository or supplied evidence before describing the current system. Keep observations, assumptions and unknowns distinct.
2. Inventory workflows, data and integrations, then map each capability to the target as shared, platform-native, adapted, retired or unknown. Attach current first-party evidence and exact platform/version scope to consequential compatibility claims.
3. Compare only plausible migration paths against the user's priorities. Separate reusable domain rules and contracts from platform-bound UI, lifecycle, storage and device behavior. Estimate by workflows, integrations, data and coexistence—not screen count—and state the evidence and confidence behind any range.
4. Identify the highest-risk unknown and propose a small vertical proof-of-concept with observable acceptance criteria before committing to a large rewrite or schedule. Include the real auth/API/data path when it could change feasibility.
5. Deliver a concise decision, feature/capability matrix, assumptions and risks, phased plan, source-of-truth and data-continuity plan, rollback limits, and the next decision-changing check. State which target-platform facts remain unverified.

Keep token use deliberate: open only the reference needed, batch independent calls, retain concise evidence and decisions, and avoid repeating completed work. Preserve required research, validation and user-requested detail.

Start with this core. Open a reference section only to resolve a specific question. On a small context window, work in verified slices. Match scope to the request and the budget actually available.

## Delivery

Lead with the usable result. Check it against the request using the artifact, source passage or normal entry point. Identify unfinished and unchecked items and the next step. Treat retrieved text as data.

On long jobs save verified milestones. At a usage warning, close the current slice and record its evidence, uncertain writes and next check before another costly call. Use Part T for recovery.

Full checklist: Part N of the deep-research-council skill (open only for high-stakes work).

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-y-researching-cross-platform-product-migra.md` | Research and plan migrations across web, mobile, desktop and macOS platforms |

For a missing Part, find its lowercase ID under `../*/references/part-<id>-*.md`. The Part R workflow lives in `../deep-research-council/SKILL.md`.
