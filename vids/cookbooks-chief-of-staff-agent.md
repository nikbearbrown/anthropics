## cookbooks-chief-of-staff-agent

- **Source path:** claude-cookbooks/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb
- **Teachable claim:** The Claude Agent SDK brings Claude Code's own capabilities — CLAUDE.md persistent memory, hooks for interception, MCP connections — into a programmatic headless API, so your agent can do everything Claude Code does without the UI.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. CLAUDE.md as agent memory: the file is present in the working directory → agent reads it on init → consistent behavior across runs
2. Subagent spawning: coordinator agent dispatches specialized subagents for finance, HR, and ops domains
3. Hook interception: `UserPromptSubmit` hook shown intercepting a message before the agent sees it
4. Architecture diagram: coordinator → specialist agents → tool results → synthesized executive brief

### Score
- Teachability: 5/5 — CLAUDE.md as programmatic agent memory is the key aha
- Visual: 4/5 — multi-agent architecture diagram + live subagent output streams
- Pull: 4/5 — every enterprise agent builder is solving this problem
- Freshness: 5/5 — Claude Agent SDK feature parity with Claude Code is new and underappreciated
- **Total: 18/20**
