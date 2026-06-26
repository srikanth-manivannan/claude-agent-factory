# Workflow Author Guide

> How to author a **workflow** — a repeatable sequence of engineering activities that
> composes ≥2 skills (and optional agents) into an **outcome**
> ([/standards/architecture.md](../../standards/architecture.md)). Reference models: the
> 10 scaffolded flagships in [/workflows/](../../workflows/).

## 1. Scaffold

```sh
sh generators/bin/new-workflow <name> <skill-id> <skill-id> [more...]
# e.g. new-workflow ship-feature backend/openapi-designer testing/unit-test-generator
```

Creates `workflows/<name>/` with `WORKFLOW.md`, `README.md`, `metadata.yaml`,
`CHANGELOG.md`. Name is **outcome-based** (`build-feature`, `fix-bug`).

## 2. Define the orchestration (WORKFLOW.md)

- **Outcome** — the state of the world after a successful run.
- **Composition** — the skills/agents it sequences (name + min version).
- **Steps** — ordered; each step says which skill/agent runs and its inputs/outputs.
- **Failure handling** — retries, rollback, partial-completion behavior.

## 3. The ≥2-skills invariant

A workflow **must orchestrate ≥2 skills** — enforced by
[workflow.schema.yaml](../../shared/schemas/workflow.schema.yaml) (`composes.skills`
`minItems: 2`). A single-capability "workflow" should be a **skill** instead. The
generator pads with placeholder skills if you give fewer than two — replace them.

## 4. Composition rules

- Reference, never copy. Point **down** to skills/agents (and optional upstream
  workflows). No upward references.
- References may be **declared-pending** (target skill not built yet) — these are
  warnings, not failures, until the skill exists (the Wave pattern).

## 5. Prove & register

```sh
sh scripts/validate
```
Add a row to [/WORKFLOWS.md](../../WORKFLOWS.md) (the library catalog) and self-review
with the [universal core](../../standards/checklists/_universal.md) + the matching
domain checklist (e.g. `security-review` for a security workflow).
