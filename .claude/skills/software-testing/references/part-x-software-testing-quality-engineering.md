# PART X — SOFTWARE TESTING & QUALITY ENGINEERING

Use for test strategy, writing or reviewing tests, and debugging failed or flaky tests in an existing codebase. It complements product-design screenshot checks and security-specific verification; it does not replace either one.

## X1. Choose the smallest test that proves the risk

Read the repository's test commands, fixtures and conventions first. Tie each test to an observable requirement or failure risk. Use a focused unit test for deterministic logic, an integration/contract test at a real boundary, a component test for stateful interaction, and end-to-end testing for a critical user journey. This is a selection guide, not a quota or rigid pyramid. Prefer a few distinct cases over repeating the same assertion at expensive layers.

## X2. Make tests meaningful and repeatable

Assert behavior that callers or users rely on, not incidental private structure. A useful test should fail for the reported defect and pass for the intended behavior. Use isolated state and explicit fixtures; control clocks, randomness and network boundaries where they affect the result. Avoid production data and external services unless the user explicitly authorized that target. Do not weaken assertions, erase a failing case or alter expected values just to turn a run green.

## X3. Exercise browser behavior as a user would

Reuse the project's existing browser runner. Prefer role, label and visible-text locators; use a stable test ID when user-facing semantics cannot identify a dynamic target. Use the runner's condition-based assertions instead of arbitrary sleeps. Isolate browser contexts, storage and test data. Cover the critical success path plus the failure, empty, permission or retry state that could change the user's outcome. Visual snapshots complement behavioral assertions; they do not prove interaction or accessibility. For rendered design critique, use Part F9.

## X4. Diagnose flakes instead of hiding them

For a failure, separate product defect, test defect and environment/tool failure. Inspect the first failing trace, assertion, logs, screenshot/DOM state, network and test data. A bounded retry can help diagnose nondeterminism, but a pass on retry remains flaky and must be reported as such. Avoid blanket retries, larger timeouts, fixed sleeps, broader selectors or skips as a substitute for finding the cause. Keep a minimal reproduction and make only the scoped correction.

## X5. Respect run scope and report evidence

Use installed commands and current project documentation. Verify official docs before adding a framework or relying on version-specific behavior. Run tests only when requested or required by applicable repository/task instructions; follow the user's authorized target and do not launch production checks by implication. When running is authorized, start with the narrowest relevant command, then expand only as appropriate. Report exact commands, environment, passed/failed/skipped/flaky counts, material failures and checks not run. Never imply a test passed if it was not executed.

Primary references: [Playwright best practices](https://playwright.dev/docs/best-practices) · [Playwright isolation](https://playwright.dev/docs/browser-contexts) · [Playwright retries and flaky classification](https://playwright.dev/docs/test-retries) · [Testing Library guiding principles](https://testing-library.com/docs/guiding-principles/) · [Testing Library query priorities](https://testing-library.com/docs/queries/about/)
