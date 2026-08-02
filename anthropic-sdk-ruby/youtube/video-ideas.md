# Claude SDK for Ruby Video Ideas

## Candidate 1 — Streaming responses accumulate state you can access at different times
- Source: `helpers.md`
- Topic: Event accumulation in streaming responses
- Hook: You can iterate text fragments as they arrive, but the final message object only exists after the stream completes — what's accumulating it?
- Key case: `stream.text.each { |text| print(text) }` gives you deltas, but `stream.accumulated_message` blocks until completion and returns a full Message object from the same stream
- The Question: If events stream individually and you consume them one at a time, how is the SDK building a complete Message object behind the scenes, and when is it safe to use?
- Core idea: MessageStream maintains internal state accumulation across events; the object graph is only valid after the final event is consumed
- Visual object: Timeline of events (TextEvent, ContentBlockStopEvent, MessageStopEvent) with a state accumulator bar growing and finalizing
- Manim move: accumulate
- Example seed: Stream receives "Wel" + "com" + "e" as three separate TextEvent payloads; snapshot shows "Wel" → "Welcom" → "Welcome"; at MessageStopEvent, the full Message object materializes with content, usage, and stop_reason populated
- Length band: 2–3 min
- Still lanes: c2v (event timeline), raster (accumulation state)
- Prerequisites: streaming responses, event loop basics, Ruby Enumerable
- Exclusions: HTTP connection lifecycle, backpressure and flow control, error recovery on partial streams
- Score: 7/10

## Candidate 2 — Tool automation hides the request-response loop inside an iterable
- Source: `helpers.md`
- Topic: Progressive abstraction of tool execution loops
- Hook: Manual tool handling exposes a 15-line request-response cycle; the SDK's auto-runner collapses it to one method call — but something must still be looping
- Key case: Manual approach uses `message.stop_reason == :tool_use`, then you build and send a tool_result message; auto-runner uses `client.beta.messages.tool_runner(...).each_message { |m| ... }` and never touches the loop
- The Question: Inside `tool_runner`, what's repeatedly fetching messages and how does the SDK know the conversation is finished without you explicitly checking stop_reason?
- Core idea: Tool runner abstracts the continuation loop — each tool execution automatically triggers a refetch, checks completion, and yields messages as they arrive
- Visual object: Side-by-side flowcharts: left shows explicit request → check stop_reason → execute → build response → request loop; right shows runner yielding messages with tool execution opaque inside
- Manim move: split
- Example seed: Ask calculator "What is 15 times 7?" — manual version calls tool directly and reassembles the message; auto-runner internally calls tool, gets 105, sends back to Claude, then yields the final "The answer is 105" message without you writing continuation logic
- Length band: 2–3 min
- Still lanes: c2v (control flow), diagram (request-response cycle)
- Prerequisites: tool_use, stop_reason, message structure
- Exclusions: input schema definition, BaseTool implementation details, error handling
- Score: 7/10

## Candidate 03 — Ruby's nil means two different things and this schema forces you to pick one
- Source: `helpers.md`
- Topic: Separating field presence from field nullability in BaseModel input schemas
- Hook: In Ruby, a missing hash key and a key set to nil both return nil — but the API server can tell them apart in the JSON body, and BaseModel forces you to say which you meant
- Key case: `required :seat, Anthropic::EnumOf[:window, :aisle], nil?: true` compiles to `"seat": null` in JSON; `optional :bags, Integer` with no value compiles to a key-absent body — same Ruby nil, two different wire representations
- The Question: `hash[:missing_key]` and `hash[:nil_key]` are identical in Ruby; so "optional" and "nilable" should be synonymous — but the 2×2 grid treats them as orthogonal axes. Why?
- Core idea: The distinction is a serialization boundary concern: a missing key and an explicit null serialize differently in JSON, and downstream API behavior may differ; BaseModel captures intent at declaration time so the serializer can translate correctly
- Visual object: 2×2 grid — rows = required/optional, columns = nil-allowed/not-allowed; each cell holds a one-line Ruby declaration and the JSON fragment it produces at the wire boundary
- Manim move: split
- Example seed: Passenger model with one field per cell: `required :name, String` → always `"name":"Alice"`; `required :seat, Enum, nil?: true` → `"seat":null` accepted; `optional :bags, Integer` → key absent from body when omitted; `optional :meal, String, nil?: true` → either key absent or `"meal":null`. Animate the four JSON outputs side by side as each field is filled or left blank.
- Length band: 2–3 min
- Still lanes: c2v (2×2 grid with JSON output per cell), diagram (Ruby value → serialization boundary → JSON wire)
- Prerequisites: JSON schema basics, Ruby hash access
- Exclusions: `ArrayOf`/`HashOf` nil?: true variants, `UnionOf[…, NilClass]` construction, Sorbet/Steep type-checking integration
- Score: 8/10

## Candidate 04 — Streaming events carry two values when you only asked for one
- Source: `helpers.md`
- Topic: Delta-and-snapshot duality inside individual streaming events
- Hook: Every `TextEvent` delivers the tiny fragment just received AND the full accumulated text up to that point — meaning the SDK is doing bookkeeping you never asked for, inside every single event tick
- Key case: A `TextEvent` simultaneously exposes `event.text = " there"` (the arriving delta) and `event.snapshot = "Hello, there"` (everything accumulated so far), both frozen at the same instant in the same object
- The Question: A display consumer only needs deltas to render text as it arrives; a summary consumer only needs the final string — if neither needs both, why does every event carry both, and who is maintaining the running total?
- Core idea: `MessageStream` keeps a mutable accumulator between yields; before each event is emitted, the accumulator absorbs the new delta and then stamps the current snapshot onto the event — so the snapshot is always "delta already applied," making every event independently self-contained without requiring the caller to track state
- Visual object: Two synchronized lanes on a horizontal timeline: the top lane shows arriving deltas one tick at a time; the bottom lane shows the growing accumulated string — both lanes advance together on each event, with a vertical line connecting the pair
- Manim move: trace
- Example seed: Three `TextEvent`s arrive. Tick 1: text=`"Hel"`, snapshot=`"Hel"`. Tick 2: text=`"lo"`, snapshot=`"Hello"`. Tick 3: text=`"!"`, snapshot=`"Hello!"`. Show two subscribers on the same stream: one reading only `.text`, one reading only `.snapshot` — both get consistent answers without sharing any state.
- Length band: 2–3 min
- Still lanes: c2v (dual-lane event timeline), raster (accumulator state at each tick)
- Prerequisites: Ruby Enumerable, streaming basics
- Exclusions: `accumulated_message` and full-message accumulation after stream completes (Candidate 1), `ContentBlockStopEvent`, `MessageStopEvent`, error recovery on partial streams
- Score: 7/10
