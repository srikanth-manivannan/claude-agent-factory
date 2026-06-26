# Release Notes — Framework v0.1.0 (Framework Freeze)

**Date:** 2026-06-26 · **Status:** Frozen · **License:** MIT

This release **freezes the framework** of the Claude Agent Factory. The framework —
its vision, architecture, standards, schemas, templates, validation model, generators,
and the 5-tier artifact hierarchy — is now stable. Skills are products generated *by*
this framework; bulk skill generation begins after this freeze.

## Highlights

### Foundation (canonical)
- **[VISION](../VISION.md)** — mission, principles, MIT, Claude-first/expandable.
- **[ARCHITECTURE](../ARCHITECTURE.md)** — repository layout + the runtime seam.
- **[Standards](../standards/)** — 13 standards docs + `VERSION` (0.1.0) + 9 review
  checklists + the universal core.
- **[Schemas](../shared/schemas/)** — 6 JSON-Schema (draft 2020-12) files for the
  5-tier hierarchy (skill → agent → team / workflow → playbook).
- **[Templates](../templates/)** — bundle templates + a technology-agnostic block library.
- **[FACTORY](../FACTORY.md)** — the generation engine (hybrid, gated).
- **[TAXONOMY](../TAXONOMY.md)** (166 skills) + **[WORKFLOWS](../WORKFLOWS.md)** (54).

### Tooling (new in this release)
- **Validation gate** — `scripts/validate` (== CI): `lint`, `check-placeholders`,
  `check-links`, plus schema validation via an optional Python adapter
  ([factory.py](../scripts/lib/factory.py)). Pure-shell basic path; graceful degrade.
- **Catalog** — `scripts/build-index` emits [`index.json`](../index.json).
- **Generators** — `new-skill`, `new-agent`, `new-workflow`, `new-playbook`,
  `new-category` produce schema-valid, standards-compliant scaffolds.

### Catalog content (at release)
- **65 artifacts, all validating:** 38 skills · 6 agents · 4 teams · 12 workflows ·
  5 playbooks, across 15 categories, plus 3 end-to-end [showcases](../examples/showcases/).
- **15 skills are reference-grade** (gold standard); **23 are baseline** skills that
  complete the dependency graph (valid contracts/structure, expanded guidance in
  progress) — see the README "Skill maturity" note.
- The **engineering graph is fully connected**: zero unresolved dependencies.

## Validation status
`scripts/validate`: **PASS** over 65 artifacts — 0 errors, 0 unresolved dependencies.
Remaining warnings are "recommended file" suggestions on non-skill artifacts (informational).

## What "frozen" means
Breaking changes to the architecture, standards, schema shapes, or the artifact format
now require a **MAJOR** standards bump + migration note ([versioning](../standards/versioning.md)).
Additive skills/workflows/categories are MINOR and do **not** unfreeze the framework.

## Next: systematic generation
- **Wave 1** — 25 flagship skills.
- **Wave 2** — 50 production skills.
- **Wave 3** — remaining categories.

## Known limitations / follow-ups
- Generators are heredoc-based (not yet template-copy) — see [ADR 0001](adr/0001-framework-v0.1.0-freeze.md).
- Schema/link validation requires Python; pure-shell path covers structure only.
- Many cross-links are intentionally "declared-pending" until their skills exist.
- `agents/`, `teams/`, `playbooks/` have schemas + generators but no content yet.
