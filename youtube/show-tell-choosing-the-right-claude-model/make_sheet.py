#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-choosing-the-right-claude-model.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Bear's order, 2026-09-27: six screenshots
for "a choosing the right model for Claude video. These are just inspiration. Use the Showtell
skill." (transcribed in SOURCE-SCREENSHOTS.md; PNGs in source/).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Sources: SOURCE-SCREENSHOTS.md, attributed aloud as "Anthropic's guide" (the screenshots carry no
URL or date), and, attributed as "Anthropic's developer docs", the live choosing-a-model page
fetched raw on 2026-09-27 (sources/live_2026-09-27_docs_choosing_a_model.md).
The one idea: there is no single best Claude model. You match the model to the job, and you
make that call, one task at a time.
Cast (one small cast, whole film): YOU (a grey figure, left); FOUR kraft FILE FOLDERS standing in
a row (Haiku, Sonnet, Opus, Fable), told apart by their names beneath them and by their staggered
tabs, never by colour; TASK SLIPS that get filed; ONE terracotta spark that sits on the tab of the
folder being chosen and travels from folder to folder; plus, per beat, the thing the task comes
from (a long email, a study, a rough idea that becomes a chain of steps) and the pointer.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Choosing the Right Claude Model"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Picture one best model, and every job goes to the same place. The quick question. The everyday draft. The hard problem. That's the picture the guide replaces.",
      "B00_OneBest", "A grey figure ('you') at the left and one kraft file folder standing alone at the centre ('best?'); three task slips appear by the figure and fly one after another into the one folder as each job is named.",
      [{"at": 0.1, "event": "you and one folder"}, {"at": 0.3, "event": "the quick question goes in"}, {"at": 0.55, "event": "the draft and the hard problem go in"}, {"at": 0.85, "event": "the picture to replace"}]),
 beat("B01", "Instead, it sorts four models by the kind of work they're for. Haiku, for instant answers. Sonnet, for everyday work. Opus, for specialized, complex tasks. And Fable, for your hardest work.",
      "B01_FourFolders", "The one folder slides to the right end of a row; its 'best?' label goes; three more folders slide in to its left, each with its tab one step further along, and each name lands beneath its folder as it is spoken ('Haiku', 'Sonnet', 'Opus', 'Fable').",
      [{"at": 0.15, "event": "the folder moves over; four slots"}, {"at": 0.35, "event": "Haiku"}, {"at": 0.5, "event": "Sonnet"}, {"at": 0.7, "event": "Opus"}, {"at": 0.9, "event": "Fable"}]),
 beat("B02", "Haiku is the guide's most efficient model, for small, routine requests. Straightforward questions, simple summaries, quick lookups, pulling specific info out of text. Say you need one date from a long email. That's a Haiku job.",
      "B02_Haiku", "A long email page appears above the figure ('email'); a small slip lifts off it ('one date') and is filed into the Haiku folder; the terracotta spark lands on Haiku's tab.",
      [{"at": 0.2, "event": "Haiku's tab"}, {"at": 0.55, "event": "the long email"}, {"at": 0.75, "event": "one date lifts off"}, {"at": 0.9, "event": "filed under Haiku"}]),
 beat("B03", "Sonnet, the guide says, is the versatile collaborator that can handle most problems. Writing and creating content, coding tasks, analysis and research, multi-step problems. Drafting a blog post. Fixing an ordinary bug. Sorting through survey answers.",
      "B03_Sonnet", "The spark moves from Haiku's tab to Sonnet's; three slips appear in a row above the figure and fly into the Sonnet folder one after another as each job is named.",
      [{"at": 0.15, "event": "the spark moves to Sonnet"}, {"at": 0.55, "event": "three everyday jobs"}, {"at": 0.9, "event": "all filed under Sonnet"}]),
 beat("B04", "When the problem is hard, Opus. The guide calls it the deep reasoning model for difficult problems. Complex research and analysis, long technical documents, methodology critique, agentic coding. Suppose you want the methods of a study picked apart, to see whether its conclusion holds.",
      "B04_Opus", "The spark moves to Opus's tab; a thick study (a stack of pages) appears above the figure ('a study'); a lens slides across it; the study shrinks and is filed into the Opus folder.",
      [{"at": 0.1, "event": "the spark moves to Opus"}, {"at": 0.6, "event": "a study"}, {"at": 0.8, "event": "the lens reads its methods"}, {"at": 0.95, "event": "filed under Opus"}]),
 beat("B05", "And for your hardest work, Fable. The guide calls it the most autonomous model, for work that takes planning, not just reasoning. Long-horizon tasks with many connected steps. Dense source material. Building something from a rough idea.",
      "B05_Fable", "The spark moves to Fable's tab; a rough-idea slip appears ('rough idea'); a chain of five connected step tiles grows out of it ('many steps'); the whole chain gathers and is filed into the Fable folder.",
      [{"at": 0.1, "event": "the spark moves to Fable"}, {"at": 0.5, "event": "planning: a chain of connected steps"}, {"at": 0.85, "event": "a rough idea, filed under Fable"}]),
 beat("B06", "And one line on Fable's card is worth noticing. It's for problems that Opus struggled with. When a hard problem beats Opus, the guide points you one folder along.",
      "B06_Struggled", "A slip rises out of the Opus folder, shakes above it, then crosses one folder along and drops into Fable.",
      [{"at": 0.2, "event": "a slip rises from Opus"}, {"at": 0.5, "event": "it struggles"}, {"at": 0.85, "event": "it moves one folder along, to Fable"}]),
 beat("B07", "So how do you choose? Start from the job, not a leaderboard. Anthropic's developer docs describe two ways in. Start with an efficient model, and upgrade only if you need to. Or start with the strongest one for your task, and move down over time.",
      "B07_StepUpDown", "A slip drops into Haiku, rises and steps up one folder at a time, with an ink arrow pointing up the row ('step up'); then a slip rises out of Opus and steps down to Sonnet, with an arrow pointing back ('step down').",
      [{"at": 0.2, "event": "start from the job"}, {"at": 0.55, "event": "start efficient; upgrade only if you need to"}, {"at": 0.85, "event": "start strong; move down over time"}]),
 beat("B08", "Either way, you make the call, one task at a time. There's no single best model. There's the right one for this job.",
      "B08_YouChoose", "A pointer glides in and clicks one folder's tab, and the spark lands there; a new slip goes from the figure into that folder; the figure is indicated ('you').",
      [{"at": 0.2, "event": "the pointer picks a folder"}, {"at": 0.6, "event": "one task at a time"}, {"at": 0.9, "event": "the right one for this job"}]),
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
    "Bonjour. This is Liam, in for Bear. Which Claude model is the best? It's the natural question. But Anthropic's guide to choosing a model answers a different one. Which model is the right one for this job?",
    "BrutalistHesitantWriter",
    {"text": "Which Claude model\nis the best?", "triggerWords": "the best", "replacementWords": "the right one for this job",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Which Claude model is the best?'"}, {"at": 0.6, "event": "backspaces 'the best' -> 'the right one for this job'"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (which model is the best) and corrects it to the real one (the right one for this job).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. A model: one version of Claude, like Sonnet or Opus. Autonomous: able to carry work forward on its own. And long-horizon: a task with many connected steps, from start to finish.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "model", "meaning": "one version of Claude, like Sonnet"},
               {"term": "autonomous", "meaning": "carries work forward on its own"},
               {"term": "long-horizon", "meaning": "a task with many connected steps"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'model' lands"}, {"at": 0.4, "event": "'autonomous' lands"}, {"at": 0.7, "event": "'long-horizon' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here are three things I need to do this week: [task 1], [task 2], [task 3]. "
             "For each one, which Claude model fits (Haiku, Sonnet, Opus or Fable), and why?")
CHECKS = ["Check: run one on its pick and one step smaller.",
          "Check: small, everyday, deep, or long? You decide."]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude, with your own three tasks: Here are three things I need to do this week: task one, task two, task three. "
    "For each one, which Claude model fits, Haiku, Sonnet, Opus or Fable, and why? "
    "Then check two things yourself. If you can, run one task on the model it picked, and on one step smaller, and compare. "
    "And before you take its answer, ask yourself: was the task small and routine, everyday, deep reasoning, or long and many-step?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE MODELS · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Sonnet", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn you-and-four-folders scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B02", "B03", "B04", "B05", "B06", "B07", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): all four samples >= 55%; B00 and B01 (40-53%) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": "Choosing the Right Claude Model. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE MODELS · WHICH ONE FOR THE JOB", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude users who see several model names and want to know which one to pick for a given job",
    "source_doc": "Anthropic's 'Choosing the right Claude model' guide, six screenshots sent by Bear on 2026-09-27 (SOURCE-SCREENSHOTS.md, source/); the live developer docs page 'Choosing the right model' fetched raw on 2026-09-27 (sources/live_2026-09-27_docs_choosing_a_model.md), attributed as 'Anthropic's developer docs'",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude models", "Haiku", "Sonnet", "Opus", "Fable", "choosing a model", "Anthropic",
             "AI model selection", "agentic AI", "Nik Bear Brown"]},
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
