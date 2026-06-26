# Implementation Guidance — Accessibility Auditor

> How to apply this skill. See [SKILL.md](SKILL.md) and
> [/standards/accessibility.md](../../../standards/accessibility.md).

## Build order

1. **Set the target level** (WCAG 2.2 AA default).
2. **Audit across POUR** — Perceivable, Operable, Understandable, Robust.
3. **Cite each finding** to an element + a WCAG success criterion (e.g. 1.4.3).
4. **Severity-tag** by user impact; recommend a fix + name the fixer skill.
5. **Note passes** + flag what needs **manual** (screen-reader/keyboard) verification.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Level | AA default; mark AAA-only findings distinctly |
| ARIA | Semantic HTML first; ARIA only to fill gaps |
| Automation | Flag what automation can't judge (don't claim full compliance) |

## Pitfalls

- ❌ "Improve a11y" → ✅ cite element + criterion + concrete fix.
- ❌ "Fully accessible" from automated checks → ✅ require a screen-reader pass.
- ❌ Severity by ease, not impact → ✅ does it block a task (🔴) or annoy (🟡)?

## Hand-off

Findings feed the fixer skills (`aria-annotator`, `color-contrast-fixer`,
`keyboard-nav-checker`) and the `accessibility-audit` workflow.
