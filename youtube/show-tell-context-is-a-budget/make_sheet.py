#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-context-is-a-budget.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #3 in show-tell-ideas.md.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: Anthropic Engineering, "Effective context engineering for AI agents" (Sep 29, 2025),
saved page anthropics/youtube/Effective context engineering for AI agents _ Anthropic.html.
One tray cast for the whole film (series continuity with show-tell-how-a-skill-loads, where the
tray was "context"): the TRAY (the context window), BLOCKS (white instruction page, dark tool
blocks, kraft message blocks, white result slabs, a kraft data box), a NEEDLE card (the fact the
model must recall, terracotta dot), a DATA CRATE outside the tray (just-in-time), a PRESS plate
(compaction), a NOTEBOOK outside the tray (note-taking), and small CRATES (sub-agents) that
send back one SUMMARY card each.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Context Is a Budget"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Picture the context window as a tray. Everything the model sees has to fit in it: the instructions, the tools, the message history, and any data it pulls in.",
      "B00_Tray", "A kraft tray slides onto the stage (context window); one block drops in per phrase: a white instruction page, dark tool blocks, kraft message blocks, a kraft data box.",
      [{"at": 0.1, "event": "tray slides in"}, {"at": 0.45, "event": "instructions, tools"}, {"at": 0.75, "event": "history, data"}]),
 beat("B01", "An agent working in a loop keeps adding to it. Every tool call, every result, lands in the tray. But more isn't better. As the tray fills, the model recalls what's inside less accurately. Anthropic calls this context rot.",
      "B01_Rot", "Rows of message blocks and white result slabs drop in until the tray is full; a small card with a terracotta dot (the fact that matters) gets buried; then every block pales, the dot fades to grey, and 'context rot' lands.",
      [{"at": 0.15, "event": "blocks pile in"}, {"at": 0.55, "event": "more isn't better"}, {"at": 0.75, "event": "blocks pale, the dot fades"}, {"at": 0.9, "event": "context rot"}]),
 beat("B02", "Why? Attention is a budget. Every token attends to every other token, so n tokens make n squared pairs. Add more, and each one gets a thinner share.",
      "B02_Budget", "Above a small tray, four token dots link to each other with ink lines; four more dots pop in and the web redraws with many more, thinner links; 'n²' sits beside it.",
      [{"at": 0.2, "event": "four tokens, every pair linked"}, {"at": 0.5, "event": "n²"}, {"at": 0.7, "event": "more tokens, thinner links"}]),
 beat("B03", "So the goal is the smallest set of high-signal tokens that gets the job done. A clear prompt. A few tools that don't overlap. A handful of good examples, not a laundry list of edge cases.",
      "B03_Curate", "The full, pale tray: the pale blocks lift out and slide away; a duplicate tool block leaves; a tall stack of thin edge-case slips is swapped for three example cards; what stays gets a terracotta dot each ('high signal').",
      [{"at": 0.15, "event": "pale blocks lift out"}, {"at": 0.5, "event": "overlapping tool leaves"}, {"at": 0.8, "event": "laundry list -> three examples"}]),
 beat("B04", "Next, don't load everything up front. Keep lightweight references, like file paths and links, and load the data just in time. Claude Code does this, using commands like head and tail to read big data without loading all of it.",
      "B04_JustInTime", "A tall data crate stands outside the tray; in the tray, only a small white tag tied to it by a dashed line ('file path'); on 'just in time' one thin slice slides from the crate into the tray; on 'head and tail' the top and bottom slices light, and only they come in.",
      [{"at": 0.15, "event": "crate stays outside"}, {"at": 0.35, "event": "a reference tag in the tray"}, {"at": 0.55, "event": "one slice loads"}, {"at": 0.85, "event": "head and tail"}]),
 beat("B05", "Long tasks outgrow any tray, and Anthropic describes three fixes. First, compaction. Near the limit, the history gets summarized. In Claude Code, that keeps decisions and unresolved bugs, and drops redundant tool outputs. Then a fresh window starts from the summary.",
      "B05_Compaction", "A full tray; two blocks with terracotta dots are marked (decisions, bugs); the pale result slabs slide away; a dark press plate comes down and squeezes what's left into one summary block, which sits alone in the fresh tray.",
      [{"at": 0.25, "event": "full tray"}, {"at": 0.5, "event": "keep / drop"}, {"at": 0.75, "event": "press -> one summary block"}]),
 beat("B06", "Second, structured note-taking. The agent writes notes to a file outside the window, like a to-do list. After the context resets, it reads them back and carries on.",
      "B06_Notes", "A notebook sits beside the tray; slips fly from the tray into it and its lines fill; the tray empties (reset); one note page flies back into the tray, and a check lands.",
      [{"at": 0.2, "event": "notes written outside"}, {"at": 0.6, "event": "context resets"}, {"at": 0.8, "event": "notes read back"}]),
 beat("B07", "Third, sub-agents. The main agent keeps the plan and hands focused jobs to sub-agents with clean windows. Each may use tens of thousands of tokens exploring, but returns only a condensed summary, often one to two thousand tokens.",
      "B07_SubAgents", "The main tray holds a plan page; three small crates slide out from it; each fills with many small blocks; then each sends back one summary card to the main tray.",
      [{"at": 0.15, "event": "three crates go out"}, {"at": 0.45, "event": "each fills"}, {"at": 0.75, "event": "one summary card back each"}]),
 beat("B08", "Whichever you use, the rule is the same. Context is a budget. Spend it on the smallest set of high-signal tokens that gets the next step right.",
      "B08_Rule", "The tray with three dotted blocks sits centre stage; the press, the notebook and a small crate arrive around it; a terracotta check lands on the tray.",
      [{"at": 0.2, "event": "the three tools around the tray"}, {"at": 0.5, "event": "context is a budget"}, {"at": 0.85, "event": "check"}]),
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
    "Ciao. This is Liam, in for Bear. When an agent loses the thread, the instinct is to give it more. So don't ask how to give your agent more context. Ask how to give it the right context.",
    "BrutalistHesitantWriter",
    {"text": "How do I give my agent\nmore context?", "triggerWords": "more context", "replacementWords": "the right context",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I give my agent more context?'"}, {"at": 0.6, "event": "backspaces 'more context' -> 'the right context' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (more context) and corrects it to the real one (the right context).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. The context window: everything the model sees at once, from instructions and tools to history and data. Context rot: as that window fills, the model recalls what's in it less accurately. And context engineering: choosing what goes in, every time the model is called.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "context window", "meaning": "everything the model sees at once: instructions, tools, history, data"},
               {"term": "context rot", "meaning": "as the window fills, the model recalls what's in it less accurately"},
               {"term": "context engineering", "meaning": "choosing what goes in, every time the model is called"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'context window' lands"}, {"at": 0.45, "event": "'context rot' lands"}, {"at": 0.78, "event": "'context engineering' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here's a long task I run with an AI agent: [describe it in two sentences]. List everything that lands in its context. "
             "Mark each item: keep, load only when needed, compact, move to a notes file, or hand to a sub-agent. "
             "Then write the summary you'd keep if the context reset right now.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. For each item you kept, "
    "does the next step use it? If not, cut it. And paste only the summary into a fresh chat. Can Claude say what's done and what's next?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Audit One Agent's Context", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: for each item you kept, does the next step use it? If not, cut it.",
                "Check: paste only the summary into a fresh chat. Can Claude say what's done and what's next?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn tray scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · CONTEXT ENGINEERING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude users and agent builders who run long tasks and want to manage what goes into the context window",
    "source_doc": "Anthropic Engineering, 'Effective context engineering for AI agents' (Sep 29, 2025); saved page anthropics/youtube/Effective context engineering for AI agents _ Anthropic.html, read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["context engineering", "context window", "context rot", "attention budget", "compaction", "agentic memory",
             "sub-agents", "just-in-time retrieval", "AI agents", "Claude Code", "Anthropic", "Claude", "Nik Bear Brown"]},
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
