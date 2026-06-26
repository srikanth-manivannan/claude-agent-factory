# System Design Reviewer

> Use this to review a system or software design against scalability, reliability, security, and cost.

**Category:** architecture · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Gives a proposed or existing design a structured, severity-tagged review across the
quality attributes that actually break systems — **scalability, reliability,
security, cost/operability, and data** — and returns a verdict with concrete
recommendations. It is the architecture equivalent of a code review: evidence-based,
actionable, and free of vague hand-waving.

Technology-agnostic and pure-reasoning: it reviews a microservice, a data pipeline,
or a whole platform with the same method.

## Quickstart

```text
1. Copy skills/architecture/system-design-reviewer/ into your skills directory.
2. Invoke with: the design (doc/diagram/description) + its goals (+ scale/constraints).
3. Receive findings per quality attribute, strengths, and a verdict.
```

## How it works

Seven steps: restate → map critical path → review per quality attribute → severity-tag
findings → note strengths → verdict → assumptions. The authoritative procedure is in
[SKILL.md](SKILL.md). Findings and verdict map 1:1 onto the
[architecture-review checklist](../../../standards/checklists/architecture-review.md).

## Inputs & outputs

- **Inputs:** `design`, `goals`, optional `expected_scale`, `constraints`.
- **Outputs:** restated design + critical-path map + severity-tagged findings (with
  recommendations) + strengths + verdict + assumptions.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Add quality attributes** (e.g. privacy, latency SLOs) at step 3.
- **Tune depth** — quick triage vs. deep audit by scope of the critical path.
- **Chain** the output into `architecture/adr-author` or `architecture/tradeoff-analyzer`.

## Limitations

- Reviews the **design as described** — it cannot catch what the design omits to mention.
- Defers deep security analysis to `security-audit`/`security-review` (flags only).
- Not a substitute for load testing or a real spike.

## Related

See [RESOURCES.md](RESOURCES.md). Complements `architecture/tradeoff-analyzer`
(option choice) and `architecture/migration-planner`; powers the `architecture-review`
workflow and feeds `play-secure-launch` / `play-zero-to-production`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- A reusable quality-attribute scenario library (e.g. ATAM-style scenarios).
- Optional risk-scoring per finding (likelihood × impact).
- Auto-generation of an ADR stub from blocker findings.
- Diagram ingestion once `documentation/diagram-generator` exists.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
