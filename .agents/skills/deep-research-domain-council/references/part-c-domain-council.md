# PART C — DOMAIN COUNCIL (Load Only What the Task Needs)

## C1. OpenCode / Agent Runtime (`opencode.ai/docs`)

- **3-level lazy discovery:**
  - L1 (~100 tokens idle): frontmatter only. `name` 1-64 lowercase alnum/hyphen, matching the directory; valid keys `name`, `description`, `license`, `compatibility`, `metadata`.
  - L2 (on demand): full `SKILL.md` from `.opencode/skills/<name>/`, `~/.config/opencode/skills/<name>/`, `.claude/skills/<name>/`, `.agents/skills/<name>/`.
  - L3 (need-to-know): `AGENTS.md` / `CLAUDE.md` / `opencode.json` load `@rules/...` only when required. Disable unused MCP servers globally (`my-mcp*: deny`), enable per agent.
- **Agents:** Plan (read-only), Build (surgical edits), Explore (parallel glob/grep/lsp).
- **Permissions:** `allow` (immediate), `ask` (destructive mutations), `deny` (blocked).

## C2. Claim-Evidence Research Writing & S1-S3 Thesis Engine (`jin-s13/ai-research-writing-skill`)

- Every major claim traces to code/logs/tables/verified metadata, with a confidence label.
- **6-journey state machine:**
  1. Story (`paper_story.md`): thesis, gap, boundaries, claims to avoid.
  2. Claim-Evidence Map (`claim_evidence_map.md`): claim → section/table/figure/script/log + confidence.
  3. Verified BibTeX (`references.bib`): each entry checked against DOI/Crossref/arXiv/Semantic Scholar; SOTA matrix ≥5 works (`Author & Year | Method | Dataset | Metric | Gap`); `[TODO:CITE]` instead of hallucinating.
  4. Deterministic figures: method diagrams (TikZ/SVG) vs result plots produced by scripts from real CSV/JSON.
  5. Skeptical reviewer loop: hostile ICML/NeurIPS/promotor critique (B4 pass 3).
  6. Build gate (`build_check.md`): zero TODO, citations locked, LaTeX log clean, venue format.
- **Indonesian S1-S3 (Bab I-V):**
  - No cliché openings ("Di era globalisasi / revolusi industri 4.0..."). Open Bab I with the concrete phenomenon and its measured anomaly.
  - Bab I: inverted pyramid; $RQ_1..RQ_n$ mapped 1:1 to *Tujuan*.
  - Bab II: SOTA matrix built with A1 S4.2 citation chasing + *Kerangka Pemikiran*.
  - Bab III: formal methodology (DSR, CRISP-DM, NDLC, RUP), math, power/effect size, $O(n)$ bounds.
  - Bab IV: black-box + white-box testing (cyclomatic $V(G)=E-N+2P$), p50/p95/p99 with causal explanation, ablation.
  - Bab V: numbered answers to each RQ.
  - Lab report: Times New Roman 12 pt; margins top/left 4 cm, bottom/right 3 cm; correct cover year; legible enlarged screenshots.

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

## C4. Android & Kotlin Architecture (`javiercamarenatriguero/android-skills`)

1. **android-modularization:** `:app` (entry + DI), `:feature:*` (MVI ViewModel), `:component:*` (use cases/repos/data), `:common:*` (design system/nav keys). Features never depend on features.
2. **mvi-editor:** immutable `ViewState`, `sealed interface ViewEvent`, `Channel<SideEffect>(BUFFERED).receiveAsFlow()` collected in `LaunchedEffect`.
3. **compose-editor:** hoisted state (`ScreenRoute(viewModel)` → stateless `ScreenContent(state, onEvent)`), `Modifier` first optional param, M3 tokens, semantics/`contentDescription`.
4. **compose-performance-auditor:** `@Immutable`/`@Stable`, `ImmutableList`, `derivedStateOf`, stable `key` + `contentType`, deferred reads (`Modifier.offset { IntOffset(...) }`, `drawWithContent`), Baseline Profiles, Macrobenchmark. Targets: jank <1%, cold start p50 ≤800 ms, warm ≤200 ms.
5. **compose-navigation3:** `@Serializable NavKey`, `NavDisplay`, decoupled navigators, `ResultStore`.
6. **kotlin-coroutines:** injected dispatchers, `stateIn(WhileSubscribed(5_000))`, `supervisorScope`, never swallow `CancellationException`.
7. **kotlin-convention:** `@JvmInline value class`, exhaustive sealed types, no `!!`, sequences without intermediate boxing.
8. **koin-editor:** `singleOf`/`viewModelOf`/`factoryOf`, correct scopes, graph verified in tests.
9. **gradle-configuration + convention plugins:** `libs.versions.toml`, `build-logic`, configuration cache, non-transitive R, `api` vs `implementation`. Targets: incremental ≤8 s, clean ≤60 s.
10. **android-permissions-editor:** `Unrequested` / `Granted` / `DeniedShouldShowRationale` / `PermanentlyDenied` → Compose rationale + MVI events.
11. **unit tests + paparazzi:** MockK + Turbine + `runTest(StandardTestDispatcher)`, GIVEN/WHEN/THEN; Paparazzi snapshots (light/dark, font scales, device sizes) without emulator.
12. **github-action + review-owasp-security:** cached Gradle matrix; OWASP MASVS pass (Keystore storage, TLS pinning, biometrics, deep links, zero hardcoded secrets).

