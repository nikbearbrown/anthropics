## cwc-workshop-research-desk-sec-agents

- **Source path:** cwc-workshops/research-desk/
- **Teachable claim:** An equity research desk that dispatches one SEC filing analyst per ticker — each running as a Managed Agent session with sub-agents for financials and risk — turns a one-at-a-time bottleneck into a concurrent fan-out where the orchestrator's laptop lid can close and agents keep running.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The console: "Sweep NVDA, AMD, and MU" → three analyst sessions fire in parallel — progress bars appearing
2. Sub-agent delegation: each analyst spawns a financials extractor and a risk analyst sub-agent
3. Memory browser: the shared desk memory showing what past analyses taught the head of research
4. Scheduled deployment: container running a weekly memo without anyone present — the always-on pattern

### Score
- Teachability: 5/5 — fan-out/fan-in long-running agents is the most architecturally important pattern
- Visual: 5/5 — the parallel analyst sessions + memory browser + console links are all visual
- Pull: 5/5 — finance professionals + AI builders both want this
- Freshness: 5/5 — long-running server-side agent orchestration is frontier territory
- **Total: 20/20**
