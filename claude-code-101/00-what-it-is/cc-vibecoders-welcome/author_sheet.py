#!/usr/bin/env python3
"""
author_sheet.py — cc-vibecoders-welcome  (cc-explainer · Claude Code 101 · tier 00)

Writes beat_sheet.json. Every CCSession block below is copied from SESSION.md —
the headless Claude Code session that actually ran on 2026-09-08 (REAL-SESSION
LAW). Prompt blocks are what Liam typed (TYPES-NOT-NARRATES). Tool names, args
and Claude's own sentences are verbatim; long paths are shortened to the file
name for display, nothing else is altered.

Operator: Liam, in for Bear (Kokoro am_onyx) — first person, present tense, Teardown. LIAM LAW:
Liam narrates every beat, body and closing block (BVDT → BHTF → BOUT — the your-turn ids GATE BOOKEND checks).
Re-narrated 2026-09-08: the first build used an "Ada" operator; Bear ruled "Liam persona ALWAYS".
"""
import json, os

SLUG  = "cc-vibecoders-welcome"
TITLE = "Vibecoders Welcome"
TOPIC = "CLAUDE CODE 101"
LIAM = "am_onyx"
WPS = 2.9

ASK1 = ("I don't write code. Build me a personal reading log as ONE self-contained index.html file: "
        "a form to add a book (title, author, date finished, a 1-5 rating), a list of what I've logged, "
        "saved in localStorage so it survives reload. No frameworks, no build step, no external requests. "
        "Keep it plain and readable.")
ASK2 = ("I read the file before running it. Two things I did not ask for: a remove button on each row, "
        "and sorting the list. Take both out — I want exactly what I asked for and nothing else. "
        "Do not add or change anything else, and don't touch the styling.")

beats = []
def est(t): return round(len(t.split()) / WPS + 0.9, 1)

def B(bid, act, lane, voice, narration, element, shot, show, **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "narration_text": narration,
         "estimated_duration_s": est(narration), "voice": voice, "engine": "kokoro",
         "voice_kokoro": voice, "new_visual_element": element, "shot": shot, "show": show}
    b.update(extra); beats.append(b)

def R(pattern, props, motion="type", **shot_extra):
    s = {"type": "REMOTION", "source": "own", "motion": motion,
         "remotion": {"pattern": pattern, "props": props, "rendered": {"out": "", "at": ""}}}
    s.update(shot_extra); return s


