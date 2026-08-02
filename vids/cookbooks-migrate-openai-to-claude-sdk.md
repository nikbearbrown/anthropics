## cookbooks-migrate-openai-to-claude-sdk

- **Source path:** claude-cookbooks/claude_agent_sdk/04_migrating_from_openai_agents_sdk.ipynb
- **Teachable claim:** Migrating from the OpenAI Agents SDK to Claude's is mostly a primitive rename — `@function_tool` → `@tool`, `Runner.run` → `ClaudeSDKClient` — but you gain built-in Read/Edit/Bash tools, automatic prompt caching, and an OTel-native audit trail.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. Side-by-side diff: same expense approval agent in OpenAI SDK vs. Claude SDK — line-by-line comparison
2. Migration map table: `@function_tool` → `@tool`, guardrails → plain functions, `Runner.run` → context manager
3. What you gain: built-in tools (Read, Edit, Bash, Grep) that OpenAI SDK doesn't have — shown in terminal
4. OTel trace: Claude SDK emitting spans to Grafana vs. OpenAI's proprietary trace dashboard

### Score
- Teachability: 5/5 — concrete migration path with a side-by-side diff is the best tutorial format
- Visual: 4/5 — code diffs and migration tables are highly scannable on screen
- Pull: 4/5 — anyone who used OpenAI agents wants to know what they're getting into
- Freshness: 5/5 — Claude Agent SDK migration is brand new territory
- **Total: 18/20**
