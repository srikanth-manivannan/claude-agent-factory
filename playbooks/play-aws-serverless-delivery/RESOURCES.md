# Resources — AWS Serverless Delivery Pipeline

> Cross-references for the hierarchy this pipeline orchestrates
> ([/standards/architecture.md](../../standards/architecture.md)).

## Team (composed)
- [team-platform](../../teams/team-platform/) → agents: platform-engineer, security-engineer, qa-engineer.

## Workflows (sequenced)
- [build-feature](../../workflows/build-feature/), [database-migration](../../workflows/database-migration/),
  [release-pipeline](../../workflows/release-pipeline/), [incident-response](../../workflows/incident-response/).

## Skills (via agents, transitively)
cloud/cloud-resource-provisioner, devops/ci-pipeline-generator,
developer-experience/project-scaffolder, security/secret-scanner,
testing/unit-test-generator.

## Standards
Conforms to [/standards/](../../standards/); infra reviewed via the
[deployment-review](../../standards/checklists/deployment-review.md) checklist.
