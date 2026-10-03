#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-one-tool-that-finds-the-rest.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #20 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Sources: anthropics/claude-cookbooks/tool_use/tool_search_with_embeddings.ipynb (every cell and saved output read in
full 2026-09-27) and the RAW live docs page
https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md (curl, 2026-09-27, saved as
sources/live_tool-search-tool-2026-09-27.md). The live docs win: the API offers a BUILT-IN server-side tool search
(regex and BM25 variants); the notebook builds the CUSTOM client-side route (embeddings) that the docs also support.
The notebook's loop sends every tool without `defer_loading`, and its saved runs call get_weather without ever
searching, so the film follows the live docs for how deferral works and never says the notebook's runs searched.
Numbers: "~100 tools" (notebook cell 0, attributed aloud and on screen). "90%+" is LEFT OUT (its only stated basis,
"19+ tool definitions", contradicts the notebook's own 8-tool library, and nothing in the notebook measures it).
The live docs' "10 or more tools" and "3-5 most used tools non-deferred" are attributed to the docs aloud.
Cast (no filing cabinet, no drawers — that is "How a Skill Loads"): CLAUDE, a kraft block with a terracotta spark on
a dark plinth (left); the CONTEXT TRAY, a low kraft open box on a dark plinth in front of Claude; the TOOL WALL, a
dark pegboard of white tool cards (right); TOOL_SEARCH, a small kraft block with a dark lens and a terracotta light;
the MEANING MAP, a pale kraft plane on a dark plinth with ink dots; a white query slip; white name tags.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Carry One Tool That Finds the Rest"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Say your app has hundreds of tools. Each has a definition: its name, what it does, and its inputs. Normally, every definition goes into Claude's context, on every request.",
      "B00_Wall", "Claude (a kraft block with a terracotta spark on a dark plinth) drops in at the left with its context tray, a low kraft open box ('Claude'); at the right a dark pegboard rises and fills with white tool cards row by row ('tools'); one card slides out and swells, and three grey bars draw on it (name, what it does, inputs) ('definition').",
      [{"at": 0.1, "event": "Claude and the context tray"}, {"at": 0.3, "event": "a wall of tool cards"}, {"at": 0.6, "event": "one definition: name, description, inputs"}]),
 beat("B01", "The context fills before work begins. Anthropic's cookbook says that past about a hundred tools, this becomes impractical: more cost, more time, and the right tool is harder to find.",
      "B01_Overflow", "Card after card flies from the wall into the tray and a white pile grows past the tray's rim ('context'); the hero number lands above ('~100 tools', 'per Anthropic's cookbook').",
      [{"at": 0.15, "event": "every card goes into the tray"}, {"at": 0.4, "event": "the pile overflows"}, {"at": 0.7, "event": "~100 tools, per Anthropic's cookbook"}]),
 beat("B02", "So Claude carries one tool instead: tool search. You still send every definition, but mark the rest defer loading. They stay out of Claude's context until a search finds them.",
      "B02_OneTool", "The pile sinks out of the tray; one small kraft block with a dark lens and a terracotta light drops into the empty tray ('tool_search'); the wall's cards fade to ghost one row at a time ('deferred').",
      [{"at": 0.1, "event": "the tray empties; one tool lands"}, {"at": 0.5, "event": "the rest are marked deferred"}, {"at": 0.85, "event": "they wait outside the context"}]),
 beat("B03", "The cookbook searches by meaning. Each definition becomes text, and a small embedding model turns it into three hundred eighty-four numbers: a point on a map. Similar tools land close together.",
      "B03_Map", "The wall shrinks to the top right; a pale kraft map plane on a dark plinth draws in below it ('map'); card after card drops from the wall onto the map and becomes an ink dot; the dots gather in clusters ('weather', 'finance').",
      [{"at": 0.1, "event": "the map"}, {"at": 0.45, "event": "each definition becomes a point"}, {"at": 0.85, "event": "similar tools land together"}]),
 beat("B04", "Claude calls tool search in plain words, like the cookbook's test: I need to check the weather. The query lands on the same map, and the closest points come back: get weather, get forecast, air quality.",
      "B04_Query", "A white query slip arcs from Claude down onto the map ('query') and becomes a terracotta dot inside the weather cluster; grey spokes draw from it to the three closest dots, which swell (three of the four weather dots; the fourth stays small) ('closest 3').",
      [{"at": 0.1, "event": "Claude sends a plain-words query"}, {"at": 0.55, "event": "it lands on the map"}, {"at": 0.8, "event": "the three closest points win"}]),
 beat("B05", "Your code sends back just their names. The API swaps each name for its full definition, and Claude calls get weather like any other tool. Tools it didn't find never entered its context.",
      "B05_Found", "Three white name tags rise from the three winning dots and arc into the tray ('names'); in the tray each tag grows into a full white card beside tool_search ('definitions'); the first card gets an ink check; the ghost wall stays outside.",
      [{"at": 0.1, "event": "names only come back"}, {"at": 0.45, "event": "the API expands them into full cards"}, {"at": 0.75, "event": "Claude calls get_weather"}]),
 beat("B06", "You don't have to build the search yourself. The live docs offer a built-in tool search on Anthropic's side: one version matches patterns, one takes plain queries. The cookbook adds search by meaning.",
      "B06_BuiltIn", "The map and cards clear; beside the kraft tool_search block, a dark block with two terracotta lights drops onto the tray ('built-in'); the kraft block gets a small map face ('custom'); from each, one card flies back from the wall to the tray.",
      [{"at": 0.2, "event": "the built-in search, two versions"}, {"at": 0.7, "event": "the custom one searches by meaning"}]),
 beat("B07", "The docs suggest tool search from ten tools up. With fewer, or when every tool is used on every request, just load them. And keep your three to five most used tools loaded, ready without a search.",
      "B07_When", "A short row of four cards slides into the tray and fits, and an ink check lands ('10+ tools' sits over the wall as the threshold); the four leave, and three favourite cards settle in the tray beside tool_search for good ('always loaded'); the ghost wall stays deferred.",
      [{"at": 0.15, "event": "ten tools and up"}, {"at": 0.45, "event": "fewer: just load them"}, {"at": 0.8, "event": "keep three to five loaded"}]),
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
    "Konnichiwa. This is Liam, in for Bear. With hundreds of tools, it's tempting to ask how to fit them all into Claude's context. But each one costs room before any work starts. So the real question is how to let Claude find the tools it needs.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nfit every tool into the context?", "triggerWords": "fit every tool into the context", "replacementWords": "let Claude find the tools it needs",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I fit every tool into the context?'"}, {"at": 0.6, "event": "backspaces 'fit every tool into the context' -> 'let Claude find the tools it needs' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I fit every tool into the context) and corrects it to the real one (how do I let Claude find the tools it needs).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A tool: a function Claude can ask your app to run. A definition: its name, what it does, and its inputs. Context: everything Claude reads, counted in tokens. And an embedding: numbers that place text by its meaning.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "tool", "meaning": "a function Claude can ask your app to run"},
               {"term": "definition", "meaning": "a tool's name, what it does, and its inputs"},
               {"term": "context", "meaning": "everything Claude reads, counted in tokens"},
               {"term": "embedding", "meaning": "numbers that place text by its meaning"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'tool' lands"}, {"at": 0.3, "event": "'definition' lands"}, {"at": 0.55, "event": "'context' lands"}, {"at": 0.8, "event": "'embedding' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Read the live docs for the tool search tool. Then write a Python script with twenty mock tools, including "
             "get_weather, all set to defer loading, plus a custom tool_search that ranks them by embeddings. Ask about the "
             "weather in Tokyo and print each tool Claude calls, in order, with each call's input tokens. Then rerun it "
             "with all twenty loaded.")
SPOKEN_PROMPT = YT_PROMPT.replace("get_weather", "get weather").replace("tool_search", "tool search")
CHECKS = ["Check: tool_search called before get_weather?",
          "Check: fewer input tokens on the first call?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In Claude Code, paste this. " + SPOKEN_PROMPT +
    " Then check: did Claude call tool search before get weather? And did the first call use fewer input tokens than with all twenty loaded?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (Claude and its context tray, a wall of tool cards, the "
                 "tool_search block, a map of meaning) on a cream stage per beat, minimal labels, with the voice carrying the "
                 "explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, "
                 "empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): every body beat measures 0.71-0.82 fill, so none carries the sparse waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE COOKBOOK · TOOL SEARCH", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Japanese (Konnichiwa)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers building agents on the Claude API with large tool libraries, who want to know why loading every tool definition hurts and how tool search (built-in, or a custom embedding search like the cookbook's) loads only the tools Claude needs",
    "source_doc": "anthropics/claude-cookbooks/tool_use/tool_search_with_embeddings.ipynb (every cell and output read in full 2026-09-27), checked against the raw live docs page platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md (sources/live_tool-search-tool-2026-09-27.md)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude API", "tool search", "tool use", "defer_loading", "embeddings", "semantic search",
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
