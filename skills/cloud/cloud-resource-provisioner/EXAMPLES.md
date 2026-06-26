# Examples — Cloud Resource Provisioner

> Realistic enterprise scenarios. Provider/tool-agnostic method; examples use AWS +
> Terraform-style pseudocode. See [SKILL.md](SKILL.md).

## Example 1 — Service + private DB across environments (happy path)

**Inputs:** resources = VPC (private) + managed Postgres + a service; cloud = AWS;
environments = [dev, prod].

**Produces (sketch):**
```hcl
variable "env" {}                      # dev | prod
locals {
  sizes = { dev = "small", prod = "large" }
  tags  = { owner = "team-x", environment = var.env, cost_center = "cc-42", managed_by = "iac" }
}
resource "db_instance" "app" {
  size              = local.sizes[var.env]
  subnet            = module.vpc.private_subnet     # private by default
  storage_encrypted = true                          # encryption at rest
  tags              = local.tags
}
resource "iam_role" "service" {
  # least privilege: only the DB connect + read its own secret
  policy = least_privilege_policy(["rds-db:connect", "secretsmanager:GetSecretValue:app/*"])
}
```
Plus: remote locked state config, no public IP on the DB, a plan summary, and a rollback
note ("replace, don't in-place, the DB size change").

## Example 2 — Least-privilege enforced

**Inputs:** a request that includes `iam:*` (admin) for convenience.

**Behavior:** **rejects the wildcard** and replaces it with the minimal action set the
resource actually needs, noting why — secure defaults over convenience.

## Example 3 — Edge: data-residency constraint

**Inputs:** `constraints: data must stay in eu-west-1`.

**Behavior:** pins region per resource, flags any global/multi-region service that would
violate residency, and documents the constraint in the plan.

## Anti-example

- ❌ Creating resources in the console "just this once" — drift, no audit, not
  reproducible. Everything as code.
- ❌ A public database with `0.0.0.0/0` ingress. Private subnet + least-privilege SG.
- ❌ Hardcoding a DB password in the IaC/state. Reference a secrets manager.

## Try it yourself

- Add a `staging` environment — note parameterization, not duplication.
- Add `constraints: PCI` — observe stricter network segmentation in the plan.
