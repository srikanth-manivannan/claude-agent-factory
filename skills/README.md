# Skills

> The collection — the product. Skills are reusable capabilities grouped by category
> (`skills/<category>/<name>/`), conforming to [/standards/](../standards/) and
> validated against [/shared/schemas/skill.schema.yaml](../shared/schemas/skill.schema.yaml).
> The full backlog is [/TAXONOMY.md](../TAXONOMY.md).

## Categories

**Wave 0** validates the framework across 9 domains (one flagship skill each, except
architecture which has 3). The remaining categories follow after Framework v0.1.0 is frozen.

| Category | Flagship skill(s) active | Status |
|----------|--------------------------|--------|
| [architecture](architecture/) | tradeoff-analyzer, system-design-reviewer, migration-planner | ✅ reference category |
| [testing](testing/) | unit-test-generator | ✅ Wave 0 |
| [documentation](documentation/) | doc-writer | ✅ Wave 0 |
| [security](security/) | secret-scanner | ✅ Wave 0 |
| [accessibility](accessibility/) | a11y-auditor | ✅ Wave 0 |
| [backend](backend/) | openapi-designer | ✅ Wave 0 |
| [ai](ai/) | prompt-engineer | ✅ Wave 0 |
| [frontend](frontend/) | component-scaffold | ✅ Wave 0 |
| [devops](devops/) | ci-pipeline-generator | ✅ Wave 0 |
| [agentic-ai](agentic-ai/) | agent-scaffold | ✅ Wave 1 |
| [database](database/) | schema-designer | ✅ Wave 1 |
| [cloud](cloud/) | cloud-resource-provisioner | ✅ Wave 1 |
| [developer-experience](developer-experience/) | project-scaffolder | ✅ Wave 1 |
| _9 more categories_ | see [/TAXONOMY.md](../TAXONOMY.md) | ⏳ pending |

> **Architecture** is the **gold-standard reference category** (Phase 9); Wave 0
> validates the bar across domains before large-scale generation. Every category
> replicates the quality bar and folder structure — see
> [architecture/README.md](architecture/README.md) for the anatomy of a skill.

## Adding a skill

1. Add a row to [/TAXONOMY.md](../TAXONOMY.md) first.
2. Scaffold from [/templates/](../templates/) (or the Factory) — inherit standards by
   construction.
3. Build to [/standards/](../standards/); validate with `scripts/validate`.
4. Self-review with the [checklists](../standards/checklists/); open a PR.

See [/standards/contributing.md](../standards/contributing.md).
