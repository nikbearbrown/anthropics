# Agent SDK Workshop Video Ideas

## Candidate 1 — Why the obvious risk indicator is wrong
- Source: `02-breakouts/account-intelligence/README.md`
- Topic: Leading indicators in decision-making
- Hook: Account metrics look healthy (usage up 40%, zero tickets, happy QBR); executive sponsor departure hidden in interaction notes; usage is a lagging indicator, not leading
- Key case: A-2201 (Pelledryn Data Sciences) — renewal in 30 days with all green signals, but the person who championed the product internally is leaving
- The Question: X (growth + no red flags) should predict renewal success; this case shows both; why did cross-referencing the churn playbook flag risk instead?
- Core idea: Consulting a leading-indicator playbook against interaction history reveals what lagging metrics (usage, support tickets) miss — sponsor departure is the #1 predictor of churn regardless of growth
- Visual object: Before/after account briefing, with the key difference being the flagged departure, its playbook rank, and the revised health assessment
- Manim move: scan (through interaction history) → rotate (playbook ranking into foreground) → collapse (surface data + playbook insight into new interpretation)
- Example seed: An API platform notices their largest customer's CTO (the only person using the product at that company) took a VP role at a competitor; usage is up 30% but that CTO *is* the customer—the real risk isn't in the metrics
- Length band: 2–3 min
- Still lanes: c2v (surface account data → hidden interaction note → playbook entry → revised briefing), raster (before/after brief excerpt)
- Prerequisites: Basic account data literacy, familiarity with sales/churn concepts
- Exclusions: Don't run the full account-intelligence breakout; don't explain all six breakouts; don't teach component selection or system-prompt tuning
- Score: 9/10

## Candidate 2 — Why the angry customer's refund claim is wrong
- Source: `02-breakouts/customer-support/README.md`
- Topic: Verification under urgency and emotion
- Hook: Customer claims duplicate charge and demands refund in an angry tone; the obvious move (refund) is the wrong move
- Key case: T-1050 (Prismwarp Media Works) — account is past-due, payment method expired, so the two charges are overdue payment + current month; both legitimate
- The Question: X (customer says "duplicate," is upset) should predict "issue refund"; this case has both signals; why did verifying account status reveal both charges are justified?
- Core idea: Checking account state before acting reveals that a duplicate-charge complaint masks a past-due situation; the support playbook (kb-duplicate-charges) covers this exact scenario and disambiguates
- Visual object: Ticket reply before/after, with the agent pivoting from "I'll issue a refund" to "I found the issue: your account was past-due, so the charge is the catch-up payment"
- Manim move: scan (customer complaint) → split (claim vs. account timeline) → overlay (both charges onto past-due timeline) → transform (reply from refund to explanation)
- Example seed: A SaaS user claims double-billing on a monthly renewal; their subscription auto-renewed on day 1, and they manually paid on day 5 not realizing auto-pay was on; both charges are correct, just unintended
- Length band: 2–3 min
- Still lanes: c2v (complaint thread → account status → both charges on timeline → corrected reply), raster (before/after reply text)
- Prerequisites: Basic support operations, understanding of account state and payment cycles
- Exclusions: Don't cover the full customer-support agent; don't run all five tickets; don't teach tool selection or config assembly
- Score: 9/10

## Candidate 3 — Why timeline-first incident diagnosis succeeds
- Source: `02-breakouts/sre-agent/README.md`
- Topic: Incident diagnosis through systematic timeline reconstruction
- Hook: Error alert fired; deploy went out 20 minutes ago; matching runbook exists; the causality seems obvious; does timeline-first analysis prevent false confidence?
- Key case: checkout service error rate spike at 12:03, deploy at 11:42, RB-001 covers this scenario — does connecting those dots in order and following the runbook actually solve it?
- The Question: X (recent deploy + matching runbook) should predict "follow the runbook"; this case has both; why is establishing timeline *before* hypothesizing the key to correct diagnosis?
- Core idea: Timeline-first analysis prevents premature causality assumptions; linking deploy time → alert time → runbook steps creates a testable causal chain that surfaces hidden confounds (e.g., a simultaneous backup job, a query plan change)
- Visual object: Incident timeline (horizontal axis) with deploy marker, alert marker, runbook step sequence, and the causality arc connecting them
- Manim move: trace (chronologically from deploy through alert to runbook) → accumulate (evidence into causal chain) → split (simple hypothesis vs. evidence-backed hypothesis)
- Example seed: Database query latency spikes 10 minutes after a deploy; the obvious culprit is the deploy code; but a timeline reveals the backup job started at the same moment, and the query plan changed to scan more rows—the issue is concurrency, not code
- Length band: 2–3 min
- Still lanes: c2v (timeline with deploy/alert markers, runbook steps, causality arc), raster (initial hypothesis → corrected diagnosis)
- Prerequisites: Basic ops/SRE concepts, understanding of deploys and alerting
- Exclusions: Don't explain the full SRE breakout; don't teach runbook design; don't cover post-mortem writing or blame-free culture
- Score: 9/10

