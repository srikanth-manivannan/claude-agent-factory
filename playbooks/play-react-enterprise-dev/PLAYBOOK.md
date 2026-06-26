---
name: play-react-enterprise-dev
description: Use this playbook to deliver accessible, performant enterprise frontend features to production.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [playbook, pipeline, frontend, accessibility, enterprise]
---

# React Enterprise Development Pipeline (Playbook)

> Use this playbook to deliver accessible, performant enterprise frontend features to production.

The top tier: composes **teams + workflows** for a complete outcome. A reference
engineering pipeline for enterprise frontend delivery (stack-agnostic method; "React" is
the canonical example — any component framework applies via the tech profile).

## Objective
Ship a frontend feature that is accessible (WCAG AA), performant, tested, reviewed, and
released to production.

## Composition

**Teams**
- `team-frontend` — frontend-engineer + qa-engineer (accessible, tested UI).

**Workflows (sequenced)**
1. `build-feature` — implement the UI feature (component → tests → docs → PR).
2. `accessibility-audit` — audit + remediate to WCAG AA.
3. `performance-optimization` — measure → fix → verify client performance.
4. `review-pr` — structured review with findings.
5. `release-pipeline` — cut → verify → deploy → announce.

## Operating guide (pipeline stages)
1. **Build** — `team-frontend` runs `build-feature` (a11y + tests baked in).
2. **Verify a11y** — run `accessibility-audit`; remediate blockers.
3. **Optimize** — run `performance-optimization` against a stated budget.
4. **Review** — run `review-pr`.
5. **Release** — run `release-pipeline`.

## Success criteria
- WCAG AA met; performance target hit; tests green; no review blockers; deployed.

## Failure handling
- A11y or perf blocker → resolve before review/release.
- Failed deploy → rollback via `release-pipeline`.
