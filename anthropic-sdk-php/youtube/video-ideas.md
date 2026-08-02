# Claude SDK for PHP Video Ideas

## Candidate 1 — Why JSON can't be parsed mid-fragment, even when it arrives complete in the stream

- Source: `fixtures/ga/tool_use.txt`
- Topic: Assembling tool input from streaming JSON deltas
- Hook: Tool invocation input arrives as tiny fragments: `{"locati`, `on\": \"P`, `ar`, `is\"}` — you can't parse until the last piece lands.
- Key case: Four separate `input_json_delta` events with partial JSON. Each one is syntactically invalid; only the concatenation is valid.
- The Question: Why can't you parse `input_json_delta` as soon as each event arrives?
- Core idea: JSON is a complete syntactic unit; a fragment like `{"locati` is not valid JSON and will fail parsing. The accumulator appends each delta to a buffer and only parses when content_block_stop signals completion.
- Visual object: A JSON buffer growing character by character, each delta appending, colors flashing invalid→valid as the closing brace completes it.
- Manim move: accumulate
- Example seed: Stream sends `input_json_delta("{ \"n")`, then `"ame\"")`, then ` : "Bob"}` — only on the third event can you parse the complete `{"name": "Bob"}`.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: streaming basics, JSON syntax
- Exclusions: SSE framing protocol details, tool_use semantics
- Score: 9/10

## Candidate 2 — How scattered SSE events fold into a coherent message

- Source: `README.md` (MessageAccumulator section), `fixtures/ga/basic_text.txt`, `fixtures/ga/tool_use.txt`
- Topic: Streaming accumulator state machine
- Hook: A single message arrives as 7–8 separate SSE events; the SDK must glue them back together so the response looks like a non-streaming call.
- Key case: Three `content_block_delta` events with text fragments ("Hello", " there", "!"), each updating the same content block until `content_block_stop` signals it's done.
- The Question: Why do streaming responses fragment into so many events instead of sending the whole message at once?
- Core idea: SSE sends updates incrementally so clients can display progress; the SDK re-assembles them by maintaining state across events (text concatenates, tool input JSON accumulates, usage totals merge). `message()` can be called mid-stream for a snapshot of what's arrived so far.
- Visual object: An accumulator state table with columns for each content block, rows showing the state after each event, text growing and usage counters incrementing.
- Manim move: accumulate
- Example seed: Receive message_start (empty), content_block_start (open), text_delta("Hi"), text_delta(" there"), content_block_stop (seal); accumulator state goes `content[0].text=""` → `"Hi"` → `"Hi there"`.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: SSE protocol, message schema
- Exclusions: HTTP streaming transport, PSR-18 details
- Score: 8/10

## Candidate 3 — Request flow through a middleware chain without library modification

- Source: `README.md` (Middleware section)
- Topic: Composable request interception pipeline
- Hook: You want to log every request, cache responses, or inject headers — but you don't want to fork or patch the SDK.
- Key case: A logging middleware inspects the request before sending, logs the URI, calls `$next()` to continue down the chain, inspects the response, logs the status code.
- The Question: How do you insert behavior into a library's HTTP layer without modifying the library itself?
- Core idea: Middleware are callables in a fixed shape: `(RequestInterface, callable $next, ?RequestOptions) → ResponseInterface`. Each middleware calls `$next()` to invoke the rest of the chain (or not, to short-circuit). The SDK traverses this chain on every request, so a middleware can inspect/modify at any point and decide whether to continue, retry, or return early.
- Visual object: A pipeline diagram showing a request entering the left, flowing left-to-right through stacked middleware boxes, with arrows showing `$next()` calls and return paths.
- Manim move: trace
- Example seed: Middleware logs "→ POST /v1/messages", calls `$next($request)`, receives response, logs "← 200", returns response. Next middleware in the chain might cache it.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: PSR-18 (request/response interfaces), closures/callables
- Exclusions: specific use case implementations (logging library, cache backend), RequestOptions details
- Score: 8/10

## Candidate 4 — Metadata arriving after the content it annotates

