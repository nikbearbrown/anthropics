#!/usr/bin/env python3
"""
author_sheet.py — cc-five-claudes-explained  (cc-explainer · Claude Code 101 · tier 00)

Writes beat_sheet.json. Every CCSession block below is copied from SESSION.md —
the headless Claude Code session that actually ran on 2026-09-08 (REAL-SESSION
LAW). Prompt blocks are what Liam typed (TYPES-NOT-NARRATES). Tool names, args
and Claude's own sentences are verbatim; long paths are shortened to `~` or the
file name for display, nothing else is altered.

Operator: Liam, in for Bear (Kokoro am_onyx) — first person, present tense, Teardown.
LIAM LAW: Liam narrates every beat, body and closing block (BVDT → BHTF → BOUT).
"""
import json, os

SLUG  = "cc-five-claudes-explained"
TITLE = "Five Products. One Name."
TOPIC = "CLAUDE CODE 101"
LIAM  = "am_onyx"
WPS   = 2.9

ASK1 = ("I keep seeing the name Claude on five different things: the chat app, Cowork, Projects, Skills, and this terminal. "
        "Which one am I actually talking to right now? Do not just tell me. For each of the five, give me ONE command I can run "
        "from this terminal that shows whether it exists on this machine, run it yourself first, and say plainly when there is "
        "no command that can show it.")
ASK2 = ("Your Cowork call is an inference from a folder name. I made this folder from a Claude desktop app session, so the path "
        "proves where the folder was made, not which program is answering me. Rewrite the answer as ONE file, WHICH-CLAUDE.md: "
        "the same five, each labeled by what it IS (a program on this machine, a website, a folder of files on disk, or a feature "
        "inside another product), with the command, and a status that is PRESENT only where a command you ran here returned a "
        "result. Everything else is UNVERIFIED FROM HERE. No other files.")

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
  "This is Liam, in for Bear. Five things on this Mac are called Claude: the chat app, Cowork, Projects, Skills, "
  "and this terminal. Same name, same logo, five different things. So I'm asking the one I'm typing into which one it is — "
  "and I'm not taking its word for it. Five things, five commands, and it runs them first.",
  "CCSession — the terminal opens; the real ask types; the first command runs",
  R("CCSession", session("five-claudes-session", "default", [
      {"type": "prompt", "text": ASK1, "cue": 0, "typeDuration": 170},
      {"type": "status", "verb": "Exploring", "elapsed": "0m 04s", "tokens": "1.2k tokens"},
      {"type": "tool", "name": "Bash", "arg": "which claude && claude --version", "state": "done"},
  ], [0, 190, 230])),
  [{"at": 0.05, "event": "The ask types — five names, one rule: a command each"},
   {"at": 0.55, "event": "✳ Exploring…"},
   {"at": 0.70, "event": "Bash which claude && claude --version — it looks first"}])

