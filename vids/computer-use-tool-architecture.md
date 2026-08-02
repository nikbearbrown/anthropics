## C19 — Computer Use: Why Claude Needs Eyes to Use a Computer

- **slug:** computer-use-tool-architecture
- **source:** ../anthropics/claude-quickstarts/computer-use-demo/README.md + ../claude-quickstarts/computer-use-best-practices/README.md
- **bucket:** BUILD-WITH-CLAUDE / SDK → cli-scout lens → terminal-screencast (claude-cli builder)
- **Lane:** BUILD (Claude Code / API)
- **premise:** Claude's computer use capability requires a feedback loop: screenshot → Claude decides next action → action executed → screenshot again. The architecture is not "Claude controls a computer" but "Claude navigates by sight, one decision at a time."
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** Computer use agents fail at scale because they treat the computer like a function call (send command, get result) rather than a visual environment (look, decide, act, look again). The best-practices guide's 7 patterns — image sizing, prompt caching, batched tool calls, trajectory recording — each fix a specific failure mode of the naive approach.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `How does Claude actually see and control a computer?`
- topic: `CLAUDE · Computer Use Architecture`
- segment: `Navigate by Sight`
- greeting: `Kumusta, Liam` (Wagwan check: not 0)

### CLI spine
INTRO → PROBLEM (the naive agent: Claude calls click(x,y) blindly → misses, crashes, loops) → CLI LOOP: ASK (set up the screenshot→decide→act loop from the best-practices quickstart) → CODE (the core loop: `screenshot()` → `client.messages.create(screenshot)` → `parse_action()` → `execute_action()` → repeat) → OUTPUT (screen recording: the demo container navigating a browser, zooming in on a UI element to identify coordinates) → CHANGE (add prompt caching: the system prompt and screenshot are cached between turns, reducing cost by ~70%) → SUMMARY → NEXT STEPS → OUTRO

### Hook
Claude is not reading the DOM — it's looking at pixels. Every click coordinate it generates comes from visual inference, not element inspection. That's why image sizing matters: too small, Claude misjudges coordinates; too large, it exceeds context limits.

### The artifact
Screen recording: the computer use demo container navigating a browser to a target URL, taking screenshots at each step, and correctly clicking UI elements. The trajectory is recorded as a JSON log (each action + the screenshot that prompted it).

### Prompt seed
```
claude "Set up a minimal computer use loop that:
1. Takes a screenshot of the current screen
2. Sends it to Claude with the task: 'Click the search bar and type hello'
3. Executes Claude's action response
4. Takes another screenshot and repeats until Claude says DONE
Use the anthropic Python SDK and the computer_use_20251124 tool."
```

### Read / check
Verify: (1) the screenshot is resized to the correct dimensions before sending (not full 4K); (2) the action parser handles all 4 action types: mouse_move, left_click, type, screenshot; (3) the loop terminates when Claude returns a stop_reason of "end_turn" with no tool call.

### Human supplies
The sandboxed Docker container from the best-practices quickstart is required for a real screen recording (run it in a VM — the README is explicit about the security risk of running against a real desktop). A synthetic animation of the screenshot→action→screenshot loop is acceptable as a stand-in.

### Output medium
Screen recording mp4 (computer use demo navigating in the container) + Onda code-block for the core loop

### The change
Add zoom actions: the 2025 update added `computer_use_20251124` with zoom support — demonstrate zooming in to a small UI element to get accurate coordinates before clicking, then zooming back out.

### Teardown angle
The design judgment: the computer use demo is containerized for a reason — an agent with mouse/keyboard control of a real desktop has full access to everything on that desktop. The trajectory recording pattern (log every action + screenshot) is not optional overhead; it's the only way to audit what happened after a run.

### Exclusions
No browser use comparison (Playwright vs screenshot agent — different video). No cost analysis. No multi-step planning. No error recovery patterns.

### Score: 7/10

### Scores (rubric dimensions)
- Teachability: 4/5 — the screenshot loop is immediately clear; the "navigate by sight" framing is the insight
- Visual potential: 4/5 — the screen recording of Claude navigating a browser is compelling motion
- Audience pull: 4/5 — computer use is one of Claude's most dramatic capabilities
- Freshness: 3/5 — computer use demos exist; the architecture + best-practices angle is less shown
- **Total: 15/20**
