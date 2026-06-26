---
name: play-enterprise-api-delivery
description: Use this playbook to deliver an enterprise API from design through secure, tested production release.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [playbook, pipeline, api, backend, enterprise]
---

# Enterprise API Delivery Pipeline (Playbook)

> Use this playbook to deliver an enterprise API from design through secure, tested production release.

The top tier: composes **teams + workflows** for a complete outcome
([/standards/architecture.md](../../standards/architecture.md)). This is a *reference
engineering pipeline* — it proves the framework coordinates whole-lifecycle delivery,
not just isolated skills.

## Objective
Take an API from requirements to a deployed, documented, security-reviewed production
release that an enterprise team can operate.

## Composition

**Teams**
- `team-backend` — designs + builds the API (api-architect, backend-engineer, qa-engineer).
- `team-security` — secures it (security-engineer, api-architect, qa-engineer).

**Workflows (sequenced)**
1. `build-feature` — implement the API feature (contract → code → tests → PR).
2. `database-migration` — apply schema changes safely (reversible, tested rollback).
3. `review-pr` — structured review with findings.
4. `security-audit` — threats, deps, secrets, config (authorized).
5. `release-pipeline` — cut → verify → deploy → announce.

## Operating guide (pipeline stages)
1. **Design** — `team-backend`'s api-architect sets the contract + system design.
2. **Build** — run `build-feature`; `database-migration` if the schema changes.
3. **Review** — run `review-pr`; `team-security` runs `security-audit` (gate on blockers).
4. **Release** — run `release-pipeline` to production with rollback ready.
5. **Operate** — hand operational ownership to the team; incidents → `incident-response`.

## Success criteria
- API meets its contract; tests green; no open security blockers; deployed with a tested
  rollback; docs current.

## Failure handling
- Security blocker → stop at stage 3; remediate before release.
- Failed deploy → automatic rollback (`release-pipeline`); investigate before retry.
