# Troubleshooting — Tradeoff Analyzer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) for the method and
> [/standards/](../../../standards/) for the rules referenced below.

## Quick diagnostics

- [ ] Are there genuinely ≥2 viable options? (1 option → no analysis to do.)
- [ ] Do the weights sum to 100%?
- [ ] Does every score have a one-line justification?
- [ ] Were hard constraints applied *before* scoring?

## Common issues

### Symptom: The recommendation feels predetermined / biased
- **Likely cause:** weights were set to favor a preferred option.
- **Fix:** redo step 3 stating the rationale for each weight *before* looking at
  options; have a second reviewer sanity-check the weights.
- **Prevent:** weights are chosen from goals/constraints, never from the options.

### Symptom: Two options tie (margin ≤ 0.2)
- **Likely cause:** the options are genuinely comparable on the chosen criteria.
- **Fix:** report it as a tie; add a tie-breaker criterion that reflects a real
  secondary priority, or escalate for a judgment call. Do not manufacture a winner.

### Symptom: Result flips with a small weight change
- **Likely cause:** the decision is weight-sensitive (step 6).
- **Fix:** flag it explicitly, surface which weight drives the flip, and escalate the
  weighting decision to stakeholders rather than auto-deciding.

### Symptom: A score has no evidence
- **Likely cause:** missing data for that option/criterion.
- **Fix:** record it as an **assumption** (step 8) instead of inventing a number;
  recommend gathering the evidence (pair with a research skill).

### Symptom: Output doesn't fit an ADR
- **Cause:** missing the recommendation/consequences framing.
- **Fix:** ensure the output includes recommendation + primary risk + assumptions;
  these map to the ADR "Decision" and "Consequences" sections (→ `architecture/adr-author`).

## Getting more help

- Re-read the method in [SKILL.md](SKILL.md) and the rules in
  [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).
- Open an issue with the decision, options, and the produced matrix attached.
