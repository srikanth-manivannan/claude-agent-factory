# Deployment Review Checklist

> Reviews safety of deploying a change. Run **after** the
> [Universal Core](_universal.md). Backs the `deploy-to-production` workflow.
> Legend: [README.md](README.md).

**Applies to:** any production deployment · **Min standard:** 0.1.0

## Safety nets
- [ ] 🔴 `[manual]` Rollback path is tested and ready.
- [ ] 🟠 `[auto]` The deployed build is the CI-verified artifact (no untested build).
- [ ] 🟠 `[manual]` DB migrations applied and reversible (→ `database-migration`).

## Configuration
- [ ] 🟠 `[manual]` Config/secrets correct for the target environment.
- [ ] 🟠 `[manual]` Health checks / readiness probes in place.

## Rollout strategy
- [ ] 🟡 `[manual]` Zero-downtime strategy used (or downtime window accepted).
- [ ] 🟡 `[manual]` Risky changes behind feature flags / gradual rollout.
- [ ] 🟡 `[manual]` Capacity/scaling validated for expected load.

## Observability & on-call
- [ ] 🟠 `[manual]` Logs/metrics/traces wired for the change.
- [ ] 🟡 `[manual]` Runbook / on-call prepared for the deployment.
