# Accessibility Standard

> Accessibility rules for user-facing artifacts. Enforced by the
> [accessibility-review checklist](checklists/accessibility-review.md).

**Min standard:** 0.1.0 · Applies to: any artifact producing UI. See also:
[documentation.md](documentation.md).

## Target

**WCAG 2.2 Level AA** by default. Higher (AAA) only when specified; never lower.

## Core rules

- **Keyboard operable.** Every interactive element works without a mouse; focus order
  is logical and the focus indicator is visible.
- **Perceivable.** Sufficient color contrast (AA); meaning never conveyed by color
  alone; images/media have text alternatives.
- **Semantic first.** Use native semantic elements; add ARIA only to fill gaps
  (no redundant/incorrect ARIA).
- **Forms.** Every field has a label and accessible error messaging.
- **Respect preferences.** Honor `prefers-reduced-motion` and similar.

## Verification

- Automated scan must pass at the target level (the a11y skills in [TAXONOMY](../TAXONOMY.md)).
- A **screen-reader pass** is required for key flows — automation alone is insufficient.

> Accessibility is part of "done," not a follow-up. UI artifacts that fail AA do not
> ship (VISION §6).
