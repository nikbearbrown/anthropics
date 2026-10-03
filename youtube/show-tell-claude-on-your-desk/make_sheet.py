#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-claude-on-your-desk.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #6 in show-tell-ideas.md.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-desktop-buddy/ (README.md, REFERENCE.md and CONTRIBUTING.md in full;
src/main.cpp, src/data.h and src/ble_bridge.cpp skimmed for what the example device does).
Cast: a kraft DESK; a kraft LAPTOP whose screen is a pale Claude window carried by a dark title
bar; a small upright kraft DEVICE (the ESP32 stick) outlined in dark kraft, with a dark screen, a
front button, a side button and a light; the dashed-then-solid Bluetooth ARC between them; white
SNAPSHOT packets that ride the arc; the pet's face on the device screen; a PROMPT card; a grey
radio DONGLE; a PADLOCK; the BLUEPRINT sheet (REFERENCE.md) with other makers' devices.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Claude on Your Desk"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's the desk. A laptop runs the Claude app, on Mac or Windows. Beside it sits a tiny device with a screen and buttons. The app can connect your Cowork and Claude Code sessions to it, over Bluetooth.",
      "B00_Desk", "A kraft desk slides up; a laptop lands on it and its screen opens to a Claude window; a tiny upright device drops in beside it; a dashed Bluetooth arc draws from the laptop to the device.",
      [{"at": 0.1, "event": "the desk"}, {"at": 0.3, "event": "laptop running Claude"}, {"at": 0.55, "event": "the tiny device"}, {"at": 0.85, "event": "a Bluetooth arc (not yet on)"}]),
 beat("B01", "That bridge is off by default, and you opt in. Turn on developer mode, open Hardware Buddy, click connect, and pick your device. After that, it reconnects by itself. It's for makers, not an official product feature.",
      "B01_OptIn", "The dashed arc greys out; on the laptop screen a toggle slides on (developer mode); a cursor clicks a Connect pill; the arc redraws solid ink with a terracotta dot at each end.",
      [{"at": 0.1, "event": "off by default"}, {"at": 0.35, "event": "developer mode on"}, {"at": 0.55, "event": "Connect"}, {"at": 0.75, "event": "the link is live"}]),
 beat("B02", "Now the app sends a snapshot whenever something changes, and every ten seconds anyway: how many sessions are running or waiting, plus a few recent transcript lines, newest first. The tiny screen scrolls them.",
      "B02_Snapshot", "The camera steps in: laptop left, the device enlarged right. Transcript lines appear in the Claude window; white snapshot packets ride the arc; on the device's dark screen new lines slide in at the top and push the older ones down.",
      [{"at": 0.15, "event": "a snapshot rides the arc"}, {"at": 0.45, "event": "another, on a change"}, {"at": 0.75, "event": "recent lines scroll on the tiny screen"}]),
 beat("B03", "The team's own example is a desk pet, on an E S P thirty-two board. It sleeps when nothing's happening. Start a session, and it wakes up.",
      "B03_PetWakes", "The device's screen shows a face with closed eyes, breathing slowly (asleep); a new session window pops open on the laptop; a packet rides the arc; the pet's eyes open (awake).",
      [{"at": 0.2, "event": "ESP32 desk pet"}, {"at": 0.45, "event": "asleep"}, {"at": 0.8, "event": "a session starts: awake"}]),
 beat("B04", "Now Claude wants to run a Bash command, and it needs your permission. The snapshot carries a prompt: the tool, a short hint, and an ID. It shows up on the device too, and the pet gets impatient. Its light blinks.",
      "B04_Prompt", "A permission prompt card appears in the Claude window (Bash); a copy rides the arc and lands on the device's screen under the pet; the device's light blinks terracotta.",
      [{"at": 0.15, "event": "Claude asks to run Bash"}, {"at": 0.45, "event": "the prompt mirrors onto the device"}, {"at": 0.8, "event": "the light blinks"}]),
 beat("B05", "Press the front button, and the device sends back one line: that same ID, and the decision, once. Once approves that one tool call. The other button sends deny. Approve quickly, and the pet shows hearts.",
      "B05_Approve", "The front button presses in; a reply packet rides the arc back to the laptop; the laptop's prompt card gets a check and the light stops; the side button pulses (deny); hearts float up from the pet.",
      [{"at": 0.15, "event": "front button pressed"}, {"at": 0.4, "event": "the reply rides back: once"}, {"at": 0.65, "event": "the other button: deny"}, {"at": 0.9, "event": "hearts"}]),
 beat("B06", "That link carries transcript snippets and tool hints, and an unencrypted one can be read by anyone in radio range with a cheap dongle. So the reference says to require encrypted pairing. The device shows a six-digit pass key, you type it into the app, and the link is encrypted from then on.",
      "B06_Pairing", "Packets ride the arc; a small grey dongle slides in below and a dashed line reaches up to the arc; a six-digit passkey appears on the device screen, then the same digits in the Claude window; a padlock closes on the arc and the dongle's line snaps back.",
      [{"at": 0.15, "event": "snippets on the air"}, {"at": 0.35, "event": "a cheap dongle listens"}, {"at": 0.6, "event": "passkey on device, typed in the app"}, {"at": 0.85, "event": "padlock: encrypted"}]),
 beat("B07", "And you don't need any of this code. REFERENCE dot md is the contract: advertise the Nordic UART Service, a standard way to send text over Bluetooth, then trade one line of JSON at a time. An Arduino, or a Raspberry Pi with a Bluetooth dongle, will do. The repo's own advice: the best contribution is a fork.",
      "B07_Blueprint", "The example device slides away; a blueprint sheet unrolls on the desk (REFERENCE.md); one line packets ride the arc; a flat board and a round puck appear on the sheet, each drawing its own arc to the laptop; a fork line branches from the sheet to them.",
      [{"at": 0.12, "event": "the example leaves"}, {"at": 0.3, "event": "REFERENCE.md: the contract"}, {"at": 0.55, "event": "one JSON line at a time"}, {"at": 0.8, "event": "other boards; fork it"}]),
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
    "Hej. This is Liam, in for Bear. Claude's desk buddy isn't a product feature. It's an opt-in API for makers, so the real question is how you build one.",
    "BrutalistHesitantWriter",
    {"text": "How do I buy\na Claude desk buddy?", "triggerWords": "buy", "replacementWords": "build",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I buy a Claude desk buddy?'"}, {"at": 0.6, "event": "backspaces 'buy' -> 'build' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (where to buy a Claude desk buddy) and corrects it to the real one (how to build one).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. B L E, Bluetooth Low Energy: a low-power wireless link. A permission prompt: Claude asking before it runs a tool. And a reference repo: one worked example, made to be copied.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "BLE", "meaning": "Bluetooth Low Energy, a low-power wireless link"},
               {"term": "permission prompt", "meaning": "Claude asking before it runs a tool"},
               {"term": "reference repo", "meaning": "one worked example, made to be copied"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'BLE' lands"}, {"at": 0.4, "event": "'permission prompt' lands"}, {"at": 0.7, "event": "'reference repo' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is REFERENCE.md from anthropics/claude-desktop-buddy: [paste it]. Help me plan a tiny device of my own "
             "that speaks this protocol: [your device]. List what its screen shows from each snapshot, which permission "
             "prompts it may approve with a button press, and what it must never do without a person. "
             "Plan only; no firmware yet.")
SPOKEN_PROMPT = (YT_PROMPT.replace("REFERENCE.md", "REFERENCE dot md")
                 .replace("anthropics/claude-desktop-buddy", "Anthropic's claude desktop buddy repo")
                 .replace("[paste it]", "paste it")
                 .replace("[your device]", "name your device"))
CHECKS = ["Check: find every approval in the plan. Is each one a button press?",
          "Check: open REFERENCE.md. Do the plan's field names match it exactly?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + SPOKEN_PROMPT + " Then check two things yourself. Find every approval in the plan. "
    "Is each one a button press? And open REFERENCE dot md. Do the plan's field names match it exactly?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Plan Your Own Desk Device", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn desk scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · HARDWARE BUDDY", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Swedish / Danish / Norwegian (Hej)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Makers and developers who use the Claude desktop app and want a small device that shows Claude's prompts and lets them approve from the desk",
    "source_doc": "anthropics/claude-desktop-buddy (README.md, REFERENCE.md, CONTRIBUTING.md; src/main.cpp, src/data.h, src/ble_bridge.cpp skimmed), read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude desktop", "Hardware Buddy", "BLE", "Bluetooth Low Energy", "ESP32", "Nordic UART Service",
             "permission prompts", "Claude Code", "Cowork", "maker", "desk pet", "Anthropic", "Claude", "Nik Bear Brown"]},
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
