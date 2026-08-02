# Claude SDK for Python Video Ideas

## Candidate 1 — Why tool execution must automatically loop until the model stops calling them

- Source: `tools.md`
- Topic: Automatic tool orchestration feedback loop
- Hook: The model calls a tool, you run it, feed the result back—but how does this keep iterating and know when to stop?
- Key case: `tool_runner()` iterates through API calls; each iteration checks for `tool_use` blocks, executes them, re-prompts the model, and stops only when no tool calls appear
- The Question: If tool calls trigger re-prompts automatically, what condition makes the iteration terminate, and what prevents infinite loops?
- Core idea: Each iteration yields a `BetaMessage`; the runner peeks at content blocks to detect `tool_use`, executes the matching tool, appends `tool_result` to messages, and re-prompts. When the model output has no `tool_use` blocks, iteration stops. The model itself controls termination by choosing not to call a tool.
- Visual object: A circular flow diagram: `user message` → `model response` → `check for tool_use` → `execute tool` → `append tool_result` → `re-prompt model` → loop back or exit
- Manim move: accumulate (each iteration adds a message pair) or trace (following the loop path)
- Example seed: User asks "What is 9 + 10?" → model calls `sum(9, 10)` → runner executes, gets "19" → runner re-prompts → model outputs "The answer is 19." with no tool calls → runner stops
- Length band: 2–3 min
- Still lanes: c2v (code to visual), raster (loop diagram)
- Prerequisites: understanding of tool definitions, basic API message flow
- Exclusions: detailed tool schema extraction, error handling paths, async variants
- Score: 9/10

## Candidate 2 — Why streaming must accumulate while yielding, so you get both speed and completeness

- Source: `helpers.md` (Streaming Responses section)
- Topic: Dual-output streaming: immediate text and final structured message
- Hook: If you stream text character-by-character for responsiveness, how do you also get a fully-structured `Message` object at the end?
- Key case: `MessageStreamManager` context manager yields a `MessageStream` that lets you iterate `.text_stream` (text deltas only), but also call `get_final_message()` after the context exits to retrieve the accumulated `Message` with all metadata
- The Question: How can the stream emit events immediately AND accumulate them into a complete object without buffering the entire response first?
- Core idea: The stream internally buffers all events while yielding them. Lenses like `.text_stream` filter on-the-fly for rapid iteration; the context manager keeps a side accumulator that reconstructs the `Message` structure from raw events after iteration completes.
- Visual object: Two parallel flows: one stream of text-delta events (→ immediate output), one accumulating buffer (→ final Message object)
- Manim move: split (events fork into text-stream and accumulator), or slosh (alternating consumption and buildup)
- Example seed: Streaming "Hello there!" yields "H", "e", "l", "l", "o" as separate events to `.text_stream`; after loop exits, `get_final_message()` returns a Message with full `content[0].text = "Hello there!"` and token counts
- Length band: 2–3 min
- Still lanes: c2v (code flow), raster (timeline of events vs. final state)
- Prerequisites: familiarity with async/await, context managers, basic Message structure
- Exclusions: token counting, event type taxonomy, cancellation mechanics
- Score: 8/10

## Candidate 3 — Why the tool decorator must parse docstrings to generate schema, not infer it blindly

- Source: `tools.md` (Tool decorator section)
- Topic: Docstring-driven schema extraction
- Hook: A Python function's signature tells you types, but how do you extract human-readable descriptions without writing schema twice?
- Key case: `@beta_tool` decorator parses the docstring's `Args:` and `Returns:` blocks alongside the function signature to build the JSON schema's `description` and `properties[...].description` fields
- The Question: If the decorator reads the function signature alone, why is the docstring required, and what breaks if it's malformed?
- Core idea: Function signature (types, parameter names) is machine-readable; docstring (prose descriptions) is human-readable. The decorator extracts both, merging them into a schema where `title`, `type`, and `required` come from the signature, but `description` fields come from docstring parsing. Malformed or missing docstrings leave descriptions empty, reducing the model's context for using the tool.
- Visual object: A side-by-side code-to-JSON transformation: function + docstring on left, structured schema on right, with arrows mapping each docstring block to a schema field
- Manim move: morph (function text becomes JSON structure) or split (signature and docstring fork into separate schema branches)
- Example seed: `sum(left: int, right: int)` with docstring describing each arg → `{"name": "sum", "input_schema": {"properties": {"left": {"description": "The first integer...", "type": "integer"}, "right": {...}}}}`
- Length band: 2–3 min
- Still lanes: c2v (code and docstring to JSON schema)
- Prerequisites: understanding of Python docstrings, JSON schema structure, decorator basics
- Exclusions: implementation of docstring regex, handling of complex types (Union, Optional), custom schema overrides
- Score: 8/10

## Candidate 4 — Why tool errors can include images, so the model sees both failure text and visual proof

