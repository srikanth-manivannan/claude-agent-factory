# Accessibility Audit (Workflow)

> Audit a UI against WCAG and remediate accessibility issues, then verify.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Finds WCAG violations in a UI, fixes them (ARIA, contrast, keyboard nav), and
re-verifies — targeting WCAG AA by default.

## The flow

`audit → categorize → remediate → verify`. See [WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:accessibility/a11y-auditor` (≥ 0.1.0)
- `skill:accessibility/aria-annotator` (≥ 0.1.0)
- `skill:accessibility/color-contrast-fixer` (≥ 0.1.0)
- `skill:accessibility/keyboard-nav-checker` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** target UI, optional WCAG level.
- **Outputs:** remediated UI + before/after report.

## Customization

Pair with `build-ui-component` to bake a11y in from the start.

## Limitations

- Automated checks can't catch everything; add `screen-reader-tester` for depth.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
