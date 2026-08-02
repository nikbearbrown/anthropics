## C06 — Build a Multi-Agent Research System in 50 Lines

- **slug:** claude-agent-sdk-multi-agent-pattern
- **source:** ../anthropics/claude-agent-sdk-demos/research-agent/README.md + claude-agent-sdk-python/README.md
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code)
- **premise:** The Claude Agent SDK lets you spawn parallel subagent workers with a single `query()` call — a coordinator breaks a topic, fires off parallel researchers, and synthesizes. The pattern is 3 functions in ~50 lines.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** A multi-agent research pipeline is not hundreds of lines of orchestration code — the Agent SDK's async iterator pattern makes coordinator + parallel workers a 3-function Python module.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Build a multi-agent research system with the Claude Agent SDK`
- topic: `CLAUDE SDK · Multi-Agent Pattern`
- segment: `Coordinator Plus Workers`
- greeting: `Hej, Liam` (Wagwan check: not 0)

### CLI spine (required for cli-scout cards)
INTRO → PROBLEM (research is slow when done linearly; parallel subagents can fan out simultaneously) → CLI LOOP: ASK (type the `query()` coordinator call) → CODE (show the 3-function structure: `research_topic`, `spawn_workers`, `synthesize`) → OUTPUT (the animated call graph showing parallel execution) → CHANGE (add one more subagent and watch wall-clock time not change) → SUMMARY → NEXT STEPS → OUTRO

### Hook
Research tools that call LLMs one-at-a-time are leaving parallelism on the table. The SDK's async iterator means you can fire 5 parallel researchers and collect results as they stream in — with no concurrency primitives you have to write yourself.

### The artifact
A visual call graph (animated Remotion scene): the coordinator node fires arrows to 5 simultaneous researcher nodes, each streamed response arrives as a tick on a timeline, all flowing back to a synthesis node. Wall-clock time bar shows the parallel speedup vs serial execution.

### Prompt seed
```
claude "Using the Python Claude Agent SDK, build a research coordinator that:
1. Takes a topic
2. Breaks it into 3-5 subtopics
3. Spawns a parallel async query() worker for each subtopic
4. Collects all results and synthesizes a report
Keep the whole thing under 60 lines."
```

### Read / check
Verify: (1) the coordinator uses `anyio.gather()` or equivalent to truly parallelize; (2) the output is a synthesized report, not just concatenated results; (3) wall-clock time for 5 workers is close to max(individual_times), not sum.

### Human supplies
Nothing — fully synthetic. The demo repo has a working reference implementation. The animated call graph is the output beat; no real API calls needed for the visualization.

### Output medium
Remotion animated call graph (coordinator + worker nodes with streaming ticks, wall-clock timeline)

### The change
Add error handling: one of the 5 worker calls raises an exception. Show how `try/except` inside the async worker prevents the coordinator from failing entirely — the synthesis continues with 4 results.

### Teardown angle
The real design judgment: when does parallel fanout help vs hurt? The cost is proportional to the number of workers (API calls), not the wall clock time. For a 5-worker system, you pay 5x the token cost to get 5x the parallelism — the right trade when synthesis quality scales with input breadth.

### Exclusions
No streaming implementation (different video). No authentication setup. No cost/token monitoring. No Bedrock or Vertex routing.

### Score: 8/10 (BUILD bar: artifact is runnable in <60 lines; output is the lesson)

### Scores (rubric dimensions)
- Teachability: 4/5 — the pattern is concrete and reusable
- Visual potential: 4/5 — the parallel call graph is a strong animated diagram
- Audience pull: 4/5 — SDK users want the copy-pasteable pattern
- Freshness: 4/5 — multi-agent is talked about; the exact SDK pattern is less shown
- **Total: 16/20**
