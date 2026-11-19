# PART F — WEB & DESIGN DEEP MODULE (Extends C3)

C3 says what to avoid. This part says **how a senior product designer + front-end engineer actually builds a page that does not look generated.**

## F0. Why AI Sites Look Like AI Sites (Diagnose Before You Design)

AI slop is not one mistake; it is the *average of the internet* rendered at once. Recognize the fingerprint:

| Slop fingerprint | Why it happens | What a senior does instead |
|:---|:---|:---|
| Centered hero, giant gradient headline, two buttons, floating 3D blob | Most common landing pattern in training data | Start from the content and the user's first job; hero can be a table, a product screenshot, a search box, a single sentence |
| Purple-to-blue gradient, glow, glassmorphism everywhere | "Modern" averaged | One brand color derived from the product's world; neutral surfaces carry 90% of the UI |
| Three feature cards with icons, identical size | Easiest grid | Vary weight: one primary capability large, secondary ones as a list, proof as real data |
| "Unlock the power of…", "Seamlessly…", "Elevate your…" | Marketing filler | Concrete verb + object + outcome: "Export invoices to Excel in one click" |
| Fake logos, "Trusted by 10,000+ teams", 5-star testimonials | Template placeholders | Real proof or nothing; placeholder marked `[REAL DATA]` |
| Inter everywhere, 16/24/48 random sizes | Default font, no scale | Chosen typeface with a reason + modular scale |
| Every section same padding, same width | No rhythm decision | Deliberate density changes: tight data sections, airy narrative sections |
| Emoji as icons, sparkle icon for "AI" | Shortcut | Icon set with consistent stroke/grid, or no icon |
| Dark mode = invert colors | Afterthought | Separate tuned palette (surfaces get lighter with elevation, saturation reduced) |
| Animations on everything on scroll | "Make it lively" | Motion only where it explains change of state |

**Slop test (run on every page):** cover the logo. Could this page belong to any of 1,000 other startups? If yes, it is slop. Fix the *content and structure* first, styling second.

## F1. Design Process (In Order, No Skipping)

1. **Job & audience.** Who lands here, from where, wanting what in the first 10 seconds? Write it: `A <role> arriving from <source> wants to <job>; success = <action>.`
2. **Content inventory.** List every real piece of content you have (copy, data, screenshots, docs, prices). Design *around real content*; never design empty boxes then fill them.
3. **Information architecture.** Order sections by the questions the visitor asks, in the order they ask them (What is it → Is it for me → Does it work → What does it cost → How do I start).
4. **Low-fi structure.** Grayscale wireframe in boxes and real text. Judge hierarchy without color.
5. **Design Read + reference system** (C3).
6. **Tokens first** (F2), then components (F4), then pages.
7. **States** for every component: default, hover, focus, active, disabled, loading, empty, error, success.
8. **Responsive pass** at 360, 768, 1024, 1440 px.
9. **Accessibility pass** (F6) and **performance pass** (F7).
10. **Critique pass** (F9) before shipping.

## F2. Design Tokens (The Foundation)

### F2.1 Typography

- **Choose a typeface for a reason**: editorial (serif for long reading: Source Serif, Literata, Newsreader), technical (grotesk + mono: IBM Plex, Geist, JetBrains Mono), friendly (humanist: Nunito Sans, Figtree), institutional (Public Sans). State the reason in one line.
- **Max two families** (one + mono is usually enough).
- **Modular scale:** pick a ratio and stop improvising. 1.125 (dense apps), 1.2 (product UI), 1.25 (marketing), 1.333 (editorial).
- **Fluid type** with `clamp()` so headings scale between breakpoints without jumps.
- **Line length** 45-75 characters for body (`max-width: 65ch`). **Line height** 1.5-1.7 body, 1.1-1.25 headings. Tighten letter-spacing slightly on large headings (−0.01 to −0.03em), never on body.
- **Weight hierarchy over size inflation:** 400 body, 500-600 UI labels, 600-700 headings. Avoid 800-900 except display.
- Numerals in tables: `font-variant-numeric: tabular-nums;`.

### F2.2 Color

- Build in **OKLCH** for perceptually even ramps: same L across hues means same perceived lightness.
- **Neutral ramp (10-12 steps)** does most of the work: background, surface, border, muted text, text. Tint neutrals slightly toward the brand hue (chroma 0.005-0.02) so gray does not feel dead.
- **One brand hue**, used for primary action and key highlights only. Plus semantic colors: success, warning, danger, info.
- **60-30-10**: ~60% neutral surface, ~30% secondary surface/text, ~10% accent.
- Never pure `#000` on pure `#fff` for long reading; use near-black on off-white.
- Contrast: body ≥4.5:1, large text and UI components ≥3:1. Never encode meaning by color alone.
- **Dark mode**: not inverted. Background around L 0.15-0.20, elevated surfaces get *lighter*, reduce accent chroma, re-test contrast.

### F2.3 Space, Size, Radius, Shadow

