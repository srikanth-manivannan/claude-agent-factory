# Documentation Review Checklist

> Reviews documentation completeness and clarity. Run **after** the
> [Universal Core](_universal.md). Backs the `documentation-review` workflow.
> "Undocumented = doesn't exist" (VISION §6.4). Legend: [README.md](README.md).

**Applies to:** every artifact · **Min standard:** 0.1.0

## Completeness
- [ ] 🔴 `[auto]` `README.md` present and complete per `standards/documentation.md`.
- [ ] 🟠 `[manual]` `description` is one action-oriented sentence.
- [ ] 🟠 `[manual]` Inputs and outputs are documented.
- [ ] 🟡 `[manual]` Quickstart is present and actually runnable.
- [ ] 🟡 `[manual]` Examples present (inline or linked to `examples/`).
- [ ] 🟡 `[manual]` Limitations stated honestly.

## Accuracy & freshness
- [ ] 🟠 `[auto]` `CHANGELOG.md` updated for this version.
- [ ] 🟡 `[manual]` Docs match current behavior (no stale claims).
- [ ] 🟡 `[manual]` Troubleshooting / Resources present where relevant.

## Hygiene
- [ ] 🔴 `[auto]` No leftover `{{placeholders}}`.
- [ ] 🟡 `[auto]` Internal links resolve (no dead links).
