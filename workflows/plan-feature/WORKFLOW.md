---
name: plan-feature
description: Use this workflow to turn a feature goal into a reviewed, decision-recorded plan.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [workflow, planning, architecture]
---

# Plan Feature (Workflow)

> Use this workflow to turn a feature goal into a reviewed, decision-recorded plan.

A repeatable sequence of activities composing >=2 skills ([/standards/architecture.md](../../standards/architecture.md)).

## Outcome
An approved feature plan: the chosen approach (with rationale), a reviewed design, and
clear acceptance criteria — ready to feed `build-feature`.

## Composition
- `skill:architecture/tradeoff-analyzer` (>= 0.1.0) — choose between approaches.
- `skill:architecture/system-design-reviewer` (>= 0.1.0) — validate the chosen design.

## Steps
1. **Frame the goal** — restate the feature, constraints, and acceptance criteria.
2. **Decide the approach** — run `tradeoff-analyzer` on the viable options; record the
   recommendation and its primary risk.
3. **Review the design** — run `system-design-reviewer`; resolve blocker findings.
4. **Produce the plan** — scope, approach + rationale, risks, acceptance criteria.

## Inputs
| Input | Required | Description |
|-------|----------|-------------|
| goal | yes | The feature to plan + its constraints |

## Outputs
A reviewed feature plan with a recorded decision and acceptance criteria.

## Failure handling
- Only one viable option → skip the trade-off; still review the design.
- Design has blocker findings → resolve before the plan is approved.
