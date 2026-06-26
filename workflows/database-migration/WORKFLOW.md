---
name: database-migration
description: Plan and apply a safe, reversible database migration with verified rollback.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [database, migration, schema]
---

# Database Migration (Workflow)

> Plan and apply a safe, reversible database migration with verified rollback.

## Outcome

A schema change applied safely (ideally zero-downtime), reversible, with rollback
tested before production.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:architecture/migration-planner` | 0.1.0 | phased plan |
| 2 | `skill:database/schema-designer` | 0.1.0 | target schema |
| 3 | `skill:database/migration-writer` | 0.1.0 | reversible migration |

## Steps

1. **Plan** — choose a strategy (expand/contract for zero-downtime); define phases.
2. **Design target schema** — finalize the intended end state.
3. **Write the migration** — forward + reversible down migration.
4. **Test** — run on a copy; verify data integrity and the rollback path.
5. **Apply** — execute by phase; monitor; keep rollback ready.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| change_intent | yes | The schema change required |
| downtime_budget | no | Allowed downtime (default: none → expand/contract) |

## Outputs

A tested, reversible migration + application/rollback runbook.

## Failure handling

- Irreversible change requested → require explicit sign-off + backup plan.
- Rollback untested → block; never apply an unproven migration to production.

## Constraints & safety

- Always reversible (or explicitly backed-up). Test rollback before applying.
