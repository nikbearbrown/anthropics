#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-pay-once-for-the-long-part.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #11 under "Batch 2 candidates" in
show-tell-ideas.md (overnight batch 2, 2026-09-27).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-cookbooks/misc/prompt_caching.ipynb (read in full, every cell and output),
confirmed against platform.claude.com/docs/en/build-with-claude/prompt-caching (fetched 2026-09-27).
Cast: a pale BELT (the request) running into a dark READER station (Claude, one terracotta light);
the novel as a thick BOOK block (dark cover, white page edges); the QUESTION as a standing white card;
the cache breakpoint as a terracotta BOOKMARK ribbon; the cache as a kraft wall SHELF where a copy of the
read prompt waits; a segmented TIME METER (grey segments fill as the reader works); a terracotta SCAN LINE
(reading from scratch); a CLOCK disc (the cache lifetime); three PRICE columns (normal / write / read).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Pay Once for the Long Part"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.1, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's the notebook's example: a whole novel, Pride and Prejudice, about a hundred and eighty-seven thousand tokens, with one short question at the end. Book and question go to Claude together, in one request.",
      "B00_Book", "A pale belt draws in toward a dark reader station; a thick book block (dark cover, white page edges) drops onto the belt ('~187k tokens'); a small white question card slides in behind it ('question'); the reader drops in at the belt's end ('Claude') and its light turns terracotta.",
      [{"at": 0.1, "event": "the belt"}, {"at": 0.3, "event": "the novel lands"}, {"at": 0.55, "event": "the question"}, {"at": 0.8, "event": "one request to Claude"}]),
 beat("B01", "With no caching, Claude reads every one of those tokens, on every call. In the notebook's run, that took four point eight nine seconds, just to answer with the book's title.",
      "B01_Slow", "A segmented time meter stands at the right; a terracotta scan line crawls the whole book and card while all ten grey segments fill ('4.89 s'); a small answer slip pops out of the reader.",
      [{"at": 0.1, "event": "every token, every call"}, {"at": 0.45, "event": "the meter fills"}, {"at": 0.85, "event": "a one-line answer"}]),
 beat("B02", "Now add one field at the top of the request: cache control. It sets a bookmark at the end of the prompt. The first call still reads everything, then writes it, up to the bookmark, to the cache. Four point two eight seconds: about the same.",
      "B02_Write", "The meter empties; a terracotta bookmark drops in behind the question card ('cache_control'); the scan line crawls the whole prompt as nine segments fill ('4.28 s'); a kraft shelf appears ('cache') and a copy of book, card and bookmark flies up onto it.",
      [{"at": 0.12, "event": "one field: cache_control"}, {"at": 0.3, "event": "the bookmark"}, {"at": 0.55, "event": "read everything"}, {"at": 0.8, "event": "written to the cache"}]),
 beat("B03", "Send the exact same request again, whole book included. Its start matches what's in the cache, so that part comes off the shelf instead of being read from scratch. One point four eight seconds: three point three times faster, in that run.",
      "B03_Hit", "The meter empties; a fresh copy of the same request rides onto the belt; a dashed line joins the shelf copy to it and an ink check lands; the shelf copy slides down into the reader with no scan; only three segments fill ('1.48 s'); '3.3×'.",
      [{"at": 0.12, "event": "the same request again"}, {"at": 0.35, "event": "the start matches"}, {"at": 0.6, "event": "off the shelf"}, {"at": 0.85, "event": "3.3x faster in that run"}]),
 beat("B04", "It pays most in a conversation. Each turn resends the whole history, and the bookmark moves forward on its own. The book and the earlier turns come from the cache; only the new turn is fresh. After turn one, the notebook says, nearly all input comes from the cache.",
      "B04_Turns", "The meter leaves; answer and question cards line up behind the book ('conversation'); a new question card slides on and the bookmark hops forward past it; a short scan crosses only the new cards, which fly up to join the shelf copy; again for a third turn.",
      [{"at": 0.12, "event": "a conversation"}, {"at": 0.3, "event": "the bookmark moves forward"}, {"at": 0.6, "event": "only the new turn is read"}, {"at": 0.85, "event": "nearly all input from the cache"}]),
 beat("B05", "The bill has the same shape. Writing to the cache costs a quarter more than normal input. Reading from it costs a tenth, or less on some newer models. That's the notebook's headline: up to ninety percent cheaper, and more than twice as fast, for repeated work.",
      "B05_Price", "Three iso columns rise from a slab: a ghost 'normal' column, a slightly taller 'write' column, and a tiny 'read' column; a dashed level line at normal height; the read column's top gets a terracotta dot.",
      [{"at": 0.12, "event": "normal input"}, {"at": 0.3, "event": "write: a quarter more"}, {"at": 0.5, "event": "read: a tenth"}, {"at": 0.8, "event": "up to 90% cheaper, >2x faster (notebook)"}]),
 beat("B06", "Two rules. The start must match exactly: put a timestamp in front of the book, and every call is a miss, and a fresh write. And the cache is short-lived: five minutes by default, per the notebook, and every hit resets the clock.",
      "B06_Rules", "A request arrives with a small card in front of the book ('timestamp'); the dashed match line from the shelf ends at an ink cross ('miss') and the scan crawls the whole book again; a clock disc by the shelf ('5 min') drains; a hit refills it.",
      [{"at": 0.12, "event": "the start must match exactly"}, {"at": 0.35, "event": "a timestamp in front: miss"}, {"at": 0.65, "event": "five minutes"}, {"at": 0.88, "event": "a hit resets the clock"}]),
 beat("B07", "For finer control, place the bookmarks yourself, on individual blocks. The notebook puts one after the book, in the system prompt, and one on the newest question. You get up to four. Its advice: start with automatic, and switch only when you need the control.",
      "B07_Explicit", "Close-up: the prompt as a stack (the book as the system prompt, then turn cards); a cursor places one bookmark after the book ('explicit') and one on the newest question; two ghost bookmark slots appear ('up to 4').",
      [{"at": 0.12, "event": "explicit breakpoints"}, {"at": 0.35, "event": "after the book, in the system prompt"}, {"at": 0.55, "event": "on the newest question"}, {"at": 0.8, "event": "up to four"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.1, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Bonjour. This is Liam, in for Bear. Claude doesn't remember your book between calls. You send it again, every time. So the real question is how to reuse the work on your book.",
    "BrutalistHesitantWriter",
    {"text": "Can Claude\nremember my book?", "triggerWords": "remember my book", "replacementWords": "reuse the work on my book",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can Claude remember my book?'"}, {"at": 0.6, "event": "backspaces 'remember my book' -> 'reuse the work on my book' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (Claude remembers my book) and corrects it to the real one (reuse the work on my book).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A token: a small piece of text. Claude reads, and bills, in tokens. A prefix: the start of a prompt, up to a chosen point. And a cache: a short-lived store of work already done.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "token", "meaning": "a small piece of text; Claude reads and bills in tokens"},
               {"term": "prefix", "meaning": "the start of a prompt, up to a chosen point"},
               {"term": "cache", "meaning": "a short-lived store of work already done"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'token' lands"}, {"at": 0.45, "event": "'prefix' lands"}, {"at": 0.72, "event": "'cache' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Find every place this project calls the Claude API with the same long context each time, like a big system "
             "prompt or a document. Turn on prompt caching with a top-level cache_control, keep that long part first and "
             "unchanged, and move anything that changes, like a timestamp, after it. Then log cache_creation_input_tokens "
             "and cache_read_input_tokens for each call.")
SPOKEN_PROMPT = (YT_PROMPT.replace("cache_creation_input_tokens", "cache creation input tokens")
                 .replace("cache_read_input_tokens", "cache read input tokens").replace("cache_control", "cache control"))
CHECKS = ["Check: run it twice. Does call two show cache reads?",
          "Check: does anything that changes sit before the long part?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + SPOKEN_PROMPT + " Then check two things yourself. Run it twice: does the "
    "second call show cache read tokens? And does anything that changes still sit before the long part?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Pay Once for the Long Part", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03"}   # measured 0.83-0.87 of the safe area at every sampled frame (1080p pre-check); B06/B07 sit at 0.55-0.57, so they keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · PROMPT CACHING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers calling the Claude API who resend the same long context (a document, a system prompt, a conversation) on every request",
    "source_doc": "anthropics/claude-cookbooks/misc/prompt_caching.ipynb (read in full, every cell and its saved outputs), read 2026-09-27; confirmed against platform.claude.com/docs/en/build-with-claude/prompt-caching, fetched 2026-09-27",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["prompt caching", "Claude API", "cache_control", "Anthropic cookbook", "cache breakpoints", "automatic caching",
             "latency", "API cost", "tokens", "multi-turn conversation", "Anthropic", "Claude", "Nik Bear Brown"]},
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
