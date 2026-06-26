# Examples — Unit Test Generator

> Worked examples. Language/framework come from the tech profile; the method is
> universal. See [SKILL.md](SKILL.md).

## Example 1 — Pure function (happy path)

**Unit:** `divide(a, b) -> number`.

**Generated cases**
- happy: `divide(6, 3) == 2`
- edge: `divide(0, 5) == 0`, `divide(-6, 3) == -2`, large operands
- failure: `divide(1, 0)` raises/handles division-by-zero gracefully

**Coverage intent:** all branches (normal, zero divisor) covered.

## Example 2 — Function with a side effect (mocking)

**Unit:** `saveUser(user, db)` writes to `db`.

**Approach:** mock `db`; assert `db.write` called once with the normalized user
(behavior), not the internal SQL string (implementation). Failure case: `db.write`
rejects → `saveUser` surfaces a domain error, doesn't swallow it.

## Example 3 — Edge: ambiguous behavior

**Unit:** `parseDate(s)` with no spec for invalid input.

**Behavior:** the skill asks "what should `parseDate('')` do — throw, or return null?"
rather than guessing, then generates tests for the agreed contract.

## Anti-example

- ❌ A test asserting an internal private method was called. Tests should assert
  observable behavior so they survive refactors.
- ❌ `sleep(1000)`-based timing tests — non-deterministic; forbidden.

## Try it yourself

- Add a `behavior_spec` that empty input returns `null` — see the failure case change.
- Request the suite for a second framework — note conventions adapt.
