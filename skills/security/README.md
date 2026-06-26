# Security Skills

> AppSec, secrets, threat modeling, and secure defaults (defensive use only). Charter source: [/TAXONOMY.md](../../TAXONOMY.md). All skills conform to
> [/standards/](../../standards/) and validate against
> [skill.schema.yaml](../../shared/schemas/skill.schema.yaml).

| Skill | Does | Maturity |
|-------|------|----------|
| [dependency-vuln-auditor](dependency-vuln-auditor/) | Use this to audit dependencies for known vulnerabilities and a remediation path. | 🔹 baseline |
| [secret-scanner](secret-scanner/) | Use this to detect committed secrets and credentials and produce a safe remediation plan. | 🥇 gold |
| [security-headers-configurer](security-headers-configurer/) | Use this to configure security headers and TLS correctly. | 🔹 baseline |
| [threat-modeler](threat-modeler/) | Use this to run a STRIDE threat model on a system design. | 🔹 baseline |

> **Maturity:** 🥇 gold = production reference · 🔹 baseline = complete but concise ·
> ⏳ draft = planned. See the [maturity model](../../README.md#maturity-model). Skill
> anatomy reference: [/skills/architecture/README.md](../architecture/README.md).
