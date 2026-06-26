# Troubleshooting — {{TITLE}}

> Symptom → cause → fix guidance for an artifact. Technology-agnostic: describe
> symptoms behaviorally and pull stack specifics from the Tech profile, so the
> same guide serves any technology.

> **Tech profile** — Technology: {{TECHNOLOGY}} · Language: {{LANGUAGE}} ·
> Stack: {{STACK}} · Toolchain: {{TOOLCHAIN}} · Domain: {{DOMAIN}}

## How to use this guide

Find your **symptom**, confirm the **likely cause**, apply the **fix**. If nothing
matches, see "Getting more help".

## Quick diagnostics

Run these first to localize the problem:

- [ ] `scripts/validate` passes? (rules out structural/standards issues)
- [ ] All `{{PLACEHOLDERS}}` replaced? (a leftover placeholder is the #1 cause)
- [ ] Tech profile filled correctly for your stack?
- [ ] Referenced artifacts exist at the declared versions?

## Common issues

### Symptom: <what the user observes>
- **Likely cause:** …
- **Confirm:** how to verify this is the cause.
- **Fix:** concrete steps.
- **Prevent:** how to avoid it recurring.

### Symptom: <another observable problem>
- **Likely cause / Confirm / Fix / Prevent:** …

### Symptom: leftover `{{PLACEHOLDER}}` / validation lint failure
- **Cause:** a template placeholder was not replaced.
- **Fix:** search the artifact for `{{` and replace or set tech-profile fields to `n/a`.

## Error reference

| Error / message | Meaning | Fix |
|-----------------|---------|-----|
| … | … | … |

## Known limitations

Things that are **expected** behavior, not bugs (link to README "Limitations").

## Getting more help

- Re-read the spec file and `standards/`.
- Open an issue using the bug-report template (include `scripts/validate` output).