def writer(text, trig, rep, seed):
    return {"text": text, "triggerWords": trig, "replacementWords": rep, "face": "serif", "fontSize": 78,
            "align": "center", "ink": "#F2F0E9", "accent": "#D97757", "bg": "#1F1E1B", "seed": seed,
            "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 5, "jitter": 20}

def session(title, mode, blocks, cues, mascot="auto"):
    return {"title": title, "mode": mode, "blocks": blocks, "cues": cues, "mascot": mascot}

# ── B00 COLD OPEN ─────────────────────────────────────────────────────────────
B("B00", "COLD OPEN", "TERMINAL", LIAM,
  "This is Liam, in for Bear. I don't write code, and I'm about to build something anyway. That's what vibecoding is: "
  "you describe the thing, Claude Code writes it, you decide whether it's right. An empty folder, "
  "one file in it, and one paragraph — every constraint I care about, up front. Watch what it does first.",
  "CCSession — the terminal opens; the real ask types; Claude looks at the folder",
  R("CCSession", session("reading-log", "default", [
      {"type": "prompt", "text": ASK1, "cue": 0, "typeDuration": 150},
      {"type": "status", "verb": "Exploring", "elapsed": "0m 03s", "tokens": "1.4k tokens"},
      {"type": "tool", "name": "Bash", "arg": "pwd && ls -la", "state": "done"},
  ], [0, 170, 210])),
  [{"at": 0.05, "event": "Her paragraph types — five constraints in it"},
   {"at": 0.50, "event": "✳ Exploring…"},
   {"at": 0.62, "event": "Bash pwd && ls -la — it looks before it writes"}])

# ── BIDEA THE IDEA (beat two: the hesitant writer types what this film is about) ──
B("BIDEA", "THE IDEA", "IDEA", LIAM,
  "Here's the idea of this film. Vibecoding means you describe a tool in plain words, Claude Code writes it, and you decide whether it's right — not by trusting it, by reading it. I'll build a reading log I'd actually use, and I'll show you the two things it added that I never asked for, and the one thing it wrote outside my folder.",
  "BrutalistHesitantWriter — the idea of the film, typed; one word reconsidered (trust → check)",
  R("BrutalistHesitantWriter", writer("Vibecoding: you describe, Claude builds,\nyou trust what comes back.\nBefore you run it, read it.", 'trust', 'check', SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at": 0.05, "event": "The writer starts the sentence"},
   {"at": 0.40, "event": "'trust' typed, reconsidered, replaced with 'check'"},
   {"at": 0.80, "event": "The last line lands; caret holds"}])

# ── BDEFS DEFINITIONS (the jargon this film cannot avoid, one plain line each) ──
B("BDEFS", "DEFINITIONS", "CARD", LIAM,
  "Five words before we start. Vibecoding: you describe the tool in plain words, Claude writes the code, you judge it. Local storage: the browser's own small store — the page keeps your data with no server. Tool call: Claude asking for permission to read, write, or run something. Diff: the exact lines removed, in red, and added, in green — nothing else. And git diff stat: the change tracker's one-line answer — which files, how many lines.",
  "CCDefinitions — five terms, one plain line each, landing one at a time",
  R("CCDefinitions", {
      "title": "TERMS IN THIS FILM",
      "terms": [
          {"term": 'vibecoding', "meaning": 'describe the tool in plain words; Claude writes the code; you judge it'},
          {"term": 'localStorage', "meaning": "the browser's own small store — the page keeps your data, no server"},
          {"term": 'tool call', "meaning": 'Claude asking the harness to read, write, or run something for it'},
          {"term": 'diff', "meaning": 'the exact lines removed (red) and added (green), nothing else'},
          {"term": 'git diff --stat', "meaning": "the change tracker's one-line answer: which files, how many lines"},
      ],
      "startCue": 12, "rowGap": 48,
  }, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience: the words the session uses without explaining them"),
  [{"at": 0.05, "event": "Title; first term lands"},
   {"at": 0.50, "event": "Terms land one at a time, meaning after term"},
   {"at": 0.90, "event": "Five rows hold"}])

# ── B01 THE PLAN (what Claude said it would build — a text line, not a plan card) ──
B("B01", "THE PLAN", "TERMINAL", LIAM,
  "Before it writes, it says what it's going to write. Listen to the end of that sentence: "
  "'and a delete option.' I never asked for a delete option. I'm going to let it write anyway — "
  "a two-line fix is cheap — but I've just learned the first rule: it will add things. "
  "So I'll read the file before I run it.",
  "CCSession — Claude's one-line plan, verbatim; the extra is in the sentence",
  R("CCSession", session("reading-log", "default", [
      {"type": "text", "text": "I'll create a single `index.html` with"},
      {"type": "text", "text": "the form, a table of logged books,"},
      {"type": "text", "text": "localStorage persistence,"},
      {"type": "text", "text": "and a delete option."},
      {"type": "text", "text": "Plain HTML/CSS/JS, no dependencies."},
      {"type": "status", "verb": "Writing", "elapsed": "0m 21s", "tokens": "4.8k tokens"},
  ], [0, 18, 36, 54, 72, 130]), motion="drawon"),
  [{"at": 0.05, "event": "Claude's sentence lands"},
   {"at": 0.45, "event": "✳ Writing…"}])

# ── B02 CHANGE ────────────────────────────────────────────────────────────────
B("B02", "CYCLE 1 — CHANGE", "TERMINAL", LIAM,
  "One tool call. Write, index.html, two hundred and eighty-six lines, in one pass. "
  "Then its own summary of what it built — and that summary is fluent, formatted, and confident. "
  "It is also a claim. The file is the artifact. Whether the file does what I asked is a separate question.",
  "CCSession — Write index.html; Claude's summary as it wrote it",
  R("CCSession", session("reading-log", "accept-edits", [
      {"type": "tool", "name": "Write", "arg": "index.html", "state": "done"},
      {"type": "text", "text": "Done. Created `index.html` —"},
      {"type": "text", "text": "a single self-contained file:"},
      {"type": "text", "text": "- Form: title, author, date, 1–5 rating."},
      {"type": "text", "text": "- List: sorted newest-finished first."},
      {"type": "text", "text": "- Storage: localStorage, survives reload."},
      {"type": "text", "text": "No dependencies."},
  ], [0, 30, 50, 80, 110, 140, 170]), motion="drawon"),
  [{"at": 0.05, "event": "Write index.html ✓"},
   {"at": 0.30, "event": "Claude's summary lands line by line"},
   {"at": 0.62, "event": "'sorted newest-finished first' — said out loud, and not asked for"}])

# ── B03 VERIFY 1 ──────────────────────────────────────────────────────────────
B("B03", "CYCLE 1 — VERIFY", "TERMINAL", LIAM,
  "Claude says done. I check. The bang runs a shell command from inside the session. "
  "Two hundred eighty-six lines. Local storage, twice. Now the one I said out loud before I looked: "
  "no external requests — grep for any URL or script tag. Nothing. That constraint held. "
  "Then the one I was waiting for. Remove, and sort. Both there. One I was told about. One I wasn't.",
  "CCSession — her four checks and their real output",
  R("CCSession", session("reading-log", "accept-edits", [
      {"type": "prompt", "text": "!wc -l index.html", "cue": 0, "typeDuration": 30},
      {"type": "text", "text": "     286 index.html"},
      {"type": "prompt", "text": "!grep -c localStorage index.html", "cue": 0, "typeDuration": 40},
      {"type": "text", "text": "2"},
      {"type": "prompt", "text": "!grep -nE \"https?://|<script src|<link \" index.html", "cue": 0, "typeDuration": 56},
      {"type": "text", "text": "(no output)"},
      {"type": "prompt", "text": "!grep -niE \"delete|remove|sort\" index.html", "cue": 0, "typeDuration": 50},
      {"type": "text", "text": "221:    books.sort(function (a, b) {"},
      {"type": "text", "text": "241:  '<div><button class=\"link\" data-id=\"' + b.id + '\">remove</button></div>' +"},
  ], [0, 40, 70, 110, 140, 200, 230, 280, 300], mascot="off")),
  [{"at": 0.05, "event": "wc -l → 286"},
   {"at": 0.25, "event": "localStorage → 2"},
   {"at": 0.45, "event": "grep for URLs → nothing; the constraint held"},
   {"at": 0.72, "event": "sort on line 221, remove on 241"}])

# ── B04 THE CORRECTION ────────────────────────────────────────────────────────
B("B04", "CYCLE 2 — THE CORRECTION", "TERMINAL", LIAM,
  "So I tell it exactly what I found and exactly what not to do. Take both out. Change nothing else. "
  "Don't touch the styling. Three edits, one file. And the diff is all red — fourteen lines gone, "
  "nothing added. That is the scope I asked for. Read the diff, not the summary.",
  "CCSession — her correction; three Edits; the deletion-only diff",
  R("CCSession", session("reading-log", "accept-edits", [
      {"type": "prompt", "text": ASK2, "cue": 0, "typeDuration": 120},
      {"type": "status", "verb": "Updating", "elapsed": "0m 09s", "tokens": "1.1k tokens"},
      # children = the three real Edit calls, labelled by the head of each old_string (SESSION.md Turn 2)
      {"type": "tool", "name": "Edit", "arg": "index.html", "state": "done", "children": [
          {"name": "Edit", "arg": "function render() { var books…"},
          {"name": "Edit", "arg": "logEl.innerHTML = books.map(fun…"},
          {"name": "Edit", "arg": "logEl.addEventListener(\"click\",…"}]},
      {"type": "diff", "file": "index.html", "addCount": 0, "delCount": 14, "lines": [
          {"gutter": "220", "text": "    var books = load();", "kind": "context"},
          {"gutter": "221", "text": "    books.sort(function (a, b) {", "kind": "del"},
          {"gutter": "222", "text": "      if (a.finished === b.finished) return b.added - a.added;", "kind": "del"},
          {"gutter": "241", "text": "  '<div><button class=\"link\" data-id=\"' + b.id + '\">remove</button></div>' +", "kind": "del"},
          {"gutter": "273", "text": "  logEl.addEventListener(\"click\", function (e) {", "kind": "del"},
      ]},
  ], [0, 140, 170, 230], mascot="off")),   # full-height block stack: Clawd would sit on the diff
  [{"at": 0.05, "event": "The correction types — with two negative constraints"},
   {"at": 0.40, "event": "✳ Updating… three Edits"},
   {"at": 0.60, "event": "Diff: 14 red lines, zero green"}])

# ── B05 THE SIDE EFFECT ───────────────────────────────────────────────────────
B("B05", "CYCLE 2 — WHAT ELSE IT DID", "TERMINAL", LIAM,
  "Then — without being asked — it did one more thing. It wrote a memory. Two files, outside my folder, "
  "in its own directory, so it remembers next time that I want exactly what I asked for. "
  "It told me. I'd have missed it if I'd stopped reading at 'both removed.' "
  "That's the product working as designed. It is also a decision made for me.",
  "CCSession — Claude's own words, then two Writes outside the repo",
  R("CCSession", session("reading-log", "accept-edits", [
      {"type": "text", "text": "Both removed: the `sort()` call,"},
      {"type": "text", "text": "the remove-button markup, and the"},
      {"type": "text", "text": "click handler. Nothing else touched."},
      {"type": "text", "text": "Let me save this preference"},
      {"type": "text", "text": "so I don't repeat it."},
      {"type": "tool", "name": "Write", "arg": "~/.claude/projects/…/memory/feedback_scope_discipline.md", "state": "done"},
      {"type": "tool", "name": "Write", "arg": "~/.claude/projects/…/memory/MEMORY.md", "state": "done"},
      {"type": "text", "text": "Removals are done and the preference is saved."},
  ], [0, 18, 36, 54, 90, 110, 150, 180, 220], mascot="off")),
  [{"at": 0.05, "event": "'Nothing else touched.'"},
   {"at": 0.30, "event": "'Let me save this preference…'"},
   {"at": 0.50, "event": "Two Writes — outside the repo"},
   {"at": 0.85, "event": "'the preference is saved.'"}])

# ── B06 VERIFY 2 ──────────────────────────────────────────────────────────────
B("B06", "CYCLE 2 — VERIFY", "TERMINAL", LIAM,
  "Check it. Git diff stat: one file, fourteen deletions, nothing else in the tree. "
  "Grep for remove or sort: gone. Local storage: still two. Inside the repo, 'nothing else touched' is true. "
  "Then I look where git can't. That memory directory. Two files. And the note it wrote is about me.",
  "CCSession — three in-repo checks, then the one outside it",
  R("CCSession", session("reading-log", "default", [
      {"type": "prompt", "text": "!git diff --stat", "cue": 0, "typeDuration": 34},
      {"type": "text", "text": " index.html | 14 --------------"},
      {"type": "text", "text": " 1 file changed, 14 deletions(-)"},
      {"type": "prompt", "text": "!grep -niE \"remove|sort\" index.html", "cue": 0, "typeDuration": 44},
      {"type": "text", "text": "(no output)"},
      {"type": "prompt", "text": "!ls ~/.claude/projects/*vibecoders-session*/memory/", "cue": 0, "typeDuration": 60},
      {"type": "text", "text": "MEMORY.md"},
      {"type": "text", "text": "feedback_scope_discipline.md"},
  ], [0, 40, 60, 100, 140, 190, 250, 270], mascot="off")),
  [{"at": 0.05, "event": "git diff --stat → 1 file, 14 deletions"},
   {"at": 0.35, "event": "grep → nothing"},
   {"at": 0.60, "event": "ls the memory dir → two files"}])

# ── B08 CONDUCT ───────────────────────────────────────────────────────────────
B("B08", "CONDUCT — THE BOONDOGGLE SCORE", "TERMINAL", LIAM,
  "Who did what. Step one was mine: the sentence with five constraints in it — that's problem formulation. "
  "Claude built the file; the handoff condition was every constraint holds under grep, and it did. "
  "Step three, the dangerous middle: reading the plan and the file, and hearing 'delete option' and 'sorted' before running anything. "
  "Claude removed both, cleanly. Then interpretive judgment: 'nothing else touched' was true inside the tree and false outside it. "
  "Notice the zero. No executive integration — one thread, one file. That's fine at this size. It won't stay fine.",
  "CCBoondoggleScore — six steps, the dangerous middle ringed, one capacity at zero",
  R("CCBoondoggleScore", {
      "system": "reading log — one file",
      "steps": [
          {"n": 1, "phase": "F", "labor": "human", "capacity": "PF", "text": "One sentence, five constraints, up front"},
          {"n": 2, "phase": "C", "labor": "claude", "text": "Build the form, the list, the storage", "handoff": "every constraint in the ask holds under grep", "dependsOn": [1]},
          {"n": 3, "phase": "C", "labor": "human", "capacity": "PA", "text": "Read plan and file first: 'delete', 'sorted'", "dependsOn": [2]},
          {"n": 4, "phase": "C", "labor": "claude", "text": "Remove both; change nothing else; don't touch styling", "handoff": "git diff --stat: one file, deletions only", "dependsOn": [3]},
          {"n": 5, "phase": "H", "labor": "human", "capacity": "IJ", "text": "'Nothing else touched' — true in the repo, false on the machine", "dependsOn": [4]},
          {"n": 6, "phase": "H", "labor": "human", "capacity": "TO", "text": "Decide whether the memory it wrote is a fence I want", "dependsOn": [5]},
      ],
      "dangerousMiddle": 3,
      "distribution": True,
      "stepGap": 22,
  }, motion="drawon"),
  [{"at": 0.05, "event": "Header: 6 steps · 2 claude · 4 human"},
   {"at": 0.20, "event": "Steps land in dependency order; handoffs under the Claude steps"},
   {"at": 0.45, "event": "Step 3 rings terracotta — the dangerous middle"},
   {"at": 0.85, "event": "Tally: EI 0, in red"}])

# ── B09 HUMAN ─────────────────────────────────────────────────────────────────
B("B09", "HUMAN — THE LEDGER", "TERMINAL", LIAM,
  "So what was mine. I must decide what done means — I wrote it down before it started. I must read the file before I run it. "
  "And I must look outside the folder, because the machine cannot tell me when it's done something I'd mind; "
  "it sounded exactly as sure about the memory file as about the form. "
  "Claude can write two hundred lines in one pass and remove exactly what I name. "
  "Next time I keep the constraints. Six lines. Mine — and one of them says: don't remember me.",
  "CCHumanLedger — the AI column first, the human column second and holding",
  R("CCHumanLedger", {
      "ai": [
          {"tier": "CAN", "text": "write 286 lines in one pass"},
          {"tier": "CAN", "text": "remove exactly what I name"},
          {"tier": "SHOULD", "text": "say what it adds — it did, once"},
          {"tier": "SHOULD", "text": "say what it writes outside the repo"},
      ],
      "human": [
          {"tier": "MUST", "text": "decide what done means, first"},
          {"tier": "MUST", "text": "read it before I run it"},
          {"tier": "MUST", "text": "look outside the folder too"},
          {"tier": "SHOULD", "text": "name the failure before I look"},
      ],
      "closing": "Next time I keep the constraints. Six lines. Mine.",
      "humanCue": 70, "rowGap": 12,
  }, motion="drawon"),
  [{"at": 0.05, "event": "THE AI column lands"},
   {"at": 0.35, "event": "THE HUMAN column lands — MUST rows ruled in terracotta"},
   {"at": 0.85, "event": "Closing line"}])

# ── CLOSING BLOCK — Liam ──────────────────────────────────────────────────────
B("BVDT", "VERDICT", "BOOKEND", LIAM,
  "Let's recap with Claude. Vibecoding is real: no code written by hand, a working tool in two turns. "
  "The first pass added two features nobody asked for and announced one of them. The correction was fourteen deleted lines and nothing else — "
  "inside the repo. Outside it, Claude wrote itself a note about me. Every check she ran was a command; the only claim she took on faith was the one that turned out to be wrong. "
  "What would prove this reel wrong: a session where reading the plan and the diff catches nothing, twice in a row.",
  "ClaudeVerdictArtifact — the verdict page",
  R("ClaudeVerdictArtifact", {
      "artifactTitle": "verdict.md",
      "artifactHeading": "Vibecoders Welcome",
      "artifactLines": [
          "No code by hand. A working tool in two turns.",
          "Pass one added two features nobody asked for, and announced one of them.",
          "The fix was fourteen deleted lines — inside the repo.",
          "Outside it, Claude wrote itself a note about the user.",
          "Every check was a command. The one claim taken on faith was the wrong one.",
          "FALSIFIABLE: a session where reading the plan and the diff catches nothing, twice.",
      ],
  }, motion="hold"),
  [{"at": 0.0, "event": "Artifact window opens"}, {"at": 0.2, "event": "Lines land"}, {"at": 0.9, "event": "Falsifiability line holds"}],
  lead_silence_s=0.5)

B("BHTF", "YOUR TURN", "BOOKEND", LIAM,
  "Your turn. Make an empty folder, open Claude Code in it, and describe one small tool you'd actually use — "
  "in a paragraph that lists every constraint you care about. Before you run what it writes, paste this: "
  "List everything you built that I did not explicitly ask for, and everything you wrote outside this folder. "
  "Then tell me which of those you would remove if I asked for exactly what I asked for and nothing else.",
  "ClaudeComposerAsk — the viewer's prompt, read aloud",
  R("ClaudeComposerAsk", {
      "greeting": "Your turn.",
      "command": "List everything you built that I did not explicitly ask for, and everything you wrote outside this folder. Then tell me which of those you would remove if I asked for exactly what I asked for and nothing else.",
      "segment": TITLE, "topic": "YOUR TURN · " + TOPIC, "runningText": "paste this into Claude Code…", "output": [],
      "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High",
  }),
  [{"at": 0.0, "event": "Composer types the prompt"}, {"at": 0.6, "event": "Send arms; prompt holds while discussed"}])

B("BOUT", "OUTRO", "BOOKEND", LIAM,
  "Vibecoders Welcome. Liam, in for Bear.",
  "ClaudeTitleOutro — OUTRO-LOCK",
  R("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}, motion="hold"),
  [{"at": 0.0, "event": "Poster-serif title, terracotta period"}, {"at": 0.35, "event": "@NikBearBrown — hardcoded"}, {"at": 0.55, "event": "Slug-seeded mascot"}])

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "subtitle": "No code by hand. Two turns. One note it wrote about me.",
        "topic": TOPIC, "skill": "cc-explainer", "playlist": "Claude Code 101", "tier": "00-what-it-is",
        "audience": "NikBearBrown", "folderLabel": "@NikBearBrown", "handle": "@NikBearBrown",
        "brand": "claude", "palette": "claude", "register": "Teardown", "engine": "kokoro",
        "voice_kokoro": LIAM, "persona": "liam", "in_for_bear": True,
        "operator": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "closing_voice": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "aspect": "16:9", "fps": 30,
        "session": "SESSION.md", "session_id": "dff47fa4-dd2f-4f65-bd3c-0c03beab300d",
        "derived_from": "claude-code-101/00-what-it-is/claude-cowork--claude-liam-claude-code (the concept; not the beats)",
        "sources": ["SESSION.md (the real session)",
                    "info-7375-computational-skepticism-for-ai/chapters/_expanded-four-moves.md",
                    "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
                    "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"],
    },
    "beats": beats,
}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(sheet, open(os.path.join(here, "beat_sheet.json"), "w"), indent=2, ensure_ascii=False)
tot = sum(b["estimated_duration_s"] for b in beats)
print(f"{len(beats)} beats — est {tot:.0f}s ({int(tot//60)}:{int(tot%60):02d}) · voice {LIAM} on every beat (LIAM LAW)")
non_terminal = [b["beat_id"] for b in beats if b["lane"] not in ("TERMINAL", "BOOKEND", "IDEA", "CARD")]
print("non-terminal body beats:", non_terminal or "none")
