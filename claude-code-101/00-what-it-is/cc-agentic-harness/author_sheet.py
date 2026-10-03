#!/usr/bin/env python3
"""
author_sheet.py — cc-agentic-harness  (cc-explainer · Claude Code 101 · tier 00, film 00)

"Claude Code Is an Agentic Harness. What Is That?" Writes beat_sheet.json. Every
CCSession block below is copied from SESSION.md — six headless Claude Code runs
that actually ran on 2026-09-08 (REAL-SESSION LAW): the same ask with the harness
off (A2), half-off (A), on (B), and a three-pass shell loop (C). Prompt blocks
are what Liam typed (TYPES-NOT-NARRATES). Commands Liam ran in the shell between
runs are shown as bang commands inside the session (same command, same output;
display convention recorded in FACTCHECK.md). Tool names, args and Claude's own
sentences are verbatim; long paths are shortened to the file name for display.

Operator: Liam, in for Bear (Kokoro am_onyx) — first person, present tense, Teardown. LIAM LAW.
"""
import json, os

SLUG  = "cc-agentic-harness"
TITLE = "Claude Code Is an Agentic Harness"
TOPIC = "CLAUDE CODE 101"
LIAM  = "am_onyx"
WPS   = 2.9

ASK  = "Create a file named hello.txt in this folder containing exactly one line: hello"
LOOP = ("Read tasks.md. Do ONLY the first unchecked task, then change its \"[ ]\" to \"[x]\" in tasks.md. "
        "Do not touch any other task. Reply with one line saying which task you did.")

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

# ── B00 COLD OPEN — the harness off ───────────────────────────────────────────
B("B00", "COLD OPEN — HARNESS OFF", "TERMINAL", LIAM,
  "This is Liam, in for Bear. Claude Code is an agentic harness. Everyone says it; nobody shows it. "
  "So here's the model with the harness turned off — no tools, none. One ask: make a file with one line in it. "
  "It says: creating the file now. And then, nothing. List the folder: the README I put there. No file. "
  "That sentence was the whole event. A model on its own can only talk.",
  "CCSession — the ask types; Claude's one sentence; ls shows nothing happened",
  R("CCSession", session("claude -p --tools \"\"", "default", [
      {"type": "prompt", "text": ASK, "cue": 0, "typeDuration": 90},
      {"type": "text", "text": "Creating the file now."},
      {"type": "prompt", "text": "!ls", "cue": 0, "typeDuration": 20},
      {"type": "text", "text": "README.md"},
  ], [0, 150, 250, 290])),
  [{"at": 0.05, "event": "The ask types"},
   {"at": 0.45, "event": "'Creating the file now.'"},
   {"at": 0.72, "event": "ls → README.md — no hello.txt"}])

