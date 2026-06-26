# Review — Migration Planner

> Review guidance + recorded self-review, per
> [/standards/review-process.md](../../../standards/review-process.md). Run the
> [Universal Core](../../../standards/checklists/_universal.md) first.

## How to review this skill

- Applicable checklists: **Universal Core** + **documentation-review** +
  **testing-review** + **deployment-review** (rollback discipline) +
  **architecture-review** (method soundness).

## Self-review result (v0.1.0)

**Reviewer:** Factory (generation self-review) · **Date:** 2026-06-26 · **Standard:** 0.1.0

**Verdict:** ✅ Approve — no open 🔴/🟠.

### Universal Core
- Structure/naming, required files, no placeholders: **pass**
- metadata ↔ frontmatter, schema validation, versioning: **pass**
- No secrets; dual-use N/A: **pass**

### documentation-review
- README complete; one-sentence description; examples/troubleshooting/resources;
  CHANGELOG updated: **pass**

### testing-review
- Happy + edge + failure/refusal + safety cases: **pass**

### deployment-review (rollback discipline)
- Every phase reversible; data integrity verification specified: **pass**

### architecture-review (method soundness)
- Strangler-fig default; de-risk-early sequencing; justified deviations: **pass**

## Known minor follow-ups (🟡)
- Phase-dependency graph output (README → Future improvements).
- `adr-author` cross-link is to a planned skill (declared-pending).
