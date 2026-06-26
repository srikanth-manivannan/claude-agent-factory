# Showcase Projects

> End-to-end demonstrations of the framework solving **real engineering scenarios** by
> composing skills, agents, teams, workflows, and playbooks. Showcases are
> **demonstrations, not catalog artifacts** (ARCHITECTURE §12) — they show *how to use*
> the collection, and link to real artifacts rather than duplicating them.

| Showcase | Scenario | Anchored on |
|----------|----------|-------------|
| [enterprise-react-application](enterprise-react-application/) | Build + ship an accessible enterprise React app | `play-react-enterprise-dev` |
| [laravel-rest-api](laravel-rest-api/) | Deliver a secure Laravel REST API to production | `play-enterprise-api-delivery` + `play-secure-software-delivery` |
| [aws-serverless-platform](aws-serverless-platform/) | Stand up + operate an AWS serverless platform | `play-aws-serverless-delivery` |

## How to read a showcase

Each showcase walks a realistic project through the framework, naming the exact
**playbook → teams → agents → skills** and **workflows** used at each stage. Every artifact
it references **exists and resolves** (`scripts/validate` confirms the graph). These are
the "see it work" companions to the [guides](../../docs/guides/).

> Showcases use technology names (React, Laravel, AWS) only as concrete *examples* — the
> underlying skills are technology-agnostic (the tech profile carries specifics).
