# Claude Agent SDK Demos Video Ideas

## Candidate 1 — Parallel subagent execution becomes traceable via parent tool IDs
- Source: `research-agent/README.md`
- Topic: Reconstructing which subagent made which tool call in parallel execution
- Hook: When a lead agent spawns multiple researchers in parallel, each making web searches and file writes, logs show 30 interleaved tool calls from 4 agents—but which WebSearch belonged to which Researcher?
- Key case: Lead Agent spawns 3 parallel Researchers to investigate quantum computing. Each calls WebSearch multiple times. Data Analyst runs Bash in parallel. Report Writer calls Write. Terminal shows tool calls streaming past. User cannot tell which output came from which agent without reading agent names in parentheses.
- The Question: Parent spawns N children making tool calls in parallel and logs stream past in interleaved order; how do you reconstruct which tool call belongs to which child?
- Core idea: SDK injects `parent_tool_use_id` into every tool call made by a subagent. This ID matches the tool_use_id of the Task call that spawned it. Hooks intercept pre/post execution, extract the parent ID, map it to agent identity ("RESEARCHER-1", "DATA-ANALYST-1"), and write JSONL logs + human-readable transcript grouping tool calls by agent.
- Visual object: Directed acyclic graph (DAG) with Task node at top, child tool_use_id nodes below, edges labeled with parent_tool_use_id. Each node colored by agent. Timeline of tool calls with agent column on left.
- Manim move: trace (draw edges as parent_tool_use_id revealed) then accumulate (build tree as execution proceeds)
- Example seed: Lead Agent spawns Task("research quantum") with ID "task_42". Researcher subagent calls WebSearch (tool_use_id "ws_100") with parent_tool_use_id = "task_42". Hook logs "RESEARCHER-1 → WebSearch quantum computing 2025 (parent: task_42)". Later, Data-Analyst's Bash (tool_use_id "bash_50") has parent_tool_use_id = "task_42b". Logs separate them. Tool_calls.jsonl includes all IDs; transcript.txt groups by agent.
- Length band: 2–3 min
- Still lanes: geo (DAG with edge labels) | c2v (hook handler extracting parent_tool_use_id) | raster (terminal screenshot showing agent name + tool name)
- Prerequisites: multi-agent systems, Task tool, hooks, async execution
- Exclusions: quantum computing research specifics, SDK internals of Task spawning, how parent IDs are generated
- Score: 9/10

## Candidate 2 — User choice round-trip via WebSocket bridges browser UI to server-side SDK
- Source: `ask-user-question-previews/README.md`
- Topic: Rendering interactive HTML previews for options while SDK decision logic runs server-side
- Hook: Claude can ask text-only multiple-choice questions. But for brand choices—color palettes, typography, layout vibe—users need to see rendered mockups, not just labels.
- Key case: Branding assistant asks "What vibe?" with 4 text labels. Claude also generates 4 HTML preview fragments (styled divs with color swatches, font specimens, UI mockups). Previews land in browser as cards. User clicks the "retro-playful" card. Browser sends label back to server. Server's canUseTool callback receives it, SDK resumes generation with the choice baked in.
- The Question: SDK runs on server asking tool questions; browser renders UI separately. How do you get a user choice from the browser back into the SDK's server-side canUseTool callback without redesigning the SDK or polling?
- Core idea: Server's `canUseTool` callback intercepts AskUserQuestion, extracts option.preview HTML fragments, stores a promise resolver in a Map keyed by question ID, sends questions + HTML to browser over WebSocket. Browser renders each option as an interactive card (HTML sanitized with DOMPurify), user clicks one. Browser WebSocket message triggers server to resolve the promise. canUseTool returns the label in updatedInput.answers. SDK continues.
- Visual object: Sequence diagram with three lanes (SDK subprocess, server callback, browser). Arrows show promise creation → WebSocket send → user click → promise resolution → SDK continuation. Thick arrow from server to browser carrying HTML; thin arrow back carrying string label.
- Manim move: morph (SDK question becomes browser card) then trace (promise callback chain from server to browser and back)
- Example seed: Prompt: "Brand a snack food startup." Claude asks "Aesthetic?" with options including `<div style='background: #FF9500; padding: 20px;'>Cheerful</div>` (orange mockup), `<div style='background: #2C3E50;'>Sophisticated</div>` (dark mockup), etc. Browser renders 4 clickable cards. User clicks orange. Server's promise resolves with label "cheerful". SDK continues: "Great choice! Now fonts..."
- Length band: 2–3 min
- Still lanes: c2v (server.ts canUseTool forwarding to WebSocket, client App.tsx rendering with DOMPurify sanitization) | raster (screenshot of branding assistant UI with 4 HTML preview cards)
- Prerequisites: WebSocket, promises, canUseTool callback, HTML sanitization
- Exclusions: Vite/React build setup, specific branding logic, DOMPurify internals
- Score: 8/10

