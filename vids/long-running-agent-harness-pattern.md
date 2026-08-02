## C11 — The Quality Loop: How to Make an Agent Actually Finish

- **slug:** long-running-agent-harness-pattern
- **source:** ../anthropics/cwc-long-running-agents/README.md
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code)
- **premise:** Most Claude Code agents fail at long tasks because the agent itself decides when it's "done." The quality loop pattern (Default-FAIL contract + fresh-context evaluator + agent-maintained handoff) fixes this by separating the agent that builds from the agent that grades.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** A long-running agent becomes reliable when you add ONE design constraint: the agent that builds cannot grade its own work. A separate evaluator subagent — with no write tools — reads the deliverable and checks it against explicit criteria.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Why does my Claude Code agent always think it finished when it hasn't?`
- topic: `CLAUDE CODE · Long-Running Agents`
- segment: `The Quality Loop Pattern`
- greeting: `Bula, Liam` (Wagwan check: not 0)

### CLI spine
INTRO → PROBLEM (agent self-certifies completion; Default-PASS problem) → CLI LOOP: ASK (copy the Default-FAIL hook + evaluator.md into project) → CODE (show the 3 hook files: `track-read.sh`, `stop-check.sh`, `operator-pause.sh` — each is one function) → OUTPUT (animated Remotion diagram: builder agent → git commit → evaluator agent reads fresh → returns PASS/FAIL → loop or stop) → CHANGE (add a second criterion: test coverage must be above 80% before the evaluator passes) → SUMMARY → NEXT STEPS → OUTRO

### Hook
Your agent says "done" and you open the PR and find it missed 3 requirements. The fix is architectural, not a better prompt: separate the builder from the grader.

### The artifact
Animated Remotion diagram showing the quality loop: Builder (with tools: Read, Write, Bash) → produces artifact → commits to git → Evaluator (Read-only, no Write tools) reads fresh from git → checks criteria → returns PASS or FAIL → loop back or stop. The Default-FAIL state shown as a locked checkbox before evidence is opened.

### Prompt seed
```
claude "Set up the cwc-long-running-agents quality loop in this project.
1. Copy the Default-FAIL stop-check hook
2. Create an agents/evaluator.md that grades against these 3 criteria: [LIST]
3. Show me how to run it headless with claude -p"
```

### Read / check
Verify: (1) the evaluator agent has no Write/Edit tools in its permissions; (2) the stop-check reads from a file the builder writes, not from the builder's own self-report; (3) the loop terminates (max-turns set).

### Human supplies
Nothing — fully synthetic. The repo has working examples; the diagram is the animated payoff.

### Output medium
Remotion animated loop diagram (builder → evaluator → loop/stop) + Onda code-block for the hook files

### The change
Add the operator-pause hook: the builder stops every N turns and waits for a human signal before continuing — useful for high-stakes automated tasks.

### Teardown angle
The design judgment: why two agents? Because the evaluator grading from a fresh context window prevents the builder from contaminating the grade with its own confident reasoning. Separate context = independent judgment.

### Exclusions
No Agent SDK translation (separate video). No cost analysis. No multi-project harness. No RLHF comparison.

### Score: 8/10

### Scores (rubric dimensions)
- Teachability: 5/5 — the Default-FAIL pattern is immediately applicable
- Visual potential: 4/5 — the builder/evaluator loop diagram is a clean animated diagram
- Audience pull: 4/5 — any Claude Code user who runs multi-step agents wants this
- Freshness: 4/5 — the pattern is from an Anthropic blog post; the video distillation is new
- **Total: 17/20**
