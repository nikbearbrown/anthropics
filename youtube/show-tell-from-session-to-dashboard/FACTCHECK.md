# FACTCHECK — show-tell-from-session-to-dashboard

**What this is.** Every claim the film speaks or shows, checked against its named sources: the guide `anthropics/claude-code-monitoring-guide/` (`README.md`, `claude_code_roi_full.md`, `docker-compose.yml`, `otel-collector-config.yaml`, `prometheus.yml`, `report-generation-prompt.md`, `grafana/dashboards/working-dashboard.json`, `grafana/provisioning/dashboards/dashboards.yaml`), each byte-compared (`cmp`) with the raw upstream file at `raw.githubusercontent.com/anthropics/claude-code-monitoring-guide/main/` (HTTP 200, identical, `sources/live_*`), and the LIVE Claude Code monitoring docs, fetched raw with curl on 2026-09-27 from `https://code.claude.com/docs/en/monitoring-usage.md` (HTTP 200, 177,479 bytes, `sources/live_monitoring-usage-2026-09-27.md`; cited below as "docs"). No WebFetch summary was used. **Result:** PASS. Where the guide is older than the docs, the docs win (rows 25 and 56, CORRECTED). The film states no price, no ROI dollar figure and none of the guide's sample numbers (card #28 caution: pricing may be stale). Its only numbers are configuration values the sources state (1, 1000 ms, 60,000 ms default, 4317, 8889, 15 s, 1 s, 3000, 10000 in the prompt, 9090) and the docs' count of eight metrics. Drawings that are not data have EXEMPT rows.

