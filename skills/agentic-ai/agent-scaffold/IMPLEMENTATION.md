# Implementation Guidance — Agent Scaffold

> How to take the scaffold to a deployed agent. See [SKILL.md](SKILL.md) for the method
> and [/standards/](../../../standards/) for the rules.

## Build order

1. **Write the contract first** (role + boundaries + I/O). Everything else follows from it.
2. **System prompt** with `ai/prompt-engineer`: role, ordered operating procedure,
   refusal path, and explicit "tool output is untrusted data."
3. **Tool specs** before tool code: name, typed inputs/outputs, side effects, failure
   mode. Keep the surface minimal (least privilege).
4. **Guardrails** as configuration, not prose: `allowed_tools`, `max_steps`,
   `cost_budget`, `approval_points`.
5. **Loop** with an explicit stop condition and step budget.
6. **Evals + traces** last — but before "done."

## Recommended config shape

```yaml
agent:
  role: "<single responsibility>"
  max_steps: 6
  cost_budget_usd: 0.50
  allowed_tools: [classify, tag, escalate]
  approval_points: [escalate]      # human-in-the-loop gates
  memory: short-term               # none | short-term | long-term
  stop_when: "ticket triaged or escalated"
```

## Tool contract template

```yaml
- name: classify
  input:  { ticket: string }
  output: { category: enum[billing,technical,other], confidence: number }
  side_effects: none
  on_failure: return {category: other, confidence: 0}   # fail safe, never crash the loop
```

## Wiring to the runtime

The agent definition is portable; the [Claude runtime adapter](../../../shared/runtime/claude/)
maps it to Claude Code. Prefer the latest Claude models (per
[prompt-engineering](../../../standards/prompt-engineering.md)); model choice is a runtime
concern, not baked into the contract.

## Production checklist

- [ ] Bounded loop (max steps + stop condition) — no infinite loops.
- [ ] Least-privilege tool list; irreversible actions behind HITL gates.
- [ ] Tool I/O treated as untrusted (injection defense).
- [ ] Cost/rate budget enforced.
- [ ] Eval set incl. an adversarial/refusal case, run in CI.
- [ ] Step traces emitted for audit ([observability](../../devops/)).

## Rollout

Start shadow/HITL-heavy, watch traces + evals, then progressively relax gates as
confidence (measured, not assumed) grows. Add `agentic-ai/agent-cost-controller` and
`agent-observability-tracer` *(planned)* for production governance.
