---
name: {{NAME}}
description: {{DESCRIPTION}}
version: {{VERSION}}
runtime: {{RUNTIME}}
min_standard: {{MIN_STANDARD}}
license: MIT
tags: {{TAGS}}
---

# {{TITLE}} (Workflow)

> {{DESCRIPTION}}

A multi-step orchestration composed of agents + skills (ARCHITECTURE §6).
Named for its **outcome** (VISION §11.2).

## Outcome

What state of the world exists after this workflow completes successfully.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `agent:{{AGENT}}` / `skill:{{CATEGORY}}/{{SKILL}}` | {{VERSION}} | … |
| 2 | … | … | … |

> Workflows **reference** agents/skills by name + min version; composition only
> points *down* the ladder (ARCHITECTURE §17).

## Steps

1. **<step name>** — what happens, which agent/skill runs, inputs → outputs.
2. **<step name>** — …
3. **<step name>** — …

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| {{INPUT}} | yes/no | … |

## Outputs

What the workflow produces (artifacts, side effects, status).

## Failure handling

What happens if a step fails: retries, rollback, partial-completion behavior.

## Constraints & safety

- Preconditions and safety rules (`standards/security.md`).
