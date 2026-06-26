# Troubleshooting — Component Scaffold

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Quick diagnostics

- [ ] Is the component contract (props/events/states) defined?
- [ ] Is the markup semantic + keyboard operable?
- [ ] Are tests generated (render + interaction + states)?
- [ ] Does it match the project's framework conventions?

## Common issues

### Symptom: Component isn't keyboard accessible
- **Cause:** non-semantic markup (e.g. clickable `div`).
- **Fix:** use native elements / correct roles + key handlers; run `a11y-auditor`.

### Symptom: No tests generated
- **Cause:** the `testing/unit-test-generator` dependency wasn't available/resolved.
- **Fix:** ensure the testing skill is present (Wave 0 dependency); re-run.

### Symptom: Wrong framework/style
- **Cause:** framework not detected.
- **Fix:** pass `framework`; the skill matches existing conventions.

### Symptom: Missing states (loading/error/empty)
- **Cause:** contract under-specified.
- **Fix:** declare the states in the component contract; they drive markup + tests.

### Symptom: Component does too much
- **Cause:** scope creep.
- **Fix:** keep it focused/composable; split into smaller components.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the accessibility + testing standards.
- Open an issue with the component spec + generated output.
