# Plan Feature (Workflow)

> Use this workflow to turn a feature goal into a reviewed, decision-recorded plan.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
Turns a feature goal into an approved plan: chooses the approach (with rationale via
`architecture/tradeoff-analyzer`), validates the design (`architecture/system-design-reviewer`),
and produces acceptance criteria — the upstream input to `build-feature`.

## Composes
- `skill:architecture/tradeoff-analyzer` · `skill:architecture/system-design-reviewer`.

See [WORKFLOW.md](WORKFLOW.md) for the full sequence.

## Version history
See [CHANGELOG.md](CHANGELOG.md).
