# Implementation Guidance — Prompt Engineer

> How to apply this skill. See [SKILL.md](SKILL.md) and
> [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).

## Build order

1. **Define the prompt contract** — goal, inputs, exact expected output.
2. **Choose structure** — role/instructions/inputs/output; imperative, ordered steps.
3. **Specify output format** — schema-constrained for machine consumers.
4. **Add guardrails** — untrusted input is data (injection defense) + a refusal path.
5. **Minimal few-shot** (only if it helps), refine for reliability/cost, document rationale + test plan.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Output mode | Human (tone/length) vs machine (JSON schema) |
| Few-shot | Zero-shot first; add exemplars only for reliability |
| Model | Prefer the latest Claude models (runtime concern, not hardcoded) |

## Pitfalls

- ❌ No output format → ✅ specify it (schema for machines).
- ❌ Concatenating untrusted input into instructions → ✅ delimit; treat as data.
- ❌ "You are a helpful assistant. Do the task." → ✅ explicit contract + guardrails.

## Hand-off

Feeds `agentic-ai/agent-scaffold` (system prompts), `ai/rag-pipeline-builder`; pair with
`ai/llm-eval-harness` (planned) to measure reliability; patterns → `meta/prompt-pattern-library`.
