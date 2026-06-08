---
name: backend-design
description: Create distinctive, production-grade backend systems with high engineering quality. Use this skill when the user asks to build APIs, services, data models, background jobs, authentication systems, or any server-side logic (examples include REST/GraphQL APIs, microservices, database schemas, queue workers, auth flows, middleware, and CLI tools). Generates robust, idiomatic, and architecturally sound backend code that avoids generic AI-slop patterns.
---

This skill guides creation of distinctive, production-grade backend systems that avoid the systematic failure patterns of AI-generated code. Implement real working server-side logic with exceptional attention to architecture, correctness, security, and operational reality.

The user provides backend requirements: a service, API, data layer, job, or system to build. They may include context about the language, framework, scale, and constraints.

## Engineering Thinking

Before writing a single line, understand the context and commit to a CLEAR architectural direction:

- **Purpose**: What problem does this system solve? What are the read/write patterns, scale expectations, and failure tolerance?
- **Architecture**: Pick the right shape — monolith, modular monolith, microservice, event-driven, serverless. Default to the **simplest architecture that actually fits** the stated scale. Do not reach for microservices prematurely.
- **Constraints**: Language, framework, deployment target, latency budget, team size, existing stack.
- **Differentiation**: What makes this implementation trustworthy? What's the one property it must never violate — consistency, availability, idempotency, auditability?

**CRITICAL**: Choose a clear structural direction and execute it with precision. A well-reasoned monolith and a well-reasoned distributed system both work — the key is intentionality, not complexity. Never add layers because they sound mature.

Then implement working code that is:

- Correct and defensively written against edge cases
- Idiomatic in the target language and framework
- Secure by default, not as an afterthought
- Observable — it must be possible to know what it is doing in production
- Structured so a new engineer can understand the domain in 30 minutes

## Backend Architecture Guidelines

Focus on:

- **Layering**: Separate concerns cleanly — routing/controllers handle HTTP concerns, services contain business logic, repositories handle data access. Business logic must never live in route handlers, and database queries must never be scattered through service files. Each layer has one job.
- **Data modeling**: Schema design determines system fate more than almost any other decision. Model the domain first, not the API. Choose normalization vs. denormalization deliberately based on read/write patterns. Name things after what they mean, not how they are stored.
- **Error handling**: Every failure path is a first-class citizen. Return structured, typed errors — not bare exceptions, not `null`, not `false`. Differentiate operational errors (expected: not found, validation failed) from programmer errors (unexpected: null dereference, assertion violated). Never leak stack traces or internal state to API consumers.
- **Idempotency**: Any operation that mutates state must be safe to retry. Design for at-least-once delivery, especially for jobs, webhooks, and external API calls. Use idempotency keys on writes that matter.
- **Transaction discipline**: Transactions must be as short as possible and as wide as necessary. Do not perform network calls, send emails, or trigger side effects inside a database transaction. Commit first, act second.

NEVER produce generic AI-slop backend patterns: N+1 queries disguised behind clean-looking ORM code, catch blocks that swallow errors silently, hardcoded credentials, `any` types used to escape type-safety, or secrets stored in environment variables without a documented management strategy.

Interpret requirements architecturally. Ask: what invariants must this system maintain even under partial failure? Design to protect those invariants, then build the happy path.

**IMPORTANT**: Match implementation complexity to the actual problem. A CRUD API for a small team does not need an event-sourcing architecture. A payment processor cannot be built without idempotency, distributed locks, and audit logs. Sophistication comes from correctly matching the tool to the problem — not from using the most tools.

## Backend Quality Pillars

### Security

Treat security as a structural property, not a checklist. Every input is untrusted until validated. Every secret lives outside the codebase. Enforce least-privilege at the database, service, and network layer. Use parameterized queries without exception. Hash passwords with bcrypt/argon2, never MD5/SHA1. Apply rate limiting at the API boundary. Use OWASP Top 10 as a floor, not a ceiling.

For authentication: prefer established libraries over hand-rolled JWT handling. Token expiry, rotation, and revocation must be designed, not assumed. For authorization: design a clear model (RBAC, ABAC, policy-based) before writing a single auth check.

### Observability

A system that cannot be understood in production is not finished. Every service must emit:

- **Structured logs** — JSON with consistent fields: `timestamp`, `level`, `trace_id`, `service`, `message`, `error` (if applicable). No unstructured `console.log`.
- **Metrics** — request count, error rate, latency percentiles (p50/p95/p99), queue depth, cache hit rate. Export to Prometheus or equivalent.
- **Traces** — distributed trace IDs on every request, propagated across service calls. Use OpenTelemetry where possible.

