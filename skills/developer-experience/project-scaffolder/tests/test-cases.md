# Tests & Validation Guidance — Project Scaffolder

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover placeholders).
3. **Dependencies:** declared `testing/unit-test-generator` + `devops/ci-pipeline-generator`
   references resolve (`tests/links/`).
4. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** project_type + stack + name.
- **Then:** produces a golden-path layout with docs, lint/pre-commit, a passing example
  test, CI, conventions, and a task runner.

### 2 — Golden-path proof
- **Given:** any generated scaffold.
- **Then:** a fresh clone runs `setup` then `test` green with no extra steps.

### 3 — Edge: project type variation
- **Given:** project_type = library (vs service).
- **Then:** library layout, same standard task verbs.

### 4 — Edge: org conventions
- **Given:** conventions (license, reviewers, commit style).
- **Then:** encodes them (LICENSE, CODEOWNERS, CI/pre-commit), not just docs.

### 5 — Safety: no secrets
- **Given:** a project needing env config.
- **Then:** ships `.env.example` only; `.env` gitignored.

### 6 — Consistency: standard verbs
- **Given:** any scaffold.
- **Then:** exposes setup/test/lint/build/run.

## Fixtures

Sample project_type + stack + conventions sets under `fixtures/`.
