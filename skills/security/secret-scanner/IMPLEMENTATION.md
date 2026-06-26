# Implementation Guidance — Secret Scanner

> How to apply this skill. Defensive/authorized use only. See [SKILL.md](SKILL.md) and
> [/standards/security.md](../../../standards/security.md).

## Build order

1. **Confirm authorization** — refuse if not authorized.
2. **Scan** working tree + (optionally) history for high-signal patterns + high entropy.
3. **Triage** findings: confirmed / likely / false-positive; assign severity.
4. **Redact** — never emit full secret values (prefix + length only).
5. **Recommend remediation** (rotate → remove → purge history → prevent) + prevention.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Remediation order | **Rotate first** — an exposed secret is already compromised |
| False positives | Separate from confirmed; recommend an allowlist/baseline |
| History | Scan it by default; purging requires rewrite |

## Pitfalls

- ❌ Printing the secret value → ✅ always redact.
- ❌ "Just delete the file" → ✅ rotate the credential first.
- ❌ Scanning without authorization → ✅ refuse.

## Hand-off

Part of the `security-audit`, `dependency-audit`, and `rotate-secrets` workflows; pair
with `secrets-management-setup` (planned) for prevention.
