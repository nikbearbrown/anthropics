## cookbooks-cma-iterate-fix-tests

- **Source path:** claude-cookbooks/managed_agents/CMA_iterate_fix_failing_tests.ipynb
- **Teachable claim:** The core Managed Agents loop — agent + environment + session — is fully captured in the "make failing tests pass" task: the agent runs tests, reads tracebacks, edits code, reruns, repeats until green, all inside its own container.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. Three resources explained with minimal code: `agents.create`, `environments.create`, `sessions.create` — the primitives shown as API calls
2. Test output with two planted bugs: red → agent reads traceback → edits code → green
3. Event stream: each agent action streaming as typed events — bash output, file edits, tool calls
4. The archive call: cleaning up the session after the run — resource lifecycle shown

### Score
- Teachability: 5/5 — "make failing tests pass" is the most graspable agent task possible
- Visual: 4/5 — red → green test progression is the universal developer narrative
- Pull: 4/5 — the iterate loop is the foundation every other Managed Agents cookbook builds on
- Freshness: 5/5 — Managed Agents is brand new; this is the entry-point cookbook
- **Total: 18/20**
