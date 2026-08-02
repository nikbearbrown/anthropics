## anthropic-sdk-managed-agents-observe

- **Source path:** anthropic-sdk-python/examples/managed-agents-observe-tool-calls.py
- **Teachable claim:** `client.beta.sessions.events.tool_runner()` is the per-call observation path — it attaches to a running session's event stream, executes each tool locally, and yields one `DispatchedToolCall` per completed call, so you can audit, log, or react to every tool call without managing lease heartbeats yourself.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The two surfaces: `tool_runner()` (observe every call on a session you own) vs. `EnvironmentWorker` (self-hosted worker with lease management) — show the decision tree
2. Primary scenario: create agent + session, send a prompt, `async for call in tool_runner(session)` — each `DispatchedToolCall` lands in order; show the call name, input, and result
3. Observer pattern: add a logging callback inside the loop — every bash call, every read, timestamped; the callback receives the full tool input before execution
4. When NOT to use tool_runner: the self-hosted worker scenario (`observe_as_self_hosted_worker()`) requires composing tool_runner with a heartbeat task — show when the complexity is worth it

### Score
- Teachability: 5/5 — "tool_runner for observation, EnvironmentWorker for hosting" is a sharp API surface decision
- Visual: 3/5 — tool call log output is readable but not visually rich
- Pull: 4/5 — observability and auditing are production requirements for every serious agent deployment
- Freshness: 5/5 — `tool_runner()` is very new SDK surface with no public coverage
- **Total: 17/20**
