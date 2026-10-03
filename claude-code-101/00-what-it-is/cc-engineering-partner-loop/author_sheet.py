#!/usr/bin/env python3
"""author_sheet.py — cc-engineering-partner-loop (cc-explainer · Claude Code 101 · tier 00, film — Engineering Partner Loop)
Two sessions on the same tiny module: bare fix, then the partner loop (plan → diff → verify) with a correction turn. Every block traces to SESSION.md. Liam, in for Bear."""
import json, os
SLUG="cc-engineering-partner-loop"
TITLE="Run the Engineering Partner Loop with Claude Code"
TOPIC="CLAUDE CODE 101"
LIAM="am_onyx"
WPS=2.9
ASK_BARE="Fix the failing tests."
ASK_PARTNER="Oracle is test_ranges.py. Don't edit. Give me the plan + exact diff."
beats=[]
def est(t): return round(len(t.split())/WPS+0.9,1)
def B(bid, act, lane, voice, narration, element, shot, show, **extra):
    b={"beat_id":bid,"act":act,"lane":lane,"narration_text":narration,"estimated_duration_s":est(narration),
       "voice":voice,"engine":"kokoro","voice_kokoro":voice,"new_visual_element":element,"shot":shot,"show":show}
    b.update(extra); beats.append(b)
def R(pattern, props, motion="type", **shot_extra):
    s={"type":"REMOTION","source":"own","motion":motion,
       "remotion":{"pattern":pattern,"props":props,"rendered":{"out":"","at":""}}}
    s.update(shot_extra); return s
def writer(text, trig, rep, seed):
    return {"text":text,"triggerWords":trig,"replacementWords":rep,"face":"serif","fontSize":78,"align":"center",
            "ink":"#F2F0E9","accent":"#D97757","bg":"#1F1E1B","seed":seed,
            "charMs":22,"hesitateBetween":6,"hesitateWithin":1,"mistakeRate":5,"jitter":20}
def session(title, mode, blocks, cues, mascot="off"):
    return {"title":title,"mode":mode,"blocks":blocks,"cues":cues,"mascot":mascot}

