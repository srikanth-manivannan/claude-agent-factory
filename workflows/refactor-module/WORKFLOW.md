---
name: refactor-module
description: Refactor a module safely under a test safety-net without changing behavior.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [refactor, maintenance, quality]
---

# Refactor Module (Workflow)

> Refactor a module safely under a test safety-net without changing behavior.

## Outcome

A module is restructured for clarity/quality with identical external behavior,
proven by a green test suite before and after.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:research/codebase-explorer` | 0.1.0 | understanding + boundaries |
| 2 | `skill:testing/unit-test-generator` | 0.1.0 | safety-net tests |
| 4 | `skill:testing/test-refactorer` | 0.1.0 | improved tests |

## Steps

1. **Understand & bound** — map the module, its callers, and the behavior contract.
2. **Establish a safety net** — ensure characterization tests cover current behavior.
3. **Refactor in small steps** — restructure; keep tests green at each step.
4. **Tidy tests** — refactor brittle/slow tests now that structure improved.
5. **Verify** — full suite green; no behavior change; document notable structural shifts.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target_module | yes | The module/area to refactor |
| goal | yes | What "better" means (readability, perf, decoupling) |

## Outputs

A behavior-preserving refactor with an intact/improved test suite.

## Failure handling

- Inadequate test coverage → build the safety net first (depends on `generate-test-suite`).
- Behavior changes detected → that's a feature/fix, not a refactor — stop and reclassify.

## Constraints & safety

- Refactor ≠ rewrite ≠ behavior change. External behavior must stay identical.
