# Resources — Unit Test Generator

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md),
  [security](../../../standards/security.md),
  [prompt-engineering](../../../standards/prompt-engineering.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Checklist it maps to:** [testing-review.md](../../../standards/checklists/testing-review.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Depended on by** | [`frontend/component-scaffold`](../../frontend/component-scaffold/) | component tests |
| **Depended on by** | [`devops/ci-pipeline-generator`](../../devops/ci-pipeline-generator/) | runs the tests it generates |
| **Sibling** | `testing/coverage-gap-finder` *(planned)* | finds gaps to fill |
| **Used by workflow** | `build-feature`, `fix-bug`, `refactor-module` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | test step |

## Concepts & background (vendor-neutral)

- **Test classes:** happy / edge / failure.
- **Test isolation, mocking/stubbing, determinism.**
- **Behavior vs implementation testing**; **AAA** (Arrange-Act-Assert).

## Provenance & credits

- Method synthesized from standard unit-testing practice. No third-party content
  copied; MIT (VISION §13).
