# Agent Author Guide

> How to author an **agent** — an AI specialist that applies one or more skills
> (tier 2 of [/standards/architecture.md](../../standards/architecture.md)).

## 1. Scaffold

```sh
sh generators/bin/new-agent <name> <skill-id> [more-skill-ids...]
# e.g. new-agent code-reviewer code-quality/lint-runner testing/unit-test-generator
```

Creates `agents/<name>/` with `AGENT.md`, `README.md`, `metadata.yaml`, `CHANGELOG.md`.
Name is **role-based** (`code-reviewer`, `release-manager`; [naming](../../standards/naming.md)).

## 2. Define the role (AGENT.md)

- **Role & responsibilities** — and explicit boundaries (what it hands off).
- **Skills used** — reference each by `name` + min version; **never copy** skills.
- **Operating instructions** — its decision procedure and when it invokes each skill.
- **Constraints & safety** — per [security](../../standards/security.md).

## 3. Metadata rules

- `type: agent`; **`uses_skills` ≥ 1** (the schema enforces this — an agent with no
  skills should be a skill or a prompt).
- Each `uses_skills` entry `{ name: <category>/<skill>, min_version }` must resolve
  (or be intentionally pending until that skill exists).
- Validated against [agent.schema.yaml](../../shared/schemas/agent.schema.yaml).

## 4. Composition rules

- Agents point **down** to skills only (ARCHITECTURE §17). No agent→workflow refs.
- Agents are composed **up** into teams and workflows — keep them single-purpose and
  reusable.

## 5. Prove

```sh
sh scripts/validate
```
Self-review with the [universal core](../../standards/checklists/_universal.md). Tests
are recommended for agents (required for skills).

## Note (v0.1.0)

No agents exist yet — agents arrive with the teams/playbooks they staff. This guide +
the schema + generator are ready; the first agents will set the agent gold standard the
way `tradeoff-analyzer` set it for skills.
