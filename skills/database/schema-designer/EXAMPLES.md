# Examples — Schema Designer

> Realistic enterprise scenarios. Engine-agnostic method; DDL shown for Postgres. See [SKILL.md](SKILL.md).

## Example 1 — Orders system (happy path)

**Inputs:** entities = customers, orders, products, line-items; engine = Postgres;
access pattern = "list a customer's recent orders" (read-heavy).

**Produces (sketch):**
```sql
CREATE TABLE customers (
  id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email         CITEXT NOT NULL UNIQUE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE orders (
  id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id   BIGINT NOT NULL REFERENCES customers(id) ON DELETE RESTRICT,
  status        TEXT NOT NULL CHECK (status IN ('pending','paid','shipped','cancelled')),
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE line_items (             -- M:N orders<->products, with quantity
  order_id      BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id    BIGINT NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
  quantity      INT NOT NULL CHECK (quantity > 0),
  PRIMARY KEY (order_id, product_id)
);
CREATE INDEX idx_orders_customer_recent ON orders (customer_id, created_at DESC);
```
**Rationale:** composite index serves the access pattern; `ON DELETE RESTRICT` on
customers prevents orphaning orders; `CHECK` enforces the status enum in-schema.

## Example 2 — Deliberate denormalization

**Inputs:** a dashboard needs `order_total` on every read; recomputation is expensive.

**Behavior:** adds a denormalized `orders.total_cents` **with a recorded rationale**
("read 100x > write; maintained via trigger/app on line-item change") rather than
silently denormalizing. Trade-off is explicit.

## Example 3 — Edge: sensitive data

**Inputs:** schema includes `customers.tax_id`.

**Behavior:** flags `tax_id` as PII, recommends encryption at rest + restricted access,
and notes it should not appear in logs/indexes used for search.

## Anti-example

- ❌ A `users` table with a JSON blob for everything and no constraints — unqueryable,
  no integrity. Model the entities; constrain invariants.
- ❌ Indexing every column "to be safe" — each index taxes writes. Index the access patterns.

## Try it yourself

- Add an access pattern "search orders by status" — see a partial index proposed.
- Switch `engine` to MySQL — note type/identity changes (`BIGINT AUTO_INCREMENT`, etc.).