# ── B00 — COLD OPEN (bare loop, the whole quick thing) ────────────────────────
B("B00","COLD OPEN — BARE LOOP","TERMINAL",LIAM,
  "This is Liam, in for Bear. Two failing tests in a tiny file. One sentence — fix them. "
  "Claude reads the test, reads the code, edits, runs. Green. That's the whole loop. "
  "It worked. But I only saw the diff after it landed. That's the film.",
  "CCSession — bare cycle: ask, tools, edit, tests pass",
  R("CCSession", session("scratch — bare","accept-edits",[
      {"type":"prompt","text":ASK_BARE,"cue":0,"typeDuration":40},
      {"type":"tool","name":"Read","arg":"ranges.py","state":"done"},
      {"type":"tool","name":"Read","arg":"test_ranges.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"Two failures — reversed and extra"},
      {"type":"text","text":"dashes both need to raise."},
      {"type":"tool","name":"Edit","arg":"ranges.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"Ran 5 tests. OK."},
  ],[0,45,60,75,110,130,150,175,205], mascot="off")),
  [{"at":0.05,"event":"ask types"},{"at":0.45,"event":"Edit lands"},{"at":0.9,"event":"OK"}])

# ── BIDEA — THE IDEA ──────────────────────────────────────────────────────────
B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Claude Code is not a code generator. It's an engineering partner — "
  "if you run it as a loop with a gate you can approve. Oracle first: the test that says done. "
  "Then the plan, before the diff. Then the diff, before you run it. Then the oracle again. "
  "Same fix, different job for you: not debugging after, approving scope before.",
  "BrutalistHesitantWriter — 'generator' reconsidered into 'partner'",
  R("BrutalistHesitantWriter", writer(
      "Claude Code is a code generator.\nType a wish, get a change.\nRun it as a loop, with a gate.\nApprove scope before the diff, not after.",
      "generator","partner",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'generator' → 'partner'"},{"at":0.85,"event":"Last line"}])

# ── BDEFS — DEFINITIONS ───────────────────────────────────────────────────────
B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Oracle: a check you can run — here, a failing test that flips to pass when done. "
  "Plan: what Claude will change, in text, before any edit. Minimal diff: the smallest patch that makes the oracle green, nothing else. "
  "Scope: what may change and what may not, named up front. Engineering partner loop: oracle, ask, plan, diff, verify, decide — the five steps.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"oracle","meaning":"a check you can run; here a failing test that flips to pass when done"},
      {"term":"plan","meaning":"what Claude will change, in text, before any edit is made"},
      {"term":"minimal diff","meaning":"the smallest patch that makes the oracle green — nothing else"},
      {"term":"scope","meaning":"what may change and what may not, named up front"},
      {"term":"partner loop","meaning":"oracle, ask, plan, diff, verify, decide — the five gates"}],
    "startCue":12,"rowGap":48}, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

# ── B01 — BARE VERIFY (Liam's take on the anti-example) ───────────────────────
B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "My verify. Five green. Two guards added, seven lines changed. All fine. "
  "But watch when it happened: after the edit. I read the diff after Claude wrote it. "
  "If Claude had touched a second file, or picked a wrong scope, I would learn now. "
  "The gate I want is before the diff, not after.",
  "CCSession — Liam's plain-shell verify of the bare fix",
  R("CCSession", session("scratch — bare","default",[
      {"type":"prompt","text":"!python3 -m unittest -v","cue":0,"typeDuration":36},
      {"type":"text","text":"Ran 5 tests in 0.000s"},
      {"type":"text","text":"OK"},
      {"type":"prompt","text":"!git diff --stat ranges.py","cue":0,"typeDuration":36},
      {"type":"text","text":" ranges.py | 7 +++++--"},
      {"type":"text","text":" 1 file changed, 6 ins, 1 del"},
      {"type":"prompt","text":"!grep -c 'raise ValueError'","cue":0,"typeDuration":36},
      {"type":"text","text":"2"},
  ],[0,40,60,80,120,140,155,195], mascot="off")),
  [{"at":0.05,"event":"tests OK"},{"at":0.4,"event":"stat"},{"at":0.8,"event":"grep 2"}])

# ── B02 — PARTNER ASK ─────────────────────────────────────────────────────────
B("B02","PARTNER — ASK","TERMINAL",LIAM,
  "Reset. Same folder, same tests. Different ask. Read the oracle. Read the code. "
  "Do not edit yet. Give me the plan, and the exact diff, in fences. Stop after that. "
  "The plan is the gate. The edit is not allowed to happen until I say the word.",
  "CCSession — the partner ask; Edit tool withheld",
  R("CCSession", session("scratch — partner","default",[
      {"type":"prompt","text":ASK_PARTNER,"cue":0,"typeDuration":100},
      {"type":"tool","name":"Read","arg":"test_ranges.py","state":"done"},
      {"type":"tool","name":"Read","arg":"ranges.py","state":"done"},
      {"type":"status","verb":"Planning","elapsed":"0m 8s","tokens":"1.4k tokens"},
  ],[0,130,155,180], mascot="off")),
  [{"at":0.05,"event":"ask types"},{"at":0.7,"event":"Reads land"},{"at":0.95,"event":"Planning"}])

# ── B03 — PARTNER PLAN (the plan block, from run-partner-plan.jsonl) ──────────
B("B03","PARTNER — PLAN + DIFF","TERMINAL",LIAM,
  "The plan comes back. Four steps. If parts is not one or two, raise. If start is more than end, raise. "
  "Leave the one-part branch alone — the empty case already raises inside int. Nothing outside parse_range. "
  "And under the plan, the exact diff, in fences. Five added lines, one removed. I can approve this before it exists on disk.",
  "CCSession — plan block with the 4-step plan",
  R("CCSession", session("scratch — partner","default",[
      {"type":"plan","sections":[
          {"title":"MINIMAL CHANGE TO parse_range","numbered":True,"items":[
              {"text":"If len(parts) is not 1 or 2, raise ValueError","path":"ranges.py"},
              {"text":"On the 2-part branch, raise if start > end","path":"ranges.py"},
              {"text":"Leave the 1-part branch — int('') already raises"},
              {"text":"No changes outside parse_range"}]}]},
      {"type":"text","text":"Diff (5 added, 1 removed):"},
      {"type":"diff","file":"ranges.py","addCount":5,"delCount":1,"lines":[
          {"gutter":"-","text":"return (int(parts[0]), int(parts[1]))","kind":"del"},
          {"gutter":"+","text":"if len(parts) != 2:","kind":"add"},
          {"gutter":"+","text":"    raise ValueError('invalid range')","kind":"add"},
          {"gutter":"+","text":"start, end = int(parts[0]), int(parts[1])","kind":"add"},
          {"gutter":"+","text":"if start > end:","kind":"add"},
          {"gutter":"+","text":"    raise ValueError('reversed range')","kind":"add"}]},
  ],[0,180,210], mascot="off")),
  [{"at":0.05,"event":"Plan lands"},{"at":0.6,"event":"Diff lands"},{"at":0.95,"event":"Ready to approve"}])

# ── B04 — PARTNER APPLY ───────────────────────────────────────────────────────
B("B04","PARTNER — APPLY","TERMINAL",LIAM,
  "Approved. Apply the diff exactly as shown. Then run the oracle. Report only the summary line. "
  "Edit is now allowed. One tool call, one shell call, one line back.",
  "CCSession — Edit + Bash unittest",
  R("CCSession", session("scratch — partner","accept-edits",[
      {"type":"prompt","text":"Plan approved. Apply the diff exactly.","cue":0,"typeDuration":60},
      {"type":"tool","name":"Edit","arg":"ranges.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"Ran 5 tests in 0.000s"},
      {"type":"text","text":"OK"},
  ],[0,75,105,135,155], mascot="off")),
  [{"at":0.05,"event":"approve types"},{"at":0.5,"event":"Edit"},{"at":0.9,"event":"OK"}])

# ── B05 — CORRECTION: Liam's grep catches drift ───────────────────────────────
B("B05","CORRECTION — VERIFY CATCHES DRIFT","SHELL",LIAM,
  "One more verify. Grep the docstring. It still says empty or reversed is an error. "
  "It does not mention extra dashes — the second guard we just added. Docstring and code disagree. "
  "That is a defect the oracle cannot see, and I can. Re-prompt.",
  "CCPlainShell — grep on ranges.py; the docstring/code drift",
  R("CCPlainShell",{"title":"zsh — scratch","lines":[
      "$ grep '\"\"\"' ranges.py",
      "    \"\"\"Parse '1-5' -> (1, 5). '7' -> (7, 7).",
      "     '' or reversed is an error.\"\"\"",
      "$ grep -n 'raise ValueError' ranges.py",
      "7:        raise ValueError('invalid range')",
      "10:       raise ValueError('reversed range')",
      "# docstring: 2 errors named",
      "# code: 2 errors raised — a DIFFERENT 2",
      "# drift"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="Liam's plain shell audit; not a session — the drift is what the session cannot see about itself"),
  [{"at":0.05,"event":"grep docstring"},{"at":0.45,"event":"grep raises"},{"at":0.9,"event":"Drift"}])

# ── B06 — CORRECTION: docstring-only re-prompt ────────────────────────────────
B("B06","CORRECTION — RE-PROMPT","TERMINAL",LIAM,
  "New ask. Update only the docstring. No logic change. Show the diff. Run the oracle. "
  "Scope: one line. And that is what lands. Docstring now names the real errors. Green still.",
  "CCSession — docstring-only Edit + verify",
  R("CCSession", session("scratch — partner","accept-edits",[
      {"type":"prompt","text":"Docstring is stale. Update only the docstring. No logic change.","cue":0,"typeDuration":80},
      {"type":"tool","name":"Edit","arg":"ranges.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"git diff ranges.py","state":"done"},
      {"type":"text","text":"-  '' or reversed is an error"},
      {"type":"text","text":"+  '', reversed, or extra dashes"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"Ran 5 tests. OK."},
  ],[0,100,130,160,180,200,225], mascot="off")),
  [{"at":0.05,"event":"re-prompt"},{"at":0.4,"event":"diff"},{"at":0.9,"event":"OK"}])

# ── BFLOW — the five gates as a flow diagram ──────────────────────────────────
B("BFLOW","BFLOW — THE FIVE GATES","FLOW",LIAM,
  "The loop, drawn. Oracle: the test that says done. Ask: the sentence with scope in it. "
  "Plan: what Claude proposes, in text, before any edit. Diff: the exact change, before it runs. "
  "Verify: run the oracle again. Five gates. You approve every one. If any of them is missing, you are not conducting — you are watching.",
  "FlowDiagram — 5-node partner loop, terracotta on cream",
  R("FlowDiagram",{
    "skin":"claude",
    "kicker":"ENGINEERING PARTNER LOOP",
    "caption":"Five gates. You approve every one.",
    "pulse":True,
    "nodes":[
      {"id":"oracle","label":"ORACLE","sub":"defines done","tier":"data","x":40,"y":440,"w":320,"h":180,"hi":True},
      {"id":"ask","label":"ASK","sub":"scope named","tier":"client","x":420,"y":440,"w":320,"h":180},
      {"id":"plan","label":"PLAN","sub":"text, no edit","tier":"compute","x":800,"y":440,"w":320,"h":180,"hi":True},
      {"id":"diff","label":"DIFF","sub":"exact, no run","tier":"compute","x":1180,"y":440,"w":320,"h":180,"hi":True},
      {"id":"verify","label":"VERIFY","sub":"run oracle","tier":"data","x":1560,"y":440,"w":320,"h":180}],
    "edges":[
      {"from":"oracle","to":"ask","order":1,"kind":"flow"},
      {"from":"ask","to":"plan","order":2,"kind":"flow"},
      {"from":"plan","to":"diff","order":3,"kind":"flow"},
      {"from":"diff","to":"verify","order":4,"kind":"flow"}],
    "viewBox":{"w":1920,"h":1080}}, motion="drawon",
    leaves_terminal_because="BFLOW: the five gates are implied by the session but not drawn anywhere in it"),
  [{"at":0.05,"event":"Nodes"},{"at":0.5,"event":"Edges draw"},{"at":0.9,"event":"Pulse"}])

# ── BSHOW — what the oracle running actually looks like ───────────────────────
B("BSHOW","BSHOW — THE ORACLE, RUNNING","SHELL",LIAM,
  "And what the fifth gate looks like when you run it. Same command every cycle. Five tests, five OKs, one line at the bottom. "
  "That is the definition of done, on the terminal, and every cycle ends here — or the cycle is not done.",
  "CCPlainShell — real unittest -v output from evidence/verify.txt",
  R("CCPlainShell",{"title":"zsh — scratch · python3 -m unittest -v","lines":[
      "$ python3 -m unittest test_ranges -v",
      "test_empty_raises          ... ok",
      "test_extra_dash_raises     ... ok",
      "test_range                 ... ok",
      "test_reversed_raises       ... ok",
      "test_single_number         ... ok",
      "----------------------------------------",
      "Ran 5 tests in 0.000s",
      "",
      "OK"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="BSHOW: this is the real oracle output from evidence/verify.txt, held long enough to read"),
  [{"at":0.05,"event":"command"},{"at":0.4,"event":"five OKs"},{"at":0.95,"event":"OK holds"}])

# ── CONDUCT — the Boondoggle Score ────────────────────────────────────────────
B("BCND","CONDUCT — BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: name the oracle — pick the test that says done. "
  "Claude did the bare run; handoff was the oracle, and it met it. "
  "Dangerous middle, step three: I read the diff after it landed. If the scope had been wrong, this is when I would learn. "
  "Then the real work, mine: write the partner ask — same problem, plan required. "
  "Claude did the plan-first run; handoff was the diff in fences. And I caught the docstring drift the oracle could not see.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"the five-gate loop","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Name the oracle — pick the failing test"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare run — Edit lands, 5 green","handoff":"oracle green; but no plan surface","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the diff — after it landed","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write the partner ask — plan required","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Plan + diff in fences; then apply","handoff":"diff shown before edit; oracle green","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Grep catches docstring drift","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon",
    leaves_terminal_because="CONDUCT: the score is drawn from the session; the terminal does not draw it itself"),
  [{"at":0.05,"event":"Header"},{"at":0.35,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

# ── HUMAN — the ledger ────────────────────────────────────────────────────────
B("BHMN","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name the oracle — nobody else can decide what done means. "
  "I must approve the plan before the edit — that is the gate. I must read the diff, not the summary. "
  "I should catch drift the oracle cannot see — like a stale docstring. "
  "Claude can fix a failing test in one shot; it did. It should show the plan before the edit; it did, when I asked. "
  "It should stay in scope when scope is named; it did. It should run the oracle after the edit; it did.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"fix a failing test in one shot"},
      {"tier":"CAN","text":"write the plan before the edit"},
      {"tier":"SHOULD","text":"stay in the scope you named"},
      {"tier":"SHOULD","text":"run the oracle after each edit"}],
      "human":[
      {"tier":"MUST","text":"name the oracle"},
      {"tier":"MUST","text":"approve the plan before edit"},
      {"tier":"MUST","text":"read the diff, not the summary"},
      {"tier":"SHOULD","text":"catch drift the oracle misses"}],
      "closing":"The gate is before the diff, not after.","humanCue":70,"rowGap":12}, motion="drawon",
    leaves_terminal_because="HUMAN: the ledger is drawn from the session; the terminal does not draw it itself"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

# ── BVDT — VERDICT (4 lines, last = FALSIFIABLE) ─────────────────────────────
B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence in a folder with two failing tests: Claude fixes them in seven turns — I read the diff after. "
  "Same problem with an oracle-first ask that requires a plan: Claude writes the plan and the diff in text — I approve the scope before the edit exists. "
  "The diff is identical. What changed is the timing of my judgment. "
  "What would prove this reel wrong: a bare run that shows me the plan before the edit, unasked.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare run: fix works — but the diff lands before you see the plan.",
      "Partner loop: plan and diff in text — approve scope before edit exists.",
      "Same code, different job for you: not debugging after, approving before.",
      "FALSIFIABLE: a bare run that shows the plan before the edit, unasked."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}],
  lead_silence_s=0.5)

# ── BHTF — YOUR TURN ─────────────────────────────────────────────────────────
B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next fix, open Claude Code and paste this: "
  "The oracle is my failing test. Read it and the code around it. Do not edit yet. "
  "Give me a numbered plan and the exact diff, in fences, for the minimal change. Nothing outside the target function. Stop after the plan.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{
      "greeting":"Your turn.",
      "command":"The oracle is my failing test. Read it and the code around it. Do not edit yet. Give me a numbered plan and the exact diff, in fences, for the minimal change. Nothing outside the target function. Stop after the plan.",
      "segment":TITLE,
      "topic":"YOUR TURN · "+TOPIC,
      "runningText":"paste this into Claude Code…",
      "output":[],
      "folderLabel":"@NikBearBrown",
      "modelLabel":"Opus 5",
      "effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

# ── BOUT — OUTRO ─────────────────────────────────────────────────────────────
B("BOUT","OUTRO","BOOKEND",LIAM,
  "Run the Engineering Partner Loop with Claude Code. Liam, in for Bear.",
  "ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

# ── Emit sheet ────────────────────────────────────────────────────────────────
sheet={"metadata":{"slug":SLUG,"title":TITLE,
    "subtitle":"Same tiny bug, two loops. In the bare loop, you read the diff after it lands. In the partner loop, you approve the plan before the diff exists.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is",
    "audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown",
    "engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md",
    "build":True,
    "derived_from":"claude-code-101/00-what-it-is/claude-code--claude-liam-engineering-partner-loop (concept; body replaced by real headless runs)",
    "sources":["SESSION.md (two real sessions)",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
               "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
    "beats":beats}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")

# ── Budget asserts (kit gotchas) ─────────────────────────────────────────────
warn=0
for b in beats:
    r=b["shot"]["remotion"]
    pat=r["pattern"]; props=r["props"]
    if pat=="CCSession":
        assert len(props["blocks"])==len(props["cues"]), b["beat_id"]
        for blk in props["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44:
                print(f"  ⚠ {b['beat_id']} text {len(blk['text'])} chars: {blk['text']}"); warn+=1
            if blk["type"]=="prompt" and len(blk["text"])>140:
                print(f"  ⚠ {b['beat_id']} prompt {len(blk['text'])} chars"); warn+=1
    if pat=="CCPlainShell":
        for ln in props["lines"]:
            if len(ln)>48:
                print(f"  ⚠ {b['beat_id']} shell-line {len(ln)}: {ln}"); warn+=1
    if pat=="CCHumanLedger":
        for c in ("ai","human"):
            for row in props[c]:
                if len(row["text"])>34:
                    print(f"  ⚠ ledger {c} {len(row['text'])}: {row['text']}"); warn+=1
        if props.get("closing") and len(props["closing"])>52:
            print(f"  ⚠ ledger closing {len(props['closing'])}: {props['closing']}"); warn+=1
    if pat=="CCBoondoggleScore":
        if len(props.get("system",""))>28:
            print(f"  ⚠ boondoggle system {len(props['system'])}: {props['system']}"); warn+=1
        for st in props["steps"]:
            if len(st["text"])>46:
                print(f"  ⚠ step {st['n']} {len(st['text'])}: {st['text']}"); warn+=1
            if st.get("handoff") and len(st["handoff"].split())>22:
                print(f"  ⚠ handoff step {st['n']} words: {st['handoff']}"); warn+=1
    if pat=="ClaudeVerdictArtifact":
        n=len(props["artifactLines"])
        assert n in (4,6), f"{b['beat_id']} verdict must have 4 or 6 lines, got {n}"
    if pat=="CCDefinitions":
        for t in props["terms"]:
            if len(t["term"])>18:
                print(f"  ⚠ defn term {len(t['term'])}: {t['term']}"); warn+=1
            if len(t["meaning"])>78:
                print(f"  ⚠ defn meaning {len(t['meaning'])}: {t['meaning']}"); warn+=1
print(f"budget warnings: {warn}")
