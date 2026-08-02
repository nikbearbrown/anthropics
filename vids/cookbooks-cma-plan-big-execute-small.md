## cookbooks-cma-plan-big-execute-small

- **Source path:** claude-cookbooks/managed_agents/CMA_plan_big_execute_small.ipynb
- **Teachable claim:** Splitting planning and execution across model tiers — frontier model coordinates, cheap models do the reading — is 2.5x cheaper and 3x faster than running a frontier model end-to-end, with 98% of input tokens billed at the worker rate.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. Architecture: coordinator (no tools, only planning) → parallel search workers (all the token-heavy reading) → synthesis
2. Cost metering: per-thread `usage` stats shown — breakdown of coordinator tokens vs. worker tokens
3. Rigor-matched comparison: same research question run on coordinator-only vs. coordinator+workers — real bills and wall-clock
4. The 84–98% stat: input tokens billed at worker rate visualized as a cost breakdown bar

### Score
- Teachability: 5/5 — the cost structure math is the lesson and it's verifiable
- Visual: 4/5 — cost comparison bars and architecture diagram are both strong
- Pull: 5/5 — anyone running large-scale agent workflows needs to know this
- Freshness: 5/5 — coordinator+worker cost pattern is underexplored territory
- **Total: 19/20**