## Candidate 3 — Template instantiation maps agent decisions to user-specific one-click workflows
- Source: `email-agent/ACTIONS_SPEC.md`
- Topic: Bridging gap between generic SDK tools and user's repetitive context-specific sequences
- Hook: SDK offers SendEmail, ArchiveEmail, SearchEmails (generic). User wants "Send payment reminder to ACME Corp for Invoice #2024-001 (15 days overdue)"—a 5-step sequence. Describing it every time is tedious; agent can't anticipate all workflows.
- Key case: User conversation shows pattern: find overdue invoices → compose reminder email → add followup label. Agent recognizes pattern. Instead of asking user to repeat, agent instantiates ActionTemplate SendPaymentReminderToVendor with {vendor: "ACME Corp", invoiceId: "2024-001", daysOverdue: 15}. UI renders button: "Send payment reminder to ACME Corp for Invoice #2024-001 (15 days overdue)". User clicks. Multi-step handler executes.
- The Question: How do you let users execute complex context-specific workflows (not generic operations) with one click, while agent learns those workflows from conversation patterns?
- Core idea: Define ActionTemplate with parameterSchema (JSON schema of required fields). Agent matches user intent to template, extracts/infers parameters from email bodies or conversation. Instantiation includes a label (specific description for button) and async handler function. Handler accepts filled parameters and executes multi-step sequence. SDK renders button. One click invokes handler.
- Visual object: Card mockup showing template name, required parameters schema on left, filled-in values (ACME Corp, 2024-001, 15) in center, rendered action button on right. Arrow from agent decision to instantiation to button render.
- Manim move: morph (generic template becomes specific action) then split (one template instantiated multiple ways) then accumulate (agent learns template library from repeated patterns)
- Example seed: Template SendPaymentReminder has parameterSchema {vendor, invoiceId, daysOverdue}. User says "Follow up on ACME's old invoice." Agent searches, finds ACME invoice INV-2024-001, 20 days old. Agent instantiates {templateId: "send_payment_reminder", params: {vendor: "ACME Corp", invoiceId: "INV-2024-001", daysOverdue: 20}, label: "Send payment reminder to ACME Corp for Invoice INV-2024-001 (20 days overdue)"}. UI renders button. User clicks. Handler searches ACME emails, writes reminder, sends, adds label.
- Length band: 2–3 min
- Still lanes: c2v (ActionTemplate interface, parameterSchema, handler function signature) | raster (mockup of action button in email UI)
- Prerequisites: template pattern, JSON schema, parameter instantiation, async handlers
- Exclusions: email-specific operations (sendEmail, searchEmails API), listener hooks, session management, full ActionContext method signatures
- Score: 8/10

## Candidate 4 — Hook-based path validation gates file operations before execution
- Source: `hello-world/README.md`
- Topic: Intercepting tool calls mid-flight to enforce constraints
- Hook: Agent has access to Write, Edit, Bash. Without guardrails, it might write `.ts` files to `/tmp`, delete directories, or install packages system-wide. You want to constrain: only allow .ts writes to `agent/custom_scripts/`.
- Key case: Agent decides to call Write({filePath: "/tmp/helper.ts", content: "..."}). Hook intercepts, checks path regex `/agent/custom_scripts/.*\.(js|ts)$/`, finds no match. Hook blocks. Agent sees error and retries with correct path `agent/custom_scripts/helper.ts`. Path matches. Hook allows. Write executes.
- The Question: How do you intercept a tool call before execution, validate constraints (path, permissions, quotas), and decide whether to allow, modify, or block it?
- Core idea: Define PreToolUse hook in hooks.matcher array. When SDK is about to invoke Write/Edit/MultiEdit, hook function receives input. Hook extracts filePath, tests regex. If match, return {continue: true}. If not, return {decision: 'block', stopReason: 'Only .js/.ts in custom_scripts', continue: false}. SDK respects decision; tool does not execute.
- Visual object: Flowchart showing tool call arriving at SDK → hook function evaluates path regex → decision diamond (valid?) → two branches: allow (tool executes) or block (error returned to agent).
- Manim move: split (tool call branches to validation gate) then collapse (decision gate reduces to allow/block outcome)
- Example seed: Agent calls Write({filePath: "helper.ts"}). Hook tests `/agent\/custom_scripts\/.*\.ts$/.test("helper.ts")` → false. Returns block. Agent retries with "agent/custom_scripts/helper.ts". Hook tests → true. Returns allow. Write executes. File created in correct directory.
- Length band: 1–2 min
- Still lanes: c2v (hook matcher function and regex validation) | raster (flowchart: tool → hook → decision → allow/block)
- Prerequisites: hooks API, regex patterns, tool input schema
- Exclusions: complex policy logic, multi-level directory traversal, symlink handling
- Score: 6/10

