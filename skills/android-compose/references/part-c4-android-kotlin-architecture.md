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
