#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-what-is-claude-code.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Bear's order, 2026-09-27: "use the show-tell
skill in Brutalist to make a film on this using the Liam persona 'What is Claude code?'" + a paste
of the Claude Code product page (saved, cleaned, as SOURCE-PASTE.md).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B13 drawn -> BHTF composer -> BOUT.

Sources: SOURCE-PASTE.md (claude.com/product/claude-code, pasted 2026-09-27) and, attributed as
"the docs", the live overview fetched raw on 2026-09-27 (sources/live_2026-09-27_docs_overview.md).
The one idea: Claude Code is not a smarter autocomplete; it is an agent you hand a whole task to.
It plans, reads, runs, edits and keeps going; YOU direct, steer and review.
Cast (one small cast, whole film): YOU (a grey figure, left), the AGENT (a dark block with a
terracotta spark, 'Claude Code', centre), the CODEBASE (a kraft tray of code pages, right), the TASK
ticket, the TEST LAMP (a post with a lamp), the PR card; plus, for the page's worked example, the PAY
button, the GATEWAY (a dark bank block) and charge slips with their idempotency-key tags.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "What Is Claude Code?"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The product page puts it in one line. Hand Claude a bug fix, a test, or a multi-day migration. Then steer and review. So there are two jobs here. You write the task and hand it over. Claude Code does the work.",
      "B00_Handoff", "A grey figure ('you') at the left, a dark block with a terracotta spark ('Claude Code') at the centre; a white task ticket appears by the figure and slides across into the block, whose spark pulses.",
      [{"at": 0.1, "event": "you and the agent"}, {"at": 0.35, "event": "the task ticket appears"}, {"at": 0.75, "event": "the ticket is handed over"}]),
 beat("B01", "What does doing the work mean? The docs call it an agentic coding tool. It reads your codebase. It edits files. And it runs commands, like your tests. Autocomplete suggests your next line. This takes the steps itself.",
      "B01_Hands", "A kraft tray of code pages ('codebase') slides in at the right; a lens reads a page ('reads'); a new grey line writes onto a page ('edits'); a small dark terminal slab rises and its prompt blinks ('runs').",
      [{"at": 0.15, "event": "the codebase arrives"}, {"at": 0.35, "event": "reads"}, {"at": 0.55, "event": "edits"}, {"at": 0.75, "event": "runs"}]),
 beat("B02", "And it doesn't just start typing. The page says it builds the plan, asks clarifying questions, and handles work that runs for hours or days.",
      "B02_Plan", "The task ticket grows a three-row plan with boxes ('plan'); a question bubble travels from the agent to the figure and an answer bubble comes back; the plan's boxes tick one by one.",
      [{"at": 0.2, "event": "the plan"}, {"at": 0.5, "event": "a question and an answer"}, {"at": 0.8, "event": "the steps tick through"}]),
 beat("B03", "Here's the example the page itself uses, from its product demo. The request reads: we're seeing duplicate charges when customers double click the pay button. Can you find and fix it?",
      "B03_Bug", "A pay button pill rises above the stage ('pay'); a dark gateway block beside it ('gateway'); the cursor clicks the button twice and two charge slips fly into the gateway; two coins drop out.",
      [{"at": 0.15, "event": "pay button and gateway"}, {"at": 0.5, "event": "two clicks"}, {"at": 0.8, "event": "two charges"}]),
 beat("B04", "First, it looks. In the demo, it reads three files and searches the checkout flow. Then it reproduces the bug against a test charge. Two clicks, before the first response lands, fire two charge requests.",
      "B04_Look", "A lens visits three code pages in the tray, a check landing by each ('3 files'); a small test lamp post rises ('test charge'); the agent fires two quick slips at the gateway and the lamp lights.",
      [{"at": 0.15, "event": "reads three files"}, {"at": 0.5, "event": "reproduces against a test charge"}, {"at": 0.8, "event": "two requests fire"}]),
 beat("B05", "Then the root cause. Each charge request carries an idempotency key, so the gateway can spot a repeat. But create charge makes a new key on every call, instead of one per checkout session. Two clicks, two different keys. So the gateway sees two fresh charges.",
      "B05_Cause", "Two charge slips sit before the gateway, each with a key tag; the tags are drawn different (one notch, two notches) ('new key per call'); both slips pass into the gateway and two coins drop.",
      [{"at": 0.2, "event": "the key on each request"}, {"at": 0.5, "event": "a new key per call"}, {"at": 0.8, "event": "two fresh charges"}]),
 beat("B06", "The fix. One key per checkout session, so the second click carries the same key, and the gateway charges once. It also disables the button while a charge is in flight. One file changed: charges dot T S, nine lines added, three removed.",
      "B06_Fix", "Both slips now carry the same key; the first passes, the second bounces back off the gateway; one coin; the pay button turns grey; a diff card rises ('charges.ts', '+9 −3').",
      [{"at": 0.2, "event": "one key per session"}, {"at": 0.45, "event": "the repeat bounces"}, {"at": 0.65, "event": "the button disables"}, {"at": 0.85, "event": "the diff"}]),
 beat("B07", "That same looking around works on a codebase you've never seen. Ask it to explain the project, and it maps the structure and the dependencies. The page calls this agentic search. It finds what to read by itself, so you don't hand pick the files it should see.",
      "B07_Map", "The tray widens into a larger codebase of six pages; a lens hops from page to page and grey lines draw between them, a map forming ('map'); no hand reaches in to pick files ('agentic search').",
      [{"at": 0.2, "event": "a new codebase"}, {"at": 0.5, "event": "the map draws"}, {"at": 0.8, "event": "it picks its own files"}]),
 beat("B08", "It works with GitHub, GitLab, and your command line tools. So one task can run the whole way: read the issue, write the code, run the tests, and open a pull request.",
      "B08_IssueToPR", "The ticket reads as an issue ('issue'); a page edits in the tray; the test lamp lights ('tests'); a kraft pull-request card rises at the right ('pull request').",
      [{"at": 0.2, "event": "the issue"}, {"at": 0.45, "event": "the code"}, {"at": 0.65, "event": "the tests"}, {"at": 0.85, "event": "the pull request"}]),
 beat("B09", "Bigger jobs, like a refactor or a migration, can run for hours. It follows imports from file to file across the repo, runs your tests, and when something breaks, it keeps going. It fixes the failure and runs them again.",
      "B09_LongRun", "A path hops from page to page across the tray ('imports'); the test lamp shows a cross; a page edits; the lamp lights and a check lands ('keeps going').",
      [{"at": 0.2, "event": "follows imports"}, {"at": 0.5, "event": "a test breaks"}, {"at": 0.8, "event": "fixed, green again"}]),
 beat("B10", "Where do you talk to it? The docs list the terminal, your editor, the desktop app, and the web, and they all connect to the same Claude Code engine. The page adds the phone app. And in Slack, you can kick off a task.",
      "B10_Doors", "Six small doors arc above the agent: a terminal, an editor window, a desktop app, a browser, a phone, a chat bubble; a cable draws from each to the block ('terminal', 'editor', 'Slack').",
      [{"at": 0.2, "event": "terminal and editor"}, {"at": 0.45, "event": "desktop and web"}, {"at": 0.75, "event": "phone and Slack"}]),
 beat("B11", "Which leaves your part. You decide what needs doing, you answer its questions, and you review the change before you keep it. Notion's co-founder puts it this way: we decide what needs to happen. Claude Code builds it.",
      "B11_Review", "The doors clear; the diff card travels from the agent back to the figure; the figure's check lands on it ('review'); a quote tag appears under the figure ('per Notion's co-founder').",
      [{"at": 0.2, "event": "you decide"}, {"at": 0.5, "event": "the change comes back to you"}, {"at": 0.8, "event": "you review it"}]),
 beat("B12", "You also choose how much it does without asking. The docs describe manual mode, where it stops and asks you before it edits files or runs commands. And auto mode, where a second model checks each action instead of you. The page says that lets it work longer, while still catching risky commands.",
      "B12_Auto", "Command slabs travel from the agent toward a terminal past a barrier arm. Manual ('manual'): the arm rises, a question mark flies to the figure, the figure answers, the arm drops and the command passes. Auto ('auto mode'): commands pass with no question; a dark risky slab arrives and the arm rises and holds it ('risky').",
      [{"at": 0.15, "event": "manual: it stops and asks you"}, {"at": 0.55, "event": "auto: commands flow, checked by a second model"}, {"at": 0.85, "event": "a risky one is caught"}]),
 beat("B13", "To try it: Claude Code is included in the Claude Pro and Max plans, and it also comes with Team and Enterprise plans, or a Claude Console account. Usage limits apply. On a Mac or on Linux, one line in the terminal installs it. Then type claude in your project.",
      "B13_Start", "Two plan tags drop beside the agent ('Pro', 'Max'); a terminal slab types one grey line ('install'); the agent block settles onto the codebase tray and its spark lights.",
      [{"at": 0.2, "event": "included in Pro and Max"}, {"at": 0.6, "event": "one-line install"}, {"at": 0.85, "event": "claude in your project"}]),
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
    "Ciao. This is Liam, in for Bear. It's easy to picture Claude Code as a smarter autocomplete, a tool that guesses your next line. Its product page describes something else. You hand it a whole task, and it does the work while you steer. So, what is Claude Code? An agent you hand work to.",
    "BrutalistHesitantWriter",
    {"text": "What is Claude Code,\na smarter autocomplete?", "triggerWords": "a smarter autocomplete", "replacementWords": "an agent you hand work to",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'What is Claude Code, a smarter autocomplete?'"}, {"at": 0.6, "event": "backspaces 'a smarter autocomplete' -> 'an agent you hand work to'"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (a smarter autocomplete) and corrects it to the real one (an agent you hand work to).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Four terms. An agent: a program you give a goal, that works through the steps itself. A codebase: all the files of your project. An idempotency key: a tag sent with a request, so a repeat of it counts only once. And a pull request: a proposed change, waiting for a person to review it.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "agent", "meaning": "a program that works through the steps itself"},
               {"term": "codebase", "meaning": "all the files of your project"},
               {"term": "idempotency key", "meaning": "a tag that makes a repeat count once"},
               {"term": "pull request", "meaning": "a proposed change, waiting for review"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'agent' lands"}, {"at": 0.3, "event": "'codebase' lands"}, {"at": 0.5, "event": "'idempotency key' lands"}, {"at": 0.8, "event": "'pull request' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = "I'm new to this codebase. Can you explain it to me? List the files you read."
CHECKS = ["Check: open two files it named. Does it match?",
          "Check: have it run the tests. Read the result yourself."]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Open Claude Code in a repository you know well, and paste this: I'm new to this codebase. Can you explain it to me? List the files you read. "
    "Then check two things yourself. Open two of the files it named. Does its description match what's in them? "
    "And ask it to run the tests, then read the result yourself, not just its summary.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn you-agent-codebase scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B04", "B05", "B06", "B07", "B10", "B12"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.56-0.74 throughout; the rest (0.24-0.49 at some point) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": "What Is Claude Code? At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · WHAT IT IS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who have heard of Claude Code and want to know what it actually is before they try it",
    "source_doc": "claude.com/product/claude-code as pasted by Bear on 2026-09-27 (SOURCE-PASTE.md); the live docs overview fetched raw on 2026-09-27 (sources/live_2026-09-27_docs_overview.md), attributed as 'the docs'",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "agentic coding", "AI agent", "coding agent", "Anthropic", "idempotency key",
             "pull requests", "auto mode", "codebase onboarding", "Nik Bear Brown"]},
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
