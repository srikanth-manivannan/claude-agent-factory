# Troubleshooting — Secret Scanner

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [/standards/security.md](../../../standards/security.md).

## Quick diagnostics

- [ ] Was authorization confirmed?
- [ ] Are findings redacted (no full secret values)?
- [ ] Does each finding recommend rotate-first remediation?
- [ ] Are false positives separated from confirmed findings?

## Common issues

### Symptom: The skill refuses to scan
- **Cause:** authorization not confirmed.
- **Fix:** confirm you are authorized to scan the target. This refusal is by design.

### Symptom: Too many false positives
- **Cause:** broad entropy heuristics over test/fixture data.
- **Fix:** add an allowlist/baseline; the report already separates likely-false-positives.

### Symptom: A real secret was missed
- **Cause:** novel/custom token format not in the pattern set.
- **Fix:** extend the pattern set with the org-specific format; re-scan.

### Symptom: Secret removed but still a risk
- **Cause:** deleting code doesn't un-expose a leaked credential.
- **Fix:** **rotate/revoke first**, then remove, then purge history.

### Symptom: Secret value appeared in output
- **Cause:** redaction bypassed — a defect.
- **Fix:** never emit full values; show prefix + length only. Report immediately.

## Getting more help

- Re-read [SKILL.md](SKILL.md) and [security-review](../../../standards/checklists/security-review.md).
- Open an issue with the (redacted) finding and context.
