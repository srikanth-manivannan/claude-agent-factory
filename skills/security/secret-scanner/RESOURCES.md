# Resources — Secret Scanner

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [security](../../../standards/security.md),
  [testing](../../../standards/testing.md),
  [documentation](../../../standards/documentation.md),
  [prompt-engineering](../../../standards/prompt-engineering.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).
- **Checklist it maps to:** [security-review.md](../../../standards/checklists/security-review.md).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Sibling** | `security/dependency-vuln-auditor` *(planned)* | supply-chain scanning |
| **Sibling** | `security/secrets-management-setup` *(planned)* | prevention/storage |
| **Used by workflow** | `security-audit`, `dependency-audit`, `rotate-secrets` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | scan step |

## Concepts & background (vendor-neutral)

- **Secret detection** (pattern + entropy); **rotate-before-remove**.
- **History rewriting** to purge leaked secrets; **secrets managers / vaults**.
- **Shift-left** prevention (pre-commit + CI scanning).

## Provenance & credits

- Method synthesized from standard secret-scanning/remediation practice. Defensive use
  only. No third-party content copied; MIT (VISION §13).
