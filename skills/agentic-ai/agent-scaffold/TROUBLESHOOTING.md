# Troubleshooting — Agent Scaffold

> Symptom → cause → fix. See [SKILL.md](SKILL.md), [IMPLEMENTATION.md](IMPLEMENTATION.md),
> and [/standards/security.md](../../../standards/security.md).

## Quick diagnostics

- [ ] Does the agent have a single, bounded role?
- [ ] Is the loop bounded (max steps + stop condition)?
- [ ] Are irreversible actions behind human-in-the-loop gates?
- [ ] Is tool output treated as data (not instructions)?

## Common issues

### Symptom: Agent loops forever / burns tokens
- **Cause:** no step/cost budget or stop condition.
- **Fix:** set `max_steps`, `cost_budget`, and an explicit `stop_when` (IMPLEMENTATION).

### Symptom: Agent followed instructions hidden in tool output / user data
- **Cause:** untrusted content treated as instructions (prompt injection).
- **Fix:** delimit tool/user content; system prompt states it is data only; add an
  injection eval case.

### Symptom: Agent took an irreversible action unexpectedly
- **Cause:** missing HITL gate on a high-impact tool.
- **Fix:** add the tool to `approval_points`; default destructive actions to gated.

### Symptom: Agent is unreliable / hard to trust
- **Cause:** no evals; behavior unmeasured.
- **Fix:** encode `success_criteria` as eval cases (success + trajectory); run in CI.

### Symptom: Can't debug a bad run
- **Cause:** no tracing.
- **Fix:** emit step traces (decision + tool + result); see `agent-observability-tracer` *(planned)*.

### Symptom: Agent does too much / scope creep
- **Cause:** over-broad role + too many tools.
- **Fix:** split into focused agents; coordinate via `multi-agent-orchestrator` *(planned)*.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and the [security-review checklist](../../../standards/checklists/security-review.md).
- Open an issue with the agent contract + a problematic trace (redact secrets).
