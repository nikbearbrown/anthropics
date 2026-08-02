# Claude Agent SDK Video Ideas

## Candidate 1 — How can a single test verify three wildly different backends work identically?
- Source: `examples/session-stores/README.md` (lines 35–45, conformance section)
- Topic: Protocol-driven conformance testing across heterogeneous storage backends
- Hook: You have S3 part-file listings, Redis RPUSH lists, and Postgres JSONB inserts — all claiming to implement the same SessionStore contract.
- Key case: The conformance suite in `shared/conformance.ts` defines 13 behavioral tests. You call `runSessionStoreConformance()` with a factory function that returns a fresh store. All three adapters pass all 13 tests without adapter-specific test code.
- The Question: If three backends have radically different consistency models and data structures, how does one test suite verify they all satisfy the same contract?
- Core idea: The conformance suite is protocol-driven, not implementation-driven. It only tests the boundary behavior (append entries, load in order, resume by ID) without caring how the backend accomplishes it. S3 uses object keys, Redis uses list operations, Postgres uses ordered inserts — invisible to the test.
- Visual object: Three architectural diagrams (S3 prefix tree, Redis key scheme, Postgres schema) visually collapsing into a unified "SessionStore contract" interface
- Manim move: collapse
- Example seed: The suite calls `store.append([{role: 'user', text: 'hello'}])`, then `load()` and asserts deep-equality. For S3, this writes a JSONL part file and lists it. For Redis, it's `RPUSH` then `LRANGE`. For Postgres, it's `INSERT` then `SELECT`. Three implementations, one protocol gate.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: polymorphism, protocol-based design, storage systems
- Exclusions: skip Redis Cluster setup, omit Minio local testing details, don't implement a new backend
- Score: 8/10

## Candidate 2 — What breaks when your file ordering depends on a client's wall clock?
- Source: `examples/session-stores/README.md` (lines 177–183, S3 production checklist)
- Topic: Distributed ordering via client-side timestamps in S3 multi-part uploads
- Hook: Session transcripts in S3 are split across JSONL part files named by epoch-millisecond + random suffix. Resume reads them in filename sort order. Latency variations and clock skew can swap the order.
- Key case: Turn 1 appends two part files seconds apart: `part-1720000000500-xx5kd2.jsonl` (10:00:00.500) then `part-1720000002100-yy7nb9.jsonl` (10:00:02.100). If the writer's clock drifts backward between writes, a third file at 10:00:01.800 would insert in the middle when sorted, breaking turn replay.
- The Question: If transcript ordering relies on client-side timestamps in filenames, and the file system sorts by name, what happens when the writer's clock is inaccurate or jumps?
- Core idea: Filename-based ordering is implicit ordering. The session assumes filename lexicographic sort equals append order. Clock skew >1 second between writes breaks this assumption silently — the resume mechanism loads turns out of order without error.
- Visual object: A timeline diagram showing part-file writes with wall-clock time above and filename timestamp below, arrows crossing when clock skew occurs
- Manim move: scan (through sorted filenames), then transform (reorder them to match clock skew)
- Example seed: Session "abc123": Turn 1 Part A at 10:00:00.500 (file sorts first). Turn 1 Part B written at 10:00:02.100 (file sorts second). Clock jumps backward; Part C written at 10:00:01.800 — now file sorts *between* A and B, so resume replays `[A, C, B]` instead of `[A, B, C]`.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: distributed systems, timestamp ordering, S3 eventual consistency
- Exclusions: don't cover NTP sync internals, skip S3 pricing, omit IAM permission details
- Score: 7/10

## Candidate 3 — Does field reordering in storage break deep equality checks?
- Source: `examples/session-stores/README.md` (lines 250–256, JSONB key ordering section)
- Topic: Structural equality semantics vs byte equality in serialized data
- Hook: Postgres JSONB reorders object keys on read-back. Your SDK stores `{created: '2026-07-15', msg: 'hi'}` and gets back `{msg: 'hi', created: '2026-07-15'}`. Does resume fail?
- Key case: Append entry `{created: '2026-07-15', msg: 'hi', role: 'user'}`. First load returns it in original order. Later session loads the same row and Postgres returns keys alphabetically sorted: `{created: '2026-07-15', msg: 'hi', role: 'user'}`. Are these equal?
- The Question: If a storage backend reorders fields in serialized data, does the resume mechanism still work?
- Core idea: The SessionStore contract specifies deep-equal (value equality), not byte-equal (byte-for-byte identity). JSONB satisfies the contract by preserving values while reordering keys. Code respecting the contract (the SDK) passes; code that byte-compares fails silently.
- Visual object: A single JSON entry displayed twice with keys in different orders, values highlighted in matching colors to show structural equivalence
- Manim move: transform
- Example seed: Append `{created: '2026-07-15', msg: 'hi', role: 'user'}`. Load 1 returns same order (happens to match). Load 2 returns `{created: '2026-07-15', msg: 'hi', role: 'user'}` with alphabetic sorting. Deep-equal says they're identical; naive byte-compare says they diverged.
- Length band: ~1 min
- Still lanes: c2v, raster
- Prerequisites: Postgres JSONB, equality semantics
- Exclusions: skip JSONB performance vs JSON, omit JSON Schema validation, don't cover PostgreSQL internals
- Score: 6/10

