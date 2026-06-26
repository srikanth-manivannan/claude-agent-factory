---
name: ci-pipeline-generator
description: Use this to generate a CI pipeline that builds, tests, and validates a project on every change.
version: 0.1.0
category: devops
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [devops, ci, pipeline, automation, quality-gate]
---

# CI Pipeline Generator

> Use this to generate a CI pipeline that builds, tests, and validates a project on every change.

> **Tech profile** — Technology: CI/CD · Language: any · Stack: any CI platform · Toolchain: any · Domain: devops
> *(Platform-agnostic method; emits config for the project's CI platform.)*

## When to use this skill

- Adding CI to a project that has none.
- Standardizing the build → test → validate gate across repos.
- Setting up the quality gate the `release-pipeline` workflow relies on.

## When NOT to use this skill

- Deployment/CD — use `devops/cd-deployment-builder`.
- Containerization — use `devops/dockerfile-author`.
- Infra provisioning — use `devops/iac-module-builder`.

## Prerequisites

- The project's language/build tooling and target CI platform (detected or stated).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `project` | yes | Repo/stack to add CI for |
| `ci_platform` | no | Target CI system; inferred if omitted |
| `stages` | no | Extra stages (lint, type-check, security scan) |

## Instructions

1. **Detect stack + platform.** Identify language, build/test tooling, and the CI
   platform (or use the stated one). Match existing conventions.
2. **Define the pipeline stages**, fast-fail ordered:
   install → lint/format → type-check (if applicable) → **test** → build → validate.
3. **Wire the test stage** to the project's tests — the suite produced by
   `testing/unit-test-generator` — and **fail the build on any test failure**.
4. **Add caching** for dependencies/build artifacts to keep CI fast.
5. **Add a security step** (e.g. dependency + secret scan) where available
   ([/standards/security.md](../../../standards/security.md)).
6. **Gate merges.** Configure required status checks so red CI blocks merge
   (`scripts/validate == CI` principle).
7. **Keep it reproducible.** Pin tool versions; ensure the pipeline runs identically
   locally and in CI; document how to reproduce a failure.

## Output

A CI configuration for the target platform: ordered fast-fail stages (lint → test →
build → validate), dependency caching, an optional security scan, required-check
merge gating, and pinned versions — plus a short note on running it locally.

## Constraints & safety

- **Fail on test failure** — never allow green CI over failing tests.
- **No secrets in config** — use the platform's secret store
  ([/standards/security.md](../../../standards/security.md)).
- **Reproducible** — pinned versions; local run matches CI.

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** a project with a unit-test suite, targeting a CI platform.
**Produces:** a pipeline that installs deps (cached), lints, runs the tests (build fails
on failure), builds, and is set as a required check on the default branch.
