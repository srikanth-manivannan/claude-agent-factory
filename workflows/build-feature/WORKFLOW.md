---
name: build-feature
description: Take a planned feature from spec to a tested, documented, review-ready PR.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [build, feature, full-stack, delivery]
---

# Build Feature (Workflow)

> Take a planned feature from spec to a tested, documented, review-ready PR.

A multi-step orchestration that turns an approved feature plan into shippable code.
Named for its outcome.

## Outcome

A feature is implemented (backend and/or frontend), covered by tests, documented,
and opened as a PR that passes CI — ready for `review-pr`.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 2 | `skill:backend/rest-endpoint-scaffold` | 0.1.0 | server-side implementation |
| 2 | `skill:frontend/component-scaffold` | 0.1.0 | client-side implementation |
| 3 | `skill:testing/unit-test-generator` | 0.1.0 | tests |
| 4 | `skill:documentation/doc-writer` | 0.1.0 | docs/README updates |

> References point only *down* the ladder (ARCHITECTURE §17). Skills are
> declared-pending until built (WORKFLOWS §3).

## Steps

1. **Confirm the spec** — load the approved plan (`plan-feature`); restate scope,
   inputs/outputs, and acceptance criteria. Stop if the spec is missing.
2. **Implement** — build the backend endpoint and/or frontend component to the spec.
3. **Test** — generate unit tests covering happy path, an edge case, and a failure
   case; run them green.
4. **Document** — update README/docs and add a changelog entry.
5. **Open PR** — push a branch and open a PR with the plan + test results attached.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| feature_spec | yes | The approved plan / acceptance criteria |
| target_surface | yes | backend / frontend / both |

## Outputs

A branch + PR with implementation, passing tests, updated docs, and a changelog entry.

## Failure handling

- Missing/ambiguous spec → halt; route back to `plan-feature`.
- Tests fail → fix the cause before proceeding (never skip step 3).
- Scope creep detected → stop and re-confirm the spec.

## Constraints & safety

- Follow `standards/security.md` for any auth/input handling.
- No feature ships without tests (VISION §6.4).
