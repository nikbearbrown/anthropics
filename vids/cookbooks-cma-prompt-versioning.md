## cookbooks-cma-prompt-versioning

- **Source path:** claude-cookbooks/managed_agents/CMA_prompt_versioning_and_rollback.ipynb
- **Teachable claim:** Managed Agents stores your agent's system prompt server-side with immutable version numbers — rolling back a bad prompt change means pointing callers at v1 by ID, no deployment required.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Traditional prompt-in-code: change → PR → CI → deploy → rollback = same path — timeline showing slowness
2. Managed Agents: `agents.update` → new version ID → running sessions choose version by ID — instant rollback
3. Live eval: agent v1 vs. v2 scored against a labeled test set — scores printed, regression visible
4. Rollback: one API call to point sessions back at v1 — before/after scores restored

### Score
- Teachability: 4/5 — the version-number-vs-code-deploy comparison is the key insight
- Visual: 3/5 — mostly terminal + scores, but the rollback moment is punchy
- Pull: 4/5 — prompt management in production is a real pain point for ML teams
- Freshness: 5/5 — server-side prompt versioning is a new Managed Agents primitive
- **Total: 16/20**
