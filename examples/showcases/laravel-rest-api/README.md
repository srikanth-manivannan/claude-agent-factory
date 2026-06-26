# Showcase — Laravel REST API

> **Scenario:** A team is delivering a secure REST API (an orders service) in Laravel and
> must take it from contract to a security-gated production release. This showcase walks
> that project through the framework end-to-end.

> Demonstration only — composes existing artifacts. Laravel/PHP are concrete examples;
> the skills are technology-agnostic (tech profile carries specifics).

## The framework artifacts used

**Playbooks:** [`play-enterprise-api-delivery`](../../../playbooks/play-enterprise-api-delivery/)
(delivery) + [`play-secure-software-delivery`](../../../playbooks/play-secure-software-delivery/) (security gate)
**Teams:** [`team-backend`](../../../teams/team-backend/), [`team-security`](../../../teams/team-security/) → agents
[`api-architect`](../../../agents/api-architect/), [`backend-engineer`](../../../agents/backend-engineer/),
[`security-engineer`](../../../agents/security-engineer/), [`qa-engineer`](../../../agents/qa-engineer/)
**Workflows:** plan-feature · build-feature · database-migration · review-pr · security-audit · release-pipeline
**Skills (via agents/workflows):** backend/openapi-designer · backend/rest-endpoint-scaffold ·
database/schema-designer · architecture/migration-planner · database/migration-writer ·
architecture/system-design-reviewer · architecture/tradeoff-analyzer · testing/unit-test-generator ·
security/secret-scanner · security/dependency-vuln-auditor · security/threat-modeler ·
security/security-headers-configurer · documentation/doc-writer · documentation/changelog-generator

## End-to-end walkthrough

### 1. Design the contract — `team-backend` (api-architect)
- **backend/openapi-designer** authors the `orders` API contract (paths, schemas, errors,
  bearer auth); **architecture/system-design-reviewer** reviews it; **tradeoff-analyzer**
  settles the datastore choice.

### 2. Model + migrate data — `database-migration`
- **database/schema-designer** designs the orders schema; **architecture/migration-planner**
  plans a phased rollout; **database/migration-writer** writes the reversible migration
  (expand/contract, tested rollback).

### 3. Build the endpoints — `build-feature` (backend-engineer)
- **backend/rest-endpoint-scaffold** implements endpoints to the contract with validation
  + error handling; **testing/unit-test-generator** covers happy/edge/failure.

### 4. Secure it — `play-secure-software-delivery` / `security-audit` (team-security)
- **security/threat-modeler** runs STRIDE on the design; **secret-scanner** confirms no
  committed secrets; **dependency-vuln-auditor** clears CVEs; **security-headers-configurer**
  hardens responses. **Release is gated** on no open 🔴 findings.

### 5. Review — `review-pr`
- `qa-engineer` runs **review-pr** (code-review-coach + dependency audit + doc-linter).

### 6. Release — `release-pipeline`
- **release-automator** + **changelog-generator** cut the release; CI verifies;
  **cd-deployment-builder** deploys with rollback.

## Outcome
A REST API delivered from contract to production with data migrated safely, security
verified and **gating** the release, tests green, and a clean changelog — two playbooks
coordinating two teams across the lifecycle.

## Try it
Start from [`play-enterprise-api-delivery`](../../../playbooks/play-enterprise-api-delivery/);
layer [`play-secure-software-delivery`](../../../playbooks/play-secure-software-delivery/)
for the security gate.
