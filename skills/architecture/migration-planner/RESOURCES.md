# Resources — Migration Planner

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [prompt-engineering](../../../standards/prompt-engineering.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [security](../../../standards/security.md),
  [architecture](../../../standards/architecture.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Checklist it aligns with:**
  [deployment-review.md](../../../standards/checklists/deployment-review.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Follows** | [`architecture/tradeoff-analyzer`](../tradeoff-analyzer/) | choose the target first |
| **Follows** | [`architecture/system-design-reviewer`](../system-design-reviewer/) | validate the target design |
| **Hands off to** | `database-migration` workflow ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | executable data steps |
| **Feeds** | `architecture/adr-author` *(planned)* | record the migration decision |
| **Used by playbook** | `play-zero-to-production` ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | replatform/launch |

## Concepts & background (vendor-neutral)

- **Strangler-fig pattern** — incrementally replace a system behind a facade.
- **Expand/contract (parallel change)** — zero-downtime data migration.
- **De-risking sequencing** — do the uncertain work first.
- **Rollback / blue-green / canary** — safe-change mechanics.

## Provenance & credits

- Method synthesized from established migration practice (strangler-fig,
  expand/contract). No third-party content copied; MIT (VISION §13).