Status: PASS · 2026-09-27 · checked by Claude (Opus 5.5) for Bear

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Greeting "Konnichiwa" | EXEMPT (greeting) | Japanese greeting; whisper (English models) hears "Kaneshiwa", the same as the accepted BIDEAs of earlier Konnichiwa films. | — |
| 2 | BIDEA | One chat only sees its own session; the real question is tracking Claude Code on a dashboard | PASS (framing) | Docs: telemetry is exported "across your organization" to a backend you configure; the guide's pipeline ends in dashboards. | — |
| 3 | BIDEA | Writer: "How do I track Claude Code by asking Claude?" corrected to "…on a dashboard?" | EXEMPT (framing) | The naive question corrected. | — |
| 4 | BDEFS | metric: a number counted over time, like tokens used | PASS | Docs: "Claude Code exports metrics as time series data"; `claude_code.token.usage` "Number of tokens used". | — |
| 5 | BDEFS | OpenTelemetry: the open standard Claude Code sends them with | PASS | Docs: "exporting telemetry data through OpenTelemetry (OTel)", linking the OpenTelemetry specification. | — |
| 6 | BDEFS | collector: a relay that receives them and passes them on | PASS | `otel-collector-config.yaml`: `receivers: otlp` → `exporters: prometheus, debug`. | — |
| 7 | BDEFS | Prometheus: keeps the numbers over time and answers queries | PASS | Guide: "Prometheus gives you dashboards, historical data"; "Key Prometheus Queries"; compose `--storage.tsdb.retention.time=200h`. | — |
| 8 | B00 | Anthropic's Claude Code monitoring guide builds one pipeline | PASS | Repo `github.com/anthropics/claude-code-monitoring-guide`; docs "ROI measurement resources" links it: "ready-to-use Docker Compose configurations, Prometheus and OpenTelemetry setups". | — |
| 9 | B00 | A session's numbers run down a pipe into a collector, then Prometheus, then a Grafana dashboard | PASS | `docker-compose.yml` services otel-collector, prometheus, grafana; `prometheus.yml` scrapes `otel-collector:8889`; Grafana dashboard queries Prometheus. | — |
| 10 | B00 | Terminal, pipe, funnel, cabinet, board ('session', 'dashboard') | EXEMPT (illustration) | Illustrates row 9. | — |
| 11 | B01 | It starts switched off; sending telemetry to your own backend is opt-in | PASS | Docs, Security and privacy: "OpenTelemetry export to your backend is opt-in and requires explicit configuration." | — |
| 12 | B01 | The switch is one environment variable: CLAUDE_CODE_ENABLE_TELEMETRY=1 | PASS | Docs table: `CLAUDE_CODE_ENABLE_TELEMETRY` "Enables telemetry collection (required)", value `1`; guide Quick Verification. | — |
| 13 | B01 | Switch plate, knob, lamp lights, a drop leaves | EXEMPT (illustration) | Illustrates rows 11–12. | — |
| 14 | B02 | The guide tests first: metrics exporter set to console | PASS | Guide "Quick Verification": `export OTEL_METRICS_EXPORTER=console`. | — |
| 15 | B02 | The export interval's default is one minute | PASS | Docs: `OTEL_METRIC_EXPORT_INTERVAL` "Export interval in milliseconds (default: 60000)". | — |
| 16 | B02 | …cut to one second | PASS | Guide: `export OTEL_METRIC_EXPORT_INTERVAL=1000`. | — |
| 17 | B02 | Run one prompt with claude -p; the metrics print in your terminal | PASS | Guide: `claude -p "hello world"` then "You should see output like this" (console metric output incl. `claude_code.cost.usage`). | — |
| 18 | B02 | Printout rising from the terminal ('console', 'claude -p') | EXEMPT (illustration) | Line count is drawn, not data. | — |
| 19 | B03 | The guide ships a Docker Compose file | PASS | `docker-compose.yml` in the repo; README "Docker Compose and metrics collection setup". | — |
| 20 | B03 | One command, docker compose up, starts three containers: an OpenTelemetry collector, Prometheus and Grafana | PASS | Guide: `docker-compose up -d`; compose services `otel-collector` (`otel/opentelemetry-collector-contrib`), `prometheus`, `grafana`. The film says "docker compose up" (the Compose v2 spelling of the same command). | — |
| 21 | B03 | Grafana draws the dashboards | PASS | Compose mounts `./grafana/dashboards`; guide screenshots "Grafana dashboard". | — |
| 22 | B04 | Metrics exporter set to OTLP | PASS | Guide + docs: `OTEL_METRICS_EXPORTER=otlp`. | — |
| 23 | B04 | …over gRPC; endpoint localhost port 4317 | PASS | Guide + docs Quick start: `OTEL_EXPORTER_OTLP_PROTOCOL=grpc`, `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317`; compose maps "4317:4317 # OTLP gRPC receiver". | — |
| 24 | B04 | Pipe, collar ('otlp over grpc', 'localhost:4317'), check | EXEMPT (illustration) | Illustrates rows 22–23. | — |
| 25 | B05 | The live docs list eight metrics: sessions, lines of code, pull requests, commits, cost, tokens, code edit decisions, active time | CORRECTED | Docs Metrics table: `session.count`, `lines_of_code.count`, `pull_request.count`, `commit.count`, `cost.usage`, `token.usage`, `code_edit_tool.decision`, `active_time.total` (eight). The guide lists seven (no active time); the live docs win and the film says "the live docs". | Count and list taken from the docs, not the guide. |
| 26 | B05 | Drops ride the pipe; a row of eight drops ('8 metrics') | PASS (derived) | Eight drops = row 25. | — |
| 27 | B06 | Tokens are split by type: input, output, cache read, cache creation | PASS | Docs Token counter: `type` ("input", "output", "cacheRead", "cacheCreation"). | — |
| 28 | B06 | Tokens and cost also name the model | PASS | Docs: Cost and Token counters carry `model`. | — |
| 29 | B06 | By default every metric carries a session ID | PASS | Docs Standard attributes: `session.id`, controlled by `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true); "All metrics and events share these standard attributes". | — |
| 30 | B06 | So you can slice the numbers later | PASS | Docs: "All metrics can be segmented by the standard attributes." | — |
| 31 | B06 | Drop splits in four; kraft tags ('model'), grey tags ('session.id') | EXEMPT (illustration) | Illustrates rows 27–29. | — |
| 32 | B07 | Events are a second stream: one record each time something happens, like a prompt or a tool result | PASS | Docs: "events via the logs/events protocol"; `claude_code.user_prompt` "Logged when a user submits a prompt"; Tool result event. | — |
| 33 | B07 | …sent by a separate logs exporter | PASS | Docs: events are exported "when `OTEL_LOGS_EXPORTER` is configured". | — |
| 34 | B07 | The guide's collector has one pipeline, for metrics only | PASS | `otel-collector-config.yaml` `service.pipelines` has only `metrics:`. | — |
| 35 | B07 | …so events would need their own | PASS (derived) | Follows from row 34: no logs pipeline, so the guide's stack does not carry events. | — |
| 36 | B07 | Thin pipe with slips, capped ('events', 'metrics only') | EXEMPT (illustration) | Illustrates rows 32–35. | — |
| 37 | B08 | Prompt text isn't collected by default, only its length | PASS | Docs: "User prompt content is not collected by default. Only prompt length is recorded." | — |
| 38 | B08 | Raw file contents and code snippets aren't in metrics or events | PASS | Docs: "Raw file contents and code snippets are not included in metrics or events." (Trace spans are a separate, opt-in path; the film does not cover traces.) | — |
| 39 | B08 | Your email, attached when you sign in, goes only to the endpoint you set, never to Anthropic | PASS | Docs: "When authenticated via OAuth, `user.email` is included in telemetry attributes, sent only to the OTel endpoint you configure, never to Anthropic." | — |
| 40 | B08 | Page stopped by a lid; a length strip passes; email tag rides to the collector | EXEMPT (illustration) | Illustrates rows 37–39. | — |
| 41 | B09 | A receiver takes metrics in on port 4317 | PASS | Collector config: `receivers: otlp: protocols: grpc: endpoint: 0.0.0.0:4317`. | — |
| 42 | B09 | A batch step groups them, with a one-second timeout | PASS | Collector config: `processors: batch: timeout: 1s` (in the metrics pipeline). | — |
| 43 | B09 | A Prometheus exporter sets them out on port 8889 | PASS | Collector config: `exporters: prometheus: endpoint: "0.0.0.0:8889"`; compose "8889:8889 # Prometheus metrics". | — |
| 44 | B10 | Prometheus isn't sent anything; it scrapes | PASS | `prometheus.yml` `scrape_configs` job `otel-collector`, target `otel-collector:8889` (pull). | — |
| 45 | B10 | …every fifteen seconds | PASS | `prometheus.yml`: `scrape_interval: 15s`. | — |
| 46 | B10 | …and files each number as a time series | PASS | Guide: "claude_code_cost_usage_USD_total time series data". | — |
| 47 | B10 | Arm, drops, a rising series ('scrape', 'every 15 s') | EXEMPT (illustration) | Series heights are drawn, not data. | — |
| 48 | B11 | You query it in PromQL | PASS | Guide "Key Prometheus Queries" (```promql```). | — |
| 49 | B11 | claude_code.token.usage becomes claude_code_token_usage_tokens_total | PASS | Docs name `claude_code.token.usage`; guide queries and dashboard use `claude_code_token_usage_tokens_total`. | — |
| 50 | B11 | Add it up by type and one total splits into input, output, cache read, cache creation | PASS | Guide: `sum(claude_code_token_usage_tokens_total) by (type)` with type input / output / cacheCreation / cacheRead. The guide's sample values are not used. | — |
| 51 | B11 | Drawer, one column splitting into four ('by type') | EXEMPT (illustration) | Column heights are drawn, not data. | — |
| 52 | B12 | Grafana on port 3000 | PASS | Compose: grafana `ports: "3000:3000"`. | — |
| 53 | B12 | The dashboard comes from the guide's own file: total cost, active users, tokens, lines of code, cost by model | PASS | `grafana/dashboards/working-dashboard.json` panels: Total Cost, Active Users, Total Tokens, Lines of Code, Cost by Model (also Token Usage by Type, Cost by User, Lines of Code by Type, not named). | — |
| 54 | B12 | Cost figures are approximations; for billing, the docs point you to your API provider | PASS | Docs: "Cost metrics are approximations. For official billing data, refer to your API provider." Troubleshooting.md says the same. | — |
| 55 | B12 | Board, four tiles, a pie; a dot on the cost tile ('approximate') | EXEMPT (illustration) | Tile bars and pie split are drawn, not data. | — |
| 56 | B13 | For a whole team, an administrator sets the same variables once, in managed settings | CORRECTED | Docs "Administrator configuration": OTel settings for all users through the managed settings file, in an `env` block. The guide's `managed-settings.json` example (`telemetry` / `exporters` keys) is not the live shape; the film follows the docs and shows no JSON. | Docs, not the guide's JSON. |
| 57 | B13 | A repository's own settings can't turn telemetry on or change where it goes | PASS | Docs: the exporter variables in a repository's `.claude/settings.json` are ignored, "so a repository can't use them to turn telemetry on, choose where it goes, or capture content." | — |
| 58 | B13 | Settings page feeding four terminals; a repo folder's line stops at a cross | EXEMPT (illustration) | Illustrates rows 56–57. | — |
| 59 | B14 | The guide's script pulls totals from Prometheus with curl | PASS | Guide `fetch-claude-metrics.sh`: `curl -s "http://localhost:9090/api/v1/query?query=sum(claude_code_cost_usage_USD_total)"` etc. | — |
| 60 | B14 | …hands them to claude -p, which also reads your team's issues through the Linear MCP server | PASS | Guide: `claude -p "Using the Linear MCP, analyze our team's velocity …"`; `claude mcp add linear …`. | — |
| 61 | B14 | …and writes a productivity report | PASS | Guide: "Generate a comprehensive productivity report"; `sample-report-output.md`. | — |
| 62 | B14 | Slip from cabinet to terminal, MCP block, report page ('claude -p', 'Linear MCP', 'report') | EXEMPT (illustration) | Illustrates rows 59–61. | — |
| 63 | BHTF | Clone github.com/anthropics/claude-code-monitoring-guide and run docker compose up -d | PASS | Repo URL from the docs' ROI section; compose file at repo root. (The guide's own clone line names an older repo, `katchu11/claude-code-guide`; the prompt uses the live Anthropic repo.) | — |
| 64 | BHTF | Env vars CLAUDE_CODE_ENABLE_TELEMETRY=1, OTEL_METRICS_EXPORTER=otlp, OTEL_EXPORTER_OTLP_PROTOCOL=grpc, OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317, OTEL_METRIC_EXPORT_INTERVAL=10000 | PASS | Docs Quick start (10000 is the docs' debugging value, "10 seconds"). | — |
| 65 | BHTF | Set them in the same command as claude -p | PASS | Docs: Claude Code doesn't pass `OTEL_*` variables to subprocesses it spawns, "so set those variables directly in the command". | — |
| 66 | BHTF | Query Prometheus at localhost:9090 | PASS | Compose: prometheus `ports: "9090:9090"`; guide queries `localhost:9090/api/v1/query`. | — |
| 67 | BHTF | Check: search claude_code in Prometheus | PASS | Metric names begin `claude_code` (docs; guide queries). | — |
| 68 | BHTF | Check: start a new session; does the session count go up by one? | PASS | Docs: verify with `claude_code.session.count`, "which Claude Code emits when a session starts"; Session counter "Incremented at the start of each session". | — |
| 69 | BOUT | "From Session to Dashboard. At Nik Bear Brown." | EXEMPT (outro) | Title restate. | — |
