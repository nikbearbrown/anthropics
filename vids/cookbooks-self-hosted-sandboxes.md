## cookbooks-self-hosted-sandboxes

- **Source path:** claude-cookbooks/managed_agents/self_hosted_sandboxes/README.md
- **Teachable claim:** Self-hosted Managed Agents environments run tool execution on your own compute — Docker, Modal, Cloudflare Containers, Vercel Sandbox, or Daytona — with a single environment key as the worker's only credential, and the contract is identical across all six providers.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The why: regulated environments (HIPAA, FedRAMP), custom runtimes, cost control — four reasons to run tools on your infra instead of Anthropic's cloud
2. The contract: three steps any provider must implement — receive `session.status_run_started` webhook, drain the environment work queue, run `ant beta:worker run` (or SDK equivalent) per work item; show it as a sequence diagram
3. Docker path (the entry-level): `Dockerfile` → container; `ant beta:worker run` handles tool calls; environment key is the single credential; no org API key in the runner
4. Modal path: `modal deploy` → `modal.Sandbox` per session; the Python `sandbox_runner.py` runs in the Modal container with a per-session Volume for persistence; cost comparison with cloud sandbox

### Score
- Teachability: 5/5 — "one contract, six providers" framing makes a complex topic approachable
- Visual: 4/5 — architecture diagram + Docker/Modal command sequence is concrete
- Pull: 4/5 — enterprise customers with data residency requirements need exactly this
- Freshness: 5/5 — self-hosted CMA environments are very new with almost no coverage
- **Total: 18/20**
