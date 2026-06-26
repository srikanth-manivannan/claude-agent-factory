# Resources — Prompt Engineer

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [prompt-engineering](../../../standards/prompt-engineering.md),
  [security](../../../standards/security.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Reusable block:** [/templates/blocks/Prompt.md](../../../templates/blocks/Prompt.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Feeds** | `agentic-ai/agent-scaffold` *(planned)* | agent system prompts |
| **Feeds** | `ai/rag-pipeline-builder` *(planned)* | answer-generation prompts |
| **Pairs with** | `ai/llm-eval-harness` *(planned)* | measures prompt reliability |
| **Future extraction** | `meta/prompt-pattern-library` *(planned)* | shared prompt patterns |
| **Used by workflow** | `build-rag-system`, `secure-ai-feature` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | prompt step |

## Concepts & background (vendor-neutral)

- **Prompt contract**; **structured output**; **few-shot** vs zero-shot.
- **Prompt injection** defense; **refusal paths**.
- Model choice: prefer the **latest Claude models** (see `claude-api` reference / AI standard).

## Provenance & credits

- Method synthesized from established prompt-engineering practice. No third-party
  content copied; MIT (VISION §13).
