# Tests & Validation Guidance — Tradeoff Analyzer

> Behavior cases proving the skill works + how to validate it. Conforms to
> [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** run `scripts/validate` (folder == name, required files, no
   leftover template placeholders).
3. **Behavior:** invoke the skill with each case below and check the expectation.

## Behavior cases

### 1 — Happy path
- **Given:** a decision + 2 options + 4 weighted criteria (sum 100%).
- **When:** invoked.
- **Then:** returns a complete scoring matrix, weighted totals, a recommendation with
  margin + primary risk, a sensitivity note, and assumptions.

### 2 — Edge: weights omitted
- **Given:** options + criteria but no weights.
- **When:** invoked.
- **Then:** applies equal weights, states it did so, and proceeds.

### 3 — Edge: hard constraint eliminates an option
- **Given:** 3 options, one violating a hard constraint.
- **When:** invoked.
- **Then:** eliminates that option at step 2 with a recorded reason; scores the rest.

### 4 — Edge: weight-sensitive result
- **Given:** options whose totals are within 0.5 and flip under a plausible weight change.
- **When:** invoked.
- **Then:** flags the result as weight-sensitive and identifies the driving weight.

### 5 — Failure/refusal: single option
- **Given:** only one viable option.
- **When:** invoked.
- **Then:** declines to produce a trade-off analysis and explains why (no trade-off).

### 6 — Failure/refusal: missing evidence
- **Given:** a criterion with no evidence for one option.
- **When:** invoked.
- **Then:** records an assumption rather than inventing a score.

## Fixtures

None required — cases are specified by inputs above (pure-reasoning skill).
