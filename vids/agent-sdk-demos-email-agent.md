## agent-sdk-demos-email-agent

- **Source path:** claude-agent-sdk-demos/email-agent/
- **Teachable claim:** An IMAP email assistant built on the Claude Agent SDK can display your inbox, perform agentic search across thousands of emails, and provide AI-powered assistance — the full architecture (client UI + TypeScript server + IMAP tool) is 200 lines.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The inbox UI loading: email list with subject, sender, date — driven by IMAP tool call
2. Agentic search: "find all emails about the Q3 report" → agent issues multiple IMAP searches → results assembled
3. Architecture: client ↔ WebSocket server ↔ Agent SDK ↔ IMAP server — the three-layer stack
4. Custom IMAP tool definition: the schema that gives the agent email access

### Score
- Teachability: 3/5 — email agent is a practical demo but the pattern (custom IMAP tool) is the lesson
- Visual: 3/5 — email UI is functional but not visually distinctive
- Pull: 3/5 — email automation is universally relatable
- Freshness: 3/5 — email agents are established; this is a clean reference implementation
- **Total: 12/20**
