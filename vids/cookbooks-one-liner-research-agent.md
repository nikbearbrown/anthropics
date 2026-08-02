## cookbooks-one-liner-research-agent

- **Source path:** claude-cookbooks/claude_agent_sdk/00_The_one_liner_research_agent.ipynb
- **Teachable claim:** A functional web-searching research agent requires literally three lines of Claude Agent SDK code — `query()` with `allowed_tools=["WebSearch"]` — and the agent autonomously decides what to search, how many times, and when it has enough to answer.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Three-line agent code in the terminal → run → watch tool calls scroll in real-time
2. Activity visualization: timeline of web search calls with queries shown — the agent's decision trace
3. Stateless vs. stateful: `query()` for one-off research vs. `ClaudeSDKClient` for multi-turn — when to use each
4. Upgrade path: adding system prompt + Read tool for multimodal research (chart analysis + web search)

### Score
- Teachability: 5/5 — three lines to a working agent is a powerful concrete claim
- Visual: 5/5 — live tool-call stream is inherently cinematic
- Pull: 5/5 — the "from zero to agent" arc earns attention immediately
- Freshness: 5/5 — Claude Agent SDK is brand new
- **Total: 20/20**