- Source: `tools.md` (ToolError section)
- Topic: Content-block error responses
- Hook: When a tool fails (e.g., a screenshot fails to load), returning just text loses the context—how can you show the model what actually happened?
- Key case: `ToolError([{"type": "text", "text": "Failed to load page: …"}, {"type": "image", "source": {…, "data": result.screenshot}}])` packages both error text and the actual failure screenshot, which the model then sees as a tool result
- The Question: Why does `ToolError` accept a content-block array instead of just a string, and what changes in how the model reacts when it sees the image?
- Core idea: Plain exceptions send only `repr()` text to the model; `ToolError` accepts a list of content blocks (text, image, etc.), allowing the tool author to annotate the failure with visual evidence. The model receives both the error narrative and the proof, enabling better recovery strategies.
- Visual object: A tool result block containing both text ("Failed to load") and an image (the broken page screenshot), displayed side-by-side to the model
- Manim move: combine (text + image fuse into one result), or spread (error breaks into multiple content blocks)
- Example seed: `take_screenshot("https://invalid-url.com")` fails → `ToolError` returns text "Failed to load page" plus the screenshot showing a 404 page → model sees both and decides to retry with a corrected URL
- Length band: ~1 min
- Still lanes: raster (before/after: plain error vs. content-block error)
- Prerequisites: understanding of tool results, content blocks, error handling patterns
- Exclusions: plain exception handling, logging behavior, error recovery strategies
- Score: 8/10

## Candidate 5 — Why MCP type conversion is a separate layer, and what fails when a conversion isn't possible

- Source: `helpers.md` (MCP Helpers section)
- Topic: Protocol bridging through explicit conversions
- Hook: MCP servers speak a different protocol than the Claude API; how do you translate resources, tools, and prompts between them without losing data?
- Key case: `mcp_tool()`, `mcp_message()`, `mcp_resource_to_content()`, etc. are dedicated conversion functions that map MCP types to Anthropic types; if an MCP value cannot be converted (e.g., unsupported content type like audio), they raise `UnsupportedMCPValueError`
- The Question: Why are conversions explicit functions rather than automatic type coercion, and what happens when you encounter an unsupported MCP value?
- Core idea: MCP and Anthropic API have overlapping but non-identical type systems. Explicit converter functions make type mapping visible and testable. When a conversion is impossible (e.g., MCP resource with MIME type audio, which Claude API doesn't support in this context), the error is raised early so the developer can decide to drop it, transform it differently, or fail gracefully. This prevents silent data loss.
- Visual object: Two protocol bubbles (MCP ↔ Anthropic) with converters bridging them; an arrow hitting a barrier represents unsupported types
- Manim move: transform (MCP resource becomes Anthropic content block), or split (successful conversions vs. errors)
- Example seed: MCP server exposes a text file at `file:///data.json`; `mcp_resource_to_content()` reads it and returns `{"type": "text", "text": "..."}` for the Claude API. If it were an audio file, the converter raises `UnsupportedMCPValueError` instead.
- Length band: ~1 min
- Still lanes: c2v (protocol-to-protocol translation)
- Prerequisites: basic familiarity with MCP concept, Claude API content types
- Exclusions: MCP server setup, detailed type taxonomy, workarounds for unsupported types
- Score: 7/10

Scanning the corpus for motion-carrying concepts not yet covered by the five existing candidates.

# Claude SDK for Python Video Ideas

## Candidate 06 — Why context compaction returns two representations, and only one survives the next call

- Source: `tests/lib/streaming/fixtures/compaction_response.txt`
- Topic: Streaming context compaction — readable summary vs. opaque encrypted token
- Hook: When conversation history overflows, the stream emits a compaction block with both a human-readable summary and an encrypted blob — but only one of them carries the context forward.
- Key case: A `compaction_delta` event fires mid-stream carrying `content: "Earlier conversation summarized."` (plain text) alongside `encrypted_content: "EpwBCioIDxgC..."` (opaque payload); the developer must thread the encrypted blob back into the next call's message history, not the readable text
- The Question: If the readable `content` is what the model "remembered," why does passing it back instead of `encrypted_content` break context continuity?
- Core idea: The readable `content` is for display and debugging only. The `encrypted_content` is a server-verifiable token that reconstructs full compressed context — turn boundaries, roles, metadata — without re-sending the entire message list. Plain text loses the structural information the API needs; the encrypted form preserves it in a format the server can decode but the developer cannot inspect.
- Visual object: A long message-list stack collapsing into one compaction block with two outputs: an open speech-bubble (readable summary) and a sealed opaque box (encrypted token) — only the box feeds the next API call
- Manim move: collapse (many messages fold into one compaction block) then split (block yields two artifacts with different fates)
- Example seed: 20-turn conversation → compaction fires → `compaction_delta` yields `content: "User asked about math; assistant explained addition."` and `encrypted_content: "Epw..."` → developer stores both; next call passes `encrypted_content` only → API reconstructs full context from token rather than 20-message payload
- Length band: 2–3 min
- Still lanes: raster (long message list vs. single compaction block), c2v (delta event → two stored values with distinct uses)
- Prerequisites: streaming basics, message history format, content block accumulation
- Exclusions: triggering threshold details, encryption algorithm, manual compaction control APIs
- Score: 7/10
