# Showcase — Enterprise React Application

> **Scenario:** A team is building an enterprise web app (a customer admin console) in
> React and must ship features that are accessible (WCAG AA), performant, tested, and
> safely released. This showcase walks that project through the framework end-to-end.

> Demonstration only — it composes existing artifacts; it is not a catalog artifact.
> Every artifact named below exists and resolves (`scripts/validate`).

## The framework artifacts used

**Playbook:** [`play-react-enterprise-dev`](../../../playbooks/play-react-enterprise-dev/)
**Team:** [`team-frontend`](../../../teams/team-frontend/) → agents
[`frontend-engineer`](../../../agents/frontend-engineer/), [`qa-engineer`](../../../agents/qa-engineer/)
**Workflows:** build-feature · accessibility-audit · performance-optimization · review-pr · release-pipeline
**Skills (via agents/workflows):** frontend/component-scaffold · accessibility/a11y-auditor ·
accessibility/aria-annotator · accessibility/color-contrast-fixer · accessibility/keyboard-nav-checker ·
frontend/client-perf-optimizer · testing/unit-test-generator · testing/coverage-gap-finder ·
documentation/doc-writer · leadership/code-review-coach

## End-to-end walkthrough

### 1. Plan the feature
The team runs the **`plan-feature`** workflow (architecture/tradeoff-analyzer +
system-design-reviewer) to decide the component approach (e.g. "server state via query
cache vs. client store") and record the decision.

### 2. Build the UI feature — `team-frontend` + `build-feature`
- `frontend-engineer` uses **frontend/component-scaffold** to scaffold the data-table
  component (accessible markup + state + a passing test, via **testing/unit-test-generator**).
- Docs updated via **documentation/doc-writer**; a PR is opened.

### 3. Make it accessible — `accessibility-audit`
- **accessibility/a11y-auditor** audits to WCAG AA → finds an unlabeled filter control,
  a 3.1:1 contrast chip, and a non-operable custom dropdown.
- Remediated with **aria-annotator** (labels), **color-contrast-fixer** (contrast), and
  **keyboard-nav-checker** (focus + operability). Re-audit: AA met.

### 4. Make it fast — `performance-optimization`
- **frontend/client-perf-optimizer** measures a baseline, finds an oversized bundle +
  unnecessary re-renders, fixes them, and verifies against the budget (p95 interaction).

### 5. Review — `review-pr`
- `qa-engineer` runs **review-pr** (leadership/code-review-coach + coverage check via
  **testing/coverage-gap-finder** + docs via **documentation/doc-linter**). Findings
  resolved; verdict: approve.

### 6. Release — `release-pipeline`
- **devops/release-automator** + **documentation/changelog-generator** cut the release;
  CI (**devops/ci-pipeline-generator**) verifies; **devops/cd-deployment-builder**
  deploys with rollback. An a11y check stays in CI to prevent regression.

## Outcome
A feature shipped to production that is accessible (AA), within performance budget,
tested, reviewed, and rollback-safe — coordinated by **one playbook** rather than a pile
of disconnected steps.

## Try it
Start from [`play-react-enterprise-dev`](../../../playbooks/play-react-enterprise-dev/)
and follow its operating guide; fork the named skills into your project.
