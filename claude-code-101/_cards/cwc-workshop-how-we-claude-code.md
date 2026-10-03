## cwc-workshop-how-we-claude-code

- **Source path:** cwc-workshops/how-we-claude-code/
- **Teachable claim:** Anthropic's own product development workflow has three phases — interview-driven brainstorm (prompts only), four divergent design directions (static HTML mockups), and verifiable component architecture (runtime DOM contracts) — and each phase is reproducible from the published prompts.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. Phase 1 prompt: the interview-driven brainstorm that produces a product spec — the actual prompt shown
2. Four design directions side-by-side: the static HTML mockups for the bill-splitting app
3. Phase 3 architecture: component fixtures + invariants + machine-readable DOM contract — the verification matrix
4. Verification dashboard: running `bun run verify` → passing/failing component contracts appear

### Score
- Teachability: 5/5 — Anthropic's own AI-assisted product workflow is the source of truth for "how to Claude Code"
- Visual: 4/5 — design mockups + verification dashboard are both visual
- Pull: 5/5 — "how Anthropic uses Claude to build products" is the most credible possible endorsement
- Freshness: 5/5 — verifiable component architecture is a novel pattern Anthropic is pioneering
- **Total: 19/20**