- Source: `fixtures/ga/citations.txt`, `fixtures/ga/thinking.txt`
- Topic: Out-of-order event assembly in streams
- Hook: Citation metadata (a char location within text) arrives as a *separate event* after the text itself is already complete.
- Key case: Text delta "The grass is green" completes, then a `citations_delta` event says "chars 10–24 of that text are cited from document X."
- The Question: How do you link metadata to content when the metadata arrives after the content block has finished?
- Core idea: Events aren't necessarily in dependency order. The accumulator holds content blocks by index; when a `citations_delta` arrives, it appends to the already-completed text block's citations array, using char indices to denote the span. Similarly, thinking blocks receive text deltas and signature deltas in sequence; all updates accumulate on the same block.
- Visual object: A timeline showing text arriving and completing, then annotation events arriving afterward, each pointing back to the text span they describe.
- Manim move: spread
- Example seed: Text arrives "AI is smart", accumulates to completion. Later, a citations_delta says "chars 0–2 (the word 'AI') came from paper_x.pdf." The accumulator appends this citation to the completed text block.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: streaming, content blocks, indexing
- Exclusions: citation domain semantics, how documents are indexed
- Score: 7/10

## Candidate 05 — Why the server encrypts context you're only going to echo straight back

- Source: `fixtures/beta/compaction_encrypted_content.txt`
- Topic: Server-sealed context compaction tokens
- Hook: After a long conversation, the API returns an encrypted blob you must store but are not allowed to read — your history has collapsed into a tamper-proof token that belongs to the server.
- Key case: A `compaction_delta` carries both `content: "summary text"` (human-readable, for display only) and `encrypted_content: "EpwBCioIDxgC_opaque_payload"` (opaque). Only the encrypted blob travels forward in future requests.
- The Question: The client just echoes the blob back unchanged — so why encrypt it instead of sending the summary as the usable context?
- Core idea: Encryption enforces a trust boundary. The server's compacted representation may be lossy, implementation-specific, or carry internal state the client must not tamper with. By encrypting, the server guarantees integrity: a modified or forged blob will fail to re-inflate. The human-readable `content` is decorative; context continuity lives in `encrypted_content` alone. The client's role is pure storage-and-echo.
- Visual object: A long message thread collapsing into a single sealed envelope icon, then that same envelope slotting unchanged into the next request.
- Manim move: collapse
- Example seed: After 50 exchanges, API returns compaction_delta with content="User asked about PHP, assistant explained closures..." and encrypted_content="Epw...". Client stores the blob. Next request sends the blob verbatim. Server internally re-inflates 50 exchanges from the blob, client never sees them again.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: streaming basics, context windows, content blocks
- Exclusions: specific encryption algorithm or key management, how the server re-inflates context internally, beta API stability caveats
- Score: 9/10

## Candidate 06 — Why stop_reason arrives after the content block has already closed

- Source: `fixtures/ga/refusal.txt`, `fixtures/ga/refusal_mid_text.txt`
- Topic: Content-layer events vs. message-layer events are structurally independent
- Hook: The model starts streaming "I can help with that..." then goes silent — and you still don't know it refused until a completely different event type arrives, after all content blocks have already closed.
- Key case: In `refusal_mid_text.txt`, two text_delta events arrive ("I can help", " with that"), content_block_stop fires, then message_delta delivers stop_reason="refusal" with category="cyber" — the "why" arrives only after all the "what" has already finished.
- The Question: The content block stopped cleanly — why doesn't content_block_stop carry the stop reason instead of requiring a separate message_delta?
- Core idea: Content events (content_block_start/delta/stop) track the lifecycle of individual content blocks. Message events (message_start/delta/stop) track the lifecycle of the entire response. These layers are independent by design: a content block always closes with a neutral stop signal, while message_delta carries outcome metadata — stop_reason, final usage, stop_details — for the response as a whole. The accumulator cannot declare the message complete until message_delta arrives; content_block_stop alone means nothing about the outcome.
- Visual object: Two horizontal timelines — a "content layer" showing blocks opening and closing, a "message layer" showing message_start and message_delta — with a gap illustrating the refusal label appearing only in the lower track, after the upper track has gone quiet.
- Manim move: split
- Example seed: Ask a borderline question. text_delta("Sure,") arrives and accumulates. content_block_stop fires. Accumulator holds content[0].text="Sure,". Then message_delta: stop_reason="refusal", category="cyber". Final assembled message: partial text "Sure," with stop_reason=refusal — a half-response and a refused outcome, reported by different layers.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: streaming basics, content block events, message_delta structure
- Exclusions: specific refusal categories and their policy meanings, how to handle partial content once a refusal is detected
- Score: 8/10
