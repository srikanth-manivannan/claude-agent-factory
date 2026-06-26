---
name: fix-bug
description: Reproduce, localize, fix, and regression-test a bug, then document the fix.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [bug, fix, debugging, maintenance]
---

# Fix Bug (Workflow)

> Reproduce, localize, fix, and regression-test a bug, then document the fix.

## Outcome

The bug is fixed with a regression test that fails before the fix and passes after,
plus a documented root cause.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 2 | `skill:research/codebase-explorer` | 0.1.0 | localized root cause |
| 4 | `skill:testing/unit-test-generator` | 0.1.0 | regression test |
| 4 | `skill:testing/coverage-gap-finder` | 0.1.0 | gap confirmation |
| 5 | `skill:documentation/doc-writer` | 0.1.0 | fix notes / changelog |

## Steps

1. **Reproduce** — establish a reliable repro; capture expected vs actual.
2. **Localize** — explore the codebase to find the root cause (not just the symptom).
3. **Write a failing test** — encode the bug as a test that currently fails.
4. **Fix** — make the minimal change; confirm the test now passes and others stay green.
5. **Document** — record root cause + fix in the changelog / notes.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| bug_report | yes | Symptoms / repro steps / environment |

## Outputs

A fix + regression test + documented root cause, ready for `review-pr`.

## Failure handling

- Cannot reproduce → stop; request more info (do not "fix" blindly).
- Root cause unclear → widen investigation before changing code.
- Fix breaks other tests → treat as incomplete; revisit root cause.

## Constraints & safety

- Always add a regression test (no fix without a test that would have caught it).
