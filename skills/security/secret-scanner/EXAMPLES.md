# Examples — Secret Scanner

> Worked examples. Defensive, authorized use only. See [SKILL.md](SKILL.md).

## Example 1 — Key in git history (happy path)

**Input:** repo with an AWS access key committed 30 commits ago; authorization = confirmed.

**Finding**
| Sev | Location | Evidence (redacted) | Class | Remediation |
|-----|----------|---------------------|-------|-------------|
| 🔴 | `config/old.env` @ commit `a1b2c3` | `AKIA…(20 chars)` | confirmed | 1) **revoke key in AWS** 2) remove file 3) purge from history 4) add to ignore + use a secrets manager |

**Note:** the key is treated as compromised — rotation comes first, deletion second.

## Example 2 — High-entropy false positive

**Input:** a base64 test fixture flagged as a possible secret.

**Behavior:** classified as **likely false-positive** (in a test fixture, no key
prefix), surfaced separately so it doesn't drown real findings. Recommends an allowlist
entry.

## Example 3 — Refusal: no authorization

**Input:** scan request without authorization.

**Behavior:** **refuses** and explains that scanning requires authorization (defensive
use only).

## Anti-example

- ❌ Printing the full secret value into the report/logs. Always redact — echoing a live
  credential re-exposes it.
- ❌ Recommending "just delete the file" without rotating the key first.

## Try it yourself

- Re-run Example 1 with `scan_history: false` — the history finding disappears (only the
  working tree is scanned).
