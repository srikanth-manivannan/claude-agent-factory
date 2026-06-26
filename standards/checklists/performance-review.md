# Performance Review Checklist

> Reviews performance work for rigor and results. Run **after** the
> [Universal Core](_universal.md). Backs the `performance-optimization` workflow.
> Legend: [README.md](README.md).

**Applies to:** performance-sensitive changes · **Min standard:** 0.1.0

## Method (measure, don't guess)
- [ ] 🔴 `[manual]` A baseline was measured before optimizing.
- [ ] 🟠 `[manual]` A performance target is stated (e.g. p95 latency, throughput).
- [ ] 🟠 `[manual]` The bottleneck was identified by profiling, not assumption.

## Results
- [ ] 🟠 `[manual]` Improvement verified with before/after numbers.
- [ ] 🟡 `[manual]` No behavior regression introduced by the optimization.

## Common hotspots
- [ ] 🟡 `[auto]` No N+1 or unindexed hot queries (→ `index-advisor`).
- [ ] 🟡 `[manual]` Caching strategy appropriate; invalidation is correct.
- [ ] 🟡 `[manual]` Large payloads paginated/streamed, not loaded whole.
- [ ] 🟡 `[manual]` Memory/CPU usage within budget.
- [ ] 🟡 `[auto]` Client bundle/asset size within budget (if applicable).
