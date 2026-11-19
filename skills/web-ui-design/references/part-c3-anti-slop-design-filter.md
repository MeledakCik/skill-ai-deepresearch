## C3. Anti-Slop Design Filter (`miqdadbadjuber/anti-slop`)

- **Design Read:** `Reading this as: <page kind> for <audience>, in <visual language>, ENERGY <1-3> / RHYTHM <1-3> / MOTION <1-3>. Reference: <system>.`
- **3 Dials:** ENERGY (1 calm / 2 balanced / 3 bold), RHYTHM (1 uniform / 2 consistent-breaks / 3 asymmetric), MOTION (1 hover / 2 scroll-reveal / 3 physics/canvas).
- **5 visual languages:** `swiss-editorial`, `spatial-hardware`, `sentinel-telemetry`, `archival-academic`, `kinetic-bento`.

**Group 1, hard gates:**
- R-02 no em dashes (`—`) in generated UI copy.
- R-03 mobile: 0 horizontal overflow, 44×44 px touch targets.
- R-17/18/36/38 zero fabricated data: no fake stats/testimonials/badges; use `[REAL DATA]` or "Coming soon".
- R-23 no silently invented logos/team photos.
- R-24/26 zero dead controls: every `<a>`/`<button>` does something real.
- R-25/32/39 accessibility: WCAG AA ≥4.5:1 (large ≥3:1), full keyboard, `:focus-visible`, landmarks, `<label>`, `prefers-reduced-motion`.
- R-27 empty/loading/error states on every data view.
- R-28 product-specific FAQ, no templates.
- R-33/34/35/40 no CSS regex patching; light+dark theme integrity; explicit media dimensions; `fetchpriority="high"` on hero.

**Group 2, purpose gates (1-line purpose + dose cap):** R-01 gradients, R-04 icons (no sparkle/robot/orb clichés), R-06 typography, R-07 background grids, R-08 button arrows, R-09 capsule badges (no "AI Powered" pill), R-10 glassmorphism ≤1-2 elements, R-12 shadows, R-13 glow ≤1-2 accents, R-14 varied card hierarchy, R-19 motion matches dial, R-22 illustrations.

**Group 3, quality locks:** R-05 no AI template layouts, R-11 radius hierarchy, R-15 specific CTAs (no "Get Started"/"Learn More"), R-16 banned buzzwords, R-20/R-30 no unprompted Linear/Vercel/Stripe clones, R-29 palette 2-3 core + 1 accent, R-31 one-line reason per design decision.

**`antislop-code` comment filter:** strip narrating comments, ASCII banners, emoji headers; keep only "why" comments (invariants, math, regex/bitmask rationale, platform workarounds).

### C3.1 Professional Design Reference Layer

| Reference | Source | Core principle | Anti-slop alignment |
|:---|:---|:---|:---|
| Apple HIG | [developer.apple.com/design](https://developer.apple.com/design/human-interface-guidelines/) | Clarity, deference, depth | R-10, R-25, R-34 |
| Microsoft Fluent 2 | [fluent2.microsoft.design](https://fluent2.microsoft.design/design-principles) | Native-first, signature where it matters | R-05, R-27, R-39 |
| Anthropic Brand | [brand-guidelines skill](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md) | Warm near-black `#141413` + cream `#faf9f5`; accents `#d97757`, `#6a9bcc`, `#788c5d`; no pure `#000`/`#fff` | R-29, R-06, R-16 |
| Google Material 3 | [m3.material.io](https://m3.material.io/) | Breakpoint-driven adaptive layout | R-03, R-27, R-05 |
| Stripe (community analysis) | [analysis](https://github.com/yc-software/qm/blob/340e553683455b61a95179eafeafeb19a4dc876c/skills-seed/popular-web-designs/templates/stripe.md) | Blue-tinted shadows `rgba(50,50,93,0.25)`, light display weight, radius 4-8 px | R-12, R-29, R-11 |
| IBM Carbon | [carbondesignsystem.com](https://carbondesignsystem.com/) | WCAG AA 4.5:1 / 3:1 large; never color alone | R-25, R-32, R-39 |

| Reference | Primary use case |
|:---|:---|
| Apple HIG | Consumer iOS/macOS/visionOS |
| Fluent 2 | Windows / productivity |
| Anthropic | Research tools, editorial AI products |
| Material 3 | Android, cross-platform |
| Stripe | Fintech, infra, premium SaaS |
| Carbon | Enterprise, government, accessibility-critical |

Every UI declares `Reference: <System>`. Defaults: Carbon (accessibility), Apple HIG (interaction), Anthropic (typography/palette).
