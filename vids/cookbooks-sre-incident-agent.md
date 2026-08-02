## cookbooks-sre-incident-agent

- **Source path:** claude-cookbooks/claude_agent_sdk/03_The_site_reliability_agent.ipynb
- **Teachable claim:** An SRE incident response agent can autonomously grep 70k-line logs inside a cloud sandbox, correlate metrics with deploy timestamps, and name the commit that caused the latency spike — the 40-minute 3am hunt, automated.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. Problem setup: dashboard showing latency spike → 40-minute manual grep hunt → agent does it in 90 seconds
2. Agent tool calls scrolling: ls → grep → read log → correlate timestamps → fetch diff
3. The incriminating commit surfaced: agent output naming the N+1 query and the commit hash
4. Architecture: local tools (metrics, deploys) + file-uploaded logs in agent's sandbox

### Score
- Teachability: 5/5 — the pain is universal and the resolution is dramatic
- Visual: 5/5 — tool-call stream tells the detective story
- Pull: 5/5 — every ops engineer wants this; the 3am pager story is the hook
- Freshness: 4/5 — agentic SRE is still novel territory
- **Total: 19/20**
