## cookbooks-cma-orchestrate-issue-to-pr

- **Source path:** claude-cookbooks/managed_agents/CMA_orchestrate_issue_to_pr.ipynb
- **Teachable claim:** An agent can run an end-to-end bug fix loop — read issue, find bug, fix it, open PR, survive CI failures, address review comments, and merge — because the session filesystem and conversation history persist across turns, each user message picking up where the last one left off.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. State chain: issue body → file paths → fix diff → PR number → CI output → review comment → merge — each passed as context
2. The CI failure: agent reads the CI traceback and adapts (adds missing docstring) — mid-chain recovery shown
3. Tool diversity: `gh-mock` CLI, file edits, JSON reads, grep — showing the agent uses all of them coherently
4. Final state: merged PR, test suite green — confirmed via `cat .gh-state/`

### Score
- Teachability: 5/5 — end-to-end software workflow is the most concrete agent value prop
- Visual: 5/5 — state transitions through the chain make a natural story arc
- Pull: 5/5 — every developer imagines this; seeing it work is compelling
- Freshness: 4/5 — agentic coding is known, but this multi-step recovery demo is fresh
- **Total: 19/20**
