## cwc-workshop-rightmodel-eval-sweep

- **Source path:** cwc-workshops/rightmodel/
- **Teachable claim:** Picking the right Claude model requires a sweep — grid your task across models × thinking × effort, instrument per-cell pass rate / cost / latency, and you get three comparison plots plus a one-sentence quality-per-dollar recommendation.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–6 min)

### Visual beats
1. The eval audit checklist: task design, harness design, metrics hygiene, grader design — the four failure modes shown
2. The grid: model × thinking level × effort — each cell running the same task
3. Three plots: pass rate vs. cost, pass rate vs. latency, cost vs. latency — the tradeoff space visualized
4. One-sentence recommendation output: "Use claude-sonnet-4-6 with extended thinking effort=medium — best quality/$ for this task"

### Score
- Teachability: 5/5 — most developers pick models by intuition; a systematic sweep is a discipline upgrade
- Visual: 5/5 — the three tradeoff plots are inherently visual and the grid concept is clear
- Pull: 5/5 — model selection affects every Claude deployment; this is universally relevant
- Freshness: 5/5 — model × thinking × effort sweep is a new methodology
- **Total: 20/20**
