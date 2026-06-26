---
name: security-audit
description: Run a full security pass over a service - threats, dependencies, secrets, and config.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [security, audit, appsec]
---

# Security Audit (Workflow)

> Run a full security pass over a service — threats, dependencies, secrets, and config.

## Outcome

A prioritized security report: threat model, dependency vulnerabilities, exposed
secrets, and misconfigurations, each with a remediation path.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 2 | `skill:security/threat-modeler` | 0.1.0 | STRIDE threat model |
| 3 | `skill:security/dependency-vuln-auditor` | 0.1.0 | CVE findings |
| 4 | `skill:security/secret-scanner` | 0.1.0 | exposed-secret findings |
| 5 | `skill:security/security-headers-configurer` | 0.1.0 | config findings |

## Steps

1. **Scope** — define the system boundary and assets in scope.
2. **Threat model** — run STRIDE over the design; identify high-risk flows.
3. **Audit dependencies** — scan for known CVEs + license risk.
4. **Scan for secrets** — detect committed/exposed credentials.
5. **Review configuration** — headers, TLS, default permissions.
6. **Report** — prioritize findings by severity with remediation steps.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target | yes | Service/repo in scope |
| authorization | yes | Confirmation this audit is authorized |

## Outputs

A severity-ranked security report with remediation guidance.

## Failure handling

- No authorization → refuse (VISION §6.6; only authorized security work).
- Critical finding (🔴) → surface immediately, don't wait for the full report.

## Constraints & safety

- Defensive/authorized use only. Dual-use findings disclosed responsibly.
