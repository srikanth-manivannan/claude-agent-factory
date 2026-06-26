# Changelog — Claude Agent Factory

Repository-level changelog. Format: [Keep a Changelog](https://keepachangelog.com/).
Versioning: SemVer ([/standards/versioning.md](standards/versioning.md)). Per-artifact
changes live in each artifact's own `CHANGELOG.md`.

## [Unreleased]

## [0.1.0] - 2026-06-26 — 🧊 FRAMEWORK FREEZE

The framework is frozen and stable. See
[Release Notes](docs/RELEASE-NOTES-v0.1.0.md) and
[ADR 0001](docs/adr/0001-framework-v0.1.0-freeze.md).

### Added — Foundation
- `VISION.md`, `ARCHITECTURE.md`, `FACTORY.md`, `TAXONOMY.md` (166 skills),
  `WORKFLOWS.md` (54 workflows).
- `standards/` — 13 standards docs + `VERSION` (0.1.0) + 9 review checklists + universal core.
- `shared/schemas/` — 6 JSON-Schema files (skill/agent/team/workflow/playbook + base).
- `templates/` — bundle templates + technology-agnostic block library.

### Added — Tooling
- `scripts/` — `validate` (the gate, == CI), `lint`, `check-placeholders`,
  `check-links`, `build-index` + Python adapter (`scripts/lib/factory.py`).
- `generators/` — `new-skill`, `new-agent`, `new-workflow`, `new-playbook`,
  `new-category` (schema-valid scaffolds).
- `index.json` — generated catalog of all artifacts.

### Added — Reference content
- Architecture reference category: `tradeoff-analyzer`, `system-design-reviewer`,
  `migration-planner`.
- Wave 0 flagships: `unit-test-generator`, `doc-writer`, `secret-scanner`,
  `a11y-auditor`, `openapi-designer`, `prompt-engineer`, `component-scaffold`,
  `ci-pipeline-generator`. (11 skills across 9 categories; all pass the gate.)

### Added — Docs
- Release notes, ADR 0001, Contributor Guide, and Skill/Agent/Workflow/Playbook
  Author Guides under `docs/`.

### Added — Open-source release preparation
- `LICENSE` (MIT), production `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `SECURITY.md`, `.gitignore`.
- `.github/`: issue templates (bug, skill request) + config, PR template, `CODEOWNERS`,
  and the `validate` CI workflow.
- Guides: Getting Started, Create Your First Skill, Validation & CI; plus FAQ,
  Release Checklist, and Mermaid architecture diagrams under `docs/`.
- Materialized previously-described dirs with READMEs: `shared/runtime/` (+ `claude/`),
  `examples/`, `tests/` — closing dead links surfaced by the first-visitor review.

### Decisions (locked)
- 5-tier hierarchy: skill → agent → team / workflow → playbook.
- Validation: shell entrypoints + optional Python adapter (graceful degrade).
- Pending references = warnings; dependency cycles = errors.
- `metadata.yaml` dates must be quoted strings.

### Status
`scripts/validate`: PASS over 21 artifacts. Framework frozen; bulk skill generation
(Wave 1: 25 flagships → Wave 2: 50 production → Wave 3: remaining categories) begins next.
