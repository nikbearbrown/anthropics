# cwc-workshops Video Ideas

## Candidate 1 — Why agents forget what you told them (and what to do about it)
- Source: `agents-that-remember/`
- Topic: Cross-session memory in agents—persistence and consolidation
- Hook: Same agent, same person—but tell it something in one session and ask in the next, it has no memory.
- Key case: Session A: "I attended a talk; learned about multi-agent orchestration." Session B (no memory store): "What did they announce?" Agent: "I don't have that context." With memory store: "You mentioned multi-agent orchestration."
- The Question: If both sessions use the same agent, why does amnesia across sessions feel inevitable—and what layer enables recall?
- Core idea: Sessions are isolated by design. A **memory store** adds persistence: the agent can read/write across sessions. The **Dreaming Service** goes further—it reads past transcripts, consolidates them into structured memories, and writes them back. The progression (isolation → persistence → self-improvement) reveals that memory isn't built-in; it's a separate lever you attach.
- Visual object: A timeline showing three sessions (A: agent hears "I use PostgreSQL"; B: asks "what database?"; agent says nothing; C: same question with memory store attached; agent recalls). Below, show the memory-store file tree growing as the agent writes entries.
- Manim move: accumulate
- Example seed: You tell the agent "I prefer async/await over promises" in session 1. Session 2 without memory: "What's your coding style?" returns nothing. With memory store: returns "You prefer async/await."
- Length band: 2–3 min
- Still lanes: c2v with session timeline
- Prerequisites: Claude Managed Agents sessions, basic context isolation concepts
- Exclusions: Dreaming Service implementation, memory CLI commands, multi-store orchestration, the specific `.md` file structure the agent chooses
- Score: 9/10

