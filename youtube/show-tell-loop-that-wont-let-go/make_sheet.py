#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-loop-that-wont-let-go.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #13 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source (ONE copy, the maintained directory one): anthropics/claude-plugins-official/plugins/ralph-loop/
(README.md, commands/ralph-loop.md, commands/cancel-ralph.md, commands/help.md, hooks/hooks.json,
hooks/stop-hook.sh, scripts/setup-ralph-loop.sh, .claude-plugin/plugin.json), all read in full 2026-09-27.
The older twin, claude-code/plugins/ralph-wiggum/, was diffed but NOT used as a source (see SOURCES.md).
Cast: Claude as a kraft WORKER with a terracotta spark; a kraft BENCH; a PINBOARD with the prompt card;
a SHELF (your repo) where file pages and commit cubes pile up; a DOORWAY on the right with a kraft
BOOTH and a parking-gate ARM (the Stop hook); a STATE FILE card by the door with a big lap numeral;
a promise TOKEN; a TEST BOARD in the last beat.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "The Loop That Won't Let Claude Leave"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Ralph Loop is a plugin in Anthropic's official plugin directory for Claude Code. You run one command, slash ralph loop, with your task in quotes. That task becomes the prompt, pinned above Claude's bench.",
      "B00_Command", "A kraft bench drops onto the stage and Claude, a kraft worker with a terracotta spark, slides in beside it ('Claude'); a command pill types in ('/ralph-loop'); a white prompt card rises out of it and pins to a board above the bench ('prompt').",
      [{"at": 0.1, "event": "bench and worker"}, {"at": 0.4, "event": "the /ralph-loop command"}, {"at": 0.8, "event": "the prompt card pinned"}]),
 beat("B01", "The command also writes a small state file into your project. It holds the prompt, a lap counter that starts at one, your cap on laps, and your promise phrase.",
      "B01_StateFile", "A doorway stands at the right; a state-file card drops onto a hook beside it ('state file'); four grey lines draw on it one by one as they are named; a big ink numeral 1 pops beside it ('lap').",
      [{"at": 0.1, "event": "the state file"}, {"at": 0.45, "event": "the lap counter: 1"}, {"at": 0.8, "event": "cap and promise lines"}]),
 beat("B02", "Claude works on the task. Files change, and the work piles up in your repo, here on the shelf. Then Claude decides it's finished, and heads for the door.",
      "B02_Work", "Pages and small commit cubes drop onto a shelf behind the bench ('your repo'); the worker walks from the bench toward the doorway.",
      [{"at": 0.2, "event": "files pile up on the shelf"}, {"at": 0.75, "event": "Claude heads for the door"}]),
 beat("B03", "At the door is the Stop hook. It reads the state file and Claude's last message. No promise there? Then it blocks the exit, adds one to the counter, and hands back the same prompt, word for word.",
      "B03_Hook", "A kraft booth rises beside the doorway ('Stop hook'); its gate arm swings down across the door and its light flashes terracotta; the lap numeral turns from 1 to 2; a copy of the prompt card slides from the booth back to the worker, who walks back to the bench.",
      [{"at": 0.1, "event": "the Stop hook at the door"}, {"at": 0.45, "event": "the arm blocks the exit"}, {"at": 0.65, "event": "lap 2"}, {"at": 0.85, "event": "the same prompt handed back"}]),
 beat("B04", "The prompt never changes. The work does. Each lap, Claude sees its own files and git history from the laps before, and picks up where it left off. And every lap is another full turn of work.",
      "B04_Laps", "The worker runs two quick laps, bench to gate and back; the arm stays down; the lap numeral climbs 2, 3, 4; the shelf fills with more pages and cubes; the pinned prompt card never changes.",
      [{"at": 0.1, "event": "the same prompt"}, {"at": 0.4, "event": "the shelf grows lap by lap"}, {"at": 0.85, "event": "every lap is a full turn"}]),
 beat("B05", "The loop ends one of two ways. One: Claude writes your promise phrase inside promise tags, as an exact match. The hook sees it, deletes the state file, and opens the door. The plugin tells Claude to say it only when it's completely true, never just to get out.",
      "B05_Promise", "The worker raises a white promise token with a terracotta dot ('promise'); it walks to the gate; an ink check lands by the booth; the state-file card and its numeral fade; the arm swings up; the worker walks out through the doorway.",
      [{"at": 0.15, "event": "the promise token"}, {"at": 0.5, "event": "the hook sees it; the state file goes"}, {"at": 0.65, "event": "the door opens"}, {"at": 0.9, "event": "only when true"}]),
 beat("B06", "Two: the counter reaches your max iterations. The hook ends the loop there, done or not. Set neither one, and the plugin warns that the loop runs forever.",
      "B06_Cap", "The stage resets: the worker is back at the bench, the state card returns with the numeral at 8 and the cap beside it ('max 10'); the worker laps as the numeral climbs 9, 10; at 10 the arm swings up and the worker leaves with no token, a grey question mark on the shelf; then an ink loop draws around bench and door with a terracotta dot riding it ('forever').",
      [{"at": 0.15, "event": "the counter climbs to the cap"}, {"at": 0.45, "event": "out, done or not"}, {"at": 0.8, "event": "no cap, no promise: forever"}]),
 beat("B07", "So the plugin's advice: always set max iterations. The promise is one exact phrase, with no way to say stuck. The cap is your main safety net. Use the loop for work a test can check, not work that needs your judgment. And to stop early, run slash cancel ralph.",
      "B07_Advice", "The loop ring fades; the cap numeral pulses ('max 10'); a test board rises beside the bench and three ink checks land on it ('tests'); then the state-file card slides off into a bin ('/cancel-ralph') and the arm swings up.",
      [{"at": 0.1, "event": "always set the cap"}, {"at": 0.55, "event": "work a test can check"}, {"at": 0.9, "event": "/cancel-ralph removes the state file"}]),
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
    "Konnichiwa. This is Liam, in for Bear. Give Claude a big job, and it stops when it thinks it's finished, which can be too soon. So the real question is how to keep Claude working until the job is actually done.",
    "BrutalistHesitantWriter",
    {"text": "Can Claude\nfinish my task in one pass?", "triggerWords": "finish my task in one pass", "replacementWords": "keep working until the job is done",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can Claude finish my task in one pass?'"}, {"at": 0.6, "event": "backspaces 'finish my task in one pass' -> 'keep working until the job is done' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (can Claude finish my task in one pass) and corrects it to the real one (can Claude keep working until the job is done).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A Stop hook: a script Claude Code runs each time Claude tries to stop. A Ralph loop: the same prompt, fed back to Claude again and again. A promise: the exact phrase that ends the loop. And max iterations: the cap on how many laps it gets.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "Stop hook", "meaning": "a script that runs each time Claude tries to stop"},
               {"term": "Ralph loop", "meaning": "the same prompt, fed back again and again"},
               {"term": "promise", "meaning": "the exact phrase that ends the loop"},
               {"term": "max iterations", "meaning": "the cap on how many laps it gets"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'Stop hook' lands"}, {"at": 0.3, "event": "'Ralph loop' lands"}, {"at": 0.55, "event": "'promise' lands"}, {"at": 0.75, "event": "'max iterations' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ('/ralph-loop "Make every test in this repo pass. Do not delete or skip any test. Run the full suite each lap. '
             'Output <promise>COMPLETE</promise> only when every test passes." --completion-promise "COMPLETE" --max-iterations 10')
SPOKEN = ("Slash ralph loop, and in quotes: Make every test in this repo pass. Do not delete or skip any test. Run the full suite each lap. "
          "Output COMPLETE in promise tags, only when every test passes. Then: completion promise, COMPLETE. Max iterations, ten.")
CHECKS = ["Check: run the tests yourself. All pass?",
          "Check: the git diff. Any test deleted or skipped?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Install the Ralph Loop plugin, open Claude Code in a repo you own with failing tests, and paste this. " + SPOKEN +
    " Then check two things yourself. Run the tests: do they all pass? And read the git diff: was any test deleted or skipped?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the /ralph-loop command types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn workshop scene (bench, shelf, doorway with a Stop-hook gate) on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B04", "B05", "B06", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.68-0.78 fill, no defect: no waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · THE RALPH LOOP PLUGIN", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Japanese (Konnichiwa)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude Code users and students who want Claude to keep iterating on a task (getting tests to pass) instead of stopping at the first 'done'",
    "source_doc": "anthropics/claude-plugins-official/plugins/ralph-loop/: README.md, commands/ralph-loop.md, commands/cancel-ralph.md, commands/help.md, hooks/hooks.json, hooks/stop-hook.sh, scripts/setup-ralph-loop.sh (read in full 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "Ralph Loop", "Ralph Wiggum technique", "Stop hook", "hooks", "plugins", "ralph-loop",
             "completion promise", "max iterations", "agentic loop", "claude-plugins-official", "Anthropic", "Nik Bear Brown"]},
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
