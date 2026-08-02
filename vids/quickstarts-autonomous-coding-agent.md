## quickstarts-autonomous-coding-agent

- **Source path:** claude-quickstarts/autonomous-coding/
- **Teachable claim:** The two-agent coding pattern — an initializer that plans the feature list and a coding agent that executes one feature at a time across multiple sessions — persists progress via git so the agent can resume from any checkpoint without losing work.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Two-agent architecture: initializer (plans, commits feature list) → coding agent (implements one at a time)
2. Git as checkpoint: each completed feature is a commit — agent resume finds the last commit and continues
3. Feature list progression: the feature file ticked off one by one across sessions
4. Multi-session span: showing the same agent picking up a project it left two hours ago

### Score
- Teachability: 5/5 — git-as-checkpoint for long-running agents is the key architectural insight
- Visual: 4/5 — feature list ticking off + git log are both readable on screen
- Pull: 5/5 — building complete apps autonomously is the most compelling agent demo
- Freshness: 5/5 — multi-session autonomous coding with state persistence is new
- **Total: 19/20**
