# Claude Agent SDK for Python Video Ideas

## Candidate 1 — Why would cancelling a query task leave the subprocess running?
- Source: `CHANGELOG.md`
- Topic: Asyncio cancellation and resource cleanup
- Hook: Cancelling a query task appears to stop it, but the subprocess lingers indefinitely.
- Key case: You start a long query, get results, then cancel the task before all cleanup happens. The `claude` process is still there 10 minutes later.
- The Question: I called `asyncio.CancelledError` on my query task; why would the subprocess cleanup code fail to actually kill the process?
- Core idea: Asyncio cancellation can interrupt even finally blocks if they contain await points. Shielding the cleanup code from cancellation ensures `SIGTERM`/`SIGKILL` always fires, even under task cancellation.
- Visual object: Timeline showing task lifetime with cancellation wave — one path shows subprocess orphaned, the other shows it terminating.
- Manim move: trace
- Example seed: Task spawns subprocess at t=0. At t=3, user cancels. Unshielded finally block gets interrupted; subprocess still running at t=10. Shielded finally always completes; subprocess gone by t=3.5.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: asyncio task cancellation, subprocess lifecycle
- Exclusions: asyncio.shield() implementation details, POSIX signal handling
- Score: 10/10

## Candidate 2 — How does a hook intercept Claude's decision before it executes?
- Source: `README.md`
- Topic: Event-driven policy enforcement in the agent loop
- Hook: You need to block Claude from running certain commands, but re-prompting it to ask permission defeats the point.
- Key case: Claude generates a ToolUse for `./foo.sh`, but your security policy forbids it. The hook sees the tool name and input, consults local policy, and says no—Claude never sees the tool succeed.
- The Question: I have a runtime security policy (block foo.sh); why does a hook let me enforce it without changing the prompt or modifying the caller?
- Core idea: Hooks are a feedback loop fired at predefined agent-loop checkpoints (`PreToolUse`, `PostToolUse`, etc.). They give the application (not Claude) a chance to inspect and veto tool use based on context unavailable to Claude.
- Visual object: State diagram of the agent loop with hook injection points labeled and a veto path branching out.
- Manim move: scan
- Example seed: User says "run foo.sh". Claude emits ToolUse(Bash, "foo.sh"). PreToolUse hook fires, pattern-matches against blocklist, returns deny. Claude sees the rejection and says "I cannot run that command."
- Length band: 3–5 min
- Still lanes: geo, c2v
- Prerequisites: Claude agent loop basics, async message handling
- Exclusions: hook execution concurrency, PermissionUpdate type details, matcher syntax
- Score: 9/10

## Candidate 3 — Why would moving tool logic in-process change latency and deployment?
- Source: `README.md`
- Topic: Subprocess I/O overhead vs. direct function calls
- Hook: You have a working external MCP server; migrating it in-process seems simpler, but you're not sure what changes.
- Key case: A calculator tool runs 100 times in a loop. External subprocess serializes 100 JSON packets through stdio; in-process runs 100 function calls. Latency differs by an order of magnitude.
- The Question: I have an external MCP server that works; why would moving the same logic into my Python process matter for performance, debugging, and how I ship code?
- Core idea: External MCP servers communicate via subprocess I/O (fork, stdio, JSON serialization, IPC round-trips). In-process SDK servers bypass all that—direct async function calls, no subprocess lifecycle, no serialization. The tradeoff: isolation lost, but latency and deployment complexity plummet.
- Visual object: Side-by-side stack diagrams—external showing 5 layers (app → CLI → stdio → server parse → tool), in-process showing 2 layers (app → tool).
- Manim move: compare
- Example seed: Tool called 100 times. External: 100 forks, 100 JSON round-trips, ~2 sec. In-process: 100 function calls, ~50 ms. Single deployment unit vs. two.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: MCP protocol basics, process I/O cost intuition
- Exclusions: MCP spec details, thread safety of in-process servers, mixed-server examples
- Score: 8/10

## Candidate 4 — How does a conformance test catch bugs that manual testing misses?
- Source: `examples/session_stores/README.md`
- Topic: Protocol contract validation at scale
- Hook: You write a Redis adapter for SessionStore, manually test read/write, and ship it. Months later, a session corruption bug surfaces—you missed an edge case.
- Key case: Your Redis adapter appends correctly and reads correctly in a simple loop. But `run_session_store_conformance` runs a 13-contract test suite and fails on the concurrent-append contract: you forgot to update the `__sessions` index atomically, so two parallel appends collide.
- The Question: I tested my SessionStore manually and it worked; why does a conformance harness catch bugs my spot-checks never triggered?
- Core idea: The conformance harness systematically exercises 13 behavioral contracts (empty load, concurrent append, deletion, subpath isolation, etc.)—each one a scenario unlikely to occur in manual testing but essential for correctness under real workload patterns.
- Visual object: A test matrix showing all 13 contracts as rows and multiple adapters as columns, with pass/fail markers.
- Manim move: accumulate
- Example seed: Contracts: load-empty, append-once, append-twice, concurrent-append (fails here), delete-all, resume-session, etc. A simple loop tests maybe 3; the harness tests all 13 systematically.
- Length band: 3–5 min
- Still lanes: geo, c2v
- Prerequisites: SessionStore interface concept, property-based testing intuition
- Exclusions: S3/Redis/Postgres implementation details, production checklist items
- Score: 8/10

