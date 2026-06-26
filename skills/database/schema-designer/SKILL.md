---
name: schema-designer
description: Use this to design a normalized, intentional database schema from requirements and access patterns.
version: 0.1.0
category: database
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [database, schema, data-modeling, normalization, migrations]
---

# Schema Designer

> Use this to design a normalized, intentional database schema from requirements and access patterns.

> **Tech profile** — Technology: database · Language: SQL/DDL · Stack: any RDBMS · Toolchain: any · Domain: database
> *(Method is engine-agnostic; emit DDL for the target RDBMS via the tech profile.)*

## When to use this skill

- Designing the schema for a new service or feature, before writing migrations.
- Refactoring an ad-hoc/denormalized schema into an intentional model.
- Producing the schema that `database/migration-writer` *(planned)* turns into migrations.

## When NOT to use this skill

- Writing/altering migrations — use the `database-migration` workflow.
- Tuning slow queries — use `database/query-optimizer` *(planned)*.
- High-level domain modeling only — use `architecture/system-design-reviewer` for review.

## Prerequisites

- The entities/relationships the system needs and the **primary access patterns**
  (the queries that must be fast).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `requirements` | yes | What data the system stores and the rules over it |
| `access_patterns` | yes | The key reads/writes (drives keys + indexes) |
| `engine` | no | Target RDBMS (Postgres/MySQL/…); affects types + features |
| `scale` | no | Expected volume/growth (informs partitioning/denormalization) |

## Instructions

1. **Model entities + relationships.** Identify entities, attributes, and
   cardinalities; draw the relationships (1:1, 1:N, M:N → join table).
2. **Normalize to 3NF**, then **denormalize deliberately** only where an access pattern
   demands it — and record *why* (trade-off, not accident).
3. **Define keys.** Choose primary keys (prefer stable surrogate keys); add foreign keys
   with explicit `ON DELETE`/`ON UPDATE` behavior.
4. **Constrain for integrity.** `NOT NULL`, `UNIQUE`, `CHECK`, and enum/domain
   constraints — push invariants into the schema, not just app code.
5. **Index for the access patterns.** Add indexes that serve the stated queries; note
   the write-cost trade-off. Don't index speculatively.
6. **Plan for change + scale.** Timestamps (`created_at`/`updated_at`), soft-delete if
   needed, and a partitioning/sharding note if `scale` warrants.
7. **Emit DDL + rationale.** Produce target-engine DDL and a short rationale per
   non-obvious decision; hand off to the `database-migration` workflow.

## Output

A schema: an entity/relationship description, engine-specific **DDL** (tables, keys,
constraints, indexes), a rationale for each non-obvious choice (normalization,
denormalization, indexing), and notes on integrity and growth. Migration-ready.

## Constraints & safety

- **Integrity in the schema** — constraints enforce invariants; don't rely on app code alone.
- **No PII by accident** — flag columns that hold sensitive data; recommend encryption
  at rest where appropriate ([/standards/security.md](../../../standards/security.md)).
- **Justify denormalization + every index** — both have costs.

## Examples

Minimal below; full enterprise examples in [EXAMPLES.md](EXAMPLES.md); build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

**Given:** an orders system (customers, orders, line items, products) on Postgres,
read-heavy on "orders by customer".
**Produces:** 3NF tables with FKs, a `M:N` line-items join, a composite index on
`orders(customer_id, created_at)`, and a rationale for it.
