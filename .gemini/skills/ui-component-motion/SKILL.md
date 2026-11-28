---
name: ui-component-motion
description: >-
  Builds custom interactive web components and purposeful UI animations around a product workflow. Use for component behavior, microinteractions, state transitions and keyboard or reduced-motion equivalents.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.33.1"
  source: deep-research-domain-council
---

# Custom UI Components and Motion

**Mandatory token policy.** Keep reusable instructions and tool definitions stable where you control the request. Append changing facts at the end. Reuse results already in context. Before another read or search, identify a changed input, missing fact or required check and fetch only that part. Batch independent checks. Never pad, warm up, or retry for a cache hit. Only host telemetry establishes cached usage.

For an existing component, take the Patch route in the design module. Start at its entry point with real data. For a new interaction, compare alternatives against the user's task and the conventions of adjacent controls.

1. Define the component's anatomy, inputs, owner of state, emitted events and recovery from a failed operation. Compose native controls or the project's accessible primitives. Give the product-specific work its own layout and behavior.
2. Build the useful static interaction first, wired to the real entry point. Drive visual, semantic and keyboard state from the same value. Keep focus predictable and preserve the user's input on retry.
3. For each meaningful transition choose its trigger, start and end, property, timing and interruption behavior. Author it with local CSS or the existing animation API. Make state correct immediately even if animation is disabled, cancelled or reversed halfway.
4. Try the primary task at narrow and wide widths. Test rapid reversal, keyboard-only operation, reduced motion and relevant empty/error states. Report the checks observed. A custom control earns its place when it makes a named task easier.

For worked components and interactive scenes, use F8. For a runnable UI, use the screenshot, overflow, keyboard and image checks in F9 before delivery.

Resolve vague follow-ups from the latest correction, relevant work and active constraints. Use a reversible assumption when safe. If blocked, finish independent items and ask only for the first decision-changing detail. Track every requested result, distinguish requirements from preferences and reuse shared evidence. Deliver the result first in the requested format, with decisive evidence and any material gap.

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-f-web-design-deep-module.md` | Design routes, materials (F2.5), responsive charts (F3), states (F4), motion/canvas (F8), browser QA (F9) |
| `references/part-u4-adaptive-layouts-and-translucent-surface.md` | Choose page regions, size a reusable component by its contents and measure contrast on glass |
