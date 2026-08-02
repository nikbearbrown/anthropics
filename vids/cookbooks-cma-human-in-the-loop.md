## cookbooks-cma-human-in-the-loop

- **Source path:** claude-cookbooks/managed_agents/CMA_gate_human_in_the_loop.ipynb
- **Teachable claim:** Custom tools in Managed Agents are not just tool calls — they pause the agent's session and emit an event your application handles; this is the seam where human approval, audit logging, and business logic take over from the AI.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Event stream diagram: agent calls `escalate()` → session pauses → `agent.custom_tool_use` event appears → human decides → `user.custom_tool_result` sent → session resumes
2. Expense approver live: receipts fed in → agent decides autonomously on clear cases, escalates ambiguous ones
3. Code: two custom tool declarations (`decide` and `escalate`) with JSON schemas — the minimal interface
4. Policy file: showing how the agent reads `policy.yaml` to calibrate when to escalate vs. decide

### Score
- Teachability: 5/5 — custom tools as "pause and hand to human" is the architectural insight
- Visual: 4/5 — the event stream pause/resume is inherently dramatic to show
- Pull: 5/5 — human-in-the-loop is the #1 requirement for enterprise AI deployments
- Freshness: 5/5 — Managed Agents custom tools are brand new
- **Total: 19/20**
