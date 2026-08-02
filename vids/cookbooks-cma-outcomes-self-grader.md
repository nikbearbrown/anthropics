## cookbooks-cma-outcomes-self-grader

- **Source path:** claude-cookbooks/managed_agents/CMA_verify_with_outcome_grader.ipynb
- **Teachable claim:** Managed Agents Outcomes provisions a second agent — a grader — that independently verifies the writer's work against a rubric you define; the grader catches real errors (like a press-release citation where a 10-K was required) and the writer revises without any human intervention.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. Architecture: writer agent → grader agent (separate context, no access to writer's reasoning) → gap list → writer revises → loop
2. Rubric shown: the seven-item checklist the grader acts on — concrete and readable
3. Grader catches a real error: press-release URL cited where 10-K was required — grader output naming the gap
4. Writer revision: agent fetches the correct 10-K, updates the citation, grader passes on next cycle

### Score
- Teachability: 5/5 — the verify-and-revise loop is one of the most powerful patterns in agentic AI
- Visual: 4/5 — the grade → gap list → revision cycle is a clear narrative arc
- Pull: 5/5 — anyone building AI that produces high-stakes documents needs output verification
- Freshness: 5/5 — Outcomes is a new Managed Agents feature
- **Total: 19/20**
