# Claude Cookbooks Video Ideas

## Candidate 01 — Agents learn from their mistakes mid-task without forgetting

- Source: `managed_agents/README.md`
- Topic: Agentic feedback loops in persistent sessions
- Hook: Agents can't learn from mistakes mid-task unless the architecture persists and streams observations
- Key case: Test suite fails with "index out of bounds at line 42". Agent observes error in event stream. Agent edits line 42. Agent reruns tests. Tests pass.
- The Question: X (session persistence + streaming events) should predict Y (agents accumulate corrections within a task); request-response stateless architectures did not; why?
- Core idea: Session persistence + streaming events allow agents to accumulate observations (errors) and apply corrections (edits) in a single feedback loop without losing context
- Visual object: Event timeline showing [test_fail] → [read_error] → [edit_code] → [test_pass] as a circular loop
- Manim move: trace
- Example seed: "Test suite runs. Agent reads event: 'AssertionError at line 42, array index 500 out of bounds'. Agent edits line 42 to add bounds check. Agent reruns suite. Event: 'all tests passed'. Feedback cycle closed."
- Length band: 2–3 min
- Still lanes: c2v with event stream, raster timeline
- Prerequisites: Managed Agents, sessions, event-streaming concepts
- Exclusions: MCP tool integration, human-in-the-loop gates, custom tool mechanics
- Score: 8/10

## Candidate 02 — Rollback an agent's behavior by pinning to a previous prompt version

- Source: `managed_agents/README.md`
- Topic: Server-side prompt versioning and regression detection
- Hook: Prompt changes are invisible, untracked, and silently degrade agent accuracy in production with no obvious rollback path
- Key case: Deploy v2 prompt ("provide detailed reasoning"). Evaluate on labeled test set: accuracy drops from 92% to 87%. Pin all new sessions to v1. Accuracy recovers.
- The Question: X (server-side prompt versioning) should predict Y (detect and revert regressions); prompt-as-code without versioning did not; why?
- Core idea: Treat prompts as versioned server-side artifacts, not code. Evaluate each version against labeled outcomes. Rollback is a session pin, not a git revert.
- Visual object: Version timeline with accuracy bars for v1 (92%) and v2 (87%), branching session IDs to their pinned versions
- Manim move: split
- Example seed: "v1 prompt: 'be concise' → 92% correct. v2 prompt: 'be thorough' → 87% correct. New sessions (after detection) default to v1. Existing session 'user-42' stays on v2 for A/B test."
- Length band: 2–3 min
- Still lanes: c2v with version decision flow, raster accuracy graph
- Prerequisites: Managed Agents, agent evaluation basics
- Exclusions: detailed prompt engineering, A/B testing statistics, evaluation metrics design
- Score: 8/10

## Candidate 03 — New agent sessions recall what previous sessions learned via shared memory

- Source: `managed_agents/README.md`
- Topic: Persistent memory stores across independent agent sessions
- Hook: Each new session is stateless with zero memory of prior conversations, yet users expect agents to recall their preferences
- Key case: Session 1 (hours ago): user says "I prefer blue widgets". Agent saves to memory store. Session 2 (new, zero shared context): Agent reads memory and prioritizes blue widgets without being told.
- The Question: X (shared memory store readable by new sessions) should predict Y (preferences transfer across sessions); per-session isolation did not; why?
- Core idea: Decouple session lifetime from memory lifetime. Use a shared memory store seeded at session creation. New sessions inherit memories written by old sessions.
- Visual object: Memory store database with two session timelines above and below, arrows showing write from session 1, read by session 2
- Manim move: duplicate
- Example seed: "Session 1 ends: agent writes 'color_preference: blue' to memory store. Session 2 starts 3 hours later: system includes memory snippet in context. User asks 'show me options'. Agent: 'Based on your history, prioritizing blue items first.'"
- Length band: 2–3 min
- Still lanes: geo with session boxes and store, c2v with write-read flow
- Prerequisites: Managed Agents, session concept
- Exclusions: multi-customer memory isolation, privacy scoping, memory versioning
- Score: 7/10

## Candidate 04 — Same Docker image deploys unchanged from laptop to Kubernetes

