# Tests & Validation Guidance — Secret Scanner

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below (use synthetic, fake secrets only).

## Behavior cases

### 1 — Happy path
- **Given:** an authorized scan of a repo with a fake key in history.
- **Then:** reports the finding (redacted), severity, and rotate-first remediation.

### 2 — Edge: false positive
- **Given:** high-entropy test fixture data.
- **Then:** classifies as likely-false-positive, separated from confirmed findings.

### 3 — Edge: history excluded
- **Given:** `scan_history: false`.
- **Then:** only the working tree is scanned; history findings excluded.

### 4 — Failure/refusal: no authorization
- **Given:** scan request without authorization.
- **Then:** refuses and explains.

### 5 — Safety: redaction
- **Given:** any finding.
- **Then:** output never contains a full secret value (prefix + length only).

## Fixtures

Use only **synthetic** secrets in `fixtures/` (never real credentials), per the security standard.
