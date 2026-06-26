# Implementation Guidance — Tradeoff Analyzer

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Frame** the decision in one sentence; enumerate ≥2 options.
2. **Apply hard constraints** to eliminate options (record why).
3. **Set criteria + weights** (sum 100%) *before* scoring — state the weighting rationale.
4. **Score** each option per criterion (1–5) with a one-line evidence justification.
5. **Total + sensitivity** — compute weighted totals; test if a plausible weight change flips it.
6. **Recommend** with margin + primary risk; record assumptions.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Weights | Derive from goals/constraints, never from preferred option (bias guard) |
| Scale | 1–5 default; 1–10 for finer comparisons |
| Tie (margin ≤ 0.2) | Report as a tie; add a tie-breaker criterion or escalate |

## Pitfalls

- ❌ Setting weights after seeing options → ✅ weights first, justified.
- ❌ Inventing scores → ✅ missing evidence becomes a recorded assumption.
- ❌ Reporting a 0.1 margin as a winner → ✅ call it a tie.

## Hand-off

The analysis drops into an ADR (`architecture/adr-author`) as Decision + Consequences;
feeds `architecture/migration-planner` (target choice) and the `architecture-review` workflow.
