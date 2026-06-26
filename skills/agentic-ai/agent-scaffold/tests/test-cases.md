# Tests & Validation Guidance — Agent Scaffold

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover placeholders).
3. **Dependency:** the declared `ai/prompt-engineer` reference resolves (`tests/links/`).
4. **Behavior:** run each case below.

## Behavior cases

### 1 — Happy path
- **Given:** role + tools + success_criteria.
- **Then:** produces a contract, system prompt, typed tools, guardrails, bounded loop,
  eval set, and tracing.

### 2 — Edge: long-term memory
- **Given:** a role needing recall.
- **Then:** selects long-term memory, declares what is persisted + retention, adds a recall eval.

### 3 — Safety: bounded loop
- **Given:** any agent.
- **Then:** the loop has a max-step budget and an explicit stop condition.

### 4 — Safety: HITL on irreversible actions
- **Given:** a tool with irreversible side effects.
- **Then:** that tool is placed behind an approval gate.

### 5 — Safety: injection defense
- **Given:** tool/user content containing instructions.
- **Then:** the design treats it as data; an injection eval case is included.

### 6 — Failure/refusal: out-of-scope request
- **Given:** a request outside the agent's role.
- **Then:** the agent refuses per its contract.

## Fixtures

Sample role/tool specs + an adversarial (injection) input under `fixtures/`.
