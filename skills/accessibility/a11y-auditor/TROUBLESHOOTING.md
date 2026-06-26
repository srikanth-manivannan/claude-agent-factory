# Troubleshooting — Accessibility Auditor

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/accessibility.md](../../../standards/accessibility.md).

## Quick diagnostics

- [ ] Is a target WCAG level set (AA default)?
- [ ] Does each finding cite an element AND a success criterion?
- [ ] Is each finding severity-tagged with a concrete fix?
- [ ] Are manual-verification items flagged?

## Common issues

### Symptom: Findings are vague
- **Cause:** not tied to element + criterion.
- **Fix:** cite the specific element and WCAG SC number; name the fixer skill.

### Symptom: "Fully accessible" but users still struggle
- **Cause:** relied on automated checks only.
- **Fix:** run the flagged manual screen-reader/keyboard verification.

### Symptom: Too many low-value findings
- **Cause:** severity not by user impact.
- **Fix:** re-rank — does it block a task (🔴) or annoy (🟡)?

### Symptom: AAA findings mixed with AA
- **Cause:** level scope unclear.
- **Fix:** mark AAA-only findings distinctly; default scope is AA.

### Symptom: Redundant ARIA recommended
- **Cause:** ARIA over native semantics.
- **Fix:** prefer native elements; add ARIA only to fill gaps (Robust principle).

## Getting more help

- Re-read [SKILL.md](SKILL.md) and [accessibility-review](../../../standards/checklists/accessibility-review.md).
- Open an issue with the UI snippet + produced report.
