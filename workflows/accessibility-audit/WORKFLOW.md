---
name: accessibility-audit
description: Audit a UI against WCAG and remediate accessibility issues, then verify.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [accessibility, a11y, wcag, audit]
---

# Accessibility Audit (Workflow)

> Audit a UI against WCAG and remediate accessibility issues, then verify.

## Outcome

A UI that meets the target WCAG level, with issues found, fixed, and re-verified.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:accessibility/a11y-auditor` | 0.1.0 | WCAG findings |
| 3 | `skill:accessibility/aria-annotator` | 0.1.0 | ARIA fixes |
| 3 | `skill:accessibility/color-contrast-fixer` | 0.1.0 | contrast fixes |
| 3 | `skill:accessibility/keyboard-nav-checker` | 0.1.0 | keyboard fixes |

## Steps

1. **Audit** — evaluate the UI against the target WCAG level.
2. **Categorize** — group findings by type/severity (perceivable, operable, etc.).
3. **Remediate** — apply ARIA, contrast, and keyboard-navigation fixes.
4. **Verify** — re-audit; confirm issues resolved without regressions.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target_ui | yes | The page/component to audit |
| wcag_level | no | A / AA (default) / AAA |

## Outputs

A remediated UI + an accessibility report (before/after).

## Failure handling

- Fix introduces a visual regression → reconcile design vs a11y; don't silently drop the fix.
- Issue can't be fixed in markup → escalate to design.

## Constraints & safety

- Target WCAG AA by default unless otherwise specified.
