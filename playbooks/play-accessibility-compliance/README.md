# Accessibility Compliance Pipeline (Playbook)

> Use this playbook to bring a product to WCAG AA compliance and keep it there through release.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
A reference engineering pipeline orchestrating `team-frontend` and 3 workflows to reach
WCAG AA compliance and prevent regressions at release.

## The pipeline
`accessibility-audit → review-pr → release-pipeline` (with an a11y check guarding CI).
Full spec in [PLAYBOOK.md](PLAYBOOK.md).

## Composes
- **Team:** [team-frontend](../../teams/team-frontend/).
- **Workflows:** accessibility-audit, review-pr, release-pipeline.

## Cross-references
See [RESOURCES.md](RESOURCES.md).

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [PLAYBOOK.md](PLAYBOOK.md).
