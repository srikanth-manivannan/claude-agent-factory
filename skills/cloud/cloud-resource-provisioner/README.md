# Cloud Resource Provisioner

> Use this to provision cloud resources via IaC with least-privilege, tagging, and per-environment config.

**Category:** cloud · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Provisions cloud resources **as code** — parameterized per environment, with
least-privilege IAM, mandatory tags, secure-by-default networking/encryption, remote
locked state, and a reviewable plan + rollback. It turns "spin up some infra" into
governed, auditable, repeatable infrastructure with no click-ops drift.

## Quickstart

```text
1. Copy skills/cloud/cloud-resource-provisioner/ into your skills directory.
2. Invoke with: resources + cloud (+ iac_tool, environments, constraints).
3. Receive parameterized IaC + plan summary + rollback note.
```

## How it works

Eight steps: scope/environments → declare as IaC → least-privilege IAM → mandatory tags
→ secure defaults → remote locked state/idempotency → plan + rollback → output.
Authoritative procedure in [SKILL.md](SKILL.md); build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

## Inputs & outputs

- **Inputs:** `resources`, `cloud`, optional `iac_tool`, `environments`, `constraints`.
- **Outputs:** parameterized IaC + least-privilege IAM + tags + state config + plan/rollback.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Cloud / IaC tool** — emit AWS/GCP/Azure with Terraform/Pulumi/etc.
- **Environments** — add/adjust dev/staging/prod parameterization.
- **Chain** into `provision-infrastructure` / `deploy-to-production` workflows.

## Limitations

- Provisions resources; reusable module authoring is `devops/iac-module-builder` *(planned)*.
- Cost analysis/optimization is `cloud/cloud-cost-optimizer` *(planned)*.
- Tool *execution* (apply) is run by your IaC tool/CI, gated by review.

## Related

See [RESOURCES.md](RESOURCES.md). Feeds `provision-infrastructure` / `deploy-to-production`;
pairs with `devops/ci-pipeline-generator`, `devops/iac-module-builder` *(planned)*;
composes into `team-platform` / `play-zero-to-production`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
- **Implementation guidance:** [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Future improvements

- Policy-as-code checks (OPA/tfsec-style) wired into the plan step.
- Drift detection + reconciliation guidance.
- Module extraction once `devops/iac-module-builder` exists.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
