---
name: migration-planner
description: Use this to plan a safe, phased migration with rollback using the strangler-fig pattern.
version: 0.1.0
category: architecture
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [architecture, migration, strangler-fig, rollback, planning]
---

# Migration Planner

> Use this to plan a safe, phased migration with rollback using the strangler-fig pattern.

> **Tech profile** — Technology: any · Language: n/a · Stack: n/a · Toolchain: n/a · Domain: architecture
> *(Pure-reasoning skill — plans migrations between any two technologies/architectures.)*

## When to use this skill

- Migrating from a legacy system/component to a new one with minimal risk.
- Replatforming, re-architecting, or splitting a monolith incrementally.
- Any change too large/risky to do as a single cutover.

## When NOT to use this skill

- Choosing *what* to migrate to — use `architecture/tradeoff-analyzer` first.
- A single reversible schema change — use the `database-migration` workflow.
- Reviewing a target design — use `architecture/system-design-reviewer`.

## Prerequisites

- The **source** (current state) and the **target** (decided end state).
- Risk tolerance, downtime budget, and any hard deadline.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `source` | yes | Current system/architecture being migrated from |
| `target` | yes | Decided end state being migrated to |
| `constraints` | no | Downtime budget, deadline, team, compliance |
| `risk_tolerance` | no | How much risk is acceptable (defaults to low) |

## Instructions

1. **Confirm source, target, and "why".** Restate both states and the driver. If the
   target isn't decided, stop and route to `architecture/tradeoff-analyzer`.
2. **Inventory & assess.** List the components/data/integrations in scope; rank by
   risk and coupling. Identify the **seams** where old and new can coexist.
3. **Choose a strategy.** Default to **strangler-fig** (incrementally route traffic
   from old to new behind a facade). Use big-bang only if explicitly justified and
   low-risk; record the rationale.
4. **Define phases.** Break the migration into independently shippable, independently
   reversible phases. Each phase has: scope, entry/exit criteria, and verification.
5. **Plan data migration.** Prefer expand/contract (dual-write/backfill/cut-read) for
   zero-downtime; specify integrity checks. (For the mechanics, the
   `database-migration` workflow applies.)
6. **Define rollback per phase.** Every phase must be reversible; state the rollback
   trigger and steps. A phase without a tested rollback is not ready.
7. **Sequence & gate.** Order phases by risk (de-risk early); define the go/no-go gate
   between phases.
8. **List risks + assumptions.** Top risks with mitigations; explicit assumptions.

## Output

A phased migration plan: source/target/driver, scope inventory, chosen strategy (+why),
ordered phases (scope, criteria, verification, rollback), the data-migration approach,
a risk register with mitigations, and assumptions.

## Constraints & safety

- **Every phase is reversible.** No phase ships without a stated, testable rollback
  (step 6). Aligns with the
  [deployment-review](../../../standards/checklists/deployment-review.md) checklist.
- **De-risk early.** Sequence the riskiest, most-uncertain phases first when feasible.
- **No silent data loss.** Data phases specify integrity verification.
- Conforms to [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md)
  and [/standards/security.md](../../../standards/security.md).

## Examples

Minimal below; full plans in [EXAMPLES.md](EXAMPLES.md).

**Given:** source = monolith auth, target = dedicated auth service, low risk tolerance.
**Produces:** a strangler-fig plan — facade/routing phase → read-path migration →
write-path migration → decommission, each with rollback and verification.
