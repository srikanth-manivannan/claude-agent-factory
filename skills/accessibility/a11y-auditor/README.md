# Accessibility Auditor

> Use this to audit a UI against WCAG and report prioritized, actionable accessibility fixes.

**Category:** accessibility · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Audits a UI against WCAG (2.2 AA by default) across the four POUR principles and
returns a **prioritized, element-specific report** — each finding cites a success
criterion, a severity by user impact, and a concrete fix (naming the fixer skill).
It also lists what passed and what needs manual (screen-reader) verification, because
honest a11y work never pretends automation catches everything.

## Quickstart

```text
1. Copy skills/accessibility/a11y-auditor/ into your skills directory.
2. Invoke with the UI/markup (+ wcag_level if not AA).
3. Receive a POUR-grouped, severity-ranked findings report with fixes.
```

## How it works

Seven steps: set level → audit POUR → cite element + criterion → severity-tag →
recommend fix → note passes → flag manual checks. Authoritative procedure in
[SKILL.md](SKILL.md). Output maps onto the
[accessibility-review checklist](../../../standards/checklists/accessibility-review.md).

## Inputs & outputs

- **Inputs:** `ui`, optional `wcag_level`, optional `context`.
- **Outputs:** POUR-grouped findings (element + criterion + severity + fix) + passed
  summary + manual-verification list.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Target level** — A / AA / AAA.
- **Scope** — single component vs. full page/flow.
- **Chain** the fixes into `aria-annotator`, `color-contrast-fixer`, `keyboard-nav-checker`.

## Limitations

- Automated auditing can't fully judge screen-reader UX or cognitive load — it flags
  these for manual verification.
- It finds and recommends; it does not apply fixes.

## Related

See [RESOURCES.md](RESOURCES.md). Drives the `accessibility-audit` workflow; pairs with
`frontend/component-scaffold` to build accessible UI from the start.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Map findings to automated test assertions (axe-style) for regression prevention.
- Cognitive-accessibility heuristics.
- Per-criterion remediation snippets.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
