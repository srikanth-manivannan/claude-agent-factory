# Unit Test Generator

> Use this to generate thorough unit tests for a unit of code, covering happy, edge, and failure cases.

**Category:** testing · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Generates a complete, isolated, deterministic unit-test suite for a given unit of
code — covering the three mandatory case classes (happy / edge / failure) the
[testing standard](../../../standards/testing.md) requires. It matches your project's
existing framework and conventions instead of imposing new ones, and asserts behavior
(not implementation) so the tests survive refactors.

This is a **foundational primitive**: many workflows (`build-feature`, `fix-bug`,
`refactor-module`) and skills depend on it.

## Quickstart

```text
1. Copy skills/testing/unit-test-generator/ into your skills directory.
2. Invoke with the unit to test (+ framework if not inferable).
3. Receive a test file in your framework with happy/edge/failure cases.
```

## How it works

Seven steps: understand contract → enumerate cases (3 classes) → detect framework →
write isolated/deterministic tests → assert behavior → name by intent → report coverage
intent. Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `unit`, optional `framework`, optional `behavior_spec`.
- **Outputs:** a framework-native test file + a coverage-intent note.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Pin the framework** to override auto-detection.
- **Adjust strictness** (e.g. require a failure case per public method).
- **Pair** with `testing/coverage-gap-finder` to find what's still untested.

## Limitations

- Tests are only as good as the stated/inferred behavior contract.
- It will not edit the unit under test; untestable code is reported, not silently fixed.

## Related

See [RESOURCES.md](RESOURCES.md). Depended on by `frontend/component-scaffold`,
`devops/ci-pipeline-generator`, and the `build-feature` / `fix-bug` / `refactor-module`
workflows.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Optional property-based test generation (hand off to `testing/property-test-builder`).
- Coverage-threshold enforcement integrated with `coverage-gap-finder`.
- Snapshot-test support for serializable outputs.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
