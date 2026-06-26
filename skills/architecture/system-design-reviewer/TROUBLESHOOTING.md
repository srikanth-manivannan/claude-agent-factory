# Troubleshooting — System Design Reviewer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Quick diagnostics

- [ ] Is the design described concretely enough to map a critical path?
- [ ] Does every finding have a severity AND a recommendation?
- [ ] Were strengths noted (not just problems)?
- [ ] Is the verdict consistent with the highest open severity?

## Common issues

### Symptom: Review is vague ("could be better")
- **Cause:** findings not tied to specific parts of the design.
- **Fix:** rewrite each finding to cite a component/flow and a concrete recommendation.

### Symptom: The skill asks questions instead of reviewing
- **Cause:** the design is too ambiguous to review responsibly (step 1).
- **Fix:** answer the clarifying questions / supply the missing flow; this is correct
  behavior, not a failure.

### Symptom: Verdict doesn't match findings
- **Cause:** verdict not derived from severity.
- **Fix:** any open 🔴 → needs-rework; 🟠 only → approve-with-changes; 🟡 only → approve.

### Symptom: Security feels under-covered
- **Cause:** by design, deep security is deferred.
- **Fix:** run `security-audit` / [security-review](../../../standards/checklists/security-review.md);
  this skill only flags security risks at the design level.

### Symptom: Recommendations assume a technology the team isn't using
- **Cause:** missing/!ignored constraints.
- **Fix:** supply `constraints`; recommendations should respect the team's stack.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and
  [architecture-review.md](../../../standards/checklists/architecture-review.md).
- Open an issue with the design + the produced review attached.
