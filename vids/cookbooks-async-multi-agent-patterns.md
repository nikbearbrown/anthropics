## cookbooks-async-multi-agent-patterns

- **Source path:** claude-cookbooks/patterns/agents/async_multi_agent_orchestration.ipynb
- **Teachable claim:** Two async multi-agent patterns from the Claude Opus 4.8 system card — a fixed N-agent team and async subagents spawned on demand — are reproducible with only `asyncio` and the public Anthropic Python SDK, and a domain-free scaffold lets you drop in your own tools and task.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Pattern 1 — fixed N-agent team: `asyncio.gather` runs N agents concurrently on the same task; show the message ordering output and explain why results arrive out-of-order
2. Pattern 2 — async subagents: the orchestrator spawns subagents dynamically based on the task; show the tool call that triggers spawning and the result aggregation
3. The scaffold design: no domain task in the notebook — just messaging and subagent mechanics; show which lines you replace with your own tools
4. Performance: wall-clock comparison of sequential vs. parallel N-agent; the `asyncio` fan-out is the entire speedup; show under-30-second typical runs

### Score
- Teachability: 5/5 — "here's the exact async code from the system card, reproducible with your API key" is a credible claim
- Visual: 4/5 — async message ordering + wall-clock timer is measurable and concrete
- Pull: 4/5 — multi-agent orchestration is the hot topic; system-card-provenance adds credibility
- Freshness: 5/5 — "reproduce the system card patterns yourself" is a novel framing
- **Total: 18/20**
