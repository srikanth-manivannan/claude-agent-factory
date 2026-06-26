# Metadata Standard

> The human-readable companion to the machine schemas. Every artifact carries a
> `metadata.yaml`; this doc explains the fields, and
> [`/shared/schemas/`](../shared/schemas/) enforces them. **The schema is
> authoritative** for validation — this doc explains *why* and *how*.

**Min standard:** 0.1.0 · See also: [naming.md](naming.md), [versioning.md](versioning.md),
[architecture.md](architecture.md).

## Why a separate machine file

`metadata.yaml` lets `tests/`, `generators/`, and the catalog index read an artifact
without parsing prose. It must **agree with the spec file's frontmatter** (checked by
the universal checklist).

## Field groups

| Group | Fields | Notes |
|-------|--------|-------|
| Identity | `name`, `title`, `description`, `type` | `type` ∈ skill/agent/team/workflow/playbook/prompt/example |
| Classification | `category`, `tags` | `category` **required for skills** ([naming.md](naming.md)) |
| Tech profile | `tech_profile.{technology,language,stack,toolchain,domain}` | how an artifact "supports any technology" — as **data**, fields may be `n/a` |
| Versioning | `version`, `min_standard`, `status`, `deprecated_by` | see [versioning.md](versioning.md) |
| Maturity | `status` (`active`/`draft`/`deprecated`), `maturity` (`gold`/`baseline`/`draft`) | content depth; see the [maturity model](../README.md#maturity-model) |
| Runtime | `runtime` | the runtime seam (ARCHITECTURE §19); `claude` today |
| Provenance | `license`, `author`, `created`, `updated` | `license: MIT` (inbound = outbound) |
| Composition | `dependencies` / `uses_skills` / `composes` | shape depends on `type` (see below) |

## Composition by type (the hierarchy)

The composition field differs per artifact type, matching [architecture.md](architecture.md):

| Type | Composition field | Points to |
|------|-------------------|-----------|
| skill | `dependencies` (usually empty) | shared building blocks |
| agent | `uses_skills` (≥1) | skills |
| team | `composes.agents` (≥1) | agents |
| workflow | `composes.{skills,agents}` (**≥2 skills**) | skills, agents |
| playbook | `composes.{teams,workflows}` | teams + workflows |

All references are `{ name, min_version }` and must resolve (see
[review-process.md](review-process.md); checked by `tests/links/`).

## Canonical templates

- Annotated example: [`/templates/_meta/metadata.yaml`](../templates/_meta/metadata.yaml)
- Reusable block: [`/templates/blocks/Metadata.yaml`](../templates/blocks/Metadata.yaml)
- Schemas: [`/shared/schemas/`](../shared/schemas/) (one per type, all extending
  `metadata.schema.yaml`).
