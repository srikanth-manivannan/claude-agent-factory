# Resources — Accessibility Compliance Pipeline

> Cross-references for the hierarchy this pipeline orchestrates
> ([/standards/architecture.md](../../standards/architecture.md)).

## Team (composed)
- [team-frontend](../../teams/team-frontend/) → agents: frontend-engineer, qa-engineer.

## Workflows (sequenced)
- [accessibility-audit](../../workflows/accessibility-audit/), [review-pr](../../workflows/review-pr/),
  [release-pipeline](../../workflows/release-pipeline/).

## Skills (via agents, transitively)
accessibility/a11y-auditor, frontend/component-scaffold, testing/unit-test-generator,
documentation/doc-writer.

## Standards
Conforms to [/standards/accessibility.md](../../standards/accessibility.md) (WCAG 2.2 AA);
gated via the [accessibility-review](../../standards/checklists/accessibility-review.md) checklist.
