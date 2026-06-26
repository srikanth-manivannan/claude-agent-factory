# Troubleshooting — Doc Writer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and
> [/standards/documentation.md](../../../standards/documentation.md).

## Quick diagnostics

- [ ] Are all required README sections present?
- [ ] Is the description a single action-oriented sentence?
- [ ] Is the Quickstart actually runnable?
- [ ] Do all links resolve and are there no leftover placeholders?

## Common issues

### Symptom: Docs describe features that don't exist
- **Cause:** aspirational writing.
- **Fix:** document only verified behavior; move wishes to "Future improvements".

### Symptom: README duplicates standards/guidance
- **Cause:** restating rules instead of linking.
- **Fix:** cross-reference the relevant `standards/*` doc.

### Symptom: Description is a paragraph
- **Cause:** over-explaining in `description`.
- **Fix:** one action-oriented sentence; details go in "What it does".

### Symptom: Quickstart doesn't work
- **Cause:** missing a step or assuming setup.
- **Fix:** test the steps end-to-end; include prerequisites.

### Symptom: Docs go stale quickly
- **Cause:** no link to source of truth.
- **Fix:** reference behavior sources; pair with `documentation/doc-linter`.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and
  [documentation-review](../../../standards/checklists/documentation-review.md).
- Open an issue with the subject + produced docs.
