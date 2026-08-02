## cookbooks-hosting-the-agent

- **Source path:** claude-cookbooks/claude_agent_sdk/07_Hosting_the_agent.ipynb
- **Teachable claim:** The same Claude Agent SDK research agent ships through three hosting tiers — Docker on a single VM, Modal serverless, Kubernetes pod-per-session — and only the operational machinery around the container changes; the agent code and HTTP interface contract are identical across all three.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The mental model: three nouns — process (Python + SDK), session (conversation on disk), container (packaged process); show how `resume=` reconnects to a persisted session
2. Tier 1 — Docker: `docker build -f hosting/Dockerfile`, `docker-compose up`; POST `/sessions/{id}/messages` returns SSE stream; the `GET /health` liveness check
3. Tier 2 — Modal: `modal deploy`; Modal hands out a public tunnel; `AGENT_AUTH_TOKEN` as the minimal auth shim; ephemeral sandbox vs. persistent volume
4. Tier 3 — Kubernetes: pod-per-session pattern; `CLAUDE_CONFIG_DIR=/data` mounted volume; the gateway that scopes session IDs to authenticated callers — the security boundary the other tiers skip

### Score
- Teachability: 5/5 — the "a Claude agent IS a process" mental model resolves the in-process SDK confusion
- Visual: 4/5 — three-tier progression with identical API contract is clean before/after cinema
- Pull: 5/5 — everyone who built the one-liner agent immediately asks "how do I ship this?"
- Freshness: 4/5 — hosting patterns exist for web apps but the Agent SDK process model is new
- **Total: 18/20**
