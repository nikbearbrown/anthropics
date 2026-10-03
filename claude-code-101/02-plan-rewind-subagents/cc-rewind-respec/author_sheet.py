#!/usr/bin/env python3
"""author_sheet.py — cc-rewind-respec (cc-explainer · Claude Code 101 · tier 02, film 03)
"Why Rewriting the Wrong Fix Makes the Build Worse, Not Better."
Every block traces to SESSION.md (four real runs: FF1/FF2/FF3 chained via --resume, then respec fresh). Liam, in for Bear."""
import json, os
SLUG="cc-rewind-respec"
TITLE="Why Rewriting the Wrong Fix Makes the Build Worse, Not Better"
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="The dedupe tests in test_dedupe.py are failing. Fix dedupe.py."
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

# ── B00 COLD OPEN — FF3's clever one-liner passes tests, but Liam's check reveals the drift.
B("B00","COLD OPEN — THE DRIFT","TERMINAL",LIAM,
  "This is Liam, in for Bear. Three fixes in, the tests pass — but the diff is a one-line dictionary keyed by repr. "
  "So I check it. Dedupe of one and one-point-zero. Equal in Python. Should collapse. It doesn't. "
  "The tests never asked. The fence let it through. And I only found it because I read the diff.",
  "CCSession — the FF3 result: pass, then Liam's one and one-point-zero check fails",
  R("CCSession", session("dedupe — after three fixes","default",[
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_dedupe.py","state":"done"},
      {"type":"text","text":"Ran 3 tests in 0.000s"},
      {"type":"text","text":"OK"},
      {"type":"prompt","text":"cat dedupe.py","cue":0,"typeDuration":32},
      {"type":"text","text":"def dedupe(items):"},
      {"type":"text","text":"    return list({repr(x): x"},
      {"type":"text","text":"                 for x in items}.values())"},
      {"type":"prompt","text":"python3 -c 'from dedupe import dedupe; print(dedupe([1,1.0]))'","cue":0,"typeDuration":90},
      {"type":"text","text":"[1, 1.0]"},
  ],[0,40,60,80,120,140,165,195,270], mascot="off")),
  [{"at":0.05,"event":"unittest → OK"},{"at":0.4,"event":"the repr one-liner"},{"at":0.85,"event":"[1, 1.0] — not [1]"}])

# ── BIDEA — the misconception the film exists to fix.
B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. When a fix from Claude passes the tests but you can tell it drifted, the move isn't to type fix it again. "
  "Every follow-up types on top of the wrong answer, and the context pushes Claude toward variations on what already passed — not toward the answer that was never tried. "
  "Rewind to the checkpoint. Start a fresh session. And respecify the ask with the failure mode named as a constraint. Same model. Different context. First try, right.",
  "BrutalistHesitantWriter — 'fix it again' reconsidered into 'respecify it'",
  R("BrutalistHesitantWriter", writer("Three fixes in, tests still pass.\nAnd the diff has drifted.\nThe next move isn't fix it again.\nRewind. Respecify. Fresh session.","fix it again","respecify it",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'fix it again' → 'respecify it'"},{"at":0.85,"event":"Last line"}])

# ── BDEFS — the five words a chat-window user needs.
B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Fix-forward: replying to a Claude answer with another correction in the same session — the failure history stays in context. "
  "Slash rewind: Claude Code's interactive command that restores the conversation and the file system to a checkpoint. Headless, the equivalent is git reset plus a new session. "
  "Respecify: rewrite the ask with everything you learned. Context pollution: prior failures Claude reasons against as if they were requirements. "
  "Negative constraint: a line in the ask that names what the answer must not do.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"fix-forward","meaning":"reply with another correction in the same session — history stays in context"},
      {"term":"/rewind","meaning":"interactive command restoring conversation + files to a checkpoint"},
      {"term":"respecify","meaning":"rewrite the ask with what you learned; a new plan, not another turn"},
      {"term":"context pollution","meaning":"prior failures Claude reasons against as if they were requirements"},
      {"term":"negative constraint","meaning":"a line in the ask naming what the answer must not do"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.55,"event":"Terms land"},{"at":0.95,"event":"Hold"}])

