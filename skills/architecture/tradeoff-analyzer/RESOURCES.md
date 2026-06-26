# Resources — Tradeoff Analyzer

> References and cross-links. Grouped by purpose so the section stays useful for any
> decision domain.

## Internal references (this repository)

- **Spec:** [SKILL.md](SKILL.md) — the authoritative method.
- **Standards conformed to:**
  [prompt-engineering](../../../standards/prompt-engineering.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [security](../../../standards/security.md),
  [metadata](../../../standards/metadata.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

> Per [/standards/architecture.md](../../../standards/architecture.md):
> Skill → Agent → Team / Workflow → Playbook.

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Feeds** | `architecture/adr-author` *(planned)* | the analysis becomes an ADR |
| **Sibling** | [`architecture/system-design-reviewer`](../system-design-reviewer/) | review surfaces trade-offs to analyze |
| **Sibling** | [`architecture/migration-planner`](../migration-planner/) | strategy selection uses this skill |
| **Used by workflow** | `architecture-review`, `tech-debt-paydown` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | decision steps |
| **Used by playbook** | `play-secure-launch`, `play-zero-to-production` ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | architecture decisions in the operating guide |

## Concepts & background (vendor-neutral)

- **Weighted decision matrix** — scoring options against weighted criteria.
- **Sensitivity analysis** — testing whether a conclusion is robust to input changes.
- **ADR (Architecture Decision Record)** — the durable home for a decision + rationale.

## Provenance & credits

- Method synthesized from standard decision-analysis practice (weighted scoring,
  sensitivity checks). No third-party content copied; MIT (VISION §13).
