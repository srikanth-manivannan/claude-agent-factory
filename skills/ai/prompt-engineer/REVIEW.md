# Review — Prompt Engineer

> Review guidance + recorded self-review, per [/standards/review-process.md](../../../standards/review-process.md).
> Run the [Universal Core](../../../standards/checklists/_universal.md) first.

## How to review this skill

- Applicable checklists: **Universal Core** + **security-review** (injection/refusal) +
  **documentation-review** + **testing-review**.

## Self-review result (v0.1.0)

**Reviewer:** Factory (Wave 0 self-review) · **Date:** 2026-06-26 · **Standard:** 0.1.0

**Verdict:** ✅ Approve — no open blocker/major.

- **Universal Core:** structure/naming, required files, no placeholders, metadata↔frontmatter,
  schema validation, versioning, no secrets — **pass**.
- **security-review:** injection-aware; refusal path; untrusted input treated as data — **pass**.
- **documentation-review / testing-review:** complete docs; happy/edge/safety/refusal cases — **pass**.

## Known minor follow-ups (🟡)
- Currently self-contained; a future `meta/prompt-pattern-library` should extract shared
  patterns (declared-pending cross-link).
- Model recommendation references the latest Claude models per the AI standard / `claude-api`.
