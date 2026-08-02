## cookbooks-sentry-scheduled-deployment

- **Source path:** claude-cookbooks/managed_agents/sentry/README.md
- **Teachable claim:** A single `POST /v1/deployments` call creates a server-side cron that fires a Managed Agent session every weekday at 9am — no host process, no scheduler, no cron daemon — and a vault `environment_variable` credential keeps the Sentry token in an opaque placeholder the model never sees.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The architecture: `cron (0 9 * * 1-5) → deployment → session → sentry-cli → /mnt/session/outputs/TRIAGE_REPORT.md`; one diagram, no host process in the picture
2. `deploy.py`: `deployments.create` with `schedule.type:"cron"`, `expression:"0 9 * * 1-5"`, `initial_events:[user.message]`; API response includes `upcoming_runs_at` — five next run times to confirm the schedule
3. Vault credential: `type:"environment_variable"`, `secret_name:"SENTRY_AUTH_TOKEN"`, `networking.allowed_hosts:["*.sentry.io"]`; the sandbox holds a placeholder; only matching egress gets the real value
4. Manual test + run log: `python run_now.py` fires immediately, streams the session; `python runs.py` shows deployment run history and any errors

### Score
- Teachability: 5/5 — "no host process, one API call" is the entire point of Managed Agents deployments
- Visual: 4/5 — cron diagram + vault placeholder substitution flow is concrete and checkable
- Pull: 5/5 — every recurring agent use case leads directly here
- Freshness: 5/5 — scheduled deployments are brand-new CMA surface area
- **Total: 19/20**
