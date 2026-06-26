# Implementation Guidance — Doc Writer

> How to apply this skill. See [SKILL.md](SKILL.md) and
> [/standards/documentation.md](../../../standards/documentation.md).

## Build order

1. **Identify** subject, audience, and purpose.
2. **Apply the required README structure** (title + one-sentence description, What it does,
   Quickstart, Inputs/outputs, Customization, Limitations, Changelog link).
3. **Write a runnable Quickstart** — the fastest path to first value.
4. **Verify accuracy** against current behavior; mark honest limitations.
5. **Cross-reference, don't duplicate**; check links + no leftover placeholders.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Tone/depth | Match the audience (end-user vs contributor) |
| Standards refs | Link to `standards/*`, never restate them |
| Extra sections | Add Troubleshooting/Resources for technical artifacts |

## Pitfalls

- ❌ Aspirational claims → ✅ document only verified behavior; wishes go to "Future improvements".
- ❌ Paragraph `description` → ✅ one action-oriented sentence.
- ❌ Stale examples → ✅ test the Quickstart end-to-end.

## Hand-off

Used by `build-feature`, `fix-bug`, and `onboarding-workflow`; pair with `doc-linter` (planned)
to verify completeness.
