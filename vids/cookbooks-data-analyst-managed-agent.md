## cookbooks-data-analyst-managed-agent

- **Source path:** claude-cookbooks/managed_agents/data_analyst_agent.ipynb
- **Teachable claim:** A Claude Managed Agents environment with `pandas` and `plotly` pre-installed turns a CSV upload into a narrative HTML report with interactive charts — the agent writes Python in its sandbox, the files land in `/mnt/session/outputs/`, and the Files API retrieves them.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. Environment creation: `packages.pip: ["pandas","plotly"]` → sessions start with them pre-installed; no `pip install` in the agent loop
2. Session kickoff: upload a CSV via Files API → attach as a resource → send `user.define_outcome` with a rubric; agent provisions sandbox and starts analyzing
3. Agent working: tool calls scroll — Python writes the analysis, generates a Plotly HTML report, saves to `/mnt/session/outputs/`
4. Retrieval: `GET /v1/files?scope_id=<session_id>` → download the HTML report; open it in the browser to show the interactive chart output

### Score
- Teachability: 5/5 — the environment pre-install + Files API output retrieval is the key aha for CMA data workflows
- Visual: 5/5 — CSV in, interactive HTML chart out is intrinsically compelling before/after cinema
- Pull: 4/5 — anyone doing ad-hoc data analysis immediately wants this
- Freshness: 4/5 — CMA is new; this is the canonical data analysis pattern on the new stack
- **Total: 18/20**
