# Incident Response (Workflow)

> Detect, mitigate, communicate, and run a postmortem for a production incident.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Drives a production incident from detection to a blameless postmortem, prioritizing
mitigation and clear stakeholder communication.

## The flow

`detect → declare/coordinate → mitigate → communicate → resolve + postmortem`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:devops/observability-instrumenter` (≥ 0.1.0)
- `skill:devops/incident-runbook-builder` (≥ 0.1.0)
- `skill:leadership/stakeholder-comms-writer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** triggering alert, optional initial severity.
- **Outputs:** mitigated incident + comms trail + postmortem with actions.

## Customization

Feed postmortem actions into `tech-debt-paydown` or `fix-bug`.

## Limitations

- Assumes some observability exists; pair with `setup-observability` if not.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
