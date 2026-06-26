---
name: cloud-resource-provisioner
description: Use this to provision cloud resources via IaC with least-privilege, tagging, and per-environment config.
version: 0.1.0
category: cloud
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [cloud, iac, provisioning, least-privilege, environments]
---

# Cloud Resource Provisioner

> Use this to provision cloud resources via IaC with least-privilege, tagging, and per-environment config.

> **Tech profile** — Technology: cloud infrastructure · Language: IaC (HCL/etc.) · Stack: any cloud · Toolchain: any IaC tool · Domain: cloud
> *(Provider- and tool-agnostic method; emit config for the target cloud/IaC via the tech profile.)*

## When to use this skill

- Provisioning new cloud resources (compute, storage, network, managed services) as code.
- Standardizing environments (dev/staging/prod) with consistent config + guardrails.
- Producing the infrastructure layer the `provision-infrastructure` / `deploy-to-production`
  workflows depend on.

## When NOT to use this skill

- Authoring reusable IaC modules — use `devops/iac-module-builder` *(planned)*.
- CI/CD pipelines — use `devops/ci-pipeline-generator`.
- Cost analysis — use `cloud/cloud-cost-optimizer` *(planned)*.

## Prerequisites

- The resources required and the **target cloud + IaC tool**.
- The **environments** to support and any compliance/network constraints.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `resources` | yes | What to provision (compute/storage/network/managed services) |
| `cloud` | yes | Target provider (AWS/GCP/Azure/…) |
| `iac_tool` | no | Terraform/Pulumi/etc. (defaults to the project's tool) |
| `environments` | no | e.g. dev/staging/prod (defaults to a single env) |
| `constraints` | no | Compliance, region/residency, network topology |

## Instructions

1. **Confirm scope + environments.** List the resources and the environments; identify
   what differs per environment (size, replicas, flags) vs. what's shared.
2. **Declare as IaC.** Express every resource as code — **no click-ops**. Parameterize
   per-environment differences with variables, not copy-paste.
3. **Apply least-privilege IAM.** Each resource/role gets the minimum permissions it
   needs; no wildcard admin ([/standards/security.md](../../../standards/security.md)).
4. **Tag everything.** Mandatory tags (owner, environment, cost-center, managed-by=IaC)
   for cost attribution and governance.
5. **Secure by default.** Private networking by default, encryption at rest/in transit,
   no public exposure unless explicitly required + justified.
6. **State + idempotency.** Use remote, locked IaC state; ensure plans are idempotent
   and re-runnable. Never store secrets in state/code — use a secrets manager.
7. **Plan before apply + rollback.** Produce a reviewable plan/diff; define how to roll
   back (and prefer immutable/replace over in-place for risky changes).
8. **Output the config + a plan summary** and a per-environment promotion path.

## Output

IaC configuration for the target cloud/tool: parameterized per-environment resources,
least-privilege IAM, mandatory tags, secure-by-default networking/encryption, remote
locked state config, and a plan summary + rollback note. Ready for the
`provision-infrastructure` workflow.

## Constraints & safety

- **Everything as code** — no manual console changes (drift).
- **Least privilege + secure defaults** — private, encrypted, minimally-permissioned.
- **No secrets in code/state** — reference a secrets manager.
- **Plan → review → apply** — never apply an unreviewed change to prod.

## Examples

Minimal below; full enterprise examples in [EXAMPLES.md](EXAMPLES.md); build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

**Given:** resources = a private VPC + a managed Postgres + a service container; cloud =
AWS; environments = [dev, prod].
**Produces:** parameterized IaC (env-sized), DB in a private subnet with encryption,
least-privilege role for the service, mandatory tags, and a plan summary.
