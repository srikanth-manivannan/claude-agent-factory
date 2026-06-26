# Secure Software Delivery Pipeline (Playbook)

> Use this playbook to deliver software through a security-first pipeline with gated release.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT · Defensive/authorized use only.

## What it does
A reference engineering pipeline orchestrating `team-security` and 5 workflows to bake
security into every delivery stage, **gating release** on security blockers.

## The pipeline
`secure design (team-security) → build-feature → security-audit → review-pr → [gate] →
release-pipeline → incident-response`. Full spec in [PLAYBOOK.md](PLAYBOOK.md).

## Composes
- **Team:** [team-security](../../teams/team-security/).
- **Workflows:** build-feature, security-audit, review-pr, release-pipeline, incident-response.

## Cross-references
See [RESOURCES.md](RESOURCES.md).

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [PLAYBOOK.md](PLAYBOOK.md).
