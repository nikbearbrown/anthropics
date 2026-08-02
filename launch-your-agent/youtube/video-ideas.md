# launch-your-agent Video Ideas

## Candidate 1 — Iterating toward a graded definition of done
- Source: `.claude/skills/launch-your-agent/references/interview.md`, `.claude/skills/launch-your-agent/references/cma-api.md`
- Topic: Outcome-graded iteration loops for agent verification
- Hook: You launch your agent and it produces something; how do you know it's actually done or if it needs to try again?
- Key case: An agent drafts a financial model in .xlsx, the outcome grader scores it against a rubric (all cells have formulas, all assumptions justified, no circular refs), it fails one criterion, the harness re-runs the agent with that feedback embedded. Second attempt passes. Done.
- The Question: You define "done" with a rubric the agent can't see while running; how does the loop converge—and when does it stop?
- Core idea: `user.define_outcome` kickoff supplies task + rubric + max_iterations; after each run, the harness scores the output and decides: satisfied (stop), needs_revision (re-run with feedback), max_iterations_reached (stop incomplete), or failed (stop error). The agent iterates with knowledge of prior attempts.
- Visual object: The rubric as a checklist of criteria (rows: pass/fail columns), iteration counter (1, 2, 3), decision tree at the end (satisfied / needs_revision / max / failed).
- Manim move: accumulate, morph, split
- Example seed: 3-round DCF model—round 1 missing tax assumptions, round 2 adds them but has circular cell refs, round 3 fixes both → satisfied.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: rubrics, outcome evaluation, agent loops
- Exclusions: financial-model domain; .xlsx skill internals; session streaming API
- Score: 9/10

## Candidate 2 — Mocking a connector you can't wire yet
- Source: `.claude/skills/launch-your-agent/references/mock-connectors.md`
- Topic: Schema-driven mocking as a bridge to unblocking integrations
- Hook: You want your agent to post to Slack, but the OAuth credential isn't on hand yet and you need to ship v0 today. How do you shape the agent so the eventual swap to the real Slack API isn't a complete redesign?
- Key case: Instead of a Slack tool, the agent is instructed to write each message as JSON to `/mnt/session/outputs/outbox/` using the exact schema that `slack.post_message` expects: `{"channel":"…", "text":"…", "thread_ts":"…"}`. Rubric validates outbox payloads are complete. Later (v1): swap the outbox instruction for the real MCP server—no redesign.
- The Question: You can't wire the connector today, but ignoring it makes the agent's behavior wrong; how do you mock it transparently so v0 and v1 are a drop-in swap?
- Core idea: Mock outbox (or custom-tool stub) matches the real tool's `input_schema`; system prompt says "you can't send X directly yet, write payloads to outbox instead"; rubric validates schema; v1 swap is remove the mock instruction, add the real MCP server + vault + permission gate.
- Visual object: The outbox folder with numbered JSON files (`1-send_slack_message.json`, `2-send_slack_thread.json`) alongside a diagram showing the real `slack.post_message` schema they match.
- Manim move: morph, trace
- Example seed: Metric-monitoring agent. v0 writes `{"channel":"#metrics","text":"Alert: latency > 500ms","thread_ts":null}` to outbox. Founder wires Slack OAuth. v1 swaps the outbox instruction for real MCP—same payloads, now they post.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: schema/JSON, mocking, MCP tools
- Exclusions: specific Slack API surface; credential/vault mechanics; custom tools vs. MCP servers
- Score: 9/10

