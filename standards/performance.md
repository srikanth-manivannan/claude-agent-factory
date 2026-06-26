# Performance Standard

> Measure-first performance rules. Enforced by the
> [performance-review checklist](checklists/performance-review.md).

**Min standard:** 0.1.0 · See also: [testing.md](testing.md), [architecture.md](architecture.md).

## Principles

1. **Measure, don't guess.** Establish a baseline before optimizing.
2. **Set a target.** State the goal (e.g. p95 latency, throughput, bundle size).
3. **Profile to find the real bottleneck.** Optimize what the data shows, not intuition.
4. **Verify.** Prove improvement with before/after numbers; confirm no behavior
   regression.
5. **Don't over-optimize.** Stop at the target; clarity beats micro-tuning.

## Common rules

- Avoid N+1 and unindexed hot-path queries (see database skills in [TAXONOMY](../TAXONOMY.md)).
- Cache deliberately; get invalidation right.
- Paginate/stream large payloads; don't load everything.
- Keep memory/CPU within budget; keep client bundles within budget.

## Documentation

Performance-sensitive artifacts state their target and measured numbers in the
README ([documentation.md](documentation.md)).
