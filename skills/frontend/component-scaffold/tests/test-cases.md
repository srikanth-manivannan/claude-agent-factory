# Tests & Validation Guidance — Component Scaffold

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
- **Given:** a component spec + props + states.
- **Then:** scaffolds semantic accessible markup, state handling, a test suite (via
  the testing primitive), a usage example, and prop docs.

### 2 — Edge: framework inference
- **Given:** no `framework`.
- **Then:** detects and matches the project's framework/conventions.

### 3 — Edge: accessibility baseline
- **Given:** an interactive component.
- **Then:** keyboard-operable + labeled by construction; recommends an `a11y-auditor` pass.

### 4 — Dependency: tests present
- **Given:** any scaffolded component.
- **Then:** render + interaction + state tests exist (no untested component).

### 5 — Failure/refusal: under-specified
- **Given:** a vague component request.
- **Then:** asks for the contract (props/states) instead of guessing.

## Fixtures

Sample component specs under `fixtures/` per target framework.
