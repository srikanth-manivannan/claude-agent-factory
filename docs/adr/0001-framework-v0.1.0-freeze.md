# ADR 0001 — Framework v0.1.0 Freeze

**Status:** Accepted · **Date:** 2026-06-26 · **Owner:** Srikanth Manivannan
**Implements / depends on:** [VISION](../../VISION.md), [ARCHITECTURE](../../ARCHITECTURE.md),
[FACTORY](../../FACTORY.md), [standards](../../standards/).

## Context

The framework (vision, architecture, standards, schemas, templates, validation model,
cross-category interactions) was validated by the Architecture reference category
(Phase 9) and Wave 0 (8 flagship skills across 9 categories). Before generating 150+
skills, we need the framework itself to be stable so that mass-generated artifacts
inherit a fixed, trustworthy contract. "The framework is the product; skills are
products it generates."

## Decision

**Freeze the framework as v0.1.0.** Concretely:

1. **Artifact format & hierarchy are fixed** — 5 tiers (skill → agent → team /
   workflow → playbook), each with a schema in `/shared/schemas/`.
2. **Standards are the law** (`standards/VERSION` = 0.1.0); changes that break existing
   artifacts require a **MAJOR** standards bump + migration note.
3. **`scripts/validate == CI`** is the single gate; the Python adapter is optional,
   with graceful degrade.
4. **Generators emit the canonical structure** and must produce gate-passing artifacts.
5. **Bulk generation proceeds in waves** (1: 25 flagships, 2: 50 production, 3: rest)
   and is **additive** (MINOR) — it does not unfreeze the framework.

## Decisions locked here

| Decision | Choice | Consequence |
|----------|--------|-------------|
| Validation runtime | Shell entrypoints + optional Python adapter | No required runtime for basic checks; full schema/link validation when Python present |
| Pending references | Warning, not error | Workflows may reference not-yet-built skills ("declared-pending") without failing the gate |
| Generator implementation | Heredoc-based (not template-copy) | Guarantees valid output now; `templates/skill/` not yet 1:1 with the gold standard |
| Date encoding | Quoted strings in `metadata.yaml` | Bare YAML dates parse as date objects and fail the schema |
| Cycle policy | Hard error | The dependency graph must stay acyclic (ARCHITECTURE §17) |

## Alternatives considered

- **Pure-shell validation (no Python):** rejected — real JSON-Schema (draft 2020-12,
  `$ref`) validation isn't practical in shell, and schema enforcement caught real bugs.
- **Require Python for all tooling:** rejected — violates "no required runtime" for the
  basic path and raises the contribution barrier.
- **Template-copy generators:** deferred — requires aligning `templates/` with the
  gold standard first; tracked as a post-freeze improvement.
- **Fail on pending references:** rejected — would make the repo red while skills are
  legitimately pending across waves.

## Consequences

- **Positive:** mass generation inherits a fixed, validated contract; contributors get
  a real gate and one-command scaffolding; the repo stays green through the waves.
- **Negative / debt:** generator/template duplication until template-copy lands; Python
  needed for full validation; pending-reference warnings accumulate until skills exist.

## Follow-ups (post-freeze, non-blocking)
- Align `templates/skill/` with the gold standard, then switch generators to template-copy.
- Add a CI workflow that installs the adapter and runs `scripts/validate` on every PR.
- Add a "pending reference" allowlist/convention to distinguish intended from broken.
