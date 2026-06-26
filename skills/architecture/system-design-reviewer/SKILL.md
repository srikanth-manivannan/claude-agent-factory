---
name: system-design-reviewer
description: Use this to review a system or software design against scalability, reliability, security, and cost.
version: 0.1.0
category: architecture
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [architecture, review, design, quality-attributes, scalability]
---

# System Design Reviewer

> Use this to review a system or software design against scalability, reliability, security, and cost.

> **Tech profile** — Technology: any · Language: n/a · Stack: n/a · Toolchain: n/a · Domain: architecture
> *(Pure-reasoning skill — reviews any design, from a microservice to a data platform.)*

## When to use this skill

- Reviewing a proposed design/RFC before implementation begins.
- Auditing an existing system for quality-attribute risks.
- Preparing input for an architecture decision or ADR.

## When NOT to use this skill

- Choosing between design options — use `architecture/tradeoff-analyzer`.
- Planning a migration of an existing system — use `architecture/migration-planner`.
- Line-by-line code review — use a code-review workflow.

## Prerequisites

- A described design (diagram, doc, or narrative) and its goals/constraints.
- The expected scale/load and any compliance requirements, if known.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `design` | yes | The design to review (doc, diagram, or description) |
| `goals` | yes | What the system must achieve |
| `expected_scale` | no | Load/growth expectations (assumed + stated if absent) |
| `constraints` | no | Budget, compliance, team, deadline constraints |

## Instructions

1. **Restate the design + goals.** Summarize the design in your own words and the
   goals it serves. If the design is ambiguous, list the clarifying questions rather
   than guessing.
2. **Map the critical path.** Identify the request/data flow that matters most and
   its dependencies.
3. **Review against quality attributes**, each producing findings:
   - **Scalability** — bottlenecks, statefulness, horizontal-scaling path.
   - **Reliability** — single points of failure, failure modes, graceful degradation.
   - **Security** — trust boundaries, authz, data protection (defer depth to
     `security-review`, but flag here).
   - **Cost & operability** — cost drivers, observability, maintenance burden.
   - **Data** — consistency model, growth, integrity.
4. **Severity-tag every finding** 🔴 blocker / 🟠 major / 🟡 minor, each with a
   concrete recommendation (see [/standards/review-process.md](../../../standards/review-process.md)).
5. **Note strengths.** Call out what is sound and should be preserved.
6. **Give a verdict** — approve / approve-with-changes / needs-rework — driven by the
   highest open severity.
7. **List assumptions.** Especially any assumed scale/constraints.

## Output

A structured design review: restated design, critical-path map, severity-tagged
findings per quality attribute (with recommendations), strengths, a verdict, and
assumptions. Maps directly onto the
[architecture-review checklist](../../../standards/checklists/architecture-review.md).

## Constraints & safety

- **Evidence-based.** Each finding cites a part of the design; no vague criticism.
- **No rewrite.** Recommend; do not silently redesign the system.
- **Defer deep security** to `security-audit`/`security-review` but never skip flagging.
- Conforms to [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).

## Examples

Minimal below; full reviews in [EXAMPLES.md](EXAMPLES.md).

**Given:** a single-instance API + single-DB design expecting 50× growth.
**Produces:** findings incl. 🔴 single point of failure (DB), 🟠 stateful API blocks
horizontal scaling, with recommendations, plus a verdict of needs-rework.
