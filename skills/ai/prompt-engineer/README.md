# Prompt Engineer

> Use this to design or refine a production prompt with an explicit contract, structure, and rationale.

**Category:** ai · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Designs production prompts the way the [prompt-engineering standard](../../../standards/prompt-engineering.md)
prescribes: an explicit contract (goal, inputs, exact output), a clear structure,
specified output format, injection guardrails, a refusal path, and a documented
rationale plus a test plan. It refines unreliable prompts and hardens output format
and safety — not "prompt tricks," but a repeatable engineering method.

## Quickstart

```text
1. Copy skills/ai/prompt-engineer/ into your skills directory.
2. Invoke with the task (+ output_consumer: human|machine, constraints).
3. Receive a production prompt with contract, guardrails, rationale, and a test plan.
```

## How it works

Seven steps: define contract → choose structure → specify output format → add
guardrails → minimal few-shot → refine for reliability/cost → document rationale +
test plan. Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `task`, optional `output_consumer`, `constraints`, `existing_prompt`.
- **Outputs:** a production prompt + rationale + suggested eval/test plan.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Output mode** — human-readable vs. schema-constrained machine output.
- **Few-shot depth** — zero-shot vs. minimal exemplars.
- **Pair** with `ai/llm-eval-harness` to measure prompt reliability.

## Limitations

- It designs the prompt; measuring real-world reliability needs an eval harness.
- Model-specific tuning may still be required; it recommends the latest Claude model
  but doesn't benchmark models.

## Related

See [RESOURCES.md](RESOURCES.md). Feeds `agentic-ai/agent-scaffold` and `ai/rag-pipeline-builder`;
pairs with `ai/llm-eval-harness`; a future `meta/prompt-pattern-library` will extract
reusable patterns from skills like this one.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Extract a shared `meta/prompt-pattern-library` (this skill is self-contained today).
- Automatic structured-output schema generation from the contract.
- Injection-robustness self-test generation.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
