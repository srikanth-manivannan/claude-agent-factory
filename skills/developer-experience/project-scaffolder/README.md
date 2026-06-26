# Project Scaffolder

> Use this to bootstrap a new project from a stack profile with structure, lint, CI, and docs baked in.

**Category:** developer-experience · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Bootstraps a new project on a **golden path** — predictable layout, README/docs, lint +
format + pre-commit, a test harness with a passing example, CI, baked-in conventions
(LICENSE/.gitignore/CODEOWNERS/CHANGELOG), and a task runner with standard verbs. A
fresh clone can `setup` then `test` green with **zero tribal knowledge**. It makes "the
right way" the default way for every new repo.

## Quickstart

```text
1. Copy skills/developer-experience/project-scaffolder/ into your skills directory.
2. Invoke with: project_type + stack + name (+ conventions).
3. Receive a ready-to-commit scaffold; `setup && test` is green on a fresh clone.
```

## How it works

Eight steps: golden-path layout → docs skeleton → lint/format/pre-commit → test harness
(via `unit-test-generator`) → CI (via `ci-pipeline-generator`) → conventions → task
runner → verify the golden path. Authoritative procedure in [SKILL.md](SKILL.md);
build steps in [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Inputs & outputs

- **Inputs:** `project_type`, `stack`, `name`, optional `conventions`.
- **Outputs:** a complete, ready-to-commit project scaffold (a fresh clone is productive).

See [EXAMPLES.md](EXAMPLES.md).

## Dependencies

- **`testing/unit-test-generator`** (≥ 0.1.0) — the passing example test.
- **`devops/ci-pipeline-generator`** (≥ 0.1.0) — the CI config.

## Customization

- **Stack / project type** — service vs library vs CLI vs app layouts.
- **Conventions** — plug in org license, CODEOWNERS, commit/branch policy.
- **Chain** into `scaffold-new-service` for a deployable service.

## Limitations

- Produces the scaffold; it doesn't implement your business logic.
- Stack-specific tooling depth depends on the chosen stack.

## Related

See [RESOURCES.md](RESOURCES.md). Depends on `testing/unit-test-generator` +
`devops/ci-pipeline-generator`; used by `scaffold-new-service` and `onboarding-workflow`;
composes into `team-platform`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
- **Implementation guidance:** [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Future improvements

- Stack profile library (curated golden paths per ecosystem).
- Dev-container / reproducible-env generation (`dev-env-bootstrapper`).
- Repo-settings-as-code (branch protection, required checks) output.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
