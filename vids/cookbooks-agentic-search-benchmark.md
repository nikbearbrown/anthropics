## cookbooks-agentic-search-benchmark

- **Source path:** claude-cookbooks/evals/agentic_search/reproduce_agentic_search_benchmarks.ipynb
- **Teachable claim:** Anthropic's published DeepSearchQA benchmark scores are reproducible on the public Messages API — the gap between published and third-party results comes from five harness configuration choices (server-side compaction, task budgets, tool setup, grader model, prompt format), not from private infrastructure.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The gap problem: side-by-side of Anthropic's published score vs. a naive harness score — the difference is harness config, not the model
2. The five configuration diffs: compaction enabled, `web_search`/`web_fetch`/`code_execution` server tools, task budget param, grader model pinned to Opus 4.6, prompt format — show each as a one-line code change
3. Run three demo DeepSearchQA questions: 30+ tool calls scroll; the question requires cross-referencing multiple sources
4. Score comparison: table of naive vs. configured harness results; the grader model labels each answer CORRECT/INCORRECT with explanation

### Score
- Teachability: 5/5 — "the benchmark is reproducible; here's why yours isn't" is an immediately actionable insight
- Visual: 4/5 — before/after config diffs + live scoring table is concrete and checkable
- Pull: 5/5 — every serious Claude user wants to verify benchmark claims independently
- Freshness: 5/5 — first public cookbook showing how to reproduce Anthropic's own published benchmark
- **Total: 19/20**
