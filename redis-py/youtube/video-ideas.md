# redis-py Video Ideas

## Candidate 1 — Parallel execution emerges from ordering-preserving node distribution
- Source: `docs/clustering.rst`
- Topic: Cluster pipeline parallelization
- Hook: A single pipeline.execute() call on a cluster sends commands to multiple nodes in parallel—yet returns results in the original order.
- Key case: Pipeline with SET {a}1=x, SET {b}1=y, GET {a}1, GET {b}1 where {a}1 hashes to node A and {b}1 to node B executes both SET operations concurrently.
- The Question: A synchronous command on a single server executes sequentially; the same synchronous pipeline on a cluster with keys on different nodes—why does execute() run commands in parallel without async syntax?
- Core idea: ClusterPipeline groups buffered commands by destination node, distributes them, collects responses, and preserves input order—a partition-execute-merge pattern invisible to the caller.
- Visual object: Fanout diagram showing pipeline → partition by slot → parallel node execution → merge-and-order results.
- Manim move: split|accumulate
- Example seed: pipe.set('user:10:name', 'alice').set('user:20:name', 'bob').get('user:10:name').get('user:20:name').execute() where user:10 and user:20 hash to different nodes.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: understanding of Redis Cluster slot routing, pipelines
- Exclusions: transaction=False caveat, non-atomic multikey operations
- Score: 10/10

## Candidate 2 — Buffering trades latency for throughput
- Source: `docs/advanced_features.rst`
- Topic: Pipeline command batching
- Hook: Sending 100 Redis commands one-by-one means 100 round trips; a pipeline compresses this to 1—why is batching so powerful?
- Key case: Setting foo, bar, blee in 3 separate calls vs piping all three and executing once; the latter eliminates wait-for-response delays.
- The Question: Network round-trip latency dominates single-command performance; buffering trades client-side latency for server throughput; what accumulates in the buffer that makes this trade-off worthwhile?
- Core idea: Pipeline accumulates commands in client memory, then execute() sends the entire batch in one write and reads one response block—reducing TCP round-trips from N to 1.
- Visual object: Timeline showing three separate command→response cycles collapsed into one send-all→receive-all cycle.
- Manim move: accumulate|collapse
- Example seed: pipe.set('a', 1).set('b', 2).set('c', 3).execute() returns [True, True, True] from a single round trip.
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: basic understanding of TCP latency
- Exclusions: transaction=False, error handling on partial pipeline failure
- Score: 9/10

## Candidate 3 — Optimistic locking via watch-then-retry
- Source: `docs/advanced_features.rst`
- Topic: WATCH-MULTI-EXEC retry loop
- Hook: You want to read a value, modify it, and write it back atomically—without an INCR command. But between reading and writing, another client might change it. How do you detect and recover?
- Key case: Implement client-side INCR by GET-then-SET; another client changes the key after your GET but before your SET, and you don't know until you execute.
- The Question: A synchronous read-modify-write in client code has a race window; you can't make it atomic with a lock; how does WATCH detect collision and trigger retry without deadlock?
- Core idea: WATCH records key versions at read time; EXEC verifies no watched key changed before committing; if any changed, WatchError is raised, and the retry loop re-executes the read-check-write sequence.
- Visual object: Timeline with WATCH → GET → [external write by other client] → EXEC → WatchError → retry arrow looping back.
- Manim move: trace|loop
- Example seed: r.pipeline() → watch('counter') → get('counter') → compute next → multi() → set('counter', next) → execute() → catch WatchError → loop.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: understanding of pipelines, race conditions, atomicity
- Exclusions: explicit lock() command, deadlock scenarios, multi-key WATCH
- Score: 8/10

## Candidate 4 — Reuse compresses connection overhead
- Source: `docs/advanced_features.rst`
- Topic: Connection pool lifecycle
- Hook: Creating a TCP socket and handshaking with Redis is slow. Connection pools avoid this by issuing idle sockets on demand and returning them for reuse. How does returning a connection make it instantly available for the next command?
- Key case: 100 commands but only 8 connections in the pool; the pool never creates new sockets—it issues connection A, runs command, returns it, then immediately issues it again for the next command.
- The Question: A new socket for each command would be slow; reusing sockets is fast; but if a socket is busy executing command 1, how can it run command 2 at the same time?
- Core idea: Command execution is synchronous and completes; when it finishes, the socket returns to the pool idle state, ready for the next waiter—a simple queue-and-reuse pattern.
- Visual object: Pool as a queue: [idle conn 1, idle conn 2, …] → issue → execute → return to idle → issue again.
- Manim move: accumulate|distribute
- Example seed: Pool of 3 connections handles 10 sequential commands; each command borrows a connection, returns it, and the next command reuses it.
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: understanding of connection setup cost
- Exclusions: SELECT statement threading caveat, pool configuration tuning, connection timeouts
- Score: 8/10

