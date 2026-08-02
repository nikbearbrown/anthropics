## agent-sdk-workshop-four-switches

- **Source path:** agent-sdk-workshop/01-guided-demo/ (config.py, GUIDE.md; breakouts in 02-breakouts/)
- **Teachable claim:** The entire anatomy of a production agent is three boolean switches — the same agent runs four times (baseline chat → +tools → +subagents → +memory), and each run visibly improves at preparing a company briefing, with `config.py` as the only file you ever edit.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Stage 0 run: `./workshop demo` — a plain system-prompted chat confidently guesses; label the failure ("no lookups, no memory")
2. Flip `ENABLE_TOOLS = True` in config.py (one-line diff on screen) → re-run → tool calls scroll; the agent now cites mock data
3. Flip `ENABLE_SUBAGENTS` → the fact-checker specialist catches the planted cross-link (Ironvane's departing CPO appearing in Tinplate's hiring news — the mock data is interlinked on purpose)
4. Flip `ENABLE_MEMORY` → run twice; second run remembers the first (`./workshop reset` shown as the counter-proof)
5. Closer chip: `./workshop demo --show-prompt` — the full context the SDK actually sends, the "no magic" reveal

### Score
- Teachability: 5/5 — one agent, four runs, one switch per run is a perfect pedagogical ladder
- Visual: 5/5 — same-task-better-output progression is inherently before/after cinema
- Pull: 5/5 — "an agent is three booleans" is a clickable, checkable claim
- Freshness: 4/5 — Agent SDK content exists on the channel, but the switch-ladder framing is new
- **Total: 19/20**
