#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-from-session-to-dashboard.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #28 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B14 drawn -> BHTF composer -> BOUT.

Sources: anthropics/claude-code-monitoring-guide/ — README.md, claude_code_roi_full.md, docker-compose.yml,
otel-collector-config.yaml, prometheus.yml, report-generation-prompt.md, troubleshooting.md and
grafana/dashboards/working-dashboard.json, all read in full 2026-09-27 and byte-compared with the raw upstream files
(raw.githubusercontent.com/anthropics/claude-code-monitoring-guide/main/): identical (sources/live_*). The LIVE Claude
Code monitoring docs (code.claude.com/docs/en/monitoring-usage.md, fetched raw with curl, sources/live_monitoring-usage-
2026-09-27.md) win wherever the guide is older: eight metrics (the guide lists seven), the managed-settings format (the
guide's JSON is not the live shape, so the film shows none), the privacy rules, the 60-second default export interval.
NO prices, NO ROI dollar figures, NO sample numbers from the guide (card #28 caution: pricing may be stale).
Cast: THE TERMINAL (kraft block, extra-dark screen, terracotta cursor dot, a side switch with a lamp); METRIC DROPS
(grey beads); THE PIPE (kraft, ink edges); THE COLLECTOR (kraft funnel on a dark plinth); PROMETHEUS (a tall kraft
cabinet with three drawers); THE DASHBOARD (a white board with grey bars); pages (printout, prompt, settings, report);
the Linear MCP block (dark).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "From Session to Dashboard"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's Claude Code monitoring guide builds one pipeline. On the left, a Claude Code session. Its numbers run down a pipe into a collector, then into Prometheus, and out onto a Grafana dashboard your team can read.",
      "B00_Pipeline", "A kraft terminal block lands at the left ('session'); a pipe draws to the right into a kraft funnel (the collector), on into a tall kraft cabinet (Prometheus), and out to a white board whose grey bars grow ('dashboard').",
      [{"at": 0.1, "event": "the monitoring guide's pipeline"}, {"at": 0.35, "event": "a Claude Code session"}, {"at": 0.85, "event": "collector, Prometheus, dashboard"}]),
 beat("B01", "It starts switched off. Sending telemetry to your own backend is opt-in, and the switch is one environment variable: Claude Code enable telemetry, set to one.",
      "B01_Switch", "The pipeline clears; the terminal grows at the left with a switch plate beside it, knob at 'off' ('opt-in'); the knob slides over, the lamp lights terracotta, and the variable lands ('CLAUDE_CODE_ENABLE_TELEMETRY=1').",
      [{"at": 0.1, "event": "switched off"}, {"at": 0.45, "event": "opt-in"}, {"at": 0.85, "event": "CLAUDE_CODE_ENABLE_TELEMETRY=1"}]),
 beat("B02", "Before any plumbing, the guide tests the tap. Set the metrics exporter to console, cut the export interval from its default of one minute to one second, and run one prompt with the command claude, dash P. The metrics print right in your terminal.",
      "B02_Console", "A 'claude -p' pill slides into the terminal; a white printout rises from the terminal's top slot ('console'), one grey line per tick ('1 s').",
      [{"at": 0.1, "event": "test the tap first"}, {"at": 0.45, "event": "exporter console, interval one second"}, {"at": 0.85, "event": "metrics print in the terminal"}]),
 beat("B03", "For the real pipeline, the guide ships a Docker Compose file. One command, docker compose up, starts three containers: an Open Telemetry collector, Prometheus, and Grafana, which draws the dashboards.",
      "B03_Compose", "The printout clears and the terminal shrinks to the left; a long dark plinth draws; three pieces drop onto it one by one: the funnel ('collector'), the cabinet ('Prometheus'), the board ('Grafana').",
      [{"at": 0.1, "event": "a Docker Compose file"}, {"at": 0.45, "event": "one command, three containers"}, {"at": 0.85, "event": "collector, Prometheus, Grafana"}]),
 beat("B04", "Then point Claude Code at the collector. Set the metrics exporter to O T L P, the Open Telemetry protocol, over g R P C, and set the endpoint to localhost, port forty-three seventeen. The pipe connects.",
      "B04_Endpoint", "A pipe draws from the terminal toward the funnel ('otlp over grpc'); a socket lands on the funnel ('localhost:4317'); the pipe meets it and a check lands.",
      [{"at": 0.1, "event": "point it at the collector"}, {"at": 0.45, "event": "OTLP over gRPC"}, {"at": 0.85, "event": "localhost:4317; connected"}]),
 beat("B05", "Now each session drips numbers down the pipe. The live docs list eight metrics: sessions, lines of code, pull requests, commits, cost, tokens, code edit decisions, and active time.",
      "B05_Metrics", "Grey metric drops leave the terminal one after another and ride the pipe into the funnel; eight drops line up above the pipe as the voice names them ('8 metrics').",
      [{"at": 0.1, "event": "drops ride the pipe"}, {"at": 0.4, "event": "eight metrics"}, {"at": 0.85, "event": "…edit decisions, active time"}]),
 beat("B06", "Each drop carries tags. Tokens are split by type: input, output, cache read and cache creation. Tokens and cost also name the model. And by default every metric carries a session I D, so you can slice the numbers later.",
      "B06_Tags", "One drop grows at the centre and splits into four smaller drops ('type'); a kraft tag on a string hangs from it ('model'); a second tag hangs from every drop ('session.id').",
      [{"at": 0.1, "event": "tags"}, {"at": 0.35, "event": "four token types"}, {"at": 0.6, "event": "the model"}, {"at": 0.85, "event": "session ID on every metric"}]),
 beat("B07", "Events are a second stream: one record each time something happens, like a prompt or a tool result, sent by a separate logs exporter. The guide's collector has one pipeline, for metrics only, so events would need their own.",
      "B07_Events", "Back to the pipe; a second, thinner pipe draws above it ('events'); white slips ride it; at the funnel a grey cap closes it ('metrics only').",
      [{"at": 0.1, "event": "a second stream: events"}, {"at": 0.45, "event": "a separate logs exporter"}, {"at": 0.85, "event": "the guide's collector: metrics only"}]),
 beat("B08", "What stays out: prompt text isn't collected by default, only its length. Raw file contents and code snippets aren't in metrics or events. And your email, attached when you sign in, goes only to the endpoint you set, never to Anthropic.",
      "B08_Privacy", "A white prompt page slides toward the pipe; a grey gate drops and stops it ('prompt text'); only a small ruler slip goes in ('length'); a code page is stopped too; a kraft email tag rides the pipe to the collector ('your endpoint').",
      [{"at": 0.1, "event": "prompt text stays out"}, {"at": 0.35, "event": "only its length"}, {"at": 0.55, "event": "no file contents or code"}, {"at": 0.85, "event": "email only to your endpoint"}]),
 beat("B09", "Inside the collector, a receiver takes the metrics in on port forty-three seventeen. A batch step groups them, with a one-second timeout, and a Prometheus exporter sets them out on port eighty-eight eighty-nine.",
      "B09_Collector", "The funnel grows at the centre; drops enter at the left ('4317'), gather in a grey batch tray ('batch'), and leave by a spout at the right onto a small shelf ('8889').",
      [{"at": 0.1, "event": "receiver on 4317"}, {"at": 0.5, "event": "batched, one-second timeout"}, {"at": 0.85, "event": "Prometheus exporter on 8889"}]),
 beat("B10", "Prometheus isn't sent anything. It scrapes: every fifteen seconds, it pulls from the collector's port eighty-eight eighty-nine and files each number as a time series.",
      "B10_Scrape", "The funnel shrinks to the left with drops waiting on its shelf; the cabinet stands at the right; a grey arm reaches out and pulls the drops in, three times ('scrape', 'every 15 s'); each pull fills a drawer.",
      [{"at": 0.1, "event": "Prometheus pulls"}, {"at": 0.45, "event": "every fifteen seconds"}, {"at": 0.85, "event": "stored as time series"}]),
 beat("B11", "You ask it questions in Prom Q L. The names change shape on the way in: claude code dot token dot usage becomes claude code token usage tokens total. Add it up by type, and one total splits into input, output, cache read and cache creation.",
      "B11_Query", "The cabinet at the left; its top drawer slides out; the metric name lands above ('claude_code_token_usage_tokens_total'); one grey column rises, then splits into four columns ('by type').",
      [{"at": 0.1, "event": "PromQL"}, {"at": 0.45, "event": "the Prometheus name"}, {"at": 0.85, "event": "split by type"}]),
 beat("B12", "Grafana, on port three thousand, draws the dashboard from the guide's own file: total cost, active users, tokens, lines of code, and cost by model. The cost figures are approximations; for billing, the docs point you to your API provider.",
      "B12_Dashboard", "The white board fills the stage ('Grafana'); four stat tiles fill with grey bars one by one, then a chart grows; a grey approximately sign lands on the cost tile ('approximate').",
      [{"at": 0.1, "event": "Grafana on port 3000"}, {"at": 0.45, "event": "the guide's panels"}, {"at": 0.85, "event": "cost is approximate"}]),
 beat("B13", "For a whole team, an administrator sets the same variables once, in managed settings. A repository's own settings can't turn telemetry on or change where it goes.",
      "B13_Team", "A white settings page at the top ('managed settings'); four small terminals in a row; grey lines draw from the page to each, and their lamps light; a kraft repo folder's own line stops short at an ink cross ('repo settings').",
      [{"at": 0.15, "event": "managed settings, once for everyone"}, {"at": 0.85, "event": "a repository can't turn it on or redirect it"}]),
 beat("B14", "Last, the report. The guide's script pulls totals from Prometheus with curl and hands them to claude, dash P, which also reads your team's issues through the Linear M C P server, and writes a productivity report.",
      "B14_Report", "The cabinet at the left; a slip rides from it to the terminal ('claude -p'); a dark MCP block plugs in beside the terminal ('Linear MCP'); a white report page rises and its lines and bars draw ('report').",
      [{"at": 0.1, "event": "the report"}, {"at": 0.4, "event": "totals from Prometheus into claude -p"}, {"at": 0.65, "event": "Linear MCP"}, {"at": 0.9, "event": "a productivity report"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Konnichiwa. This is Liam, in for Bear. To see how your team uses Claude Code, you might just ask Claude. But one chat only sees its own session. So the real question is how to track Claude Code on a dashboard.",
    "BrutalistHesitantWriter",
    {"text": "How do I track Claude Code\nby asking Claude?", "triggerWords": "by asking Claude", "replacementWords": "on a dashboard",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I track Claude Code by asking Claude?'"}, {"at": 0.6, "event": "backspaces 'by asking Claude' -> 'on a dashboard' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (track Claude Code by asking Claude) and corrects it to the real one (track Claude Code on a dashboard).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A metric: a number counted over time, like tokens used. Open Telemetry: the open standard Claude Code uses to send those numbers out. A collector: a relay that receives them and passes them on. And Prometheus: a database that keeps the numbers over time and answers queries.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "metric", "meaning": "a number counted over time, like tokens used"},
               {"term": "OpenTelemetry", "meaning": "the open standard Claude Code sends them with"},
               {"term": "collector", "meaning": "a relay that receives them and passes them on"},
               {"term": "Prometheus", "meaning": "keeps the numbers over time and answers queries"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'metric' lands"}, {"at": 0.3, "event": "'OpenTelemetry' lands"}, {"at": 0.55, "event": "'collector' lands"}, {"at": 0.8, "event": "'Prometheus' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Clone github.com/anthropics/claude-code-monitoring-guide and start it with docker compose up -d. Then run "
             "claude -p \"hello\" with CLAUDE_CODE_ENABLE_TELEMETRY=1, OTEL_METRICS_EXPORTER=otlp, "
             "OTEL_EXPORTER_OTLP_PROTOCOL=grpc, OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 and "
             "OTEL_METRIC_EXPORT_INTERVAL=10000 set in that same command. Query Prometheus at localhost:9090 until a "
             "claude_code metric arrives, and tell me its name.")
SPOKEN_PROMPT = ("Clone github dot com slash anthropics slash claude code monitoring guide, and start it with docker compose up, "
                 "dash d. Then run claude, dash P, hello, with Claude Code enable telemetry set to one, O-T-E-L metrics exporter set "
                 "to O T L P, O-T-E-L exporter O T L P protocol set to g R P C, O-T-E-L exporter O T L P endpoint set to localhost, "
                 "forty-three seventeen, and O-T-E-L metric export interval set to ten thousand, all in that same command. Query "
                 "Prometheus at localhost, nine oh nine oh, until a claude code metric arrives, and tell me its name.")
CHECKS = ["Check: open localhost:9090, search claude_code. There?",
          "Check: start a new session. Session count up by one?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code. " + SPOKEN_PROMPT +
    " Then check it yourself. Open localhost nine oh nine oh and search for claude code. Is it there? And start a new session. Does the session count go up by one?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the terminal, the pipe, the collector funnel, the "
                 "Prometheus cabinet, the dashboard board) on a cream stage per beat, minimal labels, with the voice carrying "
                 "the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, "
                 "empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B07", "B08", "B10", "B12"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.56-0.69 throughout; the rest dip below 0.55 and keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · TELEMETRY PIPELINE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Japanese (Konnichiwa)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Team leads and developers who want Claude Code's usage numbers on a dashboard: the pipeline from Anthropic's claude-code-monitoring-guide (OpenTelemetry metrics -> collector -> Prometheus -> Grafana, plus the claude -p report), checked against the live Claude Code monitoring docs; no prices",
    "source_doc": "anthropics/claude-code-monitoring-guide/ (README.md, claude_code_roi_full.md, docker-compose.yml, otel-collector-config.yaml, prometheus.yml, report-generation-prompt.md, grafana/dashboards/working-dashboard.json) byte-compared with raw upstream; live docs code.claude.com/docs/en/monitoring-usage.md fetched raw 2026-09-27 (sources/)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude Code", "telemetry", "OpenTelemetry", "OTel collector", "Prometheus", "Grafana", "PromQL", "monitoring",
             "observability", "metrics", "Docker Compose", "claude -p", "Linear MCP", "Anthropic", "Nik Bear Brown"]},
    "beats": B}

# keep measured audio fields across re-runs (audio-first: never lose the clock)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in B:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in B)), "s")
