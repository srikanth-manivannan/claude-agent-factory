# Testing Review Checklist

> Reviews test quality and coverage. Run **after** the
> [Universal Core](_universal.md). Backs the `generate-test-suite` workflow.
> Legend: [README.md](README.md).

**Applies to:** any artifact with `tests/` · **Min standard:** 0.1.0

## Presence & coverage
- [ ] 🔴 `[auto]` Tests exist (`tests/` non-empty).
- [ ] 🔴 `[manual]` Happy path covered.
- [ ] 🟠 `[manual]` Edge/boundary cases covered.
- [ ] 🟠 `[manual]` Failure / refusal cases covered.
- [ ] 🟡 `[auto]` Coverage meets the configured threshold (→ `coverage-gap-finder`).

## Quality of tests
- [ ] 🟠 `[manual]` Tests are deterministic (no flakiness, no time/order coupling).
- [ ] 🟡 `[manual]` Tests assert behavior, not implementation details.
- [ ] 🟡 `[manual]` Tests are isolated and reasonably fast.

## Data & execution
- [ ] 🟡 `[manual]` Test data via `test-data-generator`; no real PII/secrets.
- [ ] 🟡 `[auto]` Tests run green in CI.
