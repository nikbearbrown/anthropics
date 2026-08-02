## cookbooks-tool-search-embeddings

- **Source path:** claude-cookbooks/tool_use/tool_search_with_embeddings.ipynb
- **Teachable claim:** When an agent has hundreds of tools, front-loading all definitions consumes the context window and raises costs — semantic embedding search retrieves only the 5 most relevant tool definitions at query time, making 1000-tool agents practical without hitting context limits.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The scaling wall: show context token count with 10 tools vs. 100 tools vs. 1000 tools — 100 tool definitions at ~500 tokens each = 50,000 tokens consumed before the user types anything
2. Tool embeddings: `SentenceTransformer` embeds each tool's name + description; query "check current weather" retrieves only the weather, forecast, and alerts tools — not the calendar or database tools
3. Dynamic tool loading: the agent loop embeds the user's message, retrieves top-5 tools, passes only those definitions to the API call; show the token count drop
4. When to use the `describe_tool` alternative: include all tool names in the system prompt + one `describe_tool` tool; Claude calls it to load the full definition on demand — show both patterns side by side

### Score
- Teachability: 5/5 — the "tool definitions eat context" problem is universal; semantic search is the clean solution
- Visual: 4/5 — token counter + tool retrieval heatmap is concrete and measurable
- Pull: 4/5 — anyone building multi-tool agents hits the context wall
- Freshness: 4/5 — tool search is underexplored; embedding approach is new relative to the typical "just add more tools" advice
- **Total: 17/20**
