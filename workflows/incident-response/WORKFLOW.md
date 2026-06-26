---
name: incident-response
description: Detect, mitigate, communicate, and run a postmortem for a production incident.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [incident, operations, sre, postmortem]
---

# Incident Response (Workflow)

> Detect, mitigate, communicate, and run a postmortem for a production incident.

## Outcome

An incident is mitigated, stakeholders kept informed, and a blameless postmortem
with action items is produced.

## Composition

| Step | Uses | Min version | Produces |
|------|------|-------------|----------|
| 1 | `skill:devops/observability-instrumenter` | 0.1.0 | signal/triage data |
| 3 | `skill:devops/incident-runbook-builder` | 0.1.0 | mitigation runbook |
| 4 | `skill:leadership/stakeholder-comms-writer` | 0.1.0 | status comms |

## Steps

1. **Detect & assess** — confirm the incident; assign severity; pull signals.
2. **Declare & coordinate** — assign roles (IC, comms, ops).
3. **Mitigate** — stop the bleeding (rollback/flag/scale) before root-causing.
4. **Communicate** — regular stakeholder updates at the severity's cadence.
5. **Resolve & postmortem** — confirm recovery; write a blameless postmortem + actions.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| alert | yes | The triggering signal / report |
| severity | no | Initial severity (refined in step 1) |

## Outputs

A mitigated incident + comms trail + blameless postmortem with action items.

## Failure handling

- Mitigation worsens things → roll back the mitigation; reassess.
- Root cause unknown → mitigate first; investigate after stabilization.

## Constraints & safety

- Mitigate before root-causing. Postmortems are blameless (VISION §10).
