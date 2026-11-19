# PART O — PROJECT SCAFFOLDING (Gemini 4 Argon + Gemini 4 Carbon)

Scaffolding decides most of a project's long-term cost: structure, tooling, quality rails, conventions. Do it with research, not with memory of last year's templates.

## O1. Model Roles

| Role | Model | Why | Effort |
|:---|:---|:---|:---|
| **Research & architect** | Gemini 4 Argon | GA, 1M-token context, built for long-horizon research and complex workflows; strong at reading many docs at once | High thinking for stack research and ADRs |
| **Builder** | Gemini 4 Carbon | Aimed at long-running software work; spends more thinking per turn than Argon | High |
| **Fallback builder** (Carbon unavailable: as of Nov 2026 it is limited to selected cyber defenders) | Gemini 4 Argon (high) or Claude Opus 5.5 (medium-high) | Both GA and strong at agentic coding | High |
| **Boilerplate / repetitive files** | Fastest model available (e.g., Gemini 4 Hydrogen ⚠ check availability) | Cheap tokens for mechanical work | Low-medium |

The pattern matters more than the brand: **one model researches and designs, another builds, and the build is verified by running it.** If the requested models are unavailable, keep the roles and swap the models.

## O2. Scaffolding Workflow

1. **Requirements brief** (≤1 page): product type, users, scale expectation, team size and skills, deployment target, constraints (budget, compliance, region, offline, mobile).
2. **Stack research (Argon, Part A tier S):**
   - Current stable versions from **official registries/release pages** (npm, PyPI, crates.io, Maven Central, Go proxy, official changelogs). Never type a version number from memory.
   - Official getting-started docs and generators for each candidate.
   - Known breaking changes in the last 2 major versions; LTS status; maintenance activity.
3. **Architecture Decision Record (ADR)** for each major choice: context, options, decision, consequences, date.
4. **Scaffold plan** (hand-off contract, O4) from Argon to the builder.
5. **Generate with official generators first** (`npm create vite@latest`, `npx create-next-app@latest`, `cargo new`, `uv init`, `dotnet new`, `gradle init`, Android Studio templates), then customize. Hand-writing what a generator does introduces drift.
6. **Quality rails** (O3) before any feature code.
7. **One vertical slice:** a single real feature through every layer (UI → API → DB → test → CI) proves the skeleton.
8. **Verify from a clean clone** (O5).
9. **Document:** README (setup in ≤5 commands), `.env.example`, ADRs, CONTRIBUTING.

## O3. Quality Rails Every Scaffold Gets

| Rail | Examples |
|:---|:---|
| Formatting | Prettier / Biome, Black/Ruff format, rustfmt, ktlint |
| Linting | ESLint / Biome, Ruff, Clippy, detekt |
| Types | `strict: true` TS, mypy/pyright strict, Kotlin explicit API where useful |
| Tests | Unit runner + one example test per layer; coverage reporting |
| Pre-commit | Format + lint + typecheck on staged files (lefthook / husky / pre-commit) |
| CI | Install with lockfile, lint, typecheck, test, build; cache dependencies; run on PRs |
| Env & secrets | `.env.example` committed, `.env` git-ignored, runtime validation of env vars at startup |
| Error handling | Central error handler/boundary, structured logging, request IDs (Part N4) |
| Repo hygiene | `.gitignore`, `.editorconfig`, LICENSE, CODEOWNERS (teams), Dependabot/Renovate |
| Security | Dependency audit in CI, no secrets in repo, secure headers for web |

## O4. Argon → Builder Hand-off Contract (`scaffold_plan.json`)

```json
{
  "project": "kasir-umkm",
  "type": "web-app",
  "stack": {
    "runtime": {"name": "node", "version": "<from official release page>", "source": "<url>", "checked": "2026-11-18"},
    "framework": {"name": "<framework>", "version": "<verified>", "generator": "<official command>"},
    "db": {"name": "<db>", "client": "<lib>@<verified version>"},
    "test": "<runner>", "lint": "<tool>", "format": "<tool>"
  },
  "structure": ["src/app", "src/features/<feature>", "src/lib", "src/server", "tests", ".github/workflows"],
  "conventions": {"naming": "kebab-case files", "imports": "absolute via @/", "errors": "Result at boundaries, RFC 9457 in API"},
  "vertical_slice": "Create and list products end to end",
  "acceptance": ["clean clone → install → test → build passes", "lint + typecheck clean", "CI green", "README setup ≤5 commands"],
  "adrs": ["docs/adr/0001-framework.md", "docs/adr/0002-database.md"],
  "open_questions": []
}
```

The builder must not change stack choices silently; disagreements go back to the architect as `open_questions`.

## O5. Scaffold Acceptance Test

Run in a fresh directory, exactly as a new teammate would:

```bash
git clone <repo> && cd <repo>
cp .env.example .env
<install command with lockfile>
<lint> && <typecheck> && <test> && <build>
<start dev server> # and load the vertical slice in a browser / call the endpoint
```

All must pass with zero manual fixes. Any manual step becomes a README line or a script.

## O6. Reference Layouts (Adapt, Don't Copy Blindly)

```
web-app/                         api-service/                  monorepo/
├── src/                         ├── src/                      ├── apps/
│   ├── app/        (routes)     │   ├── routes/               │   ├── web/
│   ├── features/<name>/         │   ├── services/             │   └── api/
│   │   ├── components/          │   ├── repositories/         ├── packages/
│   │   ├── api.ts               │   ├── schemas/              │   ├── ui/
│   │   └── model.ts             │   ├── errors.ts             │   ├── config/
│   ├── lib/                     │   └── main.ts               │   └── types/
│   └── styles/tokens.css        ├── tests/                    ├── docs/adr/
├── tests/                       ├── migrations/               ├── .github/workflows/
├── docs/adr/                    ├── docs/adr/                 └── <workspace config>
├── .github/workflows/ci.yml     └── .github/workflows/ci.yml
└── .env.example
```

Android: follow C4 (`:app`, `:feature:*`, `:component:*`, `:common:*`, `build-logic`).

## O7. Prompt Templates

**Argon (architect):**
> "You are the architect. Using only official docs and registries, research current stable versions and recommended project structure for: <brief>. Output: (1) options table with trade-offs, (2) ADRs, (3) scaffold_plan.json per the contract, (4) risks and open questions. Cite every version with its source URL and date."

**Carbon / builder:**
> "You are the builder. Implement scaffold_plan.json exactly. Use official generators first. Add all quality rails. Build the vertical slice. Run the acceptance test and paste the final command outputs (last lines only). If anything in the plan is wrong or impossible, stop and list it under open_questions instead of improvising."
