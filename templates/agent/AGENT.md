---
name: {{NAME}}
description: {{DESCRIPTION}}
version: {{VERSION}}
runtime: {{RUNTIME}}
min_standard: {{MIN_STANDARD}}
license: MIT
tags: {{TAGS}}
---

# {{TITLE}} (Agent)

> {{DESCRIPTION}}

A reusable **role** in the composition ladder (skills → agents → workflows → teams,
ARCHITECTURE §5). An agent wields skills to fulfill a responsibility.

## Role & responsibilities

- This agent is responsible for …
- It is NOT responsible for … (boundary — hand off to which agent/workflow)

## Skills used

| Skill | Min version | Why this agent needs it |
|-------|-------------|-------------------------|
| `{{CATEGORY}}/{{SKILL}}` | {{VERSION}} | … |

> Agents **reference** skills by name + min version; they never copy them
> (single source of truth, ARCHITECTURE §6).

## Operating instructions

How the agent behaves: its decision procedure, when it invokes each skill, and
how it sequences work.

1. …
2. …

## Inputs / outputs

- **Inputs:** what the agent expects to receive.
- **Outputs:** what it produces / hands off.

## Constraints & safety

- Limits, preconditions, and safety rules (`standards/security.md`).

## Handoffs

Which workflows/teams typically use this agent, and what it expects from / returns
to them.
