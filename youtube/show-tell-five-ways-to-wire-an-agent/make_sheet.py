#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-five-ways-to-wire-an-agent.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #1 in show-tell-ideas.md.
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: Anthropic Engineering, "Building effective agents" (Erik S. and Barry Zhang,
published Dec 19, 2024), saved at anthropics/youtube/Building Effective AI Agents _ Anthropic.html.
One conveyor cast for the whole film: crates (the work), dark stations (LLM calls),
belts (predefined code paths), gates, a switch, a foreman, an inspector; B06 takes the rails away.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Five Ways to Wire an Agent"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Everything starts with one station: a model with a kit. Retrieval to look things up, tools to act, and memory to keep what matters. Every pattern after this is built from stations like this one.",
      "B00_Station", "A dark station sits by a short belt; a crate rides in; three kit pieces (a magnifier, a tool block, a page stack) drop in beside it and cable to it; the station light comes on.",
      [{"at": 0.1, "event": "station + belt"}, {"at": 0.3, "event": "retrieval"}, {"at": 0.45, "event": "tools"}, {"at": 0.6, "event": "memory"}, {"at": 0.8, "event": "crate rides in, light on"}]),
 beat("B01", "Pattern one: prompt chaining. Split the job into fixed steps. Each call works on the output of the one before, and a gate between them checks that it's still on track. Outline, check, then write.",
      "B01_Chain", "Three stations in a row behind one belt with a gate after the first; the crate stops at each station and gains a mark; at the gate a check lands before it passes.",
      [{"at": 0.15, "event": "belt, stations, gate"}, {"at": 0.4, "event": "station 1"}, {"at": 0.6, "event": "gate check"}, {"at": 0.85, "event": "stations 2 and 3"}]),
 beat("B02", "Pattern two: routing. Classify what comes in, then send it down the line built for it. Refunds go one way, tech support another. And easy questions can go to a smaller, cheaper model.",
      "B02_Route", "One belt runs into a track switch that fans out to three lines, each ending at a station (one of them small); the switch lever swings and sends each crate down its own line.",
      [{"at": 0.15, "event": "switch + three lines"}, {"at": 0.45, "event": "refund crate routed"}, {"at": 0.65, "event": "tech crate routed"}, {"at": 0.85, "event": "small crate to the small station"}]),
 beat("B03", "Pattern three: parallelization. Split the belt, run the calls at the same time, and merge the results in code. Sectioning runs different parts of the job side by side. Voting runs the same task several times and compares the answers.",
      "B03_Parallel", "A belt splits into three parallel lanes and merges again. Sectioning: a crate breaks into three different parts that ride the lanes and rejoin. Voting: three identical crates ride, marks appear, the majority merges.",
      [{"at": 0.1, "event": "split and merge belts"}, {"at": 0.45, "event": "sectioning run"}, {"at": 0.75, "event": "voting run"}]),
 beat("B04", "Pattern four: orchestrator-workers. A central model reads the job, decides the subtasks on the spot, hands them to worker models, and pulls their results together. Unlike parallelization, the pieces aren't fixed in advance.",
      "B04_Foreman", "A tall foreman station takes the crate; worker stations pop up only once it decides; crates fly out along drawn paths, workers light, crates fly back and merge into one.",
      [{"at": 0.2, "event": "foreman takes the crate"}, {"at": 0.4, "event": "workers appear"}, {"at": 0.55, "event": "hand-out"}, {"at": 0.75, "event": "collect"}]),
 beat("B05", "Pattern five: evaluator-optimizer. One call makes the work. Another judges it against clear criteria and sends it back with notes, round and round, until it passes.",
      "B05_Inspector", "A maker station and an inspector booth joined by a forward belt and a return belt; the crate is stamped with a cross and rides back, twice, then gets a check and leaves.",
      [{"at": 0.2, "event": "maker, booth, loop"}, {"at": 0.5, "event": "sent back"}, {"at": 0.75, "event": "round and round"}, {"at": 0.9, "event": "passes"}]),
 beat("B06", "Now take the rails away. That's an agent. It plans and picks its own route, one tool call at a time, checking real results, like a test run, at every step. And it gets a stop condition, such as a maximum number of steps.",
      "B06_Agent", "The belt drops out of the frame; tool stations stand loose on the floor; the crate hops between them on a route it draws itself, each landing lights a result; a row of step pips fills toward a stop post.",
      [{"at": 0.1, "event": "rails drop away"}, {"at": 0.35, "event": "crate picks its route"}, {"at": 0.6, "event": "results light"}, {"at": 0.85, "event": "step pips, stop post"}]),
 beat("B07", "So which one should you build? Start with the simplest. Often one good call with retrieval and examples is enough. Every added step costs time and money, so add one only when you can measure that it helps.",
      "B07_Simplest", "A staircase of stations from one call up to an agent; the crate lands on the bottom step; cost stacks grow on the higher steps; a gauge rises past its line before the crate climbs one step.",
      [{"at": 0.15, "event": "staircase"}, {"at": 0.35, "event": "crate on the bottom step"}, {"at": 0.65, "event": "cost stacks"}, {"at": 0.85, "event": "gauge passes, crate climbs"}]),
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
    "Bonjour. This is Liam, in for Bear. Anthropic worked with dozens of teams building agents, and the most successful ones used simple patterns, not complex frameworks. So don't ask for the smartest agent. Ask for the simplest one that works.",
    "BrutalistHesitantWriter",
    {"text": "How do I build\nthe smartest agent?", "triggerWords": "the smartest agent", "replacementWords": "the simplest one that works",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I build the smartest agent?'"}, {"at": 0.6, "event": "backspaces 'the smartest agent?' -> 'the simplest one that works?' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (the smartest agent) and corrects it to the real one (the simplest one that works).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. An augmented LLM: a language model with retrieval, tools, and memory attached. A workflow: models and tools run along paths written in code ahead of time. And an agent: the model directs its own steps and its own tool use.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "augmented LLM", "meaning": "a language model with retrieval, tools, and memory attached"},
               {"term": "workflow", "meaning": "models and tools run along paths written in code ahead of time"},
               {"term": "agent", "meaning": "the model directs its own steps and its own tool use"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'augmented LLM' lands"}, {"at": 0.45, "event": "'workflow' lands"}, {"at": 0.78, "event": "'agent' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here's a task I do every week: [describe it in two sentences]. Using the patterns in Anthropic's "
             "\"Building effective agents\", pick the simplest one that fits, from a single call up to a full agent. "
             "Tell me what a simpler pattern would get wrong, and what I should measure to prove the extra step helps.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. Can you point to a real case "
    "where the simpler version fails? And did you run the simplest version on five real examples first? If it already works, stop there.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Pick the Simplest Pattern", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: point to a real case where the simpler version fails.", "Check: run the simplest version on five real examples first."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn conveyor scene on a cream stage per beat, minimal labels, "
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · AGENTS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "developers and builders deciding how to structure an LLM app or agent",
    "source_doc": "Anthropic Engineering, 'Building effective agents' (Erik S. and Barry Zhang, Dec 19, 2024), saved page anthropics/youtube/Building Effective AI Agents _ Anthropic.html (read 2026-09-26)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["AI agents", "agentic workflows", "prompt chaining", "routing", "parallelization", "orchestrator-workers",
             "evaluator-optimizer", "Building effective agents", "Anthropic", "Claude", "Nik Bear Brown"]},
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
