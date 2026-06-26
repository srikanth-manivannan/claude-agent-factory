# Resources — System Design Reviewer

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [prompt-engineering](../../../standards/prompt-engineering.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [security](../../../standards/security.md),
  [architecture](../../../standards/architecture.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Checklist it maps to:**
  [architecture-review.md](../../../standards/checklists/architecture-review.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Sibling** | [`architecture/tradeoff-analyzer`](../tradeoff-analyzer/) | a finding may need an option trade-off |
| **Sibling** | [`architecture/migration-planner`](../migration-planner/) | rework findings feed a migration plan |
| **Feeds** | `architecture/adr-author` *(planned)* | blocker findings → ADRs |
| **Defers to** | `security/threat-modeler` *(planned)*, `security-review` | deep security |
| **Used by workflow** | `architecture-review` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | the review step |
| **Used by playbook** | `play-secure-launch`, `play-zero-to-production` | design gate |

## Concepts & background (vendor-neutral)

- **Quality attributes** (scalability, reliability, security, cost, maintainability).
- **Critical path** analysis; **single point of failure**; **graceful degradation**.
- **ATAM** (Architecture Tradeoff Analysis Method) — scenario-based evaluation.

## Provenance & credits

- Method synthesized from standard architecture-review practice. No third-party
  content copied; MIT (VISION §13).
