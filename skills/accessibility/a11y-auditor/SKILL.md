---
name: a11y-auditor
description: Use this to audit a UI against WCAG and report prioritized, actionable accessibility fixes.
version: 0.1.0
category: accessibility
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [accessibility, a11y, wcag, audit, ui]
---

# Accessibility Auditor

> Use this to audit a UI against WCAG and report prioritized, actionable accessibility fixes.

> **Tech profile** — Technology: any UI · Language: any · Stack: any frontend · Toolchain: any · Domain: accessibility
> *(Audits any markup/UI; target WCAG level is configurable.)*

## When to use this skill

- Auditing a page/component against WCAG (AA default) before release.
- Producing the findings that feed the `accessibility-audit` workflow.
- Establishing an a11y baseline for an existing UI.

## When NOT to use this skill

- Applying fixes — use `accessibility/aria-annotator`, `color-contrast-fixer`,
  `keyboard-nav-checker` (this skill *finds*; they *fix*).
- Deep screen-reader QA — use `accessibility/screen-reader-tester`.

## Prerequisites

- The UI to audit (markup, component, or page) and the target WCAG level.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `ui` | yes | The markup/component/page to audit |
| `wcag_level` | no | A / AA (default) / AAA |
| `context` | no | Intended use, interactions, key flows |

## Instructions

1. **Set the target level.** Default WCAG 2.2 **AA** ([/standards/accessibility.md](../../../standards/accessibility.md)).
2. **Audit across the four POUR principles**, producing findings:
   - **Perceivable** — text alternatives, contrast, meaning not by color alone.
   - **Operable** — keyboard operability, focus order, visible focus, no traps.
   - **Understandable** — labels, error messaging, predictable behavior.
   - **Robust** — valid semantics, correct (non-redundant) ARIA.
3. **Cite each finding** to a specific element + the WCAG success criterion (e.g. 1.4.3).
4. **Severity-tag** 🔴/🟠/🟡 by user impact (blocks a task vs. annoyance).
5. **Recommend a concrete fix** per finding and name the skill that applies it.
6. **Note what passed** (don't only list problems).
7. **Flag what needs manual verification** (e.g. screen-reader pass) — automation
   can't catch everything.

## Output

A prioritized accessibility report: findings grouped by POUR, each with element +
WCAG criterion + severity + recommended fix (and the fixer skill), a "passed" summary,
and a manual-verification list. Maps onto the
[accessibility-review checklist](../../../standards/checklists/accessibility-review.md).

## Constraints & safety

- **Target AA by default**; never silently lower the bar.
- **Findings are actionable** — element-specific + criterion-cited; no vague "improve a11y".
- **Honest about automation limits** — flag what needs human verification.

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** a form with an unlabeled input and low-contrast text.
**Produces:** 🔴 missing label (WCAG 3.3.2 → `aria-annotator`), 🟠 contrast 3.1:1
(WCAG 1.4.3 → `color-contrast-fixer`), plus a keyboard-nav manual-check note.
