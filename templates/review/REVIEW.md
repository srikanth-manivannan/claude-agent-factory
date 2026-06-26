# Review — {{TITLE}}

> A structured review/critique of an artifact or change. Use for contribution
> review, audits, or self-review before opening a PR. Findings are specific and
> actionable; verdicts are evidence-based (VISION §6: quality is earned).

**Subject:** {{SUBJECT}} (artifact / PR / version)
**Reviewer:** {{AUTHOR}} · **Date:** {{DATE}} · **Standard version:** {{MIN_STANDARD}}

## Summary

One paragraph: what was reviewed and the overall verdict.

## Verdict

- [ ] ✅ Approve
- [ ] 🟡 Approve with changes (see findings)
- [ ] ❌ Request changes (blocking findings)

## Findings

> Severity: 🔴 blocker · 🟠 major · 🟡 minor · 🔵 nit. Each finding cites a location
> and a concrete fix.

| # | Severity | Location | Finding | Suggested fix |
|---|----------|----------|---------|---------------|
| 1 | 🔴/🟠/🟡/🔵 | `path:line` | What's wrong | How to fix |

## Standards compliance

Result of running the relevant checklist (`standards/checklists/`):

- Structure & naming: pass / fail — …
- Required files: pass / fail — …
- Documentation: pass / fail — …
- Tests: pass / fail — …
- Security: pass / fail — …
- Versioning: pass / fail — …

## What's good

Call out strengths worth preserving.

## Follow-ups

Non-blocking items to track separately.
