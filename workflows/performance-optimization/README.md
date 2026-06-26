# Performance Optimization (Workflow)

> Measure, profile, fix, and verify performance against a target.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

A measurement-driven optimization loop: baseline → profile → fix the real
bottleneck → verify, iterating to a stated target.

## The flow

`measure → profile → fix → verify → repeat/stop`. See [WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:testing/load-test-designer` (≥ 0.1.0)
- `skill:database/query-optimizer` (≥ 0.1.0)
- `skill:database/index-advisor` (≥ 0.1.0)
- `skill:frontend/client-perf-optimizer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** target metric + representative workload.
- **Outputs:** verified optimization with before/after metrics.

## Customization

Scope to backend-only or client-only by dropping the irrelevant skills.

## Limitations

- Requires a reproducible workload to measure against.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
