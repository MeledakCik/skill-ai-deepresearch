# PART F — WEB & DESIGN DEEP MODULE

**Full.** For a new screen, product or redesign, start at F1. Research the audience and content, sketch three grayscale directions, select one, and build its complete flow. Use F9 before delivery.

**Patch.** For a single component, CSS bug or localized interaction, reproduce it at its normal entry point. Go directly to F2 (tokens), F4 (behavior), F6 (accessibility) and F9 (rendered verification). Add F3 for a layout/data issue or F8 for motion. Keep the surrounding product conventions.

**Find the right section.** F0 critique · F1 discovery · F2 tokens and materials · F3 layout and information design · F4 interaction states · F5 copy and assets · F6 accessibility · F7 performance · F8 motion and canvas · F9 delivery. Focused research U1–U3 offers deeper evidence on type/themes, hierarchy/usability and dashboards.

## F0. Visual direction and design critique

Cover the logo and read the first action. Could the same copy, assets and structure sell an unrelated product? Replace unsupported proof with real content or labeled fixtures. Remove badges, icon cards and effects that obscure the decision. Derive contrast from F2, semantics from F6, motion from F8 and delivery checks from F9.

The former C3 filter draws on `miqdadbadjuber/anti-slop`. Pick a reference for a concrete reason: Carbon for comparable records, Fluent for an operator workspace, Apple HIG for platform interaction, Material for an adaptive Android screen. Editorial, spatial-hardware, telemetry and archival directions are useful when the product content supports them. Use color, radius, pacing and illustration in service of that choice. In a visual instrument, MOTION 3 can justify a manipulable scene with F8's accessible controls. [Carbon](https://carbondesignsystem.com/) · [Fluent 2](https://fluent2.microsoft.design/) · [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) · [Material](https://m3.material.io/)

## F1. Research, moodboard and three grayscale directions

For a new design, write down who arrives, from where, which decision is difficult and what success looks like. Inspect the product's actual copy, data and constraints. Walk the same task in a competitor or analogue when available. Record one observed strength and one point of friction. Distinguish direct observations from assumptions. For a narrow correction, work from the existing product and its conventions.

Build a small moodboard before opening a polished canvas. Use the user's own assets, a real interface from the domain and a visual reference suited to the audience. Behance, Awwwards, Pinterest and Dribbble can help locate work. Trace a promising image to the original project where possible. For each reference keep its source, the specific design decision worth studying, and how that decision would help this audience. When working offline, use supplied materials or an explicitly proposed direction. Credit only references actually inspected.

Sketch three grayscale compositions with the **same copy, data and primary task**. Change the order of decisions, grouping or use of space. On paper, in Figma or in a lightweight coded wireframe, make the key labels legible. Compare where the eye lands, what information the user needs to remember and how they recover. Select one, put difficult content through it, and revise the weakest point. A process handoff can fit in one strip showing the three sketches, the selection reason and the resulting revision.

**Worked decision.** A rider knows their destination but has flexible dates. Explore a destination search above departures, a date picker above routes, and a departures list with filters. The first direction matches what the rider already knows. Try a fully booked departure. Move “Lihat keberangkatan berikutnya” next to that departure and retain the destination. The revision answers a failure discovered in the chosen flow. It also gives a reviewer something concrete to test.

## F2. Design Tokens (The Foundation)

### F2.1 Typography

- **Choose a typeface for a reason**: editorial (serif for long reading: Source Serif, Literata, Newsreader), technical (grotesk + mono: IBM Plex, Geist, JetBrains Mono), friendly (humanist: Nunito Sans, Figtree), institutional (Public Sans). State the reason in one line.
- **Max two families** (one + mono is usually enough).
- **Modular scale:** pick a ratio and stop improvising. 1.125 (dense apps), 1.2 (product UI), 1.25 (marketing), 1.333 (editorial).
- **Fluid type** with `clamp()` so headings scale between breakpoints without jumps.
- Start long-form copy around 55–75 characters per line where space permits. Try body leading of 1.5–1.7 and inspect multiline headings and diacritics. Part U1 gives the supporting studies and a text-spacing override test.
- **Weight hierarchy over size inflation:** 400 body, 500-600 UI labels, 600-700 headings. Avoid 800-900 except display.
- Numerals in tables: `font-variant-numeric: tabular-nums;`.

