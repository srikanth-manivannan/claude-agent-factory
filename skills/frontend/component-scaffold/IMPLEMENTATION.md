# Implementation Guidance — Component Scaffold

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Define the component contract** — props/inputs, events/outputs, states (loading/empty/
   error), variants.
2. **Detect framework + conventions** (match the project; don't impose a new stack).
3. **Scaffold semantic, accessible markup** — keyboard-operable + labeled by construction.
4. **Implement state + behavior**; keep it focused and composable.
5. **Generate tests** (via `testing/unit-test-generator`): render, props, interaction, states.
6. **Add a usage example/story** + prop docs.

## Key decisions

| Decision | Guidance |
|----------|----------|
| A11y | Semantic-first + keyboard from the start; full audit via `a11y-auditor` |
| Styling | CSS modules / utility / CSS-in-JS per project |
| Scope | One focused component; split if it grows |

## Pitfalls

- ❌ `<div onclick>` "buttons" → ✅ real elements / roles + key handlers.
- ❌ Shipping without tests → ✅ the testing dependency exists for this.
- ❌ Missing loading/error states → ✅ declare them in the contract.

## Hand-off

Composes `testing/unit-test-generator`; pair with `accessibility/a11y-auditor`; used by
`build-feature`/`build-ui-component` workflows.
