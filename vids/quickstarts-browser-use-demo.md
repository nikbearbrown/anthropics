## quickstarts-browser-use-demo

- **Source path:** claude-quickstarts/browser-use-demo/
- **Teachable claim:** Browser automation with Claude requires a Playwright-backed tool that can navigate, inspect DOM elements, extract content, and fill forms — the demo shows the complete reference implementation for giving Claude a browser as a first-class tool.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. Claude's tool calls: navigate → inspect DOM → extract text → fill form — browser state visible in parallel
2. Custom Playwright tool definition: the schema that describes browser actions to Claude
3. Resilience pattern: what happens when a page element isn't found — error handling and retry
4. DOM extraction: how Claude gets structured data from unstructured web pages

### Score
- Teachability: 4/5 — browser automation as a Claude tool is a concrete and buildable pattern
- Visual: 5/5 — the browser visibly responding to Claude's commands is inherently compelling
- Pull: 4/5 — browser automation is one of the highest-value agentic use cases
- Freshness: 4/5 — the Playwright-backed custom tool pattern is well-specified but new
- **Total: 17/20**
