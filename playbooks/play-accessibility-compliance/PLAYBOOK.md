---
name: play-accessibility-compliance
description: Use this playbook to bring a product to WCAG AA compliance and keep it there through release.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [playbook, pipeline, accessibility, wcag, compliance]
---

# Accessibility Compliance Pipeline (Playbook)

> Use this playbook to bring a product to WCAG AA compliance and keep it there through release.

The top tier: composes **teams + workflows** for a complete outcome. A reference
engineering pipeline that takes a product to accessibility compliance and prevents
regressions at release.

## Objective
Achieve and sustain WCAG 2.2 AA compliance: audit, remediate, verify, and gate releases
so accessibility doesn't regress.

## Composition

**Teams**
- `team-frontend` — frontend-engineer + qa-engineer (remediation + verification).

**Workflows (sequenced)**
1. `accessibility-audit` — audit against WCAG AA; remediate findings.
2. `review-pr` — review the remediations (a11y findings included).
3. `release-pipeline` — ship the compliant build.

## Operating guide (pipeline stages)
1. **Audit** — `team-frontend` runs `accessibility-audit`; categorize by severity.
2. **Remediate** — fix blockers (ARIA, contrast, keyboard); re-audit to confirm.
3. **Review** — run `review-pr`; gate on open a11y blockers.
4. **Release** — run `release-pipeline`; a11y check stays in CI to prevent regression.

## Success criteria
- Target WCAG AA met (automated + screen-reader pass); no open a11y blockers; an a11y
  check guards future releases.

## Failure handling
- Open a11y blocker → block release; remediate + re-audit.
- New regression → caught by the CI a11y check; route back to remediation.
