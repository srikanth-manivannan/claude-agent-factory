# Teams

> Coordinated collections of agents (tier 3 of the hierarchy,
> [/standards/architecture.md](../standards/architecture.md)). Teams are composed by
> [playbooks](../playbooks/). Conform to [/standards/](../standards/); validate against
> [team.schema.yaml](../shared/schemas/team.schema.yaml).

| Team | Domain | Agents | Composed by playbook |
|------|--------|--------|----------------------|
| [team-backend](team-backend/) | Backend delivery | api-architect, backend-engineer, qa-engineer | play-enterprise-api-delivery |
| [team-frontend](team-frontend/) | Frontend delivery | frontend-engineer, qa-engineer | play-react-enterprise-dev, play-accessibility-compliance |
| [team-platform](team-platform/) | Platform / infra | platform-engineer, security-engineer, qa-engineer | play-aws-serverless-delivery |
| [team-security](team-security/) | Security lifecycle | security-engineer, api-architect, qa-engineer | play-secure-software-delivery |

> `qa-engineer` staffs every team as the shared quality role. Authoring:
> [Agent Author Guide](../docs/guides/agent-author-guide.md) (teams compose agents).
