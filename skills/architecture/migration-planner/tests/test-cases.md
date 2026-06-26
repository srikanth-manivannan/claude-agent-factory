# Tests & Validation Guidance — Migration Planner

> Behavior cases + validation. Conforms to
> [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no placeholders).
3. **Behavior:** run each case and check the expectation.

## Behavior cases

### 1 — Happy path
- **Given:** source + decided target + low risk tolerance.
- **Then:** returns a strangler-fig phased plan; every phase has rollback +
  verification; data approach is expand/contract; includes risk register + assumptions.

### 2 — Edge: justified big-bang
- **Given:** tiny low-risk system with an accepted downtime window.
- **Then:** chooses big-bang with a tested backup/restore rollback and records the
  justification.

### 3 — Edge: missing constraints
- **Given:** no downtime budget / risk tolerance.
- **Then:** assumes low risk + ~zero downtime, states the assumption, proceeds.

### 4 — Failure/refusal: target not decided
- **Given:** source but no decided target.
- **Then:** stops and routes to `architecture/tradeoff-analyzer`; does not plan to an
  undecided target.

### 5 — Safety: every phase reversible
- **Given:** any valid plan.
- **Then:** no phase lacks a stated, testable rollback.

## Fixtures

None required (pure-reasoning skill; inputs specify cases).
