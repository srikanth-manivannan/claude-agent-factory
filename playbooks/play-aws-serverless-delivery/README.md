# AWS Serverless Delivery Pipeline (Playbook)

> Use this playbook to deliver a serverless workload to a cloud platform with operations in place.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
A reference engineering pipeline orchestrating `team-platform` and 4 workflows to
provision, deliver, release, and operate a serverless workload. Cloud-agnostic (AWS =
canonical example).

## The pipeline
`platform provisioning (team-platform) → build-feature + database-migration →
release-pipeline → incident-response`. Full spec in [PLAYBOOK.md](PLAYBOOK.md).

## Composes
- **Team:** [team-platform](../../teams/team-platform/).
- **Workflows:** build-feature, database-migration, release-pipeline, incident-response.

## Cross-references
See [RESOURCES.md](RESOURCES.md).

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [PLAYBOOK.md](PLAYBOOK.md).
