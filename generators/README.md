# Generators — The Factory's hands

> Pure-shell scaffolders that produce **standards-compliant, schema-valid** artifacts
> from the canonical structure. No runtime required (ARCHITECTURE §9). These are the
> deterministic scaffolding layer of the Factory (FACTORY.md §1).

## Commands

| Generator | Creates | Key rule (from the schemas) |
|-----------|---------|-----------------------------|
| [`bin/new-skill`](bin/new-skill) | `skills/<category>/<name>/` (9-file gold-standard) | `category` required; `dependencies: []` |
| [`bin/new-agent`](bin/new-agent) | `agents/<name>/` | `uses_skills` ≥ 1 |
| [`bin/new-workflow`](bin/new-workflow) | `workflows/<name>/` | `composes.skills` ≥ 2 |
| [`bin/new-playbook`](bin/new-playbook) | `playbooks/<name>/` | `composes.teams` ≥ 1 + `workflows` ≥ 1 |
| [`bin/new-category`](bin/new-category) | `skills/<name>/README.md` | category index |

## Usage

```sh
sh generators/bin/new-category data "Schema, migrations, query tuning."
sh generators/bin/new-skill data schema-designer "Use this to design a schema."
sh generators/bin/new-agent code-reviewer code-quality/lint-runner
sh generators/bin/new-workflow ship-it testing/unit-test-generator documentation/doc-writer
sh generators/bin/new-playbook play-launch
```

Set `FACTORY_AUTHOR=@you` to stamp authorship; the date and `min_standard`
(`standards/VERSION`) are filled automatically.

## Guarantees

Generated artifacts pass `scripts/validate` for **structure, naming, placeholders, and
schema** out of the box. They contain `TODO` content for the author to fill — the
scaffold is correct; the *content* is yours. After generating:

1. Fill the `TODO`s. 2. Register it (skill → `/TAXONOMY.md`; workflow → `/WORKFLOWS.md`).
3. Run `scripts/validate`. 4. Self-review with `/standards/checklists/`.

## Why heredoc-based (v0.1.0 note)

These generators emit the canonical structure directly (matching the Wave 0 gold
standard) rather than copying `templates/`, guaranteeing valid output. A later version
may switch to template-copy once `templates/skill/` is aligned 1:1 with the gold
standard — see [/docs/adr/0001-framework-v0.1.0-freeze.md](../docs/adr/0001-framework-v0.1.0-freeze.md).