## Candidate 05 — Why would adding `allowed_tools` make your audit callback invisible?
- Source: `CHANGELOG.md`
- Topic: Permission evaluation short-circuiting in the agent loop
- Hook: You register a callback to audit every tool use, but the audit log stays empty for every pre-approved tool.
- Key case: A security team registers `can_use_tool` to log all Bash invocations, then sets `allowed_tools=["Bash"]` for convenience. Bash runs hundreds of times. The audit log shows zero entries.
- The Question: `can_use_tool` should intercept every tool call; `allowed_tools` only pre-approves a subset — why does adding `allowed_tools` make the callback disappear?
- Core idea: `allowed_tools` is checked first in the permission evaluation chain and causes an early exit, bypassing `can_use_tool` entirely. The two options do not compose — they carry an implicit precedence that silently discards the callback when both are present.
- Visual object: Permission evaluation flowchart with two branches: `allowed_tools` hit → early exit (callback skipped) vs. fall-through → callback fires.
- Manim move: trace
- Example seed: Tool "Bash" is in `allowed_tools`. Three Bash calls fire. `can_use_tool` fires 0 times. Remove `allowed_tools`: `can_use_tool` fires 3 times. Same prompt, same callback, completely different audit coverage.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: basic permission model, callback patterns
- Exclusions: `bypassPermissions` interaction, `permission_mode` evaluation stages, `PermissionUpdate` type internals
- Score: 8/10

## Candidate 06 — Why does a rate-limiter hook fail to block the authorizer hook that fires alongside it?
- Source: `CHANGELOG.md`
- Topic: Parallel hook fan-out vs sequential middleware assumptions
- Hook: Your rate-limiter PreToolUse hook is supposed to block all other hooks when quota is exceeded — but they all fire at the same moment.
- Key case: Three PreToolUse matchers registered: `rate_limiter`, `audit_logger`, `authorizer`. The rate limiter finishes at t=0.1 with a deny; the authorizer finishes at t=0.05 with an allow. The tool runs before the denial lands.
- The Question: I registered three hooks expecting the first to gate the rest; why did the rate limiter fail to block the authorizer?
- Core idea: Hook dispatch within an event fans all matching matchers out concurrently — there is no ordering, sequencing, or short-circuit between matchers on the same event. A gate pattern requires a single hook that internally runs multiple policies, not a chain of separate hooks.
- Visual object: Fork diagram showing one event spawning three parallel hook branches versus the assumed serial chain where each node blocks the next.
- Manim move: split
- Example seed: Event fires at t=0. All three hooks start at t=0. `authorizer` returns allow at t=0.05. Tool executes. `rate_limiter` returns deny at t=0.1 — too late. Collapse to single hook: rate check runs first, blocks the rest.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: hook basics (Candidate 2), concurrent execution model
- Exclusions: hook result merging behavior, hook ordering across distinct event types, `PostToolUse` sequencing
- Score: 8/10

## Candidate 07 — Why does a background-task tracking loop hang when the task already finished?
- Source: `CHANGELOG.md`
- Topic: Dual-channel task completion signaling and tracking-loop correctness
- Hook: You poll for task completion and the loop hangs forever — the task finished two minutes ago on a different message channel.
- Key case: A background agent task completes and the SDK emits a `task_updated` message with a terminal status. The consumer's tracking loop waits only for `TaskNotificationMessage`. That message never arrives. The loop hangs indefinitely.
- The Question: I poll for `TaskNotificationMessage` to detect task completion; why does my loop hang when the task has already finished?
- Core idea: Task terminal state can arrive via two independent message paths: `TaskNotificationMessage` or a `task_updated` message whose `status` is in `TERMINAL_TASK_STATUSES`. A tracker watching only one path misses completions that arrive via the other, causing an indefinite wait.
- Visual object: Message sequence diagram showing a task's lifecycle with two parallel notification channels, one branch the consumer's loop never observes.
- Manim move: trace
- Example seed: Task finishes at t=5. `task_updated` emitted at t=5 (terminal status). `TaskNotificationMessage`: never sent. Tracking loop still waiting at t=60. After fix: `TERMINAL_TASK_STATUSES` check on `task_updated` exits the loop at t=5.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: background task concept, async message polling pattern
- Exclusions: `task_updated` patch-format internals, subagent `session_id` field semantics, `TaskUpdatedStatus` enum values
- Score: 7/10
