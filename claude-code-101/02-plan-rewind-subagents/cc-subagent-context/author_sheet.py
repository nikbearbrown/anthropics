#!/usr/bin/env python3
"""author_sheet.py — cc-subagent-context (cc-explainer · Claude Code 101 · tier 02)
"Why One Subagent Query Saved 48% of the Context Window."
Every block traces to SESSION.md (two real fresh headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-subagent-context"
TITLE="Why One Subagent Query Saved 48% of the Context Window"
TOPIC="CLAUDE CODE 101"
LIAM="am_onyx"
WPS=2.9
ASK="Add late_penalty() to grader.py from the study group's policies."
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

B("B00","COLD OPEN","TERMINAL",LIAM,
  "This is Liam, in for Bear. Same tiny build twice. Five policy documents in a folder; a function to add. "
  "First run — read them all, write the code. Second run — hand the reading to a subagent, take its summary, write the code. "
  "The mechanism is real: the subagent's window is separate from mine. The mechanism cost me nothing this time.",
  "CCSession — the ask, and the two runs about to happen",
  R("CCSession", session("studygroup — the two runs","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Glob","arg":"policies/*.md","state":"done"},
      {"type":"text","text":"5 policy docs, 156 lines total"},
      {"type":"text","text":"run 1: read them all in main"},
      {"type":"text","text":"run 2: delegate reads to subagent"},
      {"type":"text","text":"same task, two token bills"},
  ],[0,80,110,140,170,200], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.4,"event":"'5 policy docs'"},{"at":0.85,"event":"'same task, two token bills'"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea. A subagent is a separate Claude session with its own window; it reads what you tell it and returns a summary. "
  "The concept says it saves context — the source docs live in the subagent's window, not yours. It does. "
  "And then Claude opens the source docs in your window anyway, to double-check. The subagent isolates; only the human enforces.",
  "BrutalistHesitantWriter — 'saved' reconsidered into 'isolated'",
  R("BrutalistHesitantWriter", writer("A subagent saved my context window.\nIt didn't — the mechanism did.\nThe subagent isolates the reads.\nThe human enforces the boundary.","saved","isolated",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'saved' → 'isolated'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words. Main session: the Claude Code window I'm typing into — its context is my working memory for this build. "
  "Subagent: a separate Claude session I can launch with the Agent tool, with its own context window that never touches mine. "
  "Return summary: the only thing the subagent puts back into my window; the reads stay in its window. "
  "Tool boundary: what my session is allowed to do — Read, Edit, Bash — and what it isn't.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"main session","meaning":"the window I'm typing into; its context is my working memory"},
      {"term":"subagent","meaning":"a separate Claude session with its own isolated context window"},
      {"term":"return summary","meaning":"the only thing the subagent puts back into my window"},
      {"term":"tool boundary","meaning":"what my session is allowed to do — the human sets it"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","INLINE — THE BILL","TERMINAL",LIAM,
  "Run one. Read every policy, write the function. Watch the reads land. "
  "Late-submissions, four hundred twenty-four tokens; honor-code, seven hundred twenty-four; meeting-notes, six twenty-four; participation, six eighty-eight; syllabus, eight-oh-six. "
  "Five reads. Three thousand two hundred sixty-six tokens of policy, now sitting in my window for the rest of the build.",
  "CCSession — the five Reads with token counts",
  R("CCSession", session("run 1 — inline","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Read","arg":"policies/late-submissions.md","state":"done"},
      {"type":"text","text":"+424 tokens into main"},
      {"type":"tool","name":"Read","arg":"policies/honor-code.md","state":"done"},
      {"type":"text","text":"+724 tokens"},
      {"type":"tool","name":"Read","arg":"policies/meeting-notes.md","state":"done"},
      {"type":"text","text":"+624 tokens"},
      {"type":"tool","name":"Read","arg":"policies/participation.md","state":"done"},
      {"type":"text","text":"+688 tokens"},
      {"type":"tool","name":"Read","arg":"policies/syllabus.md","state":"done"},
      {"type":"text","text":"+806 tokens · total 3,266"},
  ],[0,60,90,110,140,160,190,210,240,260,290], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.4,"event":"Reads land"},{"at":0.9,"event":"'total 3,266'"}])

B("B02","INLINE — BUILD, VERIFY","TERMINAL",LIAM,
  "Now build. Edit grader.py, edit test_grader.py, run the tests. "
  "Four tests pass. The function is right. The one-day-late case: base score, minus ten percent. Correct. "
  "And every one of those three thousand tokens is still in my window. If I keep working, they come with me.",
  "CCSession — Edit, Edit, python3 -m unittest → OK, 4 tests",
  R("CCSession", session("run 1 — inline","accept-edits",[
      {"type":"tool","name":"Edit","arg":"grader.py","state":"done"},
      {"type":"tool","name":"Edit","arg":"test_grader.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_grader -v","state":"done"},
      {"type":"text","text":"test_late_penalty_one_day … ok"},
      {"type":"text","text":"test_letter_a … ok"},
      {"type":"text","text":"test_letter_f … ok"},
      {"type":"text","text":"test_score_sums_correct_points … ok"},
      {"type":"text","text":"Ran 4 tests · OK"},
  ],[0,40,80,110,140,170,200,240], mascot="off")),
  [{"at":0.05,"event":"Edits"},{"at":0.45,"event":"tests run"},{"at":0.85,"event":"OK"}])

B("B03","THE MECHANISM","SHELL",LIAM,
  "Here is what the subagent actually is. My session — the main one — is a window filling up with everything I read. "
  "The subagent is a second window. I ask it a question; it reads whatever it needs, in its own window; it hands me back a summary. "
  "Its reads never enter my window. Only the summary does. That's the whole trick — and the whole promise.",
  "CCPlainShell — the mechanism, one screen",
  R("CCPlainShell",{"title":"the mechanism","lines":[
      "$ # inline research",
      "  main session ────── Read × 5 ─────── policies (in main)",
      "                                       3,266 tokens IN",
      "",
      "$ # subagent research",
      "  main session ──Agent──▶  subagent    Read × 5",
      "                             │         (in subagent)",
      "                             ▼",
      "                          summary                     ",
      "                        ~130 words                    ",
      "                             │                        ",
      "  main session ◀────────────┘  435 tokens IN          "],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the mechanism is not a screen the session shows; it is the topology behind the two runs"),
  [{"at":0.05,"event":"Inline diagram"},{"at":0.5,"event":"Subagent diagram"},{"at":0.9,"event":"'summary only'"}])

B("B04","SUBAGENT — THE PROMISE","TERMINAL",LIAM,
  "Run two. One Agent call. The subagent goes off, reads all five, writes its summary. Waits about twelve seconds. "
  "Then this comes back into my window: one hundred twenty-nine words. Late-submissions rules, day by day, the fifty-percent floor, the grace hour. Everything the function needs. "
  "Four hundred and thirty-five tokens. Eight times smaller than reading the files myself.",
  "CCSession — the Agent call and its return",
  R("CCSession", session("run 2 — subagent","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Agent","arg":"Summarize late-submission policies","state":"done"},
      {"type":"text","text":"subagent: Read × 5, own window"},
      {"type":"text","text":"↩ summary returned to main:"},
      {"type":"text","text":"grace hour · day 1: 10% off"},
      {"type":"text","text":"day 2: 20% · d3-6: +5%/day"},
      {"type":"text","text":"day 7+: 50% floor · rounds down"},
      {"type":"text","text":"+435 tokens into main"},
  ],[0,80,120,155,185,215,245,275], mascot="off")),
  [{"at":0.05,"event":"Agent call"},{"at":0.5,"event":"summary lands"},{"at":0.9,"event":"'+435 tokens'"}])

B("B05","THE CATCH — REVISION","TERMINAL",LIAM,
  "And then, in the same main session, without being asked, Claude opens all five policies. "
  "Honor-code: four hundred sixty-six tokens. Late-submissions: six-twenty-five. Meeting-notes, participation, syllabus. Three thousand one hundred seventy more tokens into my window. "
  "The subagent isolated the reads. Claude ignored the isolation. Double-checking the summary is the default. The mechanism worked; the discipline didn't.",
  "CCSession — the redundant reads after the subagent",
  R("CCSession", session("run 2 — after the subagent","default",[
      {"type":"text","text":"# summary in hand · time to build"},
      {"type":"tool","name":"Read","arg":"policies/honor-code.md","state":"done"},
      {"type":"text","text":"+466 tokens · redundant"},
      {"type":"tool","name":"Read","arg":"policies/late-submissions.md","state":"done"},
      {"type":"text","text":"+625 tokens · redundant"},
      {"type":"tool","name":"Read","arg":"policies/meeting-notes.md","state":"done"},
      {"type":"tool","name":"Read","arg":"policies/participation.md","state":"done"},
      {"type":"tool","name":"Read","arg":"policies/syllabus.md","state":"done"},
      {"type":"text","text":"+3,170 tokens · isolation lost"},
  ],[0,45,80,110,140,170,200,225,255], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"Redundant reads"},{"at":0.5,"event":"'+3,170'"},{"at":0.9,"event":"'isolation lost'"}])

B("B06","THE FIX — VERIFY","TERMINAL",LIAM,
  "This is where the human comes in. The subagent is the mechanism; the tool boundary is the discipline. "
  "Rerun with Read removed from the policies path — deny the tool the second time you can't help using it. "
  "Same subagent, same summary, but now the main session cannot open the source docs even if it wants to. Four hundred thirty-five tokens, and only four hundred thirty-five tokens, land in my window.",
  "CCPlainShell — the fix on the command line",
  R("CCPlainShell",{"title":"the fix","lines":[
      "$ claude -p \"$ASK\" \\",
      "    --allowedTools \"Agent,Read,Edit,Bash(python3:*)\" \\",
      "    --disallowedTools \"Read(**/policies/**)\"",
      "",
      "  ↩ Agent (subagent) call:  +435 tokens",
      "  (Read on policies/ denied — no redundant reads)",
      "",
      "  main-session cache_creation, research chunk:",
      "    inline:              3,266 tokens",
      "    subagent + Read on:  3,605 tokens  (worse)",
      "    subagent + Read off:   435 tokens  (7.5× smaller)"],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the fix is a shell invocation, not a running session"),
  [{"at":0.05,"event":"The flag lands"},{"at":0.5,"event":"table"},{"at":0.9,"event":"'7.5× smaller'"}])

B("B07","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, five documents to consult, one function to write. Claude did the inline read; the handoff was tests pass, and they did — with three thousand tokens of policy sitting in my window. "
  "Step three, the dangerous middle: the subagent returned four hundred thirty-five tokens of exactly what I asked for, and Claude opened all five files anyway. That's plausibility auditing turned into a habit that erased the whole gain. "
  "Then mine: deny Read on the policies path, and rerun. Tool orchestration, one; interpretive judgment, one. Small session. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one build · two runs","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"1 task · 5 policies · 1 function"},
      {"n":2,"phase":"C","labor":"claude","text":"Inline: 5 reads · 3,266 tokens","handoff":"tests pass; policy content in main","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"claude","text":"Subagent: 435-token summary back","handoff":"summary in main; sources isolated","dependsOn":[1]},
      {"n":4,"phase":"C","labor":"claude","text":"Then reads policies anyway · +3,170","handoff":"gain cancelled","dependsOn":[3]},
      {"n":5,"phase":"H","labor":"human","capacity":"PA","text":"Names the redundant reads a defect","dependsOn":[4]},
      {"n":6,"phase":"F","labor":"human","capacity":"TO","text":"Deny Read on policies · rerun","dependsOn":[5]},
      {"n":7,"phase":"H","labor":"human","capacity":"IJ","text":"Trust the summary or don't call it","dependsOn":[6]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.5,"event":"Step 4 rings"},{"at":0.9,"event":"Tally"}])

B("B08","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide what the main session is allowed to touch — nobody else can. I must notice when a saving turned into an equal-and-opposite loss. "
  "I must trust the summary or not call a subagent at all — half-trust is the worst move. Claude can isolate reads in a subagent's window — the mechanism is honest. "
  "It can hand back a short summary — it did. It should stop at the summary when I asked it to — it didn't. It should refuse a redundant read when the tool is denied — and it does.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"isolate reads in a subagent"},{"tier":"CAN","text":"hand back a short summary"},
                          {"tier":"SHOULD","text":"stop at the summary if asked"},{"tier":"SHOULD","text":"refuse a denied redundant read"}],
                    "human":[{"tier":"MUST","text":"set the tool boundary"},{"tier":"MUST","text":"notice a cancelled gain"},
                             {"tier":"MUST","text":"trust it — or don't call it"},{"tier":"SHOULD","text":"deny Read on the sources"}],
                    "closing":"The subagent isolates. The human enforces.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Inline: five policy reads, three thousand two hundred sixty-six new tokens in the main session. "
  "Subagent, as designed: one Agent call, four hundred thirty-five tokens returned — the sources isolated in the subagent's window. "
  "Subagent, as Claude ran it: five redundant reads on top, three thousand one hundred seventy tokens back in the main window. "
  "What would prove this reel wrong: a run where Claude, given the summary and the tool, refuses the redundant read on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Inline: 5 reads, 3,266 new tokens in the main session.",
      "Subagent as designed: 1 call, 435 tokens back — sources isolated.",
      "Subagent as Claude ran it: 5 redundant reads on top, 3,170 back in main — gain cancelled.",
      "Fix: deny Read on the sources; trust the summary or don't call the subagent.",
      "The mechanism is real. The discipline is the human's.",
      "FALSIFIABLE: a run where Claude, given the summary, refuses the redundant read on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Open Claude Code in a folder with more than five source docs and paste this: "
  "Use one Agent call to summarize every document in docs into two hundred words. Then, based only on that summary, propose the first change I should make. "
  "Do not read any file under docs after the subagent returns. If you want to, print the read you would have made and stop.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Use one Agent call to summarize every document in docs into 200 words. Then, based only on that summary, propose the first change I should make. Do not read any file under docs after the subagent returns. If you want to, print the read you would have made and stop.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,
  "Why One Subagent Query Saved 48% of the Context Window. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same task, twice: five reads in main vs. one subagent — and what Claude does with the summary.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"02-plan-rewind-subagents","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-vox-subagent-context (the concept — reconstructed as two real headless runs)",
    "sources":["SESSION.md (two real headless runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print("  ⚠",b["beat_id"],len(blk["text"]),blk["text"])
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print("  ⚠ ledger",len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>46: print("  ⚠ step",len(st["text"]),st["text"])
        if len(r["props"]["system"])>28: print("  ⚠ system header",len(r["props"]["system"]),r["props"]["system"])
    if r["pattern"]=="ClaudeVerdictArtifact":
        n = len(r["props"]["artifactLines"])
        if n not in (4,6): print("  ⚠ verdict lines =", n)