- Source: `claude_agent_sdk/hosting/README.md`
- Topic: Deployment-agnostic agent architecture via HTTP interface contracts
- Hook: Agent code written for local iteration shouldn't break when orchestration machinery changes from docker-compose to cloud sandboxes to Kubernetes
- Key case: Single Dockerfile builds once. Runs locally via `docker-compose up`. Pushed to Modal, runs in cloud sandbox. Deployed to Kubernetes, runs as pod-per-session. All three use identical HTTP endpoints.
- The Question: X (stateless HTTP interface contract) should predict Y (code works unchanged across infrastructure tiers); tight coupling to orchestration did not; why?
- Core idea: Define a minimal HTTP interface (/health, /sessions/{id}/messages with streaming). Implement once. Orchestrators (docker-compose, Modal, Kubernetes) swap beneath it without agent code changes.
- Visual object: Three deployment architecture diagrams (laptop, cloud, cluster) stacked vertically, all pointing downward to a shared HTTP contract layer
- Manim move: split
- Example seed: "Agent code: run research_agent() in main loop. Local: `docker build && docker-compose up` → localhost:8000/sessions/{id}/messages (streaming events). Modal: `modal serve` → https://modal-tunnel/sessions/{id}/messages (same). Kubernetes: `kubectl apply` → cluster service IP/sessions/{id}/messages (same)."
- Length band: 2–3 min
- Still lanes: c2v with three deployment flows converging, raster architecture decision tree
- Prerequisites: Docker basics, HTTP, agent concepts
- Exclusions: Kubernetes networking details, Modal billing, containerization internals
- Score: 7/10

## Candidate 05 — Format-chaining tools create analyses the raw data can't express

- Source: `skills/README.md`
- Topic: Skill composition and emergent capabilities in multi-stage data pipelines
- Hook: Converting data between formats is busywork; combining formats shouldn't unlock new analytical insights
- Key case: Raw CSV (sales numbers). Excel adds formulas (YoY growth %, pivot tables). PowerPoint embeds charts and narrative ("Growth was 20% driven by Q4"). PDF archives for distribution. Stakeholder insight emerges from narrative, not from raw CSV.
- The Question: X (chaining format-specific tools) should predict Y (emergent analytic insight); single-format tools did not; why?
- Core idea: Each tool adds capabilities (Excel: formulas & aggregation, PowerPoint: narrative structure, PDF: portability). Composition is non-linear—downstream tools inherit upstream insights, enabling analyses no single tool expresses.
- Visual object: Sankey or pipeline diagram showing CSV → Excel (formulas calculated, growth metric appears) → PowerPoint (chart embedded, narrative added) → PDF (styled, archived)
- Manim move: transform
- Example seed: "CSV: [2023_revenue: 100, 2024_revenue: 120]. Excel formula: growth_pct = (120-100)/100 = 20%. PowerPoint embeds bar chart and text: '20% YoY growth driven by seasonal Q4 surge.' PDF locks it. Stakeholder reads narrative in PDF, says 'Aha—we have seasonal risk.' Raw CSV never prompted 'aha.'"
- Length band: 2–3 min
- Still lanes: raster with pipeline visualization, c2v with capability annotations at each stage
- Prerequisites: Skills API, file I/O basics, data literacy
- Exclusions: Excel formula design, PowerPoint slide dynamics, PDF accessibility compliance
- Score: 7/10

## Candidate 06 — Cheap workers cut frontier costs without cutting quality

- Source: `managed_agents/README.md`
- Topic: Cost-optimal task decomposition in multi-agent systems
- Hook: Using a frontier model for every subtask is wasteful; using cheap models everywhere loses quality
- Key case: Research task: 9 papers to read and synthesize. Solo frontier reads all 9 and synthesizes. Hybrid: frontier coordinator plans, three cheap workers each read 3 papers in parallel, frontier synthesizes. Cost 33% lower; quality grader scores both 8.7/10.
- The Question: X (frontier coordinator + cheap parallel workers) should predict Y (matched quality at lower cost); running frontier on all subtasks did not achieve cost efficiency; why?
- Core idea: Decompose by token-intensity. Token-heavy extraction requires throughput, not reasoning — cheap models suffice there. Frontier intelligence concentrates at planning and synthesis, where it determines outcome quality.
- Visual object: Cost-per-thread bar chart for frontier-only vs. hybrid, with fan-out arrows from coordinator to workers and back
- Manim move: accumulate
- Example seed: "Task: summarize 9 papers. Frontier-only: $0.90. Hybrid: coordinator ($0.05) + 3 workers × 3 papers ($0.15 each) + synthesis ($0.10) = $0.60. Quality grader: both 8.7/10. Savings: 33% at zero quality cost."
- Length band: 2–3 min
- Still lanes: raster with cost bar chart, c2v with task-fan-out diagram
- Prerequisites: Token pricing basics, multi-agent concept
- Exclusions: Specific model pricing comparisons, prompt routing algorithms, frontier model selection criteria
- Score: 8/10

