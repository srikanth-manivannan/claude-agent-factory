# Resources — Project Scaffolder

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md) · **Implementation:** [IMPLEMENTATION.md](IMPLEMENTATION.md).
- **Standards:** [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [security](../../../standards/security.md),
  [contributing](../../../standards/contributing.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Depends on** | [`testing/unit-test-generator`](../../testing/unit-test-generator/) | the example test |
| **Depends on** | [`devops/ci-pipeline-generator`](../../devops/ci-pipeline-generator/) | the CI config |
| **Sibling** | `developer-experience/linter-formatter-setup`, `dev-env-bootstrapper` *(planned)* | DX depth |
| **Used by workflow** | `scaffold-new-service`, `onboarding-workflow` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | bootstrap step |
| **Composed into** | `team-platform` ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | platform delivery |

## Concepts & background (vendor-neutral)

- **Golden path / paved road** engineering.
- **Convention over configuration**; **standard task verbs**.
- **Shift-left** quality (tests + CI from commit one).

## Provenance & credits

- Method synthesized from standard project-bootstrap / platform-engineering practice. No
  third-party content copied; MIT (VISION §13).
