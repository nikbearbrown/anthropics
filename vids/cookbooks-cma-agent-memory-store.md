## cookbooks-cma-agent-memory-store

- **Source path:** claude-cookbooks/managed_agents/CMA_remember_user_preferences.ipynb
- **Teachable claim:** Managed Agents memory stores give each user a persistent shared notebook — the agent reads and writes files at `/mnt/memory/` inside its sandbox, and your application has full read-write access to the same files through the REST API for seeding, auditing, and exporting.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Session 1: shopping assistant learns preferences (size, materials, budget) → writes notes to `/mnt/memory/`
2. Session 2 (new terminal): same agent → memory already there → applies preferences without being told again
3. REST API access: `client.beta.memory_stores.files.retrieve()` showing the written file contents
4. Seeding from application: your app pre-populates known facts before the first session

### Score
- Teachability: 5/5 — the two-session demo is a perfect before/after
- Visual: 4/5 — the memory file written and then read back is concrete and readable
- Pull: 5/5 — persistent user memory is the most-requested agent feature
- Freshness: 5/5 — memory stores are in public beta as of 2026
- **Total: 19/20**
