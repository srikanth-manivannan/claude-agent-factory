# Resources — Enterprise API Delivery Pipeline

> Cross-references demonstrating the full hierarchy this pipeline orchestrates
> ([/standards/architecture.md](../../standards/architecture.md)):
> skill → agent → team / workflow → **playbook**.

## Teams (composed)
- [team-backend](../../teams/team-backend/) → agents: api-architect, backend-engineer, qa-engineer.
- [team-security](../../teams/team-security/) → agents: security-engineer, api-architect, qa-engineer.

## Workflows (sequenced)
- [build-feature](../../workflows/build-feature/), [database-migration](../../workflows/database-migration/),
  [review-pr](../../workflows/review-pr/), [security-audit](../../workflows/security-audit/),
  [release-pipeline](../../workflows/release-pipeline/).

## Skills (via agents, transitively)
backend/openapi-designer, database/schema-designer, architecture/system-design-reviewer,
architecture/tradeoff-analyzer, testing/unit-test-generator, security/secret-scanner,
documentation/doc-writer.

## Standards
Conforms to [/standards/](../../standards/); reviewed via the
[review-process](../../standards/review-process.md) + relevant checklists.
