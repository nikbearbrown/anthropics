# Claude for Foundation Models Video Ideas

## Candidate 1 — Why does the credential location change between development and production?
- Source: `README.md` (Authentication section)
- Topic: Credential placement across the API bridge lifecycle
- Hook: An app bundles the API key during development, but shipping an app with an extractable key is a critical threat—so production forces the credential behind a backend proxy or awaiting a platform attestation mode, requiring completely different request handling.
- Key case: You write `auth: .apiKey("...")` to ship a prototype, then realize before release that the key is extractable from the binary and must move server-side via `auth: .proxied(headers: [...])`, forcing a relay backend into the architecture.
- The Question: Why can't one credential strategy (e.g., bundled key) work across both development and production?
- Core idea: The threat model determines where the secret lives. A bundled key is extractable by reverse engineering a shipping app; production forces the credential behind a backend boundary (or future platform attestation)—each location requires different request construction and authorization flow.
- Visual object: Three credential positions shown as layers—app binary, backend service, platform infrastructure—with the key moving from left to right as threat surface shrinks.
- Manim move: split
- Example seed: A small weather app. Dev version: `auth: .apiKey("sk-ant-...")` in the source code, works locally. Before App Store release: rewrite to use `auth: .proxied(headers: ["X-App-Token": "..."])`, add a backend relay at `https://yourcompany.com/claude`, which injects the real Anthropic key server-side before forwarding.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: API authentication, threat modeling, microservice architecture
- Exclusions: Token refresh, OAuth, API versioning, other auth mechanisms
- Score: 8/10

## Candidate 2 — Why are partial stream elements cumulative snapshots, not just deltas?
- Source: `README.md` (Streaming section)
- Topic: State accumulation model in incremental response delivery
- Hook: Streaming yields pieces of the response one at a time, but each element is a *full cumulative snapshot* of everything so far—never just the new fragment—forcing the caller to work with growing state without maintaining a buffer.
- Key case: You iterate `for try await partial in stream { print(partial.content) }` and see "Hello", then "Hello world", then "Hello world, how are you"—each print is the complete response up to that point, not `print(delta)`.
- The Question: Why make the caller work with full accumulated state instead of just the new chunk?
- Core idea: Cumulative snapshots eliminate the caller's responsibility to maintain state. The framework owns buffering and concatenation; the caller only receives complete slices, removing off-by-one bugs, reordering problems, and lost fragments.
- Visual object: A poem or message growing in place, with successive iterations shown as nested or layered text, each iteration complete.
- Manim move: accumulate
- Example seed: A chatbot streams a haiku. Iteration 1: "Roses are red". Iteration 2: "Roses are red, violets are blue". Iteration 3: "Roses are red, violets are blue, frameworks are great". The caller prints iteration 3 and sees the whole haiku; it never receives only "frameworks are great".
- Length band: ~1 min
- Still lanes: raster, text overlay
- Prerequisites: Async iteration, streaming basics
- Exclusions: Buffering strategies, chunking protocols, other providers' streaming implementations
- Score: 8/10

## Candidate 3 — Why do framework reasoning levels map to effort levels instead of aligning with them?
- Source: `README.md` (Effort section)
- Topic: Semantic translation between two distinct parameter naming systems
- Hook: Apple's Foundation Models framework uses reasoning hints (`.light`, `.moderate`, `.deep`), but Claude's API uses effort levels (low, medium, high, xhigh, max)—incompatible names and cardinality—so the bridge must translate *and drop unsupported levels silently*.
- Key case: An app requests `.deep` reasoning (framework hint), the bridge maps it to Claude's `high` effort, but if the model only supports `.low` and `.medium`, the effort field is dropped entirely and the request succeeds with Claude's default—the caller never sees that the hint was rejected.
- The Question: Why do two concepts (reasoning intensity and effort level) use different names and cardinality, and why does unsupported effort silently disappear?
- Core idea: The framework abstracts over device-local reasoning; Claude is API-specific with five effort tiers. The bridge maps framework hints to API effort, then silently drops unmapped levels to maintain compatibility—treating reasoning as a hint, not a contract.
- Visual object: Two parallel scales (framework reasoning ↔ Claude effort) showing the mapping relationship and gaps where levels don't align.
- Manim move: transform
- Example seed: A model supports only `.low` and `.high` effort. An app requests `.moderate` reasoning (framework level). The bridge maps `.moderate` → `medium` (Claude level), but `medium` isn't in `[.low, .high]`, so the bridge sends no effort field. The request completes with Claude's default `high`.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: API parameters, bridging patterns, reasoning vs. effort terminology
- Exclusions: Adaptive thinking, model-specific capability sets beyond effort levels
- Score: 7/10

