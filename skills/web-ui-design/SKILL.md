---
name: web-ui-design
description: >-
  Designs product UIs and adapts supplied screenshots across mobile and desktop. Use for screenshot-to-UI work, visual research, typography, grids, themes, component states, charts, usability and web performance.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.32.0"
  source: deep-research-domain-council
---

# Web & Product UI Design

**Mandatory token policy.** Keep reusable instructions and tool definitions stable where you control the request. Append changing facts at the end. Reuse results already in context. Before another read or search, identify a changed input, missing fact or required check and fetch only that part. Batch independent checks. Never pad, warm up, or retry for a cache hit. Only host telemetry establishes cached usage.

## Choose Transform, Full or Patch

**Transform** when the user asks to reproduce or adapt a supplied UI image. Open U5. Inspect the image, identify its component groups, alignment, color roles and current state. Compare the source-sized render first. For another width, retain the task, selection, draft and actions. Test the layout in its actual slot and resize back. An inspiration image for an original design belongs in Full.

**Full** for a new design or redesign. Research the audience and task, gather real content, annotate references and sketch three grayscale directions in F1. Select one by walking through a difficult case. Build the flow and its recovery path with shared tokens and components (F2–F8).

**Patch** for a local UI issue. Reproduce it. Use F2/F4/F6/F9 for tokens, states, accessibility and verification. For layout, component sizing or contrast over glass, use U4's shipment example. Use F3 for charts and F8 for motion or a canvas scene.

For a concept, walk the sketches. For a runnable implementation with browser access, complete F9's desktop/mobile × light/dark screenshot loop, inspect actual pixels, page overflow, focus and images, and recheck any fixes. Report the evidence and any pending checks.

For an advanced or research-led brief, isolate the decision with the biggest consequence. Look up the relevant standard, original study or first-party design pattern, record its scope, and test a plausible alternative on the actual task. Report what the source established, what you chose and what you observed. Open just the applicable guide below.

Resolve vague follow-ups from the latest correction, relevant work and active constraints. Use a reversible assumption when safe. If blocked, finish independent items and ask only for the first decision-changing detail. Track every requested result, distinguish requirements from preferences and reuse shared evidence. Deliver the result first in the requested format, with decisive evidence and any material gap.

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-f-web-design-deep-module.md` | Design routes, materials (F2.5), responsive charts (F3), states (F4), motion/canvas (F8), browser QA (F9) |
| `references/part-u1-reading-rhythm-grids-and-theme-contrast.md` | Tune type, measure, responsive grid and theme tokens with worked accessibility checks |
| `references/part-u2-visual-hierarchy-and-task-research.md` | Research a hierarchy decision, study reference designs and run a recall or task test |
| `references/part-u3-dashboard-judgments-and-component-states.md` | Choose a dashboard encoding, verify partial totals and exercise async component states |
| `references/part-u4-adaptive-layouts-and-translucent-surface.md` | Choose page regions, size a reusable component by its contents and measure contrast on glass |
| `references/part-u5-screenshot-to-responsive-layout.md` | Read a supplied UI image and preserve its hierarchy, colors, components and task across widths |
| `references/part-g-natural-writing.md` | Natural writing patterns and rewrite example |
