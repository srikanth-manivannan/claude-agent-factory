# Troubleshooting — Unit Test Generator

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/testing.md](../../../standards/testing.md).

## Quick diagnostics

- [ ] Is the behavior contract clear (inputs/outputs/errors)?
- [ ] Do generated tests cover happy + edge + failure?
- [ ] Are tests isolated (mocks for external deps) and deterministic?
- [ ] Do test names state intent?

## Common issues

### Symptom: Tests are flaky
- **Cause:** dependence on time, order, network, or shared state.
- **Fix:** mock the source of nondeterminism; seed randomness; remove timing waits.

### Symptom: Tests break on every refactor
- **Cause:** asserting implementation details, not behavior.
- **Fix:** assert observable outputs/side effects; avoid asserting private calls.

### Symptom: The skill asks questions instead of generating
- **Cause:** ambiguous behavior (e.g. undefined handling of invalid input).
- **Fix:** provide a `behavior_spec`; this is correct, safe behavior.

### Symptom: Wrong framework / style
- **Cause:** framework not detected.
- **Fix:** pass `framework` explicitly; the skill matches existing conventions.

### Symptom: "Code is untestable" report
- **Cause:** hidden dependencies / no seams.
- **Fix:** refactor for injectability (`refactor-module`); the skill won't silently
  edit the unit.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and [testing-review](../../../standards/checklists/testing-review.md).
- Open an issue with the unit + generated tests attached.
