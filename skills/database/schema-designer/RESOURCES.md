# Resources — Schema Designer

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md) · **Implementation:** [IMPLEMENTATION.md](IMPLEMENTATION.md).
- **Standards:** [security](../../../standards/security.md),
  [architecture](../../../standards/architecture.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Feeds** | `database-migration` workflow ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | applies the schema safely |
| **Feeds** | `database/migration-writer` *(planned)* | turns DDL into reversible migrations |
| **Pairs with** | [`architecture/system-design-reviewer`](../../architecture/system-design-reviewer/) | reviews the data design |
| **Sibling** | `database/query-optimizer`, `database/index-advisor` *(planned)* | tune once live |
| **Composed into** | `team-backend` → `play-ship-backend-service` ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | backend delivery |

## Concepts & background (vendor-neutral)

- **Normalization** (1NF–3NF) and **deliberate denormalization**.
- **Keys** (surrogate vs natural), **referential integrity**, **constraints**.
- **Access-pattern-driven indexing**; **partitioning/sharding** at scale.

## Provenance & credits

- Method synthesized from standard relational data-modeling practice. No third-party
  content copied; MIT (VISION §13).