## Candidate 07 — Scoping tools to specialists prevents coordinators from becoming generalists

- Source: `managed_agents/README.md`
- Topic: Per-role tool scoping in heterogeneous multi-agent teams
- Hook: Giving all agents all tools produces generalists who violate role boundaries; scoping tools enforces specialization structurally
- Key case: Sales proposal team — researcher (WebSearch only), librarian (file-read only), pricer (rules-calculator only). Pricer cannot browse internet to undercut contract rates. Librarian cannot guess missing data from web. Coordinator assembles outputs. Proposal is both accurate and compliant.
- The Question: X (scoped toolsets per role) should predict Y (role-faithful behavior without cross-role contamination); unscoped shared toolsets did not reliably enforce roles; why?
- Core idea: Tools define what an agent CAN do, not just what it should do. Scoping removes the possibility of role violations rather than relying on prompt instructions to prevent them.
- Visual object: Three agent nodes each with a locked tool palette showing only permitted icons; coordinator above with routing arrows
- Manim move: split
- Example seed: "Pricer: tools = [rules_calculator]. Query: 'find cheapest market price.' Pricer can only compute from rule table — cannot WebSearch. Returns contract-compliant price. Unscoped pricer would have Googled a lower price and broken the contract."
- Length band: 2–3 min
- Still lanes: c2v with role-tool lock diagram, geo with team topology
- Prerequisites: Multi-agent basics, tool use concept
- Exclusions: Tool design patterns, agent orchestration frameworks, prompt-level role enforcement
- Score: 7/10

## Candidate 08 — A stateless grader breaks the writer's conflict of interest

- Source: `managed_agents/README.md`
- Topic: Grade-and-revise loops with stateless outcome graders
- Hook: An LLM cannot objectively verify its own citations because it rationalizes rather than checks
- Key case: Writer drafts research brief citing 5 URLs. Stateless grader (no shared context with writer) fetches each URL, checks each quote against source text, scores against rubric. Grader: "Quote 3 misattributed; URL 5 returns 404." Writer revises. Grader rescores. Loop exits when brief passes.
- The Question: X (stateless grader with external URL fetching) should predict Y (convergence toward verifiable accuracy); self-evaluation by the writer did not; why?
- Core idea: Statelessness prevents the grader from inheriting the writer's assumptions. Ground-truth signal (live URL content, exact quote matching) cannot be manufactured by the writer — only the grader can produce it.
- Visual object: Circular loop: writer → grader → annotated feedback → writer; quality score counter ticking upward each cycle
- Manim move: trace
- Example seed: "Draft 1: 3 accurate quotes, 1 misattributed, 1 dead URL. Score: 6/10. Feedback: 'Fix quote 4, replace URL 5.' Draft 2: 5 accurate. Score: 9/10. Loop exits. Cycles: 2."
- Length band: 2–3 min
- Still lanes: raster with revision quality timeline, c2v with grader–writer feedback loop
- Prerequisites: Evaluation basics, agent sessions
- Exclusions: Rubric design methodology, specific evaluation benchmarks, LLM-as-judge debate
- Score: 7/10

## Candidate 09 — Chunks without context retrieve the wrong document 40% of the time

