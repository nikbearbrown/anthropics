# GitHub MCP Server Video Ideas

## Candidate 1 — Why a generic CLI works with any API

- Source: `cmd/mcpcurl/README.md`
- Topic: Schema-driven command generation
- Hook: A single CLI tool runs against any MCP server without hardcoding its API — how does it adapt?
- Key case: User runs `mcpcurl tools get_issue --owner golang --repo go` against the GitHub server and gets real results, even though mcpcurl has never seen those flags before
- The Question: Schema before capability / X should predict Y: if you have the tool schema, can you generate a fully typed CLI with proper validation? Yes—this one does.
- Core idea: Schema introspection feeds a command builder that generates typed flags, parameter validation, help text, and execution logic automatically
- Visual object: JSON schema document morphing into a CLI help output with --owner, --repo, --issue_number flags appearing as typed options
- Manim move: morph
- Example seed: Imagine a "weather" MCP server exposing `tools/get_temp` with schema `{city: string, units: enum["C","F"]}`. mcpcurl auto-generates `weather tools get_temp --city Seattle --units C` with validation that rejects `--units X`.
- Length band: 2–3 min
- Still lanes: c2v (schema → interface), raster (CLI help text)
- Prerequisites: JSON schema basics, MCP protocol, CLI argument parsing
- Exclusions: Docker image building, connection handshake, transport details
- Score: 9/10

## Candidate 2 — Why test suites pass but code fails in production

- Source: `e2e/README.md`
- Topic: Real API integration as a test guard rail
- Hook: A test passes locally against mock data, but the code fails in production against the real API — the surprise reveals why mocks can't replace integration tests
- Key case: Developer changes `user.Login = sPtr("foobar")` in the code, runs tests, test fails with "expected: foobar, actual: williammartin", exposing that the test runs against the real GitHub API, not a mock
- The Question: Mock before reality / X should predict Y: if a test passes against mock data, does the code work against the real API? No—mocks diverge; only live integration confirms.
- Core idea: Mock tests hide behavior divergence between what you think the API does and what it actually does; real API integration tests expose this mismatch immediately
- Visual object: Test failure output showing Expected vs. Actual side-by-side with the developer's code change visible
- Manim move: compare
- Example seed: You mock GitHub's `/user` endpoint to always return `{login: "testuser"}`. Your code works! But real GitHub returns additional fields and sometimes fails under rate limits. Integration test against the real API would catch both.
- Length band: 2–3 min
- Still lanes: raster (test output, diff), c2v (failure as signal)
- Prerequisites: testing concepts, mocking vs. integration testing tradeoffs
- Exclusions: Go test framework internals, Docker build mechanics, token setup
- Score: 8/10

## Candidate 3 — Why more tools make language models worse

- Source: `README.md` (Dynamic Tool Discovery section)
- Topic: Constraint-based model performance
- Hook: Giving an LLM more tools available makes it less reliable at choosing the right one — the counterintuitive solution is to filter tools based on user intent
- Key case: User asks to "create a GitHub repository." With all 50 tools visible, the model tries `create_pull_request` first (wrong context). With only the `repos` toolset enabled, it finds `create_repository` immediately.
- The Question: Capability before confusion / X should predict Y: if you enable all available tools, does the model make better choices? No—tool proliferation degrades decision quality.
- Core idea: Dynamic tool discovery narrows the tool set in response to user prompts, reducing context noise and improving model focus
- Visual object: A branching tree of tools progressively pruning into a smaller focused subset, or tool list narrowing as context is applied
- Manim move: split
- Example seed: An AI assistant with a 200-tool interface makes 3× as many errors picking tools as one with 6 tools. Adding intent-based filtering to show only the 6 relevant tools restores accuracy without losing capability.
- Length band: 2–3 min
- Still lanes: c2v (all tools → filtered subset), raster (tool list before/after)
- Prerequisites: LLM context limitations, tool-choice problem in multi-tool systems
- Exclusions: Specific toolset definitions, protocol negotiation, implementation complexity
- Score: 8/10

## Candidate 04 — Why rewriting one string changes what the AI does without touching any code

- Source: `README.md`
- Topic: Tool descriptions as per-tool steering prompts
- Hook: An operator edits a single JSON string — a tool's description — and the model completely reroutes its tool choice for identical user requests, with zero code changes
- Key case: Operator sets `GITHUB_MCP_TOOL_CREATE_ISSUE_DESCRIPTION` to "for feature requests only, never bug reports" via env var; the model stops routing bug-report tasks to `create_issue` and begins composing a workaround path through `search_issues` instead
- The Question: Code vs. description / X should predict Y: if a tool's implementation is unchanged, does the model's tool-selection behavior stay constant? No — the description field alone redirects routing decisions.
- Core idea: Tool descriptions are not human documentation — they are per-tool prompts embedded in the schema that the LLM reads as instructions about when to invoke a tool; changing them is prompt engineering at the infrastructure layer
- Visual object: A JSON schema block with the `description` field highlighted in a different color, its text morphing word-by-word from default to custom while a routing arrow shifts from one tool node to another in a parallel diagram
- Manim move: morph
- Example seed: Two agents share `send_email` and `send_sms`. Description A: "send_email — Send a message to a user." Description B: "send_email — Send a message to a user; prefer for non-urgent communication." Same prompt "alert me immediately" → Description A picks email; Description B routes to SMS. (illustrative)
- Length band: 2–3 min
- Still lanes: c2v (description text → routing decision), raster (env var override in terminal)
- Prerequisites: LLM tool calling, JSON schema basics, prompt engineering concepts
- Exclusions: translation file export mechanics, i18n for non-English locales, full list of overridable keys
- Score: 7/10
