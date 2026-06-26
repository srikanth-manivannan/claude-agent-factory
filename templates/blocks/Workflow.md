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

> **Tech profile** — Technology: {{TECHNOLOGY}} · Language: {{LANGUAGE}} ·
> Stack: {{STACK}} · Toolchain: {{TOOLCHAIN}} · Domain: {{DOMAIN}}

A multi-step orchestration of agents + skills, named for its **outcome**.

## Outcome

The state of the world after a successful run.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `agent:{{AGENT}}` / `skill:{{CATEGORY}}/{{SKILL}}` | {{VERSION}} | … |

> References point only *down* the ladder (ARCHITECTURE §17); never copy artifacts.

## Steps

1. **<step>** — what happens, which agent/skill runs, inputs → outputs.
2. **<step>** — …

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| {{INPUT}} | yes/no | … |

## Outputs

Artifacts, side effects, status produced.

## Failure handling

Retries, rollback, partial-completion behavior per step.

## Constraints & safety

- Preconditions and safety rules (`standards/security.md`).
