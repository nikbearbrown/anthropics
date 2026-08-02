# Server Sent Events for [Starlette](https://github.com/encode/starlette) and [FastAPI](https://fastapi.tiangolo.com/) Video Ideas

## Candidate 1 — Infinite generators stop when clients disconnect
- Source: `README.md`
- Topic: Async generator cleanup on client disconnect
- Hook: An infinite `while True:` loop on the server keeps running even after the client closes the connection—until asyncio tells it to stop.
- Key case: User refreshes the browser tab while the server's SSE generator is mid-loop; the socket closes but the generator keeps yielding.
- The Question: How does a graceful shutdown signal reach a generator that's buried inside a coroutine? The client socket and the event loop are separate systems—why doesn't it just leak forever?
- Core idea: When the client disconnects, asyncio propagates a `CancelledError` into the generator's current `await` point; the generator's `try-except` block catches it, runs cleanup code, and re-raises to signal completion.
- Visual object: Stack trace unfurling from socket close → asyncio dispatch → CancelledError landing in the generator's `await asyncio.sleep()` → control flow jumping to the `except` block.
- Manim move: trace
- Example seed: Live activity feed streams user logins and logouts; a user loads the page and immediately closes the tab; the polling generator should stop to avoid database churn.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: asyncio generators, try-except-finally blocks
- Exclusions: general Python exception handling; socket-level connection mechanics
- Score: 7/10

## Candidate 2 — Signal handlers must cancel background SSE tasks to shut down cleanly
- Source: `CHANGELOG.md`, `README.md`
- Topic: Coordinating process shutdown with long-running generators
- Hook: A process with 50 active SSE streams receives SIGTERM; the OS doesn't know how to stop asyncio background tasks, so the process hangs waiting for them.
- Key case: Admin sends `kill` to a uvicorn server with concurrent SSE clients; instead of exiting, it prints "Waiting for background tasks to complete. (CTRL+C to force quit)."
- The Question: How does a Unix signal (SIGTERM) coordinate with Python's asyncio event loop to cancel an unbounded number of running generators that have no explicit timeout?
- Core idea: The library monkeypatches uvicorn's signal handler to intercept shutdown and explicitly cancel every running background task before the process exits; generators receive `CancelledError` and clean up.
- Visual object: Bifurcated timeline: one track showing SIGTERM arriving, task cancellations rippling outward in parallel, then process exit; paired against the baseline (no monkeypatch) where the process hangs indefinitely.
- Manim move: accumulate (tasks being cancelled in a wave) then collapse (process exits)
- Example seed: Real-time notification hub with 60 connected clients; deployment script sends SIGTERM; graceful shutdown takes 0.5 seconds instead of hanging until SIGKILL.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: asyncio task lifecycle, signal handling (SIGTERM/SIGINT), uvicorn execution model
- Exclusions: generic graceful-shutdown patterns; uvicorn's internal signal routing
- Score: 7/10

## Candidate 03 — GZipMiddleware silently kills SSE without raising a single error
- Source: `README.md`
- Topic: Middleware buffering vs. SSE streaming incompatibility
- Hook: Wrapping a Starlette app with GZipMiddleware to save bandwidth causes every SSE endpoint to go silent—no error, no timeout, just events that never arrive.
- Key case: Developer adds GZipMiddleware globally before a demo; the browser's `EventSource` never fires; 50 server-side events accumulate and none reach the client.
- The Question: GZip is a byte-level transformation that should be invisible to higher layers—why does it silently break SSE while leaving ordinary JSON endpoints unaffected?
- Core idea: GZip middleware must accumulate a complete response body before it can compute a valid compressed block and flush; SSE is an unbounded stream with no terminal byte, so the compressor's internal buffer never reaches flush threshold—events are trapped in the compressor indefinitely.
- Visual object: A filling buffer with SSE events queuing on the left, a flush-threshold line on the right that events never cross, while a parallel plain-text lane shows events escaping immediately.
- Manim move: accumulate (events pile into the buffer) then freeze (nothing exits the threshold while the plain lane keeps flowing)
- Example seed: Real-time dashboard streams 5 price ticks per second; GZipMiddleware added; after 10 seconds the buffer holds 50 trapped events and the client chart flatlines. *(illustrative)*
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: HTTP middleware pipeline, response buffering vs. streaming
- Exclusions: GZip algorithm internals; Brotli/deflate alternatives; HTTP chunked transfer encoding mechanics
- Score: 7/10
