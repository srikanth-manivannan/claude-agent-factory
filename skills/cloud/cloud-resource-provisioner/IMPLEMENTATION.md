# Implementation Guidance — Cloud Resource Provisioner

> How to go from a resource list to a reviewed, applied environment. See [SKILL.md](SKILL.md)
> and [/standards/security.md](../../../standards/security.md).

## Build order

1. **Remote state first** — configure a locked, remote backend before creating resources.
2. **Network/foundation** — VPC/subnets/security groups (private by default).
3. **Resources** — compute/storage/managed services, parameterized by `env`.
4. **IAM** — least-privilege roles/policies per resource.
5. **Tags** — mandatory tag block applied everywhere.
6. **Plan → review → apply** — never apply unreviewed to prod.

## Per-environment pattern

Parameterize differences; never copy-paste environments:
```hcl
variable "env" {}
locals {
  size      = { dev = "small",  prod = "large"  }[var.env]
  replicas  = { dev = 1,        prod = 3        }[var.env]
  tags      = { environment = var.env, managed_by = "iac", owner = "team-x", cost_center = "cc-42" }
}
```

## Least-privilege rule

> Start from **zero** permissions and add only the specific actions a resource needs.
> Wildcards (`*`, `iam:*`) are rejected in review. Prefer scoped resource ARNs.

## Secure defaults checklist

- [ ] No public IPs / `0.0.0.0/0` ingress unless explicitly justified.
- [ ] Encryption at rest + in transit on by default.
- [ ] Secrets via a secrets manager — **never** in code or state.
- [ ] Mandatory tags present (owner, environment, cost-center, managed-by).
- [ ] Remote, locked state; idempotent, re-runnable plans.

## State & secrets

State can contain sensitive values — store it remotely with encryption + locking, and
restrict access. Reference secrets at apply time from a manager; do not commit them.

## Apply & rollback

Produce a `plan` diff for review (PR). For risky changes prefer **replace** over
in-place mutation; document the rollback (revert to the previous plan/version). Run
applies through CI ([`ci-pipeline-generator`](../../devops/ci-pipeline-generator/)) with
the plan as a required, reviewed artifact. Add policy-as-code checks where available.