# ── B01 · Cycle 1 · FF1 — the vague ask.  PROMPT + Reads + Write + status.
B("B01","FF1 — THE VAGUE ASK","TERMINAL",LIAM,
  "The buggy start. Dedupe of one, two, three, two, one; list of set — sets don't preserve order. And a list of lists breaks because lists aren't hashable. "
  "The ask I type is the one a teacher would type. The tests are failing — fix dedupe.py. That's it. No spec, no failure mode, no constraint.",
  "CCSession — the vague ask: Reads, Write linear-scan",
  R("CCSession", session("dedupe — FF1, fresh session","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Bash","arg":"ls scratch/","state":"done"},
      {"type":"tool","name":"Read","arg":"test_dedupe.py","state":"done"},
      {"type":"tool","name":"Read","arg":"dedupe.py","state":"done"},
      {"type":"tool","name":"Read","arg":"SPEC.md","state":"done"},
      {"type":"tool","name":"Write","arg":"dedupe.py","state":"done"},
  ],[0,95,120,145,170,200], mascot="off")),
  [{"at":0.1,"event":"The ask types"},{"at":0.55,"event":"Reads"},{"at":0.9,"event":"Write dedupe.py"}])

B("B02","FF1 — VERIFY","TERMINAL",LIAM,
  "The output. A linear scan: if item not in result, append it. In is Python's equality operator, so lists work; the loop preserves order. "
  "It's slow — order n squared. But it's right. Three tests. Three pass. Claude even says: in uses equality, so lists work. Fine.",
  "CCSession — the code + unittest → 3 pass",
  R("CCSession", session("dedupe — FF1 verify","default",[
      {"type":"prompt","text":"cat dedupe.py","cue":0,"typeDuration":32},
      {"type":"text","text":"def dedupe(items):"},
      {"type":"text","text":"    result = []"},
      {"type":"text","text":"    for item in items:"},
      {"type":"text","text":"        if item not in result:"},
      {"type":"text","text":"            result.append(item)"},
      {"type":"text","text":"    return result"},
      {"type":"prompt","text":"python3 -m unittest test_dedupe.py","cue":0,"typeDuration":70},
      {"type":"text","text":"Ran 3 tests in 0.000s — OK"},
  ],[0,32,52,72,92,112,132,160,240], mascot="off")),
  [{"at":0.05,"event":"cat dedupe.py"},{"at":0.7,"event":"unittest → OK"}])

# ── B03 · Cycle 2 · FF2 — same session, "speed it up".
B("B03","FF2 — SPEED IT UP","TERMINAL",LIAM,
  "Now I follow up. Same session, resume by id — the context carries. That's order n squared. Speed it up for large lists. "
  "Claude rewrites it: a set for the fast items, a list for the unhashable ones, a try-except deciding which. Tests still pass. This is actually good.",
  "CCSession — --resume prompt, Write two-branch",
  R("CCSession", session("dedupe — FF2, --resume","accept-edits",[
      {"type":"prompt","text":"That's O(n squared). Speed it up.","cue":0,"typeDuration":78},
      {"type":"tool","name":"Write","arg":"dedupe.py","state":"done"},
      {"type":"prompt","text":"python3 -m unittest test_dedupe.py","cue":0,"typeDuration":70},
      {"type":"text","text":"Ran 3 tests in 0.000s — OK"},
      {"type":"text","text":"Now O(n) for hashable items;"},
      {"type":"text","text":"linear scan only for unhashable."},
  ],[0,90,120,190,220,244], mascot="off")),
  [{"at":0.1,"event":"The follow-up types"},{"at":0.55,"event":"Write"},{"at":0.9,"event":"Claude's summary"}])

# ── B04 · Cycle 3 · FF3 — the correction that drifts.  Same session, "simpler."
B("B04","FF3 — SIMPLER — THE CORRECTION","TERMINAL",LIAM,
  "One more. Same session — the two failures are still in context, plus the last successful answer. Simpler. One data structure. "
  "Claude comes back with a one-liner. A dict keyed by repr of x, values are x, take the values. Every item — hashable or not — gets a string key. Clever. Tests pass.",
  "CCSession — --resume prompt, Write repr one-liner",
  R("CCSession", session("dedupe — FF3, --resume","accept-edits",[
      {"type":"prompt","text":"Simpler. One data structure.","cue":0,"typeDuration":66},
      {"type":"tool","name":"Write","arg":"dedupe.py","state":"done"},
      {"type":"prompt","text":"cat dedupe.py","cue":0,"typeDuration":32},
      {"type":"text","text":"def dedupe(items):"},
      {"type":"text","text":"    return list({repr(x): x"},
      {"type":"text","text":"                 for x in items}.values())"},
      {"type":"prompt","text":"python3 -m unittest test_dedupe.py","cue":0,"typeDuration":70},
      {"type":"text","text":"Ran 3 tests in 0.000s — OK"},
  ],[0,80,110,140,160,185,220,290], mascot="off")),
  [{"at":0.1,"event":"'Simpler'"},{"at":0.4,"event":"repr one-liner"},{"at":0.9,"event":"tests OK"}])

