## cookbooks-session-browser

- **Source path:** claude-cookbooks/claude_agent_sdk/05_Building_a_session_browser.ipynb
- **Teachable claim:** Every Claude Agent SDK conversation is stored as a JSONL transcript on disk with session management functions built in — you can list, rename, fork, and resume past sessions without writing a file parser, which is exactly how Claude Code's own conversation sidebar works.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. JSONL transcript file opened in terminal — the raw storage format, then the abstraction on top
2. Session list with metadata: branch, title, last-modified — the sidebar data model exposed
3. Session fork: branch a past conversation at a specific message, then resume the fork as a live query
4. The connection: "this is the same code Claude Code Desktop uses for its sidebar"

### Score
- Teachability: 4/5 — practical SDK feature with a satisfying "behind the curtain" reveal
- Visual: 3/5 — mostly terminal + JSON, but the fork/resume demo is clear
- Pull: 4/5 — any product built on Claude SDK wants a conversation history UI
- Freshness: 4/5 — session management API is new in SDK v0.1.51
- **Total: 15/20**
