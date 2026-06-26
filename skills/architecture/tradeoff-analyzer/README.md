# Tradeoff Analyzer

> Use this to weigh multiple options against weighted criteria and produce a defensible recommendation.

**Category:** architecture · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Turns a fuzzy "which should we pick?" into a transparent, weighted comparison and a
**defensible recommendation** — the kind you can paste into an ADR and defend in
review. It forces the implicit (criteria, weights, bias) to become explicit, and
flags when a decision is too close or too weight-sensitive to call confidently.

It is a **pure-reasoning, technology-agnostic** skill: it works for picking a
database, a framework, a vendor, an algorithm, or an org process.

## Quickstart

```text
1. Copy skills/architecture/tradeoff-analyzer/ into your project's skills directory.
2. Invoke via Claude Code with: the decision, the options (≥2), and any constraints.
3. Receive a weighted scoring matrix + recommendation + sensitivity note.
```

## How it works

It runs an eight-step decision procedure (frame → apply constraints → criteria &
weights → score → total → sensitivity → recommend → assumptions). The full,
authoritative procedure is in [SKILL.md](SKILL.md). The method deliberately
separates **weights** (what matters, set once, up front) from **scores** (how each
option does) so that bias is isolated in one auditable place.

## Inputs & outputs

- **Inputs:** `decision`, `options` (≥2), optional `criteria`, `weights`, `constraints`.
- **Outputs:** a weighted scoring matrix, a recommendation (with margin + primary
  risk), a sensitivity note, and an assumptions list. ADR-ready.

See [EXAMPLES.md](EXAMPLES.md) for worked end-to-end runs.

## Customization

- **Swap the scale.** 1–5 is the default; 1–10 works for finer comparisons.
- **Add criteria.** Domain-specific criteria (e.g. compliance, latency) plug in at
  step 3 without changing the method.
- **Pin weights.** Provide `weights` to lock stakeholder-agreed priorities.

## Limitations

- Output is a **decision aid, not a proof** — a small margin is a tie.
- Quality depends on honest scoring; garbage evidence → garbage recommendation.
- It does not gather the evidence for you; pair it with a research skill for that.

## Related

See [RESOURCES.md](RESOURCES.md) for cross-links. In brief: feeds
`architecture/adr-author`; complements `architecture/system-design-reviewer` and
`architecture/migration-planner`; used by the `architecture-review` workflow and the
`play-secure-launch` / `play-zero-to-production` playbooks.

## Validation & review

- **Validation guidance:** [tests/test-cases.md](tests/test-cases.md) — behavior
  cases + how to verify.
- **Review guidance + self-review result:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Optional Monte-Carlo sensitivity (vary all weights within ±10%, report flip rate).
- Pairwise (AHP-style) weight elicitation for contested decisions.
- A machine-readable matrix output (JSON) for downstream tooling.
- Confidence scoring per criterion to distinguish "low score" from "low evidence".

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0** (initial reference release).
