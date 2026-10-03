#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-claude-asks-your-code-runs.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #10 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/courses/tool_use/01_tool_use_overview.ipynb ("How tool use works", steps 0-4) and
04_complete_workflow.ipynb (tool_use / tool_result blocks, the id match, the system-prompt fix), read in full;
current behaviour confirmed on platform.claude.com/docs (tool-use overview; parallel tool use).
Caution (SHOW-TELL-BATCH.md, Batch 2, #10): the notebook's line that Claude "does not have access to any
built-in server-side tools" is out of date; the film doesn't repeat it, and B08 says what the docs say now.
Cast: Claude as a dark BLOCK on a kraft DESK (a light on its top face); your code as a dark MACHINE (the kit's
server stack) at the far end of a pale BELT; TOOL CARDS (white cards with a dark name bar, grey description
lines and an outlined input field); request and result SLIPS lying on the belt (white; the terracotta dot is
the id); an ANSWER card with an ink check; a SYSTEM PROMPT note; Anthropic's own grey machine behind the desk.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Claude Asks, Your Code Runs"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's Claude, at a desk. At the far end is your code, a machine that does real work, like looking up a stock price. Tool use, also called function calling, connects the two.",
      "B00_Desk", "A pale belt draws in; a kraft desk with a dark block on it lands at the near end ('Claude'); a dark machine stack rises at the far end ('your code'); the belt's centre line draws between them and Claude's light turns terracotta.",
      [{"at": 0.1, "event": "Claude at a desk"}, {"at": 0.35, "event": "your code: a machine"}, {"at": 0.75, "event": "tool use connects the two"}]),
 beat("B01", "First, you send a question and a stack of tool cards. Each card has a name, a description, and an input schema: the form its inputs must fill. Claude sees the cards. The code stays with you.",
      "B01_Cards", "A question card slides onto the desk ('question'); three tool cards fan in above it ('tools'); one card grows large: its dark name bar, grey description lines, and an outlined input field ('input schema'); the machine's lights pulse at the far end (the code stays with you).",
      [{"at": 0.1, "event": "a question"}, {"at": 0.3, "event": "tool cards"}, {"at": 0.55, "event": "name, description, input schema"}, {"at": 0.85, "event": "the code stays with you"}]),
 beat("B02", "Claude reads the question and decides a tool would help. So it writes a request slip, a tool use block: which tool, and what input. Then it stops. The stop reason says tool use.",
      "B02_Ask", "Claude's light flashes; a white slip with a terracotta dot appears on the desk and a copy slides onto the belt ('tool_use'); Claude's light goes out; an ink square and 'stop_reason: tool_use' appear at the upper left.",
      [{"at": 0.12, "event": "Claude decides"}, {"at": 0.4, "event": "a request slip"}, {"at": 0.7, "event": "it stops"}, {"at": 0.88, "event": "stop_reason: tool_use"}]),
 beat("B03", "Now your code reads the slip, takes out the tool's name and input, and runs the real function. Claude doesn't run it. Your code does.",
      "B03_Run", "The slip rides down the belt into the machine; the machine's lights come on one by one, terracotta ('runs'); Claude's block stays dark and still.",
      [{"at": 0.15, "event": "your code reads the slip"}, {"at": 0.5, "event": "runs the function"}, {"at": 0.8, "event": "Claude doesn't run it"}]),
 beat("B04", "Your code sends the output back as a tool result, in a new user message. It carries the ID of the request it answers, so Claude can match them up.",
      "B04_Result", "A result slip (darker lines, a terracotta dot) comes out of the machine and rides back to the belt's start, beside the request kept on the desk; a close-up of the two slips grows in the lower right ('tool_use', 'tool_result') and a dashed ink line ties their dots ('id').",
      [{"at": 0.12, "event": "a result slip"}, {"at": 0.45, "event": "back to Claude"}, {"at": 0.75, "event": "the id matches"}]),
 beat("B05", "Now Claude has what it was missing, and writes the answer. Ask, stop, run, return, answer. That's the whole loop.",
      "B05_Answer", "Claude's light turns terracotta; an answer card rises from the desk ('answer') and an ink check lands on it; an ink loop draws out along the belt to the machine and back.",
      [{"at": 0.15, "event": "Claude writes the answer"}, {"at": 0.55, "event": "ask, stop, run, return, answer"}, {"at": 0.85, "event": "the whole loop"}]),
 beat("B06", "Some questions need two lookups. Claude can ask for both in one response. Your code runs both, and sends both results back in one message, each with its ID.",
      "B06_Two", "A second machine rises in front of the belt; two request slips appear on the desk and copies slide onto the belt ('two calls'); one rides to each machine and both run; two result slips come back together on one kraft tray ('one message'), each dot tied to its request.",
      [{"at": 0.12, "event": "two lookups"}, {"at": 0.35, "event": "both in one response"}, {"at": 0.6, "event": "your code runs both"}, {"at": 0.85, "event": "back in one message, each with its id"}]),
 beat("B07", "Claude doesn't have to ask. If it already knows the answer, it can just reply. And a line in your system prompt, like only call the tool when needed, steers how often it asks.",
      "B07_Skip", "A question card lands on the desk; Claude's light turns terracotta and an answer card rises straight away ('answer'); the belt stays empty and the machine stays dark; a system prompt note slides in beside the desk ('system prompt') and a line gains a terracotta dot.",
      [{"at": 0.15, "event": "no tool needed"}, {"at": 0.45, "event": "it just replies"}, {"at": 0.75, "event": "the system prompt steers"}]),
 beat("B08", "Anthropic also runs a few tools itself, on its own servers, like web search and code execution. Those come back without your code. But every tool you define, your code runs.",
      "B08_Server", "A grey machine rises in front of the belt, near the desk ('Anthropic'); a slip arcs to it and a result arcs straight back, never touching the belt; then a tool card rides to your machine, its lights come on, and an ink check lands under 'your code'.",
      [{"at": 0.15, "event": "Anthropic's own machine"}, {"at": 0.5, "event": "comes back without your code"}, {"at": 0.8, "event": "every tool you define, your code runs"}]),
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
    "Hallo. This is Liam, in for Bear. Give Claude a tool through the API, and it's easy to think Claude runs it. For the tools you write, it doesn't. So the real question is how Claude asks your code to run them.",
    "BrutalistHesitantWriter",
    {"text": "How does Claude\nrun my tools?", "triggerWords": "run my tools", "replacementWords": "ask my code to run them",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How does Claude run my tools?'"}, {"at": 0.6, "event": "backspaces 'run my tools' -> 'ask my code to run them' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how does Claude run my tools) and corrects it to the real one (how does Claude ask my code to run them).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A tool: a function you describe to Claude, with a name, a description, and its inputs. A tool use block: Claude's request to call one. And a tool result: your reply, with what the tool returned.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "tool", "meaning": "a function you describe: a name, a description, its inputs"},
               {"term": "tool_use", "meaning": "Claude's request to call one tool, with its input"},
               {"term": "tool_result", "meaning": "your reply: what the tool returned, matched by ID"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'tool' lands"}, {"at": 0.45, "event": "'tool_use' lands"}, {"at": 0.72, "event": "'tool_result' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Write a short Python script that gives Claude one tool, get_weather, with a name, a description and an "
             "input schema, and asks for the weather in Boston. When the response stops for tool_use, print the request, "
             "run a fake weather function, send a tool_result back with the matching ID, and print Claude's answer.")
SPOKEN_PROMPT = (YT_PROMPT.replace("get_weather", "get weather").replace("tool_use", "tool use")
                 .replace("tool_result", "tool result"))
CHECKS = ["Check: the first stop_reason is tool_use?",
          "Check: tool_use_id matches the request's id?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + SPOKEN_PROMPT + " Then run it, and check two things yourself. Does the "
    "first response stop for tool use? And does your result's ID match the request's?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Claude Asks, Your Code Runs", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn desk-belt-machine scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {f"B0{i}" for i in range(9)}   # all nine measured at 0.82-0.85 fill with no Gate V defect (local pre-check, 2026-09-27): no waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · TOOL USE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers and students calling the Claude API for the first time, who want to know who actually runs a tool",
    "source_doc": "anthropics/courses/tool_use/01_tool_use_overview.ipynb and 04_complete_workflow.ipynb (read in full 2026-09-27); platform.claude.com/docs tool-use overview and parallel tool use (fetched 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude API", "tool use", "function calling", "tool_use", "tool_result", "stop_reason", "input schema",
             "parallel tool use", "server tools", "Anthropic courses", "agents", "Anthropic", "Claude", "Nik Bear Brown"]},
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
