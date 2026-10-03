#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-let-the-code-make-the-calls.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #18 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Sources: anthropics/claude-cookbooks/tool_use/programmatic_tool_calling_ptc.ipynb (every cell and saved
output read in full 2026-09-27) and the RAW live docs page
https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling.md (curl, 2026-09-27,
saved as sources/live_programmatic-tool-calling-2026-09-27.md; front matter `status: ga`, so the film does not call
it beta, and the notebook's beta header, tool version and model are out of date and not named).
One number on screen: the notebook's own run, 110,473 -> 15,919 total tokens (its table: "85.6%"), attributed.
Left out because the notebook's figures disagree: API-call counts (table 4 vs 4, printout 3, prose "more"), the
line-item count (tool description "20-50+", prose "100+" / "several hundred"), the per-person dollar totals (the two
runs disagree on Alice's total), and latency (35.38 s vs 34.88 s, 1.4%, against the intro's "substantially").
Cast: CLAUDE, a kraft block with a terracotta spark on a dark plinth (left); a kraft CONTEXT gauge beside it that
fills with grey segments; YOUR APP, a dark three-slab server stack (right), one slab per tool, lights turn terracotta;
a white REQUEST slip; a white RESULT ream (a thick block of paper with grey page edges); a kraft SANDBOX, an open box
on a dark plinth (centre); a white SCRIPT page with grey code lines; a small PRINTOUT card; an ANSWER card with a check.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Let the Code Make the Calls"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's cookbook asks Claude which engineers went over their quarterly travel budget. Its three tools run in your app: one lists the team, one fetches expenses, one checks for a custom budget.",
      "B00_Setup", "Claude, a kraft block with a terracotta spark on a dark plinth, drops in at the left ('Claude') with a question card beside it ('?'); at the right a dark server stack rises slab by slab ('your app'), and each slab's light turns terracotta as its tool is named.",
      [{"at": 0.1, "event": "Claude and the question"}, {"at": 0.45, "event": "your app rises"}, {"at": 0.6, "event": "one light per tool"}]),
 beat("B01", "Normally, each tool call is a round trip. Claude asks for a tool, your app runs it, and the whole result comes back into Claude's context, before Claude picks the next step.",
      "B01_RoundTrip", "A kraft context gauge rises beside Claude ('context'); a white request slip arcs over from Claude to the server ('round trip'); the middle slab lights; a thick white result ream arcs back and drops into the gauge, which gains a grey segment.",
      [{"at": 0.15, "event": "the request goes over"}, {"at": 0.45, "event": "your app runs the tool"}, {"at": 0.75, "event": "the whole result lands in the context"}]),
 beat("B02", "The expense tool sends back every line item, with receipt links, approval chains and merchant details. Eight engineers means eight big results, all in Claude's context.",
      "B02_Pile", "A result ream grows large at centre and its grey page edges draw in one by one ('line items'); it shrinks away; eight reams arc from the server into the gauge one after another, and the gauge fills almost to the top ('8 results').",
      [{"at": 0.1, "event": "one result, many line items"}, {"at": 0.55, "event": "eight results"}, {"at": 0.85, "event": "the context gauge is nearly full"}]),
 beat("B03", "Programmatic tool calling moves the calls into code. Turn it on per tool: add Anthropic's code execution tool, and give each tool that code may call a field named allowed callers.",
      "B03_Switch", "The gauge empties; a kraft open box on a dark plinth drops in between Claude and the server ('sandbox'); a dashed ink cable draws from the box to the server; each slab's port turns terracotta in turn ('allowed callers').",
      [{"at": 0.2, "event": "the code execution sandbox"}, {"at": 0.6, "event": "each tool is marked, one by one"}]),
 beat("B04", "Claude writes a short Python script, and it runs in the sandbox, a sealed container Anthropic manages. To the script, each tool is just a function, and it can call several at once.",
      "B04_Script", "A white script page arcs from Claude down into the sandbox ('script'); grey code lines draw on it one by one; three small ink call ticks pop along its edge (several calls at once).",
      [{"at": 0.1, "event": "Claude writes a script"}, {"at": 0.45, "event": "it runs in the sandbox"}, {"at": 0.8, "event": "tools are functions"}]),
 beat("B05", "When the script calls a tool, it pauses. Your app runs the tool and hands the result back to the script, not to Claude. The eight results pile up in the sandbox; Claude's context stays empty.",
      "B05_Calls", "Request slips shuttle from the sandbox to the server; the middle slab lights; result reams come back into the sandbox, not to Claude, and stack up inside the open box ('results'); the context gauge beside Claude stays empty.",
      [{"at": 0.15, "event": "the script pauses on a call"}, {"at": 0.4, "event": "your app runs it"}, {"at": 0.75, "event": "results pile up in the sandbox"}]),
 beat("B06", "Then the code does the sums. It keeps approved travel, totals each person, and prints just the three engineers over five thousand dollars. Only that printout goes back to Claude.",
      "B06_Filter", "A terracotta scan line sweeps down through the sandbox and the reams sink away; a small printout card with three grey lines rises out ('printout'); it arcs to the context gauge, which gains one thin segment.",
      [{"at": 0.1, "event": "the code does the sums"}, {"at": 0.5, "event": "three names printed"}, {"at": 0.85, "event": "only the printout reaches Claude"}]),
 beat("B07", "In the notebook's run, on a made-up API built for big results, the normal way used over a hundred and ten thousand tokens; the script, under sixteen thousand. Eighty-five point six percent fewer, in that one run.",
      "B07_Tokens", "Two grey bars grow side by side, one beside a ream ('110,473') and one beside a printout card ('15,919'); the second bar shrinks; the hero number lands ('85.6%', 'per Anthropic's notebook').",
      [{"at": 0.25, "event": "two token bars"}, {"at": 0.6, "event": "the script bar shrinks"}, {"at": 0.85, "event": "85.6%, per Anthropic's notebook"}]),
 beat("B08", "It pays with many calls and big results. The docs say it gains little when each step needs Claude to think about the last result, or the calls are few and small. Only open it to tools that are safe to run again and again.",
      "B08_Fit", "The sandbox fans dashed lines out to the server's three slabs and an ink check lands beside it ('many calls'); then a single slip crosses from Claude straight to the server and back, and the sandbox fades to ghost ('one at a time'); the server's lights pulse.",
      [{"at": 0.15, "event": "many calls, big results: a check"}, {"at": 0.55, "event": "step by step: little gain"}, {"at": 0.85, "event": "only safe tools"}]),
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
    "Hola. This is Liam, in for Bear. When Claude calls a tool again and again, it's tempting to ask how to make each tool call faster. But the real cost is what comes back: every result passes through Claude. So the real question is how to let the code make the calls.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nmake each tool call faster?", "triggerWords": "make each tool call faster", "replacementWords": "let the code make the calls",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I make each tool call faster?'"}, {"at": 0.6, "event": "backspaces 'make each tool call faster' -> 'let the code make the calls' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I make each tool call faster) and corrects it to the real one (how do I let the code make the calls).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A tool call: Claude asking your app to run a function. A round trip: one pass from Claude to your app and back. Context: everything Claude reads, counted in tokens. And a sandbox: a sealed container where code runs.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "tool call", "meaning": "Claude asking your app to run a function"},
               {"term": "round trip", "meaning": "one pass from Claude to your app and back"},
               {"term": "context", "meaning": "everything Claude reads, counted in tokens"},
               {"term": "sandbox", "meaning": "a sealed container where code runs"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'tool call' lands"}, {"at": 0.3, "event": "'round trip' lands"}, {"at": 0.55, "event": "'context' lands"}, {"at": 0.8, "event": "'sandbox' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Read the live docs for programmatic tool calling, then write a Python script with a mock get_orders tool "
             "that returns long JSON orders. Let code execution call it for ten customers, find who spent over a thousand "
             "dollars, and print each call's caller and the input tokens. Then rerun it with direct calls only.")
