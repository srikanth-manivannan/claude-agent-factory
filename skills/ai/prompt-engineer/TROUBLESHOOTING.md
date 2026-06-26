# Troubleshooting — Prompt Engineer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and
> [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).

## Quick diagnostics

- [ ] Does the prompt state an explicit contract (goal/inputs/output)?
- [ ] Is the output format specified (schema for machine consumers)?
- [ ] Are there injection guardrails + a refusal path?
- [ ] Is untrusted input clearly separated from instructions?

## Common issues

### Symptom: Inconsistent / unparseable output
- **Cause:** output format not specified.
- **Fix:** require a structured format (e.g. JSON to a schema); add one example.

### Symptom: Prompt follows injected instructions
- **Cause:** untrusted input concatenated into the instruction block.
- **Fix:** delimit untrusted content; instruct the model to treat it as data only; add
  an injection test case.

### Symptom: Verbose, drifting answers
- **Cause:** ambiguous, over-long instructions.
- **Fix:** tighten to imperative steps; remove redundancy; set length constraints.

### Symptom: Works in testing, fails in production
- **Cause:** no evaluation across real inputs.
- **Fix:** build an eval suite with `ai/llm-eval-harness`; iterate on failures.

### Symptom: Hardcoded to one stack/model
- **Cause:** specifics baked into the prompt body.
- **Fix:** pass them as variables; keep the body portable (recommend latest Claude model).

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the prompt-engineering + security standards.
- Open an issue with the task + prompt + failing outputs.
