# Tests & Validation Guidance — System Design Reviewer

> Behavior cases + validation. Conforms to
> [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no placeholders).
3. **Behavior:** run each case and check the expectation.

## Behavior cases

### 1 — Happy path
- **Given:** a concrete design + goals + scale.
- **Then:** returns severity-tagged findings across quality attributes, strengths, a
  verdict derived from severity, and assumptions.

### 2 — Edge: sound design
- **Given:** a design with only minor issues.
- **Then:** verdict = approve-with-changes or approve; no fabricated 🔴.

### 3 — Edge: missing scale
- **Given:** no `expected_scale`.
- **Then:** states an assumed scale explicitly and proceeds.

### 4 — Failure/refusal: ambiguous design
- **Given:** a design too vague to map a critical path.
- **Then:** returns clarifying questions and pauses instead of inventing a design.

### 5 — Consistency: verdict matches findings
- **Given:** a design with one 🔴 finding.
- **Then:** verdict = needs-rework (never approve over an open blocker).

## Fixtures

None required (pure-reasoning skill; inputs specify cases).