## Candidate 3 — Parallel specialist team with automatic orchestration
- Source: `.claude/skills/launch-your-agent/references/examples-bank.md`, `.claude/skills/launch-your-agent/references/cma-api.md`
- Topic: Partitioning complex work across specialist agents with harness-managed coordination
- Hook: Your task needs research *and* review *and* writing in parallel; one agent will bottleneck itself doing them sequentially. How do you split it without building an orchestration harness?
- Key case: A compliance report: coordinator agent forks to three specialists in parallel (researcher collects regs, reviewer audits drafts, writer outlines). Each runs independently. Coordinator waits, collects results, synthesizes final report. CMA harness handles all forking/waiting/result collection.
- The Question: Parallel work needs someone to coordinate; if you hand-build that, you're building infrastructure, not domain logic. How does CMA hide the orchestration?
- Core idea: `"multiagent": {"type": "coordinator", "agents": [{"type": "agent", "id": "researcher"}, ...]}` — one config field. Coordinator calls other agents as tools; harness manages session lifecycle, waits for all results, returns them.
- Visual object: Coordinator node at top, three specialist nodes below (researcher, reviewer, writer) with arrows forking out and joining back; time axis showing parallelism.
- Manim move: split, accumulate, morph
- Example seed: Due-diligence task. Coordinator: "I need a risk assessment." Researcher queries public filings, finds competitors. Reviewer checks prior assessments, flags changed assumptions. Writer drafts the report. All three in parallel; coordinator weaves them. Time: ~10 min vs. ~30 min sequential.
- Length band: 2–3 min
- Still lanes: geo, c2v
- Prerequisites: idea of agents, task decomposition, basic concurrency
- Exclusions: agent domain logic; per-agent model/tool differences; load-balancing or fault tolerance
- Score: 9/10

## Candidate 4 — Interview questions as decision locks
- Source: `.claude/skills/launch-your-agent/references/interview.md`
- Topic: Structured interviews as constraint-tightening pipelines
- Hook: You're describing what you want to build in natural language; eight questions later you have a concrete agent.json. How does the interview *tighten* your vague idea into something buildable?
- Key case: Founder: "I want an agent that analyzes customer support tickets and drafts responses." Q1 locks in name + system. Q2 locks in rubric checks draft quality. Q3 locks in tools (web_fetch, read). Q4 locks in skill (docx). Q5 locks in session type (on-demand). Q6 locks in permission gates. By Q8, every field in agent.json is determined.
- The Question: You have a vague idea + eight decision points; how do you order the questions so each one narrows the option space without the founder feeling trapped?
- Core idea: Interview clusters (Q1–Q8) each lock in one or more CMA primitives (agent name/system/model, outcome rubric, tools, skills, environment, session type, permissions, multiagent). Open-ended questions invite context; follow-ups tighten only ambiguous parts. Result: fully-determined build sheet.
- Visual object: Flow chart from "what do you want to build?" through interview tree (eight clusters, branching decisions) to build sheet (agent.json, environment.json, outcome.md). Table mapping decision → primitive.
- Manim move: accumulate, trace, morph
- Example seed: Two founders, same domain (data analysis). Founder A: "Analyze spreadsheets, produce Slack summary." Q3 narrows to Slack MCP. Founder B: "Analyze spreadsheets, produce formal HTML report." Q3 narrows to read tools. Same Q1 job, different Q3–Q4, different agent.
- Length band: 3–5 min
- Still lanes: c2v, raster
- Prerequisites: agent configuration, primitives, decision trees
- Exclusions: specific question wording; founder domain; soft skills (how to ask well) vs. structure (how questions lock decisions)
- Score: 8/10

## Candidate 5 — Versioning by deferring capability, not cutting vision
- Source: `.claude/skills/launch-your-agent/references/interview.md`, `.claude/skills/launch-your-agent/references/cma-primitives.md`
- Topic: Staged shipping through explicit deferral lists
- Hook: Your agent needs to read issues, write PRs, and merge them—but gated approval is complex and webhooks need setup. You could build it all now (month-long project) or cut the merge logic (ships faster, incomplete). What's the middle ground?
- Key case: v0: read issues, analyze, draft PRs, write to outbox (no merge). Rubric: "PR draft is correct, uses right branch, has test coverage." v1: add GitHub MCP + vault + approval gate (always_ask), actually open PRs. v2: add merge gate (wait for CI + human approval). Each version ships; each adds one capability; PR schema unchanged between v0 and v1.
- The Question: Your workflow is multi-step; some pieces are wireable today, others need setup or review; how do you ship something today and still communicate the full vision?
- Core idea: Version by *primitive addition*, not feature cutting. v0 is intentionally scoped (read-only, drafts-only, outbox mocks for unavailable connectors). NEXT-DIRECTIONS lists v1/v2 as numbered increments, each with its mechanism. Founder sees both what shipped and what's planned.
- Visual object: Three-column table (v0 | v1 | v2) showing capabilities lighting up, or vertical timeline with each version adding a row.
- Manim move: accumulate, spread
- Example seed: Legal-contract reviewer. v0: analyze contracts, flag risks, draft summary. Rubric: "summary accurate, no false positives." v1: add Slack integration, post to channel. v2: add version control, file summaries with diffs. Same v0 agent, three versions' worth of shipping.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: MVP, staged shipping, deferral without cutting
- Exclusions: mechanics of building each connector; evaluation/grading loop; specific domain
- Score: 7/10