## C5. Full-Stack, 60fps Motion & Distributed Back-End

- **Full-stack (Next.js / React / Tauri 2 Rust / .NET):** strict TS (0 `any`), clean server/client boundaries, streaming Suspense, zero-copy Rust serde IPC or .NET `Span<T>`/`ValueTask`/`ArrayPool<T>`; precompute `Map`/`Set`; batch DOM/canvas writes per `rAF`; roofline check before optimizing. Verify framework versions against current docs before using version-specific APIs.
- **Motion engine:** seeded `mulberry32` PRNG rigs, 240 Hz RK4 spring, negative anticipation `v0=-2.5`, optional Web Audio FFT sub-bass sync. Budget <16.67 ms/frame, 0 allocs/frame.

```typescript
export interface RK4Spring { stiffness: number; damping: number; mass?: number; v0?: number; }

export function createSeededPRNG(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    let t = (a += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function solveRK4Spring(tSec: number, { stiffness: k, damping: c, mass: m = 1, v0 = -2.5 }: RK4Spring) {
  const dt = 1 / 240, steps = Math.max(0, Math.floor(tSec / dt));
  let x = 0, v = v0;
  const a = (p: number, vel: number) => (-k * (p - 1) - c * vel) / m;
  for (let i = 0; i < steps; i++) {
    const k1x = v, k1v = a(x, v);
    const k2x = v + 0.5 * dt * k1v, k2v = a(x + 0.5 * dt * k1x, v + 0.5 * dt * k1v);
    const k3x = v + 0.5 * dt * k2v, k3v = a(x + 0.5 * dt * k2x, v + 0.5 * dt * k2v);
    const k4x = v + dt * k3v, k4v = a(x + dt * k3x, v + dt * k3v);
    x += (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x);
    v += (dt / 6) * (k1v + 2 * k2v + 2 * k3v + k4v);
  }
  return { value: x, velocity: v };
}
```

- **Upstash Redis:** batch with `mget`; rate-limit + cache write in a single `pipeline()` with `EX 300`; no N+1 `GET`.
- **Turso / libSQL:** durable logs via `@libsql/client`; covering composite index `CREATE INDEX idx_domain_ts ON records(domain, created_at DESC)`; circuit breaker CLOSED → OPEN → HALF_OPEN with exponential backoff + jitter.
- **Targets:** cache hit ≥95%, p99 ≤200 ms, ≤3 Redis commands/request.

## C6. Skill Security Auditor (`dabit3/skill-audit`) & Cryptographic Vault

**Part A, audit scoring (security starts at 100):**
- CRITICAL (−40): RCE (`eval`, `curl…|sh`, `wget…|bash`), reads of `/etc/passwd`, `~/.ssh`, `.env`; fork bombs.
- HIGH (−25): unsanitized `child_process.exec`/`spawn`, `sudo`, hardcoded keys, remote shell exec.
- MEDIUM (−15): path-traversal writes, unverified downloads (no SHA-256), `chmod 777`.
- LOW (−5): sensitive stdout, missing `set -euo pipefail`.
- Quality (0-100): frontmatter, examples, links, pinned deps, input validation.
- Overall $=0.6\cdot\text{Security}+0.4\cdot\text{Quality}$; grades A-F. Ship ≥80 (B) with 0 CRITICAL/HIGH.

**Part B, vault + exposure scanner:**

```typescript
import crypto from "node:crypto";

// why: salt must be random per deployment and stored alongside config; a constant salt is only safe for high-entropy secrets.
export function deriveKeyHKDF(masterSecret: Buffer, salt: Buffer, context: string): Buffer {
  return Buffer.from(crypto.hkdfSync("sha256", masterSecret, salt, Buffer.from(context), 32));
}

export function encryptVaultGCM(plaintext: string, key: Buffer, aadContext: string) {
  const iv = crypto.randomBytes(12); // why: 96-bit random IV; never reuse an IV with the same key
  const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
  cipher.setAAD(Buffer.from(aadContext, "utf8"));
  const ciphertext = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]).toString("hex");
  return { iv: iv.toString("hex"), authTag: cipher.getAuthTag().toString("hex"), ciphertext, aadContext };
}

export function decryptVaultGCM(rec: { iv: string; authTag: string; ciphertext: string; aadContext: string }, key: Buffer): string {
  const decipher = crypto.createDecipheriv("aes-256-gcm", key, Buffer.from(rec.iv, "hex"));
  decipher.setAAD(Buffer.from(rec.aadContext, "utf8"));
  decipher.setAuthTag(Buffer.from(rec.authTag, "hex"));
  return Buffer.concat([decipher.update(Buffer.from(rec.ciphertext, "hex")), decipher.final()]).toString("utf8");
}

export function shannonEntropy(str: string): number {
  if (!str) return 0;
  const freq = new Map<string, number>();
  for (const c of str) freq.set(c, (freq.get(c) ?? 0) + 1);
  let h = 0;
  for (const n of freq.values()) { const p = n / str.length; h -= p * Math.log2(p); }
  return Number(h.toFixed(3));
}
```

**Scanner signatures (defensive use on your own assets only):** `/.env`, `/.git/HEAD`, high-entropy strings $H(X) > 4.5$ bits/char, known webshell filenames (`wp2shell`, `php2shell`, `node2shell`, `go2shell`, `py2shell`, `tinyfilemanager.php`, `node-oob`).
