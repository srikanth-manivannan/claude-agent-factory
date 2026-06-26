# Schemas

> The **formal, machine-validatable** definition of every artifact's `metadata.yaml`.
> JSON Schema (draft 2020-12), authored in YAML. These are the authoritative spec for
> validation; the human companion is [`/standards/metadata.md`](../../standards/metadata.md).
> Run by `scripts/validate` and CI (ARCHITECTURE §14).

## Structure

`metadata.schema.yaml` is the **base** (shared identity, versioning, runtime,
provenance, and reusable `$defs`). Each artifact schema **extends it** via
`allOf: [$ref metadata.schema.yaml]`, adds its composition fields, and closes the
object with `unevaluatedProperties: false`.

| Schema | Tier | Composition | Key constraint |
|--------|------|-------------|----------------|
| [metadata.schema.yaml](metadata.schema.yaml) | base | — | shared fields + `$defs` |
| [skill.schema.yaml](skill.schema.yaml) | Skill | `dependencies` | `category` required |
| [agent.schema.yaml](agent.schema.yaml) | Agent | `uses_skills` (≥1) | applies skills |
| [team.schema.yaml](team.schema.yaml) | Team | `composes.agents` (≥1) | collection of agents |
| [workflow.schema.yaml](workflow.schema.yaml) | Workflow | `composes.skills` (**≥2**) + agents | ≥2 skills (Phase 7 invariant) |
| [playbook.schema.yaml](playbook.schema.yaml) | Playbook | `composes.teams` (≥1) + `composes.workflows` (≥1) | composes teams + workflows |

## Reusable `$defs` (in the base)

- `semver` — `MAJOR.MINOR.PATCH`
- `slug` — kebab-case identifier ([naming.md](../../standards/naming.md))
- `techProfileField` — a tech-profile value (may be `n/a`)
- `reference` — `{ name, min_version }` for composition

## Hierarchy

See [`/standards/architecture.md`](../../standards/architecture.md):
`Skill → Agent → Team / Workflow → Playbook`.
