#!/usr/bin/env python3
"""
author_sheet.py — cc-claude-md  (cc-explainer · Claude Code 101 · tier 01, film 01)

"CLAUDE.md: The File It Reads First." Every CCSession block traces to SESSION.md
(three real headless runs, 2026-09-08). Prompt blocks are what Liam typed;
commands he ran in the shell are shown as bang commands (same command, same
output). Tool names/args and Claude's sentences are verbatim; paths shortened
to file names for display.

Spine (cc-explainer, restructured): B00 cold open → BIDEA → BDEFS → the loop →
CONDUCT → HUMAN → BVDT → BHTF → BOUT. Liam, in for Bear, on every beat.
"""
import json, os

SLUG  = "cc-claude-md"
TITLE = "CLAUDE.md: The File It Reads First"
TOPIC = "CLAUDE CODE 101"
LIAM  = "am_onyx"
WPS   = 2.9

ASK2 = ("CLAUDE.md says \"Run tests: pytest\", but pytest is not installed on this machine and I do not want any "
        "dependencies. Rewrite tests/test_gradebook.py with the standard library unittest module only (no fixtures), "
        "and change the test commands in CLAUDE.md to the exact command that works here. Do not touch src/gradebook.py.")
ASK3 = ("Add a \"remove NAME\" command that deletes a student and their scores. Follow this repo's conventions "
        "and run the tests when you are done.")

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

# ── B00 COLD OPEN — /init ─────────────────────────────────────────────────────
B("B00", "COLD OPEN — /init", "TERMINAL", LIAM,
  "This is Liam, in for Bear. Every Claude Code session starts by reading one file, if it exists: CLAUDE.md, "
  "in the folder you opened. Nothing in it is magic — it's a text file. So let's make one the way the product makes it. "
  "A tiny gradebook: two Python files and a test. I type slash init. Watch what it reads before it writes.",
  "CCSession — /init types; four Reads before the Write",
  R("CCSession", session("gradebook", "accept-edits", [
      {"type": "prompt", "text": "/init", "cue": 0, "typeDuration": 20},
      {"type": "status", "verb": "Exploring", "elapsed": "0m 05s", "tokens": "1.9k tokens"},
      {"type": "tool", "name": "Bash", "arg": "ls -la", "state": "done"},
      {"type": "tool", "name": "Read", "arg": "README.md", "state": "done"},
      {"type": "tool", "name": "Read", "arg": "src/gradebook.py", "state": "done"},
      {"type": "tool", "name": "Read", "arg": "tests/test_gradebook.py", "state": "done"},
      {"type": "tool", "name": "Read", "arg": ".gitignore", "state": "done"},
  ], [0, 60, 110, 150, 185, 220, 255])),
  [{"at": 0.05, "event": "/init types"},
   {"at": 0.45, "event": "✳ Exploring…"},
   {"at": 0.60, "event": "ls, then four Reads — it reads before it writes"}])

