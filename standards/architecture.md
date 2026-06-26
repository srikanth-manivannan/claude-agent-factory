# Architecture Standard

> The canonical **artifact hierarchy** and **composition rules** every artifact must
> obey. This is the authoritative statement of the five tiers; the repository-level
> [`/ARCHITECTURE.md`](../ARCHITECTURE.md) describes the folder layout that hosts them.
> Enforced by the schemas + `tests/links/` (dependency-graph checks).

**Min standard:** 0.1.0 · See also: [metadata.md](metadata.md), [naming.md](naming.md).

## The five tiers

| Tier | Is | Composes | Schema |
|------|----|----------|--------|
| **Skill** | a reusable capability | (leaf; `shared/` only) | [skill.schema.yaml](../shared/schemas/skill.schema.yaml) |
| **Agent** | an AI specialist that applies skills | **skills** (≥1) | [agent.schema.yaml](../shared/schemas/agent.schema.yaml) |
| **Team** | a coordinated collection of agents | **agents** (≥1) | [team.schema.yaml](../shared/schemas/team.schema.yaml) |
| **Workflow** | a repeatable sequence of engineering activities | **skills (≥2)** + agents | [workflow.schema.yaml](../shared/schemas/workflow.schema.yaml) |
| **Playbook** | a higher-level operating guide for a complete outcome | **teams + workflows** | [playbook.schema.yaml](../shared/schemas/playbook.schema.yaml) |

```
Playbook ── composes ──▶ Teams ── composes ──▶ Agents ── apply ──▶ Skills ──▶ shared/
    └──────── composes ──▶ Workflows ──▶ Skills (≥2) + Agents ─────────────▶
```

## Composition rules (non-negotiable)

1. **Reference, never copy.** Composition uses `{ name, min_version }` and points to
   the artifact's canonical home (single source of truth).
2. **Point down the hierarchy only.** Playbook→{team,workflow}→{agent}→{skill}→shared.
   No upward or sideways-into-a-peer references.
3. **Acyclic.** The dependency graph must never contain a cycle (`tests/links/`).
4. **A workflow orchestrates ≥2 skills.** A single-capability "workflow" should be a
   skill instead (the Phase 7 invariant; enforced in `workflow.schema.yaml`).
5. **References must resolve** at the declared `min_version` before merge.

## The runtime seam (expansion)

The artifact **format is portable**; the **runtime is pluggable**
([`/shared/runtime/claude/`](../shared/runtime/)). Adding a model is additive — no
artifact rewrites (VISION §15, ARCHITECTURE §19). `runtime: claude` today.

## Relationship to `/ARCHITECTURE.md`

`/ARCHITECTURE.md` defines the **folders** (`skills/`, `agents/`, `teams/`,
`workflows/`, `playbooks/`, `shared/`, …). **This standard defines the conceptual
**tiers and their composition. Where they describe the same thing they must agree;
this standard governs the hierarchy semantics.
