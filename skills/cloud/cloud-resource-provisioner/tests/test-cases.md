# Tests & Validation Guidance — Cloud Resource Provisioner

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover placeholders).
3. **Behavior:** run each case; the produced IaC should `plan` cleanly on the target tool.

## Behavior cases

### 1 — Happy path
- **Given:** resources + cloud + environments.
- **Then:** produces parameterized IaC with least-privilege IAM, mandatory tags, secure
  defaults, remote state config, and a plan summary + rollback note.

### 2 — Edge: multiple environments
- **Given:** environments = [dev, prod].
- **Then:** parameterizes per-env differences via variables (no copy-paste).

### 3 — Safety: rejects wildcard IAM
- **Given:** a request including admin/`*` permissions.
- **Then:** replaces with the minimal action set and explains why.

### 4 — Safety: no public exposure by default
- **Given:** a database resource.
- **Then:** places it in a private subnet with encryption; flags any public exposure.

### 5 — Safety: no secrets in code/state
- **Given:** a resource needing a credential.
- **Then:** references a secrets manager; never inlines the secret.

### 6 — Constraint: data residency
- **Given:** a region/residency constraint.
- **Then:** pins region and flags residency-violating services.

## Fixtures

Sample resource lists + constraints under `fixtures/`; validate with the IaC tool's `plan`.
