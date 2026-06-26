# Threat Modeler

> Use this to run a STRIDE threat model on a system design.

**Category:** security · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT · **Maturity:** baseline

> ℹ️ **Baseline skill** — complete but intentionally concise (see the
> [maturity model](../../../README.md#maturity-model)). The gold-standard skills (e.g.
> [`architecture/tradeoff-analyzer`](../../../skills/architecture/tradeoff-analyzer/)) are the
> deep reference implementations.

## What it does
Provides a focused, standards-aligned capability so teams have a consistent way to
achieve this without rebuilding it each time: _Use this to run a STRIDE threat model on a system design._

## Quickstart
```text
1. Copy skills/security/threat-modeler/ into your project's skills directory.
2. Invoke it via Claude Code with the inputs listed in SKILL.md.
```

## Inputs & outputs
- **Inputs:** the subject to operate on, plus optional context/constraints.
- **Outputs:** a reviewable result fulfilling the skill's purpose.

## Customization
Adapt to your stack via the tech profile and inputs. To deepen this skill toward gold
standard, expand `SKILL.md` and the docs — contributions welcome ([Contributing](../../../CONTRIBUTING.md)).

## Limitations
- Baseline depth: the method is sound but examples and edge-case coverage are minimal.

## Validation & review
- [tests/test-cases.md](tests/test-cases.md) · [REVIEW.md](REVIEW.md) ·
  [TROUBLESHOOTING.md](TROUBLESHOOTING.md) · [IMPLEMENTATION.md](IMPLEMENTATION.md)

## Version history
See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0** (baseline).
