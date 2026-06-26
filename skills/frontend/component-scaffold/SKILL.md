---
name: component-scaffold
description: Use this to scaffold an accessible, tested UI component with markup, state, and tests.
version: 0.1.0
category: frontend
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [frontend, component, ui, scaffold, accessibility]
---

# Component Scaffold

> Use this to scaffold an accessible, tested UI component with markup, state, and tests.

> **Tech profile** — Technology: UI component · Language: any · Stack: any component framework · Toolchain: any · Domain: frontend
> *(Framework-agnostic method; adapts to the project's component framework.)*

## When to use this skill

- Creating a new UI component (input, card, modal, etc.).
- Standardizing component structure (markup + state + tests + a11y) across a UI.
- Starting the UI portion of the `build-feature` workflow.

## When NOT to use this skill

- Auditing accessibility of existing UI — use `accessibility/a11y-auditor`.
- App-wide state architecture — use `frontend/state-management-advisor`.
- Page layout — use `frontend/responsive-layout-helper`.

## Prerequisites

- The component's purpose, its props/inputs, and the project's framework.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `component` | yes | What the component is + its behavior |
| `props` | no | Inputs/props and their types |
| `framework` | no | Component framework; inferred from project if omitted |

## Instructions

1. **Define the component contract.** Props/inputs, events/outputs, states (loading,
   empty, error), and visual variants.
2. **Detect framework + conventions.** Match the project's component patterns, file
   layout, and styling approach; don't introduce a new framework.
3. **Scaffold semantic, accessible markup.** Use native semantic elements; ensure
   keyboard operability and labels by construction
   ([/standards/accessibility.md](../../../standards/accessibility.md)). Defer a full
   audit to `accessibility/a11y-auditor`.
4. **Implement state + behavior** per the contract; keep the component focused and
   composable.
5. **Generate tests.** Use `testing/unit-test-generator` to cover render, props,
   interaction, and the empty/error states (happy/edge/failure).
6. **Add a usage example/story** demonstrating the variants.
7. **Document** props and usage in a short component README/section.

## Output

A component in the project's framework: semantic accessible markup, typed props, state
handling for key states, an interaction/render test suite (via the testing primitive),
a usage example, and prop documentation.

## Constraints & safety

- **Accessible by construction** — keyboard + semantics from the start (AA baseline).
- **Tested** — no component without render + interaction tests.
- **Framework-consistent** — match existing conventions, don't impose new ones.

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** a `SearchInput` component with `value`, `onChange`, and a loading state.
**Produces:** semantic labeled input + clear button, state handling, tests for typing /
clearing / loading, and a usage example.