## Candidate 4 — How do you unit-test a backend when you can't mock it locally?
- Source: `examples/session-stores/README.md` (lines 23–28 layout, 117–125 Postgres live-only)
- Topic: Test infrastructure trade-offs between local testability and CI coverage
- Hook: S3 and Redis have in-process mocks; Postgres does not. Tests for Postgres skip silently if the URL env var is unset. Developers without local Postgres can't run Postgres tests, but CI can.
- Key case: Developer A runs `npm test` in the S3 directory; mock tests pass immediately. Developer B runs `npm test` in the Postgres directory; tests skip with "SESSION_STORE_POSTGRES_URL not set." Both work fine locally, but CI runs live Postgres tests when the env var is configured.
- The Question: If a backend has no in-process mock, how do you ensure unit tests run in CI without requiring every developer to provision local infrastructure?
- Core idea: Conditional test gating by environment variable. Tests marked `env-gated` skip silently when the backend URL is absent. This trades developer-local testability for CI coverage — the promise is "developers get fast local unit tests; CI gets full conformance with real backends."
- Visual object: A test-run matrix showing three backends (S3, Redis, Postgres) with columns for "Dev (mock)" and "CI (live)" and rows indicating pass/skip
- Manim move: split (test suite splitting into mock and live branches)
- Example seed: Dev runs `npm test` and Postgres tests skip (`skipped: SESSION_STORE_POSTGRES_URL not set`). CI runs with URL set; live Postgres tests run and pass. S3 and Redis always run mock tests, skipping the conditional gate.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: CI/CD, test fixtures, local dev trade-offs
- Exclusions: skip Docker setup tutorials, omit GitHub Actions syntax, don't cover cost optimization
- Score: 6/10

## Candidate 05 — Why does tracking "what's running" break the moment you miss one event?
- Source: `CHANGELOG.md` (0.3.203 entry)
- Topic: Level-triggered vs edge-triggered state delivery for background task tracking
- Hook: A background workflow fires `task_started` and `task_notification` events. Miss one delta and your consumer's task list drifts permanently from reality — with no error and no recovery path.
- Key case: A consumer tracks background tasks by accumulating `task_started` events and removing finished ones on `task_notification`. One `task_started` is dropped mid-queue. The consumer now permanently undercounts live tasks. The `background_tasks_changed` event was added to replace this pattern: it emits the complete current membership set on every change.
- The Question: Edge events are smaller and only send what changed; so why does the SDK replace them with a full-set emission on every membership change?
- Core idea: Level-triggered delivery makes the receiver's state a simple "latest message wins" problem. A dropped delivery means "stale for a moment," not "permanently wrong." Edge delivery is efficient per message but fragile over time — one lost delta permanently corrupts any consumer that doesn't have a resync mechanism. Level delivery is redundant but idempotent.
- Visual object: Two side-by-side timelines — edge stream with one event dropped (consumer diverges and never recovers) vs level stream with one event dropped (consumer is stale for one interval, then snaps back on the next emission)
- Manim move: accumulate (state building from edge deltas, then diverging after a dropped event), then slosh (level signal overwriting consumer state on each delivery, recovering automatically)
- Example seed: Tasks A, B, C start sequentially. `task_started(A)` and `task_started(B)` arrive; `task_started(C)` is dropped. Edge consumer: {A, B} — permanently wrong. Level consumer receives `background_tasks_changed([A,B,C])`, then the next emission is also dropped, then `background_tasks_changed([A,B])` arrives when C finishes — consumer is always correct after any non-dropped message.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: event streams, idempotency, distributed systems basics
- Exclusions: skip WebSocket transport internals, don't cover task scheduling APIs, omit background workflow step sequencing
- Score: 8/10

## Candidate 06 — When a subagent needs file-write permission, who in the agent tree answers?
- Source: `CHANGELOG.md` (0.3.186 entry)
- Topic: Permission request routing from background subagent to parent session callback
- Hook: A background subagent tries to write a file. Before v0.3.186, the SDK auto-denied the tool call silently. After: the permission prompt rises to the parent session's `canUseTool` callback, tagged with `agent_id` identifying which subagent asked.
- Key case: An orchestrator spawns a background file-refactoring subagent. The subagent calls `Write`. The SDK constructs a `can_use_tool` control request stamped with `agent_id: 'refactor-agent'` and delivers it to the parent session's `canUseTool` callback. The callback inspects `agent_id`, returns `{behavior: 'allow'}`, and the write executes. Without the routing, auto-deny fires and the subagent stalls with no explanation.
- The Question: A subagent runs in a separate process scope with no `canUseTool` handler registered — so how does a tool-use permission decision reach anyone with the authority to grant it?
- Core idea: The control protocol carries `agent_id` on every `can_use_tool` request and routes it to the nearest registered handler in the parent session. The parent receives the identical callback structure it uses for its own tool calls, plus `agent_id` to identify the source. The subagent's stdin stays open during the round-trip, blocking its execution until the parent responds.
- Visual object: A two-node agent tree with a dashed permission-request arrow rising from the subagent node to the parent's `canUseTool` handler, and a solid approval arrow descending back; the subagent node shows a "waiting" indicator while the arrow is in flight
- Manim move: trace (arrow rising from subagent to parent, response descending, subagent unblocking)
- Example seed: Parent: `canUseTool: (req) => req.agent_id === 'refactor-agent' ? {behavior:'allow'} : {behavior:'deny'}`. Subagent calls `Write('/src/foo.ts', '...')`. SDK tags the request with `agent_id: 'refactor-agent'`. Parent callback returns allow. Write executes. Same scenario without `agent_id` routing: auto-deny, subagent never writes.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: agent trees, callback patterns, tool-use lifecycle
- Exclusions: skip MCP server permission models, omit sandbox credential injection, don't cover `bypassPermissions` flag or `allowedTools` shadowing
- Score: 7/10
