#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-inspector-says-no-first.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #5 in show-tell-ideas.md.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/cwc-long-running-agents/ (README.md in full; claude-code-config/README.md;
.claude/agents/evaluator.md, .claude/CLAUDE.md, .claude/settings.json, and the five hooks
track-read.sh, verify-gate.sh, commit-on-stop.sh, kill-switch.sh, steer.sh).
Cast: a kraft WORKBENCH with the dark BUILDER station (the station of show-tell-five-ways-to-wire-an-agent),
kraft PART crates with a white stamp TAG (FAIL / PASS), the RESULTS BOARD (test-results.json), the
HOOK GATE of show-tell-inside-a-plugin-folder, a SCREENSHOT card (evidence), a closed kraft INSPECTOR
BOOTH behind a WALL (fresh context), a CLIPBOARD (PROGRESS.md) and a grey COMMIT stack (git log), the
conveyor LOOP, a STOP file and a STEER note, and a small dark /goal booth.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "The Inspector Says No First"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's a long-running agent as a workshop. At the bench, a builder makes one feature at a time. Left alone, it grades itself: after one unit test, it marks the part passing, even when the screen is visibly broken.",
      "B00_Bench", "A kraft workbench with the dark builder station slides in; the station's light comes on; a kraft part crate rises out of the bench; a crack draws across its face; the builder slaps its own PASS tag on it anyway.",
      [{"at": 0.1, "event": "bench + builder"}, {"at": 0.35, "event": "a part is built"}, {"at": 0.6, "event": "it marks itself passing"}, {"at": 0.85, "event": "the crack shows"}]),
 beat("B01", "Asking nicely doesn't reliably stop that. So the harness flips the default. Every feature is a row in test-results dot json, and every row starts false.",
      "B01_DefaultFail", "A prompt note slides to the station and the PASS tag stays put; on 'flips the default' the PASS tag flies off and a FAIL tag drops on; the results board slides in and three rows each draw an ink cross.",
      [{"at": 0.15, "event": "asking nicely: nothing changes"}, {"at": 0.45, "event": "PASS torn off, FAIL on"}, {"at": 0.75, "event": "board: every row false"}]),
 beat("B02", "A hook guards that file. The builder can't write to it until it has opened evidence: a screenshot, a console log. Each read unlocks one write. The next change needs fresh proof.",
      "B02_EvidenceGate", "A hook gate stands in front of the board; a write slip rides from the bench and stops at the closed gate; a screenshot card flies out and opens large; the gate light turns terracotta, the slip passes, row one turns to a check and the part's tag flips to PASS; the screenshot is used up and the light goes out; a second slip waits at the gate.",
      [{"at": 0.12, "event": "hook gate"}, {"at": 0.3, "event": "write blocked"}, {"at": 0.5, "event": "evidence opened"}, {"at": 0.7, "event": "one write passes"}, {"at": 0.9, "event": "next write waits"}]),
 beat("B03", "Then a second agent inspects the work, from its own booth, with a fresh context. It never saw the build. It gets the spec, the diff and the screenshots, and it has no Write or Edit tools.",
      "B03_Booth", "A wall rises beside the bench, leaving the builder's reasoning pages behind it; a closed kraft booth slides in on the far side; a spec page, a diff card and the screenshot slide through a hatch into the booth; a pencil beside the booth is crossed out.",
      [{"at": 0.15, "event": "wall + booth"}, {"at": 0.4, "event": "the reasoning stays behind"}, {"at": 0.65, "event": "spec, diff, screenshot through the hatch"}, {"at": 0.9, "event": "no write, no edit"}]),
 beat("B04", "Its instructions say plausibility is not correctness, and missing evidence means needs work. So it answers PASS or needs work, and its findings become the next build session's first prompt.",
      "B04_NeedsWork", "Inside the booth's window the screenshot's crack is circled; the booth's lamp comes on; a NEEDS_WORK slip slides out; a findings note rides back over the wall to the builder station; the part's tag flips back to FAIL.",
      [{"at": 0.2, "event": "the crack is found"}, {"at": 0.5, "event": "NEEDS_WORK"}, {"at": 0.8, "event": "findings ride back to the bench"}]),
 beat("B05", "Each session starts cold. So the builder keeps its own handoff note, PROGRESS dot md, and reads it first on every restart. It commits as it goes, and a hook commits what's left when the session stops.",
      "B05_Handoff", "The builder station's light goes out and a fresh station slides in; a clipboard on the bench fills with lines; it lifts toward the station on 'reads it first'; grey commit slabs drop onto a git-log stack; the light goes out and one last slab drops.",
      [{"at": 0.1, "event": "a cold new session"}, {"at": 0.35, "event": "the note fills"}, {"at": 0.55, "event": "read first"}, {"at": 0.8, "event": "commits stack up; the stop commit"}]),
 beat("B06", "Put it together and it's a loop: build, inspect, rebuild, until no row says false, a cycle changes nothing, or the budget runs out. Want true to mean the inspector agreed? Let only its PASS write the row.",
      "B06_Loop", "A conveyor loop joins the bench and the booth; parts ride out to the booth and back; the board above flips its rows from cross to check one at a time; a dashed line runs from the booth to the board.",
      [{"at": 0.15, "event": "the loop"}, {"at": 0.45, "event": "rows flip one by one"}, {"at": 0.85, "event": "the booth writes the row"}]),
 beat("B07", "And you stay in charge. Create a file called agent stop, and every tool call halts. Write a note in STEER dot md, and the agent sees it once, mid-run, with no restart.",
      "B07_Operator", "The loop is running; an AGENT_STOP file card drops beside it and every light goes grey, the part frozen on the belt; the file lifts away and the lights come back; a STEER note slides to the builder station and vanishes once read.",
      [{"at": 0.15, "event": "the loop runs"}, {"at": 0.3, "event": "AGENT_STOP: everything halts"}, {"at": 0.7, "event": "STEER note read once"}]),
 beat("B08", "Claude Code also has a built-in checker. Slash goal takes a condition, and after every turn a separate fast model checks it until it's met. Write your own evaluator dot md when you want your own inspector and the evidence gate.",
      "B08_GoalVsYours", "A small dark /goal booth with a one-line condition card; parts pass it turn by turn and its lamp blinks each time until a check lands; then the kraft evaluator.md booth with the hook gate in front slides in beside it.",
      [{"at": 0.15, "event": "/goal + its one-line condition"}, {"at": 0.45, "event": "checked every turn until met"}, {"at": 0.8, "event": "your evaluator.md booth + the gate"}]),
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
    "Namaste. This is Liam, in for Bear. A long-running agent will tell you it's done. The real question is how you make it prove it.",
    "BrutalistHesitantWriter",
    {"text": "How do I get my agent\nto say it's done?", "triggerWords": "say", "replacementWords": "prove",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get my agent to say it's done?'"}, {"at": 0.6, "event": "backspaces 'say' -> 'prove' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how to get an agent to say it's done) and corrects it to the real one (how to make it prove it).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. The builder: the agent session that writes the feature. The evaluator: a separate agent that checks the work. And default-FAIL: every check starts as failing, until evidence proves it passes.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "builder", "meaning": "the agent session that writes the feature"},
               {"term": "evaluator", "meaning": "a separate agent that checks the work"},
               {"term": "default-FAIL", "meaning": "every check starts failing until evidence proves it passes"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'builder' lands"}, {"at": 0.4, "event": "'evaluator' lands"}, {"at": 0.7, "event": "'default-FAIL' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Help me write a default-FAIL evaluator for one long task: [task]. Save it as .claude/agents/evaluator.md, "
             "with no Write or Edit tools. List the exact conditions it must see to pass, and the evidence that proves each one: "
             "a screenshot, a console log, or a test result. It reviews only the spec, the diff and that evidence, never the builder's "
             "reasoning. Its first line is PASS or NEEDS_WORK; missing evidence is NEEDS_WORK. Don't build the task.")
SPOKEN_PROMPT = (YT_PROMPT.replace("[task]", "name your task")
                 .replace(".claude/agents/evaluator.md", "dot claude, slash agents, slash evaluator dot md")
                 .replace("NEEDS_WORK", "needs work"))
CHECKS = ["Check: hand it a commit with no screenshot. Does it say NEEDS_WORK?",
          "Check: open evaluator.md. Does its tools line leave out Write and Edit?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + SPOKEN_PROMPT + " Then check two things yourself. Hand it a commit with no "
    "screenshot. Does it say needs work? And open evaluator dot md. Does its tools line leave out Write and Edit?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Write the Inspector First", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn workshop scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · LONG-RUNNING AGENTS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hindi (Namaste)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude Code users running long agent tasks who want 'done' to mean proven, not claimed",
    "source_doc": "anthropics/cwc-long-running-agents (README.md; claude-code-config/README.md; .claude/agents/evaluator.md, .claude/CLAUDE.md, .claude/settings.json, hooks track-read.sh, verify-gate.sh, commit-on-stop.sh, kill-switch.sh, steer.sh), read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["long-running agents", "Claude Code", "evaluator", "subagents", "hooks", "default-FAIL", "agent harness",
             "PROGRESS.md", "/goal", "generator evaluator loop", "Anthropic", "Claude", "Nik Bear Brown"]},
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