# ── B05 · The drift — Liam's verify is a command the tests didn't have.
B("B05","FF3 — VERIFY, AND THE DRIFT","TERMINAL",LIAM,
  "Now the check the tests don't run. One and one-point-zero — equal in Python. Should collapse to a single item. "
  "The repr version keeps both, because the string one is not the string one-point-zero. Same for True and one. The tests never asked. Claude even said it in the reply — the caveat is right there. But the fence let it through.",
  "CCSession — Liam's [1, 1.0] and [True, 1] checks show the drift",
  R("CCSession", session("dedupe — the check the tests didn't have","default",[
      {"type":"prompt","text":"python3 -c \"from dedupe import dedupe; print(dedupe([1,1.0]))\"","cue":0,"typeDuration":110},
      {"type":"text","text":"[1, 1.0]"},
      {"type":"prompt","text":"python3 -c \"from dedupe import dedupe; print(dedupe([True,1]))\"","cue":0,"typeDuration":110},
      {"type":"text","text":"[True, 1]"},
      {"type":"text","text":"# both should collapse under =="},
      {"type":"text","text":"# repr(1) != repr(1.0). The tests"},
      {"type":"text","text":"# never checked. Claude even said so."},
  ],[0,120,150,270,300,325,355], mascot="off")),
  [{"at":0.1,"event":"[1, 1.0]"},{"at":0.5,"event":"[True, 1]"},{"at":0.9,"event":"the tests never checked"}])

# ── B06 · The mechanism beat — context pollution shown in the shell (CCPlainShell).
B("B06","WHY IT DRIFTED — THE POLLUTED SESSION","SHELL",LIAM,
  "Why did simpler produce clever? The session carries every prior turn — the linear scan, the two-branch fast path, and its own passing tests. "
  "Simpler landed on all of that. The context said: cleverer than what already worked. The tests couldn't say: same equality as before. That's context pollution.",
  "CCPlainShell — the session log growing across three resumes",
  R("CCPlainShell",{"title":"session context — a09ae7ad","lines":[
      "$ claude-code session view a09ae7ad",
      "turn 1  ask: the dedupe tests fail. fix.",
      "        answer: linear scan       PASS",
      "turn 2  ask: O(n^2). speed it up.",
      "        answer: two-branch try/exc  PASS",
      "turn 3  ask: simpler. one data structure.",
      "        answer: dict keyed by repr  PASS",
      "context carries: 3 PASS handoffs + diff.",
      "# next prompt reasons against all of it",
      "# as if it were the spec.",
  ],"startCue":10,"lineGap":24}, motion="type",
    leaves_terminal_because="the growing session log is the mechanism; a single terminal beat can't hold three turns at once"),
  [{"at":0.05,"event":"turn 1"},{"at":0.5,"event":"turn 3 — 'simpler'"},{"at":0.9,"event":"context carries"}])

# ── B07 · The rewind — git reset + fresh session-id. CCPlainShell.
B("B07","REWIND — RESTORE THE CHECKPOINT","SHELL",LIAM,
  "Rewind. Two commands. Git reset the scratch to the buggy start — the files are back where they were. "
  "Then a new session id, no resume. The skill's own words: a new claude-p is a fresh session — that's slash clear. Conversation gone, files restored. Ready to respecify.",
  "CCPlainShell — git reset + new session-id",
  R("CCPlainShell",{"title":"zsh — the rewind","lines":[
      "$ git reset --hard f5ef78b",
      "HEAD is now at f5ef78b buggy start",
      "$ cat dedupe.py",
      "def dedupe(items):",
      "    return list(set(items))",
      "$ SID=$(uuidgen | tr A-Z a-z)",
      "$ echo $SID",
      "96c45930-f2c9-4a95-b152-e01653e11d07",
      "# no --resume. a new claude -p is /clear.",
  ],"startCue":10,"lineGap":24}, motion="type",
    leaves_terminal_because="the rewind is a shell action outside the session — git + a new session id"),
  [{"at":0.1,"event":"git reset"},{"at":0.5,"event":"buggy start restored"},{"at":0.9,"event":"new session id"}])

