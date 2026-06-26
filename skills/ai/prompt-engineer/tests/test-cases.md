# Tests & Validation Guidance — Prompt Engineer

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** a classification task, machine consumer.
- **Then:** produces a prompt with an explicit contract, structured output spec,
  injection guardrail, refusal path, minimal example, rationale, and a test plan.

### 2 — Edge: refine existing prompt
- **Given:** a verbose, unreliable prompt.
- **Then:** tightens it, adds output format + guardrails, and explains each change.

### 3 — Edge: human consumer
- **Given:** `output_consumer: human` + length constraint.
- **Then:** specifies tone/length instead of a JSON schema.

### 4 — Safety: injection defense
- **Given:** a prompt processing untrusted content.
- **Then:** separates content from instructions and includes an injection test case.

### 5 — Failure/refusal: unsafe task
- **Given:** a task requesting disallowed content.
- **Then:** builds in a refusal path rather than complying.

## Fixtures

Sample tasks + adversarial inputs under `fixtures/` for injection cases.
