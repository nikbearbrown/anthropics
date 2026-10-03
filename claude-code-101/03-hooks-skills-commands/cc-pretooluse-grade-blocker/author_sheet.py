#!/usr/bin/env python3
"""author_sheet.py — cc-pretooluse-grade-blocker (cc-explainer · Claude Code 101 · tier 03, hooks)
"Build a PreToolUse Hook That Blocks Grade Generation with Claude Code." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-pretooluse-grade-blocker"; TITLE="Build a PreToolUse Hook That Blocks Grade Generation with Claude Code"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Read students.csv and write a one-paragraph summary of each student to summary.md, with an overall performance line at the end of each. Include a suggested letter grade for the teacher's reference."
BUILD_ASK="Write a PreToolUse hook at hooks/block-grades.py that blocks Write/Edit/MultiEdit whose content contains a final letter grade. Read tool_input JSON on stdin. On match: stderr reason, exit 2. Also wire .claude/settings.local.json."
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

B("B00","COLD OPEN — BARE","TERMINAL",LIAM,
  "This is Liam, in for Bear. Same ask, twice. A CSV of three students and one sentence: write a summary with a suggested letter grade. "
  "No hook, no CLAUDE.md — nothing between the model and disk. It reads the CSV, writes summary.md, and lands three lines with letter grades in them. "
  "Nobody said not to. The instruction to only let the teacher grade is in the README, and the model doesn't have to read the README.",
  "CCSession — bare run: the ask, Read, Write, three grades",
  R("CCSession", session("gradebook — bare","accept-edits",[
      {"type":"prompt","text":"Read students.csv and write a","cue":0,"typeDuration":50},
      {"type":"prompt","text":"one-paragraph summary of each to","cue":0,"typeDuration":50},
      {"type":"prompt","text":"summary.md — include a suggested","cue":0,"typeDuration":50},
      {"type":"prompt","text":"letter grade for the teacher.","cue":0,"typeDuration":50},
      {"type":"tool","name":"Read","arg":"students.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
      {"type":"text","text":"Suggested letter grade: **A-**"},
      {"type":"text","text":"Suggested letter grade: **C**"},
      {"type":"text","text":"Suggested letter grade: **B+**"},
  ],[0,60,120,180,220,255,285,305,325], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.5,"event":"Write summary.md"},{"at":0.85,"event":"Three grades land"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. A note in CLAUDE.md is a hope — the model reads it, weights it, sometimes overrides it. "
  "A PreToolUse hook is a fence. It runs between the model and disk on every Write, sees what's about to be written, and can refuse. "
  "So we build one. Thirty-six lines of Python, wired in fifteen lines of JSON, and the same ask stops behaving the same way.",
  "BrutalistHesitantWriter — 'hope' reconsidered into 'hook'",
  R("BrutalistHesitantWriter", writer("A note in CLAUDE.md is a hope.\nA model reads it. Weights it. Sometimes ignores it.\nA PreToolUse hook is a fence.\nOn every Write. Between the model and disk.","hope","hook",SLUG), motion="type",
    leaves_terminal_because="the film's argument — hope vs. fence — is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'hope' → 'hook'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words. PreToolUse: a hook that runs before Claude Code executes a tool call, so it can veto. tool_input: the JSON body of the pending call — for a Write, it contains the file path and the content. "
  "matcher: the regex Claude Code uses to decide which tools your hook applies to — here, Write, Edit, and MultiEdit. Exit 2: the shell exit code Claude Code reads as a hard deny — anything on stderr becomes the reason. "
  "settings.local.json: the per-project hook wiring — permission-guarded, because a hook changes what Claude Code is allowed to do.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"PreToolUse","meaning":"a hook that runs BEFORE Claude Code executes a tool call — so it can veto"},
      {"term":"tool_input","meaning":"the pending call's JSON — for Write, the file path and the content"},
      {"term":"matcher","meaning":"the regex that picks which tools the hook covers — Write, Edit, MultiEdit"},
      {"term":"exit 2","meaning":"Claude Code reads exit 2 as a hard deny; stderr becomes the reason"},
      {"term":"settings.json","meaning":"per-project hook wiring — permission-guarded even under accept-edits"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BUILD — THE ASK","TERMINAL",LIAM,
  "Now I ask Claude Code to build the hook itself. Spec in one paragraph: read the tool_input JSON on stdin, match a grade pattern, print the reason on stderr, exit two. "
  "It thinks, makes a hooks folder, and writes thirty-six lines of Python — two regexes over the content, one for the labelled pattern, one for any grade-adjacent line.",
  "CCSession — build run: prompt, mkdir hooks, Write hooks/block-grades.py",
  R("CCSession", session("build the hook","accept-edits",[
      {"type":"prompt","text":"Write PreToolUse hook","cue":0,"typeDuration":40},
      {"type":"prompt","text":"hooks/block-grades.py:","cue":0,"typeDuration":40},
      {"type":"prompt","text":"read tool_input JSON on stdin,","cue":0,"typeDuration":50},
      {"type":"prompt","text":"match a grade pattern,","cue":0,"typeDuration":40},
      {"type":"prompt","text":"stderr reason, exit 2.","cue":0,"typeDuration":40},
      {"type":"tool","name":"Read","arg":"BUILD-ASK.txt","state":"done"},
      {"type":"tool","name":"Bash","arg":"mkdir -p hooks","state":"done"},
      {"type":"tool","name":"Write","arg":"hooks/block-grades.py","state":"done"},
      {"type":"text","text":"36 lines · stdlib only · two regexes"},
  ],[0,40,80,130,175,215,240,270,305], mascot="off")),
  [{"at":0.05,"event":"Spec types"},{"at":0.55,"event":"mkdir hooks"},{"at":0.85,"event":"Write block-grades.py"}])

B("B02","THE REFUSAL","TERMINAL",LIAM,
  "I ask it for the second file — the wiring. And it stops. Claude Code refuses to write .claude/settings.local.json on its own, even with accept-edits on. "
  "Hook configs are permission-guarded, because a hook changes what Claude Code will do. It prints the JSON body and says: drop this in yourself. Honest. Correct. Mine to do.",
  "CCSession — Claude Code refuses to write settings.local.json",
  R("CCSession", session("build the hook","accept-edits",[
      {"type":"prompt","text":"Also write","cue":0,"typeDuration":30},
      {"type":"prompt","text":".claude/settings.local.json.","cue":0,"typeDuration":50},
      {"type":"text","text":"The permission dialog is still"},
      {"type":"text","text":"awaiting your approval for"},
      {"type":"text","text":"`.claude/settings.local.json` —"},
      {"type":"text","text":"Claude Code guards that file"},
      {"type":"text","text":"since it changes hook behavior."},
      {"type":"text","text":"Drop this JSON in yourself."},
  ],[0,40,80,105,130,155,180,210], mascot="off")),
  [{"at":0.05,"event":"Second ask"},{"at":0.4,"event":"Permission dialog"},{"at":0.9,"event":"Drop it in yourself"}])

B("B03","LIAM WIRES THE HOOK","SHELL",LIAM,
  "So I wire it. Fifteen lines of JSON — matcher: Write, Edit, MultiEdit; command: python3 the hook, expanded to the project directory. That's the whole handoff. "
  "The model wrote the mechanism it can't approve; the human approves the mechanism the model wrote. That's the split you want on anything that changes what Claude Code is allowed to do.",
  "CCPlainShell — cat .claude/settings.local.json (Liam's step)",
  R("CCPlainShell",{"title":"zsh — ~/gradebook","lines":[
      "$ cat .claude/settings.local.json",
      "{",
      "  \"hooks\": {",
      "    \"PreToolUse\": [",
      "      {",
      "        \"matcher\": \"Write|Edit|MultiEdit\",",
      "        \"hooks\": [",
      "          { \"type\": \"command\",",
      "            \"command\": \"python3 …/block-grades.py\" }",
      "        ] } ] } }",
      "$ wc -l .claude/settings.local.json",
      "      15 .claude/settings.local.json"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the wiring is outside any Claude Code session — Liam types it in a plain shell"),
  [{"at":0.05,"event":"cat the wiring"},{"at":0.5,"event":"matcher line"},{"at":0.9,"event":"wc → 15"}])

B("B04","VERIFY — THE HOOK ALONE","TERMINAL",LIAM,
  "Before the end-to-end run, I test the hook itself. Three payloads that look like the JSON Claude Code will hand it: one carrying 'grade: A-', one carrying 'top fifteen percent', one carrying clean prose. "
  "Grade payload: exit two, stderr says refusing to write. Fifteen percent payload: exit zero — it's a quantity, not a grade. Clean prose: exit zero. The hook draws the line where I want it drawn.",
  "CCSession — three payloads, three exit codes",
  R("CCSession", session("test the hook","default",[
      {"type":"prompt","text":"!python3 hooks/block-grades.py","cue":0,"typeDuration":50},
      {"type":"prompt","text":"    < evidence/bad.json","cue":0,"typeDuration":40},
      {"type":"text","text":"refusing to write a letter grade"},
      {"type":"text","text":"→ 'grade: **A-'"},
      {"type":"text","text":"exit=2"},
      {"type":"prompt","text":"!… < evidence/quantity.json","cue":0,"typeDuration":40},
      {"type":"text","text":"exit=0  (top 15% — a quantity)"},
      {"type":"prompt","text":"!… < evidence/ok.json","cue":0,"typeDuration":40},
      {"type":"text","text":"exit=0  (clean prose)"},
  ],[0,40,85,110,135,175,215,255,290], mascot="off")),
  [{"at":0.05,"event":"bad.json"},{"at":0.4,"event":"exit 2"},{"at":0.7,"event":"quantity → exit 0"},{"at":0.9,"event":"ok → exit 0"}])

B("BFLOW","HOOK LIFECYCLE","DIAGRAM",LIAM,
  "So the flow is this. Claude decides to call Write. Before the tool runs, Claude Code pipes the tool_input JSON into my hook on stdin. "
  "The hook reads it, matches the grade pattern, prints the reason on stderr, exits two. Claude Code turns that exit code into a denied tool result, and Claude sees the reason and gets to try again. "
  "None of it needed the model's cooperation. None of it needed a rule the model had to remember.",
  "FlowDiagram — the PreToolUse pipeline",
  R("FlowDiagram",{
      "skin":"claude","kicker":"PRETOOLUSE HOOK","pulse":True,
      "caption":"Between the model and disk. Every Write.",
      "nodes":[
          {"id":"claude","label":"CLAUDE","sub":"decides to Write","tier":"client","x":80,"y":460,"w":300,"h":160,"hi":True},
          {"id":"harness","label":"CLAUDE CODE","sub":"the harness","tier":"edge","x":460,"y":460,"w":320,"h":160},
          {"id":"hook","label":"HOOK","sub":"block-grades.py","tier":"compute","x":880,"y":320,"w":300,"h":180,"hi":True},
          {"id":"stdin","label":"stdin","sub":"tool_input JSON","tier":"data","x":880,"y":600,"w":300,"h":160},
          {"id":"deny","label":"exit 2","sub":"stderr = reason","tier":"data","x":1280,"y":460,"w":280,"h":160,"hi":True},
          {"id":"retry","label":"RETRY","sub":"Claude tries again","tier":"compute","x":1620,"y":460,"w":240,"h":160}],
      "edges":[
          {"from":"claude","to":"harness","order":1,"kind":"flow","label":"Write"},
          {"from":"harness","to":"hook","order":2,"kind":"flow","label":"spawn"},
          {"from":"stdin","to":"hook","order":3,"kind":"data","label":"JSON"},
          {"from":"hook","to":"deny","order":4,"kind":"reply"},
          {"from":"deny","to":"harness","order":5,"kind":"flow","dashed":True,"label":"denied"},
          {"from":"harness","to":"retry","order":6,"kind":"flow","label":"error result"}],
      "viewBox":{"w":1920,"h":1080}}, motion="drawon",
      leaves_terminal_because="BFLOW: the harness's pre-tool boundary is not visible in any single session frame"),
  [{"at":0.05,"event":"CLAUDE lights"},{"at":0.35,"event":"Hook fires"},{"at":0.75,"event":"denied → retry"}])

B("B05","HOOKED — THE BLOCK","TERMINAL",LIAM,
  "Now the end-to-end run. Same ask. Same model. Fresh session, hook active. Claude reads the CSV, writes its first draft — and every letter grade line trips the hook. "
  "Exit two comes back as an is_error tool result. The message on stderr shows up in Claude's context. Then Claude does what it does when it hits a wall: it reads the wall.",
  "CCSession — hooked run: Write blocked, hook message returned",
  R("CCSession", session("gradebook — hooked","accept-edits",[
      {"type":"prompt","text":"Read students.csv and write a","cue":0,"typeDuration":50},
      {"type":"prompt","text":"summary with a suggested grade.","cue":0,"typeDuration":50},
      {"type":"tool","name":"Read","arg":"students.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"summary.md","state":"error"},
      {"type":"text","text":"PreToolUse:Write hook error:"},
      {"type":"text","text":"block-grades: refusing to write"},
      {"type":"text","text":"a final letter grade"},
      {"type":"text","text":"→ 'grade: A'"},
      {"type":"tool","name":"Read","arg":"hooks/block-grades.py","state":"done"},
  ],[0,50,110,150,180,205,230,255,285], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.4,"event":"Write blocked"},{"at":0.8,"event":"Reads the hook"}])

B("BSHOW","THE TWO FILES","TERMINAL",LIAM,
  "So what's on disk. Bare summary: three graded lines, thirteen rows, the words 'letter grade' three times. Hooked summary: seventeen rows, no graded lines at all, one mention of grades — in a footer explaining that the teacher assigns them. "
  "Same model. Same ask. Different disk. The difference is fifty-one lines of scaffolding that Claude wrote most of and I wired the rest.",
  "CCPlainShell — grep and wc on the two summaries",
  R("CCPlainShell",{"title":"zsh — grep the two outputs","lines":[
      "$ wc -l evidence/summary.bare.md",
      "      13 evidence/summary.bare.md",
      "$ wc -l evidence/summary.hooked.md",
      "      17 evidence/summary.hooked.md",
      "$ grep -cE 'grade:? [A-F][+-]?' \\",
      "    evidence/summary.bare.md",
      "3",
      "$ grep -cE 'grade:? [A-F][+-]?' \\",
      "    evidence/summary.hooked.md",
      "0",
      "$ grep 'letter grade' evidence/summary.hooked.md",
      "the teacher assigns final letter grades."],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="BSHOW: the two outputs on disk are the receipt for the whole film"),
  [{"at":0.05,"event":"wc counts"},{"at":0.55,"event":"grep → 3 vs 0"},{"at":0.9,"event":"footer line"}])

B("BCONDUCT","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Score. Step one, mine: a one-sentence spec for the hook — read stdin, match, exit two. Claude did step two — wrote thirty-six lines that passed my three unit tests. "
  "Step three, the dangerous middle: Claude tried to wire settings.local.json and Claude Code refused — a plausible action stopped by the harness, not by me. I audited the refusal and did the wiring myself. "
  "Then the end-to-end run — Claude retried without grades on its own. Tool orchestration counts twice: settings.local.json is guarded, and matcher was mine to choose.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one spec · one hook · one wiring","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One spec: stdin, match, exit 2"},
      {"n":2,"phase":"C","labor":"claude","text":"36 lines · two regexes · stdlib","handoff":"3 payloads: 2 exit 0, 1 exit 2","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"claude","text":"Tried to Write settings.local.json","handoff":"Claude Code refuses hook config","dependsOn":[2]},
      {"n":4,"phase":"H","labor":"human","capacity":"PA","text":"Audit the refusal — correct call","dependsOn":[3]},
      {"n":5,"phase":"I","labor":"human","capacity":"TO","text":"Pick the matcher; wire the JSON","dependsOn":[4]},
      {"n":6,"phase":"B","labor":"claude","text":"Same ask, hooked: retry without grades","handoff":"grep grade:[A-F] → 0","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("BHUMAN","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide what a grade even is — the regex is a policy, not a fact. I must pick the matcher — which tools the fence applies to. "
  "I must wire the hook, because settings.local.json is mine to sign for. Claude can draft the mechanism, run its own tests, and retry when the wall pushes back. It can and it did.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"draft the hook from a spec"},{"tier":"CAN","text":"read the wall it just tripped"},
                          {"tier":"SHOULD","text":"retry without the pattern"},{"tier":"SHOULD","text":"refuse to wire its own fence"}],
                    "human":[{"tier":"MUST","text":"decide what counts as a grade"},{"tier":"MUST","text":"pick the tools the hook covers"},
                             {"tier":"MUST","text":"wire settings.local.json"},{"tier":"SHOULD","text":"unit-test with fake payloads"}],
                    "closing":"The fence is mine. The bricks are Claude's.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Bare: same ask, three letter grades on disk. Build: Claude wrote the hook in thirty-six lines and refused to wire it. Hooked: same ask, first Write denied, second Write clean. "
  "The mechanism sits between the model and disk, not inside the model's judgment. "
  "What would prove this reel wrong: a bare run that refuses the letter-grade line on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare run, no hook: three letter grades landed on disk in one Write.",
      "Build run: Claude wrote 36 lines of hook and refused to wire it; the human wired 15.",
      "Hooked run: same ask, first Write denied on stderr, second Write clean.",
      "FALSIFIABLE: a bare run that refuses the letter-grade line on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Pick one thing your project should never write — a customer email, an API key in code, a raw SSN. Then open Claude Code and paste this: "
  "write me a PreToolUse hook that blocks Write, Edit, and MultiEdit whose content matches this pattern, with the reason on stderr and exit two. Then hand me the settings.local.json to wire it. "
  "Don't skip the tests: three payloads — one that should trip, one that should pass, one edge case near the line.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Write me a PreToolUse hook that blocks Write, Edit, and MultiEdit whose content matches this pattern: <pattern>. Read tool_input JSON on stdin. On match: stderr reason, exit 2. On no match: exit 0. Then hand me the settings.local.json to wire it. Include three test payloads: one that should trip, one that should pass, one edge case near the line.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Build a PreToolUse Hook That Blocks Grade Generation with Claude Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same ask, twice — before the hook, and after 36 lines of Python between the model and disk.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md","build":True,
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-pretooluse-grade-blocker (the concept; card body replaced by three real runs)",
    "sources":["SESSION.md (three real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print("  ⚠",b["beat_id"],len(blk["text"]),blk["text"])
            if blk["type"]=="prompt" and len(blk["text"])>44: print("  ⚠ prompt",b["beat_id"],len(blk["text"]),blk["text"])
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print("  ⚠ ledger",len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>44: print("  ⚠ step",len(st["text"]),st["text"])
    if r["pattern"]=="CCPlainShell":
        for line in r["props"]["lines"]:
            if len(line)>60: print("  ⚠ shell",len(line),line)
    if r["pattern"]=="CCDefinitions":
        for t in r["props"]["terms"]:
            if len(t["term"])>18: print("  ⚠ term",len(t["term"]),t["term"])
            if len(t["meaning"])>75: print("  ⚠ meaning",len(t["meaning"]),t["meaning"])
    if r["pattern"]=="ClaudeVerdictArtifact":
        n=len(r["props"]["artifactLines"])
        if n not in (4,6): print("  ⚠ verdict lines",n)