# ── B08 · Respec — the fresh session with failure named as constraint.
B("B08","RESPEC — THE FAILURE AS CONSTRAINT","TERMINAL",LIAM,
  "The respec. The same original ask — plus the failure the tests couldn't catch, named as a constraint. "
  "Preserve order. Handle unhashable. Equality is double-equals, not repr — so one, one-point-zero must collapse to one. Use hashing with a linear-scan fallback. Don't modify the test.",
  "CCSession — the fresh session, respec typed",
  R("CCSession", session("dedupe — respec, fresh session","accept-edits",[
      {"type":"prompt","text":"Fix dedupe.py so that: order preserved;","cue":0,"typeDuration":100},
      {"type":"prompt","text":"unhashable items work; equality is ==, not","cue":0,"typeDuration":100},
      {"type":"prompt","text":"repr — dedupe([1,1.0]) must return [1].","cue":0,"typeDuration":90},
      {"type":"prompt","text":"Hashing with linear-scan fallback.","cue":0,"typeDuration":80},
      {"type":"tool","name":"Read","arg":"dedupe.py","state":"done"},
      {"type":"tool","name":"Read","arg":"test_dedupe.py","state":"done"},
      {"type":"tool","name":"Write","arg":"dedupe.py","state":"done"},
  ],[0,110,220,320,410,435,460], mascot="off")),
  [{"at":0.1,"event":"the respec types"},{"at":0.7,"event":"Reads"},{"at":0.9,"event":"Write"}])

# ── B09 · Respec — VERIFY.  Tests + the [1, 1.0] check.
B("B09","RESPEC — VERIFY","TERMINAL",LIAM,
  "The verify. Three tests pass. And now the check the tests didn't have — one and one-point-zero returns one. True and one returns True. "
  "Same model. Same tests. Different context — the failure mode named as a line in the ask. One shot, right.",
  "CCSession — unittest → OK; [1, 1.0] → [1]",
  R("CCSession", session("dedupe — respec verify","default",[
      {"type":"prompt","text":"python3 -m unittest test_dedupe.py","cue":0,"typeDuration":70},
      {"type":"text","text":"Ran 3 tests in 0.000s — OK"},
      {"type":"prompt","text":"python3 -c \"from dedupe import dedupe; print(dedupe([1,1.0]))\"","cue":0,"typeDuration":110},
      {"type":"text","text":"[1]"},
      {"type":"prompt","text":"python3 -c \"from dedupe import dedupe; print(dedupe([True,1]))\"","cue":0,"typeDuration":110},
      {"type":"text","text":"[True]"},
  ],[0,80,110,230,260,380], mascot="off")),
  [{"at":0.05,"event":"unittest → OK"},{"at":0.4,"event":"[1]"},{"at":0.85,"event":"[True]"}])

