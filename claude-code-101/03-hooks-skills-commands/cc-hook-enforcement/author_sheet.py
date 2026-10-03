#!/usr/bin/env python3
"""author_sheet.py — cc-hook-enforcement (cc-explainer · Claude Code 101 · tier 03, hooks/skills/commands)
"The Hook That Cannot Be Talked Out Of." Every block traces to SESSION.md (three real fresh runs — two headless claude -p + one direct hook demo). Liam, in for Bear."""
import json, os
SLUG="cc-hook-enforcement"; TITLE="When 'Never' Needs an Exit Code"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Read students.csv and write a one-paragraph summary of each student to summary.md, with an overall performance line at the end of each. Include a suggested letter grade for the teacher's reference."
beats=[]
def est(t): return round(len(t.split())/WPS+0.9,1)
def B(bid, act, lane, voice, narration, element, shot, show, **extra):
    b={"beat_id":bid,"act":act,"lane":lane,"narration_text":narration,"estimated_duration_s":est(narration),"voice":voice,"engine":"kokoro",
       "voice_kokoro":voice,"new_visual_element":element,"shot":shot,"show":show}; b.update(extra); beats.append(b)
def R(pattern, props, motion="type", **shot_extra):
    s={"type":"REMOTION","source":"own","motion":motion,"remotion":{"pattern":pattern,"props":props,"rendered":{"out":"","at":""}}}; s.update(shot_extra); return s
def writer(text, trig, rep, seed):
    return {"text":text,"triggerWords":trig,"replacementWords":rep,"face":"serif","fontSize":78,"align":"center","ink":"#F2F0E9","accent":"#D97757","bg":"#1F1E1B","seed":seed,
            "charMs":22,"hesitateBetween":6,"hesitateWithin":1,"mistakeRate":5,"jitter":20}
def session(title, mode, blocks, cues, mascot="auto"): return {"title":title,"mode":mode,"blocks":blocks,"cues":cues,"mascot":mascot}