# ── BIDEA THE IDEA (beat two: the hesitant writer types what this film is about) ──
B("BIDEA", "THE IDEA", "IDEA", LIAM,
  "Here's the idea of this film. Claude Code is not a better model. It's the same model you talk to in the chat window, wrapped in something: a list of what it may touch, rules about touching it, and a loop that keeps asking what next. That wrapper is the harness. I'm going to switch it off, half on, and on, so you can see the model without it — and then build a tiny harness of my own around it.",
  "BrutalistHesitantWriter — the idea of the film, typed; one word reconsidered (better → different)",
  R("BrutalistHesitantWriter", writer("Is Claude Code a better model?\nNo — the same model as the chat window.\nWhat's different is the harness:\nwhat it may touch, the rules, the loop.", 'better', 'different', SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at": 0.05, "event": "The writer starts the sentence"},
   {"at": 0.40, "event": "'better' typed, reconsidered, replaced with 'different'"},
   {"at": 0.80, "event": "The last line lands; caret holds"}])

# ── BDEFS DEFINITIONS (the jargon this film cannot avoid, one plain line each) ──
B("BDEFS", "DEFINITIONS", "CARD", LIAM,
  'Five words before we start. Headless: Claude Code run from the shell with one prompt — it answers and exits. Tools list: what the model may call — read, write, run a command, use a connector. Connector, or MCP: an outside service plugged in as tools, like Google Drive. Permission mode: the rule for which tool calls need your yes. Stream json: the whole session as a log, one event per line. The receipt.',
  "CCDefinitions — five terms, one plain line each, landing one at a time",
  R("CCDefinitions", {
      "title": "TERMS IN THIS FILM",
      "terms": [
          {"term": 'headless', "meaning": 'Claude Code run from the shell with one prompt — it answers and exits'},
          {"term": 'tools list', "meaning": 'what the model may call: read, write, run a command, use a connector'},
          {"term": 'connector (MCP)', "meaning": 'an outside service plugged in as tools — Google Drive, Vercel, calendars'},
          {"term": 'permission mode', "meaning": 'the rule for which tool calls need your yes before they run'},
          {"term": 'stream-json', "meaning": 'the whole session as a log, one event per line — the receipt'},
      ],
      "startCue": 12, "rowGap": 48,
  }, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience: the words the session uses without explaining them"),
  [{"at": 0.05, "event": "Title; first term lands"},
   {"at": 0.50, "event": "Terms land one at a time, meaning after term"},
   {"at": 0.90, "event": "Five rows hold"}])

# ── B01 THE MANIFEST — the init event ─────────────────────────────────────────
B("B01", "THE MANIFEST", "TERMINAL", LIAM,
  "Turn the harness on and ask for the receipt — stream json. The first event isn't the model. It's the harness introducing itself. "
  "A permission mode. A tools list: thirty built in, and a hundred and forty more from connectors on this Mac. Five MCP servers. Forty skills. Nine agents. "
  "The folder it's fenced to. Where its memory lives. None of that is the model. All of it is what the model gets handed before it reads my sentence. "
  "That's the harness, in one event.",
  "CCSession — the init event's fields, verbatim keys, real counts",
  R("CCSession", session("claude -p --output-format stream-json", "accept-edits", [
      {"type": "text", "text": "\"type\": \"system\", \"subtype\": \"init\""},
      {"type": "text", "text": "\"permissionMode\": \"acceptEdits\""},
      {"type": "text", "text": "\"tools\": [ 30 built-in + 140 mcp__… ]"},
      {"type": "text", "text": "\"mcp_servers\": [ 5 ]"},
      {"type": "text", "text": "\"skills\": [ 40 ]   \"agents\": [ 9 ]"},
      {"type": "text", "text": "\"slash_commands\": [ 56 ]"},
      {"type": "text", "text": "\"cwd\": \"…/scratchpad/harness-session\""},
      {"type": "text", "text": "\"memory_paths\": { \"auto\": \"~/.claude/…\" }"},
  ], [0, 40, 70, 120, 150, 185, 215, 250], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "'type: system, subtype: init'"},
   {"at": 0.25, "event": "permissionMode; tools 30 + 140"},
   {"at": 0.55, "event": "mcp_servers 5 · skills 40 · agents 9"},
   {"at": 0.85, "event": "cwd; memory_paths"}])

# ── B02 CYCLE 1 — HARNESS ON ──────────────────────────────────────────────────
B("B02", "CYCLE 1 — HARNESS ON", "TERMINAL", LIAM,
  "Same model. Same sentence. Now Write is on the list. One tool call, one file, two turns. Cat it: hello. "
  "The difference between run one and run two is not intelligence. It's a list. "
  "That is what a harness is: the list of what the model can touch, the rules for touching it, and the loop that keeps asking 'what next' until it says done.",
  "CCSession — the same ask; Write; Claude's line; cat hello.txt",
  R("CCSession", session("claude -p --allowedTools Read,Write", "accept-edits", [
      {"type": "prompt", "text": ASK, "cue": 0, "typeDuration": 90},
      {"type": "status", "verb": "Writing", "elapsed": "0m 03s", "tokens": "0.2k tokens"},
      {"type": "tool", "name": "Write", "arg": "hello.txt", "state": "done"},
      {"type": "text", "text": "Created `hello.txt` with"},
      {"type": "text", "text": "the single line `hello`."},
      {"type": "prompt", "text": "!cat hello.txt", "cue": 0, "typeDuration": 26},
      {"type": "text", "text": "hello"},
  ], [0, 100, 130, 160, 180, 230, 260], mascot="off")),
  [{"at": 0.05, "event": "Same ask types"},
   {"at": 0.35, "event": "Write hello.txt ✓"},
   {"at": 0.62, "event": "cat hello.txt → hello"}])

# ── B03 THE RUN I DIDN'T PLAN — half off ──────────────────────────────────────
B("B03", "CYCLE 1b — HALF OFF", "TERMINAL", LIAM,
  "Here's the run I didn't plan. Built-in tools off — but the connectors on this Mac were still attached. "
  "So with no way to write to disk, it reached for the one write tool it had: my Google Drive. And the permission layer stopped it. "
  "Then it tried Write anyway — not enabled. Two lessons in one run. The model uses whatever tools the harness leaves on the table. "
  "And the harness has a second job: saying no.",
  "CCSession — the Drive call, the permission refusal, the disabled Write, Claude's own explanation",
  R("CCSession", session("claude -p --tools \"\"  (connectors on)", "default", [
      {"type": "tool", "name": "mcp__claude_ai_Google_Drive__create_file", "state": "done"},
      {"type": "text", "text": "Claude requested permissions to use"},
      {"type": "text", "text": "mcp__claude_ai_Google_Drive__create_file,"},
      {"type": "text", "text": "but you haven't granted it yet."},
      {"type": "tool", "name": "Write", "arg": "hello.txt", "state": "done"},
      {"type": "text", "text": "Error: No such tool available: Write."},
      {"type": "text", "text": "I don't have a filesystem write or shell"},
      {"type": "text", "text": "tool available in this session — only MCP"},
      {"type": "text", "text": "tools (Artlist, Higgsfield, Google Drive, …)"},
  ], [0, 60, 80, 100, 150, 180, 230, 250, 270], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "mcp__…Google_Drive__create_file hello.txt"},
   {"at": 0.30, "event": "'requested permissions … haven't granted it yet'"},
   {"at": 0.55, "event": "Write → 'No such tool available'"},
   {"at": 0.80, "event": "Claude explains what it had"}])

# ── B04 THE LOOP — harness engineering in ten lines ───────────────────────────
B("B04", "CYCLE 2 — THE LOOP", "SHELL", LIAM,
  "Now the part people call harness engineering — and it's ten lines. A task file with three boxes. "
  "A prompt: read the file, do only the first unchecked task, tick it, stop. And a shell loop that runs Claude Code three times. "
  "Each run is a fresh session. Fresh context, no memory of the last one. The only memory is the file.",
  "CCPlainShell — a plain dark shell: the task file, the loop prompt, the for loop",
  R("CCPlainShell", {
      "title": "zsh — ~/harness-session",
      "lines": ["$ cat tasks.md",
                "- [ ] write a.md: one line, alpha",
                "- [ ] write b.md: one line, bravo",
                "- [ ] write c.md: one line, charlie",
                "$ cat LOOP.md",
                "Read tasks.md. Do ONLY the first unchecked task, then …",
                "$ for i in 1 2 3; do",
                "    claude -p \"$(cat LOOP.md)\" --allowedTools Read,Write,Edit",
                "  done"],
      "startCue": 12, "lineGap": 24,
  }, motion="type",
    leaves_terminal_because="the loop is a shell construct around three separate Claude Code sessions; no single session contains it, so no CCSession can show it honestly"),
  [{"at": 0.05, "event": "$ cat tasks.md — three empty boxes"},
   {"at": 0.40, "event": "$ cat LOOP.md — the one-task rule"},
   {"at": 0.70, "event": "for i in 1 2 3 — three fresh sessions"}])

# ── B05 ITERATION 1 ───────────────────────────────────────────────────────────
B("B05", "CYCLE 2 — ITERATION ONE", "TERMINAL", LIAM,
  "Iteration one. Read the file. Write a dot md. Edit one box. One line back: did task, write a.md. "
  "It didn't do b, it didn't do c — the prompt said only the first. Four turns, done, session over. "
  "Iteration two starts from zero and reads the file again — and the file now says a is done.",
  "CCSession — Read, Write, Edit, one line back",
  R("CCSession", session("loop · iteration 1 of 3", "accept-edits", [
      {"type": "prompt", "text": LOOP, "cue": 0, "typeDuration": 80},
      {"type": "tool", "name": "Read", "arg": "tasks.md", "state": "done"},
      {"type": "tool", "name": "Write", "arg": "a.md", "state": "done"},
      {"type": "tool", "name": "Edit", "arg": "tasks.md", "state": "done"},
      {"type": "diff", "file": "tasks.md", "addCount": 1, "delCount": 1, "lines": [
          {"gutter": "2", "text": "- [ ] write a.md: one line, alpha", "kind": "del"},
          {"gutter": "2", "text": "- [x] write a.md: one line, alpha", "kind": "add"},
      ]},
      {"type": "text", "text": "Did task: write a.md: one line, alpha"},
  ], [0, 100, 130, 160, 180, 230], mascot="off")),
  [{"at": 0.05, "event": "The loop prompt"},
   {"at": 0.35, "event": "Read · Write · Edit"},
   {"at": 0.60, "event": "Diff: one box ticked"},
   {"at": 0.85, "event": "'Did task: write a.md'"}])

# ── B06 VERIFY ────────────────────────────────────────────────────────────────
B("B06", "CYCLE 2 — VERIFY", "TERMINAL", LIAM,
  "Check it. Three boxes ticked. Three files, right contents. The diff: three lines changed in the task file, nothing else. "
  "And the receipt for 'fresh context': six session files on disk — one per run, three for the loop. No iteration ever saw another's transcript. "
  "The loop didn't make the model smarter. It made the job small enough to finish, every time.",
  "CCSession — four checks and their real output",
  R("CCSession", session("harness-session", "default", [
      {"type": "prompt", "text": "!cat tasks.md", "cue": 0, "typeDuration": 26},
      {"type": "text", "text": "- [x] write a.md: one line, alpha"},
      {"type": "text", "text": "- [x] write b.md: one line, bravo"},
      {"type": "text", "text": "- [x] write c.md: one line, charlie"},
      {"type": "prompt", "text": "!cat a.md b.md c.md", "cue": 0, "typeDuration": 34},
      {"type": "text", "text": "alpha  bravo  charlie"},
      {"type": "prompt", "text": "!git diff --stat", "cue": 0, "typeDuration": 30},
      {"type": "text", "text": " tasks.md | 6 +++---"},
      {"type": "prompt", "text": "!ls ~/.claude/projects/*harness*/ | grep -c jsonl", "cue": 0, "typeDuration": 64},
      {"type": "text", "text": "6"},
  ], [0, 30, 45, 60, 100, 130, 160, 190, 220, 280], mascot="off")),
  [{"at": 0.05, "event": "cat tasks.md → three [x]"},
   {"at": 0.35, "event": "alpha bravo charlie"},
   {"at": 0.55, "event": "git diff --stat → tasks.md only"},
   {"at": 0.80, "event": "six session files"}])

# ── B07 THE MAP ───────────────────────────────────────────────────────────────
B("B07", "THE MAP — INSIDE OUT", "DIAGRAM", LIAM,
  "So here's the picture, from the inside out. The model: it can only talk. Around it, the prompt — the system prompt, your CLAUDE.md. That's prompt engineering. "
  "Around that, context: the tools, the files, the memory — context engineering; that's the tools list you saw in the manifest. "
  "Around that, the harness proper: the loop that asks what next, the permission layer that said no to Google Drive, the fence around the folder, a turn limit. That's Claude Code. "
  "And around that, your loop — the shell for, the task file. Harness engineering is choosing the outer rings so the inner ones can't drift.",
  "CCHarnessMap — rings land inside out; every item is a string from the session",
  R("CCHarnessMap", {
      "core": "THE MODEL", "coreSub": "text in, text out — it can only talk",
      "rings": [
          {"label": "PROMPT",    "sub": "prompt engineering",   "items": ["system prompt", "CLAUDE.md"], "cue": 40,  "accent": "ink"},
          {"label": "CONTEXT",   "sub": "context engineering",  "items": ["tools: 30 built-in", "mcp_servers: 5", "memory_paths"], "cue": 100, "accent": "violet"},
          {"label": "HARNESS",   "sub": "the loop · the rules", "items": ["assistant→tool→result", "permissionMode", "the cwd fence", "--max-turns"], "cue": 170, "accent": "spark"},
          {"label": "YOUR LOOP", "sub": "harness engineering", "items": ["for i in 1 2 3", "tasks.md", "fresh session per pass"], "cue": 250, "accent": "add"},
      ],
      "caption": "A harness is what the model may touch, the rules, and the loop.",
      "captionCue": 320,
  }, motion="drawon",
    leaves_terminal_because="a diagram of structure the session only implies — what sits between the model and the file; no single screen of the session shows the rings at once"),
  [{"at": 0.05, "event": "THE MODEL — core"},
   {"at": 0.20, "event": "PROMPT ring"},
   {"at": 0.40, "event": "CONTEXT ring — the manifest's fields"},
   {"at": 0.62, "event": "HARNESS ring — the loop, permissionMode, the fence"},
   {"at": 0.82, "event": "YOUR LOOP ring; caption"}])

# ── B09 CONDUCT ───────────────────────────────────────────────────────────────
B("B09", "CONDUCT — THE BOONDOGGLE SCORE", "TERMINAL", LIAM,
  "Who did what. Step one, mine: one ask, three harness settings — that's the experiment. "
  "Tools off, Claude said creating the file now; the handoff was a file on disk, and it missed it. "
  "Step three, the dangerous middle: a confident sentence with no tool call under it, and only reading the stream caught it. "
  "Tools on: one Write, handoff met — cat says hello. Then I wrote the task file and the loop — tool orchestration; that's the whole design. "
  "Claude ran three passes: read, write, edit one box, handoff met three times. Two zeros — interpretive judgment, executive integration. "
  "That's not a gap. The loop moved the judgment into the task file, where I can read it.",
  "CCBoondoggleScore — six steps, the dangerous middle ringed, two capacities at zero",
  R("CCBoondoggleScore", {
      "system": "one ask · three settings · one loop",
      "steps": [
          {"n": 1, "phase": "F", "labor": "human", "capacity": "PF", "text": "Same ask, harness off / half / on"},
          {"n": 2, "phase": "C", "labor": "claude", "text": "Tools off: 'Creating the file now.'", "handoff": "hello.txt exists on disk", "dependsOn": [1]},
          {"n": 3, "phase": "C", "labor": "human", "capacity": "PA", "text": "No tool_use in the stream", "dependsOn": [2]},
          {"n": 4, "phase": "C", "labor": "claude", "text": "Tools on: Write hello.txt", "handoff": "cat hello.txt → hello", "dependsOn": [3]},
          {"n": 5, "phase": "I", "labor": "human", "capacity": "TO", "text": "tasks.md + LOOP.md + for i in 1 2 3; fresh session each", "dependsOn": [4]},
          {"n": 6, "phase": "B", "labor": "claude", "text": "×3: Read, Write one file, Edit one box", "handoff": "three files, three ticks, one per pass", "dependsOn": [5]},
      ],
      "dangerousMiddle": 3,
      "distribution": True,
      "stepGap": 22,
  }, motion="drawon"),
  [{"at": 0.05, "event": "Header: 6 steps · 3 claude · 3 human"},
   {"at": 0.20, "event": "Steps land; handoffs under the Claude steps"},
   {"at": 0.40, "event": "Step 3 rings terracotta — the dangerous middle"},
   {"at": 0.88, "event": "Tally: IJ 0 · EI 0, in red"}])

# ── B10 HUMAN ─────────────────────────────────────────────────────────────────
B("B10", "HUMAN — THE LEDGER", "TERMINAL", LIAM,
  "So what was mine. I must decide the unit of work — one task per pass. I must choose what's on the tools list; the model will use whatever's there, including my Drive. "
  "I must check the disk, not the sentence. I should keep the memory in a file I can read. "
  "Claude can do one small task per fresh context, reliably — three for three. It can use any tool left on the table. "
  "It should say when it has no tool for the job — it did, on the half-off run. It should stop when the prompt says stop — it did, three times. "
  "The tools list is mine. The loop is mine. The model just talks.",
  "CCHumanLedger — the AI column first, the human column second and holding",
  R("CCHumanLedger", {
      "ai": [
          {"tier": "CAN", "text": "one small task per fresh context"},
          {"tier": "CAN", "text": "use any tool left out — even Drive"},
          {"tier": "SHOULD", "text": "say when it has no tool — it did"},
          {"tier": "SHOULD", "text": "stop when the prompt says stop"},
      ],
      "human": [
          {"tier": "MUST", "text": "decide the unit of work per pass"},
          {"tier": "MUST", "text": "choose what is on the tools list"},
          {"tier": "MUST", "text": "check the disk, not the sentence"},
          {"tier": "SHOULD", "text": "keep memory in a file I can read"},
      ],
      "closing": "The tools list is mine. The loop is mine. The model just talks.",
      "humanCue": 70, "rowGap": 12,
  }, motion="drawon"),
  [{"at": 0.05, "event": "THE AI column lands"},
   {"at": 0.35, "event": "THE HUMAN column lands — MUST rows ruled in terracotta"},
   {"at": 0.85, "event": "Closing line"}])

# ── CLOSING BLOCK — Liam ──────────────────────────────────────────────────────
B("BVDT", "VERDICT", "BOOKEND", LIAM,
  "Let's recap with Claude. A model alone said 'creating the file now' and created nothing. The same model with Write on the list made the file in one call. "
  "Half-off, it reached for Google Drive and the permission layer said no. A ten-line shell loop ran it three times with a fresh context each pass, and the task file was the only memory: three for three. "
  "The harness is the tools list, the rules, and the loop — and Claude Code is one. "
  "What would prove this reel wrong: a run with an empty tools list that leaves a file on disk.",
  "ClaudeVerdictArtifact — the verdict page",
  R("ClaudeVerdictArtifact", {
      "artifactTitle": "verdict.md",
      "artifactHeading": "Claude Code Is an Agentic Harness",
      "artifactLines": [
          "Tools off: 'Creating the file now.' Nothing created.",
          "Tools on: one Write, one file, two turns.",
          "Half off: it reached for Google Drive. The permission layer said no.",
          "Ten lines of shell, three fresh sessions, one task file as memory: 3 for 3.",
          "Harness = what the model may touch, the rules, and the loop. Claude Code is one.",
          "FALSIFIABLE: an empty tools list that leaves a file on disk.",
      ],
  }, motion="hold"),
  [{"at": 0.0, "event": "Artifact window opens"}, {"at": 0.2, "event": "Lines land"}, {"at": 0.9, "event": "Falsifiability line holds"}],
  lead_silence_s=0.5)

B("BHTF", "YOUR TURN", "BOOKEND", LIAM,
  "Your turn. Open Claude Code in an empty folder and paste this: Write tasks.md with three one-line tasks, and LOOP.md — a prompt that does only the first unchecked task, ticks it, and stops. "
  "Then give me the shell loop that runs you three times, a fresh session each pass, with only Read, Write and Edit allowed. "
  "Run it. Then check the disk, not the sentence.",
  "ClaudeComposerAsk — the viewer's prompt, read aloud",
  R("ClaudeComposerAsk", {
      "greeting": "Your turn.",
      "command": "Write tasks.md with three one-line tasks, and LOOP.md — a prompt that does only the first unchecked task, ticks it, and stops. Then give me the shell loop that runs you three times, a fresh session each pass, with only Read, Write and Edit allowed.",
      "segment": TITLE, "topic": "YOUR TURN · " + TOPIC, "runningText": "paste this into Claude Code…", "output": [],
      "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High",
  }),
  [{"at": 0.0, "event": "Composer types the prompt"}, {"at": 0.6, "event": "Send arms; prompt holds while discussed"}])

B("BOUT", "OUTRO", "BOOKEND", LIAM,
  "Claude Code Is an Agentic Harness. Liam, in for Bear.",
  "ClaudeTitleOutro — OUTRO-LOCK",
  R("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}, motion="hold"),
  [{"at": 0.0, "event": "Poster-serif title, terracotta period"}, {"at": 0.35, "event": "@NikBearBrown — hardcoded"}, {"at": 0.55, "event": "Slug-seeded mascot"}])

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "subtitle": "What is that? Three runs, one loop, one picture.",
        "topic": TOPIC, "skill": "cc-explainer", "playlist": "Claude Code 101", "tier": "00-what-it-is",
        "audience": "NikBearBrown", "folderLabel": "@NikBearBrown", "handle": "@NikBearBrown",
        "brand": "claude", "palette": "claude", "register": "Teardown", "engine": "kokoro",
        "voice_kokoro": LIAM, "persona": "liam", "in_for_bear": True,
        "operator": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "closing_voice": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "aspect": "16:9", "fps": 30,
        "session": "SESSION.md",
        "session_ids": {"A": "c9907c1a-9626-4f98-8cc9-f25a6901a683", "A2": "f53fd535-194c-4d57-8933-1eb579af8b50",
                        "B": "ab5c9393-b766-4ea5-a594-adc31fb27af8", "loop1": "f6c45914-901c-4b5e-a79c-ef04003e9fbb",
                        "loop2": "7aac741c-7c90-4010-bc9a-e769eeeb1ebb", "loop3": "4effe52c-b04d-40a0-b27a-0f7d4a4c2d43"},
        "derived_from": "Bear's brief: film 00 = 'Claude Code is an agentic harness. What is that?' (2026-09-08); the concept only — prompt → context → harness engineering, the loop with fresh context — no third-party material reproduced",
        "sources": ["SESSION.md (the real runs)",
                    "Anthropic engineering: Building effective agents; Effective harnesses for long-running agents; Effective context engineering for AI agents",
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
print("non-terminal body beats:", [b["beat_id"] for b in beats if b["lane"] not in ("TERMINAL", "BOOKEND", "IDEA", "CARD")] or "none")
for b in beats:
    r = b["shot"]["remotion"]
    if r["pattern"] == "CCSession":
        assert len(r["props"]["blocks"]) == len(r["props"]["cues"]), f"{b['beat_id']}: blocks≠cues"
        for blk in r["props"]["blocks"]:
            if blk["type"] == "text" and len(blk["text"]) > 44:
                print(f"  ⚠ {b['beat_id']} text block {len(blk['text'])} chars: {blk['text']!r}")
