# Playbook Author Guide

> How to author a **playbook** — the top tier: a higher-level operating guide that
> composes **teams + workflows** to achieve a complete engineering outcome
> ([/standards/architecture.md](../../standards/architecture.md)).

## 1. Scaffold

```sh
sh generators/bin/new-playbook play-<objective>
# e.g. new-playbook play-zero-to-production
```

Creates `playbooks/<name>/` with `PLAYBOOK.md`, `README.md`, `metadata.yaml`,
`CHANGELOG.md`. Name is **objective-based**, prefixed `play-` ([naming](../../standards/naming.md)).

## 2. Define the operating guide (PLAYBOOK.md)

- **Objective** — the complete outcome (e.g. "take a service from zero to production").
- **Composition** — the teams it coordinates and the workflows it sequences.
- **Operating guide** — the ordered plan that ties them together.
- **Success criteria** — how you know the outcome was achieved.

## 3. Metadata rules

- `type: playbook`; **`composes.teams` ≥ 1 and `composes.workflows` ≥ 1** (schema:
  [playbook.schema.yaml](../../shared/schemas/playbook.schema.yaml)).
- Each ref `{ name, min_version }` must resolve (or be intentionally pending).
- A playbook that composes only workflows (no teams) should probably be a workflow;
  one that composes only one thing isn't a playbook.

## 4. Composition rules

- Points **down** to teams and workflows only (ARCHITECTURE §17) — the top of the
  hierarchy. Nothing composes a playbook.
- See the indicative `play-*` roll-ups in [/WORKFLOWS.md §2](../../WORKFLOWS.md).

## 5. Prove

```sh
sh scripts/validate
```
Self-review with the [universal core](../../standards/checklists/_universal.md) plus the
domain checklists relevant to the outcome.

## Note (v0.1.0)

No playbooks (or teams) exist yet — they arrive after enough skills/workflows are built
to compose meaningfully. The tier, schema, naming, and generator are frozen and ready;
the first playbook will set the playbook gold standard.
