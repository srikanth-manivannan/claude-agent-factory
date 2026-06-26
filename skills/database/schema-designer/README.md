# Schema Designer

> Use this to design a normalized, intentional database schema from requirements and access patterns.

**Category:** database · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Turns requirements + access patterns into an **intentional, normalized schema** with
keys, constraints, and access-pattern-driven indexes — plus a rationale for every
non-obvious choice. It pushes data integrity into the schema (not just app code) and
flags sensitive columns, producing migration-ready DDL for your engine.

## Quickstart

```text
1. Copy skills/database/schema-designer/ into your skills directory.
2. Invoke with: requirements + access_patterns (+ engine, scale).
3. Receive engine-specific DDL + rationale + integrity/growth notes.
```

## How it works

Seven steps: model entities → normalize (3NF, deliberate denormalization) → keys →
integrity constraints → access-pattern indexes → plan for change/scale → emit DDL +
rationale. Authoritative procedure in [SKILL.md](SKILL.md); build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

## Inputs & outputs

- **Inputs:** `requirements`, `access_patterns`, optional `engine`, `scale`.
- **Outputs:** entity model + DDL + rationale + integrity/growth notes (migration-ready).

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Engine** — emit Postgres/MySQL/etc. dialect.
- **Normalization stance** — adjust deliberate denormalization for read-heavy systems.
- **Chain** into the `database-migration` workflow to apply it safely.

## Limitations

- Designs the schema; it does not write/run migrations (that's `database-migration`).
- Index recommendations are access-pattern-based, not workload-measured (pair with
  `database/query-optimizer` *(planned)* once live).

## Related

See [RESOURCES.md](RESOURCES.md). Feeds the `database-migration` workflow and
`model-data-domain`; pairs with `architecture/system-design-reviewer`; composes into
`team-backend` / `play-ship-backend-service`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
- **Implementation guidance:** [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Future improvements

- Reverse-engineer a schema from existing DDL and report normalization issues.
- Emit an ER diagram (via `documentation/diagram-generator`).
- Workload-aware index recommendations once query stats exist.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
