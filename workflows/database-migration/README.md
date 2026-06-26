# Database Migration (Workflow)

> Plan and apply a safe, reversible database migration with verified rollback.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Plans, writes, tests, and applies a schema migration safely — defaulting to a
zero-downtime expand/contract strategy with a proven rollback.

## The flow

`plan → design schema → write migration → test (incl. rollback) → apply`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:database/migration-planner` (≥ 0.1.0)
- `skill:database/schema-designer` (≥ 0.1.0)
- `skill:database/migration-writer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** change intent, optional downtime budget.
- **Outputs:** tested reversible migration + runbook.

## Customization

Pair with `release-pipeline` to coordinate the migration with a deploy.

## Limitations

- Irreversible changes require explicit sign-off + a backup plan.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
