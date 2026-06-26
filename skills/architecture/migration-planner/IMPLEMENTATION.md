# Implementation Guidance — Migration Planner

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Confirm source, target, and "why"** — if the target isn't decided, route to
   `architecture/tradeoff-analyzer` first.
2. **Inventory & assess** components/data/integrations; find the seams where old + new coexist.
3. **Choose strategy** — default strangler-fig; big-bang only if justified + low-risk.
4. **Define phases** — each independently shippable AND reversible, with verification.
5. **Plan data** (expand/contract) and **rollback per phase**; sequence to de-risk early.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Strategy | Strangler-fig by default; record any deviation's rationale |
| Data | Dual-write → backfill → verify → cut-read (zero-downtime) |
| Sequencing | Riskiest/most-uncertain phases first |

## Pitfalls

- ❌ A phase with no rollback → ✅ every phase has a tested rollback or it isn't ready.
- ❌ One giant phase → ✅ decompose along seams.
- ❌ Migrating to an undecided target → ✅ decide first.

## Hand-off

Data mechanics hand off to the `database-migration` workflow; the plan feeds
`play-zero-to-production` and is recorded via `architecture/adr-author`.
