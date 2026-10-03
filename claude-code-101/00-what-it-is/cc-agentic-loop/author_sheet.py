#!/usr/bin/env python3
"""author_sheet.py — cc-agentic-loop (cc-explainer · Claude Code 101 · tier 00, film 06)
"The Loop Runs While You Read. Plan Mode Is The Pause." Every block traces to SESSION.md
(two real fresh headless runs, same one-sentence ask, only --permission-mode changes).
Liam, in for Bear."""
import json, os
SLUG="cc-agentic-loop"
TITLE="The Loop Runs While You Read. Plan Mode Is The Pause."
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Fix the bug in calc.py, add a test that would have caught it, and run the tests."
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
def session(title, mode, blocks, cues, mascot="off"): return {"title":title,"mode":mode,"blocks":blocks,"cues":cues,"mascot":mascot}

# ───────── B00 · COLD OPEN — the loop, unattended ─────────
B("B00","COLD OPEN — LOOP","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence. Watch a chatbot cannot do this. "
  "Two Reads. A finding. Two Edits. A Bash run. Seven tool calls, two files changed, and tests pass — "
  "in one turn. Thirty-eight seconds. Nobody said yes to any of it.",
  "CCSession — the loop run: prompt, 2 Reads, finding, 2 Edits, Bash test, OK",
  R("CCSession", session("scratch — acceptEdits","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"calc.py","state":"done"},
      {"type":"tool","name":"Read","arg":"test_calc.py","state":"done"},
      {"type":"text","text":"The bug: `add` returns 0 when"},
      {"type":"text","text":"either operand is negative."},
      {"type":"tool","name":"Edit","arg":"calc.py","state":"done"},
      {"type":"tool","name":"Edit","arg":"test_calc.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_calc.py","state":"done"},
      {"type":"text","text":"Ran 4 tests in 0.000s — OK."},
  ],[0,90,115,140,160,185,210,235,265], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.35,"event":"finding lands"},{"at":0.7,"event":"two Edits"},{"at":0.95,"event":"tests OK"}])

# ───────── BIDEA · the idea, hesitated ─────────
B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Claude Code isn't a faster chatbot. A chatbot produces text and waits. "
  "Claude Code runs a loop: gather, act, verify — and closes it, on its own, until it thinks it's done. "
  "Plan mode is the one place the loop stops. Same request, same tools, same repo — one flag is the difference.",
  "BrutalistHesitantWriter — 'faster' reconsidered into 'a loop'",
  R("BrutalistHesitantWriter",
    writer("Claude Code is a faster chatbot.\nIt reads. It writes. It runs.\nAll in one turn, before you look.\nThe pause is a flag you set first.",
           "faster chatbot","a loop, not text",SLUG),
    motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.22,"event":"'faster chatbot' → 'a loop, not text'"},{"at":0.85,"event":"Last line"}])

