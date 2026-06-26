# Component Scaffold

> Use this to scaffold an accessible, tested UI component with markup, state, and tests.

**Category:** frontend · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Scaffolds a UI component that is **accessible and tested by construction** — semantic
markup, typed props, handling for loading/empty/error states, an interaction test
suite, and a usage example — in your project's existing framework. It bakes the
accessibility and testing standards in up front instead of bolting them on later.

It composes the **`testing/unit-test-generator`** primitive to produce the component's
tests — a deliberate cross-category dependency.

## Quickstart

```text
1. Copy skills/frontend/component-scaffold/ into your skills directory.
2. Invoke with the component + props (+ framework if not inferable).
3. Receive component code + tests + usage example + prop docs.
```

## How it works

Seven steps: define contract → detect framework → semantic accessible markup → state &
behavior → generate tests (via `unit-test-generator`) → usage example → document props.
Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `component`, optional `props`, optional `framework`.
- **Outputs:** component + tests + usage example + prop docs.

See [EXAMPLES.md](EXAMPLES.md).

## Dependencies

- **`testing/unit-test-generator`** (≥ 0.1.0) — generates the component's test suite.

## Customization

- **Framework** — override auto-detection.
- **Styling approach** — CSS modules / utility classes / CSS-in-JS per project.
- **Chain** into `accessibility/a11y-auditor` for a full WCAG audit.

## Limitations

- Produces a solid baseline; visual/design polish is out of scope.
- Bakes in a11y basics but doesn't replace a full audit (`a11y-auditor`).

## Related

See [RESOURCES.md](RESOURCES.md). Depends on `testing/unit-test-generator`; pairs with
`accessibility/a11y-auditor`; used by the `build-feature` / `build-ui-component` workflows.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Story/visual-test generation (`frontend/component-test-harness`).
- Design-token integration (`frontend/design-token-manager`).
- Variant matrix generation from the prop contract.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