B("B00","COLD OPEN — HOOK DIRECT","TERMINAL",LIAM,
  "This is Liam, in for Bear. Forty-two lines of Python. Two payloads, one with a letter grade, one without. Fed to the script on standard input. "
  "The one with the grade: exit two, block message on standard error. The clean one: exit zero, silent. No model in this loop. No prompt. A regex and an exit code. "
  "That's a hook. This film is about what it buys you that a rule in a file cannot.",
  "CCSession (default mode) — the direct hook demo: bad → exit 2, ok → exit 0",
  R("CCSession", session("scratch — direct hook demo","default",[
      {"type":"prompt","text":"!wc -l hooks/guard.py","cue":0,"typeDuration":32},
      {"type":"text","text":"      42 hooks/guard.py"},
      {"type":"prompt","text":"!cat ../evidence/bad.json","cue":0,"typeDuration":40},
      {"type":"text","text":"{'tool_name':'Write',"},
      {"type":"text","text":" 'tool_input':{'file_path':'summary.md',"},
      {"type":"text","text":"   'content':'Ada scored 88.\\nGrade: A'}}"},
      {"type":"prompt","text":"!python3 hooks/guard.py < bad.json","cue":0,"typeDuration":48},
      {"type":"text","text":"BLOCKED by PreToolUse hook —"},
      {"type":"text","text":"pattern: 'Grade: A'. exit 2."},
      {"type":"prompt","text":"!python3 hooks/guard.py < ok.json","cue":0,"typeDuration":46},
      {"type":"text","text":"(silent) exit 0."},
  ],[0,40,80,130,170,210,260,300,330,380,420], mascot="off")),
  [{"at":0.05,"event":"guard.py — 42 lines"},{"at":0.5,"event":"bad → exit 2"},{"at":0.9,"event":"ok → exit 0"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea. A rule in CLAUDE.md is something Claude reads and tries to honor. It usually does. "
  "But 'usually' has no receipt: you don't know when it held and you don't know when it will. "
  "A hook is a shell script the operating system runs before every tool call. It exits or it lets pass — every time, every call. "
  "Different guarantees. Different failure modes. This film is about picking the right one.",
  "BrutalistHesitantWriter — 'might' reconsidered into 'must'",
  R("BrutalistHesitantWriter", writer("A rule in CLAUDE.md — Claude reads it, tries.\nUsually holds. No receipt when it does.\nA hook exits. Every call. Every time.\nSometimes the rule might.","might","must",SLUG), motion="type",
    leaves_terminal_because="the idea is not in any session; the writer types the film's argument and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.55,"event":"'might' → 'must'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words. Advisory: text Claude reads and tries to follow — CLAUDE.md is this. "
  "PreToolUse hook: a shell script Claude Code runs before every tool call, fed the call as JSON on standard input. "
  "Exit two: the exit code that tells Claude Code to block the tool call and show the message to the model. "
  "Deterministic: enforced by the operating system, not the model's judgment. "
  "Receipt: an artifact the run leaves behind proving what happened.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"advisory","meaning":"text Claude reads and tries to follow — CLAUDE.md is this"},
      {"term":"PreToolUse hook","meaning":"shell script Claude Code runs before every tool call, JSON on stdin"},
      {"term":"exit 2","meaning":"exit code that blocks the tool call and shows the message to Claude"},
      {"term":"deterministic","meaning":"enforced by the OS, not by the model's judgment"},
      {"term":"receipt","meaning":"artifact the run leaves behind proving what happened"}],
    "startCue":10,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience who may not know the terminal words"),
  [{"at":0.05,"event":"First term"},{"at":0.55,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","ADVISORY — THE ASK","TERMINAL",LIAM,
  "Advisory first. CLAUDE.md in the folder — never a letter grade, never overall performance followed by one. Hook stashed for now. "
  "Same ask that names both. Read the csv, write summary.md, include a suggested letter grade. Claude reads the rule, refuses in one sentence, no tool call. "
  "The advisory held. That's what it looks like when it works.",
  "CCSession — advisory: the ask, Claude's verbatim refusal, no Write",
  R("CCSession", session("studygroup — advisory","accept-edits",[
      {"type":"prompt","text":"Read students.csv, write summary.md","cue":0,"typeDuration":58},
      {"type":"prompt","text":"(with a suggested letter grade)","cue":0,"typeDuration":52},
      {"type":"text","text":"I can't do the letter grades or"},
      {"type":"text","text":"the 'overall performance' line —"},
      {"type":"text","text":"CLAUDE.md forbids both. Only the"},
      {"type":"text","text":"teacher assigns grades."},
  ],[0,60,120,150,180,210], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.55,"event":"Claude refuses"},{"at":0.9,"event":"No Write"}])

B("B02","ADVISORY — THE MISSING RECEIPT","TERMINAL",LIAM,
  "Now check what the file system remembers. List the folder. No summary. Grep the transcript for tool_use — zero. Nothing landed on disk; nothing tried. "
  "It held today. But the file system does not know the rule was there. The rule was in the model's context, and the context is gone when the session ends. "
  "It held today is not the same as it cannot fail.",
  "CCSession — plain shell VERIFY: ls, grep for tool_use → 0",
  R("CCSession", session("studygroup — advisory · verify","default",[
      {"type":"prompt","text":"!ls scratch/","cue":0,"typeDuration":26},
      {"type":"text","text":"CLAUDE.md   README.md   ask.txt"},
      {"type":"text","text":"hooks   students.csv"},
      {"type":"prompt","text":"!grep -c tool_use run-advisory.jsonl","cue":0,"typeDuration":48},
      {"type":"text","text":"0"},
      {"type":"text","text":"held today. no artifact on disk."},
      {"type":"text","text":"no receipt the rule was in play."},
  ],[0,40,70,120,160,190,220], mascot="off")),
  [{"at":0.05,"event":"ls"},{"at":0.4,"event":"tool_use → 0"},{"at":0.85,"event":"no receipt"}])

B("B03","HOOK ACTIVE — THE FIRST WRITE","TERMINAL",LIAM,
  "Second run. Move CLAUDE.md out of the folder. Hook armed. Same ask. "
  "Claude lists, reads the csv, and goes straight to a Write — a full summary with a suggested letter grade line under each student. "
  "The tool_result comes back with is_error true. The message is the guard's: BLOCKED by PreToolUse hook — pattern grade colon A. The file did not land.",
  "CCSession — hook run: ls, Read csv, Write attempt, is_error BLOCKED",
  R("CCSession", session("studygroup — hook active","accept-edits",[
      {"type":"prompt","text":"Read students.csv, write summary.md","cue":0,"typeDuration":56},
      {"type":"tool","name":"Bash","arg":"ls","state":"done"},
      {"type":"tool","name":"Read","arg":"students.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"summary.md","state":"error"},
      {"type":"text","text":"PreToolUse:Write hook error:"},
      {"type":"text","text":"BLOCKED by PreToolUse hook —"},
      {"type":"text","text":"pattern: 'grade: A'. Rewrite"},
      {"type":"text","text":"without any letter grade."},
  ],[0,90,120,150,175,205,235,265], mascot="off")),
  [{"at":0.05,"event":"Ask, no CLAUDE.md"},{"at":0.5,"event":"Write attempt"},{"at":0.9,"event":"BLOCKED, is_error"}])

B("B04","HOOK ACTIVE — THE CORRECTION","TERMINAL",LIAM,
  "The block is not a suggestion. Claude reads the README. Reads the guard. Now it understands the rule — from the script that just stopped it, not from a paragraph it read at startup. "
  "It rewrites summary.md without any grade colon letter, keeps the overall performance line as prose. Second Write, allowed, thirteen lines. "
  "The hook made the model do a thing the model did not know it needed to do.",
  "CCSession — Reads README + guard.py, second Write succeeds",
  R("CCSession", session("studygroup — hook active · fix","accept-edits",[
      {"type":"text","text":"The PreToolUse hook blocked it."},
      {"type":"text","text":"Let me read the rules and rewrite."},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"hooks/guard.py","state":"done"},
      {"type":"text","text":"Only the teacher awards grades."},
      {"type":"text","text":"Rewriting without any letter grade."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
  ],[0,30,60,110,160,190,240], mascot="off")),
  [{"at":0.05,"event":"Reads the guard"},{"at":0.5,"event":"Understands the rule"},{"at":0.9,"event":"Second Write OK"}])

B("B05","HOOK ACTIVE — VERIFY","TERMINAL",LIAM,
  "Check what landed. Thirteen lines. Grep for any line that starts with Grade or Overall-performance-letter — zero. Grep for a plain letter-colon pattern — zero. "
  "But grep for the word grade anywhere — three: the descriptive overall lines. The word is legal, the letter is not. The hook enforces the shape you wrote, nothing else.",
  "CCSession — wc, grep for grade patterns, grep for the word",
  R("CCSession", session("studygroup — hook active · verify","default",[
      {"type":"prompt","text":"!wc -l summary.md","cue":0,"typeDuration":28},
      {"type":"text","text":"      13 summary.md"},
      {"type":"prompt","text":"!grep -c '^Grade\\|:\\s*[A-F]' summary.md","cue":0,"typeDuration":50},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep -ci grade summary.md","cue":0,"typeDuration":38},
      {"type":"text","text":"3"},
      {"type":"text","text":"word grade — legal."},
      {"type":"text","text":"grade colon letter — not."},
  ],[0,40,75,120,160,200,230,255], mascot="off")),
  [{"at":0.05,"event":"wc → 13"},{"at":0.4,"event":"grep pattern → 0"},{"at":0.85,"event":"grep word → 3"}])

B("B06","THE HONEST LIMIT","TERMINAL",LIAM,
  "One more thing. Test the guard against gradebook, and against gradual improvement in A students. Both pass through. Neither is a grade. Neither matches the pattern. "
  "So the deterministic guarantee is real, and its shape is exactly the regex you wrote. Not the intent — the pattern. That trade is the design.",
  "CCSession — the regex edge cases: gradebook / gradual",
  R("CCSession", session("studygroup — the honest limit","default",[
      {"type":"prompt","text":"!python3 -c 'import guard, sys; …'","cue":0,"typeDuration":50},
      {"type":"text","text":"'gradebook access is here'"},
      {"type":"text","text":"→ False"},
      {"type":"text","text":"'gradual improvement in A students'"},
      {"type":"text","text":"→ False"},
      {"type":"text","text":"'Suggested grade: B+' → True"},
      {"type":"text","text":"the shape you named. nothing else."},
  ],[0,50,80,110,145,180,220], mascot="off")),
  [{"at":0.05,"event":"tests"},{"at":0.5,"event":"gradebook, gradual → False"},{"at":0.9,"event":"the trade"}])

B("BCONDUCT","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: named the one shape that must never land — a letter grade. "
  "Step two, mine: wrote the guard — forty-two lines, a regex, exit two. Reviewed it, tested both payloads. "
  "Step three, Claude: advisory run — read CLAUDE.md, refused in one sentence. Handoff met by absence — no summary. "
  "Step four, the dangerous middle: Claude wrote a full summary with letter grades. The operating system stopped it. Not the model. "
  "Step five, Claude: read the guard, understood the rule from the block, rewrote clean. Handoff met — grep for the pattern returns zero. "
  "Step six, mine: read the second file, decided the descriptive overall lines were the right compromise. Interpretive judgment. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one shape · one exit code","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Name the shape that must never land"},
      {"n":2,"phase":"F","labor":"human","capacity":"PF","text":"Write the guard — 42 lines, exit 2"},
      {"n":3,"phase":"C","labor":"claude","text":"Advisory run: read CLAUDE.md, refused","handoff":"no summary.md on disk","dependsOn":[1]},
      {"n":4,"phase":"C","labor":"claude","text":"Hook run: wrote grades, OS blocked","handoff":"tool_result is_error, hook message","dependsOn":[2]},
      {"n":5,"phase":"C","labor":"claude","text":"Read the guard, rewrote clean","handoff":"grep pattern in summary.md → 0","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Descriptive overall lines — kept","dependsOn":[5]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.55,"event":"Step 4 rings"},{"at":0.95,"event":"Tally"}])

B("BHUMAN","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide the one line that must never ship. I must write the pattern the operating system will read. "
  "I must audit the regex for holes — gradebook slips, that is my call. I should keep the rule text in CLAUDE.md too, because two layers cover different failure modes. "
  "Claude can read a rule and follow it — it did in the advisory run. It can be stopped by a shell script's exit code — it was. "
  "It should read the guard when blocked — it did, unprompted. It should say the pattern back to the user — it did. The redundancy is the design.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"read a rule and follow it"},{"tier":"CAN","text":"be stopped by an exit code"},
                          {"tier":"SHOULD","text":"read the guard when blocked"},{"tier":"SHOULD","text":"say the pattern back"}],
                    "human":[{"tier":"MUST","text":"decide what never ships"},{"tier":"MUST","text":"write the OS-side pattern"},
                             {"tier":"MUST","text":"audit the regex for holes"},{"tier":"SHOULD","text":"keep the rule in CLAUDE.md"}],
                    "closing":"Two layers. The redundancy is the design.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Advisory held on the ask — Claude read CLAUDE.md, refused, wrote nothing. No receipt on disk that a rule was in play. "
  "Hook run, CLAUDE.md gone — Claude wrote a full summary with suggested letter grade A minus, B minus, A. The tool_result came back is_error, the guard's message verbatim. The Write never landed. "
  "Claude read the guard, understood the rule from the block, and rewrote the file without any grade colon letter. The word grade appears in it; the letter does not. The regex enforces the shape you named, and nothing else. "
  "What would prove this reel wrong: a hook-active run that lands a matching grade colon letter line on disk.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Advisory held — Claude refused in text, wrote nothing. No receipt on disk that a rule was in play.",
      "Hook run: Claude wrote 'Suggested letter grade: A-'; tool_result is_error; the file never landed.",
      "Claude read the guard, rewrote clean. The word 'grade' appears three times; the pattern does not.",
      "FALSIFIABLE: a hook-active run that lands a matching grade-colon-letter line on disk."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.25,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Open Claude Code in a project you actually own and paste this: "
  "Pick one line that must never land on disk in this project. Write me a PreToolUse hook — a small shell script that exits two on any Write whose content matches your pattern — and register it in dot-claude slash settings dot local dot json. "
  "Then hand me two payloads I can pipe in: one that trips the hook, one that doesn't. Print exit two and exit zero.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Pick one line that must never land on disk in this project. Write me a PreToolUse hook — a small shell script that exits 2 on any Write whose content matches your pattern — and register it in .claude/settings.local.json. Then hand me two payloads I can pipe in: one that trips the hook, one that doesn't. Print exit 2 and exit 0.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"When Never Needs an Exit Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"CLAUDE.md is a rule Claude reads. A hook is one exit code the OS honors — every call, every time.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-vox-hook-enforcement (the concept; the card body replaced by two fresh headless runs + a direct hook demo)",
    "sources":["SESSION.md (2 real runs + direct hook demo, 2026-09-10)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
warn=0
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print("  ⚠",b["beat_id"],len(blk["text"]),blk["text"]); warn+=1
            if blk["type"]=="prompt" and len(blk["text"])>44: print("  ⚠ prompt",b["beat_id"],len(blk["text"]),blk["text"]); warn+=1
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print("  ⚠ ledger",len(row["text"]),row["text"]); warn+=1
    if r["pattern"]=="CCBoondoggleScore":
        if len(r["props"]["system"])>28: print("  ⚠ score-system",len(r["props"]["system"]),r["props"]["system"]); warn+=1
        for st in r["props"]["steps"]:
            if len(st["text"])>44: print("  ⚠ step",len(st["text"]),st["text"]); warn+=1
    if r["pattern"]=="CCPlainShell":
        for line in r["props"]["lines"]:
            if len(line)>48: print("  ⚠ shell",len(line),line); warn+=1
    if r["pattern"]=="CCDefinitions":
        for t in r["props"]["terms"]:
            if len(t["term"])>18: print("  ⚠ term-name",len(t["term"]),t["term"]); warn+=1
            if len(t["meaning"])>70: print("  ⚠ term-def",len(t["meaning"]),t["meaning"]); warn+=1
    if r["pattern"]=="ClaudeVerdictArtifact":
        n=len(r["props"]["artifactLines"])
        if n not in (4,6): print("  ⚠ verdict lines",n); warn+=1
print(f"warnings: {warn}")
