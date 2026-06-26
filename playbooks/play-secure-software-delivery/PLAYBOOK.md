---
name: play-secure-software-delivery
description: Use this playbook to deliver software through a security-first pipeline with gated release.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [playbook, pipeline, security, sdlc, enterprise]
---

# Secure Software Delivery Pipeline (Playbook)

> Use this playbook to deliver software through a security-first pipeline with gated release.

The top tier: composes **teams + workflows** for a complete outcome. A reference
engineering pipeline that bakes security into every stage of delivery. Defensive,
authorized use only ([/standards/security.md](../../standards/security.md)).

## Objective
Deliver a change to production with security verified at design, build, review, and
release — release **gated** on security blockers.

## Composition

**Teams**
- `team-security` — security-engineer + api-architect + qa-engineer (secure-by-design + review).

**Workflows (sequenced)**
1. `build-feature` — implement with tests.
2. `security-audit` — threats, deps, secrets, config (authorized).
3. `review-pr` — structured review incl. security findings.
4. `release-pipeline` — cut → verify → deploy (gated on no open security blockers).
5. `incident-response` — operate with security incident readiness.

## Operating guide (pipeline stages)
1. **Secure design** — `team-security` reviews the design before build.
2. **Build** — run `build-feature`.
3. **Audit + review** — run `security-audit` then `review-pr`; **gate**: no open blockers.
4. **Release** — run `release-pipeline` only after the security gate passes.
5. **Operate** — `incident-response` ready; postmortems feed back into design.

## Success criteria
- No open security blockers at release; secrets clean; deps free of known CVEs; deployed
  with rollback; incident runbook ready.

## Failure handling
- Any 🔴 security finding → **block release**; remediate, re-audit.
- Security incident → `incident-response` (mitigate first).
