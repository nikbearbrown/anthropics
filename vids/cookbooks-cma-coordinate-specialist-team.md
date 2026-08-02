## cookbooks-cma-coordinate-specialist-team

- **Source path:** claude-cookbooks/managed_agents/CMA_coordinate_specialist_team.ipynb
- **Teachable claim:** Scoping tools per agent role — the pricing modeler sees only the pricing rules file, never the web — isn't just tidiness, it's a correctness guarantee: isolated agents can't hallucinate data from the wrong source.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Three specialist agents defined: researcher (web search), librarian (local case-study files), pricing modeler (one rules file) — each shown with its tool restriction
2. Coordinator orchestrating: send to researcher → wait → send to librarian → wait → send to pricer → synthesize proposal
3. Tool isolation diagram: why the pricer must never see the web — prevents hallucinated competitor numbers
4. Final proposal output: two-page sales proposal assembled from three specialist outputs

### Score
- Teachability: 5/5 — tool scoping as correctness guarantee is the architectural insight
- Visual: 4/5 — the three-agent fan-out and synthesis is a clean diagram
- Pull: 4/5 — multi-agent system design is what every serious agent builder needs next
- Freshness: 5/5 — Managed Agents multi-agent is new
- **Total: 18/20**
