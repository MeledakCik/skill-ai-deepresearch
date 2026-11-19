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
