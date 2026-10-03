#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-one-plugin-per-service.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #7 in show-tell-ideas.md.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-tag-plugins/ (README.md in full; .claude-plugin/marketplace.json; the asana,
bigquery, claude-tag-data-viz and claude-tag-troubleshoot folders, incl. the troubleshoot README, the
config-guide references and the debug-plugins skill).
Cast: a kraft WALL (the team's workspace) with a grid of SOCKETS (dark-kraft outlines, a light above each);
kraft PLUGS (small boxes with a cord) kept in a kraft CRATE; the @Claude chat BUBBLE (white, DIM outline,
terracotta spark); ink CORDS from the bubble to the plugs; white request PACKETS; the plug opened as an
open box with a manifest tag, a SKILL page, a reference stack and a script tile; a KEY that comes from the
runtime, not the plug; the wall split into org / workspace / channel sections; grey READ plugs and a taped
WRITE plug; a TABLE card that becomes a CHART card; the TESTER, a small kraft handheld with a probe.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "One Plugin per Service"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's your team's workspace, drawn as a wall of sockets, one for each service it could use. And here's Claude Tag: the Claude that answers when you tag it in a chat thread, backed by remote Claude Code sessions.",
      "B00_Wall", "A kraft wall rises; eight sockets draw onto its face, their lights blinking once; a white chat bubble with a terracotta spark drops in to the right ('@Claude') and three typing dots pulse in it.",
      [{"at": 0.1, "event": "the wall"}, {"at": 0.3, "event": "sockets, one per service"}, {"at": 0.55, "event": "the @Claude bubble"}, {"at": 0.85, "event": "typing dots: remote sessions"}]),
 beat("B01", "The repo lists eighteen plugins. Sixteen are services, from Asana and Big Query to Jira and Datadog. The other two are helpers. You add the repo as a marketplace, then install the services you use.",
      "B01_Crate", "A kraft crate slides in below the wall; eighteen small plugs drop into it row by row (sixteen kraft, two grey); the hero '18' lands beside it; the two grey helper plugs lift and settle.",
      [{"at": 0.1, "event": "the crate"}, {"at": 0.3, "event": "eighteen plugs drop in"}, {"at": 0.55, "event": "two grey helpers lift"}, {"at": 0.85, "event": "one at a time"}]),
 beat("B02", "Each service is its own plugin, so a workspace can connect exactly the services it uses. Say this team works in Asana, and keeps its data in Big Query. Two plugs go in. Every other socket stays empty.",
      "B02_PlugIn", "One plug rises from the crate and rides an arc into a socket ('Asana'); a second follows ('BigQuery'); both sockets' lights turn terracotta; the six empty sockets fade to ghost.",
      [{"at": 0.15, "event": "one plugin per service"}, {"at": 0.45, "event": "Asana plugs in"}, {"at": 0.65, "event": "BigQuery plugs in"}, {"at": 0.9, "event": "the rest stay empty"}]),
 beat("B03", "Now tag Claude in a thread. It can reach those two: Asana tasks, and S Q L in Big Query. Each skill activates when it's relevant. Ask about Jira, and there's no Jira plugin to reach for.",
      "B03_Reach", "Ink cords draw from the bubble to the two plugs; request packets ride out along each and back; a dashed grey line reaches from the bubble toward an empty socket ('Jira') and stops short, then fades.",
      [{"at": 0.15, "event": "cords to the two plugs"}, {"at": 0.4, "event": "packets ride each"}, {"at": 0.8, "event": "Jira: no plug, the line stops short"}]),
 beat("B04", "Open one plug. There's a manifest, plugin dot json. A skill: how to connect, and the core operations. A catalog of endpoints, read only when needed. And usually, small scripts. What you won't find is a key. The runtime injects the credentials into each request.",
      "B04_Inside", "Close-up: the Asana plug opens as a kraft box; a manifest tag rises out ('plugin.json'), then a skill page ('SKILL.md'), a stack of reference pages and a small script tile; an empty key outline appears in the box; a key slides in from the wall side ('runtime') and rides out on a request packet.",
      [{"at": 0.1, "event": "the plug opens"}, {"at": 0.25, "event": "plugin.json"}, {"at": 0.4, "event": "SKILL.md, references, scripts"}, {"at": 0.65, "event": "no key inside"}, {"at": 0.85, "event": "the runtime brings the key"}]),
 beat("B05", "Claude's settings come in layers: the organization, a workspace, then a channel. Plugins add up along that chain. A channel can plug in more, but can't unplug what a layer above provides. So what you plug in at the top reaches every channel.",
      "B05_Layers", "The wall is three sections rising left to right ('org', 'workspace', 'channel'); a plug goes into the org section and copies slide along into the same socket on the other two; the channel section adds a plug of its own; a cursor tugs the inherited plug in the channel section, it comes out a little and snaps back.",
      [{"at": 0.12, "event": "three layers"}, {"at": 0.35, "event": "the org plug copies down the chain"}, {"at": 0.55, "event": "the channel adds one"}, {"at": 0.75, "event": "can't unplug the inherited one"}]),
 beat("B06", "For GitHub, the repo's best practice goes further: a read-only profile bound everywhere, and a write profile bound only to the channels allowed to push or merge. That limits the blast radius. Plug in what you use, and give each plug the least it needs.",
      "B06_ReadWrite", "Three channel sections; a grey read plug drops into each ('read'); one dark-taped write plug goes into a single section ('write'); a terracotta ring expands from it and stops at its own section's edges.",
      [{"at": 0.15, "event": "read everywhere"}, {"at": 0.4, "event": "write in one channel"}, {"at": 0.65, "event": "the blast radius stays small"}, {"at": 0.9, "event": "least access"}]),
 beat("B07", "Now the two helpers. Hand the data visualization plugin a table, say rows from Big Query, and it composes a polished chart: a P N G, an S V G, or an interactive H T M L page.",
      "B07_Chart", "A white table card slides out from the BigQuery plug ('table'); a grey data-viz plug lights; a copy of the table moves and becomes a chart card: grey bars grow with gaps, an ink line draws, a terracotta dot lands on its end ('chart'); three small file cards fan out below.",
      [{"at": 0.15, "event": "a table"}, {"at": 0.45, "event": "the chart builds"}, {"at": 0.8, "event": "PNG, SVG, HTML"}]),
 beat("B08", "The other helper is troubleshoot. Config changes only reach new sessions, so start a fresh Slack thread. Then run debug plugins. From inside the session, it checks which plugins actually loaded, which failed, and why.",
      "B08_Tester", "The wall with its two plugs; a new thread bubble replaces the old one; a small kraft tester slides in ('debug-plugins'); its probe line touches the Asana plug, a check lands; then the BigQuery plug, a second check.",
      [{"at": 0.15, "event": "a fresh thread"}, {"at": 0.45, "event": "the tester arrives"}, {"at": 0.7, "event": "check: Asana loaded"}, {"at": 0.9, "event": "check: BigQuery loaded"}]),
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
    "Olá. This is Liam, in for Bear. Anthropic's claude tag plugins repo doesn't hook Claude up to everything. Each service is its own plugin, so the real question is what your team uses.",
    "BrutalistHesitantWriter",
    {"text": "How do I connect Claude\nto everything?", "triggerWords": "everything", "replacementWords": "what we use",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I connect Claude to everything?'"}, {"at": 0.6, "event": "backspaces 'everything' -> 'what we use' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (connect Claude to everything) and corrects it to the real one (what we use).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A plugin: one service's skill and scripts, packed to install. An agent scope: Claude's settings for one workspace, or one channel. And an identity profile: a reusable bundle of rules, credentials and plugins.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "plugin", "meaning": "one service's skill and scripts, packed to install"},
               {"term": "agent scope", "meaning": "Claude's settings for one workspace or one channel"},
               {"term": "identity profile", "meaning": "a reusable bundle of rules, credentials and plugins"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'plugin' lands"}, {"at": 0.4, "event": "'agent scope' lands"}, {"at": 0.7, "event": "'identity profile' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here are the tools my team uses each week: [list them]. From the plugin list in anthropics/claude-tag-plugins, "
             "pick the ones our Claude Tag needs. For each, say whether it should only read or also write, and in which "
             "channels. Then list what to leave unplugged, and why.")
SPOKEN_PROMPT = (YT_PROMPT.replace("anthropics/claude-tag-plugins", "Anthropic's claude tag plugins repo")
                 .replace("[list them]", "list them"))
CHECKS = ["Check: every plugin. Who used that tool this week?",
          "Check: every write. Which channel and task need it?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. For every plugin, who used that tool this week? "
    "And for every write, which channel and task need it?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Plug In Only What You Use", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn wall-of-sockets scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = set()   # beats measured to fill >= 55% without the waiver (set after the first Gate V pass)
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · CLAUDE TAG PLUGINS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Portuguese (Olá)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Teams and admins setting up Claude Tag (@Claude in a chat workspace) who want to connect only the services they use",
    "source_doc": "anthropics/claude-tag-plugins (README.md, .claude-plugin/marketplace.json; asana, bigquery, claude-tag-data-viz, claude-tag-troubleshoot folders incl. config-guide references and debug-plugins), read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude Tag", "@Claude", "Claude in Slack", "claude-tag-plugins", "Claude plugins", "Asana", "BigQuery",
             "agent scopes", "identity profiles", "least privilege", "data viz", "debug-plugins", "Anthropic", "Claude", "Nik Bear Brown"]},
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
