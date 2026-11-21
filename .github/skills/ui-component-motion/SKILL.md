---
name: ui-component-motion
description: >-
  Builds custom interactive web components and purposeful UI animations around a product workflow. Use for component behavior, microinteractions, state transitions and keyboard or reduced-motion equivalents.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.13.0"
  source: deep-research-domain-council
---

# Custom UI Components and Motion

For an existing component, take the Patch route in the design module. Start at its entry point with real data. For a new interaction, compare alternatives against the user's task and the conventions of adjacent controls.

1. Define the component's anatomy, inputs, owner of state, emitted events and recovery from a failed operation. Compose native controls or the project's accessible primitives. Give the product-specific work its own layout and behavior.
2. Build the useful static interaction first, wired to the real entry point. Drive visual, semantic and keyboard state from the same value. Keep focus predictable and preserve the user's input on retry.
3. For each meaningful transition choose its trigger, start and end, property, timing and interruption behavior. Author it with local CSS or the existing animation API. Make state correct immediately even if animation is disabled, cancelled or reversed halfway.
4. Try the primary task at narrow and wide widths. Test rapid reversal, keyboard-only operation, reduced motion and relevant empty/error states. Report the checks observed. A custom control earns its place when it makes a named task easier.

For worked components and interactive scenes, use F8. For a runnable UI, use the screenshot, overflow, keyboard and image checks in F9 before delivery.

Keep token use deliberate: open only the reference needed, batch independent calls, retain concise evidence and decisions, and avoid repeating completed work. Preserve required research, validation and user-requested detail.

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-f-web-design-deep-module.md` | Unified design module: Full/Patch, materials (F2.5), responsive charts (F3), states (F4), motion/canvas (F8), browser QA (F9) |