## Candidate 5 — Hash routing fragments multi-key commands
- Source: `docs/clustering.rst`
- Topic: Cluster key-slot routing and multi-key constraints
- Hook: A command like mset(foo1, val1, foo2, val2) works fine on a single server but fails on a cluster—you changed nothing. Why does the same code behave differently?
- Key case: mset({foo}1: 'a', {foo}2: 'b') succeeds (both keys hash to the same slot); mset(foo1: 'a', foo2: 'b') fails or gets split (keys hash to different slots).
- The Question: Multi-key operations assume atomicity; clusters partition data by key-slot; what determines whether a command touches one node or many, and why does "many" break atomicity?
- Core idea: Keys hash via CRC16 to one of 16384 slots; each slot lives on one primary node; commands with keys on different slots must either be rejected (atomic) or partitioned and sent separately (non-atomic).
- Visual object: Ring diagram of 16384 slots with keys highlighted showing which slot each hashes to; multi-key commands that span slots are marked as split or invalid.
- Manim move: transform|split
- Example seed: mset({x}1: 'a', {x}2: 'b') both go to slot N (atomic); mset(x1: 'a', z1: 'b') go to different slots (requires mset_nonatomic).
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: understanding of consistent hashing, cluster partitioning
- Exclusions: hash tag edge cases, ASKING redirect, slot migration
- Score: 8/10

## Candidate 06 — One publish returns 2: pattern subscriptions create a shadow delivery channel
- Source: `docs/advanced_features.rst`
- Topic: PubSub fan-out with pattern matching
- Hook: A single `publish()` call returns 2—but you only sent one message. Who received the extra copy, and why does it count separately?
- Key case: Client subscribes to `'my-first-channel'` and pattern-subscribes to `'my-*'`; `r.publish('my-first-channel', 'some data')` returns 2 and the subscriber receives two distinct messages: one `'message'` type and one `'pmessage'` type.
- The Question: One publish should reach one subscriber; the return value reports 2; why does a pattern subscription generate a second, independent delivery rather than matching the existing one?
- Core idea: Redis maintains two separate index structures—a channel map and a pattern list; PUBLISH walks both independently and delivers to every match, incrementing the count per delivery; pattern and channel subscriptions are never deduplicated even for the same underlying connection.
- Visual object: Forked delivery tree: one PUBLISH arrow splits into a channel branch and a pattern branch, each terminating in a distinct message envelope (`type: message` vs `type: pmessage`).
- Manim move: split|spread
- Example seed: `p.subscribe('news'); p.psubscribe('new*'); r.publish('news', 'hello')` → returns 2; `p.get_message()` yields `{'type': 'message', 'channel': b'news', 'data': b'hello'}` then `{'type': 'pmessage', 'pattern': b'new*', 'data': b'hello'}`.
- Length band: ~1 min
- Still lanes: c2v, raster
- Prerequisites: basic publish/subscribe model
- Exclusions: cluster PubSub node pinning, unsubscribe flow, pattern syntax edge cases
- Score: 7/10

## Candidate 07 — Scripts travel as 40-character hashes until Redis forgets them
- Source: `docs/lua_scripting.rst`
- Topic: Lua script SHA caching with NOSCRIPT fallback
- Hook: After `register_script()`, redis-py never sends your Lua source code to Redis again—just its SHA1 hash. But Redis can flush its script cache, making the hash meaningless. What happens next?
- Key case: After `r.script_flush()` empties the server cache, the first call to a registered Script sends `EVALSHA <sha>`, receives a `NOSCRIPT` error, silently executes `SCRIPT LOAD <code>` to re-cache it, then retries `EVALSHA`—all before returning the result.
- The Question: Sending only a hash should permanently fail once the server cache is cleared; it does fail; yet the call succeeds—what intercepts the error and restores the cached state?
- Core idea: `Script.__call__` wraps `EVALSHA` in a try/except: on `NOSCRIPT`, it falls back to `SCRIPT LOAD` (which caches the Lua source and returns the SHA on all nodes), then retries `EVALSHA`—a lazy-load where the error itself is the cache-miss signal.
- Visual object: Decision diamond: `EVALSHA` → `NOSCRIPT?` → yes: `SCRIPT LOAD` → `EVALSHA` → success; no: success immediately.
- Manim move: trace|morph
- Example seed: `multiply = r.register_script(lua); r.script_flush(); multiply(keys=['foo'], args=[5])` → internally: `EVALSHA` fails → `LOAD` re-caches → `EVALSHA` returns `10`.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: SHA1 hashing concept, basic Redis command round-trip
- Exclusions: EVALSHA vs EVAL performance comparison, Lua syntax, cluster scripting limitations (SCRIPT EXISTS AND-reduction)
- Score: 7/10
