# Examples — Component Scaffold

> Worked examples. Framework-agnostic; adapts to the project. See [SKILL.md](SKILL.md).

## Example 1 — SearchInput (happy path)

**Input:** `SearchInput` with props `value`, `onChange`, `loading`.

**Produces:**
- semantic `<label>` + `<input type="search">` + a clear button (keyboard operable);
- state handling for `loading` (spinner) and empty value;
- tests (via `unit-test-generator`): renders, types → `onChange` fires, clear resets,
  loading shows spinner (happy/edge), missing required prop handled (failure);
- a usage example showing default + loading variants;
- prop docs table.

## Example 2 — Edge: framework inference

**Input:** no `framework` given.

**Behavior:** detects the project's component framework and matches its file layout,
styling, and test conventions rather than imposing a new stack.

## Example 3 — Edge: accessibility baked in

**Input:** a custom `Toggle` component.

**Behavior:** scaffolds it with proper role/labeling and keyboard support by
construction; recommends a follow-up `accessibility/a11y-auditor` pass for full WCAG
verification (it does not claim full compliance from scaffolding alone).

## Anti-example

- ❌ A `<div onclick>` "button" with no keyboard support. Use a real button / proper
  role + key handlers.
- ❌ Shipping a component with no tests — the testing dependency exists for this reason.

## Try it yourself

- Add an `error` prop to Example 1 — note the error state + test appear.
- Request a second framework — observe conventions adapt.
