#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-inside-a-plugin-folder.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #4 in show-tell-ideas.md, the direct
sequel to show-tell-claude-plugin-portal (same kraft box, same dark MCP block, same pages).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Sources: anthropics/claude-plugins-official/ (README; plugins/plugin-dev/skills/plugin-structure;
the real plugins commit-commands, code-simplifier, security-guidance, hookify, example-plugin,
external_plugins/github; .claude-plugin/marketplace.json) and anthropics/knowledge-work-plugins/README.md.
Cast: the kraft PLUGIN BOX (opens; its shipping LABEL is plugin.json), COMMAND pages and a Claude
Code WINDOW, a small kraft HELPER crate (sub-agent), SKILL pages, an event BELT with a HOOK gate
and a dark COMMAND slab, the dark MCP block + SERVER stack + KEY (token), two smaller boxes
(commit-commands, github), a catalog SHELF (the marketplace) and a MAGNIFIER (trust it first).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "What's Inside a Plugin Folder"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's the plugin box from last time. On disk, a plugin is just a folder. Open it, and each kind of part has its own place inside.",
      "B00_Folder", "The sealed kraft plugin box from the portal film drops in; a folder tab clips to its lid on 'just a folder'; the lid lifts off and the tops of the parts (a page, a dark block, a small crate) rise into view inside.",
      [{"at": 0.1, "event": "box drops in"}, {"at": 0.4, "event": "folder tab"}, {"at": 0.7, "event": "lid lifts, parts peek out"}]),
 beat("B01", "First, the shipping label: a file called plugin dot json, in a folder named dot claude-plugin. It holds the plugin's name, a description, and sometimes a version. Only the name is required.",
      "B01_Label", "A white shipping label rises out of the open box and slaps onto its front face; an enlarged copy slides out to the right and its three lines draw one by one; the first line (name) thickens to ink on 'Only the name is required'.",
      [{"at": 0.15, "event": "label slaps on"}, {"at": 0.5, "event": "name, description, version lines"}, {"at": 0.85, "event": "name line is the required one"}]),
 beat("B02", "Slash commands are the parts you trigger yourself. Each one is a markdown file in the commands folder. Type slash commit, and Claude follows the steps written in that file.",
      "B02_Commands", "The box steps left; a command page rises out of it; a Claude Code window with a prompt bar types '/commit'; the page slides into the window and three step lines tick off.",
      [{"at": 0.15, "event": "page rises"}, {"at": 0.55, "event": "/commit typed"}, {"at": 0.8, "event": "steps tick off"}]),
 beat("B03", "Sub-agents are helpers with one job, and each one is a markdown file in the agents folder. Claude hands one a multi-step task. It works through it on its own, then reports back.",
      "B03_SubAgent", "A small kraft helper crate rises out of the box, rides to a stack of task pages on the right, the pages clear one by one, and the crate rides back carrying one report card.",
      [{"at": 0.15, "event": "helper crate rises"}, {"at": 0.5, "event": "rides to the task"}, {"at": 0.75, "event": "works through it"}, {"at": 0.9, "event": "returns with a report"}]),
 beat("B04", "Skills are folders of know-how, each with a SKILL.md file. You don't have to type anything. Claude reads each skill's description, and opens one when the task matches.",
      "B04_Skills", "Three skill pages rise out of the box and fan out; a task card slides in from the right; the matching page lifts toward it and its dot lights terracotta.",
      [{"at": 0.2, "event": "three pages fan out"}, {"at": 0.6, "event": "task card arrives"}, {"at": 0.85, "event": "the matching page lifts"}]),
 beat("B05", "Hooks fire on events. The hooks file says: when Claude edits a file, or finishes a turn, run this command. The security-guidance plugin uses hooks to check each edit for risky code. That's a real program, running on your machine.",
      "B05_Hooks", "An event belt with a hook gate; edit slabs ride along it; each time one passes the gate, the gate's light flashes and a dark command slab beside it lights up.",
      [{"at": 0.15, "event": "belt and hook gate"}, {"at": 0.4, "event": "an edit passes, the gate fires"}, {"at": 0.85, "event": "the command slab runs"}]),
 beat("B06", "MCP servers are listed in dot mcp dot json. They plug Claude into outside tools and data, and they start when the plugin is turned on. GitHub's plugin holds one entry: GitHub's own server, reached with your access token.",
      "B06_MCP", "A dark MCP block rises out of the box; a cable draws from it to a server stack on the right whose lights come on; a small ink key rides along the cable to the server.",
      [{"at": 0.15, "event": "MCP block rises"}, {"at": 0.45, "event": "cable to the server, lights on"}, {"at": 0.85, "event": "the key rides the cable"}]),
 beat("B07", "And a plugin carries only the parts it needs. Commit-commands is a label and three slash commands. GitHub's is a label and one MCP server. Nothing else.",
      "B07_OnlyWhatItNeeds", "Two smaller open boxes side by side, each with a label on its face: three command pages drop into the left one; one dark MCP block drops into the right one.",
      [{"at": 0.2, "event": "two boxes"}, {"at": 0.45, "event": "three pages drop in"}, {"at": 0.75, "event": "one MCP block drops in"}]),
 beat("B08", "Plugins live in a marketplace, a catalog you install from. Anthropic's official one lists two hundred fifty-five. But the catalog's own README says: make sure you trust a plugin before you install it. Anthropic doesn't control what's inside.",
      "B08_Marketplace", "A shelf unit of small plugin boxes and a big '255'; one box slides off the shelf toward the viewer and stops; a magnifier glides over it before anything else happens.",
      [{"at": 0.15, "event": "shelves fill"}, {"at": 0.3, "event": "255"}, {"at": 0.5, "event": "one box slides out"}, {"at": 0.75, "event": "magnifier: trust it first"}]),
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
    "Konnichiwa. This is Liam, in for Bear. Installing a plugin takes one command. So the question isn't how to install one. It's how to look inside it first.",
    "BrutalistHesitantWriter",
    {"text": "How do I install\na Claude plugin?", "triggerWords": "install", "replacementWords": "look inside",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I install a Claude plugin?'"}, {"at": 0.6, "event": "backspaces 'install' -> 'look inside' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how to install a plugin) and corrects it to the real one (how to look inside it).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. The manifest: a file called plugin dot json that names the plugin. A hook: a command that runs by itself when something happens in your session. And an MCP server: a program that plugs Claude into outside tools and data.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "manifest", "meaning": "plugin.json, the file that names the plugin"},
               {"term": "hook", "meaning": "a command that runs by itself when something happens in your session"},
               {"term": "MCP server", "meaning": "a program that plugs Claude into outside tools and data"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'manifest' lands"}, {"at": 0.45, "event": "'hook' lands"}, {"at": 0.78, "event": "'MCP server' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Before I install the Claude Code plugin [name], read its folder. List every part it ships: plugin.json, "
             "commands, sub-agents, skills, hooks, and MCP servers. For each hook, give the event and the exact command it runs. "
             "For each MCP server, say where it connects and what keys it needs. Then list what it could read, change, "
             "or send off my machine. Don't install or run anything.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + YT_PROMPT.replace("plugin.json", "plugin dot json") + " Then check two things yourself. Open the hooks file and read "
    "every command it runs. And open dot mcp dot json. Does every server match what the plugin says it does?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Look Inside Before You Install", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": ["Check: open hooks/hooks.json and read every command it runs.",
                "Check: open .mcp.json. Does every server match what the plugin says it does?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn plugin-box scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · PLUGINS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Japanese (Konnichiwa)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude Code users who install plugins and want to know what each part of one can do before they trust it",
    "source_doc": "anthropics/claude-plugins-official (README, plugins/plugin-dev/skills/plugin-structure/SKILL.md, real plugins commit-commands, code-simplifier, security-guidance, hookify, example-plugin, external_plugins/github, .claude-plugin/marketplace.json; HEAD 47ebd6a5, 2026-08-27) and anthropics/knowledge-work-plugins/README.md, read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude plugins", "Claude Code", "plugin.json", "slash commands", "sub-agents", "Agent Skills", "hooks", "MCP",
             "Model Context Protocol", "plugin marketplace", "plugin security", "Anthropic", "Claude", "Nik Bear Brown"]},
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
