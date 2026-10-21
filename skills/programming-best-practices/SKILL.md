---
name: programming-best-practices
description: >-
  Apply production Go and Rust practices for project layout, errors,
  concurrency, HTTP and GraphQL APIs, PostgreSQL, Redis caching,
  authentication, web security, observability, testing, payments, and
  background jobs. Use when writing, reviewing, or refactoring Go or Rust
  services, APIs, schemas, caches, auth, or production readiness.
---

# Programming Best Practices

Write or review production Go and Rust by reading the reference that matches the task. Read that reference only. Open a second when the change crosses concerns, such as an endpoint that also needs auth and a migration. Apply the patterns marked good, and run the checklist in each reference you opened before finishing.

## Choose a reference

| Task | Read |
| --- | --- |
| Go layout, errors, concurrency, HTTP, generics | [references/golang-best-practices.md](references/golang-best-practices.md) |
| Go fan-out, worker pools, circuit breakers, DDD | [references/go-advanced-patterns.md](references/go-advanced-patterns.md) |
| Rust ownership, errors, async, types, Clippy | [references/rust-best-practices.md](references/rust-best-practices.md) |
| Rust zero-copy, type state, actors, macros | [references/rust-advanced-patterns.md](references/rust-advanced-patterns.md) |
| Auth, forms, uploads, WebSockets | [references/web-application-patterns.md](references/web-application-patterns.md) |
| REST, GraphQL, OpenAPI, events | [references/api-design-patterns.md](references/api-design-patterns.md) |
| Schema, migrations, queries, transactions, pooling | [references/database-engineering-patterns.md](references/database-engineering-patterns.md) |
| Redis, CDN, rate limits, compression | [references/caching-performance-patterns.md](references/caching-performance-patterns.md) |
| Authn, authz, validation, idempotency, privacy | [references/api-security-patterns.md](references/api-security-patterns.md) |
| Preventing listed web vulnerabilities | [references/web-security-attacks-guide.md](references/web-security-attacks-guide.md) |
| Logs, traces, metrics, health checks | [references/observability-patterns.md](references/observability-patterns.md) |
| Property, contract, integration, load, fuzz tests | [references/testing-patterns.md](references/testing-patterns.md) |
| Payments, orders, job queues | [references/real-world-project-patterns.md](references/real-world-project-patterns.md) |
| Short reminders while editing | [references/QUICK_REFERENCE.md](references/QUICK_REFERENCE.md) |

For a new Go or Rust repo, also use the matching files under [examples/](examples/).

## How to apply

1. Match the language and the layer being changed. Stay inside the requested scope. Leave unrelated code as it is.
2. Follow the patterns marked good. Treat the patterns marked bad as defects to avoid or remove when they are in the code you are changing.
3. Prefer the project's existing libraries and layout when they already satisfy the reference. Do not introduce a new framework, cache, or queue to match an example.
4. Security references are for prevention and review. Implement the mitigations. Do not write exploit procedures, payloads, or attack walkthroughs.
5. Before finishing, walk the checklist at the end of each reference you used, then the shared production checklist in the quick reference.

## Defaults

Go:

- Entry points live in `cmd/`. Private code lives in `internal/`. Put a package in `pkg/` only when other modules should import it.
- Wrap errors with `%w`. Propagate `context.Context`. Set timeouts on every HTTP client and server.
- Call `WaitGroup.Add` before starting the goroutine. Use `errgroup` when the goroutines must fail together.
- Test with `go test -race ./...`.

Rust:

- Use `thiserror` in libraries and `anyhow` in applications.
- Borrow when the caller keeps the value. Keep `unwrap` out of production paths.
- Use Tokio for async. Address Clippy warnings.
- Run `cargo test` and `cargo clippy -- -D warnings`.

Both:

- Handle every error. Close resources. Externalize configuration. Log with context. Shut down gracefully.
- Measure before optimizing.

## Examples

- Go CI, golangci-lint, and Makefile: [examples/go-api-example](examples/go-api-example)
- Rust CI, rustfmt, Clippy, and Cargo settings: [examples/rust-api-example](examples/rust-api-example)

These notes compile 100 Go Mistakes, Effective Go, the Rust API Guidelines, and OWASP guidance. The source collection is [nutcas3/best-practices](https://github.com/nutcas3/best-practices).
