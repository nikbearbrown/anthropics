## agent-sdk-demos-simple-chatapp

- **Source path:** claude-agent-sdk-demos/simple-chatapp/README.md
- **Teachable claim:** An Express + WebSocket server backed by the Claude Agent SDK, with a React frontend, shows the four production gaps every chat app must close — session persistence across server restarts, transcript syncing for multi-turn SDK conversations, user authentication, and agent isolation in a separate container.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. `npm run dev` → `http://localhost:5173`; create a chat; ask a question with tools enabled; show the `tool_use` WebSocket event rendering in the UI as Claude uses Bash
2. The transcript syncing gap: stop the server; restart it; the in-memory `ChatStore` is gone — conversation lost; show the fix (persistent storage + transcript restore from SDK's internal conversation state)
3. Architecture diagram from the README: React → WebSocket → Express → Claude Agent SDK → Claude API; highlight where the API key stays (server side only) and where the agent isolation boundary should be (separate container)
4. Production gap checklist: run through the four improvements from the README — storage, transcript sync, auth, isolation — as a "what this demo doesn't do and why that matters" beat

### Score
- Teachability: 5/5 — the "here are the four production gaps this demo intentionally leaves open" framing is the best possible tutorial structure
- Visual: 3/5 — chat app is familiar; the tool_use WebSocket event rendering is the interesting visual
- Pull: 4/5 — every developer wants to build a Claude chat app; this is the canonical starting point
- Freshness: 3/5 — chat apps exist; the Claude Agent SDK backing and explicit production gap list are the fresh angle
- **Total: 15/20**
