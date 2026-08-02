## quickstarts-computer-use-best-practices

- **Source path:** claude-quickstarts/computer-use-best-practices/
- **Teachable claim:** The production-grade computer-use agent is radically different from the demo — explicit tool definitions, image size pruning, prompt caching, server-side compaction, batched tool calls, a sandboxed shell, and trajectory recording all exist to prevent the same screenshot from burning $50 in tokens.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. The naive computer-use loop: screenshot → full-res image → tokens → action → repeat — cost explosion shown
2. Image sizing and pruning: resize to 1568px width, drop older screenshots — token count drops dramatically
3. Batched tool calls: clicking a menu + waiting for it to open in one batch vs. two separate calls
4. Trajectory recording: every action logged as a structured event — for replay, debugging, and cost auditing

### Score
- Teachability: 5/5 — the gap between demo and production computer-use is the key lesson
- Visual: 4/5 — cost comparison and architecture diagram are both strong
- Pull: 4/5 — everyone building computer-use agents hits these issues
- Freshness: 5/5 — the best-practices guide is new and the failure modes are not yet widely understood
- **Total: 18/20**
