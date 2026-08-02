## sdk-python-examples-web-search

- **Source path:** anthropic-sdk-python/examples/web_search.py
- **Teachable claim:** Claude's built-in web search tool requires zero infrastructure — pass `{"type": "web_search_20250305"}` in the tools array and Claude automatically searches the web, synthesizes results, and cites sources without any custom tool implementation.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–3 min)

### Visual beats
1. Minimal web-search call: one tool definition, no handler code — Claude does all the searching
2. Response anatomy: `web_search_tool_result` block showing actual URLs queried + `text` block with answer
3. Citations in output: Claude citing the sources it consulted — verifiable provenance
4. Streaming version: web search results appearing token-by-token as Claude synthesizes

### Score
- Teachability: 4/5 — "no infrastructure" is the key insight; most developers expect to write a search handler
- Visual: 3/5 — terminal output with citations is functional
- Pull: 5/5 — web search is the most universally requested Claude capability
- Freshness: 4/5 — built-in web search tool is new; the zero-infrastructure framing is the fresh angle
- **Total: 16/20**
