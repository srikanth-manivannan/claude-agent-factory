# Secret Scanner

> Use this to detect committed secrets and credentials and produce a safe remediation plan.

**Category:** security · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Scans a codebase (and optionally its history) for committed secrets — API keys,
tokens, private keys, connection strings — triages findings to cut false positives,
and returns a **safe, ordered remediation plan** (rotate → remove → purge → prevent).
It never prints live secret values: evidence is always redacted.

**Defensive, authorized use only** ([security standard](../../../standards/security.md)).

## Quickstart

```text
1. Copy skills/security/secret-scanner/ into your skills directory.
2. Invoke with the target path + authorization confirmation.
3. Receive a severity-ranked, redacted findings report with remediation steps.
```

## How it works

Seven steps: confirm authorization → scan tree/history → triage → redact → remediate
(rotate-first) → recommend prevention → report. Authoritative procedure in
[SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `target`, `authorization` (required), optional `scan_history`.
- **Outputs:** severity-ranked findings (redacted) + ordered remediation + prevention plan.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **History depth** — full history vs. working tree only.
- **Pattern set** — extend with org-specific token formats.
- **Chain** into `security/secrets-management-setup` for prevention.

## Limitations

- Pattern/entropy detection can miss novel secret formats and yields some false positives.
- It recommends remediation; it does not rotate credentials for you.

## Related

See [RESOURCES.md](RESOURCES.md). Part of the `security-audit` workflow; complements
`security/dependency-vuln-auditor` and `security/secrets-management-setup`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Verified-secret checks (probe whether a key is live) — gated, opt-in, authorized.
- Allowlist/baseline support to suppress known false positives.
- Auto-generated pre-commit + CI scanning config.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
