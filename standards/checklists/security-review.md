# Security Review Checklist

> Reviews application security posture. Run **after** the
> [Universal Core](_universal.md). Backs the `security-audit` workflow. Defensive /
> authorized use only (VISION §6.6). Legend: [README.md](README.md).

**Applies to:** any artifact handling input, auth, data, or dependencies · **Min standard:** 0.1.0

## Secrets & dependencies
- [ ] 🔴 `[auto]` No secrets/keys/credentials committed.
- [ ] 🟠 `[auto]` Dependencies free of known CVEs; licenses compatible.
- [ ] 🟠 `[manual]` Secrets sourced from a vault/manager, not code or committed env.

## Authentication & authorization
- [ ] 🔴 `[manual]` AuthN enforced on all protected entrypoints.
- [ ] 🔴 `[manual]` AuthZ enforced with least privilege (no broken access control).

## Input & output
- [ ] 🔴 `[manual]` Input validated/sanitized at every trust boundary.
- [ ] 🔴 `[manual]` No injection vectors (SQL/command/path/prompt injection).
- [ ] 🟡 `[manual]` Error messages don't leak internals/stack traces.

## Data protection
- [ ] 🟠 `[manual]` Sensitive data encrypted at rest and in transit.
- [ ] 🟠 `[auto]` Security headers / TLS configured correctly.

## Risk
- [ ] 🟠 `[manual]` Threat model performed for new high-risk flows (STRIDE).
- [ ] 🟡 `[manual]` Dual-use behavior disclosed; authorization confirmed.
