# Skill Author Guide

> How to author a **skill** — a reusable capability (the leaf of the hierarchy,
> [/standards/architecture.md](../../standards/architecture.md)). Reference model: the
> [architecture category](../../skills/architecture/) (Phase 9 gold standard).

## 1. Scaffold

```sh
sh generators/bin/new-skill <category> <name> "Use this to <one action-oriented sentence>."
```

Creates `skills/<category>/<name>/` with the canonical **10 files**:

| File | Purpose | Standard |
|------|---------|----------|
| `SKILL.md` | The skill: frontmatter + instructions | [documentation](../../standards/documentation.md), [prompt-engineering](../../standards/prompt-engineering.md) |
| `README.md` | GitHub-quality overview + Future improvements + Version history | [documentation](../../standards/documentation.md) |
| `metadata.yaml` | Machine metadata (schema-validated) | [metadata](../../standards/metadata.md) |
| `IMPLEMENTATION.md` | **Required.** How to apply the skill: build order, decisions, pitfalls, hand-off | [documentation](../../standards/documentation.md) |
| `EXAMPLES.md` | Worked examples (happy/edge/anti) | — |
| `TROUBLESHOOTING.md` | Symptom → cause → fix | — |
| `RESOURCES.md` | References + hierarchy cross-links | — |
| `REVIEW.md` | Review guidance + recorded self-review | [review-process](../../standards/review-process.md) |
| `CHANGELOG.md` | Version history (Keep a Changelog) | [versioning](../../standards/versioning.md) |
| `tests/test-cases.md` | Validation guidance + behavior cases | [testing](../../standards/testing.md) |

> **`IMPLEMENTATION.md` is required for skills** (`scripts/validate` fails without it).

## 2. Author the contract (SKILL.md)

- **`description`**: one action-oriented sentence ("Use this to…") — must match
  `metadata.yaml` exactly.
- **When to / not to use**, **Inputs**, **Instructions** (imperative, ordered),
  **Output**, **Constraints & safety**.
- Keep the body **technology-neutral**; put stack specifics in the **Tech profile** /
  inputs (this is how a skill "supports any technology").

## 3. Metadata rules

- `type: skill`, `category` matches the folder, `dependencies: []` unless it composes
  shared building blocks.
- **Quote dates** (`created: "2026-06-26"`) — bare YAML dates fail the schema.
- Validated against [skill.schema.yaml](../../shared/schemas/skill.schema.yaml).

## 4. Tests (mandatory)

Cover **happy + edge + failure/refusal** ([testing standard](../../standards/testing.md)).
Deterministic; no real PII/secrets.

## 5. Prove & register

```sh
sh scripts/validate          # must be green
```
Then add a row to [/TAXONOMY.md](../../TAXONOMY.md) and self-review with the
[universal core](../../standards/checklists/_universal.md) + domain checklist.

## Quality bar (what "gold standard" means)

Trace every section to a standard; cross-reference don't duplicate; examples that run;
honest limitations; a recorded self-review verdict. See
[tradeoff-analyzer](../../skills/architecture/tradeoff-analyzer/) as the canonical example.
