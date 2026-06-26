# Resources — Component Scaffold

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [accessibility](../../../standards/accessibility.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md),
  [prompt-engineering](../../../standards/prompt-engineering.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Depends on** | [`testing/unit-test-generator`](../../testing/unit-test-generator/) | generates component tests |
| **Pairs with** | [`accessibility/a11y-auditor`](../../accessibility/a11y-auditor/) | full WCAG audit of the component |
| **Sibling** | `frontend/component-test-harness` *(planned)* | visual/story tests |
| **Used by workflow** | `build-feature`, `build-ui-component` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | UI step |

## Concepts & background (vendor-neutral)

- **Component contract** (props/events/states/variants).
- **Accessible-by-construction** UI; **semantic HTML first**.
- **Composability**; **testing the rendered behavior**.

## Provenance & credits

- Method synthesized from standard component-engineering practice. No third-party
  content copied; MIT (VISION §13).
