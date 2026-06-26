# Generate Test Suite (Workflow)

> Use this workflow to produce a layered, gap-free test suite for a unit or module.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
Builds a deterministic test suite: generates core tests (`testing/unit-test-generator`),
fills meaningful gaps (`testing/coverage-gap-finder`), and removes flakiness
(`testing/test-refactorer`) — the safety net `refactor-module` depends on.

## Composes
- `skill:testing/unit-test-generator` · `skill:testing/coverage-gap-finder` ·
  `skill:testing/test-refactorer`.

See [WORKFLOW.md](WORKFLOW.md) for the full sequence.

## Version history
See [CHANGELOG.md](CHANGELOG.md).
