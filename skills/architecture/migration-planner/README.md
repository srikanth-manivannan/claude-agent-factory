# Migration Planner

> Use this to plan a safe, phased migration with rollback using the strangler-fig pattern.

**Category:** architecture · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Turns a scary "we need to replace X" into an **incremental, reversible plan** — broken
into independently shippable phases, each with a rollback, sequenced to de-risk early.
It defaults to the **strangler-fig** pattern (run old and new side-by-side, shift
traffic gradually) so you are never one cutover away from disaster.

Technology-agnostic and pure-reasoning: it plans a monolith split, a cloud
replatform, a database swap, or a framework migration with the same method.

## Quickstart

```text
1. Copy skills/architecture/migration-planner/ into your skills directory.
2. Invoke with: the source state, the (decided) target state, and constraints.
3. Receive a phased plan with per-phase rollback, data approach, and a risk register.
```

## How it works

Eight steps: confirm source/target/why → inventory & assess → choose strategy →
define phases → plan data migration → define rollback per phase → sequence & gate →
risks & assumptions. Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `source`, `target`, optional `constraints`, `risk_tolerance`.
- **Outputs:** a phased migration plan (strategy, phases with rollback + verification,
  data approach, risk register, assumptions).

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Strategy override** — choose big-bang or parallel-run when justified (recorded).
- **Granularity** — fewer, larger phases vs. many small ones by risk tolerance.
- **Hand off** data mechanics to the `database-migration` workflow.

## Limitations

- Requires a **decided target** — it plans the *how*, not the *what* (use
  `tradeoff-analyzer` for the what).
- It produces a plan, not the execution; pair with the relevant build/release workflows.
- Estimates depend on an accurate scope inventory.

## Related

See [RESOURCES.md](RESOURCES.md). Follows `architecture/tradeoff-analyzer` (target
choice) and `architecture/system-design-reviewer` (target soundness); hands data
work to the `database-migration` workflow; feeds the `play-zero-to-production`
playbook.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Phase-dependency graph output (which phases unblock which).
- Effort/risk scoring per phase to support scheduling.
- A migration "readiness" checklist generated from the plan.
- Integration with `database-migration` for executable data steps.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
