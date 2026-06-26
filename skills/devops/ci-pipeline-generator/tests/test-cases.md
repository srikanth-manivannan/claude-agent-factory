# Tests & Validation Guidance — CI Pipeline Generator

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Dependency:** the declared `testing/unit-test-generator` reference resolves
   (`tests/links/`).
4. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** a project with tests + a CI platform.
- **Then:** generates a fast-fail pipeline (lint→test→build→validate) with caching,
  pinned versions, and a required-check gate.

### 2 — Edge: extra stages
- **Given:** `stages: [type-check, security-scan]`.
- **Then:** inserts them in fast-fail order.

### 3 — Edge: platform inference
- **Given:** no `ci_platform`.
- **Then:** detects the platform and emits its native config.

### 4 — Safety: tests gate the build
- **Given:** any generated pipeline.
- **Then:** a failing test fails the build (no error suppression).

### 5 — Safety: no secrets in config
- **Given:** a pipeline needing credentials.
- **Then:** references the platform secret store, never inline secrets.

## Fixtures

Sample project descriptors under `fixtures/` per platform.
