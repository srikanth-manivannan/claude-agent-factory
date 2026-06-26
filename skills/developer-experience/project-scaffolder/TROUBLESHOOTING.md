# Troubleshooting — Project Scaffolder

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Quick diagnostics

- [ ] Does a fresh clone `setup` then `test` green?
- [ ] Are the standard task verbs present (setup/test/lint/build/run)?
- [ ] Is CI wired and set as a required check?
- [ ] Is there an `.env.example` (and no committed `.env`)?

## Common issues

### Symptom: Fresh clone won't build/test
- **Cause:** hidden setup steps / undocumented deps.
- **Fix:** make `setup` install everything; verify on a clean checkout (golden-path rule).

### Symptom: Contributors relearn commands per repo
- **Cause:** inconsistent task names.
- **Fix:** expose the same verbs (setup/test/lint/build/run) everywhere.

### Symptom: Style debates in review
- **Cause:** lint/format not automated.
- **Fix:** pre-commit + CI lint; style is enforced, not argued.

### Symptom: "We'll add tests/CI later"
- **Cause:** scaffold shipped without the golden path.
- **Fix:** bake test harness + CI in from commit one (that's the point of this skill).

### Symptom: Secret committed via .env
- **Cause:** real `.env` shipped.
- **Fix:** ship `.env.example`; gitignore `.env`; rotate if leaked (`secret-scanner`).

### Symptom: CI not enforced
- **Cause:** status check not required.
- **Fix:** mark CI required on the protected branch (note in CODEOWNERS/repo settings).

## Getting more help

- Re-read [SKILL.md](SKILL.md); for CI specifics, `devops/ci-pipeline-generator`.
- Open an issue with project_type + stack + the generated tree.