# ── BIDEA THE IDEA ────────────────────────────────────────────────────────────
B("BIDEA", "THE IDEA", "IDEA", LIAM,
  "Here's the idea of this film. CLAUDE.md is not settings. It's a briefing for a colleague who forgets everything between sessions: "
  "what to run, how the code is shaped, what not to touch. Claude Code reads it first, every time, in the folder you opened. "
  "I'll let the product write one, break it on purpose with the truth about my machine, fix it, "
  "and then open a fresh session to see whether the briefing actually steers.",
  "BrutalistHesitantWriter — 'settings' reconsidered into 'a briefing'",
  R("BrutalistHesitantWriter", writer("CLAUDE.md is settings for Claude.\nNo — it's a note to a colleague\nwho forgets everything between sessions:\nwhat to run, what not to touch.", "settings", "a briefing", SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at": 0.05, "event": "The writer starts"}, {"at": 0.30, "event": "'settings' reconsidered → 'a briefing'"}, {"at": 0.85, "event": "Last line lands"}])

# ── BDEFS DEFINITIONS ─────────────────────────────────────────────────────────
B("BDEFS", "DEFINITIONS", "CARD", LIAM,
  "Five words before we start. CLAUDE.md: a text file in your project that Claude Code reads at the start of every session. "
  "Slash init: the built-in command that reads your project and drafts that file. Session: one run of Claude Code — it forgets everything when it ends. "
  "Pytest and unittest: two ways to run Python tests; pytest has to be installed, unittest is built in. "
  "Convention: the way this codebase does things. The briefing's job is to say it out loud.",
  "CCDefinitions — five terms",
  R("CCDefinitions", {"title": "TERMS IN THIS FILM", "terms": [
      {"term": "CLAUDE.md", "meaning": "a text file in your project that Claude Code reads at the start of every session"},
      {"term": "/init", "meaning": "the built-in command that reads your project and drafts a CLAUDE.md"},
      {"term": "session", "meaning": "one run of Claude Code — it forgets everything when it ends"},
      {"term": "pytest · unittest", "meaning": "two ways to run Python tests; pytest must be installed, unittest is built in"},
      {"term": "convention", "meaning": "the way this codebase does things — the briefing's job is to say it out loud"},
  ], "startCue": 12, "rowGap": 48}, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience: the words the session uses without explaining them"),
  [{"at": 0.05, "event": "First term lands"}, {"at": 0.5, "event": "Terms land one at a time"}, {"at": 0.9, "event": "Five rows hold"}])

# ── B01 THE FILE ──────────────────────────────────────────────────────────────
B("B01", "THE FILE", "TERMINAL", LIAM,
  "It read four files and wrote seventeen lines. Two sections. Commands: how to run it, how to test it. "
  "Architecture: the two things you can't see from the file names — every command re-reads the whole JSON file, "
  "and new subcommands go in one dict. That last sentence is the kind of thing a new colleague spends an afternoon discovering. Now it's a line.",
  "CCSession — Write CLAUDE.md; its lines, verbatim",
  R("CCSession", session("gradebook", "accept-edits", [
      {"type": "tool", "name": "Write", "arg": "CLAUDE.md", "state": "done"},
      {"type": "text", "text": "## Commands"},
      {"type": "text", "text": "- Run tests: `pytest`"},
      {"type": "text", "text": "## Architecture"},
      {"type": "text", "text": "Each command re-reads and re-writes"},
      {"type": "text", "text": "the entire file — there is no in-memory"},
      {"type": "text", "text": "session state. … adding a subcommand"},
      {"type": "text", "text": "means adding a top-level function"},
      {"type": "text", "text": "and an entry to that dict."},
  ], [0, 30, 55, 110, 135, 155, 175, 195, 215], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "Write CLAUDE.md ✓"}, {"at": 0.25, "event": "Commands: pytest"}, {"at": 0.55, "event": "Architecture: the dict sentence"}])

# ── B02 VERIFY 1 ──────────────────────────────────────────────────────────────
B("B02", "CYCLE 1 — VERIFY", "TERMINAL", LIAM,
  "Check it. Seventeen lines. Now the command it wrote: pytest. Command not found. Python three, dash m, pytest: no module named pytest. "
  "The briefing is wrong about my machine — not about the code. It wrote what most Python projects do, not what this Mac has. "
  "A briefing you didn't check is a briefing your next session will trust.",
  "CCSession — three checks; the file's own command fails",
  R("CCSession", session("gradebook", "default", [
      {"type": "prompt", "text": "!wc -l CLAUDE.md", "cue": 0, "typeDuration": 28},
      {"type": "text", "text": "      17 CLAUDE.md"},
      {"type": "prompt", "text": "!pytest", "cue": 0, "typeDuration": 16},
      {"type": "text", "text": "zsh: command not found: pytest"},
      {"type": "prompt", "text": "!python3 -m pytest -q", "cue": 0, "typeDuration": 34},
      {"type": "text", "text": "No module named pytest"},
  ], [0, 40, 80, 120, 170, 220], mascot="off")),
  [{"at": 0.05, "event": "wc -l → 17"}, {"at": 0.35, "event": "pytest → command not found"}, {"at": 0.65, "event": "No module named pytest"}])

# ── B03 THE CORRECTION ────────────────────────────────────────────────────────
B("B03", "CYCLE 2 — THE CORRECTION", "TERMINAL", LIAM,
  "So I tell it the truth: pytest isn't here, I don't want dependencies, rewrite the test on the standard library, "
  "and put the exact command that works in the file. It rewrites the test. Then it tries to run it — and the fence stops it: "
  "python isn't on my allow-list, only python three. It asks. Nobody's there to answer in a headless run. "
  "So it says so, and edits the file anyway — twice, because the architecture paragraph still mentioned pytest fixtures.",
  "CCSession — the correction; the blocked run; the question nobody answers; two Edits",
  R("CCSession", session("gradebook", "accept-edits", [
      {"type": "prompt", "text": ASK2, "cue": 0, "typeDuration": 150},
      {"type": "tool", "name": "Write", "arg": "tests/test_gradebook.py", "state": "done"},
      {"type": "tool", "name": "Bash", "arg": "python tests/test_gradebook.py", "state": "done"},
      {"type": "text", "text": "This command requires approval"},
      {"type": "tool", "name": "AskUserQuestion", "arg": "May I run the test?", "state": "done"},
      {"type": "text", "text": "I'll proceed without running verification."},
      {"type": "tool", "name": "Edit", "arg": "CLAUDE.md", "state": "done", "children": [
          {"name": "Edit", "arg": "- Run tests: `pytest`…"}, {"name": "Edit", "arg": "Tests import `gradebook` by inserting…"}]},
  ], [0, 165, 195, 215, 240, 265, 290], mascot="off")),
  [{"at": 0.05, "event": "The correction types"}, {"at": 0.55, "event": "Write the test; python blocked; it asks"}, {"at": 0.85, "event": "Two Edits to CLAUDE.md"}])

# ── B04 THE DIFF ──────────────────────────────────────────────────────────────
B("B04", "CYCLE 2 — THE DIFF", "TERMINAL", LIAM,
  "Read the diff, not the summary. Pytest out, a python command in; the dependency line fixed. "
  "And the honest line at the end: I was not able to verify the commands run — please run one to confirm. "
  "That's the right sentence. The briefing now has a command it never ran.",
  "CCSession — the CLAUDE.md diff; Claude's last sentence",
  R("CCSession", session("gradebook", "accept-edits", [
      {"type": "diff", "file": "CLAUDE.md", "addCount": 4, "delCount": 4, "lines": [
          {"gutter": "8", "text": "- Run tests: `pytest`", "kind": "del"},
          {"gutter": "8", "text": "- Run tests: `python tests/test_gradebook.py`", "kind": "add"},
          {"gutter": "11", "text": "No dependencies beyond the standard library and `pytest` for tests.", "kind": "del"},
          {"gutter": "11", "text": "No dependencies beyond the standard library. Tests use `unittest`.", "kind": "add"},
      ]},
      {"type": "text", "text": "I was not able to verify the commands run"},
      {"type": "text", "text": "(verification was declined), so please"},
      {"type": "text", "text": "run one to confirm."},
  ], [0, 120, 140, 160], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "Diff: pytest out, python in"}, {"at": 0.6, "event": "'I was not able to verify…'"}])

# ── B05 VERIFY 2 ──────────────────────────────────────────────────────────────
B("B05", "CYCLE 2 — VERIFY", "TERMINAL", LIAM,
  "I run it myself. One test, OK. But look at the command in the file: python. On this Mac, python is an alias in my shell; "
  "inside Claude's fence it wasn't allowed. I'll leave that for now — the next session should see the file exactly as Claude wrote it.",
  "CCSession — the test passes by hand; the file still says python",
  R("CCSession", session("gradebook", "default", [
      {"type": "prompt", "text": "!python3 tests/test_gradebook.py", "cue": 0, "typeDuration": 44},
      {"type": "text", "text": "Ran 1 test in 0.002s"},
      {"type": "text", "text": "OK"},
      {"type": "prompt", "text": "!grep -n \"Run tests\" CLAUDE.md", "cue": 0, "typeDuration": 40},
      {"type": "text", "text": "8:- Run tests: `python tests/test_…py`"},
      {"type": "prompt", "text": "!which python", "cue": 0, "typeDuration": 22},
      {"type": "text", "text": "python: aliased to python3"},
  ], [0, 50, 65, 110, 150, 195, 230], mascot="off")),
  [{"at": 0.05, "event": "Ran 1 test — OK"}, {"at": 0.45, "event": "The file says python"}, {"at": 0.8, "event": "python is an alias here"}])

# ── B06 THE FRESH SESSION ─────────────────────────────────────────────────────
B("B06", "CYCLE 3 — A FRESH SESSION", "TERMINAL", LIAM,
  "Now the payoff. A brand-new session — no memory of anything above — and one line: add a remove command, follow this repo's conventions, run the tests. "
  "It reads the two files, and it does exactly what the briefing said: a top-level function, one entry in the dict, a test in the existing pattern. "
  "Then it runs the file's test command, the fence blocks it, it asks, nobody answers, it stops and hands back. It never guessed.",
  "CCSession (new session) — the one-line ask; Read, Edit, Edit; the blocked run; the handback",
  R("CCSession", session("gradebook — new session", "accept-edits", [
      {"type": "prompt", "text": ASK3, "cue": 0, "typeDuration": 80},
      {"type": "tool", "name": "Read", "arg": "src/gradebook.py", "state": "done"},
      {"type": "tool", "name": "Edit", "arg": "src/gradebook.py", "state": "done"},
      {"type": "text", "text": "Now add a test following the pattern."},
      {"type": "tool", "name": "Edit", "arg": "tests/test_gradebook.py", "state": "done"},
      {"type": "tool", "name": "Bash", "arg": "python tests/test_gradebook.py", "state": "done"},
      {"type": "text", "text": "This command requires approval"},
      {"type": "text", "text": "I've added the `remove` command and a test,"},
      {"type": "text", "text": "but the Bash approval … was denied twice"},
      {"type": "text", "text": "in a row. … I'll stop and hand it back."},
  ], [0, 95, 125, 150, 175, 205, 225, 260, 280, 300], mascot="off")),
  [{"at": 0.05, "event": "One line, fresh session"}, {"at": 0.35, "event": "Read · Edit · Edit — the pattern"}, {"at": 0.7, "event": "Blocked; asks; hands back"}])

# ── B07 VERIFY 3 ──────────────────────────────────────────────────────────────
B("B07", "CYCLE 3 — VERIFY", "TERMINAL", LIAM,
  "Check it. Two files changed — the two I'd expect. The dispatch line: remove is in the dict. Two tests, OK. "
  "Remove on a missing student says so instead of crashing; that branch was tested too. "
  "One thing left: the briefing says python, my machine says python three. One sed, three lines, and the file is true of the code and the machine. "
  "That's the whole discipline. The file only steers if it's right.",
  "CCSession — diff stat, the dict line, two tests OK, the by-hand fix",
  R("CCSession", session("gradebook", "default", [
      {"type": "prompt", "text": "!git diff --stat", "cue": 0, "typeDuration": 30},
      {"type": "text", "text": " 2 files changed, 31 insertions(+)"},
      {"type": "diff", "file": "src/gradebook.py", "addCount": 1, "delCount": 1, "lines": [
          {"gutter": "46", "text": "{\"add\": add, \"score\": score, \"report\": report}", "kind": "del"},
          {"gutter": "46", "text": "{\"add\": add, \"score\": score, \"remove\": remove, …}", "kind": "add"},
      ]},
      {"type": "prompt", "text": "!python3 tests/test_gradebook.py", "cue": 0, "typeDuration": 44},
      {"type": "text", "text": "Ran 2 tests in 0.002s — OK"},
      {"type": "prompt", "text": "!sed -i '' 's/python /python3 /g' CLAUDE.md", "cue": 0, "typeDuration": 56},
      {"type": "prompt", "text": "!grep -c python3 CLAUDE.md", "cue": 0, "typeDuration": 32},
      {"type": "text", "text": "3"},
  ], [0, 40, 80, 140, 180, 230, 280, 310], mascot="off")),
  [{"at": 0.05, "event": "git diff --stat → two files"}, {"at": 0.3, "event": "The dict line"}, {"at": 0.55, "event": "Ran 2 tests — OK"}, {"at": 0.85, "event": "sed → python3, three lines"}])

# ── B08 CONDUCT ───────────────────────────────────────────────────────────────
B("B08", "CONDUCT — THE BOONDOGGLE SCORE", "TERMINAL", LIAM,
  "Who did what. Step one, mine: a tiny repo and slash init — let the product draft it. Claude read four files and wrote seventeen lines; "
  "the handoff was every command in the file runs on this machine, and it missed that. Step three, the dangerous middle: a confident briefing with a command nobody had run, "
  "and only running it stood between that line and every future session. Claude rewrote the test and fixed the file, and said it couldn't verify. "
  "Then tool orchestration: a fresh session with one line, to let the file steer. And it did: function, dict entry, test in the pattern, handoff met. "
  "Two zeros — interpretive judgment, executive integration. The python three edit was judgment, and I did it by hand. A small session, honestly scored.",
  "CCBoondoggleScore — six steps, the dangerous middle ringed",
  R("CCBoondoggleScore", {
      "system": "CLAUDE.md — draft, break, fix, steer",
      "steps": [
          {"n": 1, "phase": "F", "labor": "human", "capacity": "PF", "text": "A tiny repo, then /init: let the product draft"},
          {"n": 2, "phase": "C", "labor": "claude", "text": "/init: read four files, write 17 lines", "handoff": "every command in the file runs on this machine", "dependsOn": [1]},
          {"n": 3, "phase": "C", "labor": "human", "capacity": "PA", "text": "Ran the file's command: pytest not found", "dependsOn": [2]},
          {"n": 4, "phase": "C", "labor": "claude", "text": "Rewrite the test on unittest; fix the file", "handoff": "the file's test command passes here", "dependsOn": [3]},
          {"n": 5, "phase": "I", "labor": "human", "capacity": "TO", "text": "Fresh session, one line: let the file steer", "dependsOn": [4]},
          {"n": 6, "phase": "B", "labor": "claude", "text": "remove(): function + dict entry + test in the pattern", "handoff": "two tests pass; conventions followed", "dependsOn": [5]},
      ],
      "dangerousMiddle": 3, "distribution": True, "stepGap": 22,
  }, motion="drawon"),
  [{"at": 0.05, "event": "Header"}, {"at": 0.3, "event": "Steps land; handoffs"}, {"at": 0.45, "event": "Step 3 rings"}, {"at": 0.9, "event": "Tally"}])

# ── B09 HUMAN ─────────────────────────────────────────────────────────────────
B("B09", "HUMAN — THE LEDGER", "TERMINAL", LIAM,
  "So what was mine. I must run every command the file claims. I must keep the file true of the machine, not just the code. "
  "I must answer when the fence asks — or run the thing myself. I should let slash init draft, then read all of it. "
  "Claude can draft a briefing from four files. It can follow one in a fresh session — it did, to the letter. "
  "It should say when it couldn't verify — it did. It should stop when it's denied twice — it did. "
  "The briefing steers only if it's true. Keeping it true is mine.",
  "CCHumanLedger — AI column, then HUMAN column",
  R("CCHumanLedger", {
      "ai": [{"tier": "CAN", "text": "draft a briefing from four files"},
             {"tier": "CAN", "text": "follow it in a fresh session"},
             {"tier": "SHOULD", "text": "say when it couldn't verify"},
             {"tier": "SHOULD", "text": "stop when denied twice — it did"}],
      "human": [{"tier": "MUST", "text": "run every command the file claims"},
                {"tier": "MUST", "text": "keep the file true of the machine"},
                {"tier": "MUST", "text": "answer the fence, or run it myself"},
                {"tier": "SHOULD", "text": "let /init draft; read all of it"}],
      "closing": "The briefing steers only if it's true. Keeping it true is mine.",
      "humanCue": 70, "rowGap": 12,
  }, motion="drawon"),
  [{"at": 0.05, "event": "THE AI column"}, {"at": 0.35, "event": "THE HUMAN column"}, {"at": 0.85, "event": "Closing line"}])

# ── CLOSING BLOCK ─────────────────────────────────────────────────────────────
B("BVDT", "VERDICT", "BOOKEND", LIAM,
  "Let's recap with Claude. CLAUDE.md is a briefing, not settings, and Claude Code reads it first every session. "
  "Slash init drafted seventeen lines from four files and got the code right and the machine wrong. I broke it with one command, fixed it with one prompt, "
  "and a fresh session followed it to the letter: a function, a dict entry, a test in the pattern. It couldn't run the tests, said so, and stopped. "
  "What would prove this reel wrong: a fresh session that ignores a convention the file states plainly.",
  "ClaudeVerdictArtifact — the verdict page",
  R("ClaudeVerdictArtifact", {"artifactTitle": "verdict.md", "artifactHeading": TITLE, "artifactLines": [
      "CLAUDE.md is a briefing, not settings. Claude Code reads it first, every session.",
      "/init drafted 17 lines from four files: right about the code, wrong about the machine.",
      "One command broke it (pytest: not found). One prompt fixed it.",
      "A fresh session followed it to the letter: function, dict entry, test in the pattern.",
      "It could not run the tests, said so, and stopped. The human ran them.",
      "FALSIFIABLE: a fresh session that ignores a convention the file states plainly.",
  ]}, motion="hold"),
  [{"at": 0.0, "event": "Artifact opens"}, {"at": 0.2, "event": "Lines land"}, {"at": 0.9, "event": "Falsifiable line holds"}],
  lead_silence_s=0.5)

B("BHTF", "YOUR TURN", "BOOKEND", LIAM,
  "Your turn. Open Claude Code in a project of yours and type slash init. Then paste this: "
  "List every command you wrote into CLAUDE.md and run each one. For any that fails on this machine, fix the file, not the machine. "
  "Then open a fresh session and give it one small task — and read whether it followed the file.",
  "ClaudeComposerAsk — the viewer's prompt",
  R("ClaudeComposerAsk", {"greeting": "Your turn.",
      "command": "List every command you wrote into CLAUDE.md and run each one. For any that fails on this machine, fix the file, not the machine.",
      "segment": TITLE, "topic": "YOUR TURN · " + TOPIC, "runningText": "paste this into Claude Code…", "output": [],
      "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High"}),
  [{"at": 0.0, "event": "Composer types the prompt"}, {"at": 0.6, "event": "Send arms"}])

B("BOUT", "OUTRO", "BOOKEND", LIAM,
  "CLAUDE.md: The File It Reads First. Liam, in for Bear.",
  "ClaudeTitleOutro — OUTRO-LOCK",
  R("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}, motion="hold"),
  [{"at": 0.0, "event": "Title"}, {"at": 0.35, "event": "@NikBearBrown"}, {"at": 0.55, "event": "Mascot"}])

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "subtitle": "A briefing, not settings. /init drafts it; you keep it true.",
    "topic": TOPIC, "skill": "cc-explainer", "playlist": "Claude Code 101", "tier": "01-context-and-memory",
    "audience": "NikBearBrown", "folderLabel": "@NikBearBrown", "handle": "@NikBearBrown",
    "brand": "claude", "palette": "claude", "register": "Teardown", "engine": "kokoro",
    "voice_kokoro": LIAM, "persona": "liam", "in_for_bear": True,
    "operator": {"name": "Liam", "voice": LIAM, "engine": "kokoro"}, "closing_voice": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
    "aspect": "16:9", "fps": 30, "session": "SESSION.md",
    "session_ids": {"A": "fe0edef3-b504-4ce2-8996-386d9c3a68b7", "B": "see evidence/turn3.jsonl"},
    "derived_from": "claude-code-101/01-context-and-memory/claude-code--claude-liam-claudemd-constitution (the concept; not the beats)",
    "sources": ["SESSION.md (the real runs)", "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
                "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"],
}, "beats": beats}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(sheet, open(os.path.join(here, "beat_sheet.json"), "w"), indent=2, ensure_ascii=False)
tot = sum(b["estimated_duration_s"] for b in beats)
print(f"{len(beats)} beats — est {tot:.0f}s ({int(tot//60)}:{int(tot%60):02d})")
for b in beats:
    r = b["shot"]["remotion"]
    if r["pattern"] == "CCSession":
        assert len(r["props"]["blocks"]) == len(r["props"]["cues"]), f"{b['beat_id']}: blocks≠cues"
        for blk in r["props"]["blocks"]:
            if blk["type"] == "text" and len(blk["text"]) > 44: print(f"  ⚠ {b['beat_id']} text {len(blk['text'])}: {blk['text']!r}")
    if r["pattern"] == "CCHumanLedger":
        for col in ("ai", "human"):
            for row in r["props"][col]:
                if len(row["text"]) > 34: print(f"  ⚠ ledger {len(row['text'])}: {row['text']}")
