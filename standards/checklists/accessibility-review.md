# Accessibility Review Checklist

> Reviews UI accessibility (target WCAG AA by default). Run **after** the
> [Universal Core](_universal.md). Backs the `accessibility-audit` workflow.
> Legend: [README.md](README.md).

**Applies to:** any user-facing UI · **Min standard:** 0.1.0

## Automated baseline
- [ ] 🟠 `[auto]` Automated a11y scan passes at the target WCAG level (AA default).
- [ ] 🟠 `[auto]` Color contrast meets WCAG AA for text and UI components.

## Operability
- [ ] 🔴 `[manual]` All interactive elements are keyboard-operable.
- [ ] 🟡 `[manual]` Focus order is logical; focus indicator is visible.
- [ ] 🟡 `[manual]` Motion/animation respects `prefers-reduced-motion`.

## Perceivability & semantics
- [ ] 🟠 `[manual]` Semantic HTML used; ARIA roles/labels correct (no redundant ARIA).
- [ ] 🟠 `[manual]` Images/media have meaningful text alternatives.
- [ ] 🟡 `[manual]` Meaning is not conveyed by color alone.

## Forms & flows
- [ ] 🟡 `[manual]` Form fields have labels and accessible error messaging.
- [ ] 🟠 `[manual]` Screen-reader pass completed for key user flows.
