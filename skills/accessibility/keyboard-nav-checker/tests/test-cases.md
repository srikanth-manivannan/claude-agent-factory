# Tests & Validation Guidance — Keyboard Nav Checker

> Conforms to [/standards/testing.md](../../../../standards/testing.md). Validate with `scripts/validate`.

## Behavior cases
### 1 — happy path
- **Given:** valid inputs **When:** the skill runs **Then:** it fulfils its purpose.
### 2 — edge / boundary
- **Given:** an unusual but valid input **Then:** the skill handles it gracefully.
### 3 — failure / refusal
- **Given:** invalid or out-of-scope input **Then:** the skill declines or fails safely.