## Candidate 2 — Six agent variants reveal what prompt changes actually improve output
- Source: `eval-driven-agent-development/`
- Topic: Measuring prompt changes with a two-layer grading system
- Hook: You tweak the system prompt—does it actually help, or did you just shuffle tokens?
- Key case: Naive agent generates a slide deck with poor typography. Add a 2-sentence hint about typography choices. Re-run the eval on the same 10-task suite. The structural grader (XML metrics) + semantic grader (LLM judge on rendered slides) show measurable improvement in readability and layout balance.
- The Question: How do you know a prompt change improves output without manually inspecting every variant—and spending hours doing it?
- Core idea: Split the eval into two layers: **structural** (parse the `.pptx` XML and measure layout metrics programmatically—font consistency, alignment, color contrast) and **semantic** (render the deck and use an LLM to grade visual impact and usability). Now every prompt iteration is measured against the same rubric, not vibed.
- Visual object: A timeline showing six agent variants stacked horizontally (naive → visual → typography → palette → density → QA-loop), with colored bar charts below each showing score deltas across the 10 tasks—which ones improved, which ones regressed.
- Manim move: accumulate
- Example seed: An agent generates a 5-slide financial report. Naive version: Comic Sans, poor contrast, cluttered. Typography pass: serif fonts, improved spacing, readable. Both get parsed; the typography version scores higher on a "readability %" dimension and lower on "text overflow." The delta is visible and measurable.
- Length band: 3–5 min
- Still lanes: raster with score bars
- Prerequisites: LLM-as-judge, iterative prompt improvement, PowerPoint/PPTX structure basics
- Exclusions: The specific grader mechanics (XML parsing libraries), the 10 task prompts themselves, multi-model comparison (that's a separate video)
- Score: 9/10

## Candidate 3 — Coordinating dozens of agents in parallel without blocking
- Source: `research-desk/`
- Topic: Multi-session orchestration—fan-out, parallel execution, result accumulation
- Hook: One agent can't analyze 50 SEC filings in parallel. But dispatch them separately and have the main agent wait for all three to finish at once.
- Key case: Head of research gets the prompt "Sweep NVDA, AMD, and MU; rank by margin durability." It calls a custom `dispatch_analysts` tool with the ticker list. The server intercepts that call, spawns three analyst sessions (each reads 20 pages independently, scores on a rubric, returns a grade). The head waits for all three, sees the accumulated results, then synthesizes: "NVDA (9), AMD (6), MU (4)."
- The Question: How does a single agent coordinate long-running parallel sub-agents without resorting to multiple separate conversations or blocking the whole flow?
- Core idea: A **custom tool** becomes the orchestration trigger. When the agent calls `dispatch_analysts(["NVDA", "AMD", "MU"])`, the server intercepts that call, spawns three independent sessions (each is a full agent with its own context window), monitors them in the background, and resumes the main agent with the results folded back. Accumulation is many independent analyses merging into one decision.
- Visual object: A flow diagram with the head agent at the left, calling a `dispatch_analysts` tool, which splits into three parallel analyst sessions (each with a progress bar), then converging back as a results table that the head reads and synthesizes.
- Manim move: spread
- Example seed: Head agent asked "Which of these 3 candidates is the best hire?" Calls `dispatch_analysts(["Alice", "Bob", "Carol"])`. Server spawns three sessions. Each analyst independently reads a resume (20 pages), grades it on "technical depth," "leadership," "communication." Returns (8, 7, 9). Head resumes: "Carol is the best fit (9)."
- Length band: 3–5 min
- Still lanes: c2v with flow diagram
- Prerequisites: Claude Managed Agents sessions, custom tools, server-side event handling
- Exclusions: Memory stores, outcome grading, weekly memo deployment, MCP + Vault, the specific SEC analysis rubric
- Score: 9/10

## Candidate 4 — The tooling decision that makes agent prompts 10× cheaper
- Source: `agent-decomposition/`
- Topic: Decomposing monolithic agent prompts into tools, skills, and code execution
- Hook: A 402-line system prompt with 12 tools is slow and expensive. A 15-line prompt with the same knowledge split into skills runs faster and gets better answers.
- Key case: One task (daily low-stock sweep) originally made 102 tool calls over 488 seconds. After decomposing the prompt—splitting knowledge into skills, enabling code execution instead of tool calls—the same task runs in 3 bash scripts in ~100 seconds. Same correctness, 5× faster, drastically fewer tokens spent.
- The Question: Why does cutting the system prompt in half while keeping all the knowledge actually improve the agent's reasoning—and make it cheaper?
- Core idea: Three levers trade cost vs. control: **tools** (stateless function calls), **skills** (instructions loaded on-demand), **subagents** (separate agents with their own context). A 402-line monolithic prompt tries to force all knowledge into one window; the decomposed version lets the agent request what it needs when it needs it, keeping context lean and decisions focused. The accumulation of tokens saved across many tasks is the payoff.
- Visual object: A decomposition tree showing the 402-line prompt splitting into a 15-line core + five skill modules (reorder-policy, forecasting, notification-templates, etc.) + the original 12 tools, with cost/latency metrics before and after at each branch.
- Manim move: split
- Example seed: A reorder-policy skill (200 lines of business rules) is uploaded separately. The core prompt shrinks to: "use reorder-policy skill to decide stock levels." Agent loads the skill only for reorder tasks, keeping context budget free for detection and alerting.
- Length band: 3–5 min
- Still lanes: raster with prompt-size bars and cost deltas
- Prerequisites: Claude Managed Agents, skills, multi-task agents, tool-call tracing
- Exclusions: The full 12-tool API, the complete eval-suite mechanics, how to write a skill from scratch
- Score: 8/10

## Candidate 5 — Finding the cheapest model that actually solves your task
- Source: `rightmodel/`
- Topic: Model selection through empirical eval sweeps—the pareto frontier
- Hook: Claude Opus is smartest but costs 5× more. Haiku is cheap. You have no idea which one makes sense for your task.
- Key case: An LLM eval suite on a customer-support classification task: Opus scores 98% accuracy, costs $0.08 per call, takes 2 seconds. Haiku: 82% accuracy, $0.01 per call, 0.3 seconds. Sonnet: 90% accuracy, $0.04, 0.8 seconds. You run the sweep; plot the three on a 2D graph (cost on x, accuracy on y); the pareto frontier passes through Sonnet—96% is "good enough," and you save $0.04 per call across 100,000 calls.
- The Question: How do you know which model to use for a task without trying them all and paying for them all?
- Core idea: Run the same eval suite against multiple models (and inference parameters like extended thinking, effort level). Plot quality (accuracy %) vs. cost ($) and latency (s). The **pareto frontier** is the curve of non-dominated points—you can't improve accuracy without paying more or waiting longer. Your task's optimal model sits on that frontier.
- Visual object: A 2D scatter plot with models as colored dots (Opus / Sonnet / Haiku, maybe Claude 3.5), axes labeled cost (x) and accuracy (y), a pareto frontier curve passing through the best points, and a highlight on the model that wins your specific task's cost-quality tradeoff.
- Manim move: accumulate
- Example seed: Handwriting-recognition task. Opus (95%, $0.10), Sonnet (91%, $0.05), Haiku (78%, $0.01). The pareto frontier shows Sonnet is the rational choice—91% is excellent for handwriting, saves $0.05, and frees token budget for other tasks.
- Length band: 2–3 min
- Still lanes: raster with pareto scatter plot
- Prerequisites: Basic eval metrics (accuracy, cost, latency), Claude model lineup knowledge
- Exclusions: How to construct the eval itself, extended thinking vs. low-effort mechanics, batch processing for cost reduction, quantitative ROI of quality gains
- Score: 8/10

## Candidate 06 — Why your agent config needs a 30-second test before a 5-minute one
- Source: `agent-battle/`
- Topic: Decision probes as a fast pre-flight for expensive agent runs
- Hook: Every prompt tweak costs 5 minutes of real game time — but most config changes fail for the same 3 behavioral reasons you could catch in 30 seconds.
- Key case: A naive agent gets diamonds but "chats too much, polls state redundantly, and doesn't relocate after veins." The `--eval` mode fires 10 single-turn decision probes in ~30 s: "Should you relocate after a vein is exhausted?" Probes 4 and 7 fail. Fix the system prompt; probes pass. Only then commit to the 5-minute run.
- The Question: If the full run fails for the same behavioral reasons every time, why can't you see those reasons without paying for the whole game?
- Core idea: Decision probes are single-turn behavioral assertions ("Given this state, what do you do?") — each targets one failure mode in isolation with no game overhead. A full run adds variance (vein luck, world seed, timing) that obscures behavioral signal; probes isolate causation. Running 10 probes in 30 s gives you pass/fail on the specific decisions that determine outcome before you pay for outcome measurement.
- Visual object: Two horizontal timelines: top = 10 probe dots firing along a 30-second bar (each dot turns green or red); bottom = a single 5-minute bar. A vertical arrow from the moment all probes go green pointing down: "commit to full run."
- Manim move: accumulate
- Example seed: Probe 1 — "You've mined a vein to exhaustion. Next action?" Agent A: "Mine adjacent block." Fails. Prompt adds: "relocate after exhaustion." Agent B: "Move 15 blocks and scan." Passes. Full run only now.
- Length band: 2–3 min
- Still lanes: raster with probe results grid
- Prerequisites: Agent evaluation basics, system-prompt iteration, cost-vs-fidelity tradeoffs
- Exclusions: Minecraft mechanics, MCP wiring, leaderboard scoring rules, how the probes themselves are authored
- Score: 8/10