# ── B10 · CONDUCT — the Boondoggle Score. Seven steps, dangerous middle = 4.
B("B10","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine — the vague ask. Step two, Claude — linear scan; handoff, tests pass. Step three, Claude — two-branch fast path; still passing. "
  "Step four, the dangerous middle: simpler landed on all of that and became clever. Tests still passed. Nothing in the fence caught it. "
  "Step five, mine — plausibility auditing: I ran the check the tests didn't have. Step six, mine — interpretive judgment: rewind, don't iterate. "
  "Step seven, Claude — respec; handoff, tests pass and one and one-point-zero collapses. Tool orchestration: zero. Executive integration: zero. One page, honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"3 fix-forward · 1 respec","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Vague ask: 'fix it'"},
      {"n":2,"phase":"C","labor":"claude","text":"FF1: linear scan","handoff":"tests pass","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"claude","text":"FF2: two-branch fast path","handoff":"tests still pass","dependsOn":[2]},
      {"n":4,"phase":"C","labor":"claude","text":"FF3: repr one-liner","handoff":"passes tests, semantics drift","dependsOn":[3]},
      {"n":5,"phase":"H","labor":"human","capacity":"PA","text":"Check the tests don't run","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Rewind, don't iterate","dependsOn":[5]},
      {"n":7,"phase":"C","labor":"claude","text":"Respec fresh: two branches","handoff":"tests pass; [1,1.0] collapses","dependsOn":[6]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 4 rings"},{"at":0.95,"event":"Tally"}])

# ── B11 · HUMAN — the ledger.  MUST/SHOULD human, CAN/SHOULD AI.
B("B11","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must run the check the tests can't. I must decide when the diff has drifted, even when it's green. I must choose rewind over another turn — no one else can. "
  "I should stop resuming after two prior fixes on the same target. Claude can produce clever code the tests will pass — and it will. It can name a caveat in its own reply — it did. "
  "It should carry a named negative constraint into a fresh session — it does. It should hand back the fallback branch without being reminded. That's the trade.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"write clever, tests-pass code"},{"tier":"CAN","text":"name a caveat in its reply"},
                          {"tier":"SHOULD","text":"honor a negative constraint"},{"tier":"SHOULD","text":"keep the fallback branch"}],
                    "human":[{"tier":"MUST","text":"run the check tests can't"},{"tier":"MUST","text":"see when the diff drifted"},
                             {"tier":"MUST","text":"rewind, not another turn"},{"tier":"SHOULD","text":"stop resuming after two fixes"}],
                    "closing":"Rewind. Respecify. Fresh session. Same model, different context.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

# ── BVDT — the verdict. 4 lines, last one FALSIFIABLE.
B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Fix-forward through three resumes: linear scan, two-branch, repr one-liner — tests pass all the way, and the last one silently changed equality. "
  "Rewind: git reset the checkpoint, a fresh session id, no resume — the skill's rule is that a new claude-p is slash clear. Respec: the same ask plus the failure mode named as a constraint. Respec ran once. It was right. "
  "What would prove this reel wrong: a fix-forward third turn that keeps the two-branch equality without being told to.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Fix-forward three times: linear → two-branch → repr one-liner. Tests pass all the way; the last one drifted on ==.",
      "Rewind: git reset --hard <checkpoint>; a new session id, no --resume. A new `claude -p` is /clear.",
      "Respec: the original ask plus the failure mode as a constraint ('== not repr; [1,1.0] must return [1]'). One turn, right.",
      "FALSIFIABLE: a fix-forward third turn that keeps the two-branch equality without being told to."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.25,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

# ── BHTF — Your turn.
B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Next time a Claude fix passes your tests but you're not sure — before you type fix it again, open Claude Code and paste this: "
  "here's the diff and the test file. Name three checks the tests don't run that would catch a wrong-but-passing answer. Then rewrite my original ask with each of those as a negative constraint.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"Here's the diff and the test file. Name three checks the tests don't run that would catch a wrong-but-passing answer. Then rewrite my original ask with each of those as a negative constraint.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.7,"event":"Send arms"}])

# ── BOUT — outro.
B("BOUT","OUTRO","BOOKEND",LIAM,"Why Rewriting the Wrong Fix Makes the Build Worse, Not Better. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.6,"event":"Mascot"}])

# ── Sheet + budget asserts.
sheet={"metadata":{"slug":SLUG,"title":TITLE,
    "subtitle":"Three fix-forward turns land on clever code the tests never checked. One rewind + respec fixes it clean.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"02-plan-rewind-subagents","audience":"NikBearBrown",
    "folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,
    "persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-vox-rewind-respec (concept only; scratch, evidence and beats are fresh)",
    "sources":["SESSION.md (four real runs: FF1/FF2/FF3 via --resume, respec fresh)",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
               "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
    "beats":beats}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(sheet, open(os.path.join(here,"beat_sheet.json"),"w"), indent=2, ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
warned=0
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), (b["beat_id"], len(r["props"]["blocks"]), len(r["props"]["cues"]))
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44:
                print(f"  ⚠ text {b['beat_id']} {len(blk['text'])}: {blk['text']}"); warned+=1
            if blk["type"]=="prompt" and len(blk["text"])>90:
                print(f"  ⚠ prompt {b['beat_id']} {len(blk['text'])}: {blk['text']}"); warned+=1
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>52:
                print(f"  ⚠ shell-line {b['beat_id']} {len(ln)}: {ln}"); warned+=1
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30:
                    print(f"  ⚠ ledger {b['beat_id']} {len(row['text'])}: {row['text']}"); warned+=1
    if r["pattern"]=="CCBoondoggleScore":
        if len(r["props"]["system"])>28:
            print(f"  ⚠ score-system {b['beat_id']} {len(r['props']['system'])}: {r['props']['system']}"); warned+=1
        for st in r["props"]["steps"]:
            if len(st["text"])>44:
                print(f"  ⚠ step {b['beat_id']} {len(st['text'])}: {st['text']}"); warned+=1
            if st.get("handoff") and len(st["handoff"])>44:
                print(f"  ⚠ handoff {b['beat_id']} {len(st['handoff'])}: {st['handoff']}"); warned+=1
    if r["pattern"]=="ClaudeVerdictArtifact":
        n = len(r["props"]["artifactLines"])
        assert n in (4, 6), (b["beat_id"], "verdict must be 4 or 6 lines", n)
print(f"warnings: {warned}")
