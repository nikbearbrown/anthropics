# anthropic-tools Video Ideas

## Candidate 1 — Schema shapes Claude's SQL generation

- Source: `tool_use_package/EXAMPLES.md`
- Topic: Customizing tool prompts to inject constraints
- Hook: Claude must generate SQL queries without knowing the table schema — how does it avoid hallucinating column names?
- Key case: SQLTool overrides `format_tool_for_claude()` to embed `db_schema` and `db_dialect` directly into how the tool appears in Claude's instructions
- The Question: If Claude doesn't see the database schema before generating queries, won't it invent tables and columns that don't exist?
- Core idea: The `format_tool_for_claude()` method lets tools customize their system-prompt description. The SQL tool uses this to inject schema upfront, so Claude generates only syntactically valid queries against real columns.
- Visual object: The database schema (e.g., `CREATE TABLE employees (id INTEGER, name TEXT, department TEXT)`) embedded as part of the tool definition, acting as a generative constraint
- Manim move: morph
- Example seed: SQLTool describes a table with columns `id`, `name`, `department`. User asks "which employee is in Sales?" — Claude correctly queries the `department` column because the schema was in the prompt, not because it guessed.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: SQL basics, Python class inheritance
- Exclusions: CRUD loops, transaction handling, connection pooling, performance indexing
- Score: 8/10

## Candidate 2 — Message turns force sequential planning

- Source: `README.md`
- Topic: Why agentic iteration cannot parallelize tool requests
- Hook: Claude decides to call two tools — why does it have to wait for the first result before calling the second?
- Key case: The addition/subtraction example shows `tool_inputs` requesting both tools in one message, but `tool_outputs` must return both results before Claude can proceed
- The Question: If Claude can see all the tool names it needs, why can't it decide its entire plan upfront and request all tools at once?
- Core idea: The message format enforces turn-taking: Claude sends `tool_inputs`, the system executes and returns `tool_outputs`, Claude reads the results and decides its next move. This sequential rhythm prevents planning beyond the current round.
- Visual object: The `messages` list growing with alternating roles — user → assistant → `tool_inputs` → `tool_outputs` → assistant (repeat)
- Manim move: accumulate
- Example seed: "Get time in Los Angeles, then 2 hours later, what time in London?" Claude sends tool_inputs for LA time, receives tool_outputs (3pm), then sends *new* tool_inputs for London time (now knowing 3pm LA = 11pm London)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Understanding of turn-based conversation
- Exclusions: Token limits, reasoning traces, parallel execution, streaming
- Score: 7/10

## Candidate 3 — Abstraction unifies incompatible search sources

- Source: `tool_use_package/EXAMPLES.md`
- Topic: Polymorphic interface hiding source-specific complexity
- Hook: Elasticsearch, Wikipedia, vector databases, and web search have completely different APIs — how can Claude call them identically?
- Key case: `BaseSearchTool` is subclassed into ElasticsearchSearchTool, WikipediaSearchTool, and WebSearchTool; each overrides `raw_search()` and `truncate_page_content()` but Claude sees only the base interface
- The Question: If each source needs different authentication (API keys for Elasticsearch, none for Wikipedia), different query languages, and different result formats, how do you make them transparent to Claude?
- Core idea: `BaseSearchTool` defines a common contract — `raw_search(query, n_results)` and `truncate_page_content()`. Each subclass implements source-specific mechanics behind this interface. Claude always calls `search()` the same way; the framework routes to the right backend invisibly.
- Visual object: An inheritance tree with one base class at the root and four implementations branching outward
- Manim move: transform
- Example seed: Claude asks to "search for neural networks." The framework silently dispatches to ElasticsearchSearchTool (internal papers), VectorDatabaseSearchTool (research), and WikipediaSearchTool (definitions) — all through identical `search()` calls.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Python inheritance, search concepts
- Exclusions: Reranking, fusion, deduplication, hybrid search, embedding generation
- Score: 6/10

## Candidate 04 — The same channel that carries results also carries mistakes

- Source: `README.md`
- Topic: Error messages as self-correction signals inside agentic loops
- Hook: Claude requests a tool with a missing required parameter — the framework can't execute it, so what prevents the conversation from deadlocking?
- Key case: Claude issues `tool_inputs` for `perform_addition` with only `a=9`, omitting required `b`. Instead of crashing or guessing, the system returns a `tool_outputs` message where `tool_outputs=None` and `tool_error='Missing required parameter "b" in tool perform_addition.'` — Claude reads it and reissues the call correctly.
- The Question: If the error path returned something structurally different from the success path, Claude would need two mental models for reading responses — yet it corrects itself seamlessly. Why?
- Core idea: `tool_error` is a field on the same `tool_outputs` message type as successful results, mutually exclusive with `tool_outputs` but using identical turn-taking rhythm. Claude's error-correction loop is architecturally identical to its result-processing loop — no special case, no new channel. The message format's mutual-exclusion constraint (`tool_outputs` xor `tool_error`) is what enforces clean signaling without ambiguity.
- Visual object: Two side-by-side `tool_outputs` message dicts — one with `tool_outputs=[...]` and `tool_error=None`, one with `tool_outputs=None` and `tool_error='Missing required parameter "b"'` — then the corrected `tool_inputs` that follows the error
- Manim move: morph
- Example seed: Claude calls `perform_addition(a=9)`. Framework returns `{tool_outputs: None, tool_error: "Missing required parameter 'b'"}`. Claude's next message: `perform_addition(a=9, b=1)` — correct.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: tool_inputs/tool_outputs message format (Candidate 2)
- Exclusions: Retry limits, exponential backoff, exception handling outside the message loop, Claude's internal reasoning about why it made the mistake
- Score: 8/10
