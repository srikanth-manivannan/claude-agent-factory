# Agent Scaffold

> Use this to scaffold a production-ready agent with a defined role, typed tools, memory, guardrails, and evals.

**Category:** agentic-ai · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Turns "we want an agent that does X" into a **deployable, safe agent definition** —
role contract, system prompt, typed tools, memory policy, guardrails with
human-in-the-loop gates, a bounded plan→act→observe→reflect loop, evals, and tracing.
It is the agentic flagship: the thing teams reach for to build agents *right* instead of
wiring an unbounded prompt+tools loop and hoping.

## Quickstart

```text
1. Copy skills/agentic-ai/agent-scaffold/ into your skills directory.
2. Invoke with: role, tools, (memory), (approval_points), (success_criteria).
3. Receive an agent definition + tool specs + guardrails + eval set.
```

## How it works

Eight steps: contract → system prompt (via `ai/prompt-engineer`) → typed tools →
memory → guardrails + HITL → bounded loop → evals → observability. Authoritative
procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `role`, `tools`, optional `memory`, `approval_points`, `success_criteria`.
- **Outputs:** agent contract + system prompt + typed tool specs + memory policy +
  guardrails/HITL + bounded loop + eval task set + trace instrumentation.

See [EXAMPLES.md](EXAMPLES.md) for enterprise scenarios. Detailed build steps in
[IMPLEMENTATION.md](IMPLEMENTATION.md).

## Dependencies

- **`ai/prompt-engineer`** (≥ 0.1.0) — authors the agent's system prompt with guardrails.

## Customization

- **Memory** — swap short-term for a vector store when the role needs recall.
- **Guardrails** — tighten tool scopes, cost/step budgets, and approval points to policy.
- **Compose** — drop the agent into a `team` or `workflow`; add `multi-agent-orchestrator`
  for coordination.

## Limitations

- Defines a **single-purpose** agent; multi-agent coordination is a separate skill.
- Eval execution depends on `agentic-ai/agent-eval-harness` *(planned)*.
- Tool *implementations* are yours; this defines their contracts and safety.

## Related

See [RESOURCES.md](RESOURCES.md). Depends on `ai/prompt-engineer`; composes into
`team-ai` and the `play-ship-ai-feature` playbook; pairs with `ai/rag-pipeline-builder`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
- **Implementation guidance:** [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Future improvements

- Native `agent-eval-harness` integration (run, don't just define, evals).
- Tool auto-generation from an OpenAPI spec (`backend/openapi-designer`).
- Memory adapters (vector/SQL) as pluggable resources.
- Cost-governor integration (`agentic-ai/agent-cost-controller`).

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