## Candidate 4 — Why does the bridge check capabilities before constructing the request?
- Source: `README.md` (Capabilities section)
- Topic: Capability-gated request field filtering
- Hook: Sending a field that a model doesn't accept is a hard error—so the bridge reads the model's capability declaration first and decides which request fields to *include* before construction, preemptively dropping unsupported fields.
- Key case: Model A declares `capabilities: .init(effortLevels: [.low, .high], structuredOutput: true)`. Code requests `.xhigh` effort. The bridge sees `.xhigh` is not in `[.low, .high]`, drops the field, and sends no effort—the request succeeds without ever hitting the API rejection.
- The Question: Why preemptively filter request fields based on declared capabilities instead of letting the API reject what it doesn't accept?
- Core idea: Capability declaration functions as a schema filter. The bridge treats each model's capabilities as a gate on request fields—unknown or unsupported fields are never sent, making the integration more robust than reactive error handling and avoiding hard failures.
- Visual object: A capability matrix (models × features) with a request template being checked cell-by-cell before sending.
- Manim move: scan
- Example seed: You register a new model with `capabilities: .init(effortLevels: [.low, .high])`. Later, code sets `.medium` effort. The bridge scans the capability matrix, sees `.medium` is not declared, and omits the effort field from the request.
- Length band: 2–3 min
- Still lanes: raster
- Prerequisites: Protocol adaptation, type-driven design, capability models
- Exclusions: Runtime version negotiation, feature detection beyond static capability declaration
- Score: 6/10

The server-side vs. client-side tool round-trip distinction is the one genuinely new motion-carrying concept. No other mechanism in the corpus clears the bar — structured output is schema-convention, `fixedEffort` precedence is too thin, and the coming-soon App Attest mode has no implementable motion yet.

# Claude for Foundation Models Video Ideas

## Candidate 05 — Why does adding web search never call your code, but a custom tool always does?
- Source: `README.md` (Server-side tools section)
- Topic: Single-round-trip execution for infrastructure-bound tools
- Hook: Every tool call looks identical from the model's side — it emits a tool-use block — but server-side tools (web search, code execution) are absorbed inside the API call and never touch the device, while client-side tools exit the request cycle, invoke device code, and require a second API request.
- Key case: An app declares `.webSearch(maxUses: 5)` in `serverTools:` and a Swift `lookupFavorites()` function in the framework's `tools:` array. The model decides to search and then call `lookupFavorites`. Web search: Anthropic's servers execute it, results embed in the response — one request total. `lookupFavorites`: the model emits a tool-use block, the framework calls your function on device, you send the result in a second API request. The session configuration looks symmetric; the latency profiles are not.
- The Question: A tool call should always produce a round-trip through the caller's code; this case did not; why?
- Core idea: Server-side tools need infrastructure the caller cannot provide (web indexes, code sandboxes) — Anthropic runs them within the same API turn. Client-side tools are arbitrary device code only the caller can execute — the framework must exit the request cycle, invoke the function, and re-enter. Round-trip count is determined by who has execution capability, not by how the caller wrote the configuration.
- Visual object: A two-lane timeline — one lane shows a request bubble that closes after the server tool fires inside it; the other shows a request → device callback → second request chain for the client tool.
- Manim move: trace
- Example seed: Model is asked "search Wikipedia for 'osmosis,' then check my saved notes." Web search (server-side): one request completes with results embedded. `checkNotes()` (client-side): model emits tool call, framework calls `checkNotes()` on device, result sent in second API request. Same session, same invocation syntax, two different execution paths.
- Length band: 2–3 min
- Still lanes: raster, c2v
- Prerequisites: Tool calling basics, async request-response cycles, API round-trips
- Exclusions: Domain filtering (`.allowing`, `.blocking`), `maxUses` rate limiting, tool result schema formatting
- Score: 8/10
