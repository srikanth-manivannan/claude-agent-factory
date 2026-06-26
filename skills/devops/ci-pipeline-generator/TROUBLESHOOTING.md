# Troubleshooting — CI Pipeline Generator

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Quick diagnostics

- [ ] Does the test stage fail the build on test failure?
- [ ] Are dependencies cached?
- [ ] Are tool versions pinned (reproducible)?
- [ ] Is CI a required check for merge?

## Common issues

### Symptom: CI green despite failing tests
- **Cause:** `continue-on-error` / non-failing test command.
- **Fix:** make the test stage fail the build; remove error suppression.

### Symptom: CI is slow
- **Cause:** no caching / redundant work.
- **Fix:** cache dependencies + build artifacts; parallelize independent stages.

### Symptom: "Works locally, fails in CI"
- **Cause:** unpinned versions / environment drift.
- **Fix:** pin tool versions; ensure local commands match CI (`scripts/validate == CI`).

### Symptom: Secret leaked in CI logs
- **Cause:** secret in config or echoed in a step.
- **Fix:** use the platform secret store; never print secrets (see `security/secret-scanner`).

### Symptom: Red CI can still be merged
- **Cause:** status check not required.
- **Fix:** configure the pipeline as a required check on the protected branch.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the target CI platform docs.
- Open an issue with the project type + generated config.
