#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-spending-your-effort.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #9 in show-tell-ideas.md
(Bear: "show-tell for this film as well", with 16 frames of Anthropic's effort-dial animation).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Sources: Thariq Shihipar, "Using Claude Code: Spending your effort", claude.dev/blog/spending-your-effort/
(Sep 25, 2026), and Anthropic's docs, platform.claude.com/docs/en/build-with-claude/effort. Both read 2026-09-26.
Cast: the kraft effort DIAL (a knob on a round base, five ticks: low, medium, high, xhigh, max; ink pointer,
terracotta tip dot, terracotta marker dot beside the active level), a dark SERVER stack (compute), two CLOCK
faces, grey VERIFICATION / JUDGEMENT columns, the kraft FILTER box (html-js-filter), five TRY tiles, four
step icons, use-case icons per level, and the four LOOP pills with the /effort chip.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Spending Your Effort"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's the dial. Five settings: low, medium, high, x high, and max. Opus five point five starts at medium. Most other models start at high.",
      "B00_Dial", "The kraft dial rises onto the stage; five ticks draw with their labels as each is spoken; the pointer sweeps low to max, then settles on medium and a terracotta marker dot lands beside 'medium'; a grey dot marks 'high' for the other models.",
      [{"at": 0.1, "event": "the dial arrives"}, {"at": 0.35, "event": "five ticks and labels"}, {"at": 0.65, "event": "pointer settles on medium"}, {"at": 0.9, "event": "high marked for other models"}]),
 beat("B01", "So what is effort, really? Thariq Shihipar, in his post Spending your effort, says it gives the model an approximation of how much compute you want it to spend on the task.",
      "B01_Compute", "The dial steps left; a dark server stack slides in on the right ('compute'); a cable draws from the dial to it; the pointer turns up and the server lights come on one by one, then back down and they go out.",
      [{"at": 0.15, "event": "dial steps left"}, {"at": 0.4, "event": "compute stack + cable"}, {"at": 0.75, "event": "pointer up, lights on"}]),
 beat("B02", "Think of it like a deadline. Given one hour, you'd bring the best version that meets the task, then expect to iterate. Given twelve hours straight, you'd assume they want you to try very hard.",
      "B02_Clocks", "The dial shrinks to the top; two clock faces arrive; on 'one hour' the pointer turns to low, a grey wedge sweeps one hour on the left clock and a single draft page lands with a loop arrow; on 'twelve hours' the pointer turns to max, the right clock's wedge sweeps the full face and pages stack high.",
      [{"at": 0.1, "event": "two clocks"}, {"at": 0.35, "event": "1 hour: a draft, then iterate"}, {"at": 0.75, "event": "12 hours: try very hard"}]),
 beat("B03", "Effort works the same way. Claude always tries to do your task reasonably, but higher effort means more independent action on verification and judgement.",
      "B03_CheckJudge", "The dial returns at the left, pointer on low, with two short grey columns on the right ('verification', 'judgement'); as the pointer steps up through each level, both columns grow a slab at a time.",
      [{"at": 0.15, "event": "dial on low, two short columns"}, {"at": 0.55, "event": "pointer steps up"}, {"at": 0.85, "event": "columns grow"}]),
 beat("B04", "The clearest case is HTML JS filter, a Terminal-Bench three point oh task: an HTML sanitizer that strips every way of smuggling JavaScript into a page. In Anthropic's runs, Fable five point one on low passed one of five tries: about two minutes, one pass, one hand-written test page.",
      "B04_LowRun", "A kraft filter box slides in ('html-js-filter'); a page carrying a dark script block goes in and comes out clean, the block dropped; on 'on low' a small dial set to low appears at the left with a clock showing a thin wedge; five try tiles appear, one checks and four cross; '1/5' lands; one test page passes through once.",
      [{"at": 0.1, "event": "the filter box"}, {"at": 0.3, "event": "a script block is stripped"}, {"at": 0.6, "event": "low: 1 of 5"}, {"at": 0.9, "event": "one pass, one test page"}]),
 beat("B05", "On x high, it passed five of five. The run he traced took about thirty-three minutes. It reviewed its own draft adversarially, read the installed parser's source, ran a standard X S S test suite, and wrote a random-document fuzzer.",
      "B05_XhighRun", "The filter box leaves; beside the low column an xhigh column arrives: a dial set to xhigh, a clock with a wide wedge, five try tiles that all check, '5/5'; four step icons drop in one per spoken step (a ringed draft, the parser's dark source block, a stack of test pages, a spray of random cubes).",
      [{"at": 0.15, "event": "xhigh: 5 of 5"}, {"at": 0.4, "event": "a long run"}, {"at": 0.6, "event": "self-review, parser source"}, {"at": 0.85, "event": "XSS suite, fuzzer"}]),
 beat("B06", "His rule of thumb. Low for quick responses while you're in the loop: brainstorming, sketching, easy changes. Medium for most regular engineering work, like new features.",
      "B06_LowMedium", "The big dial on the left; the pointer turns to low and the marker dot jumps beside 'low'; a sketch page draws its doodle ('sketches'); the pointer turns to medium and a feature crate is assembled ('new features').",
      [{"at": 0.15, "event": "low"}, {"at": 0.4, "event": "a sketch"}, {"at": 0.65, "event": "medium"}, {"at": 0.85, "event": "a feature crate"}]),
 beat("B07", "High where verification matters or there are edge cases, like fixing a bug. Max when you want Claude working fully on its own on difficult problems.",
      "B07_HighMax", "The pointer turns to high; a bug appears under a magnifier ring ('bug fixes'); the pointer turns to max and a crate with its own light runs laps on a loop belt, alone ('on its own').",
      [{"at": 0.15, "event": "high"}, {"at": 0.35, "event": "a bug under a lens"}, {"at": 0.65, "event": "max"}, {"at": 0.85, "event": "a crate runs on its own"}]),
 beat("B08", "And his loop for feature work. Have Claude interview you about the spec. Build it on low. Review it, iterating on low. Then verify and test on high. In Claude Code, slash effort switches the level mid-conversation.",
      "B08_Loop", "The dial shrinks to the centre; four pills arrive around it (interview, build on low, review, verify on high) joined by ink arrows; a terracotta dot moves to each step as it is spoken while the pointer sits on low, then turns to high at verify; a '/effort' chip drops in and a cursor clicks it.",
      [{"at": 0.1, "event": "the loop"}, {"at": 0.3, "event": "interview, build on low"}, {"at": 0.55, "event": "review, verify on high"}, {"at": 0.85, "event": "/effort"}]),
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
    "Salaam. This is Liam, in for Bear. Claude Code has an effort dial, and it's tempting to always turn it up. The better question is how to match effort to the job.",
    "BrutalistHesitantWriter",
    {"text": "Should I always\nturn effort up?", "triggerWords": "turn effort up", "replacementWords": "match effort to the job",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Should I always turn effort up?'"}, {"at": 0.6, "event": "backspaces 'turn effort up' -> 'match effort to the job' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (should I always turn effort up) and corrects it to the real one (match effort to the job).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Effort: how much compute Claude spends on a task. An edge case: an unusual input where code tends to break. And slash effort: the Claude Code command that changes the level mid-conversation.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "effort", "meaning": "how much compute Claude spends on a task"},
               {"term": "edge case", "meaning": "an unusual input where code tends to break"},
               {"term": "/effort", "meaning": "the Claude Code command that changes the level mid-conversation"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'effort' lands"}, {"at": 0.4, "event": "'edge case' lands"}, {"at": 0.7, "event": "'/effort' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Plan one real task with me through the effort loop: [task]. First, interview me about any details I'm missing. "
             "Then list which steps to run on low effort and which on high. For the high-effort verification, say exactly what "
             "it must check: which edge cases, which tests, and what counts as a failure. Don't build anything yet.")
SPOKEN_PROMPT = YT_PROMPT.replace("[task]", "name your task")
CHECKS = ["Check: does every high step name something concrete to verify?",
          "Check: build on low, then /effort high to verify. Did it catch what low missed?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + SPOKEN_PROMPT + " Then check two things yourself. Does every high step "
    "name something concrete to verify? And build on low, then switch to high with slash effort to verify. Did it catch what low missed?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Plan One Task Through the Loop", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "Low"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn isometric scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · EFFORT", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Arabic / Persian / Urdu (Salaam)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude Code users deciding which effort level to run a task at",
    "source_doc": "Thariq Shihipar, 'Using Claude Code: Spending your effort', https://claude.dev/blog/spending-your-effort/ (Sep 25, 2026); Anthropic docs, https://platform.claude.com/docs/en/build-with-claude/effort; both read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["effort", "Claude Code", "/effort", "xhigh", "Opus 5.5", "Fable 5.1", "Terminal-Bench 3.0", "html-js-filter",
             "verification", "edge cases", "Thariq Shihipar", "Anthropic", "Claude", "Nik Bear Brown"]},
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
