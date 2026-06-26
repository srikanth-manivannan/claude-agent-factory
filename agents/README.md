# Agents

> AI specialists that apply one or more skills (tier 2 of the hierarchy,
> [/standards/architecture.md](../standards/architecture.md)). Agents are composed into
> [teams](../teams/) and orchestrated by [playbooks](../playbooks/). Conform to
> [/standards/](../standards/); validate against
> [agent.schema.yaml](../shared/schemas/agent.schema.yaml).

| Agent | Role | Skills used | Staffs |
|-------|------|-------------|--------|
| [api-architect](api-architect/) | API + system design | system-design-reviewer, openapi-designer, tradeoff-analyzer | team-backend, team-security |
| [backend-engineer](backend-engineer/) | Server-side build | openapi-designer, schema-designer, unit-test-generator | team-backend |
| [frontend-engineer](frontend-engineer/) | Accessible UI build | component-scaffold, a11y-auditor, unit-test-generator | team-frontend |
| [security-engineer](security-engineer/) | Security posture | secret-scanner, system-design-reviewer | team-security, team-platform |
| [platform-engineer](platform-engineer/) | Infra + CI/CD + scaffolding | cloud-resource-provisioner, ci-pipeline-generator, project-scaffolder | team-platform |
| [qa-engineer](qa-engineer/) | Quality gate | unit-test-generator, a11y-auditor, doc-writer | all teams |

> Authoring: [Agent Author Guide](../docs/guides/agent-author-guide.md). Skill anatomy
> reference: [/skills/architecture/README.md](../skills/architecture/README.md).
