## cookbooks-usage-cost-admin-api

- **Source path:** claude-cookbooks/observability/usage_cost_api.ipynb
- **Teachable claim:** The Anthropic Admin API returns token consumption and cost broken down by model, workspace, and API key in configurable time buckets — enabling cache efficiency tracking, chargeback reports, and spend anomaly detection without leaving the API.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. The four token types: `uncached_input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` — show what each means and why the cache split matters for cost analysis
2. Usage query: `GET /usage_report/messages` with `bucket_width="1d"`, 7-day window; plot the daily token consumption bar chart; highlight the cache read ratio
3. Chargeback pattern: filter by `api_key_id` to attribute costs to teams; show the per-team cost breakdown table built from the raw usage data
4. Anomaly detection: compare today's hourly usage against the 7-day average; flag hours where `uncached_input_tokens` spikes more than 2x — the "something changed" alert

### Score
- Teachability: 4/5 — the four token types + time bucket structure is specific and checkable
- Visual: 4/5 — bar chart + per-team cost table is concrete and useful output
- Pull: 4/5 — finance and platform teams need this for any production Claude deployment
- Freshness: 4/5 — the Admin API is underdocumented; this is the first cookbook showing the usage patterns
- **Total: 16/20**
