## agent-sdk-python-hooks-budget

- **Source path:** claude-agent-sdk-python/examples/hooks.py
- **Teachable claim:** Claude Agent SDK hooks intercept every tool call before and after execution — a `PreToolUse` hook can block, redirect, or log any tool call by returning `{decision:"block"}` or `{continue:true}`, and `max_budget_usd` terminates the agent when it would exceed a cost cap.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. Hook anatomy: `hooks.PreToolUse` with a matcher (`"Write|Edit|MultiEdit"`) and an async callback — return `{continue:true}` to allow or `{decision:"block", stopReason:"..."}` to deny
2. Security demo: a hook restricts `.js`/`.ts` writes to `custom_scripts/` only; attempt to write outside — hook fires, blocks, logs the blocked path
3. Budget control: `max_budget_usd=0.10` vs. `0.0001`; the tight budget triggers early termination with a `BudgetExceeded` result message; show the `total_cost_usd` in the ResultMessage
4. Hooks as audit log: a `PostToolUse` hook logs every tool call to a file; replay the log to reconstruct exactly what the agent did

### Score
- Teachability: 5/5 — `PreToolUse` hooks are the safety primitive every production agent needs
- Visual: 3/5 — terminal output of blocked calls and cost termination is readable but not visual
- Pull: 4/5 — every production agent deployment needs cost control and tool auditing
- Freshness: 4/5 — hooks are in the SDK but rarely demonstrated end-to-end
- **Total: 16/20**
