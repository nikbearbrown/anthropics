## agent-sdk-demos-ask-user-question-previews

- **Source path:** claude-agent-sdk-demos/ask-user-question-previews/
- **Teachable claim:** The Agent SDK's `AskUserQuestion` tool can return options as HTML preview cards instead of plain text labels — an agent branding assistant can show rendered mockups of each option before the user picks one, enabling approval-gated agentic workflows with full visual context.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Default AskUserQuestion: plain text option labels — "Option A", "Option B"
2. With `previewFormat: "html"`: each option renders as a styled HTML mockup in the browser
3. The WebSocket round-trip: SDK `canUseTool` callback → browser renders preview → user approves
4. Plan mode steering: agent asks clarifying questions before acting when in plan mode

### Score
- Teachability: 4/5 — HTML preview options is a non-obvious but powerful UX pattern
- Visual: 5/5 — the visual option cards are the entire point and they look great
- Pull: 3/5 — specialized but highly relevant for anyone building approval-gated agents
- Freshness: 5/5 — previewFormat: "html" is a new Agent SDK feature
- **Total: 17/20**
