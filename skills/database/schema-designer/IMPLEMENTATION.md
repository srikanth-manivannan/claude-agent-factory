# Implementation Guidance — Schema Designer

> How to go from requirements to migration-ready DDL. See [SKILL.md](SKILL.md) and
> [/standards/](../../../standards/).

## Build order

1. **Entities & relationships first** — get cardinalities right before any DDL.
2. **Normalize to 3NF** — eliminate redundancy; one fact in one place.
3. **Keys** — surrogate PKs (`IDENTITY`/`BIGSERIAL`); FKs with explicit delete behavior.
4. **Constraints** — `NOT NULL`, `UNIQUE`, `CHECK`, enums; encode invariants here.
5. **Indexes** — one per stated access pattern; justify each.
6. **Denormalize last** — only with a recorded read/write trade-off.

## Choosing keys

| Choice | When |
|--------|------|
| Surrogate (`IDENTITY`) | Default — stable, opaque, simple FKs |
| Natural key | Only if truly immutable and externally meaningful |
| Composite PK | Join tables (`(order_id, product_id)`) |

## Index decision rule

> Add an index **iff** it serves a stated read access pattern *and* its write cost is
> acceptable. Composite index column order = equality columns first, then range/sort.

## Integrity over app-code

Prefer schema-level guarantees:
```sql
status TEXT NOT NULL CHECK (status IN ('pending','paid','shipped','cancelled'))
quantity INT NOT NULL CHECK (quantity > 0)
email CITEXT NOT NULL UNIQUE
```
App validation is a UX nicety; the database is the source of truth.

## Handing off to migrations

This skill emits DDL + rationale. Apply it through the
[`database-migration`](../../../WORKFLOWS.md) workflow (expand/contract, reversible,
tested rollback) — never hand-apply to production.

## Sensitive data

Flag PII columns; recommend encryption at rest and access restriction; keep PII out of
search indexes and logs ([/standards/security.md](../../../standards/security.md)).

## Scale notes

Add `created_at`/`updated_at` everywhere; consider partitioning by time/tenant when
`scale` is large; document the partition key choice and its query implications.
