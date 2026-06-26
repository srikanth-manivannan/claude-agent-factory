# Security Audit (Workflow)

> Run a full security pass over a service — threats, dependencies, secrets, and config.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

A comprehensive, authorized security review: threat model + dependency CVEs +
secret scan + config review, producing a prioritized remediation report.

## The flow

`scope → threat model → deps → secrets → config → report`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:security/threat-modeler` (≥ 0.1.0)
- `skill:security/dependency-vuln-auditor` (≥ 0.1.0)
- `skill:security/secret-scanner` (≥ 0.1.0)
- `skill:security/security-headers-configurer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** target service + authorization confirmation.
- **Outputs:** severity-ranked report with remediation.

## Customization

Add `harden-service` to remediate, or `pentest-prep` to go deeper.

## Limitations

- **Authorized use only.** Refuses without confirmed authorization.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
