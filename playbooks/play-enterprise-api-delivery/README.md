# Enterprise API Delivery Pipeline (Playbook)

> Use this playbook to deliver an enterprise API from design through secure, tested production release.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
A reference engineering pipeline that orchestrates **2 teams** and **5 workflows** to take
an API from design to operated production — proving the framework coordinates whole
lifecycles, not just individual skills.

## The pipeline
`design (team-backend) → build-feature + database-migration → review-pr + security-audit
(team-security) → release-pipeline → operate`. Full spec in [PLAYBOOK.md](PLAYBOOK.md).

## Composes
- **Teams:** [team-backend](../../teams/team-backend/), [team-security](../../teams/team-security/).
- **Workflows:** build-feature, database-migration, review-pr, security-audit, release-pipeline.

## Cross-references
See [RESOURCES.md](RESOURCES.md) for the full skill→agent→team→workflow→playbook map.

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [PLAYBOOK.md](PLAYBOOK.md).
