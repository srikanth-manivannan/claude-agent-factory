# Troubleshooting — Migration Planner

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Quick diagnostics

- [ ] Is the target state actually decided?
- [ ] Does every phase have a stated, testable rollback?
- [ ] Are phases independently shippable AND reversible?
- [ ] Do data phases specify integrity verification?

## Common issues

### Symptom: The planner refuses and points to tradeoff-analyzer
- **Cause:** the target isn't decided (step 1).
- **Fix:** decide the target (use `architecture/tradeoff-analyzer`), then re-run.
  This is correct behavior.

### Symptom: A phase has no rollback
- **Cause:** rollback step skipped.
- **Fix:** add a rollback trigger + steps; if a phase truly can't be reversed, split it
  or add a backup/restore as the rollback. No rollback → phase not ready (step 6).

### Symptom: Plan is one giant phase
- **Cause:** scope not decomposed.
- **Fix:** break along seams identified in step 2; each phase independently shippable.

### Symptom: Risky work scheduled last
- **Cause:** sequencing not risk-driven.
- **Fix:** re-order to de-risk early (step 7) so surprises surface while cheap to fix.

### Symptom: Data migration risks loss
- **Cause:** no integrity verification / no expand-contract.
- **Fix:** use dual-write → backfill → verify → cut-read; specify the integrity checks;
  hand mechanics to the `database-migration` workflow.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the
  [deployment-review checklist](../../../standards/checklists/deployment-review.md).
- Open an issue with source, target, constraints, and the produced plan.