## Candidate 06 — The agent pauses mid-run and waits for a human—indefinitely

- Source: `.claude/skills/launch-your-agent/references/cma-api.md`
- Topic: Session idle-bounce as a human-approval gate
- Hook: Your agent investigates an incident and is ready to merge a fix to main—but you never told it to wait for you. How do you wire a mandatory human checkpoint into an otherwise autonomous run without losing the agent's full conversation context?
- Key case: SRE incident responder: agent diagnoses a latency spike, drafts a hotfix PR, then calls `approve_pr()` (a custom tool). Session flips to `idle` with `stop_reason: {type: "requires_action"}`. On-call engineer gets paged, reviews the draft in Console, sends `user.tool_confirmation` with `result: "allow"`. Agent resumes the same session, opens the PR, monitors CI.
- The Question: Running → idle is normal at end-of-task; but `requires_action` idle happens mid-sequence with context still live. How does the agent freeze, wait indefinitely, and resume as if the pause never happened?
- Core idea: When a custom tool surfaces, the session suspends at that turn boundary—no token spend, no timeout, event log intact. The harness holds state until a `user.tool_confirmation` event arrives (`allow` or `deny` + optional message). The agent receives the result as a tool response and continues forward in the same session; `deny` gives it a reason to try an alternative path.
- Visual object: Session state-machine diagram: `running` → `idle (requires_action)` → [notification arrow out to pager/Slack, confirmation arrow back] → `running` → `idle (end_turn)`. The event log scrolling beneath it.
- Manim move: trace, morph
- Example seed: Expense-approval agent. Finds $47,200 vendor invoice. Calls `approve_payment({"amount": 47200, "vendor": "Acme Corp"})`. Session idles. CFO sends `allow`. Agent books the payment, writes receipt path to outbox. If CFO sends `deny`: "over budget cap," agent flags for manual review instead.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: session state machine, custom tools, event-driven systems
- Exclusions: webhook notification wiring to external systems; building the approval UI; distinction between always_ask gate and custom-tool confirmation
- Score: 9/10

## Candidate 07 — Changing the agent breaks it; the version number is what saves you

- Source: `.claude/skills/launch-your-agent/references/cma-api.md`, `.claude/skills/launch-your-agent/references/examples-bank.md`
- Topic: Optimistic-lock versioning with eval-score-triggered rollback
- Hook: You updated your agent's system prompt to handle a new edge case—and now it fails three cases it previously got right. How do you detect the regression before it touches live runs, and how do you ship the fix without destroying the working version?
- Key case: Financial analyst agent. v1 scores 8/10 on evals. You add FX-normalization logic → v2. Eval run: 5/10 (broke three DCF checks). Live sessions are pinned to `{"type":"agent","id":"...","version":1}`. You debug, ship v3 with the fix. Eval: 9/10. Pin removed; live sessions advance.
- The Question: You incremented one thing; how do you know you broke three others—and how do you hold live traffic on the old version while you fix the new one?
- Core idea: Every `PUT /agents/:id` requires the current `version` field as an optimistic concurrency guard—stale version → rejected update. Each accepted update returns a new version number. Sessions default to "latest" but can pin a specific version. Regression detected (eval score drops) → pin live sessions to last-good version → iterate in a new version → evals pass → remove pin.
- Visual object: Version timeline (v1 → v2 → v3) with an eval-score curve overlaid; score dips at v2, triggering a "PIN" annotation; live-session pointer frozen at v1; score recovers at v3, pin annotation removed.
- Manim move: trace, accumulate, morph
- Example seed: 3-version DCF agent. v1: standard inputs, 8/10. v2: adds currency handling, breaks depreciation logic, 5/10—live sessions pinned to v1. v3: fixes depreciation, retains FX, 9/10—pin lifted.
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: agent creation, rubric-based eval, session version pinning
- Exclusions: full regression suite CI/CD wiring; version archive and lifecycle; per-version model or tool differences
- Score: 8/10
