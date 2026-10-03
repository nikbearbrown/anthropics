#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-screenshot-point-click.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #21 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Sources (read in full, raw): anthropics/claude-quickstarts/computer-use-demo/README.md and
computer_use_demo/loop.py (sampling_loop, _maybe_filter_to_n_most_recent_images), computer_use_demo/tools/computer.py
(screenshot after each action, coordinate scaling); computer-use-best-practices/README.md; the RAW live docs page
platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md (curl, 2026-09-27, sources/). The local
quickstart files were diffed against raw GitHub main (sources/live_claude-quickstarts_*): the README caution block,
the loop and the pruning are unchanged; GitHub adds toolset support. The live docs say `status: ga` on the Claude API
(computer_toolset_20260801, no beta header); the demo README still says "beta" (earlier tool versions stay beta).
Cast: a kraft CRATE (the container) with a flat MONITOR standing in it (grey bezel, cream screen, grey title bar,
window blocks, a terracotta-dot button); YOUR CODE, a kraft terminal inside the crate; the kraft CLAUDE box (slot,
mouth, spark); the SCREENSHOT, a small copy of the screen; the ACTION slip; a grey target ring with a terracotta dot;
the kit cursor; a SHELF of screenshots; login card, allowlist sites, a note on a web page; YOUR BOARD and a confirm pill.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Screenshot, Point, Click"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's quickstart demo runs a whole Linux desktop inside a Docker container. Claude never connects to that desktop. Your code sits in between. The demo's read me still says beta; the live docs now say generally available, on the Claude API.",
      "B00_Crate", "A kraft crate drops in ('container'); a monitor rises inside it and its desktop draws (title bar, windows, a button); a kraft terminal lands beside it ('your code'); the Claude box lands at the right ('Claude'); a cable draws from the terminal to Claude.",
      [{"at": 0.1, "event": "the crate, 'container'"}, {"at": 0.3, "event": "the desktop rises inside it"}, {"at": 0.5, "event": "your code, between"}, {"at": 0.7, "event": "Claude, outside"}]),
 beat("B01", "Step one. You send Claude your task. Claude asks to see the screen, so your code takes a screenshot, and sends it back.",
      "B01_Snap", "A task slip rides from your code into Claude's slot ('task'); a small request slip rides back out of Claude's mouth; the screen flashes; a small copy of it (the screenshot) lifts off above the terminal ('screenshot') and rides into Claude's slot.",
      [{"at": 0.15, "event": "the task goes to Claude"}, {"at": 0.4, "event": "Claude asks to see the screen"}, {"at": 0.6, "event": "the screen flashes; the screenshot lifts off"}, {"at": 0.85, "event": "the screenshot rides to Claude"}]),
 beat("B02", "Claude looks at the picture, and answers with an action: say, a left click, at an x, y spot, counted in pixels from the screenshot's top left corner. It can't click anything itself.",
      "B02_Point", "The screenshot opens large beside Claude; a grey target ring with a terracotta dot lands on its button; grey guide lines draw from the top edge and the left edge ('x, y'); an action slip rides out of Claude's mouth ('left click').",
      [{"at": 0.15, "event": "the screenshot, large"}, {"at": 0.35, "event": "the target lands on the button"}, {"at": 0.55, "event": "x from the left, y from the top"}, {"at": 0.85, "event": "an action slip, not a click"}]),
 beat("B03", "So your code does the clicking. If it shrank the screenshot to fit, it first scales the spot back up to the real screen. Then it moves the mouse, and clicks.",
      "B03_Click", "The action slip rides into the terminal; the target on the small screenshot grows to the same spot on the big screen ('scale up'); the cursor glides to it; a click ring; a new window opens on the desktop ('click').",
      [{"at": 0.15, "event": "the slip reaches your code"}, {"at": 0.45, "event": "the spot scales up to the screen"}, {"at": 0.75, "event": "the mouse moves and clicks; a window opens"}]),
 beat("B04", "Then a fresh screenshot goes back, so Claude can see what the click did. It picks the next action, and round it goes. The loop ends when Claude answers in text, instead of asking for another action.",
      "B04_Loop", "A second flash and screenshot ride to Claude; a slip comes back; a loop arrow draws round the path ('loop') and turns again; then Claude sends a white text card instead of a slip, and a check lands ('done').",
      [{"at": 0.1, "event": "a fresh screenshot"}, {"at": 0.35, "event": "the next action"}, {"at": 0.55, "event": "the loop goes round"}, {"at": 0.85, "event": "a text answer ends it"}]),
 beat("B05", "Every screenshot stays in the conversation, and each one costs tokens. The docs suggest keeping the last three, pruning older ones in batches, not every turn, so the prompt cache keeps working. On the newest models, let the API clear old ones instead.",
      "B05_Shelf", "A shelf under Claude fills with screenshots one by one ('screenshots'); a grey bar under them grows (tokens); the oldest ones drop off together in one batch; three stay ('last three').",
      [{"at": 0.1, "event": "screenshots pile up"}, {"at": 0.3, "event": "the cost bar grows"}, {"at": 0.6, "event": "the old ones drop together"}, {"at": 0.8, "event": "the last three stay"}]),
 beat("B06", "Now the warning, in Anthropic's own words. Use a dedicated virtual machine or container, with minimal privileges. Avoid giving the model access to sensitive data, such as account login information. And limit internet access to an allowlist of domains.",
      "B06_Sandbox", "The crate returns and a grey strap with one terracotta seal wraps it ('dedicated VM'); a login card slides toward it and is stopped with an ink cross ('no logins'); a cable leaves the crate to four site blocks; two get checks, two get crosses ('allowlist').",
      [{"at": 0.2, "event": "a dedicated, sealed crate"}, {"at": 0.5, "event": "no login card goes in"}, {"at": 0.8, "event": "only allowlisted sites"}]),
 beat("B07", "Because Claude reads the screen, the screen can talk back. Instructions on a web page, or in an image, might override yours. That's prompt injection. Anthropic's tool scans screenshots for it, but the precautions still matter.",
      "B07_Inject", "A web page on the desktop grows a planted note; the screenshot rides to Claude and a dashed line pulls Claude's target off the button toward the note ('prompt injection'); a terracotta scan line sweeps the screenshot; a flag pops up ('scan'); the crate's seal pulses.",
      [{"at": 0.15, "event": "a note planted on the page"}, {"at": 0.4, "event": "the note pulls the target off course"}, {"at": 0.7, "event": "a scan flags it"}]),
 beat("B08", "And a human confirms decisions with real-world consequences, like accepting cookies, paying, or agreeing to terms of service. Claude can send several actions in one turn, so check before each one runs.",
      "B08_Confirm", "Three action slips ride from Claude toward the crate; a gate bar across the path; the third slip (terracotta dot) stops at it; your board's lamp is grey ('you confirm'); your cursor presses a confirm pill; the lamp turns terracotta; the gate lifts and the slip passes ('each action').",
      [{"at": 0.15, "event": "slips head to the desktop"}, {"at": 0.4, "event": "a consequential one stops at the gate"}, {"at": 0.65, "event": "you confirm"}, {"at": 0.85, "event": "checked before each action"}]),
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
    "Namaste. This is Liam, in for Bear. Computer use lets Claude work a desktop, so it's natural to ask how Claude controls your computer. It doesn't, directly. Your code takes every screenshot and makes every click. So the real question is how your code turns a screenshot into a click.",
    "BrutalistHesitantWriter",
    {"text": "How does\nClaude control my computer?", "triggerWords": "Claude control my computer", "replacementWords": "my code turn a screenshot into a click",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How does Claude control my computer?'"}, {"at": 0.6, "event": "backspaces 'Claude control my computer' -> 'my code turn a screenshot into a click' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how does Claude control my computer) and corrects it to the real one (how does my code turn a screenshot into a click).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Computer use: Claude sees screenshots, and asks for mouse and keyboard actions. The agent loop: your code runs each one, and reports back. A coordinate: an x, y spot in the screenshot. A sandbox: a virtual machine or container, walled off from your machine.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "computer use", "meaning": "Claude sees screenshots and asks for mouse and keyboard actions"},
               {"term": "agent loop", "meaning": "your code runs each action and reports back"},
               {"term": "coordinate", "meaning": "an x, y spot in the screenshot"},
               {"term": "sandbox", "meaning": "a VM or container, walled off from your machine"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'computer use' lands"}, {"at": 0.35, "event": "'agent loop' lands"}, {"at": 0.6, "event": "'coordinate' lands"}, {"at": 0.8, "event": "'sandbox' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Clone anthropics/claude-quickstarts and read computer-use-demo/README.md. Start its Docker container with my "
             "API key from the environment, mounting only ~/.anthropic. Then tell me which page to open, and suggest a harmless first task.")
SPOKEN_PROMPT = ("Clone anthropics slash claude quickstarts, and read the computer use demo read me. Start its Docker container with my "
                 "API key from the environment, mounting only the dot anthropic folder. Then tell me which page to open, and suggest a harmless first task.")
CHECKS = ["Check: docker inspect shows only ~/.anthropic mounted?",
          "Check: a fresh screenshot after every click?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In Claude Code, paste this: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Does docker inspect show only the dot anthropic folder mounted? And does a fresh screenshot come back after every click?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn crate-desktop-and-Claude scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B04", "B07", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.63-0.73 throughout; B00 (0.37 at 25%), B05 (0.53) and B06 (0.40 at 25-40%) keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE API · COMPUTER USE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hindi (Namaste)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who want to see how Claude's computer use actually runs, and how to run it safely",
    "source_doc": "anthropics/claude-quickstarts/computer-use-demo/ (README.md, computer_use_demo/loop.py, tools/computer.py) and computer-use-best-practices/README.md, read in full 2026-09-27 and diffed against raw GitHub main; raw live docs platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md (curl, 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "computer use", "agent loop", "screenshots", "coordinates", "Claude API", "Docker", "sandbox",
             "prompt injection", "human in the loop", "AI safety", "Anthropic", "Nik Bear Brown"]},
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
