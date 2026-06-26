# Security Standard

> Secure-by-default rules for every artifact. Security is a default, not a feature
> (VISION §6.6). Enforced by the [security-review checklist](checklists/security-review.md).

**Min standard:** 0.1.0 · See also: [testing.md](testing.md), [review-process.md](review-process.md).

## Secure defaults

- **No secrets in the repo.** Ever. Use a vault/secrets manager; `.env` files stay
  gitignored.
- **Validate input at every trust boundary.** Never trust external input — guard
  against injection (SQL/command/path/**prompt**).
- **Least privilege.** Default to the minimum access/permissions that work.
- **Encrypt sensitive data** at rest and in transit.
- **Fail safe.** On error, deny; don't leak internals in error messages.
- **Dependencies.** Keep them current; no known CVEs; license-compatible
  ([contributing.md](contributing.md)).

## AI / agent specifics

- Defend prompts against injection; treat tool inputs/outputs as untrusted.
- Add guardrails and permission gates to agents (see the agentic-ai skills in
  [TAXONOMY](../TAXONOMY.md)).

## Dual-use disclosure

This project supports **authorized** security testing, defensive security, CTF, and
education. For any dual-use artifact:

- State the **authorized/defensive use case** explicitly.
- **Require authorization confirmation** where the artifact acts on a target.
- Refuse destructive/mass-targeting/detection-evasion-for-harm use.

## What this standard forbids

- Committing credentials, hardcoding secrets, disabling security checks "to ship."
- Skills that encourage unsafe patterns without disclosure.
