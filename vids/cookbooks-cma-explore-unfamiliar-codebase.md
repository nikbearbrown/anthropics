## cookbooks-cma-explore-unfamiliar-codebase

- **Source path:** claude-cookbooks/managed_agents/CMA_explore_unfamiliar_codebase.ipynb
- **Teachable claim:** A well-grounded agent checks the code against the documentation before trusting either — the cookbook plants a trap where ARCHITECTURE.md is stale, and an agent that reads only the docs gives the wrong answer while one that explores the actual file tree gives the right one.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The trap setup: ARCHITECTURE.md describes a monolith, but `ls services/` shows a microservices layout
2. Agent 1 (doc-trusting): reads ARCHITECTURE.md → gives confident wrong answer about the codebase
3. Agent 2 (grounded): ls → grep → read actual files → notices the discrepancy → correct answer
4. `sessions.resources.add`: mid-session file injection — pushing a new file into a running session

### Score
- Teachability: 5/5 — "grounding over documentation" is a safety-critical agent principle
- Visual: 4/5 — the stale docs vs. actual code discrepancy is easy to show on screen
- Pull: 4/5 — any codebase-exploring agent hits this problem
- Freshness: 4/5 — mid-session resource injection is a new Managed Agents capability
- **Total: 17/20**