## Candidate 05 — V2 sessions accumulate a rolling transcript that can be rehydrated by ID alone
- Source: `hello-world-v2/README.md`
- Topic: How send()/stream() separation enables stateful multi-turn conversations and cross-process resumption
- Hook: V1's `query()` generator is a one-shot pipe—one prompt in, one stream of responses out; a follow-up question arrives with no memory of the prior exchange.
- Key case: User asks "Who invented radio?" in V1: caller must manually concatenate prior turns into the next `query()` call or context is lost. In V2, `session.send("What year?")` already knows the prior exchange; `session.stream()` returns a contextual answer. Server restarts. `resumeSession("sess_7")` is called with only the ID—full history is back.
- The Question: V1's single `query()` generator already handles a complete turn end-to-end; what structural change in V2 lets the SDK carry conversation state across multiple turns and even process restarts from a single string ID?
- Core idea: A V2 Session maintains an internal rolling transcript. `send()` appends a message and starts generation. `stream()` yields response chunks without resetting state. Each send/stream cycle adds one turn to the accumulating transcript. `resumeSession(sessionId)` rehydrates that entire transcript—the ID is the key, the transcript is the value. State is not in the caller's code; it lives inside the session object and can be reconstructed at any time.
- Visual object: Two-panel comparison: left panel shows V1 as isolated generator bars (each prompt starts a fresh bar, no state carries over); right panel shows a V2 transcript stack with send/stream pairs stacking layers, a `resumeSession` arrow pointing mid-stack to reload a saved run.
- Manim move: accumulate (transcript stack grows one send/stream pair at a time) then trace (resumeSession arrow locating and reloading the saved stack)
- Example seed: Session ID "sess_7". Turn 1: `send("What is Ohm's Law?")` → stream yields "V=IR". Turn 2: `send("Give an example.")` → stream yields "12V / 4Ω = 3A". Server restarts. `resumeSession("sess_7")` restores both turns. `send("Unit of resistance?")` → stream yields "Ohm (Ω)" — context intact without re-sending history. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v (V1 vs V2 comparison table from README; `send`/`stream`/`resumeSession` call signatures) | geo (two-panel transcript accumulation diagram with session ID label)
- Prerequisites: async generators, conversation context, session state
- Exclusions: the `unstable_` prefix and API stability guarantees, SDK subprocess management, OAuth vs API key credential flow
- Score: 7/10

## Candidate 06 — openpyxl writes formula strings but LibreOffice must fill the cached result values
- Source: `excel-demo/agent/README.md`
- Topic: Why AI-generated Excel files need a headless recalculation pass before values appear
- Hook: Claude writes syntactically correct Excel formulas via openpyxl (`=SUM(B2:B10)`), but the output file opens with blank or zero cells—the formula exists, but no result is cached.
- Key case: Agent generates a budget tracker with `=SUM(income)` and `=budget-expenses` formulas. openpyxl writes the formula strings into .xlsx XML. File opens: cells show 0 or raw formula text. `recalc.py` invokes LibreOffice headless: open → calculate → save → exit. File reopens: all cells show computed values. `recalc.py` also flags any `#REF!` or `#DIV/0!` errors before the file reaches the user.
- The Question: openpyxl successfully writes the formula text to the correct cells; why does the spreadsheet still display wrong or missing values until a separate tool recalculates it?
- Core idea: Each formula cell in .xlsx stores two things: the formula string and a cached result from the last save. openpyxl writes the formula but leaves the cached result empty (or at a prior stale value). Interactive spreadsheet apps recalculate on open; a programmatically generated file delivered directly to users may never pass through that recalculation step. LibreOffice headless acts as an invisible spreadsheet engine that fills every cached-result slot. `recalc.py` then reads the file and scans for error tokens (`#REF!`, `#DIV/0!`) as a post-recalc validation pass.
- Visual object: A formula cell split into two slots: left slot = formula string (`=SUM(B2:B10)`), right slot = cached result (blank → 450). A LibreOffice headless process arrow points into the right slot and fills it.
- Manim move: split (cell divided into formula-slot and cache-slot) then morph (cache-slot transitions from blank to computed value after LibreOffice pass)
- Example seed: Cell C5 formula: `=B2+B3+B4`. openpyxl writes `formula="=B2+B3+B4"`, `cached_value=None`. LibreOffice evaluates: B2=100, B3=200, B4=150 → writes `cached_value=450`. `recalc.py` reads C5: value=450, no error token. User opens file and sees 450 immediately with no client-side recalculation. [illustrative]
- Length band: ~1 min
- Still lanes: c2v (`recalc.py` invocation and error-check logic from README) | geo (cell anatomy diagram: formula slot + cache slot with before/after)
- Prerequisites: .xlsx XML structure, openpyxl library, LibreOffice headless mode
- Exclusions: openpyxl formatting/styling API, Pandas data manipulation, the full agent CLAUDE.MD instruction set
- Score: 6/10
