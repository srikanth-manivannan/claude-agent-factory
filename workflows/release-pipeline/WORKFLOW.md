---
name: release-pipeline
description: Cut, verify, deploy, and announce a versioned release end to end.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [release, ci-cd, deployment, devops]
---

# Release Pipeline (Workflow)

> Cut, verify, deploy, and announce a versioned release end to end.

## Outcome

A versioned release built, tested, deployed with rollback capability, and
announced with an accurate changelog.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:devops/release-automator` | 0.1.0 | version bump + tag |
| 2 | `skill:documentation/changelog-generator` | 0.1.0 | changelog |
| 3 | `skill:devops/ci-pipeline-generator` | 0.1.0 | build/test run |
| 4 | `skill:devops/cd-deployment-builder` | 0.1.0 | deployment + rollback |

## Steps

1. **Cut the release** — bump SemVer, tag (VISION §12).
2. **Generate the changelog** — from merged changes since the last tag.
3. **Build & verify** — run the full CI suite; block on any failure.
4. **Deploy** — roll out with a rollback path ready.
5. **Announce** — publish release notes; notify stakeholders.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| release_type | yes | major / minor / patch |
| target_env | yes | Where to deploy |

## Outputs

A tagged, deployed release + published notes.

## Failure handling

- CI red → abort the release; do not deploy.
- Deploy fails → automatic rollback; investigate before retry.

## Constraints & safety

- Never deploy an unverified build (FACTORY: scripts/validate == CI).
