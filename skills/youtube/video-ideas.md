# Skills Video Ideas

## Candidate 1 — Adaptive thinking allocates reasoning budget to match problem difficulty
- Source: `skills/claude-api/go/claude-api/README.md`
- Topic: Adaptive Thinking in Language Models
- Hook: Why did Claude spend 5000 thinking tokens on "what is 2+2" but 100 on "prove Fermat's Last Theorem"?
- Key case: Simple factual question ("What color is the sky?") vs. complex derivation ("Show me the error in this proof")
- The Question: How do you allocate compute to reasoning? Fixed budget wastes tokens on simple problems; unlimited budget breaks economics.
- Core idea: Claude's adaptive thinking layer decides dynamically whether and how much to think based on input complexity, then executes that decision
- Visual object: A horizontal timeline showing thinking blocks of variable length (short for simple queries, long for complex ones) preceding the final text response
- Manim move: compare
- Example seed: "Fact: a square has 4 sides" (no thinking block shown) vs. "Determine the sum of all prime numbers less than 100" (long thinking block shown, then answer)
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Basic LLM concept
- Exclusions: Internal attention mechanics, token economics, training details
- Score: 9/10

## Candidate 2 — Agent event streaming reveals intermediate work in real-time instead of blocking on final output
- Source: `skills/claude-api/go/managed-agents/README.md`
- Topic: Streaming Agent Progress Events
- Hook: Agent silently processes for 2 minutes, then dumps the final answer—how do you show what it's doing while it thinks?
- Key case: Long-running data analysis: agent querying database → processing results → compiling report (multiple tool calls)
- The Question: How do you avoid blocking the user while long-running operations complete? Wait-for-final-answer causes perceived stalling; showing steps during work keeps users engaged.
- Core idea: Open the event stream before sending the user message; events (tool calls, status changes, agent messages) arrive continuously as the agent processes, not buffered at the end
- Visual object: A vertical timeline of event boxes (AgentToolUseEvent → text block → ToolResultEvent → StatusIdleEvent) unfolding top-to-bottom as time advances
- Manim move: trace
- Example seed: User asks "analyze this CSV", stream shows "StartedProcessing" → "QueryingDatabase" → "Processing10000Rows" → "GeneratingReport" → "Done", each event arriving ~2 seconds apart
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Async streams, agent concept
- Exclusions: SSE protocol details, error recovery, reconnection logic
- Score: 9/10

## Candidate 3 — Prompt caching reuses immutable system context across requests instead of reprocessing
- Source: `skills/claude-api/go/claude-api/README.md`
- Topic: Caching System Prompts in API Calls
- Hook: Your 10k-token system prompt (tools, guidelines, context) runs on every request—how do you not pay for it 100 times?
- Key case: First request processes full system prompt + tools + user query; second request processes same system + different user query
- The Question: How do you avoid reprocessing unchanging context? Re-tokenizing the system block on every call wastes compute; caching it requires knowing where to mark the boundary.
- Core idea: Mark the last system block with a cache-control header; subsequent requests read that block from cache instead of reprocessing
- Visual object: Two request boxes side-by-side; first request fills cache (boundary line drawn), second request reads from cache (cache block highlighted, arrow pointing to hit)
- Manim move: accumulate
- Example seed: System prompt + 100 tools (10000 tokens) cached after Request 1; Requests 2–100 reuse it. Token savings: 990,000 input tokens over 100 calls.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: API request structure, token concept
- Exclusions: Cache invalidation, TTL details, billing math
- Score: 7/10

## Candidate 4 — Agent versions are immutable snapshots; sessions pin to a version so instructions cannot shift mid-conversation
- Source: `skills/claude-api/go/managed-agents/README.md`
- Topic: Immutable Agent Versioning
- Hook: You deploy new agent instructions, but 5 active sessions already started with the old version—who gets the new behavior?
- Key case: AgentID "assist-2" updates from system="math tutor" (v1) to system="code reviewer" (v2) while Sessions A and B are mid-conversation
- The Question: How do you change an agent's behavior without breaking active sessions? Free updates mid-session cause inconsistency; freezing sessions locks users out of improvements.
- Core idea: Agent updates create new immutable versions; sessions permanently pin to a specific (agent ID, version number) pair; new sessions can target new versions
- Visual object: A version tree showing the agent ID trunk splitting into branches v1 and v2, with session A anchored to v1 and session B anchored to v2
- Manim move: split
- Example seed: "assist-2" v1 created (math tutor). Session A starts on v1. Update to v2 (code reviewer). Session A stays on v1, Session B (new) starts on v2. Both run correctly.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Agent concept, session concept
- Exclusions: Migration paths, version deprecation, A/B testing
- Score: 7/10

## Candidate 5 — Refusal fallbacks chain to a secondary model when the primary model declines a request
- Source: `skills/claude-api/go/claude-api/README.md`
- Topic: Model Fallback on Refusal
- Hook: Your primary model refuses the request (safety policy triggered), user gets an error—deploy a fallback model to answer instead?
- Key case: Fable 5 refuses "how to synthesize explosives" on safety grounds; request rerouted to Opus 4.8 which provides educational chemistry context
- The Question: How do you serve a response when the primary model won't? Raw refusal leaves users blocked; unrestricted fallback bypasses safety.
- Core idea: When primary model stops with refusal reason, automatically retry the same request on a secondary (less restrictive or differently trained) model within the same API call
- Visual object: Two sequential model boxes; first (red, labeled "Fable 5") shows refusal stop reason, arrow points to second (green, "Opus 4.8") showing response text
- Manim move: morph
- Example seed: Request denied by Fable 5 with category="bio". Same request silently retried on Opus 4.8, which returns educational answer. User receives response, not error.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: Model refusal concept, fallback concept
- Exclusions: Policy categories, billing for retries, sticky routing
- Score: 6/10

## Candidate 06 — Context compaction lets a long-running agent survive past its own memory limit
- Source: `skills/claude-api/go/claude-api/README.md`
- Topic: Compacting Growing Conversation Context in Long Agent Sessions
- Hook: Your agent has run 50 tool calls and the context window is nearly full—do you truncate and drop history, or compact and keep the gist?
- Key case: A coding agent processes 50 rounds of tool calls across a 2-hour session; context approaches the model's token ceiling mid-task.
- The Question: Context grows monotonically with every message and tool result—how does a long-running agent stay alive without losing the conversation thread? Truncating drops information; unlimited accumulation breaks the model.
- Core idea: Insert a `BetaCompact20260112Edit` directive into the context management config; the model emits a `BetaCompactionBlock` that summarizes removed content, then continues on the compressed context as if it had been there all along.
- Visual object: A vertical stack of content blocks—tool calls, results, assistant turns—accumulating until a compaction boundary fires, then collapsing into a single summary block, with a token counter shown before and after.
- Manim move: collapse
- Example seed: Agent accumulates 50 tool-call rounds (≈ 40,000 tokens). Compaction fires at 80% capacity. All 50 rounds compress into 1 `BetaCompactionBlock` (≈ 2,000 tokens). Round 51 begins with 3,000 tokens of live context instead of hitting the ceiling.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Context window concept, token accumulation
- Exclusions: `ClearToolUses` and `ClearThinking` edit variants, cache/TTL interaction with compaction, billing for compaction tokens
- Score: 8/10
