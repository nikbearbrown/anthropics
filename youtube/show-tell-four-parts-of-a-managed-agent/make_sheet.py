#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-four-parts-of-a-managed-agent.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #14 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/launch-your-agent/cma-primitives.md ("The 4 core primitives": Agent / Environment /
Session / Events), read in full, plus .claude/skills/launch-your-agent/references/cma-api.md. Claude
Managed Agents is in BETA and that file says "live public docs win", so every claim was re-checked
against the raw live pages (platform.claude.com/docs/en/managed-agents/*.md, fetched 2026-09-27, saved
in sources/live-docs-2026-09-27/). One point CORRECTED from the local file: sandbox state lasts 30 days
from when the sandbox was CREATED and activity does not extend it (the local file said "after last
activity", reset by a ping).
Cast: the AGENT as a white BLUEPRINT card stack (dark header strip, ghost lines, parts tiles; a second
card drops on for version 2); the ENVIRONMENT as a kraft CRATE (open, packages drop in) with a
FENCE and one gap to an allowed HOST; each SESSION as a closed kraft crate on a pad with a LAMP post
(ghost = idle, terracotta = running); EVENTS as white cards riding a pale BELT into and out of the
session; a CHECKPOINT photo card; an OUTPUTS tray.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Four Parts of a Managed Agent"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's docs name four parts. The agent. The environment. The session. And events. You make the first two once. Every run is a session, and events are how you talk to it.",
      "B00_FourParts", "Four objects drop onto four ghost pads, one per name: a white blueprint card (agent), a kraft crate (environment), a closed crate with a lamp post (session), a short belt with a card (events); a 'beta' pill lands; the blueprint and crate get an ink ring ('once') while a card rides the belt into the session.",
      [{"at": 0.1, "event": "agent, environment, session, events drop in"}, {"at": 0.6, "event": "the first two, once"}, {"at": 0.85, "event": "a card rides into the session"}]),
 beat("B01", "The agent is the blueprint: the model, a system prompt, tools, MCP servers and skills. Create it once, and reuse it by its ID. Change it, and you get a new version. Version one becomes version two, and the old one stays in the history.",
      "B01_Blueprint", "The blueprint card grows to centre ('agent'); five part tiles drop onto it as each is named (dark model block, white prompt page, kraft tools, dark MCP block, white skill page); an ID tag hangs off it; an ink pen line redraws a tile, a second card drops on top of the stack ('v1' -> 'v2'), and the first card slides back behind it ('history').",
      [{"at": 0.1, "event": "the blueprint"}, {"at": 0.2, "event": "five parts drop in"}, {"at": 0.55, "event": "reuse by ID"}, {"at": 0.75, "event": "v1 -> v2"}, {"at": 0.9, "event": "the old card stays behind"}]),
 beat("B02", "The environment says where sessions run: Anthropic's cloud sandbox, or a self-hosted one on your own machines. It lists packages to install ahead of time, and which hosts the network may reach.",
      "B02_Environment", "The blueprint shrinks to the upper left; a kraft crate slides in to centre ('environment'); small package boxes drop into it; a fence of posts draws around the right side with one gap, and a dark host block lands beyond the gap with a dashed ink line through it ('allowed host').",
      [{"at": 0.1, "event": "the crate"}, {"at": 0.55, "event": "packages drop in"}, {"at": 0.8, "event": "the fence, one allowed host"}]),
 beat("B03", "A session is one run. It names an agent and an environment, and it gets its own fresh container. Two sessions, two sandboxes, no shared files. Created without a first event, it starts idle.",
      "B03_Session", "Blueprint and crate sit small at the left; a closed session crate slides out to the right on a pad, ink threads draw to it from the blueprint and the crate ('session'); a second crate slides out on a second pad; a ghost lamp on each post ('idle').",
      [{"at": 0.1, "event": "one session"}, {"at": 0.35, "event": "names an agent and an environment"}, {"at": 0.6, "event": "two sessions, two sandboxes"}, {"at": 0.9, "event": "idle"}]),
 beat("B04", "Events are how you talk to it. You send a user dot message. The session switches to running, and the agent works on its own. Tool calls, results and replies stream back as agent events. Mid-run, another message steers it, and an interrupt stops it.",
      "B04_Events", "One session crate large at centre with its lamp; a pale belt runs in from the left; a white card rides in ('user.message'); the lamp turns terracotta ('running'); three white cards ride out on a second belt to the right ('agent events'); a second card rides in (steer), then a kraft card (interrupt) and the lamp goes ghost.",
      [{"at": 0.1, "event": "the belt"}, {"at": 0.25, "event": "user.message rides in"}, {"at": 0.4, "event": "lamp: running"}, {"at": 0.6, "event": "agent events ride out"}, {"at": 0.85, "event": "steer, interrupt"}]),
 beat("B05", "When a turn ends, the session sends status idle, and waits. Its sandbox is checkpointed: the files, the installed packages, everything the agent made. Send another user message, and it picks up from there.",
      "B05_Checkpoint", "The lamp is ghost ('idle'); a camera flash, and a white photo card of the crate pops up beside it ('checkpoint'); a new card rides in on the belt, the photo slides back into the crate, and the lamp turns terracotta again.",
      [{"at": 0.1, "event": "idle"}, {"at": 0.3, "event": "the checkpoint photo"}, {"at": 0.75, "event": "a new message resumes it"}]),
 beat("B06", "One limit, from the live docs. The conversation history stays until you delete it. The sandbox state lasts thirty days from when the sandbox was created, and activity doesn't extend it. So have the agent save what matters as outputs.",
      "B06_ThirtyDays", "The checkpoint photo sits on a ghost timeline bar; a history stack of cards stays solid beside the crate ('history'); a hero '30 days' counter climbs as the bar fills in grey segments ('per Anthropic's docs'); the photo fades at the bar's end; a file card drops into a kraft tray ('outputs').",
      [{"at": 0.2, "event": "history stays"}, {"at": 0.45, "event": "30 days, per the docs"}, {"at": 0.7, "event": "activity doesn't extend it"}, {"at": 0.9, "event": "save to outputs"}]),
 beat("B07", "Put together: one agent and one environment, made once, and as many sessions as you need, each one driven by events. Anthropic runs the loop. You design the four parts.",
      "B07_Together", "The blueprint and the crate sit at the left; three session crates slide out on pads at the right, one after another, each with its lamp; a card rides a short belt into each and its lamp lights ('one agent', 'many sessions').",
      [{"at": 0.2, "event": "one agent, one environment"}, {"at": 0.5, "event": "many sessions"}, {"at": 0.8, "event": "events drive each"}]),
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
    "Namaste. This is Liam, in for Bear. It's easy to picture a managed agent as one thing you switch on. Claude Managed Agents, now in beta, splits it into four parts. So the real question is how those four parts fit together.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nswitch on a managed agent?", "triggerWords": "switch on a managed agent", "replacementWords": "fit its four parts together",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I switch on a managed agent?'"}, {"at": 0.6, "event": "backspaces 'switch on a managed agent' -> 'fit its four parts together' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I switch on a managed agent) and corrects it to the real one (how do I fit its four parts together).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A managed agent: Anthropic runs the agent loop for you. A sandbox: an isolated Linux container, where the agent's tools run. And an event: one message into, or out of, a session.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "managed agent", "meaning": "Anthropic runs the agent loop for you (beta)"},
               {"term": "sandbox", "meaning": "an isolated Linux container where tools run"},
               {"term": "event", "meaning": "one message into, or out of, a session"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'managed agent' lands"}, {"at": 0.4, "event": "'sandbox' lands"}, {"at": 0.7, "event": "'event' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Plan a Claude Managed Agent that runs this repo's tests and reports what fails. Don't create anything yet. "
             "Write FOUR_PARTS.md: the agent (model, prompt, tools), the environment (packages, allowed hosts), "
             "one session, and the events I'd send and watch for. Check each part against the live docs.")
SPOKEN_PROMPT = YT_PROMPT.replace("Write FOUR_PARTS.md:", "Write a four parts file:")
CHECKS = ["Check: every field it names is in the live docs?",
          "Check: the network allows only the hosts it needs?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code, in a repo with tests: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Is every field it names in the live docs? And does the network allow only the hosts the job needs?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn blueprint-crate-and-belt scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = set()   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): every body beat dips under 0.55 fill somewhere (0.13-0.45 at 25%), so all keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · MANAGED AGENTS (BETA)", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hindi (Namaste)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers who know the Messages API or Claude Code and want a plain map of Claude Managed Agents before they build one",
    "source_doc": "anthropics/launch-your-agent/cma-primitives.md (read in full 2026-09-27) + .claude/skills/launch-your-agent/references/cma-api.md; checked against the raw live docs at platform.claude.com/docs/en/managed-agents/ (overview, agent-setup, environments, sessions, session-operations, events-and-streaming, reference; fetched 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Managed Agents", "managed agents", "agents", "Claude API", "beta", "agent", "environment",
             "session", "events", "sandbox", "checkpoint", "Anthropic", "Nik Bear Brown"]},
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
