# Tests — {{TITLE}}

> Skill-local validation per `standards/testing.md`. Advanced skills should also
> test their helper scripts and the progressive-disclosure branches.

## Behavior cases

### 1 — happy path
- **Given:** … **When:** invoked **Then:** …

### 2 — edge / boundary
- **Given:** … **When:** … **Then:** …

### 3 — failure / refusal
- **Given:** invalid/unsafe input **When:** … **Then:** graceful failure

## Helper-script cases

### `scripts/{{HELPER}}`
- **Given:** `<args>` **When:** run **Then:** `<exit code + output>`
- **Given:** missing args **When:** run **Then:** usage error, non-zero exit

## Fixtures

List fixture files in this folder and what they represent.