- Source: `capabilities/contextual-embeddings/README.md`
- Topic: Contextual embeddings add document-level context before chunk embedding
- Hook: A chunk split from its document loses the surrounding information that makes it retrievable for the right query
- Key case: Medical paper split into 20 chunks. Chunk 7: "This treatment reduced mortality by 12%." No disease mentioned. BM25 retrieves it for "diabetes mortality" because "mortality" matches. Same chunk prepended with "Context: hypertension study in elderly patients" — no longer retrieved for diabetes query.
- The Question: X (context-augmented chunks) should predict Y (precise retrieval for the right queries); bare chunks did not; why?
- Core idea: Prepend a generated summary of the surrounding document to each chunk before embedding. The embedding captures both local content and document-level context, resolving ambiguous token matches.
- Visual object: Side-by-side: bare chunk vs. context-prepended chunk, with a retrieval hit/miss matrix across 10 queries
- Manim move: transform
- Example seed: "Chunk: 'mortality reduced 12%'. Bare: retrieves for cancer, diabetes, heart queries. With context ('hypertension study; elderly; mortality reduced 12%'): retrieves only for hypertension query. Precision: 33% → 90%."
- Length band: 2–3 min
- Still lanes: raster with retrieval precision comparison, c2v with context-prepend transformation step
- Prerequisites: RAG basics, embeddings concept, BM25 basics
- Exclusions: Chunking strategies, embedding model comparisons, full RAG pipeline benchmarking
- Score: 7/10

## Candidate 10 — Safety hooks reject invalid writes before the agent touches infrastructure

- Source: `claude_agent_sdk/README.md`
- Topic: PreToolUse hooks as write-operation guardrails for autonomous agents
- Hook: Agents that can write to infrastructure will eventually propose writes that break it — prompt instructions are the only gate, and they fail silently
- Key case: SRE agent investigates high DB error rate. Root cause: connection pool = 5. Agent proposes: set pool_size = 500. PreToolUse hook fires, checks range (max allowed = 100), rejects. Reason returned to agent. Agent retries: pool_size = 80. Hook: valid. Write executes. Service recovers.
- The Question: X (PreToolUse hooks with invariant validation) should predict Y (agents self-correct invalid write proposals); prompt-only instructions did not reliably prevent out-of-range writes; why?
- Core idea: Hooks intercept tool calls before execution and return approve/reject with a reason. The rejection reason becomes agent context — the agent adapts its next proposal rather than hitting a silent failure or a system crash.
- Visual object: Agent → hook intercept box → decision gate → approved writes pass through, rejected writes return with reason annotation
- Manim move: split
- Example seed: "Agent: config_write(pool_size=500). Hook: max=100; reject; reason='500 exceeds max 100.' Agent: config_write(pool_size=80). Hook: valid. Write executes. Agent log: 'pool corrected to 80; within bounds.'"
- Length band: 2–3 min
- Still lanes: c2v with hook intercept diagram, raster with agent retry trace
- Prerequisites: Tool use basics, agent concepts
- Exclusions: Hook implementation internals, PagerDuty integration, Prometheus PromQL details
- Score: 7/10

## Candidate 11 — An idle webhook eliminates 120 polling requests for one human decision

- Source: `managed_agents/README.md`
- Topic: Webhook-on-idle pattern for human-in-the-loop without long-lived connections
- Hook: Waiting for a human decision keeps a server connection open for minutes; polling burns requests; neither scales
- Key case: Agent pauses for expense approval ($50,000). Polling: client sends GET /status every 5 seconds for 10 minutes — 120 requests, connection held open. Webhook pattern: agent signals `session.status_idled`, platform fires Slack message. Manager approves 8 minutes later. Single callback resumes session. Requests sent: 1.
- The Question: X (status_idled webhook + callback) should predict Y (HITL gates without connection overhead); long-lived polling did not scale to many concurrent sessions; why?
- Core idea: Model the human decision as an external event, not a synchronous wait. Agent idles; platform fires webhook; human acts on notification; callback resumes. Connection is held only during active agent turns.
- Visual object: Two side-by-side timelines — webhook (flat line until single callback spike) vs. polling (120 identical vertical ticks across 8 minutes)
- Manim move: accumulate
- Example seed: "Agent idles 00:00. Webhook fires → Slack ping sent. Manager approves 08:23. Callback: session.resume(approved=True). Agent active 08:23. Polling alternative: 99 identical status requests, 8-minute open connection, same outcome."
- Length band: 2–3 min
- Still lanes: raster with request timeline comparison, c2v with webhook topology diagram
- Prerequisites: Webhooks basics, HTTP polling concept, agent sessions
- Exclusions: Slack API integration details, custom-tool round-trip mechanics, vault credential scoping
- Score: 6/10
