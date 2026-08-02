## quickstarts-managed-agents-chat-sdk

- **Source path:** claude-quickstarts/managed-agents/chat-sdk/
- **Teachable claim:** One Managed Agents session per conversation — paired with Vercel's Chat SDK — produces a research analyst that streams its tool calls and final brief token-by-token, and the same backend handler works for Slack, Teams, Discord, or Telegram by swapping one adapter.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. Chat UI with live tool-call feed: browser chat surface showing web search calls streaming in a side panel
2. Session persistence: closing and reopening the conversation — Managed Agents session resumes
3. Adapter swap: the one-line change that routes the same session to Slack instead of the browser chat
4. Architecture: Next.js + Chat SDK → Managed Agents session → web search → streaming brief

### Score
- Teachability: 4/5 — the adapter pattern for multi-channel deployment is the key insight
- Visual: 4/5 — streaming chat with live tool-call feed is visually rich
- Pull: 4/5 — shipping a chat product on top of Claude Managed Agents is a common goal
- Freshness: 5/5 — Managed Agents + Vercel Chat SDK is a brand-new quickstart
- **Total: 17/20**
