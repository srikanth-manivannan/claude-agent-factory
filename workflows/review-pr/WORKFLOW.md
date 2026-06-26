---
name: review-pr
description: Produce a structured, standards-based PR review with severity-tagged findings.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [review, pr, quality, code-review]
---

# Review PR (Workflow)

> Produce a structured, standards-based PR review with severity-tagged findings.

## Outcome

A review verdict (approve / approve-with-changes / request-changes) backed by
specific, actionable, severity-tagged findings and follow-ups.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 2 | `skill:leadership/code-review-coach` | 0.1.0 | correctness/design findings |
| 3 | `skill:security/dependency-vuln-auditor` | 0.1.0 | dependency/security findings |
| 4 | `skill:documentation/doc-linter` | 0.1.0 | docs completeness findings |

## Steps

1. **Understand the change** — read the diff + PR intent; restate what it does.
2. **Review correctness & design** — logic, edge cases, design fit; tag findings.
3. **Review security & dependencies** — new deps, secrets, unsafe patterns.
4. **Review docs & tests** — completeness vs `standards/`.
5. **Verdict** — produce a Review (templates/review) with findings + follow-ups.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| pr_ref | yes | The PR / diff to review |

## Outputs

A structured review with a verdict and severity-tagged findings.

## Failure handling

- Diff too large/unfocused → request the author split it.
- Missing context → ask before assuming intent.

## Constraints & safety

- Findings address the work, never the person (VISION §10).
- Blocking findings (🔴) must cite a concrete fix.