SPOKEN_PROMPT = YT_PROMPT.replace("get_orders", "get orders").replace("JSON", "Jason")
CHECKS = ["Check: every get_orders call from code execution?",
          "Check: far fewer input tokens than direct?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In Claude Code, paste this. " + SPOKEN_PROMPT +
    " Then check: does every get orders call come from code execution? And did the script use far fewer input tokens?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (Claude and its context gauge, your app's server stack, a "
                 "code-execution sandbox, request slips and result reams) on a cream stage per beat, minimal labels, with the "
                 "voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; "
                 "edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B04", "B05", "B06", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.63-0.82 throughout; B00 (0.21 before the server rises) and B07 (0.20 before the bars grow) keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE COOKBOOK · PROGRAMMATIC TOOL CALLING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Spanish (Hola)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers building agents on the Claude API whose tools return large results, who want to know why tool-heavy tasks burn tokens and how programmatic tool calling keeps raw results out of Claude's context",
    "source_doc": "anthropics/claude-cookbooks/tool_use/programmatic_tool_calling_ptc.ipynb (every cell and output read in full 2026-09-27), checked against the raw live docs page platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling.md (sources/live_programmatic-tool-calling-2026-09-27.md)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude API", "programmatic tool calling", "tool use", "code execution", "sandbox", "allowed_callers",
             "context window", "tokens", "agents", "claude-cookbooks", "Anthropic", "Nik Bear Brown"]},
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
