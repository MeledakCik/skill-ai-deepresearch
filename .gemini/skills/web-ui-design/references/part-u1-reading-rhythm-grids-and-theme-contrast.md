## U1. Reading rhythm, grids and theme contrast

### Set one specimen before styling the page

Use the product's longest heading, a paragraph, a caption and a numeric value. For a Latin-script prototype, try size tokens of 12, 14, 16, 20, 24, 32, 48 and 64 CSS px at the default root size. Expose roles in rem. Try a 48 px display at 1.05 leading and −0.02em tracking, a 24 px section heading at 1.25, 16 px body at 1.5–1.7, and 14 px captions at about 1.4. Test tighter display tracking down to −0.04em or caption tracking up to +0.05em against the actual typeface. Widen leading if accents or two-line titles collide. Favor start alignment for prose and inspect word gaps before using justification.

As an exercise, set “Jadwal pengambilan”, “Ambil pesanan setelah pukul 14.00” and “Loket B · Lantai 2” in one family at one width. Make three specimens using size, weight and color alone. Give the time priority for someone checking when to leave, the location priority for someone already inside, and the heading priority for someone browsing a directory. Cover the title and check whether the remaining labels still answer the assigned question.

**What reading studies support.** In screen-reading experiments by Dyson and Kipping, participants preferred the 55-character lines. They read the 100-character lines faster than the 25-character ones, with similar comprehension. In a later experiment by Dyson and Haselgrove, 55-character lines yielded the best comprehension among the tested lengths. These experiments used particular texts, devices and tasks. Start extended prose near 55–75 characters and compare variants using comprehension, time or comfort according to the job. A CSS width of 65ch approximates 65 zero glyphs. Count a few rendered lines of the actual proportional typeface. [Dyson & Kipping, 1998](https://journals.uc.edu/index.php/vl/article/view/5671) · [Dyson & Haselgrove, 2001](https://doi.org/10.1006/ijhc.2001.0458)

**Accessibility check.** Apply the WCAG 2.2 SC 1.4.12 overrides together for supported writing systems: line height 1.5 times the font size, space after paragraphs 2em, letter spacing 0.12em and word spacing 0.16em. Inspect the filled form, error message and long heading for clipping or lost controls. These values test the page's tolerance of user overrides. Separately inspect reflow at 320 CSS px and record any scrolling region that genuinely needs two axes. [W3C text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) · [W3C reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

### Work out the grid and vertical rhythm

Pick shared space tokens such as 4, 8, 12, 16, 24, 32, 48, 64 and 96. Assign them jobs: 8 between label and value, 24 inside a group, 48 or 96 between sections. This makes it possible to change density consistently. Optical corrections and 1 px borders can have their own roles. Treat “60/30/10” as a sketch prompt for dominant, supporting and accent areas. Judge the result by what the user can compare, read or act on.

A 1440 px canvas with two 120 px margins leaves 1200 px. Eleven 24 px gutters use 264 px, so each of 12 columns gets 78 px. At 390 px, use two 16 px margins and three 16 px gutters for four columns of 77.5 px. Fractional track widths are normal. The following starting point expresses the two layouts without carrying desktop margins onto a phone. Put each block on a named region or an explicit span, then check a long label, the transition between layouts and 320 px. IBM Carbon is a useful counterexample to treating twelve columns as a requirement: its own grid starts with sixteen. [Carbon grid guidelines](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines)

```css
.layout {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  width: min(calc(100% - 2rem), 75rem);
  margin-inline: auto;
}
@media (min-width: 64rem) {
  .layout {
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 1.5rem;
  }
}
```

### Verify semantic colors on the surfaces that use them

Map a palette value to a semantic role and then to a component, for example `neutral-700 → text-secondary → table caption`. Map primary action, text on action, surface, border, focus, success, warning and error separately. In dark mode, try a near-black base, progressively lighter surfaces and a visible edge for overlays. Retain the role name and choose a value for the new background. Pair status hues with text or shape. Carbon documents this role-to-theme mapping in its own system. [Carbon color and layering](https://www.carbondesignsystem.com/building-blocks/foundations/color/overview)

| Example pair for ordinary text | WCAG contrast, displayed approximately | Design decision |
|:---|---:|:---|
| #777777 on #FFFFFF | 4.478:1 | Below the 4.5:1 AA threshold. Rounding the displayed number would hide the failure. |
| #595959 on #FFFFFF | 7.005:1 | Suitable for the light caption in this pair. |
| #595959 on #121212 | 2.674:1 | Reusing the same foreground fails on the dark surface. |
| #B8C2CC on #121212 | 10.372:1 | Remap the dark caption to this lighter foreground. |

Calculate relative luminance from the final sRGB pair and compare the unrounded ratio with the threshold. Ordinary text requires 4.5:1 and large text 3:1 under SC 1.4.3, subject to its exceptions. Required visual cues for an enabled control or its state generally need 3:1 against adjacent colors under SC 1.4.11. Sample composited backgrounds when overlays or opacity are involved. Record the token, theme, state, foreground and adjacent surface. These checks establish the pairs tested. An outdoor legibility claim would also need observation on the device in that light. [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