## Candidate 4 — How incremental feature-add teaches agent capability
- Source: `01-guided-demo/README.md`
- Topic: Capability emergence through sequential feature unlock
- Hook: One agent, one task, four runs; flip one boolean each time; the same task output transforms as capabilities unlock
- Key case: Same briefing task (intelligence on three companies) across four stages: baseline chat (hallucinates data) → tools enabled (looks data up) → sub-agents enabled (delegates research) → memory enabled (recalls context)
- The Question: How does agent output quality transform as you add capabilities (tools, sub-agents, memory) one at a time to the same task?
- Core idea: Each SDK primitive (tools, sub-agents, memory) unlocks a qualitatively different behavior: Stage 0 confidently invents, Stage 1 fetches real data, Stage 2 parallelizes specialists, Stage 3 carries context across sessions
- Visual object: Four-panel output comparison (Stage 0, 1, 2, 3) showing the same briefing task output getting progressively detailed, accurate, and contextualized
- Manim move: accumulate (four outputs stacking vertically) → scan (across the four) → morph (content transforming between stages, especially Stage 0→1 hallucinated → real)
- Example seed: Briefing five companies: Stage 0 invents growth percentages (sounds confident, all wrong); Stage 1 fetches real data (slower but accurate); Stage 2 spawns one researcher per company in parallel; Stage 3 recalls "last time you asked about Tinplate, you flagged the profitability gap" and leads with that context
- Length band: 3–5 min
- Still lanes: c2v (task prompt → four stage outputs side-by-side, showing hallucination → data fetch → delegation → context), raster (snippets of each stage's output)
- Prerequisites: Basic understanding of what agents do and what tools/sub-agents are
- Exclusions: Don't teach the SDK code or implementation details; don't dive into any single stage's plumbing; don't explain how to write tools or define sub-agents
- Score: 9/10

The grep results are from the broader working directory, not the workshop corpus. The corpus was supplied inline — I have everything I need from the prompt. Here are two new concepts that pass the bar:

# Agent SDK Workshop Video Ideas

## Candidate 05 — Why parallelism is a prompt problem, not a code problem
- Source: `docs/FAQ.md`
- Topic: Prompt-driven parallelism in multi-agent orchestration
- Hook: You expect to write `asyncio.gather()` to parallelize; instead you edit the system prompt and the SDK parallelizes automatically
- Key case: Briefing five companies — sequential prompt ("research each one at a time") takes five turns; parallel prompt ("spawn one researcher per company in the same turn") runs all five concurrently — same SDK code, different instruction
- The Question: X (need parallel execution) should predict "write concurrent code"; this case achieves parallelism with zero code changes; why does the system prompt determine whether sub-agents run sequentially or in parallel?
- Core idea: Sub-agents spawn when the model emits `Task` tool calls; multiple `Task` calls in a single model turn are run in parallel by the SDK automatically. Whether the orchestrator emits them together or one at a time is a strategy encoded in the system prompt, not application code.
- Visual object: Two turn timelines side by side — sequential (five turns, one Task each) vs parallel (one turn, five simultaneous Tasks) — with wall-clock elapsed time shown on both
- Manim move: split (one sequential timeline → one parallel timeline) → accumulate (five Task emissions collapsing into a single turn) → compare (elapsed-time bars shrinking)
- Example seed: Five company briefings, sequential vs parallel: sequential orchestrator takes ~25 seconds across five API round-trips; parallel orchestrator takes ~6 seconds in one turn — the only difference is "in the same turn" appearing in the system prompt
- Length band: 2–3 min
- Still lanes: c2v (two-column timeline: sequential turn-by-turn vs parallel single-turn burst, with task arrows), raster (before/after system prompt diff showing the one added phrase)
- Prerequisites: Understanding of what sub-agents are; Candidate 4 (capability stages) helps but is not required
- Exclusions: Don't cover async Python internals or thread safety; don't explain Task tool implementation; don't discuss SDK retry or rate-limit behavior
- Score: 9/10

## Candidate 06 — Why the model can't see its own memory guardrail
- Source: `docs/FAQ.md`, `docs/CHEATSHEET.md`
- Topic: Tools vs hooks — model-visible capabilities vs invisible lifecycle callbacks
- Hook: Two mechanisms intercept what an agent does; only one of them the model knows exists
- Key case: Stage 3 memory uses both simultaneously — a `save_memory` tool the model *chooses* to call, and a `UserPromptSubmit` hook that *automatically* injects saved context before every turn without the model's knowledge or consent
- The Question: X (need model to save memories + inject them next session) should predict "one mechanism handles both"; this case splits the task across two entirely different primitives; why does memory require a tool for writing and a hook for reading?
- Core idea: Tools are model-controllable (model decides when to invoke, result returned mid-turn); hooks are SDK-controllable (fire on lifecycle events, invisible to model, can inject context before the model ever sees the prompt). Intentional saving needs the model's agency; guaranteed injection must not depend on it.
- Visual object: Two-lane diagram — Tool lane (model emits call → SDK executes → result returned to model) vs Hook lane (SDK event fires → callback runs → context silently prepended) — with the memory system's write path in one lane and read path in the other
- Manim move: split (one agent interaction → two parallel lanes) → trace (save\_memory call down tool lane; UserPromptSubmit event down hook lane) → overlay (showing next session start: hook fires before model sees anything)
- Example seed: Agent saves "user prefers bullet points" via the memory tool (model's deliberate choice). Next session: before the user types a word, the UserPromptSubmit hook fires, reads the store, and prepends "user prefers bullet points" to the context. Model responds with bullets — not because it remembered, but because it was silently told at session start.
- Length band: 2–3 min
- Still lanes: c2v (two-lane diagram with tool path vs hook path; memory use-case overlaid showing write in tool lane, read in hook lane), raster (hook event table from CHEATSHEET.md)
- Prerequisites: Basic understanding of what tools are; Stage 3 of the guided demo provides useful context
- Exclusions: Don't explain all four hook event types in depth; don't cover PreToolUse/PostToolUse guardrail patterns; don't show raw hook implementation code
- Score: 8/10
