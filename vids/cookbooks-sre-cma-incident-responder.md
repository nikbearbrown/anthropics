## cookbooks-sre-cma-incident-responder

- **Source path:** claude-cookbooks/managed_agents/sre_incident_responder.ipynb
- **Teachable claim:** The same SRE incident-response logic that runs in a notebook also runs as a Claude Managed Agent — the CMA version adds human-approval gating via `user.define_outcome`, automatic context compaction for long sessions, and a history that persists so you can re-examine the agent's reasoning at 4am without rerunning it.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. CMA vs. Agent SDK: the same log-analysis task; CMA handles the loop, compaction, and session persistence; show that the "notebook version" requires manual loop management while CMA provides it
2. `user.define_outcome` as the SRE safety gate: rubric requires the agent to check a runbook before recommending a rollback; the grader blocks "rollback immediately" verdicts without runbook citation
3. Session persistence: run the investigation; exit; re-open the session; show the full transcript waiting — the 3am handoff without context loss
4. Outcome grader log: `span.outcome_evaluation_end` shows NEEDS_REVISION with specific feedback; agent loops back and finds the runbook citation; grader passes on iteration 2

### Score
- Teachability: 5/5 — "outcome rubric as a safety gate on high-stakes ops decisions" is the key design principle
- Visual: 4/5 — grader feedback → agent revision → pass is concrete and shows the outcome loop working
- Pull: 5/5 — SRE is a natural CMA use case and every ops team wants this
- Freshness: 4/5 — the Agent SDK version is already carded; this CMA version shows the managed-hosting advantage
- **Total: 18/20**