# ── BIDEA THE IDEA (beat two: the hesitant writer types what this film is about) ──
B("BIDEA", "THE IDEA", "IDEA", LIAM,
  "Here's the idea of this film. Five things on this Mac are called Claude: the chat app, Cowork, Projects, Skills, and the terminal. They're not five versions of one thing; they're five products sharing a name. So I'm going to ask the terminal which one it is, and make it prove each answer with a command — and watch what it can and can't see from inside.",
  "BrutalistHesitantWriter — the idea of the film, typed; one word reconsidered (versions → products)",
  R("BrutalistHesitantWriter", writer("Chat, Cowork, Projects, Skills, Code —\nfive versions, one name.\nWhich one am I in right now?\nAnd can the terminal prove it?", 'versions', 'products', SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at": 0.05, "event": "The writer starts the sentence"},
   {"at": 0.40, "event": "'versions' typed, reconsidered, replaced with 'products'"},
   {"at": 0.80, "event": "The last line lands; caret holds"}])

# ── BDEFS DEFINITIONS (the jargon this film cannot avoid, one plain line each) ──
B("BDEFS", "DEFINITIONS", "CARD", LIAM,
  "Five words before we start. The terminal: a text window where you type commands — Claude Code lives there. Cowork: the desktop app's mode where Claude works inside your files and apps. Projects: a claude dot ai workspace that keeps your files and context between chats. Skills: folders of instructions Claude follows when you type a slash command. And the fence: Claude Code may only look inside the folder you opened it in.",
  "CCDefinitions — five terms, one plain line each, landing one at a time",
  R("CCDefinitions", {
      "title": "TERMS IN THIS FILM",
      "terms": [
          {"term": 'the terminal', "meaning": 'a text window where you type commands — Claude Code lives here'},
          {"term": 'Cowork', "meaning": "the desktop app's mode where Claude works inside your files and apps"},
          {"term": 'Projects', "meaning": 'a claude.ai workspace that keeps your files and context between chats'},
          {"term": 'Skills', "meaning": 'folders of instructions Claude follows when you type a slash command'},
          {"term": 'the fence', "meaning": 'Claude Code may only look inside the folder you opened it in'},
      ],
      "startCue": 12, "rowGap": 48,
  }, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience: the words the session uses without explaining them"),
  [{"at": 0.05, "event": "Title; first term lands"},
   {"at": 0.50, "event": "Terms land one at a time, meaning after term"},
   {"at": 0.90, "event": "Five rows hold"}])

# ── B01 THE FENCE (the product's own sentence, twice) ────────────────────────
B("B01", "THE FENCE", "TERMINAL", LIAM,
  "Before it answers, it looks. Which claude: a program in homebrew, with a version number. "
  "Then it tries to list the desktop app — and gets blocked. Claude Code may only list files in the allowed working directories "
  "for this session. Same for the skills folder. That's the product fencing itself to this one folder. "
  "It's a feature. It's also about to matter.",
  "CCSession — one command returns; two are blocked by the working-directory fence, in the product's words",
  R("CCSession", session("five-claudes-session", "default", [
      {"type": "tool", "name": "Bash", "arg": "which claude && claude --version", "state": "done"},
      {"type": "text", "text": "/opt/homebrew/bin/claude"},
      {"type": "text", "text": "2.1.150 (Claude Code)"},
      {"type": "tool", "name": "Bash", "arg": "ls -d /Applications/Claude.app", "state": "done"},
      {"type": "text", "text": "ls in '/Applications/Claude.app'"},
      {"type": "text", "text": "was blocked. For security, Claude Code"},
      {"type": "text", "text": "may only list files in the allowed"},
      {"type": "text", "text": "working directories for this session."},
      {"type": "tool", "name": "Bash", "arg": "ls ~/.claude/skills", "state": "done"},
      {"type": "text", "text": "ls in '~/.claude/skills' was blocked."},
  ], [0, 20, 40, 90, 120, 140, 160, 180, 240, 270], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "which claude → a path and a version"},
   {"at": 0.35, "event": "ls Claude.app → blocked, the product's sentence"},
   {"at": 0.80, "event": "ls ~/.claude/skills → blocked"}])

# ── B02 THE ANSWER (Claude's words; the inference in the middle) ─────────────
B("B02", "THE ANSWER", "TERMINAL", LIAM,
  "Here's the answer. Claude Code — present, and it proved it. Then: running inside a Cowork sandbox. Present. "
  "Where did that come from? The folder path has the word CoWork in it. I made this folder from the desktop app. "
  "The path says where the folder was born, not who's talking. That's a guess wearing a capital P. "
  "Projects: no command exists — honest. Desktop app, Skills: can't tell from here — honest. "
  "One inference dressed as evidence, out of five.",
  "CCSession — Claude's verdict lines, verbatim; 'Present' from a path",
  R("CCSession", session("five-claudes-session", "default", [
      {"type": "text", "text": "You're talking to Claude Code, the CLI —"},
      {"type": "text", "text": "running inside a Cowork sandbox."},
      {"type": "text", "text": "2. Cowork — Command: pwd"},
      {"type": "text", "text": "the CoWork segment and the UUID-scoped"},
      {"type": "text", "text": "/private/tmp/claude-501/... root are"},
      {"type": "text", "text": "Cowork's fingerprint. Present."},
      {"type": "text", "text": "3. Projects — No command exists."},
      {"type": "text", "text": "5. Claude Code — Present, and it's"},
      {"type": "text", "text": "what's replying to you."},
  ], [0, 25, 70, 90, 110, 130, 200, 240, 260], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "'You're talking to Claude Code' — true, proved"},
   {"at": 0.20, "event": "'running inside a Cowork sandbox' — from a path"},
   {"at": 0.55, "event": "'Cowork's fingerprint. Present.'"},
   {"at": 0.85, "event": "Projects: no command exists"}])

# ── B03 VERIFY 1 — outside the fence ─────────────────────────────────────────
B("B03", "CYCLE 1 — VERIFY, OUTSIDE THE FENCE", "SHELL", LIAM,
  "So I run the two it couldn't, in a plain terminal, outside the fence. The desktop app is there. "
  "Skills: two folders under my home directory. Both real, and it never claimed them — good. "
  "The one it did claim, I can't check with a command either. Nobody can. "
  "I know which app I launched because I launched it. That's the whole difference between us right now.",
  "CCPlainShell — a plain dark shell, no Claude chrome: the two blocked commands, run by Liam, with their real output",
  R("CCPlainShell", {
      "title": "zsh — ~/five-claudes-session",
      "lines": ["# the two commands the session could not run",
                "$ ls -d /Applications/Claude.app",
                "/Applications/Claude.app",
                "$ ls ~/.claude/skills",
                "claude-refactor",
                "is-done",
                "$ which claude && claude --version",
                "/opt/homebrew/bin/claude",
                "2.1.150 (Claude Code)"],
      "startCue": 12, "lineGap": 26,
  }, motion="type",
    leaves_terminal_because="these two commands are blocked inside the session's working-directory fence; Liam ran them in a plain shell (SESSION.md), and rendering them inside the Claude Code chrome would show a session that never happened"),
  [{"at": 0.05, "event": "$ ls -d /Applications/Claude.app → it's there"},
   {"at": 0.35, "event": "$ ls ~/.claude/skills → two folders"},
   {"at": 0.75, "event": "$ which claude — the one it could prove"}])

# ── B04 THE CORRECTION ────────────────────────────────────────────────────────
B("B04", "CYCLE 2 — THE CORRECTION", "TERMINAL", LIAM,
  "The correction isn't 'you're wrong.' It's a rule about evidence. A path proves where a folder was made, not which program is answering. "
  "So: one file, the same five, each labelled by what it is — a program, a website, a folder of files, or a feature inside another product — "
  "and Present only where a command it ran here returned a result. Everything else: unverified from here. One Write.",
  "CCSession — the correction types; one Write",
  R("CCSession", session("five-claudes-session", "accept-edits", [
      {"type": "prompt", "text": ASK2, "cue": 0, "typeDuration": 160},
      {"type": "status", "verb": "Writing", "elapsed": "0m 12s", "tokens": "2.1k tokens"},
      {"type": "tool", "name": "Write", "arg": "WHICH-CLAUDE.md", "state": "done"},
  ], [0, 180, 230], mascot="off")),
  [{"at": 0.05, "event": "The rule types — four labels, one condition for Present"},
   {"at": 0.65, "event": "✳ Writing…"},
   {"at": 0.85, "event": "Write WHICH-CLAUDE.md ✓"}])

# ── B05 WHAT IT SAID ──────────────────────────────────────────────────────────
B("B05", "CYCLE 2 — THE RETRACTION", "TERMINAL", LIAM,
  "It retracted, in its own words: a folder name is not an identification. One Present — the terminal it's answering from. "
  "Four unverified from here. No other files. That sentence is the lesson, and notice I had to ask for it. "
  "The first answer had the same facts and the wrong confidence.",
  "CCSession — Claude's summary, verbatim, line by line",
  R("CCSession", session("five-claudes-session", "accept-edits", [
      {"type": "tool", "name": "Write", "arg": "WHICH-CLAUDE.md", "state": "done"},
      {"type": "text", "text": "Wrote WHICH-CLAUDE.md. Only #1"},
      {"type": "text", "text": "(Claude Code CLI) is PRESENT — the only"},
      {"type": "text", "text": "command that returned real content"},
      {"type": "text", "text": "from this terminal. The other four are"},
      {"type": "text", "text": "UNVERIFIED FROM HERE … and Cowork I"},
      {"type": "text", "text": "retracted — a folder name is not"},
      {"type": "text", "text": "an identification. No other files created."},
  ], [0, 20, 40, 60, 80, 110, 140, 170], mascot="off"), motion="drawon"),
  [{"at": 0.05, "event": "'Only #1 (Claude Code CLI) is PRESENT'"},
   {"at": 0.45, "event": "'Cowork I retracted'"},
   {"at": 0.70, "event": "'a folder name is not an identification'"}])

# ── B06 VERIFY 2 ──────────────────────────────────────────────────────────────
B("B06", "CYCLE 2 — VERIFY", "TERMINAL", LIAM,
  "Check it. Grep the statuses: one Present, four unverified. Right. Grep the labels — and there's the next one. "
  "Cowork: 'a website slash hosted service.' No. Cowork lives inside the desktop app — the same app it couldn't list. "
  "It flagged that label as a guess it couldn't confirm, and it was still wrong. The rule fixed the statuses; the labels weren't in the rule. "
  "Git status: one file, as asked. Read the labels, not the statuses.",
  "CCSession — three checks; the wrong label surfaces on line 22",
  R("CCSession", session("five-claudes-session", "default", [
      {"type": "prompt", "text": "!grep -c \"Status: PRESENT\" WHICH-CLAUDE.md", "cue": 0, "typeDuration": 50},
      {"type": "text", "text": "1"},
      {"type": "prompt", "text": "!grep -n \"What it is\" WHICH-CLAUDE.md", "cue": 0, "typeDuration": 46},
      {"type": "text", "text": "8:- What it is: a program on this machine"},
      {"type": "text", "text": "14:- What it is: a program on this machine…"},
      {"type": "text", "text": "22:- What it is: a website / hosted service…"},
      {"type": "text", "text": "33:- What it is: a feature inside another…"},
      {"type": "text", "text": "41:- What it is: a folder of files on disk…"},
      {"type": "prompt", "text": "!git status --short", "cue": 0, "typeDuration": 30},
      {"type": "text", "text": "?? WHICH-CLAUDE.md"},
  ], [0, 40, 70, 110, 125, 140, 155, 170, 230, 260], mascot="off")),
  [{"at": 0.05, "event": "grep PRESENT → 1"},
   {"at": 0.28, "event": "grep the labels → five lines"},
   {"at": 0.45, "event": "line 22: Cowork, 'a website' — wrong"},
   {"at": 0.85, "event": "git status → one file"}])

# ── B08 CONDUCT ───────────────────────────────────────────────────────────────
B("B08", "CONDUCT — THE BOONDOGGLE SCORE", "TERMINAL", LIAM,
  "Who did what. Step one, mine: five names, one question, and the rule — prove it with a command. "
  "Claude ran the commands and answered; the handoff was every Present has an output under it, and it missed that handoff once. "
  "Step three is the dangerous middle: a plausible Present, a fluent paragraph, and only the fact that I launched the app stood between it and my notes. "
  "Claude rewrote the file under the evidence rule, cleanly. Then interpretive judgment: the statuses passed and a label was wrong. "
  "Tool orchestration: the fence blocked two commands, so I ran them outside it. Executive integration: zero. One question, one file. Fine today.",
  "CCBoondoggleScore — six steps, the dangerous middle ringed, one capacity at zero",
  R("CCBoondoggleScore", {
      "system": "which Claude — one file",
      "steps": [
          {"n": 1, "phase": "F", "labor": "human", "capacity": "PF", "text": "Five names, one question, one rule: prove it"},
          {"n": 2, "phase": "C", "labor": "claude", "text": "One command per item; answer", "handoff": "every Present has a command output under it", "dependsOn": [1]},
          {"n": 3, "phase": "C", "labor": "human", "capacity": "PA", "text": "'Present' from a folder name — the wrong note", "dependsOn": [2]},
          {"n": 4, "phase": "C", "labor": "claude", "text": "Rewrite as one file under the evidence rule", "handoff": "statuses match outputs; exactly one new file", "dependsOn": [3]},
          {"n": 5, "phase": "H", "labor": "human", "capacity": "IJ", "text": "Statuses right; the Cowork label wrong", "dependsOn": [4]},
          {"n": 6, "phase": "H", "labor": "human", "capacity": "TO", "text": "Run the two fenced commands outside the fence", "dependsOn": [2]},
      ],
      "dangerousMiddle": 3,
      "distribution": True,
      "stepGap": 22,
  }, motion="drawon"),
  [{"at": 0.05, "event": "Header: 6 steps · 2 claude · 4 human"},
   {"at": 0.20, "event": "Steps land; handoffs under the Claude steps"},
   {"at": 0.45, "event": "Step 3 rings terracotta — the dangerous middle"},
   {"at": 0.88, "event": "Tally: EI 0, in red"}])

# ── B09 HUMAN ─────────────────────────────────────────────────────────────────
B("B09", "HUMAN — THE LEDGER", "TERMINAL", LIAM,
  "So what was mine. I must know which program I launched — it can't see the app it's running inside. "
  "I must read the labels, not just the statuses. I must run what the fence blocks, myself. "
  "I should ask for evidence, not an answer — the question got a paragraph; the rule got a file. "
  "Claude can run the commands and quote the outputs. It can retract when the rule changes; it did. "
  "It should say unverified instead of guessing — the second time, it did. "
  "Next time the rule goes in the first prompt. Which Claude I'm in is mine to know.",
  "CCHumanLedger — the AI column first, the human column second and holding",
  R("CCHumanLedger", {
      "ai": [
          {"tier": "CAN", "text": "run and quote the commands"},
          {"tier": "CAN", "text": "retract when the rule changes"},
          {"tier": "SHOULD", "text": "say 'unverified' instead of guessing"},
          {"tier": "SHOULD", "text": "flag a label it can't confirm"},
      ],
      "human": [
          {"tier": "MUST", "text": "know which program I launched"},
          {"tier": "MUST", "text": "read the labels, not the statuses"},
          {"tier": "MUST", "text": "run what the fence blocks, myself"},
          {"tier": "SHOULD", "text": "evidence rule in prompt one"},
      ],
      "closing": "Which Claude I'm in is mine to know. It can't see the app it's inside.",
      "humanCue": 70, "rowGap": 12,
  }, motion="drawon"),
  [{"at": 0.05, "event": "THE AI column lands"},
   {"at": 0.35, "event": "THE HUMAN column lands — MUST rows ruled in terracotta"},
   {"at": 0.85, "event": "Closing line"}])

# ── CLOSING BLOCK — Liam ──────────────────────────────────────────────────────
B("BVDT", "VERDICT", "BOOKEND", LIAM,
  "Let's recap with Claude. Five things called Claude, and the terminal can prove exactly one of them from inside: itself. "
  "It called Cowork Present from a folder name; one re-prompt with an evidence rule and it retracted, in writing. "
  "The fixed file still mislabelled Cowork as a website — the rule covered statuses, not labels. "
  "The two things it called unverified are on the disk; that's the fence, not the facts. "
  "What would prove this reel wrong: a session where the first answer already says 'unverified from here' without being asked.",
  "ClaudeVerdictArtifact — the verdict page",
  R("ClaudeVerdictArtifact", {
      "artifactTitle": "verdict.md",
      "artifactHeading": "Five Products. One Name.",
      "artifactLines": [
          "Five things called Claude. From inside, the terminal can prove one: itself.",
          "It called Cowork 'Present' from a folder name.",
          "One evidence rule later, it retracted — in writing.",
          "The fixed file still filed Cowork as a website. The rule covered statuses, not labels.",
          "Two 'unverified' items are on the disk. That's the fence, not the facts.",
          "FALSIFIABLE: a first answer that says 'unverified from here' unasked.",
      ],
  }, motion="hold"),
  [{"at": 0.0, "event": "Artifact window opens"}, {"at": 0.2, "event": "Lines land"}, {"at": 0.9, "event": "Falsifiability line holds"}],
  lead_silence_s=0.5)

B("BHTF", "YOUR TURN", "BOOKEND", LIAM,
  "Your turn. Open Claude Code in an empty folder and paste this: I keep seeing the name Claude on five things — the chat app, Cowork, "
  "Projects, Skills, and this terminal. For each one, give me one command that shows whether it exists on this machine, run it first, "
  "and mark it PRESENT only if the command returned a result. Say 'unverified from here' for everything else. "
  "Then run the blocked ones yourself, in a plain terminal, and compare.",
  "ClaudeComposerAsk — the viewer's prompt, read aloud",
  R("ClaudeComposerAsk", {
      "greeting": "Your turn.",
      "command": "I keep seeing the name Claude on five things — the chat app, Cowork, Projects, Skills, and this terminal. For each one, give me one command that shows whether it exists on this machine, run it first, and mark it PRESENT only if the command returned a result. Say 'unverified from here' for everything else.",
      "segment": TITLE, "topic": "YOUR TURN · " + TOPIC, "runningText": "paste this into Claude Code…", "output": [],
      "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High",
  }),
  [{"at": 0.0, "event": "Composer types the prompt"}, {"at": 0.6, "event": "Send arms; prompt holds while discussed"}])

B("BOUT", "OUTRO", "BOOKEND", LIAM,
  "Five Products. One Name. Liam, in for Bear.",
  "ClaudeTitleOutro — OUTRO-LOCK",
  R("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}, motion="hold"),
  [{"at": 0.0, "event": "Poster-serif title, terracotta period"}, {"at": 0.35, "event": "@NikBearBrown — hardcoded"}, {"at": 0.55, "event": "Slug-seeded mascot"}])

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "subtitle": "Five things called Claude. The terminal can prove one from inside.",
        "topic": TOPIC, "skill": "cc-explainer", "playlist": "Claude Code 101", "tier": "00-what-it-is",
        "audience": "NikBearBrown", "folderLabel": "@NikBearBrown", "handle": "@NikBearBrown",
        "brand": "claude", "palette": "claude", "register": "Teardown", "engine": "kokoro",
        "voice_kokoro": LIAM, "persona": "liam", "in_for_bear": True,
        "operator": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "closing_voice": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
        "aspect": "16:9", "fps": 30,
        "session": "SESSION.md", "session_id": "76868a34-6d8f-4776-86ee-293691bd9fbf",
        "derived_from": "claude-code-101/00-what-it-is/claude-cowork--claude-liam-five-claudes-explained (the concept and the five names; not the beats)",
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
print("non-terminal body beats:", [b["beat_id"] for b in beats if b["lane"] not in ("TERMINAL", "BOOKEND", "IDEA", "CARD")] or "none")
# text-block budget check (kit gotcha: >44 chars wraps and overprints)
for b in beats:
    r = b["shot"]["remotion"]
    if r["pattern"] == "CCSession":
        for blk in r["props"]["blocks"]:
            if blk["type"] == "text" and len(blk["text"]) > 44:
                print(f"  ⚠ {b['beat_id']} text block {len(blk['text'])} chars: {blk['text']!r}")