- **4 px base grid**, spacing scale `4, 8, 12, 16, 24, 32, 48, 64, 96, 128`. Use only these.
- **Proximity rule:** space inside a group < space between groups. If everything has 24 px gaps, nothing is grouped.
- **Radius hierarchy:** nested radius = outer radius − padding. Pick one personality: sharp (0-4), soft (6-10), round (12-16). Pills only for tags/toggles.
- **Elevation:** at most 3 shadow levels; shadows are tinted with the background hue, low opacity, with a tight + soft layer combination. In dark mode, use lighter surfaces instead of shadows.

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

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

## F3. Layout & Composition

- **Grid:** 12 columns desktop, 8 tablet, 4 mobile; content max-width ~1200-1280 px; reading column ~65ch.
- **Hierarchy tools, in order of strength:** position → size → weight → color → decoration. Reach for decoration last.
- **One focal point per viewport.** If two things shout, neither is heard.
- **Rhythm:** alternate dense and airy sections deliberately; break the grid once per page at most, with a reason.
- **Alignment:** everything aligns to something. Ragged-left text blocks and centered paragraphs longer than 2 lines are reading penalties.
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

## F4. Components (Behavior Matters More Than Looks)

- **Buttons:** one primary per view; label = verb + object ("Create invoice", "Download report"); min target 44×44 px; loading state keeps width (no layout jump); disabled buttons explain why (tooltip or helper text).
- **Forms:** labels above inputs (not placeholder-as-label); inline validation on blur, not on every keystroke; error text says how to fix ("Use at least 8 characters"), not just "Invalid"; preserve input on error; group related fields; mark optional, not required, when most are required.
- **Tables:** left-align text, right-align numbers, tabular numerals, sticky header for long tables, sortable columns show sort state, row density toggle for power users, empty state with next action.
- **Navigation:** ≤7 top-level items; current location always visible; search for >30 pages.
- **Feedback:** every action gets a response within 100 ms (visual) and a result or progress indicator within 1 s; optimistic UI with undo beats confirmation dialogs for reversible actions.
- **Empty states:** explain what will appear here and the single action that fills it.
- **Errors:** human language, cause, fix, and a way out. Never a raw stack trace.

## F5. Copywriting for Interfaces (Natural, Not Generated)

- Write like a knowledgeable colleague explaining to a busy peer.
- **Specific > clever.** "Sync 3 calendars, see conflicts before they happen" beats "Your time, reimagined".
- **Verbs and nouns carry meaning; adjectives are suspicious.** Delete "powerful", "seamless", "robust", "innovative", "cutting-edge", "next-gen", "revolutionary", "effortless", "unlock", "elevate", "supercharge", "empower", "leverage", "harness", "in today's fast-paced world".
- Headline = the outcome; subhead = how; CTA = the next concrete step.
- Sentence-case headings, not Title Case Everywhere.
- Numbers must be real and sourced; otherwise remove the claim.
- Indonesian copy: use natural register (baku but not stiff); avoid literal translations like "Buka kekuatan…"; prefer "Kirim faktur dalam satu klik".

## F6. Accessibility (Hard Requirements)

- Semantic HTML first (`header`, `nav`, `main`, `section` with headings, `button` for actions, `a` for navigation). ARIA only when HTML can't express it.
- Logical heading order (one `h1`, no skipped levels).
- Full keyboard operation, visible `:focus-visible` ring ≥3:1 contrast, no keyboard traps, skip-to-content link.
- Images: meaningful `alt`; decorative `alt=""`.
- Forms: `<label for>`, `aria-describedby` for help/error text, error summary on submit.
- Motion respects `prefers-reduced-motion`; nothing flashes >3 times/second.
- Zoom to 200% without loss of content; reflow at 320 px width without horizontal scroll.
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
- Durations: micro-interactions 100-200 ms, panels/modals 200-320 ms, page transitions ≤400 ms. Exits faster than entrances.
- Ease-out for entering, ease-in for leaving; springs for direct manipulation (C5 RK4).
- Animate `transform` and `opacity` only (compositor-friendly); avoid animating layout properties.
- MOTION dial 1 = hover/focus only; 2 = + subtle reveal on first view (once, not every scroll); 3 = physics/canvas, only when the product is itself visual.

## F9. Design Critique Protocol (Before Shipping)

Score 1-5, ship only if all ≥4:

| Criterion | Question |
|:---|:---|
| Clarity | Can a first-time visitor say what this is in 5 seconds? |
| Specificity | Would the page still make sense if the logo were swapped for a competitor's? (It should NOT.) |
| Hierarchy | Is there exactly one focal point per viewport? |
| Honesty | Is every number, logo and quote real? |
| Consistency | Only token values used? Same component behaves the same everywhere? |
| States | Are loading/empty/error designed, not default? |
| Accessibility | Keyboard, contrast, semantics, reduced motion pass? |
| Performance | CWV within thresholds on a mid-range phone? |
| Craft | Alignment, optical spacing, widows/orphans in headlines fixed? |

**Squint test:** blur the screenshot. The primary action and the main message must still be the strongest shapes.
