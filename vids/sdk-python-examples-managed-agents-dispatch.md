## sdk-python-examples-managed-agents-dispatch

- **Source path:** anthropic-sdk-python/examples/managed-agents-worker-dispatch.py
- **Teachable claim:** Worker dispatch with Managed Agents — the coordinator session calls a custom tool, your server fans out to N worker sessions, waits for all to complete, returns a merged result — is the core pattern for parallelizing long-running agent work.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. Coordinator calls dispatch tool → server fans out 3 worker sessions simultaneously — concurrency shown
2. Worker sessions running: each in its own terminal tab, all progressing in parallel
3. Merge: all three results collected → coordinator receives merged result → produces final output
4. Bounded concurrency: the semaphore limiting parallel workers to prevent API rate limits

### Score
- Teachability: 5/5 — fan-out worker dispatch is the most important scalable agent architecture pattern
- Visual: 4/5 — parallel sessions running simultaneously is visually compelling
- Pull: 4/5 — any production agent that processes many items in parallel needs this
- Freshness: 5/5 — Managed Agents worker dispatch is brand new
- **Total: 18/20**
