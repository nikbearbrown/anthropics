## agent-sdk-demos-resume-generator

- **Source path:** claude-agent-sdk-demos/resume-generator/
- **Teachable claim:** A resume generator that web-searches a person's name across LinkedIn, GitHub, and news — then assembles the findings into a one-page `.docx` — is 30 lines of Claude Agent SDK code and demonstrates the research-then-format pattern at its simplest.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. Input: name → agent begins searching LinkedIn, GitHub, news in sequence
2. Raw search results flowing in → agent synthesizing into resume structure
3. `.docx` file produced: terminal shows the file created, then opened to reveal the formatted resume
4. Code: the 30-line TypeScript that drives the whole thing — brevity is the point

### Score
- Teachability: 4/5 — research-then-format is a fundamental agentic pattern in miniature
- Visual: 4/5 — the resume document appearing from a name is satisfying to watch
- Pull: 3/5 — fun demo, niche direct use case, but good as a pattern illustration
- Freshness: 3/5 — document generation via agents is established
- **Total: 14/20**
