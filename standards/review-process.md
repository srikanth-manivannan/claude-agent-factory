# Review Process Standard

> How artifacts are reviewed and gated before they ship. Operationalizes the
> [checklists](checklists/) and the Factory's gates (FACTORY §6–§7).

**Min standard:** 0.1.0 · See also: [contributing.md](contributing.md),
[testing.md](testing.md).

## Every review runs two layers

1. **[Universal Core checklist](checklists/_universal.md)** — always, for any artifact.
2. **The relevant domain checklist(s)** — e.g. [security-review](checklists/security-review.md)
   for security-sensitive work, [documentation-review](checklists/documentation-review.md)
   for docs, etc.

## Item annotations & verdict

Items are tagged severity (🔴 blocker / 🟠 major / 🟡 minor) and `[auto]` / `[manual]`
(see the [checklists README](checklists/README.md)).

| Outcome | Condition |
|---------|-----------|
| **Request changes** | any unresolved 🔴 |
| **Approve with changes** | open 🟠, no 🔴 |
| **Approve** | only 🟡 remaining |

Every item is checked or marked **N/A with a reason**.

## The gates (FACTORY.md)

1. **Plan gate (human)** — approve the build plan before scaffolding.
2. **Validation wall (auto)** — `scripts/validate` 100% green (== CI).
3. **Review gate (human)** — domain + universal review verdict = approve.
4. **CI gate (auto)** — CI re-runs every `[auto]` check at handoff.

Gates are ordered and non-skippable; a failure routes backward, never forward.

## Who reviews

- The Factory's Reviewer (single or escalated sub-agent, FACTORY §4.4) for generated
  artifacts.
- Area maintainers via `CODEOWNERS` for human PRs (governance: VISION §9).
- Feedback addresses the work, never the person (VISION §10).
