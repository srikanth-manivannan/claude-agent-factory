# Tests & Validation Guidance — Accessibility Auditor

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** markup with label/contrast/keyboard issues at AA.
- **Then:** findings grouped by POUR, each citing element + WCAG criterion + severity +
  fix; passed items noted; manual checks flagged.

### 2 — Edge: AAA target
- **Given:** `wcag_level: AAA`.
- **Then:** audits to AAA and marks AAA-only findings distinctly.

### 3 — Edge: accessible UI
- **Given:** compliant markup.
- **Then:** reports pass with at most 🟡 items; no fabricated 🔴.

### 4 — Failure/refusal: not a UI
- **Given:** non-UI input (e.g. a config file).
- **Then:** declines — nothing to audit for accessibility.

### 5 — Honesty: manual limits
- **Given:** any audit.
- **Then:** flags items requiring manual screen-reader verification.

## Fixtures

Sample markup snippets under `fixtures/` for per-criterion cases.
