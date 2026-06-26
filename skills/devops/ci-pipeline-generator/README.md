# CI Pipeline Generator

> Use this to generate a CI pipeline that builds, tests, and validates a project on every change.

**Category:** devops · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Generates a fast-fail CI pipeline (install → lint → test → build → validate) for the
project's CI platform, wires the **test stage to the project's test suite**, caches
dependencies, adds a security scan where available, and gates merges on green CI. It
encodes the repo's core principle — *`scripts/validate == CI`* — so "passes locally"
means "passes CI."

It composes the **`testing/unit-test-generator`** primitive (the tests it runs) — a
deliberate cross-category dependency.

## Quickstart

```text
1. Copy skills/devops/ci-pipeline-generator/ into your skills directory.
2. Invoke with the project (+ ci_platform / extra stages if desired).
3. Receive a CI config with caching, a required-check gate, and pinned versions.
```

## How it works

Seven steps: detect stack/platform → define fast-fail stages → wire tests (fail-on-red)
→ caching → security step → merge gating → reproducibility. Authoritative procedure in
[SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `project`, optional `ci_platform`, optional `stages`.
- **Outputs:** a CI config + a local-reproduction note.

See [EXAMPLES.md](EXAMPLES.md).

## Dependencies

- **`testing/unit-test-generator`** (≥ 0.1.0) — the tests the pipeline executes.

## Customization

- **Platform** — override auto-detection.
- **Extra stages** — type-check, container build, coverage upload.
- **Chain** into `devops/cd-deployment-builder` for deployment.

## Limitations

- Generates CI (build/test/validate), not CD/deploy (use `cd-deployment-builder`).
- Security step depends on available scanners on the platform.

## Related

See [RESOURCES.md](RESOURCES.md). Depends on `testing/unit-test-generator`; feeds the
`release-pipeline` workflow; pairs with `devops/dockerfile-author`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Matrix builds across language/OS versions.
- Coverage-threshold gating via `testing/coverage-gap-finder`.
- Auto-generated local pre-push hook mirroring the pipeline.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
