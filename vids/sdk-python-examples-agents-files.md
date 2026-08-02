## sdk-python-examples-agents-files

- **Source path:** anthropic-sdk-python/examples/agents_with_files.py
- **Teachable claim:** The Anthropic Python SDK's agent loop with file uploads — uploading a file via the Files API, passing the file ID in the message, having the agent read and process it — is the foundational pattern for all document-processing agents.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. File upload: `client.beta.files.upload(file=open("report.pdf", "rb"))` → file ID returned
2. File ID in agent message: passing the file reference (not the bytes) in the user message
3. Agent processing: reading the file contents inside the agent's context, then answering questions
4. File lifecycle: creating, using, then deleting — the full resource lifecycle shown

### Score
- Teachability: 4/5 — Files API is the clean way to pass large documents to agents
- Visual: 3/5 — mostly terminal, but the file-ID pattern is the lesson
- Pull: 4/5 — document-processing agents are extremely common
- Freshness: 4/5 — Files API with agents is a new SDK pattern
- **Total: 15/20**
