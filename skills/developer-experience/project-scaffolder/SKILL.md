---
name: project-scaffolder
description: Use this to bootstrap a new project from a stack profile with structure, lint, CI, and docs baked in.
version: 0.1.0
category: developer-experience
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [developer-experience, scaffold, bootstrap, ci, conventions]
---

# Project Scaffolder

> Use this to bootstrap a new project from a stack profile with structure, lint, CI, and docs baked in.

> **Tech profile** — Technology: project scaffold · Language: any · Stack: any · Toolchain: any · Domain: developer-experience
> *(Stack-agnostic method; emits a layout + config for the chosen stack via the tech profile.)*

## When to use this skill

- Starting a new service/library/app and wanting consistent, golden-path conventions.
- Standardizing how an org bootstraps repos (structure, lint, CI, docs, conventions).
- Producing the baseline the `scaffold-new-service` workflow builds on.

## When NOT to use this skill

- Configuring CI for an existing repo — use `devops/ci-pipeline-generator`.
- Setting up only lint/format — use `developer-experience/linter-formatter-setup` *(planned)*.
- Provisioning infra — use `cloud/cloud-resource-provisioner`.

## Prerequisites

- The project **type** (service/library/CLI/app) and target **stack**.
- Any org conventions to enforce (license, code owners, commit style).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `project_type` | yes | service / library / CLI / app |
| `stack` | yes | Language/framework/toolchain |
| `name` | yes | Project name (kebab-case) |
| `conventions` | no | Org rules: license, CODEOWNERS, commit/branch policy |

## Instructions

1. **Choose the golden-path layout** for the project type + stack: source, tests,
   config, and docs directories with predictable names.
2. **Add a README + docs skeleton** following [/standards/documentation.md](../../../standards/documentation.md)
   (what/quickstart/inputs-outputs/limitations) — the project is documented from commit one.
3. **Wire lint + format + pre-commit** for the stack so style is automatic, not argued.
4. **Add a test harness** with one passing example test (so `test` works day one) —
   use `testing/unit-test-generator` for the example.
5. **Add CI** via `devops/ci-pipeline-generator` (install → lint → test → build), set as
   a required check.
6. **Bake in conventions:** LICENSE, `.gitignore`, editorconfig, CODEOWNERS, and a
   CHANGELOG — plus commit/branch policy if provided.
7. **Add a task runner** (make/just/npm-scripts) exposing `setup`, `test`, `lint`,
   `build`, `run` so every project has the same verbs.
8. **Verify the golden path:** a fresh clone can `setup` then `test` green with no
   tribal knowledge.

## Output

A ready-to-commit project scaffold: golden-path directory layout, README + docs
skeleton, lint/format/pre-commit config, a test harness with a passing example, CI
config, baked-in conventions (LICENSE/.gitignore/CODEOWNERS/CHANGELOG), and a task
runner with standard verbs. A fresh clone is productive immediately.

## Constraints & safety

- **Golden path works on a fresh clone** — `setup` → `test` green, no hidden steps.
- **Conventions are enforced, not suggested** (lint/CI/pre-commit), so quality is automatic.
- **No secrets** in the scaffold; provide `.env.example`, never `.env`
  ([/standards/security.md](../../../standards/security.md)).

## Examples

Minimal below; full enterprise examples in [EXAMPLES.md](EXAMPLES.md); build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

**Given:** project_type = service, stack = "<your backend stack>", name = `billing-svc`.
**Produces:** `src/`, `tests/` (with a passing example), lint+pre-commit, CI
(lint→test→build, required), README/docs, LICENSE/.gitignore/CODEOWNERS, and a task
runner — `setup && test` green on a fresh clone.
