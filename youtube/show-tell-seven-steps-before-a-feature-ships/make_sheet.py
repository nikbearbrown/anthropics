#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-seven-steps-before-a-feature-ships.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #19 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-plugins-official/plugins/feature-dev/ (README.md, commands/feature-dev.md,
agents/code-explorer.md, agents/code-architect.md, agents/code-reviewer.md, .claude-plugin/plugin.json),
all read in full, and diffed byte-for-byte against the raw live files on GitHub (main, 2026-09-27): identical.
Where the README and the command file differ, the command file (what actually runs) wins; the agent file wins
on the reviewer's confidence floor (README's "75-100" output line vs the agent's "Only report issues with
confidence >= 80").
Cast: a CORRIDOR of seven open kraft rooms (numerals 1-7 beside them) with terracotta stop lamps; the feature
TICKET (a white slip with a terracotta dot); the kraft CLAUDE box (dark slot, dark mouth, terracotta spark);
YOU (a kraft terminal) with your dark signal BOARD (grey lamp = Claude waits for you, terracotta = you said go);
AGENTS as small copies of the Claude box; FILES as white cards with grey lines; QUESTIONS as white slips with
kraft number seals and your kraft ANSWER cards with the same seals; three kraft BLUEPRINT sheets; the FEATURE
as a kraft box that closes with terracotta tape; a white TO-DO card with ink checks; a white SUMMARY card.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Seven Steps Before a Feature Ships"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Type slash feature dev, then the feature in plain words. The command walks it through seven phases, in order, and several of them stop and wait for you.",
      "B00_Corridor", "The feature ticket (a white slip with a terracotta dot) sits top left ('/feature-dev'); seven open kraft rooms drop into a row with ink numerals 1-7 under them; the ticket hops over the rooms from 1 to 7 in order; terracotta stop lamps light over rooms 1, 3, 4, 5 and 6 ('waits for you').",
      [{"at": 0.1, "event": "the ticket, '/feature-dev'"}, {"at": 0.35, "event": "seven rooms, 1 to 7"}, {"at": 0.55, "event": "the ticket hops through them in order"}, {"at": 0.85, "event": "stop lamps: waits for you"}]),
 beat("B01", "Phase one, discovery. If the request is unclear, Claude asks what problem it solves, what it should do, and any constraints. Then it sums up what it understood, and checks with you.",
      "B01_Discover", "The corridor clears; the Claude box at the right ('Claude'), you (a kraft terminal) at the left ('you') with your signal board, lamp grey; the ticket drops into Claude's slot; three white question slips ride from Claude's mouth to you; a white summary card comes out between you; your lamp turns terracotta and an ink check lands on the card ('discovery').",
      [{"at": 0.1, "event": "the ticket goes in"}, {"at": 0.35, "event": "three questions ride to you"}, {"at": 0.75, "event": "the summary; your lamp lights; a check"}]),
 beat("B02", "Phase two, exploration. Two or three code explorer agents go out in parallel, each tracing a different part of the codebase. Each brings back a list of five to ten key files, and Claude reads them all.",
      "B02_Explore", "Claude moves left; a grid of white file cards at the right ('codebase'); three small copies of the Claude box ride out of Claude's mouth in parallel ('code-explorer'), one per row; a terracotta beam sweeps each row; each agent comes back with a file card; the cards stack beside Claude ('key files') and slide into its slot.",
      [{"at": 0.1, "event": "the codebase"}, {"at": 0.3, "event": "three explorers go out in parallel"}, {"at": 0.6, "event": "each returns with files"}, {"at": 0.85, "event": "Claude reads them"}]),
 beat("B03", "Phase three, clarifying questions. The command calls it critical: do not skip. Claude lists every gap, like edge cases and error handling, and waits for your answers before designing anything.",
      "B03_Questions", "Claude top left, you and your board bottom left; four white question slips with kraft seals 1-4 slide out of Claude into a row ('questions'); slips 1 and 2 pulse; your lamp stays grey and pulses (Claude waits); four kraft answer cards with the same seals ride from your terminal into the row below ('your answers'); your lamp turns terracotta.",
      [{"at": 0.1, "event": "four questions in a row"}, {"at": 0.45, "event": "edge cases, error handling"}, {"at": 0.65, "event": "Claude waits for you"}, {"at": 0.85, "event": "your answers; the lamp lights"}]),
 beat("B04", "Phase four, architecture. Two or three code architect agents each draw one blueprint: minimal changes, clean architecture, or a pragmatic balance. Claude recommends one, says why, and asks which you prefer.",
      "B04_Design", "Three small architect agents drop in a row; a kraft blueprint sheet with grey layout blocks slides out under each ('minimal', 'clean', 'pragmatic'); a terracotta dot lands on one (recommended); your cursor clicks it; it lifts and the other two fade back.",
      [{"at": 0.1, "event": "three architects"}, {"at": 0.35, "event": "three blueprints, one approach each"}, {"at": 0.7, "event": "the recommended one"}, {"at": 0.85, "event": "you pick; it lifts"}]),
 beat("B05", "Phase five, the build, and it doesn't start until you approve. Claude follows the blueprint you chose, sticks to the codebase's conventions, and ticks off its to-do list as it goes.",
      "B05_Build", "Your board's lamp is grey beside the chosen blueprint; it turns terracotta ('your go'); an open kraft box (the feature) appears; file cards drop into it one by one while ink checks land on a white to-do card ('to-dos'); the box closes and terracotta tape lands on it.",
      [{"at": 0.1, "event": "your lamp lights: go"}, {"at": 0.4, "event": "files drop into the feature"}, {"at": 0.6, "event": "to-dos tick off"}, {"at": 0.85, "event": "the box is taped"}]),
 beat("B06", "Phase six, quality review. Three code reviewer agents check the new code in parallel: for simplicity, for bugs, and for the project's conventions. Each rates its confidence in every issue from zero to a hundred, and reports only those at eighty or above. Then you choose: fix now, fix later, or proceed as is.",
      "B06_Review", "The taped feature box at the centre; three small reviewer agents above it ('code-reviewer'); terracotta scan lines sweep the box; five finding slips pop out, each with a grey score bar; a threshold line ('≥ 80'); the short-bar slips fade; your board's lamp lights and one finding goes back into the box.",
      [{"at": 0.1, "event": "three reviewers in parallel"}, {"at": 0.3, "event": "scan lines sweep"}, {"at": 0.5, "event": "findings with scores"}, {"at": 0.7, "event": "only 80 and above stay"}, {"at": 0.9, "event": "you choose"}]),
 beat("B07", "Phase seven, the summary. Claude marks every to-do done, then writes up what was built, the key decisions, the files it changed, and suggested next steps.",
      "B07_Summary", "The feature box at the left; the to-do card gets its last check; a white summary card slides out beside it ('summary') with four grey lines, and an ink check lands on each line in turn.",
      [{"at": 0.1, "event": "every to-do done"}, {"at": 0.35, "event": "the summary card"}, {"at": 0.5, "event": "four lines tick, one by one"}]),
 beat("B08", "The plugin's read me says it's for features that touch several files or need an architecture decision. Not for one-line bug fixes, trivial changes, or urgent hotfixes.",
      "B08_When", "The corridor of seven rooms returns across the top; a big feature (the ticket with three file cards) rides into room 1 ('several files'); below, a single small slip ('one-line fix') rides straight past, under the corridor.",
      [{"at": 0.1, "event": "the corridor returns"}, {"at": 0.3, "event": "a multi-file feature goes in"}, {"at": 0.7, "event": "a one-line fix skips it"}]),
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
    "Ciao. This is Liam, in for Bear. Ask Claude Code to build a new feature, and it may start coding straight away. The feature dev plugin slows it down first. So the real question isn't how to get the feature coded faster. It's how to make Claude understand it before building.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nget this feature coded faster?", "triggerWords": "get this feature coded faster", "replacementWords": "make Claude understand it before building",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get this feature coded faster?'"}, {"at": 0.6, "event": "backspaces 'get this feature coded faster' -> 'make Claude understand it before building' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I get this feature coded faster) and corrects it to the real one (how do I make Claude understand it before building).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Slash feature dev: the plugin's one command. An agent: a helper Claude sends off on one job, which reports back. And a blueprint: an architect agent's plan, naming the files to create or change.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "/feature-dev", "meaning": "the plugin's one command"},
               {"term": "agent", "meaning": "a helper Claude sends off on one job; it reports back"},
               {"term": "blueprint", "meaning": "an architect's plan: the files to create or change"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'/feature-dev' lands"}, {"at": 0.4, "event": "'agent' lands"}, {"at": 0.75, "event": "'blueprint' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("/feature-dev Add a --dry-run flag to this repo's main script that prints what it would change without "
             "changing anything. Run discovery, exploration and your clarifying questions, then stop and wait for my "
             "answers. Don't design or write any code yet.")
SPOKEN_PROMPT = ("Slash feature dev. Add a dash dash dry run flag to this repo's main script that prints what it would change, "
                 "without changing anything. Run discovery, exploration and your clarifying questions, then stop and wait for my "
                 "answers. Don't design or write any code yet.")
CHECKS = ["Check: do the questions cite files it read?",
          "Check: git status shows no changes yet?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Install the feature dev plugin, open Claude Code in a repo you know, and paste this: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Do its questions point at files it actually read? And does git status show that nothing has changed yet?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn corridor-Claude-and-agents scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B05"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.60-0.79 throughout; B00 (0.54), B04 (0.42 at 99%), B06 (0.46), B07 (0.25 at 25%) and B08 (0.46) keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · FEATURE-DEV PLUGIN", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who use Claude Code on real codebases and want it to understand, ask and design before it builds",
    "source_doc": "anthropics/claude-plugins-official/plugins/feature-dev/ (README.md, commands/feature-dev.md, agents/code-explorer.md, code-architect.md, code-reviewer.md; read in full 2026-09-27, identical to the raw live files on GitHub main)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "feature-dev", "plugin", "slash command", "subagents", "code-explorer", "code-architect",
             "code-reviewer", "clarifying questions", "software design", "code review", "Anthropic", "Nik Bear Brown"]},
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