Log the right things: requests in, responses out, background job start/finish, external calls attempted/completed/failed. Never log credentials, PII, or full request/response bodies without sanitization.

### Testing

Write tests that would catch the actual bugs in the system, not just the happy paths. Unit test pure business logic. Integration test database interactions against a real (containerized) database. Contract test external API integrations. For critical paths — payments, auth, data mutations — write explicit tests for the failure scenarios, not just success.

Test names must read as specifications: `should return 409 when email already exists`, not `test_create_user_2`. Tests are documentation.

### Performance

Measure before optimizing. Every performance claim must be backed by a profiler or a load test, not intuition. Common structural issues to prevent by default: N+1 queries (use eager loading or explicit joins), missing indexes on foreign keys and filter columns, synchronous work that could be async (email sending, webhook dispatch, report generation), unbounded queries without pagination.

For any read-heavy path: design the caching strategy alongside the data model. State what is cached, for how long, what invalidates it, and what happens when the cache is cold.

### Resilience

External calls fail. Design for it. Every call to a third-party API or downstream service must have: a timeout, a retry policy with backoff and jitter, and a defined behavior when the dependency is unavailable (degrade gracefully, queue for later, or fail fast with a clear error). Circuit breakers for dependencies that are flaky. Bulkheads to prevent one slow dependency from exhausting the connection pool.

## Code Character

What makes backend code excellent is not what it does — it's how it handles what goes wrong.

Excellent backend code:

- Makes impossible states unrepresentable in the type system
- Fails loudly during startup if configuration is missing or invalid
- Returns consistent error shapes across every endpoint
- Has no hidden global state or shared mutable singletons
- Is boring — it does the obvious thing, clearly, every time

Avoid cleverness. A clever piece of backend code is a future debugging session. Prefer explicit over implicit, verbose over ambiguous, typed over stringly-typed. Write the code you would want to read at 2am during an incident.

## What to Never Produce

| Anti-pattern                                         | Why it is harmful                                                 |
| ---------------------------------------------------- | ----------------------------------------------------------------- |
| Silent `catch` blocks                                | Errors disappear; failures become mysteries                       |
| Secrets in source code or env files committed to git | Immediate security exposure                                       |
| ORM queries inside loops                             | N+1 problem; kills performance at scale                           |
| Unbounded list queries without pagination            | Blows up memory and response times                                |
| Hand-rolled auth/crypto logic                        | Almost always wrong; use audited libraries                        |
| `any` / untyped data flowing through the system      | Type safety is the load-bearing wall                              |
| Transactions wrapping network calls                  | Holds locks while waiting for the network; deadlocks and timeouts |
| Microservices for a team of two                      | Operational complexity without benefit                            |
| Error messages that expose internals to the client   | Information disclosure vulnerability                              |
| Tests that only test success paths                   | The system is only as reliable as its tested failure paths        |

## Language and Framework Idioms

Write idiomatic code for the target ecosystem. Each language has a grain — write with it, not against it:

- **Node.js/TypeScript**: async/await throughout, strict TypeScript, Zod or similar for runtime validation, no callback hell, no `require()` in new code
- **Python**: type hints on all function signatures, Pydantic for validation, context managers for resources, explicit over implicit, dataclasses or attrs over raw dicts for structured data
- **Go**: errors as values, explicit error propagation, small interfaces, no global state, `context.Context` threaded through every I/O call
- **Java/Kotlin**: immutable value objects, constructor injection (not field injection), checked exceptions only for truly recoverable conditions, records/data classes for DTOs
- **Rust**: ownership means the compiler enforces the invariants — use it; `Result` and `Option` over panics in library code; no `unwrap()` in production paths

If the language is unspecified, ask — or choose the language that best fits the stated problem and justify the choice.

## Deployment and Operational Readiness

Production code includes its operational surface:

- **Health endpoints**: `/health` (liveness) and `/ready` (readiness) for every service, returning structured status with dependency checks
- **Graceful shutdown**: drain in-flight requests, close database connections cleanly, flush pending log buffers before exit
- **Configuration**: all config from environment; fail fast with a clear error if required variables are missing at startup; document every variable
- **Migrations**: schema changes must be backwards-compatible before the code that uses them is deployed; never drop columns in the same deployment that removes their usage
- **Secrets management**: document the expected secrets provider (Vault, AWS Secrets Manager, GCP Secret Manager) rather than assuming plain environment variables are sufficient

Remember: the code that ships is the beginning, not the end. Write systems that can be understood, monitored, debugged, and modified by someone who wasn't in the original design meeting.
