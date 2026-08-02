# Claude SDK for Go Video Ideas

## Candidate 1 — Why delegate the loop?
- Source: `tools.md`
- Topic: Tool-use conversation loops
- Hook: Managing multi-turn tool conversations requires tracking state, handling retries, maintaining order—until you abstract it.
- Key case: User asks "What's the weather in Tokyo?"; Claude calls tool; gets result; asks follow-up about humidity; calls tool again; runner handles both rounds invisibly.
- The Question: State tracking and conversation loops are complex; why does caller code stay simple?
- Core idea: The BetaToolRunner iteratively calls Claude, intercepts tool calls, executes them in parallel, accumulates results, and repeats until no more tool calls are requested.
- Visual object: A feedback loop diagram showing request → Claude response → tool extraction → parallel execution → result accumulation → next request.
- Manim move: accumulate
- Example seed: Weather app queries Tokyo, then London, each spawning nested queries for humidity and wind speed; runner manages the multi-level loop invisibly.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: tool use, Claude API basics
- Exclusions: streaming variants, manual message management, managed agents
- Score: 9/10

## Candidate 2 — Deltas into wholes
- Source: `tools.md`, `CHANGELOG.md`
- Topic: Streaming event accumulation by index
- Hook: Streaming sends events as they arrive—one character at a time—but code expects complete blocks, not fragments.
- Key case: Text block streams in as deltas: "The", " weather", " is", " 72°F"; four separate events must merge into one complete text block.
- The Question: How does the SDK reconstruct complete blocks from a delta-only stream without losing or duplicating content?
- Core idea: Each content block is tracked by index; incoming deltas are merged into the indexed slot; the runner emits complete blocks only after accumulation finishes.
- Visual object: A time-indexed table where each row is a content block and successive columns show deltas progressively filling in the text.
- Manim move: accumulate
- Example seed: Real-time weather response streams character-by-character; code reads a single complete text block, not thirty delta events.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: streaming, content blocks
- Exclusions: image streaming, code execution output, beta event compaction
- Score: 8/10

## Candidate 3 — Parallel in order
- Source: `tools.md`
- Topic: Parallel tool execution with result ordering
- Hook: Claude requests three tools at once; run them concurrently for speed—but return results in the original order, not finish order.
- Key case: Claude calls [get_weather(NYC), get_weather(LA), get_temperature(Chicago)] in one message; all three execute in parallel; results return as [NYC, LA, Chicago], not in completion sequence.
- The Question: How do you run requests in parallel without scrambling result order or losing errors from individual executions?
- Core idea: Each tool call is assigned an index; an errgroup executes them concurrently; results are collected into an indexed slice, preserving order regardless of finish time.
- Visual object: Three parallel execution timelines with different durations, all converging to an indexed result array in original sequence.
- Manim move: morph
- Example seed: Weather for three cities runs concurrently; NYC finishes at 2ms, LA at 5ms, Chicago at 3ms; results still arrive as [NYC, LA, Chicago].
- Length band: ~2 min
- Still lanes: c2v
- Prerequisites: tool calls, goroutines
- Exclusions: error handling recovery, context cancellation
- Score: 8/10

## Candidate 4 — Runaway prevention
- Source: `tools.md`
- Topic: Iteration limits as loop safeguards
- Hook: An agentic loop with no limit can spin indefinitely; a single misconfigured tool or model quirk starves resources.
- Key case: Weather tool returns a result that prompts Claude to ask for weather again; without MaxIterations, Claude and tool call each other until timeout or resource exhaustion.
- The Question: How do you prevent infinite tool loops when the model and tools are not under your direct control?
- Core idea: MaxIterations sets a hard cap on API calls; the runner increments a counter on each iteration and halts when the limit is hit, returning the last message.
- Visual object: An iteration counter ticking upward, crossing a configurable threshold, and triggering a stop signal.
- Manim move: accumulate
- Example seed: Recursive weather lookup—city → nearby cities → repeat—stops after five API calls instead of spinning for 500.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: tool runners, agentic loops
- Exclusions: error-driven loops, exponential backoff, rate-limit handling
- Score: 7/10

## Candidate 05 — Why does a tool failure make Claude smarter?
- Source: `tools.md`
- Topic: Tool errors as conversational feedback
- Hook: A tool crash normally ends a workflow—unless the failure itself becomes the next message Claude reads.
- Key case: Weather tool receives empty city string, returns `errors.New("city is required")`; SDK wraps it as `is_error: true` in a `BetaToolResultBlock`; Claude reads the error text and asks the user to clarify instead of halting.
- The Question: Exceptions terminate programs; why does Claude keep reasoning productively after a tool error?
- Core idea: The SDK converts every tool execution error into a `BetaToolResultBlockParam` with `is_error: true` and the error message as content, appended to the conversation exactly like a success result—so Claude sees failure as data to reason about, not a termination signal.
- Visual object: A forking path where one branch shows an unhandled exception crashing a call stack and the other shows the same error wrapped in a message block flowing back into the conversation thread.
- Manim move: transform
- Example seed: Tool returns "city must not be empty"; Claude replies "Could you specify a city?"; user says "Paris"; loop continues to completion.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: tool use, Go error handling basics
- Exclusions: retry policies, exponential backoff, MaxIterations interplay with errors
- Score: 8/10

## Candidate 06 — The hidden goroutine keeping your work alive
- Source: `tools.md`
- Topic: Parallel lease heartbeating in EnvironmentWorker
- Hook: Claiming a work item starts a race: finish before the lease expires—or keep renewing it in parallel while working.
- Key case: EnvironmentWorker claims a work item with a 30-second lease; the session runs a multi-tool agent taking 90 seconds; without a parallel heartbeat goroutine the lease expires at second 30 and another worker steals the item, causing duplicate execution.
- The Question: A session outlasts its lease; how does the SDK prevent duplicate work without blocking session execution?
- Core idea: `EnvironmentWorker` launches a goroutine that fires heartbeat API calls at a fixed interval concurrently with the session loop; when the session finishes, both tracks converge and `force-stop` cleans up—the caller sees a single blocking `worker.Run(ctx)`.
- Visual object: Two parallel horizontal timelines—session execution on top, heartbeat pulses firing on the bottom—both running until session completion triggers force-stop.
- Manim move: trace
- Example seed: Lease renews every 20 seconds; session takes 65 seconds; heartbeat pulses fire at t=20, t=40, t=60; session finishes at t=65; force-stop fires; no duplicate claim.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: goroutines, distributed work queues, lease-based concurrency
- Exclusions: WorkPoller internals, skill download mechanics, EnvironmentKey auth flow
- Score: 7/10
