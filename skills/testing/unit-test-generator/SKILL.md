---
name: unit-test-generator
description: Use this to generate thorough unit tests for a unit of code, covering happy, edge, and failure cases.
version: 0.1.0
category: testing
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [testing, unit-tests, coverage, quality, tdd]
---

# Unit Test Generator

> Use this to generate thorough unit tests for a unit of code, covering happy, edge, and failure cases.

> **Tech profile** — Technology: any · Language: any · Stack: any test framework · Toolchain: any · Domain: testing
> *(Adapts to the target language/framework via the tech profile; the method is universal.)*

## When to use this skill

- Adding tests to new or untested code (a function, class, or module).
- Backfilling coverage before a refactor (`refactor-module` workflow).
- Establishing a regression test for a bug (`fix-bug` workflow).

## When NOT to use this skill

- End-to-end / integration flows — use `testing/e2e-test-builder` / `integration-test-builder`.
- Assessing existing test quality — use `testing/coverage-gap-finder` or mutation testing.

## Prerequisites

- The unit under test (code or a precise behavior spec).
- The target test framework (detected from the project, or stated).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `unit` | yes | The function/class/module to test |
| `framework` | no | Test framework; inferred from the project if omitted |
| `behavior_spec` | no | Intended behavior, if not obvious from the code |

## Instructions

1. **Understand the contract.** Identify the unit's inputs, outputs, side effects,
   and error conditions. If behavior is ambiguous, ask rather than assume.
2. **Enumerate cases** across three mandatory classes ([/standards/testing.md](../../../standards/testing.md)):
   - **Happy path** — typical valid inputs → expected outputs.
   - **Edge / boundary** — empty, max, min, null, unusual-but-valid inputs.
   - **Failure / refusal** — invalid input handled gracefully (no silent failure).
3. **Detect the framework + conventions.** Match the project's existing test style,
   naming, and assertion library. Don't introduce a new framework.
4. **Write isolated, deterministic tests.** No reliance on time, order, network, or
   shared state; stub/mock external dependencies; use generated, non-real data.
5. **Assert behavior, not implementation.** Test observable outcomes so tests survive
   refactors.
6. **Name tests by intent.** `it("returns 0 for an empty list")`, not `test1`.
7. **Report coverage intent.** State which branches/cases are and are not covered, and
   why any are intentionally omitted.

## Output

A test file (or files) in the project's framework: organized, named-by-intent tests
covering happy/edge/failure classes, with mocks for external dependencies and a short
note on coverage intent.

## Constraints & safety

- **No real PII/secrets** in fixtures ([/standards/security.md](../../../standards/security.md)).
- **No flaky tests** — determinism is non-negotiable.
- **Don't change the unit under test.** If the code is untestable, report *why* and
  recommend a refactor rather than silently editing it.

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** a `divide(a, b)` function.
**Produces:** tests for normal division (happy), division by zero (failure), and large
/ negative / zero operands (edge), each named by intent and isolated.
