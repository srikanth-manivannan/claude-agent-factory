# Security Policy

The Claude Agent Factory takes security seriously — for the framework itself and for
the artifacts it produces (see [standards/security.md](standards/security.md)).

## Supported versions

| Version | Supported |
|---------|-----------|
| Framework 0.1.x | ✅ |
| < 0.1.0 | ❌ |

## Reporting a vulnerability

**Do not open a public issue for security vulnerabilities.**

Please report privately via either:

1. **GitHub private vulnerability reporting** — the
   [Security tab](https://github.com/srikanth-manivannan/claude-agent-factory/security/advisories/new)
   → "Report a vulnerability" (preferred), **or**
2. **Email** — [srikanth.gmb@gmail.com](mailto:srikanth.gmb@gmail.com) with subject
   `SECURITY: <short description>`.

Please include: affected artifact/file, a description, reproduction steps, and impact.
We aim to acknowledge within **5 business days** and to provide a remediation timeline
after triage. Please allow reasonable time to fix before public disclosure
(coordinated disclosure).

## Scope

In scope: the framework tooling (`scripts/`, `generators/`), schemas, and any skill
that handles input, credentials, or executes logic. Out of scope: vulnerabilities in
your own forks/derivatives, and third-party dependencies you add downstream.

## Security expectations for contributed skills

Every contributed artifact must satisfy [standards/security.md](standards/security.md)
and pass the [security-review checklist](standards/checklists/security-review.md):

- **No committed secrets** (enforced by `secret-scanner` + the validation gate).
- **Input validated at trust boundaries**; injection-aware (incl. prompt injection).
- **Least privilege**; secrets via a manager, never in code.
- **Dual-use disclosure** — security tooling is for **authorized, defensive** use only;
  it must state its authorized use case and refuse destructive/mass-harm requests.

Thank you for helping keep the ecosystem safe.
