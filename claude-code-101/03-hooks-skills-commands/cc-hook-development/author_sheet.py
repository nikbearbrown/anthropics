#!/usr/bin/env python3
"""author_sheet.py — cc-hook-development (cc-explainer · Claude Code 101 · tier 03).
"Claude, Hook Development." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG = "cc-hook-development"
TITLE = "Claude, Hook Development."
TOPIC = "CLAUDE CODE 101"
LIAM = "am_onyx"
WPS = 2.9
ASK = "Add a bullet under the '## Notes' section of target.md saying: 'Reviewed 2026-09-10 by Liam.' Nothing else."
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
    return {"text": text, "triggerWords": trig, "replacementWords": rep,
            "face": "serif", "fontSize": 78, "align": "center",
            "ink": "#F2F0E9", "accent": "#D97757", "bg": "#1F1E1B", "seed": seed,
            "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
            "mistakeRate": 5, "jitter": 20}


def session(title, mode, blocks, cues, mascot="off"):
    return {"title": title, "mode": mode, "blocks": blocks, "cues": cues, "mascot": mascot}


B("B00", "COLD OPEN — BARE", "TERMINAL", LIAM,
  "This is Liam, in for Bear. One sentence, an ordinary edit — add a bullet to target.md. Watch what leaves behind. "
  "Read, Edit, done. Three turns, fifteen seconds. And no receipt. Nothing outside the model observed the edit. "
  "If somebody asks tomorrow what Claude changed this week, my answer is: I trust it. That's not an answer.",
  "CCSession — the bare run: ls, Read, Edit, 'Added the bullet' — no log exists after",
  R("CCSession", session("scratch — bare", "accept-edits", [
      {"type": "prompt", "text": ASK, "cue": 0, "typeDuration": 70},
      {"type": "tool", "name": "Bash", "arg": "ls target.md", "state": "done"},
      {"type": "tool", "name": "Read", "arg": "target.md", "state": "done"},
      {"type": "tool", "name": "Edit", "arg": "target.md", "state": "done"},
      {"type": "text", "text": "Added the bullet under `## Notes`."},
  ], [0, 90, 130, 170, 210], mascot="off")),
  [{"at": 0.05, "event": "The ask types"}, {"at": 0.55, "event": "Edit lands"},
   {"at": 0.85, "event": "no receipt anywhere"}])

B("BIDEA", "THE IDEA", "IDEA", LIAM,
  "Here's the idea of this film. A hook isn't magic. It's a shell command Claude Code runs at a lifecycle moment — "
  "after a Write, before a Bash, at the start of a session. Wire the shape right and it fires every time. "
  "The interesting part isn't the script. The interesting part is which two lines Claude can draft, and which two lines only you can sign.",
  "BrutalistHesitantWriter — 'magic' reconsidered into 'wired'",
  R("BrutalistHesitantWriter",
    writer("A hook feels like magic.\nIt is not magic.\nIt is a shell command at a moment.\nSome lines you sign, not Claude.",
           "magic", "wired", SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at": 0.05, "event": "Writer starts"}, {"at": 0.25, "event": "'magic' → 'wired'"},
   {"at": 0.85, "event": "Last line"}])

B("BDEFS", "DEFINITIONS", "CARD", LIAM,
  "Five words before we start. Hook: a shell command Claude Code runs at a lifecycle moment. "
  "PostToolUse: fires after a tool call succeeds — it can log, it can't stop. "
  "PreToolUse: fires before — exit two rejects the call and hands Claude the reason. Different event, different contract. "
  "Matcher: a regex over the tool name — which tool calls trigger the hook. "
  "settings dot local dot json: the file that wires it in. The one file Claude Code will not let Claude edit.",
  "CCDefinitions — five terms",
  R("CCDefinitions", {"title": "TERMS IN THIS FILM", "terms": [
      {"term": "hook", "meaning": "a shell command Claude Code runs at a lifecycle moment"},
      {"term": "PostToolUse", "meaning": "fires after a tool call succeeds — can log, can't stop"},
      {"term": "PreToolUse", "meaning": "fires before — exit 2 rejects the call and hands Claude the reason"},
      {"term": "matcher", "meaning": "a regex over the tool name — which calls trigger the hook"},
      {"term": "settings.local.json", "meaning": "the file that wires the hook in — Claude cannot edit it"}],
      "startCue": 12, "rowGap": 48},
    motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience"),
  [{"at": 0.05, "event": "First term"}, {"at": 0.5, "event": "Terms land"}, {"at": 0.9, "event": "Hold"}])

B("B01", "DRAFT — CLAUDE WRITES THE SCRIPT", "TERMINAL", LIAM,
  "Fresh folder. I ask Claude for a PostToolUse hook that logs every Write, Edit, and MultiEdit to a file. "
  "Two files, I said: the bash script and the settings that wire it. Don't test it. Just write them. "
  "Twenty seconds later, one file on disk: hooks slash log dash write dot sh. Read stdin, extract tool name and file path, "
  "append UTC and tool and path to hooks dash log slash writes dot log. Twenty lines. It's fine.",
  "CCSession — draft run: pwd, ls, Write log-write.sh, chmod",
  R("CCSession", session("scratch — draft", "accept-edits", [
      {"type": "prompt", "text": "Draft a PostToolUse hook that logs every", "cue": 0, "typeDuration": 60},
      {"type": "prompt", "text": "Write, Edit, MultiEdit. Two files. Don't test.", "cue": 0, "typeDuration": 60},
      {"type": "tool", "name": "Bash", "arg": "pwd && ls -la", "state": "done"},
      {"type": "tool", "name": "Bash", "arg": "ls -la .claude/ hooks/", "state": "done"},
      {"type": "tool", "name": "Write", "arg": "hooks/log-write.sh", "state": "done"},
      {"type": "tool", "name": "Bash", "arg": "chmod +x hooks/log-write.sh", "state": "done"},
  ], [0, 40, 90, 130, 170, 220], mascot="off")),
  [{"at": 0.1, "event": "The ask"}, {"at": 0.55, "event": "Write log-write.sh"},
   {"at": 0.9, "event": "chmod +x — done"}])

B("B02", "DRAFT — THE WALL", "TERMINAL", LIAM,
  "Then Claude tries to write the second file. dot claude slash settings dot local dot json. Blocked. "
  "Not because it did something wrong — because of what settings can do. A setting can grant Claude tools. "
  "Claude retried the same Write. Blocked. Tried a bash heredoc. Blocked as brace-quoted expansion. Tried a printf fallback. Blocked, same message. "
  "Four attempts. Four blocks. Then Claude gave up and printed the JSON in the chat for me to paste.",
  "CCSession — draft run: four blocked Writes, Claude gives up",
  R("CCSession", session("scratch — draft", "accept-edits", [
      {"type": "tool", "name": "Write", "arg": ".claude/settings.local.json", "state": "done"},
      {"type": "text", "text": "ERROR: permission not granted."},
      {"type": "tool", "name": "Write", "arg": ".claude/settings.local.json", "state": "done"},
      {"type": "text", "text": "ERROR: permission not granted."},
      {"type": "tool", "name": "Bash", "arg": "cat > .claude/settings.local.json", "state": "done"},
      {"type": "text", "text": "ERROR: brace with quote."},
      {"type": "tool", "name": "Bash", "arg": "printf %s\\n { \"hooks\": …", "state": "done"},
      {"type": "text", "text": "ERROR: permission not granted."},
      {"type": "text", "text": "I've stopped retrying. Paste this in."},
  ], [0, 40, 70, 110, 140, 200, 230, 290, 320], mascot="off")),
  [{"at": 0.05, "event": "First blocked Write"}, {"at": 0.55, "event": "Third fallback fails"},
   {"at": 0.9, "event": "Claude gives up"}])

B("B03", "THE HUMAN WIRING", "SHELL", LIAM,
  "So I write it. Fifteen lines, mine. hooks, PostToolUse, matcher Write pipe Edit pipe MultiEdit, "
  "command bash hooks slash log dash write dot sh. That's the wire. "
  "The matcher is a regex over the tool name. The command is what Claude Code shells out to after any matching tool call succeeds. "
  "This is the part only I can sign — because a settings file can hand Claude tools, and nobody hands themselves tools.",
  "CCPlainShell — cat the wired settings.local.json",
  R("CCPlainShell", {"title": "zsh — scratch/.claude", "lines": [
      "$ cat .claude/settings.local.json",
      "{",
      "  \"hooks\": {",
      "    \"PostToolUse\": [",
      "      {",
      "        \"matcher\": \"Write|Edit|MultiEdit\",",
      "        \"hooks\": [",
      "          { \"type\": \"command\",",
      "            \"command\": \"bash hooks/log-write.sh\" }",
      "        ]",
      "      }",
      "    ]",
      "  }",
      "}"],
      "startCue": 8, "lineGap": 22},
    motion="type",
    leaves_terminal_because="the file is read in a plain shell before the next session; no session contains this cat"),
  [{"at": 0.05, "event": "cat"}, {"at": 0.5, "event": "matcher line"}, {"at": 0.9, "event": "command line"}])

B("B04", "SMOKE TEST — VERIFY", "TERMINAL", LIAM,
  "Before I put a real session on this, I pipe three payloads to the script by hand. "
  "A Write to slash tmp — exit zero, one log line. An Edit on target — exit zero, one log line. "
  "A Bash payload — exit zero, an empty third column. The script logs anything piped to it. "
  "That's on purpose. The matcher in settings decides which tool names call the script. The script itself stays defensive.",
  "CCSession — smoke test on the hook script: three payloads, three exit 0s, log file",
  R("CCSession", session("scratch — smoke test", "default", [
      {"type": "prompt", "text": "!echo Write payload | bash log-write.sh", "cue": 0, "typeDuration": 60},
      {"type": "text", "text": "exit=0"},
      {"type": "prompt", "text": "!echo Edit payload | bash log-write.sh", "cue": 0, "typeDuration": 60},
      {"type": "text", "text": "exit=0"},
      {"type": "prompt", "text": "!echo Bash payload | bash log-write.sh", "cue": 0, "typeDuration": 60},
      {"type": "text", "text": "exit=0"},
      {"type": "prompt", "text": "!cat hooks-log/writes.log", "cue": 0, "typeDuration": 46},
      {"type": "text", "text": "…Z  Write  /tmp/foo.md"},
      {"type": "text", "text": "…Z  Edit   target.md"},
      {"type": "text", "text": "…Z  Bash"},
  ], [0, 45, 80, 120, 155, 195, 230, 265, 285, 305], mascot="off")),
  [{"at": 0.1, "event": "Write payload"}, {"at": 0.5, "event": "Bash payload — empty column"},
   {"at": 0.85, "event": "the log"}])

B("B05", "FIRES — THE REAL SESSION", "TERMINAL", LIAM,
  "Fresh headless session. Same ask I opened the film with — add the bullet to target dot md. "
  "Read. Edit. Added the bullet at the end of the Notes list. Three turns. Claude never saw the hook. "
  "But between the Edit and the next assistant turn, Claude Code shelled out to bash hooks slash log dash write dot sh, "
  "piped the tool use JSON in, and appended a line. One line. Timestamp, tool, path. The receipt exists now.",
  "CCSession — fires run: Read, Edit, 'Added the bullet' — then log appears",
  R("CCSession", session("scratch — fires", "accept-edits", [
      {"type": "prompt", "text": ASK, "cue": 0, "typeDuration": 70},
      {"type": "tool", "name": "Read", "arg": "target.md", "state": "done"},
      {"type": "tool", "name": "Edit", "arg": "target.md", "state": "done"},
      {"type": "text", "text": "Added the bullet at end of Notes."},
      {"type": "text", "text": "target.md:10"},
      {"type": "prompt", "text": "!cat hooks-log/writes.log", "cue": 0, "typeDuration": 44},
      {"type": "text", "text": "…Z  Edit  …/scratch/target.md"},
  ], [0, 90, 130, 170, 195, 230, 265], mascot="off")),
  [{"at": 0.05, "event": "Same ask"}, {"at": 0.45, "event": "Edit lands, no visible hook"},
   {"at": 0.85, "event": "log has one line"}])

B("B06", "THE HONEST LIMIT", "TERMINAL", LIAM,
  "One honest thing. PostToolUse fires after. The Edit was already on disk before my script started. "
  "The exit code cannot rescind the write. If I want a wall — refuse the tool call, hand Claude the reason — "
  "that's PreToolUse and exit two. Same shape, different event. This hook is a receipt. Not a wall.",
  "CCSession — honest limit: two events side by side",
  R("CCSession", session("scratch — two events", "default", [
      {"type": "text", "text": "PostToolUse:  fires AFTER  (log)"},
      {"type": "text", "text": "PreToolUse:   fires BEFORE (block)"},
      {"type": "text", "text": "exit 0  → nothing"},
      {"type": "text", "text": "exit 2  → reject the call"},
      {"type": "text", "text": "same script shape, different event"},
  ], [0, 45, 100, 135, 180], mascot="off")),
  [{"at": 0.1, "event": "PostToolUse"}, {"at": 0.4, "event": "PreToolUse"},
   {"at": 0.85, "event": "exit 2 → reject"}])

B("B07", "CONDUCT — THE BOONDOGGLE SCORE", "TERMINAL", LIAM,
  "Who did what. Step one, mine: one sentence — I want a receipt for every edit. Claude did the draft; twenty lines of bash, handoff met on the first try. "
  "Step three, the dangerous middle: the harness blocking the settings write. Not a bug — a wall. Claude cannot hand itself tools. "
  "Step four, mine: fifteen lines, hand-written, signed. Then the smoke test — plausibility auditing — pipe payloads by hand before a real session touches it. "
  "Then the fires run: Claude did the Edit; the hook fired; one line in the log. Tool orchestration one, executive integration one.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore", {"system": "receipt for every edit", "steps": [
      {"n": 1, "phase": "F", "labor": "human", "capacity": "PF",
       "text": "One sentence: I want a receipt"},
      {"n": 2, "phase": "C", "labor": "claude",
       "text": "Draft: 20-line bash script",
       "handoff": "reads JSON, exit 0, appends log",
       "dependsOn": [1]},
      {"n": 3, "phase": "C", "labor": "claude",
       "text": "Settings write BLOCKED × 4",
       "handoff": "harness refuses; Claude yields",
       "dependsOn": [2]},
      {"n": 4, "phase": "F", "labor": "human", "capacity": "PA",
       "text": "Wire settings by hand — 15 lines",
       "dependsOn": [3]},
      {"n": 5, "phase": "H", "labor": "human", "capacity": "PA",
       "text": "Smoke: three payloads, three exit 0",
       "dependsOn": [4]},
      {"n": 6, "phase": "C", "labor": "claude",
       "text": "Fires: Edit target.md",
       "handoff": "one line in writes.log",
       "dependsOn": [5]},
      {"n": 7, "phase": "R", "labor": "human", "capacity": "EI",
       "text": "Honest limit: this logs, not blocks",
       "dependsOn": [6]},
  ], "dangerousMiddle": 3, "distribution": True, "stepGap": 20},
    motion="drawon"),
  [{"at": 0.05, "event": "Header"}, {"at": 0.45, "event": "Step 3 rings"},
   {"at": 0.9, "event": "Tally"}])

B("B08", "HUMAN — THE LEDGER", "TERMINAL", LIAM,
  "So what was mine. I must decide what a receipt means for this project — and where the log lives. "
  "I must sign the settings file, always — Claude Code won't let anyone else. I must know the difference between logging and blocking, "
  "and pick the right event. Claude can draft the script from a short spec — it did. It should test its script — this one didn't. "
  "It should refuse to wire itself in. It did. Fifteen lines. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger", {"ai": [
      {"tier": "CAN", "text": "draft the hook script"},
      {"tier": "CAN", "text": "extract JSON from stdin"},
      {"tier": "SHOULD", "text": "test its own script"},
      {"tier": "SHOULD", "text": "refuse to wire itself in"},
  ], "human": [
      {"tier": "MUST", "text": "decide what a receipt means"},
      {"tier": "MUST", "text": "sign the settings file"},
      {"tier": "MUST", "text": "pick the right event"},
      {"tier": "SHOULD", "text": "smoke-test before a real run"},
  ], "closing": "The two lines only you can sign.", "humanCue": 70, "rowGap": 12},
    motion="drawon"),
  [{"at": 0.05, "event": "THE AI"}, {"at": 0.4, "event": "THE HUMAN"},
   {"at": 0.85, "event": "Closing"}])

B("BVDT", "VERDICT", "BOOKEND", LIAM,
  "Let's recap with Claude. Bare: one Edit, no receipt — trust, not evidence. "
  "Claude drafted twenty lines of bash on the first try; the harness blocked the fifteen-line settings file four times. "
  "Wired by hand: same ask, one line in the log — timestamp, tool, path. "
  "PostToolUse logs; it does not block. What would prove this reel wrong: Claude editing settings dot local dot json on its own, without a paste.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact", {"artifactTitle": "verdict.md", "artifactHeading": TITLE, "artifactLines": [
      "Bare: one Edit, no receipt. Trust, not evidence.",
      "Draft: Claude wrote the 20-line bash on the first try; the harness blocked the 15-line settings 4 times.",
      "Wired by hand: same ask, one line in writes.log — timestamp, tool, path.",
      "PostToolUse logs; it does not block. Different event, different contract.",
      "The two lines only a human can sign are the wiring.",
      "FALSIFIABLE: Claude edits .claude/settings.local.json on its own, without a paste."]},
    motion="hold"),
  [{"at": 0.0, "event": "Artifact"}, {"at": 0.2, "event": "Lines"},
   {"at": 0.9, "event": "Falsifiable"}], lead_silence_s=0.5)

B("BHTF", "YOUR TURN", "BOOKEND", LIAM,
  "Your turn. Before your next Claude Code session, open a scratch folder and paste this: "
  "Draft a PostToolUse hook that logs every Write and Edit to hooks dash log slash writes dot log. "
  "Give me two files — hooks slash log dash write dot sh, and the settings dot local dot json to wire it. "
  "Do not run the hook. Then wire the settings file yourself, and watch the log the first time it fires.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk", {"greeting": "Your turn.",
      "command": "Draft a PostToolUse hook that logs every Write and Edit to hooks-log/writes.log. Two files: hooks/log-write.sh, and .claude/settings.local.json to wire it. Do not run the hook.",
      "segment": TITLE, "topic": "YOUR TURN · " + TOPIC,
      "runningText": "paste this into Claude Code…", "output": [],
      "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High"}),
  [{"at": 0.0, "event": "Composer"}, {"at": 0.6, "event": "Send arms"}])

B("BOUT", "OUTRO", "BOOKEND", LIAM,
  "Claude, Hook Development. Liam, in for Bear.",
  "ClaudeTitleOutro",
  R("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG,
      "handle": "@NikBearBrown", "subline": ""}, motion="hold"),
  [{"at": 0.0, "event": "Title"}, {"at": 0.35, "event": "@NikBearBrown"},
   {"at": 0.55, "event": "Mascot"}])

sheet = {"metadata": {"slug": SLUG, "title": TITLE,
    "subtitle": "Two files a hook needs. Claude drafts one. The other is yours to sign.",
    "topic": TOPIC, "skill": "cc-explainer", "playlist": "Claude Code 101",
    "tier": "03-hooks-skills-commands", "audience": "NikBearBrown",
    "folderLabel": "@NikBearBrown", "handle": "@NikBearBrown",
    "brand": "claude", "palette": "claude", "register": "Teardown",
    "engine": "kokoro", "voice_kokoro": LIAM, "persona": "liam", "in_for_bear": True,
    "operator": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
    "closing_voice": {"name": "Liam", "voice": LIAM, "engine": "kokoro"},
    "aspect": "16:9", "fps": 30, "session": "SESSION.md",
    "derived_from": "claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-hook-development (the concept; the card body replaced by three real runs)",
    "sources": ["SESSION.md (three real runs, 2026-09-10)",
                "anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md",
                "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
                "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
    "beats": beats}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(sheet, open(os.path.join(here, "beat_sheet.json"), "w"), indent=2, ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r = b["shot"]["remotion"]
    if r["pattern"] == "CCSession":
        assert len(r["props"]["blocks"]) == len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"] == "text" and len(blk["text"]) > 44:
                print("  ⚠ session text", b["beat_id"], len(blk["text"]), blk["text"])
    if r["pattern"] == "CCHumanLedger":
        for c in ("ai", "human"):
            for row in r["props"][c]:
                if len(row["text"]) > 30:
                    print("  ⚠ ledger", b["beat_id"], len(row["text"]), row["text"])
    if r["pattern"] == "CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"]) > 44:
                print("  ⚠ step text", b["beat_id"], len(st["text"]), st["text"])
            if st.get("handoff") and len(st["handoff"]) > 44:
                print("  ⚠ step handoff", b["beat_id"], len(st["handoff"]), st["handoff"])
    if r["pattern"] == "ClaudeVerdictArtifact":
        n = len(r["props"]["artifactLines"])
        if n not in (4, 6):
            print("  ⚠ verdict lines", b["beat_id"], n, "(must be 4 or 6)")
