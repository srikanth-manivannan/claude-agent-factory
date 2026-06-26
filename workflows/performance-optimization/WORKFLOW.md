---
name: performance-optimization
description: Measure, profile, fix, and verify performance against a target.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [performance, optimization, profiling]
---

# Performance Optimization (Workflow)

> Measure, profile, fix, and verify performance against a target.

## Outcome

A measured performance improvement against a stated target, verified with
before/after numbers and no behavior regression.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:testing/load-test-designer` | 0.1.0 | baseline measurement |
| 2 | `skill:database/query-optimizer` | 0.1.0 | DB bottleneck fixes |
| 2 | `skill:database/index-advisor` | 0.1.0 | index recommendations |
| 2 | `skill:frontend/client-perf-optimizer` | 0.1.0 | client-side fixes |

## Steps

1. **Measure baseline** — establish reproducible metrics against the target.
2. **Profile** — find the actual bottleneck (don't guess); rank by impact.
3. **Fix the top bottleneck** — apply DB and/or client fixes.
4. **Verify** — re-measure; confirm improvement + no regression.
5. **Repeat or stop** — iterate to target, then stop (avoid premature optimization).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target_metric | yes | What to improve + the goal (e.g. p95 < 200ms) |
| workload | yes | Representative load/scenario |

## Outputs

A verified optimization with before/after metrics.

## Failure handling

- No baseline → measure first; never optimize blind.
- Fix doesn't move the metric → revert; re-profile (wrong bottleneck).

## Constraints & safety

- Optimize against measurements, not intuition. Preserve behavior.
