---
name: tradeoff-analyzer
description: Use this to weigh multiple options against weighted criteria and produce a defensible recommendation.
version: 0.1.0
category: architecture
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [architecture, decision-making, tradeoffs, analysis, adr]
---

# Tradeoff Analyzer

> Use this to weigh multiple options against weighted criteria and produce a defensible recommendation.

> **Tech profile** — Technology: any · Language: n/a · Stack: n/a · Toolchain: n/a · Domain: architecture
> *(Pure reasoning skill — applies to any technology decision.)*

## When to use this skill

- When choosing between ≥2 viable options (libraries, designs, vendors, patterns).
- When a decision needs a written, defensible rationale (e.g. feeding an ADR).
- When stakeholders disagree and need an explicit, criteria-based comparison.

## When NOT to use this skill

- When there is only one viable option — there is no trade-off to analyze.
- For pure fact lookup (use a research skill).
- For designing a system from scratch (use `architecture/system-design-reviewer`
  to critique a design, or an `architecture` design skill).

## Prerequisites

- A decision to make and the candidate options (or enough context to enumerate them).
- The constraints that matter (budget, deadline, team skills, compliance).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `decision` | yes | The decision to be made, in one sentence |
| `options` | yes | The candidate options (≥2); may be elicited if not given |
| `criteria` | no | Evaluation criteria; derived from constraints if omitted |
| `weights` | no | Relative importance per criterion; defaults to equal |
| `constraints` | no | Hard constraints that disqualify an option outright |

## Instructions

1. **Frame the decision.** Restate it in one sentence and confirm the options
   (minimum two). If only one option exists, stop and say so.
2. **Apply hard constraints first.** Eliminate any option that violates a
   non-negotiable constraint; record why. Never silently drop an option.
3. **Establish criteria + weights.** Derive 4–7 decision criteria from the
   constraints and goals. Assign each a weight (sum = 100%). State the rationale
   for the weighting — this is where bias hides, so make it explicit.
4. **Score each option per criterion.** Use a consistent scale (1–5). For each
   score, give a one-line justification grounded in evidence, not vibes.
5. **Compute weighted totals.** Multiply scores by weights; sum per option.
   Present the full matrix (see Output).
6. **Run a sensitivity check.** Ask: would a reasonable change in the top one or two
   weights flip the result? If yes, flag the decision as *weight-sensitive*.
7. **Recommend.** State the winning option, the margin, the key reasons, and the
   main risk of choosing it. If it is weight-sensitive or close, say so plainly.
8. **Record assumptions.** List every assumption made; these are what a reviewer
   should challenge.

## Output

A decision analysis containing:

- The framed decision and the final option set (with any eliminated options + why).
- A **weighted scoring matrix** (options × criteria, scores, weighted totals).
- A **recommendation** with margin, top reasons, and primary risk.
- A **sensitivity note** (is the result robust?).
- An **assumptions** list.

This output is ADR-ready: it drops directly into an ADR's "Decision" and
"Consequences" sections.

## Constraints & safety

- **Never fabricate scores.** If evidence for a score is missing, mark it as an
  assumption (step 8) rather than inventing certainty.
- **Surface bias.** The weighting step must state *why* each weight was chosen.
- **No false precision.** Weighted totals are a decision aid, not a proof; a 0.1
  margin is a tie — say so.
- Conforms to [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md)
  and [/standards/security.md](../../../standards/security.md).

## Examples

A minimal example is below; full worked examples are in [EXAMPLES.md](EXAMPLES.md).

**Given:** Decision = "Which datastore for the events service?", Options =
[PostgreSQL, DynamoDB], Criteria = [operational-cost, query-flexibility,
team-familiarity, scalability].
**Produces:** a 2×4 weighted matrix, a recommendation (e.g. *PostgreSQL, margin
0.6, weight-sensitive on scalability*), and the assumptions behind it.
