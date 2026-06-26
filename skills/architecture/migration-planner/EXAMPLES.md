# Examples — Migration Planner

> Worked plans. Method is technology-agnostic; specifics come from source/target.
> See [SKILL.md](SKILL.md).

## Example 1 — Extract auth from a monolith (happy path, strangler-fig)

**Input:** source = monolith with embedded auth; target = standalone auth service;
risk tolerance = low; downtime budget = ~zero.

**Strategy:** strangler-fig (facade routes auth calls; migrate incrementally).

| Phase | Scope | Verification | Rollback |
|-------|-------|--------------|----------|
| 1 | Introduce auth facade/routing in front of monolith auth | traffic unchanged, latency flat | remove facade (no-op) |
| 2 | Stand up new auth service; mirror reads (shadow) | shadow results match monolith | disable mirroring |
| 3 | Cut **read** path to new service | login/validate works; error rate flat | route reads back to monolith |
| 4 | Cut **write** path (dual-write → backfill → cut) | data integrity checks pass | revert to monolith writes |
| 5 | Decommission monolith auth | no traffic to old path for N days | re-enable old path |

**Data approach:** expand/contract — dual-write during phase 4, backfill historical
users, verify counts/hashes, then cut reads.
**Risks:** session compatibility (mitigate: shared token format); **Assumptions:**
user volume migratable within the backfill window.

## Example 2 — Edge: target not yet decided

**Input:** "We want off our current queue but haven't picked the replacement."

**Behavior:** the planner **stops at step 1** and routes to
`architecture/tradeoff-analyzer` to choose the target first — it will not plan a
migration to an undecided destination.

## Example 3 — Edge: justified big-bang

**Input:** a tiny internal tool, 5 users, accepted maintenance window.

**Behavior:** records that strangler-fig overhead isn't warranted; chooses a big-bang
cutover **with** a full backup + tested restore as the rollback. Justification is
documented (per step 3).

## Anti-example

- ❌ A phase with no rollback ("we'll figure it out if it breaks"). Step 6 forbids
  this — every phase needs a stated, testable rollback before it's ready.

## Try it yourself

- Re-plan Example 1 with a generous downtime budget — which phases simplify?
- Add `compliance: data-residency` to Example 1 — note the new phase/verification.