# ───────── BDEFS · four terms ─────────
B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Agentic loop: gather, act, verify, and repeat — Claude Code's own cycle, run without you between steps. "
  "Tool call: one atomic thing Claude does — read a file, run a shell, edit a line. "
  "Permission mode: the flag that decides which tools may fire without asking. Accept-edits fires them; plan fires nothing. "
  "Exit plan mode: the interruption point — the tool call that puts the plan in front of you and waits for yes.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"agentic loop","meaning":"gather, act, verify, repeat — closed by Claude, not by you"},
      {"term":"tool call","meaning":"one atomic action — read, edit, shell — one line in the transcript"},
      {"term":"permission mode","meaning":"the flag that decides which tools fire without asking"},
      {"term":"ExitPlanMode","meaning":"the interruption point — the plan appears and waits for your yes"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

# ───────── B01 · LOOP — VERIFY (plain shell) ─────────
B("B01","LOOP — VERIFY","SHELL",LIAM,
  "Check the loop run. Git diff: five lines added, two removed, two files touched — mine now, whether I read them or not. "
  "The tests pass, four of them. And the count: seven tool calls, one turn, thirty-eight seconds. Claude's checkmark and my count agree. That is not the question. The question is when I got to look.",
  "CCPlainShell — git diff --stat, unittest OK, the count",
  R("CCPlainShell",{"title":"zsh — scratch/","lines":[
      "$ git diff --stat",
      " calc.py       | 2 --",
      " test_calc.py  | 5 +",
      " 2 files changed, 5 insertions(+), 2 deletions(-)",
      "$ python3 -m unittest test_calc.py 2>&1 | tail -1",
      "OK",
      "# 7 tool calls · 2 files · 38 seconds",
      "# one turn · no pause"],
    "startCue":12,"lineGap":20}, motion="type",
    leaves_terminal_because="what the session claimed, checked from a plain shell — REAL-SESSION LAW's verify step"),
  [{"at":0.05,"event":"git diff --stat"},{"at":0.5,"event":"unittest OK"},{"at":0.85,"event":"the count"}])

# ───────── B02 · THE CORRECTION — reset + one-flag change ─────────
B("B02","THE CORRECTION","SHELL",LIAM,
  "Reset. Same folder, same files, same ask. One flag change. Not a better prompt. Not a smaller model. Not fewer allowed tools. "
  "The same seven tools are on the allow-list. Only the permission mode changes — accept-edits becomes plan. Watch the loop's shape change with one flag.",
  "CCPlainShell — git reset, then the one flag change",
  R("CCPlainShell",{"title":"zsh — scratch/","lines":[
      "$ git reset --hard pristine",
      "HEAD is now at 4ef4d45 initial: tinycalc with bug",
      "$ diff calc.py evidence/before/calc.py",
      "# no diff — the loop's edits are gone",
      "# same ask. one flag change:",
      "#   --permission-mode acceptEdits",
      "#   --permission-mode plan"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the reset and the flag change happen outside the Claude session — REAL-SESSION LAW"),
  [{"at":0.05,"event":"reset"},{"at":0.55,"event":"one flag change"}])

# ───────── B03 · PLAN — the same ask, the loop stops ─────────
B("B03","PLAN — SAME ASK","TERMINAL",LIAM,
  "Same sentence. Plan mode. Two Reads — same files. A finding — the same bug. Then something acceptEdits never does: it writes the plan to a file. "
  "Then a tool call I've never seen before: ExitPlanMode, carrying the plan and the shell commands it would like next. And it stops. Exit plan mode? "
  "In headless there's nobody to answer. In the app, that is your keystroke.",
  "CCSession — plan run: 2 Reads, finding, Write plan, ExitPlanMode, waiting",
  R("CCSession", session("scratch — plan","plan",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"calc.py","state":"done"},
      {"type":"tool","name":"Read","arg":"test_calc.py","state":"done"},
      {"type":"text","text":"The bug in calc.py:2-3 — the"},
      {"type":"text","text":"guard returns 0 for negatives."},
      {"type":"text","text":"Writing the plan; not the fix."},
      {"type":"tool","name":"Write","arg":"~/.claude/plans/fix-the-bug.md","state":"done"},
      {"type":"tool","name":"ExitPlanMode","arg":"plan + allowedPrompts","state":"done"},
      {"type":"text","text":"Exit plan mode?  (waiting…)"},
  ],[0,90,115,145,170,195,225,255,285], mascot="off")),
  [{"at":0.05,"event":"Ask (same)"},{"at":0.4,"event":"finding"},{"at":0.75,"event":"Write plan; ExitPlanMode"},{"at":0.95,"event":"'Exit plan mode?'"}])

# ───────── B04 · PLAN — VERIFY (nothing in scratch, plan on disk) ─────────
B("B04","PLAN — VERIFY","SHELL",LIAM,
  "Check the plan run. Git status: nothing to commit — scratch is untouched. The plan is on disk, twenty-eight lines, at a path Claude chose, "
  "with context, change, and verify. And a tests-pass count of zero — because the tests never ran. Same ask. Zero writes to my repo. The loop stopped at gather.",
  "CCPlainShell — git status clean, wc plan, head plan, count",
  R("CCPlainShell",{"title":"zsh — after plan run","lines":[
      "$ git status --short",
      "# (empty — scratch is untouched)",
      "$ wc -l ~/.claude/plans/fix-the-bug*.md",
      "      28  fix-the-bug-in-virtual-bachman.md",
      "$ head -3 ~/.claude/plans/fix-the-bug*.md",
      "# Fix `add` bug in tinycalc",
      "## Context",
      "# 3 Reads · 1 plan · 0 writes to scratch"],
    "startCue":12,"lineGap":20}, motion="type",
    leaves_terminal_because="what the plan-mode session left behind, checked from a plain shell"),
  [{"at":0.05,"event":"git status clean"},{"at":0.5,"event":"plan on disk, 28 lines"},{"at":0.9,"event":"0 writes"}])

# ───────── B05 · CONDUCT — the Boondoggle Score ─────────
B("B05","CONDUCT — BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, two permission modes — the whole experiment. "
  "Claude did the loop: seven tools, in one turn; handoff was tests pass without a pause, and it met it. "
  "Step three, the dangerous middle: two files were mine before I could read either. Then me again: reset, and add one flag. "
  "Claude did the plan run: three Reads, one Write, then ExitPlanMode, and stopped. Then interpretive judgment: the same loop can close on its own or wait for a keystroke — I choose which.",
  "CCBoondoggleScore — six steps, dangerous middle at 3",
  R("CCBoondoggleScore",{"system":"one sentence · two permission modes","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence · two permission modes"},
      {"n":2,"phase":"C","labor":"claude","text":"Loop: 7 tools, 2 files, one turn","handoff":"tests pass without a pause","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the diff after — 5 lines, 2 files","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Reset · add --permission-mode plan","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Plan: 3 Reads · Write · ExitPlanMode","handoff":"waits on 'Exit plan mode?'","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"The loop stopped at gather","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

# ───────── B06 · HUMAN — the ledger ─────────
B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. Claude can run seven tools in one turn, and it will. It can close the loop without pausing, and it did. "
  "It should propose a plan before writes — it does, when I ask. It should wait on Exit plan mode — and it does. "
  "I must choose the permission mode; nobody else can pick it for a session on my repo. I must read the diff, not the summary — the summary is Claude's; the diff is mine. "
  "I must answer Exit plan mode myself. And I should reach for plan mode first, on anything I would not want undone by hand.",
  "CCHumanLedger — 4×4, closing",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"run seven tools per turn"},
      {"tier":"CAN","text":"close the loop without pause"},
      {"tier":"SHOULD","text":"propose a plan before writes"},
      {"tier":"SHOULD","text":"wait on 'Exit plan mode?'"}],
    "human":[
      {"tier":"MUST","text":"choose the permission mode"},
      {"tier":"MUST","text":"read the diff, not the summary"},
      {"tier":"MUST","text":"answer 'Exit plan mode?' myself"},
      {"tier":"SHOULD","text":"reach for plan mode first"}],
    "closing":"The loop is the loop. I choose the pause.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

# ───────── BVDT · verdict ─────────
B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence in accept-edits: seven tool calls, two files changed, tests pass — in one turn, no pause. "
  "Same sentence in plan mode: three Reads, one plan file, zero writes to my repo, and the loop stops on Exit plan mode. "
  "The loop is one design. Plan mode is the interruption point that lets a human read before act. "
  "What would prove this reel wrong: a plan-mode run that edits a file in scratch without a human answering Exit plan mode first.",
  "ClaudeVerdictArtifact — 4 lines",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Accept-edits: 7 tool calls, 2 files changed, 4 tests pass — one turn, no pause.",
      "Plan mode: 3 Reads, 1 plan file on disk, 0 writes to scratch — loop stops on 'Exit plan mode?'.",
      "The loop is one design; plan mode is the interruption point that lets a human read before act.",
      "FALSIFIABLE: a plan-mode run that edits a file in scratch without a human answering 'Exit plan mode?' first."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

# ───────── BHTF · your turn ─────────
B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next non-trivial edit, press Shift+Tab twice to enter plan mode, and type your ask. "
  "Read what it proposes. Then approve, or edit the plan first. Once. Notice how much of the loop you would have missed.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"Before your next non-trivial edit in Claude Code, press Shift+Tab twice to enter plan mode. Type your ask. Read what Claude proposes. Then approve it, or edit the plan first. Do it once. Notice how much of the loop you would have missed.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"try this in Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

# ───────── BOUT · title outro ─────────
B("BOUT","OUTRO","BOOKEND",LIAM,
  "The Loop Runs While You Read. Plan Mode Is The Pause. Liam, in for Bear.",
  "ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

# ───────── sheet + budget checks ─────────
sheet={"metadata":{"slug":SLUG,"title":TITLE,
    "subtitle":"Same one-sentence ask. Only --permission-mode changes. The loop's shape changes with the flag.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is",
    "audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown",
    "engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-code--claude-liam-vox-agentic-loop (the concept; body replaced by two real headless runs)",
    "sources":["SESSION.md (two real headless runs, 2026-09-09)",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
               "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
    "beats":beats}

here=os.path.dirname(os.path.abspath(__file__))
json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")

# ───────── budget asserts (exemplar shape) ─────────
warn=0
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44:
                print("  ⚠",b["beat_id"],"text",len(blk["text"]),blk["text"]); warn+=1
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>52:
                print("  ⚠",b["beat_id"],"shell-line",len(ln),ln); warn+=1
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>34:
                    print("  ⚠ ledger",len(row["text"]),row["text"]); warn+=1
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>46:
                print("  ⚠ step",len(st["text"]),st["text"]); warn+=1
        if len(r["props"]["steps"])>7:
            print("  ⚠ boondoggle exceeds 7 steps"); warn+=1
    if r["pattern"]=="CCDefinitions":
        for t in r["props"]["terms"]:
            if len(t["term"])>18: print("  ⚠ term",len(t["term"]),t["term"]); warn+=1
            if len(t["meaning"])>70: print("  ⚠ meaning",len(t["meaning"]),t["meaning"]); warn+=1
    if r["pattern"]=="ClaudeVerdictArtifact":
        n=len(r["props"]["artifactLines"])
        if n not in (4,6): print("  ⚠ verdict lines",n); warn+=1
if warn==0: print("budget: all clean.")
else: print(f"budget: {warn} warning(s) above.")
