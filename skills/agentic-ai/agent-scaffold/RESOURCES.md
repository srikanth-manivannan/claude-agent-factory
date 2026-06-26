# Resources — Agent Scaffold

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md) · **Implementation:** [IMPLEMENTATION.md](IMPLEMENTATION.md).
- **Standards:** [prompt-engineering](../../../standards/prompt-engineering.md),
  [security](../../../standards/security.md),
  [architecture](../../../standards/architecture.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Runtime:** [/shared/runtime/claude/](../../../shared/runtime/claude/).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Depends on** | [`ai/prompt-engineer`](../../ai/prompt-engineer/) | authors the system prompt + guardrails |
| **Pairs with** | `ai/rag-pipeline-builder` *(planned)* | retrieval-backed agents |
| **Evaluated by** | `agentic-ai/agent-eval-harness` *(planned)* | runs the eval set |
| **Coordinated by** | `agentic-ai/multi-agent-orchestrator` *(planned)* | multi-agent teams |
| **Composed into** | `team-ai` (team) → `play-ship-ai-feature` (playbook) ([/WORKFLOWS.md §2](../../../WORKFLOWS.md)) | the AI delivery org |
| **Used by workflow** | `build-agent`, `secure-ai-feature` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | agent build step |

## Concepts & background (vendor-neutral)

- **Agent loop** (plan → act → observe → reflect); **bounded execution**.
- **Tool use** with typed contracts; **least privilege**.
- **Prompt injection** defense; **human-in-the-loop** gating; **agent evals** (success + trajectory).

## Provenance & credits

- Method synthesized from established agent-engineering practice (tool use, guardrails,
  evals). No third-party content copied; MIT (VISION §13).
