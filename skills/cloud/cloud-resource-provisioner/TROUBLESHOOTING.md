# Troubleshooting — Cloud Resource Provisioner

> Symptom → cause → fix. See [SKILL.md](SKILL.md), [IMPLEMENTATION.md](IMPLEMENTATION.md),
> and [/standards/security.md](../../../standards/security.md).

## Quick diagnostics

- [ ] Is every resource declared as code (no console changes)?
- [ ] Is IAM least-privilege (no wildcards)?
- [ ] Are mandatory tags present on every resource?
- [ ] Is state remote + locked, with no secrets in code/state?

## Common issues

### Symptom: Infra drift (console ≠ code)
- **Cause:** manual console changes (click-ops).
- **Fix:** make all changes via IaC; enable drift detection; reconcile.

### Symptom: Over-permissioned roles flagged in review
- **Cause:** wildcard IAM for convenience.
- **Fix:** scope to the minimal action set + resource ARNs (IMPLEMENTATION).

### Symptom: Resource publicly exposed
- **Cause:** default/0.0.0.0 ingress, public subnet.
- **Fix:** private subnet by default; restrict security groups; justify any exposure.

### Symptom: Secret leaked via state/code
- **Cause:** hardcoded secret.
- **Fix:** reference a secrets manager; encrypt + lock state; rotate the exposed secret
  (`security/secret-scanner`).

### Symptom: Environments diverge / copy-paste errors
- **Cause:** duplicated per-env config.
- **Fix:** parameterize with variables/locals keyed by `env`.

### Symptom: Risky apply broke prod
- **Cause:** applied an unreviewed/in-place change.
- **Fix:** plan → review (PR) → apply via CI; prefer replace over in-place; keep rollback.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the [deployment-review checklist](../../../standards/checklists/deployment-review.md).
- Open an issue with the resource list + plan summary (redact account IDs/secrets).
