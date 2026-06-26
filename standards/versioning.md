# Versioning Standard

> Two-layer SemVer for the repository and for every artifact. Implements VISION §12.
> Enforced by the schemas and the [release](checklists/release-review.md) /
> [maintenance](checklists/maintenance-review.md) checklists.

**Min standard:** 0.1.0 · See also: [metadata.md](metadata.md), [review-process.md](review-process.md).

## Two layers

1. **Repository version** — the collection as a whole (`/VERSION`, `/CHANGELOG.md`).
2. **Per-artifact version** — every skill/agent/team/workflow/playbook carries its own
   `version` in `metadata.yaml` and its own `CHANGELOG.md`.

Both use SemVer `MAJOR.MINOR.PATCH` (`^\d+\.\d+\.\d+$`).

## Bump rules (per artifact)

| Bump | When |
|------|------|
| **MAJOR** | Breaking change to behavior, inputs, or contract |
| **MINOR** | Backward-compatible new capability |
| **PATCH** | Fix or docs-only change |

The Factory derives the bump from the diff against the contract (FACTORY §9), not by
feel.

## `min_standard`

Every artifact declares `min_standard` — the minimum [standards `VERSION`](VERSION)
it targets. Compatibility is therefore explicit and checkable.

## Standards versioning

The standards layer itself is versioned (`standards/VERSION`):
- **MAJOR** — a change that breaks existing artifacts (requires a migration note).
- **MINOR** — additive clarification.
- **PATCH** — fix.
A standards change updates its doc + [schema](../shared/schemas/) + [checklist](checklists/)
together.

## Deprecation, not deletion

- Superseding an artifact sets `status: deprecated` + `deprecated_by: <name>` in
  `metadata.yaml`.
- Deprecated artifacts are kept for **≥1 MINOR cycle** with a stated replacement
  before removal.

## Changelogs

Every `CHANGELOG.md` follows [Keep a Changelog](https://keepachangelog.com/): an
`[Unreleased]` section plus dated, versioned entries.
