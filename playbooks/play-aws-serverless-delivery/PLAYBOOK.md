---
name: play-aws-serverless-delivery
description: Use this playbook to deliver a serverless workload to a cloud platform with operations in place.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [playbook, pipeline, cloud, serverless, platform]
---

# AWS Serverless Delivery Pipeline (Playbook)

> Use this playbook to deliver a serverless workload to a cloud platform with operations in place.

The top tier: composes **teams + workflows** for a complete outcome. A reference
engineering pipeline for cloud/serverless delivery (cloud-agnostic method; AWS is the
canonical example via the tech profile).

## Objective
Provision the platform, deliver a serverless workload, release it, and have incident
operations ready.

## Composition

**Teams**
- `team-platform` — platform-engineer + security-engineer + qa-engineer (infra, CI/CD, security).

**Workflows (sequenced)**
1. `build-feature` — implement the serverless function/feature with tests.
2. `database-migration` — apply any datastore changes safely.
3. `release-pipeline` — cut → verify → deploy.
4. `incident-response` — operate: detect → mitigate → postmortem.

## Operating guide (pipeline stages)
1. **Platform** — `team-platform` provisions infra (IaC, least-privilege, per-env) + CI.
2. **Build** — run `build-feature`; `database-migration` if state changes.
3. **Release** — run `release-pipeline` to the cloud environment with rollback.
4. **Operate** — observability on; incidents run `incident-response`.

## Success criteria
- Infra provisioned as code (least-privilege, tagged); workload deployed with rollback;
  observability + incident runbook in place.

## Failure handling
- Provisioning/policy violation → fix in IaC before deploy.
- Production incident → `incident-response` (mitigate first, then root-cause).
