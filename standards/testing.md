# Testing Standard

> What every artifact's `tests/` must cover. "Nothing ships untested" (VISION §6.4).
> Enforced by the [testing-review checklist](checklists/testing-review.md).

**Min standard:** 0.1.0 · See also: [review-process.md](review-process.md).

## Minimum coverage

Every artifact's `tests/` must cover at least:

1. **Happy path** — the intended use produces the intended result.
2. **Edge / boundary** — empty input, large input, unusual-but-valid cases.
3. **Failure / refusal** — invalid or unsafe input fails gracefully (ties to
   [security.md](security.md)).

## Quality bar for tests

- **Deterministic** — no flakiness; no dependence on time, order, or network.
- **Behavior, not implementation** — assert observable outcomes.
- **Isolated and fast** — independent of other artifacts and external state.
- **Safe data** — use generated test data; never real PII/secrets.

## Two tiers (ARCHITECTURE §14)

- **Local tests** live in each artifact's `tests/` (behavior).
- **Global tests** in [`/tests/`](../tests/) check consistency, schema, links, docs.
- **`scripts/validate` == CI** — the same checks run locally and in CI.

## Composition testing

Workflows/teams/playbooks must verify their references resolve at the declared
versions (`tests/links/`) — see [metadata.md](metadata.md) and
[architecture.md](architecture.md).
