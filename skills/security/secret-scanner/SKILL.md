---
name: secret-scanner
description: Use this to detect committed secrets and credentials and produce a safe remediation plan.
version: 0.1.0
category: security
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [security, secrets, credentials, scanning, remediation]
---

# Secret Scanner

> Use this to detect committed secrets and credentials and produce a safe remediation plan.

> **Tech profile** — Technology: any · Language: any · Stack: any VCS · Toolchain: any · Domain: security
> *(Scans any codebase/history; defensive, authorized use only.)*

## When to use this skill

- Auditing a repo (and its history) for committed secrets before going public.
- As a pre-release gate or part of the `security-audit` workflow.
- After a suspected leak, to find and scope exposed credentials.

## When NOT to use this skill

- Dependency CVEs — use `security/dependency-vuln-auditor`.
- Designing secrets storage — use `security/secrets-management-setup`.

## Prerequisites

- Read access to the codebase (and history, if in scope).
- **Authorization** to scan the target (defensive use only).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `target` | yes | Repo/path to scan |
| `scan_history` | no | Whether to scan VCS history (default: yes) |
| `authorization` | yes | Confirmation the scan is authorized |

## Instructions

1. **Confirm authorization.** If not confirmed, refuse
   ([/standards/security.md](../../../standards/security.md)).
2. **Scan working tree + (optionally) history** for high-signal patterns: API keys,
   tokens, private keys, connection strings, cloud credentials, high-entropy strings.
3. **Triage findings.** Classify each as confirmed / likely / false-positive; assign
   severity. Reduce noise — a wall of false positives helps no one.
4. **Do NOT print full secret values.** Redact (show a prefix + length); never echo a
   live credential into logs/output.
5. **Recommend remediation per finding:** rotate/revoke the credential first (it is
   already exposed), then remove from code, then purge from history if needed, then add
   to ignore + move to a secrets manager.
6. **Recommend prevention:** pre-commit hooks, CI secret scanning, a secrets manager
   (`security/secrets-management-setup`).
7. **Report** severity-ranked findings with redacted evidence and remediation steps.

## Output

A severity-ranked report: each finding with location, redacted evidence,
confirmed/likely classification, and ordered remediation (rotate → remove → purge →
prevent). No live secret values are exposed.

## Constraints & safety

- **Authorized/defensive use only**; refuse otherwise (VISION §6.6).
- **Never reveal full secret values** — always redact.
- **Rotate before remove:** an exposed secret is compromised; deletion alone is insufficient.

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** a repo with an AWS key in an old commit.
**Produces:** a finding (redacted `AKIA…`, file+commit), severity high, remediation =
revoke the key → remove → purge history → enable CI scanning.
