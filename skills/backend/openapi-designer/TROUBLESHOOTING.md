# Troubleshooting — OpenAPI Designer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Quick diagnostics

- [ ] Does the spec validate as OpenAPI 3.1?
- [ ] Are schemas reused via `components` (not inlined repeatedly)?
- [ ] Is security explicitly defined?
- [ ] Do operations use correct HTTP status codes?

## Common issues

### Symptom: Spec fails OpenAPI validation
- **Cause:** structural errors (bad `$ref`, missing required keys).
- **Fix:** run the lint step; resolve reported errors before handing off.

### Symptom: Duplicated schemas everywhere
- **Cause:** inline objects instead of components.
- **Fix:** extract to `components/schemas` and `$ref` them.

### Symptom: API is unintentionally open
- **Cause:** no `securitySchemes` / `security` applied.
- **Fix:** define auth and apply it; the skill flags unspecified auth.

### Symptom: Wrong status codes
- **Cause:** non-semantic responses (e.g. 200 for create/errors).
- **Fix:** 201 for create, 204 for empty, 4xx/5xx for errors with the shared Error schema.

### Symptom: Implementation drifts from the spec
- **Cause:** spec treated as docs, not contract.
- **Fix:** generate the implementation via `rest-endpoint-scaffold`; add contract tests.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the OpenAPI 3.1 specification.
- Open an issue with requirements + the produced spec.
