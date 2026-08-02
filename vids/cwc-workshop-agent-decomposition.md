## cwc-workshop-agent-decomposition

- **Source path:** cwc-workshops/agent-decomposition/
- **Teachable claim:** A 402-line system prompt with 12 tools is not a more powerful agent than a clean one — decomposing it into Skills, code execution, and one well-placed subagent improves eval scores from 71% to over 90% while making the system auditable.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. The monolith: 402-line system prompt + 12 tools — the before state, eval score 71%
2. Skills extraction: three capabilities pulled into named Skills uploaded to Managed Agents — code shown
3. Eval run after each decomposition step: scores improving incrementally
4. The failing task that drove decomposition: F1 (wall budget), F2 (qualitative confidence) — root causes diagnosed

### Score
- Teachability: 5/5 — the eval-driven decomposition story is the key lesson for production agents
- Visual: 4/5 — score progression across decomposition steps is clean and readable
- Pull: 4/5 — every team with a struggling agent will recognize this scenario
- Freshness: 5/5 — Skills API + eval-driven decomposition is cutting-edge Managed Agents work
- **Total: 18/20**
