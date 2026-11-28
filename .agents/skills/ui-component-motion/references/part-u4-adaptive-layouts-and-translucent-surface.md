## U4. Adaptive layouts and translucent surfaces

### Decide what belongs together

Start with a real question. For “Kiriman mana yang terlambat, dan apa langkah berikutnya?”, group the shipment, its status and its action. Align dates and amounts across rows when people compare shipments. A summary can sit beside the list when both need to stay in view. Use a single reading column for instructions followed in sequence. GOV.UK demonstrates a two-thirds main column with an optional one-third rail in public services. Try that proportion only when the secondary content helps the current decision. [GOV.UK layout examples](https://design-system.service.gov.uk/styles/layout/)

Sketch the narrow reading order first. Place prerequisite information before the action in the document. Align wide-screen regions to common edges, keep label/value spacing tighter than spacing between records, and spend spare width on the comparison or on whitespace. Follow the sequence once with Tab. CSS grid placement can move a control visually while its keyboard and reading positions still follow the document. [CSS Grid ordering and accessibility](https://www.w3.org/TR/css-grid-2/#order-accessibility)

### Let the component earn its breakpoint

For a shipment row, the parent owns the available width. The component owns the arrangement of its summary and action. Keep the ID, status text and primary action available in every placement. Let the title wrap, put optional metadata on a second line, and omit an absent thumbnail together with its reserved column. Keep one interactive element per action so focus and pending state survive a resize. Use flex wrapping for peer controls and grid tracks when two columns must align.

Worked estimate for the row below: allow 18rem for the summary using the actual localized text, 12rem for the action, 1rem between them and 2rem total inline padding. Try two columns at a **33rem container**. These are specimen dimensions. Recalculate for the project's font, padding and longest supported label. The query measures the unpadded host's content box. [MDN container size queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#using_container_size_queries)

```html
<div class="shipment-slot">
  <article class="shipment">
    <div>
      <h3>Pengiriman perlengkapan ruang pemeriksaan</h3>
      <p>INV-2048 · Terlambat · Rp 1.250.000.000</p>
    </div>
    <a href="/kiriman/2048">Lihat detail pengiriman</a>
  </article>
</div>
```

```css
.shipment-slot { container: shipment / inline-size; }
.shipment {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  padding: 1rem;
  gap: 1rem;
  align-items: start;
  overflow-wrap: anywhere;
}
.shipment > * { min-inline-size: 0; }
.shipment h3, .shipment p { margin: 0; }
.shipment p { margin-block-start: .5rem; }
.shipment a { justify-self: start; max-inline-size: 100%; }
@container shipment (min-width: 33rem) {
  .shipment { grid-template-columns: minmax(0, 1fr) 12rem; }
}
```

Resize the same instance in a drawer and in the main list on one desktop viewport. Check just below and above the switch with a three-line title, an unbroken ID and a missing optional field. Keep the full amount available. Use a full-width action in a narrow slot if the label needs it. In a long list, compare scanability against the cost of rows growing taller. For a comparison table that needs two axes, contain horizontal scrolling within the labeled table region. Ordinary vertical page content must reflow at the equivalent of 320 CSS px with its functions available. [WCAG reflow and exceptions](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

### Choose color by role and background

Use a quiet surface for the list, a named text/foreground pair for its values, and action color for the link. An overdue row can use a short “Terlambat” label and a status accent. If an entire row becomes saturated, compare whether finding exceptions becomes easier and whether the action is still identifiable. In each theme, resolve selected, hover, error and focus separately. Inspect the intersection of states such as a focused link inside a selected row. Keep status readable in grayscale. [Carbon color guidelines](https://www.carbondesignsystem.com/building-blocks/foundations/color/guidelines) · [WCAG use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

### Decide how much of the backdrop can show through

Use a frosted layer for the controls on a shipment map when seeing the route underneath helps orientation. Start dense records on an opaque surface. Give tint, foreground, edge and blur separate controls. The tint sets a floor under dark patches or a ceiling over bright ones. Blur softens changing detail but has no effect on a uniform field of color. Apply alpha to the fill so text and focus cues stay opaque. F2.5 contains the implementation, theme tokens and solid fallback. [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)

For example, take opaque ink `#202020` and a white overlay on a uniform black patch. In an ordinary 8-bit sRGB source-over calculation, 35% white gives about `#595959` and **2.33:1** text contrast. Raising the fill to 60% gives `#999999` and **5.72:1**. White behind the same overlay gives **16.29:1** in both cases. A white artboard alone would approve both designs. These are calculated examples. For the actual material, capture the area behind the label with only the text ink hidden and inspect the weakest patch at each crop, theme and scroll position. For gradients, include the transition under the text. [W3C alpha compositing §5.1](https://www.w3.org/TR/compositing-1/#simplealphacompositing) · [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

Check ordinary text at 4.5:1, large text at 3:1 and essential visual cues of active controls against adjacent colors at 3:1, subject to each criterion's exceptions. Check a focus ring against its surrounding pixels separately. If a map highlight or photo breaks the pair, move the label onto a local opaque backing or adjust the tint and measure again. When transparency is reduced or filtering is unavailable, the solid variant must retain labels and boundaries. Compare scrolling the same view with glass enabled and disabled on the target device before attributing a slowdown to blur. Record the affected panel size and observed frame times if performance affects the choice. [WCAG non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) · [Media Queries 5, reduced transparency](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-transparency)

### Verify the layout decision

In F9's render pass, also try the breakpoint ±1 CSS px and increased text size. Resize while the action has focus. Check its name, tab position, visible outline and access to the entire label. In a sticky toolbar, scroll to the last focusable item and verify it remains visible. For image-heavy cards, reserve the image's aspect ratio and compare the browser's selected image candidate and transfer size with the rendered slot at the same device pixel ratio. Correct an oversized `sizes` estimate before adding another layout breakpoint. Record the failing combination, the smallest change and the observed result. [WCAG focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) · [Responsive image selection](https://web.dev/learn/images/descriptive)
