# PROMPTS — show-tell-from-session-to-dashboard

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with the variable names spelled for Kokoro: "O-T-E-L", "O T L P", "g R P C"):

```
Clone github.com/anthropics/claude-code-monitoring-guide and start it with docker compose up -d. Then run claude -p "hello" with CLAUDE_CODE_ENABLE_TELEMETRY=1, OTEL_METRICS_EXPORTER=otlp, OTEL_EXPORTER_OTLP_PROTOCOL=grpc, OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 and OTEL_METRIC_EXPORT_INTERVAL=10000 set in that same command. Query Prometheus at localhost:9090 until a claude_code metric arrives, and tell me its name.
```

Checks shown under it (the viewer runs these themselves):
- Check: open localhost:9090, search claude_code. There?
- Check: start a new session. Session count up by one?
