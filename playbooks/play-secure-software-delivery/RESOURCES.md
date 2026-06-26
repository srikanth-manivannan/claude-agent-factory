# Resources — Secure Software Delivery Pipeline

> Cross-references for the hierarchy this pipeline orchestrates
> ([/standards/architecture.md](../../standards/architecture.md)).

## Team (composed)
- [team-security](../../teams/team-security/) → agents: security-engineer, api-architect, qa-engineer.

## Workflows (sequenced)
- [build-feature](../../workflows/build-feature/), [security-audit](../../workflows/security-audit/),
  [review-pr](../../workflows/review-pr/), [release-pipeline](../../workflows/release-pipeline/),
  [incident-response](../../workflows/incident-response/).

## Skills (via agents, transitively)
security/secret-scanner, architecture/system-design-reviewer, backend/openapi-designer,
testing/unit-test-generator, documentation/doc-writer.

## Standards
Conforms to [/standards/security.md](../../standards/security.md); gated via the
[security-review](../../standards/checklists/security-review.md) checklist.
