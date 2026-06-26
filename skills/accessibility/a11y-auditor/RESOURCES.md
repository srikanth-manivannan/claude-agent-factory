# Resources — Accessibility Auditor

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [accessibility](../../../standards/accessibility.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [prompt-engineering](../../../standards/prompt-engineering.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Checklist it maps to:** [accessibility-review.md](../../../standards/checklists/accessibility-review.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Fixers** | `accessibility/aria-annotator`, `color-contrast-fixer`, `keyboard-nav-checker` *(planned)* | apply the recommended fixes |
| **Pairs with** | [`frontend/component-scaffold`](../../frontend/component-scaffold/) | build accessible UI up front |
| **Used by workflow** | `accessibility-audit`, `review-pr` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | a11y step |

## Concepts & background (vendor-neutral)

- **WCAG 2.2** + the **POUR** principles (Perceivable/Operable/Understandable/Robust).
- **Success criteria** and conformance levels (A/AA/AAA).
- **Semantic HTML first, ARIA second.**

## Provenance & credits

- Method synthesized from WCAG 2.2 guidance and standard a11y-audit practice. No
  third-party content copied; MIT (VISION §13).
