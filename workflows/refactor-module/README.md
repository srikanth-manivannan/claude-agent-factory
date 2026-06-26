# Refactor Module (Workflow)

> Refactor a module safely under a test safety-net without changing behavior.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Restructures code for quality while guaranteeing behavior stays identical, using
a characterization-test safety net.

## The flow

`understand → safety net → refactor in small steps → tidy tests → verify`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:research/codebase-explorer` (≥ 0.1.0)
- `skill:testing/unit-test-generator` (≥ 0.1.0)
- `skill:testing/test-refactorer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** target module + refactor goal.
- **Outputs:** behavior-preserving refactor with a healthy test suite.

## Customization

Chain into `performance-optimization` if the goal is speed.

## Limitations

- Requires (or builds) adequate test coverage first; depends on `generate-test-suite`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
