# Tests & Validation Guidance — Doc Writer

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** an undocumented subject + audience.
- **Then:** produces a README with every required section; one-sentence description;
  runnable quickstart; working links; no placeholders.

### 2 — Edge: refresh stale docs
- **Given:** existing docs with an outdated claim.
- **Then:** corrects the claim to match current behavior.

### 3 — Edge: thin intent
- **Given:** subject with unclear purpose.
- **Then:** documents observable behavior and asks for intent rather than inventing.

### 4 — Failure/refusal: invented features
- **Given:** a request to document a non-existent feature.
- **Then:** declines to document unverified behavior; suggests "Future improvements".

### 5 — Standard compliance
- **Given:** any produced README.
- **Then:** passes documentation-review (all required sections present).

## Fixtures

Optional sample subjects under `fixtures/` for language-specific cases.
