# Showcase — AWS Serverless Platform

> **Scenario:** A platform team is standing up a serverless workload (an event-processing
> service) on AWS and must provision it as code, deliver a function, release it, and have
> incident operations ready. This showcase walks that project through the framework
> end-to-end.

> Demonstration only — composes existing artifacts. AWS is a concrete example; the cloud
> skills are provider-agnostic (tech profile carries specifics).

## The framework artifacts used

**Playbook:** [`play-aws-serverless-delivery`](../../../playbooks/play-aws-serverless-delivery/)
**Team:** [`team-platform`](../../../teams/team-platform/) → agents
[`platform-engineer`](../../../agents/platform-engineer/), [`security-engineer`](../../../agents/security-engineer/),
[`qa-engineer`](../../../agents/qa-engineer/)
**Workflows:** build-feature · database-migration · release-pipeline · incident-response
**Skills (via agents/workflows):** cloud/cloud-resource-provisioner · devops/ci-pipeline-generator ·
developer-experience/project-scaffolder · database/schema-designer · architecture/migration-planner ·
database/migration-writer · testing/unit-test-generator · security/secret-scanner ·
devops/release-automator · devops/cd-deployment-builder · devops/observability-instrumenter ·
devops/incident-runbook-builder · leadership/stakeholder-comms-writer

## End-to-end walkthrough

### 1. Bootstrap + provision — `team-platform` (platform-engineer)
- **developer-experience/project-scaffolder** lays the golden-path repo (lint, CI, docs);
- **cloud/cloud-resource-provisioner** provisions the VPC, function, queue, and a private
  datastore **as code** — least-privilege IAM, mandatory tags, encryption, per-env config;
- **devops/ci-pipeline-generator** wires the required-check CI gate.

### 2. Build the function — `build-feature`
- The event-processing function is implemented with **testing/unit-test-generator** coverage.
- If it has state: **database-migration** (schema-designer → migration-planner →
  migration-writer) applies it safely.

### 3. Secure — `security-engineer`
- **security/secret-scanner** confirms no secrets in code/IaC/state (secrets via a manager).

### 4. Release — `release-pipeline`
- **release-automator** + **changelog-generator** cut the release; **cd-deployment-builder**
  deploys with rollback to the cloud environment.

### 5. Operate — `incident-response`
- **devops/observability-instrumenter** wires logs/metrics/traces;
  **devops/incident-runbook-builder** produces the runbook; on an incident,
  **leadership/stakeholder-comms-writer** drives status comms (mitigate first, postmortem after).

## Outcome
A serverless workload provisioned entirely as code (least-privilege, tagged, encrypted),
delivered through CI, released with rollback, and operable with observability + a runbook
— the full platform lifecycle coordinated by one playbook and one team.

## Try it
Start from [`play-aws-serverless-delivery`](../../../playbooks/play-aws-serverless-delivery/)
and follow its operating guide.
