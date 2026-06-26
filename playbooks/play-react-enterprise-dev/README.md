# React Enterprise Development Pipeline (Playbook)

> Use this playbook to deliver accessible, performant enterprise frontend features to production.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
A reference engineering pipeline orchestrating `team-frontend` and 5 workflows to ship
accessible, performant frontend features. Stack-agnostic (React = canonical example).

## The pipeline
`build-feature → accessibility-audit → performance-optimization → review-pr →
release-pipeline`. Full spec in [PLAYBOOK.md](PLAYBOOK.md).

## Composes
- **Team:** [team-frontend](../../teams/team-frontend/).
- **Workflows:** build-feature, accessibility-audit, performance-optimization, review-pr, release-pipeline.

## Cross-references
See [RESOURCES.md](RESOURCES.md).

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [PLAYBOOK.md](PLAYBOOK.md).
