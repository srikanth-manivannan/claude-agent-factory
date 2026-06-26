---
name: generate-test-suite
description: Use this workflow to produce a layered, gap-free test suite for a unit or module.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [workflow, testing, quality]
---

# Generate Test Suite (Workflow)

> Use this workflow to produce a layered, gap-free test suite for a unit or module.

A repeatable sequence of activities composing >=2 skills ([/standards/architecture.md](../../standards/architecture.md)).

## Outcome
A deterministic test suite covering happy/edge/failure cases with meaningful coverage and
no flaky or brittle tests — the safety net `refactor-module` and `build-feature` rely on.

## Composition
- `skill:testing/unit-test-generator` (>= 0.1.0) — generate the core tests.
- `skill:testing/coverage-gap-finder` (>= 0.1.0) — find + fill meaningful gaps.
- `skill:testing/test-refactorer` (>= 0.1.0) — remove flakiness/brittleness.

## Steps
1. **Generate** baseline tests with `unit-test-generator` (happy/edge/failure).
2. **Find gaps** with `coverage-gap-finder`; add tests for meaningful uncovered paths.
3. **Harden** with `test-refactorer` — remove flaky/slow/brittle tests.
4. **Verify** the suite is green and deterministic.

## Inputs
| Input | Required | Description |
|-------|----------|-------------|
| target | yes | The unit/module to cover |

## Outputs
A layered, deterministic test suite with meaningful coverage.

## Failure handling
- Untestable code → recommend a refactor (`refactor-module`) before forcing tests.
- Flaky test can't be stabilized → quarantine + track, never ignore silently.
