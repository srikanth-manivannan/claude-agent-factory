# Resources — Cloud Resource Provisioner

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md) · **Implementation:** [IMPLEMENTATION.md](IMPLEMENTATION.md).
- **Standards:** [security](../../../standards/security.md),
  [architecture](../../../standards/architecture.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Feeds** | `provision-infrastructure`, `deploy-to-production` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | the infra step |
| **Pairs with** | [`devops/ci-pipeline-generator`](../../devops/ci-pipeline-generator/) | runs plan/apply in CI |
| **Related** | `devops/iac-module-builder` *(planned)* | reusable modules this composes |
| **Related** | `cloud/cloud-cost-optimizer`, `cloud/cloud-iam-designer` *(planned)* | cost + IAM depth |
| **Composed into** | `team-platform` → `play-zero-to-production` ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | platform delivery |

## Concepts & background (vendor-neutral)

- **Infrastructure as Code**; **immutable infrastructure**; **drift**.
- **Least-privilege IAM**; **secure-by-default** networking/encryption.
- **Remote/locked state**; **plan → apply**; **policy as code**.

## Provenance & credits

- Method synthesized from standard cloud/IaC practice (least privilege, tagging,
  plan-review-apply). No third-party content copied; MIT (VISION §13).
