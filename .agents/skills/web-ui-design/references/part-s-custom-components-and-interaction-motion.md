# PART S — CUSTOM COMPONENTS AND INTERACTION MOTION

Use the user's workflow to choose what to build. Observe a real item with an unusually long name, an empty collection and a failed operation. Trace how a person finds the relevant item, acts, sees confirmation and recovers from a mistake. Preserve existing conventions that people rely on. Sketch another layout and compare the effort needed to complete that particular task.

**Worked component.** A technician scans a maintenance queue on a phone. Opening a detail page for each fault loses their place. An inline disclosure keeps the machine name and fault visible while exposing the repair notes. If the notes grow into a multi-step edit, a dedicated view can preserve input and offer a clear return to the same row.

| Design decision | Implementation and check |
|:---|:---|
| Anatomy and interface | Row receives the fault ID, machine name, notes and open state. Use a native disclosure or a labeled button with synchronized expanded state and controlled content. Use a stable ID per row. |
| Ownership | Keep the domain data in the parent. Represent expanded/collapsed once. If a request fails, keep the user's place and show retry by the affected row. |
| Motion | Rotate a disclosure indicator from 0 to 90 degrees on expansion. A local CSS transform transition (e.g. 140 ms ease-out) can reverse from its current position on a rapid second press. |
| Reduced motion | Keep the indicator's final orientation and reveal the notes immediately with transitions disabled. Never depend on an animation-end event to unlock the control. |
| Verification | Activate by keyboard twice before the transition finishes. Check focus, final expanded state, hidden content, wrapping and sibling rows. Repeat with reduced motion. |

With a native `details` element, the browser owns keyboard activation and the open state. The animation below affects only the indicator. The machine name remains accessible when the notes are hidden.

```html
<details class="fault-row">
  <summary>Press 04 · Hydraulic leak <span class="chevron" aria-hidden="true">▸</span></summary>
  <p>Inspect the return hose before restarting.</p>
</details>
```

```css
.fault-row > summary { list-style: none; }
.fault-row > summary::-webkit-details-marker { display: none; }
.fault-row .chevron { display: inline-block; }
.fault-row[open] > summary .chevron { transform: rotate(90deg); }
@media (prefers-reduced-motion: no-preference) {
  .fault-row > summary .chevron { transition: transform 140ms ease-out; }
}
```

Choose a pattern that matches the work. When a dispatcher reorders stops, keep the stop identity and focus as its position changes, with a keyboard action to move it. When a shopper adjusts a range, expose exact editable values as well as the drag interaction. In both cases the saved value and final position should agree after rapid input. Preserve the same information with motion reduced. [W3C guidance on animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
