# Resources — CI Pipeline Generator

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [security](../../../standards/security.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md),
  [review-process](../../../standards/review-process.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Depends on** | [`testing/unit-test-generator`](../../testing/unit-test-generator/) | the tests CI runs |
| **Feeds** | `devops/cd-deployment-builder` *(planned)* | deploy after green CI |
| **Pairs with** | `devops/dockerfile-author` *(planned)* | container build stage |
| **Used by workflow** | `release-pipeline`, `scaffold-new-service` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | CI step |

## Concepts & background (vendor-neutral)

- **Fast-fail pipelines**; **dependency caching**; **required status checks**.
- **Reproducible builds** (pinned versions); **shift-left** security.
- Repo principle: **`scripts/validate == CI`**.

## Provenance & credits

- Method synthesized from standard CI practice. No third-party content copied; MIT (VISION §13).
