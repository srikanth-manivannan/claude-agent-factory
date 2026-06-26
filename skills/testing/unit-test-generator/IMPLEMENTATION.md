# Implementation Guidance — Unit Test Generator

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/testing.md](../../../standards/testing.md).

## Build order

1. **Understand the contract** — inputs, outputs, side effects, error conditions.
2. **Detect the framework** + project conventions (don't introduce a new one).
3. **Enumerate cases** — happy + edge/boundary + failure/refusal (all three classes).
4. **Write isolated, deterministic tests** — mock external deps; no time/order/network coupling.
5. **Name by intent**; report coverage intent (what's covered + intentional omissions).

## Key decisions

| Decision | Guidance |
|----------|----------|
| Assertion target | Behavior (observable outcomes), not implementation |
| Test data | Generated; never real PII/secrets |
| Untestable code | Report + recommend refactor; never silently edit the unit |

## Pitfalls

- ❌ `sleep`-based timing tests → ✅ control time via mocks (deterministic).
- ❌ Asserting private calls → ✅ assert outputs/side effects (survives refactors).
- ❌ Guessing ambiguous behavior → ✅ ask for the contract.

## Hand-off

Consumed by `frontend/component-scaffold`, `devops/ci-pipeline-generator`, and the
`build-feature`/`fix-bug`/`refactor-module` workflows; pair with `coverage-gap-finder` (planned).
