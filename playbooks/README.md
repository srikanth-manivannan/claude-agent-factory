# Playbooks — Reference Engineering Pipelines

> The top tier of the hierarchy: operating guides that compose **teams + workflows** for
> a complete engineering outcome ([/standards/architecture.md](../standards/architecture.md)).
> These **reference pipelines** prove the framework enables coordinated, end-to-end
> engineering — not just a collection of isolated skills. Validate against
> [playbook.schema.yaml](../shared/schemas/playbook.schema.yaml).

| Pipeline (playbook) | Outcome | Team(s) | Workflows |
|---------------------|---------|---------|-----------|
| [play-enterprise-api-delivery](play-enterprise-api-delivery/) | API: design → secure, tested production | team-backend, team-security | build-feature, database-migration, review-pr, security-audit, release-pipeline |
| [play-react-enterprise-dev](play-react-enterprise-dev/) | Accessible, performant frontend to prod | team-frontend | build-feature, accessibility-audit, performance-optimization, review-pr, release-pipeline |
| [play-aws-serverless-delivery](play-aws-serverless-delivery/) | Serverless workload to cloud + ops | team-platform | build-feature, database-migration, release-pipeline, incident-response |
| [play-secure-software-delivery](play-secure-software-delivery/) | Security-gated SDLC | team-security | build-feature, security-audit, review-pr, release-pipeline, incident-response |
| [play-accessibility-compliance](play-accessibility-compliance/) | Reach + sustain WCAG AA | team-frontend | accessibility-audit, review-pr, release-pipeline |

## How a pipeline proves the framework

Each pipeline exercises the **full hierarchy**:

```
playbook → team → agent → skill        (the "who")
playbook → workflow → skill            (the "how")
```

Every reference here resolves to a real artifact — `scripts/check-links` confirms the
chains are intact. Authoring: [Playbook Author Guide](../docs/guides/playbook-author-guide.md).
