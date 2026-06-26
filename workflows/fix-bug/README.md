# Fix Bug (Workflow)

> Reproduce, localize, fix, and regression-test a bug, then document the fix.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

The disciplined debugging loop: reproduce → localize → failing test → fix →
document. Guarantees every fix ships with a regression test.

## The flow

`reproduce → localize → write failing test → fix → document`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:research/codebase-explorer` (≥ 0.1.0)
- `skill:testing/unit-test-generator` (≥ 0.1.0)
- `skill:testing/coverage-gap-finder` (≥ 0.1.0)
- `skill:documentation/doc-writer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** a bug report with repro steps.
- **Outputs:** fix + regression test + documented root cause.

## Customization

Add a `performance-optimization` handoff if the bug is a perf regression.

## Limitations

- Requires a reproducible bug; flaky/non-deterministic issues need extra triage.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
