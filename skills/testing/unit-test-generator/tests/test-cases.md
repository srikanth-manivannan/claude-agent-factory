# Tests & Validation Guidance — Unit Test Generator

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** a pure function with a clear contract.
- **Then:** generates happy + edge + failure tests, named by intent, in the project framework.

### 2 — Edge: side effects
- **Given:** a unit with an external dependency.
- **Then:** mocks the dependency; asserts behavior, not internals.

### 3 — Edge: framework inference
- **Given:** no `framework` provided.
- **Then:** detects the project's framework and matches its conventions.

### 4 — Failure/refusal: ambiguous behavior
- **Given:** undefined handling of invalid input.
- **Then:** asks for the contract instead of guessing.

### 5 — Safety: deterministic, no real data
- **Given:** any generated suite.
- **Then:** no time/order/network coupling; no real PII/secrets in fixtures.

### 6 — Refusal: untestable code
- **Given:** code with no seams.
- **Then:** reports why + recommends a refactor; does not edit the unit.

## Fixtures

Provide a sample unit per target language under `fixtures/` when adding language-specific cases.