Start by setting one real headline, a paragraph, a long name and a caption together. A practical starting scale in CSS pixels is H1 36/42 on phones and 48/54 on wide layouts, H2 24/30, body 16/24, caption 14/20 (size/line height). Express sizes in rem in code and map them to named text styles in Figma. One family can cover every role. Add a display face only if it gives the title a useful voice alongside the quieter body. For example, try Instrument Serif for an exhibition title and Source Sans 3 for opening hours and directions. For a dense departures table, one functional sans with distinguishable digits suffices. Check wrapping, weight, tracking and spacing around headings at actual widths and at text zoom. Rounded type, tight bold headings and gradient text used together can obscure the reading order.

### F2.2 Color

- Build in **OKLCH** for perceptually even ramps: same L across hues means same perceived lightness.
- **Neutral ramp (10-12 steps)** does most of the work: background, surface, border, muted text, text. Tint neutrals slightly toward the brand hue (chroma 0.005-0.02) so gray does not feel dead.
- **One brand hue**, used for primary action and key highlights only. Plus semantic colors: success, warning, danger, info.
- Start with one primary color, one accent role and a neutral family. The primary hue can also fill the accent role. Put the strongest contrast at the current decision. Add status colors only for meaningful states and pair them with text or a symbol. If a gradient or glass surface has no job in the content, simplify it to a solid surface.
- Inspect actual foreground/background pairs, including labels over the brightest part of a photograph. Ordinary text needs at least 4.5:1, large text 3:1, and visual cues required to identify active controls or their states generally need 3:1 against adjacent colors. Check focus, hover and errors as well as the default view. [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- **Dark mode**: not inverted. Background around L 0.15-0.20, elevated surfaces get *lighter*, reduce accent chroma, re-test contrast.

### F2.3 Space, Size, Radius, Shadow

- Start with shared spacing steps such as 8, 16, 24, 32 and 48. Give dense controls a small inset token if needed. A repeated 17 px gap in one screen and 13 px in the next is a signal to compare their roles and consolidate.
- **Proximity rule:** space inside a group < space between groups. If everything has 24 px gaps, nothing is grouped.
- **Radius hierarchy:** nested radius = outer radius − padding. Pick one personality: sharp (0-4), soft (6-10), round (12-16). Pills only for tags/toggles.
- **Elevation:** at most 3 shadow levels; shadows are tinted with the background hue, low opacity, with a tight + soft layer combination. In dark mode, use lighter surfaces instead of shadows.
- Use one icon family with consistent view box, stroke and optical size. Reuse named roles for field radius, primary button shape, focus ring and overlay elevation. Test the same action on two screens. Changing its shared style once should update both instances.

### F2.4 Token Example (copy and adapt; values are a starting point)

```css
:root {
  /* why: one hue, neutrals tinted toward it so grays don't feel dead */
  --hue: 250;
  --bg:        oklch(0.985 0.004 var(--hue));
  --surface:   oklch(1     0     0);
  --surface-2: oklch(0.965 0.006 var(--hue));
  --border:    oklch(0.90  0.008 var(--hue));
  --text-2:    oklch(0.48  0.015 var(--hue));
  --text:      oklch(0.22  0.02  var(--hue));
  --accent:    oklch(0.55  0.16  var(--hue));
  --accent-fg: oklch(0.99  0     0);
  --danger:    oklch(0.55  0.19  25);
  --success:   oklch(0.58  0.13  150);

  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;

  /* why: 1.25 scale, fluid between 360px and 1440px viewports */
  --step--1: clamp(0.80rem, 0.78rem + 0.10vw, 0.875rem);
  --step-0:  clamp(1.00rem, 0.96rem + 0.20vw, 1.125rem);
  --step-1:  clamp(1.25rem, 1.17rem + 0.40vw, 1.50rem);
  --step-2:  clamp(1.56rem, 1.42rem + 0.70vw, 2.00rem);
  --step-3:  clamp(1.95rem, 1.70rem + 1.20vw, 2.75rem);
  --step-4:  clamp(2.44rem, 2.00rem + 2.00vw, 3.75rem);

  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px; --space-9: 96px;

  --radius-sm: 6px; --radius-md: 10px; --radius-lg: 14px;
  --shadow-1: 0 1px 2px oklch(0.2 0.02 var(--hue) / 0.06), 0 1px 1px oklch(0.2 0.02 var(--hue) / 0.04);
  --shadow-2: 0 4px 12px oklch(0.2 0.02 var(--hue) / 0.08), 0 1px 3px oklch(0.2 0.02 var(--hue) / 0.06);
  --ease-out: cubic-bezier(0.2, 0.8, 0.2, 1);
  --dur-1: 120ms; --dur-2: 200ms; --dur-3: 320ms;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg:        oklch(0.17 0.01 var(--hue));
    --surface:   oklch(0.21 0.012 var(--hue));
    --surface-2: oklch(0.25 0.014 var(--hue));
    --border:    oklch(0.32 0.014 var(--hue));
    --text-2:    oklch(0.72 0.012 var(--hue));
    --text:      oklch(0.94 0.008 var(--hue));
    --accent:    oklch(0.72 0.12 var(--hue)); /* why: lighter, less chroma on dark */
    --accent-fg: oklch(0.18 0.02 var(--hue));
  }
}

```

### F2.5 Gradient and frosted surfaces

Choose the information the surface carries. A directional tint can connect a title to a product view. Frosted glass can keep a toolbar visible while revealing the scene it controls. Keep dense forms and charts on solid reading surfaces. To adapt a palette board, pick the dominant hue, the lightness range and the intended text color. Then choose a gradient axis and stop positions for the actual crop. The supplied Pinterest board collects color-scheme ideas. Color Hunt also indexes a gradient collection; its individual swatches were unavailable during review. [Pinterest gradient board](https://id.pinterest.com/zaaazzzaaaa/kode-gradasi-warna/) · [Color Hunt collection](https://colorhunt.co/palettes/gradient) · [web.dev gradient mechanics](https://web.dev/learn/css/gradients?hl=id)

**Two original recipes.** For a coastal itinerary, try ink blue → petrol → teal (`#102C43`, `#135064`, `#176760`) with white text on the quieter end. For an exhibition invitation, try a paper → apricot → rose wash (`#FFF6E8`, `#F1D2AC`, `#DEAAB0`) with ink text `#272128`. Mark the subject and text zones on both crops first. A linear gradient gives an axis, a radial gradient can put a localized light behind a subject. Move the middle stop to make room for the title. Sample the brightest, darkest and intermediate rendered pixels behind the actual text, including when the layout reflows. A contrast check at just the endpoints can miss a failing strip.

In a Chromium fixture at 390 and 1440 CSS px, the lowest contrast behind three label rectangles was 6.75:1 for the cool recipe and 7.91:1 for the warm one at the same stop positions. A control with navy ends and a white middle dropped to 1.00:1 under the central white label. Repeat the measurement after changing placement, palette or crop.

The Pinterest glass collection and Vecteezy photos are material references. Look for what stays visible through a surface and where a highlight defines its edge. Dribbble includes refracted artwork as well as frosted cards. In Shashikanth Kapikad’s card study, the published palette spans near-black, saturated blue and red. For a toolbar over a changing scene, carry over the edge and tint, then choose the panel opacity independently against the content underneath. Keep reeded distortion in the artwork, clear of labels and focus rings. [Pinterest glass collection](https://id.pinterest.com/ideas/glass-effect-gradient-backgrounds/930020598575/) · [Vecteezy glass photos](https://www.vecteezy.com/free-photos/glass-gradient) · [Dribbble glass collection](https://dribbble.com/search/glass-gradient) · [Kapikad’s original study](https://dribbble.com/shots/15759398-Rainy-Frosted-Glass-Glassmorphism-Card-Design)

```css
.scene {
  background-color: #102c43;
  background-image: linear-gradient(115deg, #102c43 0%, #135064 58%, #176760 100%);
}
.scene-tools {
  --panel: #f5f8fa;
  --wash: rgb(245 248 250 / 92%);
  --ink: #172833;
  --edge: #74818a;
  color: var(--ink);
  background: var(--panel);
  border: 1px solid var(--edge);
}
@media (prefers-color-scheme: dark) {
  .scene-tools {
    --panel: #192a34;
    --wash: rgb(25 42 52 / 92%);
    --ink: #f3f7f9;
    --edge: #8998a1;
  }
}
@supports (backdrop-filter: blur(1px)) {
  .scene-tools { background: var(--wash); backdrop-filter: blur(12px); }
}
@media (prefers-reduced-transparency: reduce), (forced-colors: active) {
  .scene-tools { background: var(--panel); backdrop-filter: none; }
}
```

Match the theme selector to the host app when it offers its own switch. Blur the backdrop of a bounded panel. Applying `opacity` or `filter: blur()` to the whole panel also affects its contents. Move the panel over a bright highlight, a dark patch and moving detail. For a contrast measurement, capture the crop again with only the ink hidden and sample the composed background beneath the glyphs. Compare the intended ink with the worst sample before rounding. Repeat with the solid panel and check keyboard focus separately. If scrolling or orbiting stutters on the target device, reduce the affected area or use the opaque surface. [Backdrop filter specification](https://drafts.csswg.org/filter-effects-2/#BackdropFilterProperty) · [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · [MDN reduced transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency)

## F3. Layout & Composition

- A 12/8/4 grid can align several page regions. For a single reading task, start with one measured column. Add a rail only when its contents support the task and both regions have room. U4 shows how to derive the switch from content.
- Use position, scale, weight and contrast to signal the next decision. Test the resulting reading order on a real task (U2).
- Give each section one focal point. On a 12-column landing layout, try a copy block across five columns and a product view across six with one column of breathing room. Align the next section to one of those same edges. On a phone, keep the meaningful reading order when the blocks stack.
- Put extra space around changes of topic and less between a label and its value. An empty column can separate decisions. Remove ornaments one at a time and keep the space if the task is as clear or clearer. Data-heavy work may benefit from compact rows. Choose density by what people need to compare.
- Align reading text to its starting edge. Centering can suit a short invitation. Compare the ragged edge and line breaks of a full paragraph at mobile width before centering it.
- **Above the fold** answers "what is this and is it for me", not "how beautiful are we".
- **Show the product.** Real UI screenshots (with real-looking data you are allowed to show) beat illustrations nearly every time for software.

### F3.1 Section Patterns That Don't Read as Template

| Instead of | Try |
|:---|:---|
| Hero + 3 icon cards | Hero with a live demo, a real input, or a single annotated screenshot |
| "Features" grid | A walkthrough of one real task, step by step, with screenshots |
| Testimonial carousel | One specific case: who, problem, number before/after, quote with name and role (real only) |
| Generic pricing with "Most popular" ribbon | Pricing table that states limits honestly and answers "what happens if I exceed" |
| FAQ of filler | The 5 questions support actually receives |
| Footer link farm | Footer with what people actually look for: docs, status, pricing, contact, legal |

### F3.2 Choose a layout for the surface

| Surface | First view and progression | Test the decision |
|:---|:---|:---|
| Landing page | Give the audience a specific outcome, a relevant product screenshot or other substantiated proof, and a next action. Order the scroll by the visitor's uncertainties, such as problem, demonstration, evidence, price or terms, then action. | At phone width, can someone identify the offer, who it serves and how to try it? If the actual evidence is a screenshot, crop it to the task at a readable size. |
| Mobile app | Give the screen one primary task. Put frequent actions within thumb reach, use familiar bottom navigation for peer destinations, and reserve sheets for short contextual choices. Respect the keyboard and safe-area inset. | Can someone finish with one hand, correct an entry with the keyboard visible, go back and find their input intact? A sticky action must leave the last field reachable. |
| Desktop dashboard | Start with the operator's question and the data that answers it. Keep navigation and filters stable. A 2–3 column workspace can show navigation, a sortable list and the selected item's details. Use shared table headers, comparable units, right-aligned amounts and dates. | Can someone scan for an exception, compare two rows, open details, act, then return to the same filter and position? Add a chart only if the time series or comparison answers an actual question. |

### F3.3 Information design

| Decision | Chart and interpretation |
|:---|:---|
| When did a metric change? | Time-ordered line. Show gaps for missing observations, mark unit and time interval and label each series at its last visible point. If zooming a line's axis, make its bounds and scope explicit. |
| Which category ranks highest? | Sort horizontal bars from a common zero. Place value labels beside bar ends. Preserve ties, show negative bars across zero and keep missing observations distinct from a measured zero. |
| How do a few parts compose a whole? | Use a 100% stacked bar for exhaustive nonnegative shares of one stated denominator. Label the segments directly. When small segments collide, use adjacent callouts or aligned bars. |

Pick hues distinguishable under common color-vision deficiencies. For lines, also vary dash or marker. Reserve one accent for the decision. Remove decorative fills, gradients and rainbow ordering from quantitative marks whose length, position or color already carries meaning. Give the chart a descriptive heading and a short takeaway. Provide a reachable, semantic HTML table with a caption, row/column headers, units and all plotted values synchronized to the current filter. Check it with keyboard and assistive technology where available. Part U3 works through incomplete revenue data. [UK Analysis Function chart guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) · [W3C complex images](https://www.w3.org/WAI/tutorials/images/complex/) · [W3C use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

### F3.4 Component stress tests

At one viewport, mount the same component in a narrow sidebar and in the wide main area. Try “Jadwalkan pengiriman berikutnya”, a three-line title, a missing image, zero results and “Rp 1.250.000.000”. Compare actual localized strings. Allow headings and actions to wrap, keep currency associated with its value and preserve the full amount for comparison. An inline-size query belongs on an ancestor. Choose the cutoff where that component's real content fits. The one-column base below also works when container queries are unavailable. [MDN container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)

```css
.payment-slot { container: payment / inline-size; }
.payment-row { display: grid; gap: .5rem; }
.payment-row > * { min-inline-size: 0; }
@container payment (min-width: 32rem) {
  .payment-row { grid-template-columns: minmax(0, 1fr) auto; align-items: baseline; }
}
```

Choose the mobile table treatment by task. For reading one record, stack labeled fields, preserving their header associations and row actions. For comparing many values across the same rows, keep a table in a labeled local horizontal scroll region with a visible scroll hint and keyboard access. Pin the identifier column only when it leaves enough room to read a value and its header. Test sticky-column overlap and focus while scrolled. The page itself should still reflow.

## F4. Components (Behavior Matters More Than Looks)

- **Buttons.** Use a verb and object. Give a frequent touch action a comfortable hit area, for example 44 × 44 CSS px. Keep its width and accessible name stable during submission. Explain blocked actions in nearby visible text. A disabled control cannot reliably expose a hover tooltip to a keyboard or touch user.
- **Forms:** labels above inputs (not placeholder-as-label); inline validation on blur, not on every keystroke; error text says how to fix ("Use at least 8 characters"), not just "Invalid"; preserve input on error; group related fields; mark optional, not required, when most are required.
- **Tables:** left-align text, right-align numbers, tabular numerals, sticky header for long tables, sortable columns show sort state, row density toggle for power users, empty state with next action.
- **Navigation:** ≤7 top-level items; current location always visible; search for >30 pages.
- **Feedback:** every action gets a response within 100 ms (visual) and a result or progress indicator within 1 s; optimistic UI with undo beats confirmation dialogs for reversible actions.
- **Empty states:** explain what will appear here and the single action that fills it.
- **Errors:** human language, cause, fix, and a way out. Never a raw stack trace.

Map the entry point, the action and the destination before drawing screens. First use, an empty filtered result, and failure to fetch require different next actions. For example, first arrival → load daftar pesanan → “Belum ada pesanan” → “Buat pesanan” → edit → submit → receipt. Branch a failed save back to the populated form with “Coba simpan lagi”. A successful empty search offers “Hapus filter”. A failed fetch keeps the filter and offers “Muat ulang”. Preserve scroll and selection when returning from detail.

| Reusable component | Variants and behavior to exercise |
|:---|:---|
| Button and input | Button supports default, hover, focus-visible, pressed, disabled and loading. Input covers empty, filled, focused, invalid and confirmed when meaningful. Keep label, help and error associated with the field. |
| Card or list row and dropdown | A row exposes its main action and selection separately. Use a native select for simple choices. For a custom popup, verify keyboard selection, Escape and return of focus. |
| Modal, sheet and toast | Keep focus within an open modal and return it to the trigger on close. A toast can acknowledge success. Put failures needing action in a persistent place close to the affected item. |

In Figma, keep real text and image layers editable. Define component properties such as label, emphasis and state, and compose instances in auto layout. Connect prototype variants so the reviewer can complete the success and failure paths. In code, map these same properties to shared components with one source of state. Try replacing a short label with “Jadwalkan pengiriman berikutnya” in two instances and check reflow.

### F4.1 Leaving, undoing and revealing work

- Track changes against the last saved value. A clean form or a successful save can leave immediately. For a dirty form, “Lanjut mengedit” keeps draft and focus, “Buang perubahan” discards only after the user chooses it. If saving fails, keep the draft dirty. Guard in-app navigation and Back. Use a browser unload warning only while dirty where supported; persist a draft if interruption would otherwise lose valuable input.
- For a reversible archive, show which item moved and offer keyboard-accessible “Urungkan” with enough time or a persistent recovery location. For a permanent, high-impact operation, show the exact item and consequence first. Typing the item name can be appropriate before irreversible bulk deletion. Disable duplicate submissions and handle a failed delete on the item.
- Match a first-load skeleton to the final image aspect ratio, table columns, row heights and text lines at each breakpoint. Reserve its space, then swap in the real data and inspect the layout-shift trace. During refresh keep existing data and timestamp visible.
- In a long form, show the frequent fields first and disclose advanced settings on demand. Keep expanded values when collapsing. A validation error inside a closed group must reveal the group, identify the field and restore an actionable focus target.

## F5. Copywriting for Interfaces (Natural, Not Generated)

- Write like a knowledgeable colleague explaining to a busy peer.
- **Specific > clever.** "Sync 3 calendars, see conflicts before they happen" beats "Your time, reimagined".
- **Verbs and nouns carry meaning; adjectives are suspicious.** Delete "powerful", "seamless", "robust", "innovative", "cutting-edge", "next-gen", "revolutionary", "effortless", "unlock", "elevate", "supercharge", "empower", "leverage", "harness", "in today's fast-paced world".
- Headline = the outcome; subhead = how; CTA = the next concrete step.
- Sentence-case headings, not Title Case Everywhere.
- Numbers must be real and sourced; otherwise remove the claim.
- Indonesian copy: use natural register (baku but not stiff); avoid literal translations like "Buka kekuatan…"; prefer "Kirim faktur dalam satu klik".

For an Indonesian workshop, “Pilih jam servis motor” names the task and “Lihat jam tersedia” states what the button opens. On a conflict, offer “Pilih jam lain” only if another slot is available. If all slots are full, retain the entry and offer another date or a refresh that actually works. “Kapasitas 8 peserta per sesi” describes capacity. “Tersisa 2 tempat” requires current availability. Read the headline, button and confirmation together to check that they describe the same promise. Remove generic copy like “Discover the Future”.

### F5.1 Local content and art direction

Use approved product content first. For a concept, label fixtures as **data contoh**. “Muhammad Kasyaf”, “Rp 149.000” and a long multi-part name can exercise localization and wrapping. A chart fixture should have an explicit unit and period. Include flat or falling values, zero and missing data when relevant. Keep missing data distinct from zero. Never present sample customers, prices, metrics, avatars or quotes as proof. A stock portrait can illustrate a context, while an actual testimonial requires its real, authorized attribution.

Pick the image by what the user needs to learn. A screenshot can show where to find a refund. A real photo can show the entrance to a clinic. Look first in the approved product library, then at suitable licensed stock such as Unsplash or Pexels. Confirm the specific asset can be used as intended and keep its source with production notes. Set a common light direction, color temperature, perspective, crop and focal subject across the series. Preview both wide and narrow crops. When a photo adds no information, leave the space clear.

If an original bitmap is necessary, generate one isolated element and compose it with real text and controls. Inspect fingers, eyes, lettering, reflections, contacts with surfaces, skin texture and excessive blur at delivery size. Replace a flawed asset or use a tighter crop only if the crop still communicates the intended subject. Use meaningful alt text for informative images.

## F6. Accessibility (Hard Requirements)

- Semantic HTML first (`header`, `nav`, `main`, `section` with headings, `button` for actions, `a` for navigation). ARIA only when HTML can't express it.
- Logical heading order (one `h1`, no skipped levels).
- Full keyboard operation, visible `:focus-visible` ring ≥3:1 contrast, no keyboard traps, skip-to-content link.
- Images: meaningful `alt`; decorative `alt=""`.
- Forms: `<label for>`, `aria-describedby` for help/error text, error summary on submit.
- Motion respects `prefers-reduced-motion`; nothing flashes >3 times/second.
- Check text resizing to 200%. For horizontal writing, test reflow at 320 CSS px. Keep two-dimensional content that needs both axes, such as a wide comparison table, within its own scrollable region. [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Test: keyboard-only run, screen reader spot check (NVDA/VoiceOver), automated axe/Lighthouse (automation catches only part of the issues; manual checks are required).

## F7. Web Performance (Measured, Not Claimed)

**Core Web Vitals "good" thresholds (75th percentile of real users):** LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1.

| Lever | Practice |
|:---|:---|
| LCP | Hero image preloaded or `fetchpriority="high"`, sized, modern format (AVIF/WebP), served from CDN; no client-side-only rendering of the hero |
| CLS | Explicit `width`/`height` or `aspect-ratio` on media; reserve space for ads/embeds; `font-display: swap` + `size-adjust` fallback metrics |
| INP | Keep main-thread tasks <50 ms; split long tasks; defer non-critical JS; avoid heavy hydration of static content (islands / server components) |
| Fonts | Subset, self-host, 1-2 families, `woff2`, preload only the one used above the fold |
| JS budget | Ship the minimum; audit bundles; remove unused libraries (date libs, icon packs imported whole) |
| Images | `srcset` + `sizes`, lazy-load below fold (`loading="lazy"`), never lazy-load the LCP image |
| CSS | Critical CSS inline for above-the-fold; avoid giant utility bundles without purge |
| Caching | Immutable hashed assets with long cache; HTML short cache; CDN edge |

Measure with field data (CrUX / RUM) when available, lab data (Lighthouse, WebPageTest) otherwise. Report the numbers, device class and network profile.

## F8. Motion With Purpose

- Motion explains **change**: where something came from, where it went, what changed state.
- Give a press immediate feedback, reserve the shape of known content during a wait, and mark a confirmed save with a quiet check and status text. Keep layout stable across navigation. In reduced motion, show the same final state and announce meaningful status changes. An empty screen and a skeleton signal different things.
- Durations: micro-interactions 100-200 ms, panels/modals 200-320 ms, page transitions ≤400 ms. Exits faster than entrances.
- Ease-out for entering, ease-in for leaving; springs for direct manipulation (C5 RK4).
- Animate `transform` and `opacity` only (compositor-friendly); avoid animating layout properties.
- MOTION dial 1 = hover/focus only; 2 = + subtle reveal on first view (once, not every scroll); 3 = physics/canvas, only when the product is itself visual.

### F8.1 Component contract and worked disclosure

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

### F8.2 Canvas, WebGL and interactive scenes

Start with a useful semantic view: an image/poster, scene description, and the selected item's values or list in HTML. Enhance it only after a rendering context is available. Keep the main scene visible. Use a compact collapsible HTML control panel, arrow or button equivalents for essential drag gestures, and a keyboard path back from expanded controls. On mobile, let the panel fold or dock under the scene.

Keep one owner for the animation loop. On `visibilitychange`, check `document.hidden`, cancel the pending frame and suspend animation work. On return, start at most one loop if motion is enabled, reset the time origin and retain the user's selection and pose. Respect user pause and reduced motion even after a tab switch. Release observers, frames and GPU resources on teardown. [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)

Handle a null context at startup, a lost context during interaction and sustained slow frames on the actual device. Reduce render scale or effects first when useful. Offer the static view with the same essential data and controls if the scene remains slow or fails. To support restoration, call `event.preventDefault()` in `webglcontextlost`, suspend the loop and keep the selection in application state. On `webglcontextrestored`, rebuild textures, buffers and programs, apply the latest selection and honor visibility and pause before resuming. Keep the static controls usable if restoration never occurs. Verify startup failure, forced loss, a tab switch and the static path. Report which cases were simulated. [WebGL specification](https://registry.khronos.org/webgl/specs/latest/1.0/#5.15.2) · [MDN context restoration](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event)

## F9. Design Critique Protocol (Before Shipping)

For a concept, walk the same scenario through the sketches, record the break and revise it. For an implementation, repeat the scenario in the rendered artifact. A portfolio or client handoff can show the alternatives, the reason for choosing one and the observed change. Identify actual user feedback separately from a designer's walkthrough. Keep browser and device checks pending until performed.

**Required render loop for coding agents with a browser.** Run the real route with representative data. Capture and visually inspect screenshots at desktop (e.g. 1440 px) and mobile (390 px), each in light and dark. Exercise both browser color preferences even for a single-theme product and record what it renders. When an app has a manual theme switch, test its actual control. Settle fonts, data and transitions, and scroll to lazy content. Capture the affected state for a Patch. Keep screenshots in the task's QA location and record which route, state, viewport and theme each represents.

1. Compare each screenshot for obscured actions, clipped labels, broken wraps, unreadable gradients and unintended overlays. In each case check `document.documentElement.scrollWidth > document.documentElement.clientWidth`. Identify the specific offending element. Check an intentionally scrollable table separately and verify its last column is reachable.
2. Navigate with real Tab/Shift+Tab, Enter/Space and Escape as appropriate. Verify visible focus against the actual backgrounds, logical order, modal/disclosure behavior and focus restoration. Check the main action and a failure or recovery path.
3. Inspect each expected image after it loads, including the narrow crop. For `img` elements check `currentSrc`, `complete`, and `naturalWidth > 0`. Inspect CSS backgrounds, SVG and canvas visually. Verify a failed or unavailable image has a usable fallback.
4. Fix any defect, recapture the failing combination and rerun its checks. Report artifacts or their paths and any unavailable checks. With no executable UI or browser, provide the walkthrough and identify the missing render evidence.

| Criterion | Question |
|:---|:---|
| Clarity | Can a first-time visitor say what this is in 5 seconds? |
| Specificity | Would the page still make sense if the logo were swapped for a competitor's? (It should NOT.) |
| Hierarchy | What draws the eye first in each section when viewed in grayscale? Does that help the user decide? |
| Honesty | Can each public proof claim be traced? Are prototype fixtures clearly identified? |
| Consistency | Only token values used? Same component behaves the same everywhere? |
| States | Are loading/empty/error designed, not default? |
| Accessibility | Keyboard, contrast, semantics, reduced motion pass? |
| Performance | CWV within thresholds on a mid-range phone? |
| Craft | Alignment, optical spacing, widows/orphans in headlines fixed? |

**Squint test:** blur the screenshot. The primary action and the main message must still be the strongest shapes.
