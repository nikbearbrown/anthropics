## cwc-workshop-ship-first-managed-agent

- **Source path:** cwc-workshops/ship-your-first-managed-agent/
- **Teachable claim:** Building a Managed Agent that can grep a 70k-line log, correlate timestamps with deploys, and name the offending commit requires filling in exactly seven functions — `setup_agent`, `setup_environment`, `upload_log`, `start_session`, `stream_reply`, `handle_tool`, `delete_session` — and nothing else.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. The SRE dashboard: metrics, logs, deploys pages running — the "agent offline" panel on the right
2. Seven functions, seven API calls: filling each one in order — the panel comes online one step at a time
3. The agent working: "what caused the latency spike?" → grep → correlate → diff → named commit
4. Function-to-API-call table: each function mapped to its Managed Agents API method — the full surface in one view

### Score
- Teachability: 5/5 — seven functions to a working SRE agent is an irresistible concrete promise
- Visual: 5/5 — the dashboard coming online as each function is filled is a natural narrative
- Pull: 5/5 — the 3am incident story + structured build path is maximally compelling
- Freshness: 5/5 — Managed Agents API is new; this is the official first-agent tutorial
- **Total: 20/20**
