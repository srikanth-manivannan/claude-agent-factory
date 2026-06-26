# Release Pipeline (Workflow)

> Cut, verify, deploy, and announce a versioned release end to end.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

The full release path: version bump → changelog → CI verify → deploy with
rollback → announce.

## The flow

`cut → changelog → build/verify → deploy → announce`. See [WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:devops/release-automator` (≥ 0.1.0)
- `skill:documentation/changelog-generator` (≥ 0.1.0)
- `skill:devops/ci-pipeline-generator` (≥ 0.1.0)
- `skill:devops/cd-deployment-builder` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** release type (major/minor/patch), target environment.
- **Outputs:** tagged, deployed release + published notes.

## Customization

Chain `database-migration` before deploy when schema changes ship together.

## Limitations

- Aborts on any CI failure by design; will not force a release.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
