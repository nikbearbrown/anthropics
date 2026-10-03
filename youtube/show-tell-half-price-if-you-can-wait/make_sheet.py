#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-half-price-if-you-can-wait.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #17 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-cookbooks/misc/batch_processing.ipynb (read in full), checked against the RAW
live docs page (platform.claude.com/docs/en/build-with-claude/batch-processing.md, fetched with curl
2026-09-27, saved in sources/live_batch-processing-2026-09-27.md). Where they differ the live docs win:
the notebook calls the beta namespace and names an old model; the film names no model and no SDK path.
Cast: a pile of white ENVELOPES (requests), each later sealed with a kraft TAG carrying an ink numeral
(its custom_id); a big kraft CLAUDE box with a dark slot on top, a dark mouth on its left face and a
terracotta spark; a kraft TERMINAL (your code); a CLOCK; a dark STATUS board with one lamp
(grey = in_progress, terracotta = ended); four LANES where requests run independently; kraft ANSWER cards
with the same tags; ink checks and one ink cross; two price bars and a hero 50%.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Half Price If You Can Wait"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The usual way is a loop. Send one request, wait for its answer, then send the next. A thousand questions means a thousand waits, and every one is billed at the standard price.",
      "B00_Loop", "A pile of white envelopes at the left ('requests'), the big kraft Claude box at the right ('Claude'), a clock above ('one at a time'); the top envelope rides into the box's slot, the clock hand sweeps a full turn, an answer card slides back out of the box's mouth to the left; then the next envelope, the next wait, the next answer.",
      [{"at": 0.1, "event": "one envelope rides into the slot"}, {"at": 0.35, "event": "the clock sweeps; the answer comes back"}, {"at": 0.7, "event": "the next one, the next wait"}]),
 beat("B01", "A batch is the same requests, in one list. Each one is an ordinary Messages request, plus a custom ID: a tag you choose, like question zero, question one. That tag is how you find its answer later.",
      "B01_Batch", "The loose answers and the clock clear; four envelopes drop into a row on a kraft tray ('batch'); a kraft seal with an ink numeral lands on each, 0, 1, 2, 3, one after another ('custom_id').",
      [{"at": 0.1, "event": "four envelopes on one tray"}, {"at": 0.4, "event": "tags 0, 1, 2, 3 land"}, {"at": 0.8, "event": "the tags pulse"}]),
 beat("B02", "You submit the whole list in one call. It all goes in at once, and you get back a batch ID straight away, with its status: in progress.",
      "B02_Submit", "The tray of sealed envelopes lifts over the Claude box and drops through the slot; a white ticket pops out of the slot and lands at the left ('batch ID'); a dark status board rises beside the box with a grey lamp ('in_progress').",
      [{"at": 0.1, "event": "the tray drops through the slot"}, {"at": 0.55, "event": "the batch ID ticket"}, {"at": 0.8, "event": "the status board, lamp grey"}]),
 beat("B03", "Then it runs asynchronously. Each request is handled on its own, so one failing doesn't hold up the rest. The docs say most batches finish within an hour, and a batch that isn't done within twenty four hours expires.",
      "B03_Async", "The Claude box sits at the left ('Claude'); four lanes run from it to the right; the sealed envelopes ride along them at different speeds and a lamp at the end of each lane lights terracotta as it arrives, in the order 2, 0, 3, 1; then 'most: under 1 hour' and '24 h limit' land at the top.",
      [{"at": 0.1, "event": "four lanes, four envelopes"}, {"at": 0.3, "event": "they finish out of order, lamps light"}, {"at": 0.7, "event": "the time limits, per the docs"}]),
 beat("B04", "Meanwhile, your code polls. Every so often it asks for the batch's status. It says in progress until every request has finished. Then it flips to ended, and the results are ready.",
      "B04_Poll", "Your code (a kraft terminal) at the left ('your code'), the Claude box with its status board at the right; a small white slip rides from the terminal to the board and back, three times, while the clock hand advances; on the third the lamp turns terracotta and 'in_progress' becomes 'ended'.",
      [{"at": 0.1, "event": "a poll rides to the board and back"}, {"at": 0.45, "event": "still in progress"}, {"at": 0.8, "event": "the lamp lights: ended"}]),
 beat("B05", "The results come back as one list, but in any order. The docs say so plainly. So never match by position. Match by custom ID. The answer tagged two goes with the request tagged two.",
      "B05_Match", "The four sealed envelopes in a row at the top ('requests'); four kraft answer cards slide out of the Claude box into a row below in the order 2, 0, 3, 1 ('results'); then each answer card moves under the envelope with the same tag ('by custom_id').",
      [{"at": 0.1, "event": "answers arrive 2, 0, 3, 1"}, {"at": 0.55, "event": "never by position"}, {"at": 0.75, "event": "each moves under its tag"}]),
 beat("B06", "Each result also says how it went. Most say succeeded, with Claude's message inside. One might say errored, and errored requests aren't billed. So you send just the failed ones again.",
      "B06_Results", "The matched pairs: ink checks land beside answers 0, 2 and 3 ('succeeded'); an ink cross lands beside answer 1 ('errored'); answer 1 clears, and envelope 1 rides back into the Claude box on its own.",
      [{"at": 0.15, "event": "checks: succeeded"}, {"at": 0.45, "event": "a cross: errored"}, {"at": 0.8, "event": "only the failed one goes back"}]),
 beat("B07", "And the payoff. Anthropic's docs say all batch usage is charged at fifty percent of standard API prices. The trade is time, and results stay available for twenty nine days. If the answers can wait, they cost half.",
      "B07_Half", "Two price bars in grey segments: 'standard' grows full height; 'batch' grows full, then its top half slides away; a hero '50%' lands with 'per Anthropic's docs' under it; a clock rises beside the batch bar and its hand sweeps.",
      [{"at": 0.15, "event": "the standard bar"}, {"at": 0.35, "event": "the batch bar loses its top half"}, {"at": 0.5, "event": "50%, per Anthropic's docs"}, {"at": 0.7, "event": "the clock: the trade is time"}]),
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
    "Bonjour. This is Liam, in for Bear. Say you have a thousand questions for Claude. You could send them one at a time and wait on each. But if the answers can wait, you can send them all as one batch, at half the price. So the real question is how to hand Claude the whole pile at once.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nsend a thousand requests faster?", "triggerWords": "send a thousand requests faster", "replacementWords": "hand Claude the whole pile at once",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I send a thousand requests faster?'"}, {"at": 0.6, "event": "backspaces 'send a thousand requests faster' -> 'hand Claude the whole pile at once' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I send a thousand requests faster) and corrects it to the real one (how do I hand Claude the whole pile at once).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A batch: a list of requests you send together and collect later. A custom ID: the tag you put on each request. And a result: what comes back for each one, saying whether it succeeded or errored.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "batch", "meaning": "a list of requests sent together, collected later"},
               {"term": "custom_id", "meaning": "the tag you put on each request"},
               {"term": "result", "meaning": "what comes back for each: succeeded or errored"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'batch' lands"}, {"at": 0.4, "event": "'custom_id' lands"}, {"at": 0.75, "event": "'result' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Find the loop in this repo that calls the Claude API once per item. Rewrite it as a Message Batches job: "
             "give each request a valid custom_id built from the item's key, submit them as one batch, poll until "
             "processing_status is ended, then match each result to its item by custom_id and print any that errored.")
SPOKEN_PROMPT = (YT_PROMPT.replace("valid custom_id", "valid custom ID").replace("by custom_id", "by custom ID")
                 .replace("processing_status", "processing status"))
CHECKS = ["Check: one result per item, matched by custom_id?",
          "Check: are errored items printed, not dropped?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code, in a repo with a script that calls Claude in a loop: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Does every item get exactly one result, matched by its custom ID? And are the errored ones printed, not silently dropped?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn envelopes-box-and-tags scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B05", "B06"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.61-0.66 throughout; B01 (0.51), B02 (0.17), B03 (0.53), B04 (0.58, kept for margin) and B07 (0.29 at 25%) keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE API · MESSAGE BATCHES", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who grade, label or summarise in bulk with the Claude API and don't need the answers right away",
    "source_doc": "anthropics/claude-cookbooks/misc/batch_processing.ipynb (read in full 2026-09-27); checked against the raw live docs page platform.claude.com/docs/en/build-with-claude/batch-processing.md (fetched with curl 2026-09-27, saved in sources/)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude API", "Message Batches", "batch processing", "custom_id", "asynchronous", "polling",
             "50% discount", "bulk", "evaluation", "Anthropic", "cookbook", "Nik Bear Brown"]},
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
