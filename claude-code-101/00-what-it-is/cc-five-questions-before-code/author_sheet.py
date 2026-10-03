#!/usr/bin/env python3
"""author_sheet.py — cc-five-questions-before-code (cc-explainer · Claude Code 101 · tier 00, film 04)
"Five Questions Before Code." Every block traces to SESSION.md (four real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-five-questions-before-code"; TITLE="Five Questions Before Code: The Calibration Session"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Add avg_temp(readings) to stats.py that returns the average temperature across all readings, and add tests using unittest."
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

B("B00","COLD OPEN — BARE","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence, an empty folder: add avg-temp to stats.py, with tests. Watch what Claude does when the ask has holes and there is nobody to ask. "
  "It tries to ask. The tool is fenced. It uses its defaults. Seven tests. Green. Ready to ship.",
  "CCSession — the cold run: ask, Reads, blocked question, defaults, Edit, Write, unittest green",
  R("CCSession", session("study-readings — cold","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Read","arg":"stats.py","state":"done"},
      {"type":"tool","name":"Read","arg":"readings.log","state":"done"},
      {"type":"text","text":"A few things here are ambiguous."},
      {"type":"tool","name":"AskUserQuestion","arg":"3 clarifying questions","state":"done"},
      {"type":"text","text":"Dismissed. Using recommended defaults."},
      {"type":"tool","name":"Edit","arg":"stats.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_stats.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_stats","state":"done"},
      {"type":"text","text":"Ran 7 tests. OK."},
  ],[0,100,120,140,170,200,230,260,285,310], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.4,"event":"AskUserQuestion, blocked"},{"at":0.9,"event":"Ran 7 tests, OK"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here is the idea. Five questions before code is not a courtesy. It is not extra work you do to be polite. It is where the ambiguity in the ask becomes an explicit choice — one you make, or Claude quietly makes for you. "
  "The building is the easy half. The setup is where the wrong assumption dies. Same one-sentence ask, with and without the five. You will see the difference in the number that comes out.",
  "BrutalistHesitantWriter — 'extra' reconsidered into 'the setup'",
  R("BrutalistHesitantWriter", writer("Five questions, no code.\nThe build is the second half.\nThe first half is extra.\nThe wrong assumption dies here.","extra","the setup",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.35,"event":"'extra' → 'the setup'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Calibration session: the short read-only conversation you have with Claude before any tool call, to check what it thinks it heard. Read-only mode: a permission fence — Claude may read files, "
  "but may not write, edit, or run anything. Agentic loop: the gather-act-verify cycle Claude runs on its own between your turns. NaN: 'not a number' — a value that means the sensor was silent. Definition of done: a check "
  "you can run; here, a unittest suite that either passes or does not.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"calibration session","meaning":"a short read-only chat with Claude before any tool call"},
      {"term":"read-only mode","meaning":"a fence — Claude may Read, but not Write, Edit, or run"},
      {"term":"agentic loop","meaning":"the gather-act-verify cycle Claude runs on its own"},
      {"term":"NaN","meaning":"'not a number' — a reading where the sensor was silent"},
      {"term":"definition of done","meaning":"a check you can run; here, a unittest suite that passes"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience who may not know these words"),
  [{"at":0.05,"event":"First term"},{"at":0.55,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the cold build against real data. Seven tests, pass — Claude's own. Now the production log: three rows where the sensor dropped and wrote NaN. Python's float accepts NaN. The mean is poisoned. Twenty degrees became n-a-n. "
  "Not a crash. A wrong number, silently. That is the tests-pass, production-breaks moment the five questions exist to prevent.",
  "CCSession — Liam's verify: 7 tests OK, production.log → nan, head shows the NaN rows",
  R("CCSession", session("study-readings — cold · verify","default",[
      {"type":"prompt","text":"!python3 -m unittest test_stats","cue":0,"typeDuration":56},
      {"type":"text","text":"Ran 7 tests. OK."},
      {"type":"prompt","text":"!python3 -c 'read_log,avg_temp(prod)'","cue":0,"typeDuration":60},
      {"type":"text","text":"avg= nan"},
      {"type":"prompt","text":"!head -3 production.log","cue":0,"typeDuration":40},
      {"type":"text","text":"09:00  temp=20.4  humid=45"},
      {"type":"text","text":"10:00  temp=NaN    humid=44"},
      {"type":"text","text":"11:00  temp=21.3  humid=44"},
  ],[0,50,90,140,175,215,235,255], mascot="off")),
  [{"at":0.05,"event":"7 tests pass"},{"at":0.4,"event":"avg = nan"},{"at":0.8,"event":"the NaN row"}])

B("B02","THE FIVE QUESTIONS","SHELL",LIAM,
  "The five questions I am about to paste. Written to run in read-only mode — Claude may read files, may not write, edit, or run anything. Files. Purpose. What would you write. What would you not touch. What are you uncertain about. "
  "That last one is where the whole conversation earns its keep.",
  "CCPlainShell — cat five-questions.txt, the five in order",
  R("CCPlainShell",{"title":"zsh — ~/study-readings","lines":[
      "$ cat five-questions.txt",
      "1. What files do you see and what is each for?",
      "2. What do you think this project is for?",
      "3. If I asked you to <TASK>, what would you write?",
      "4. What would you not touch?",
      "5. What are you uncertain about that I should clarify?",
      "",
      "$ wc -l five-questions.txt",
      "       8 five-questions.txt"],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the questions are a plain text file Liam pastes; no session contains them yet"),
  [{"at":0.05,"event":"cat"},{"at":0.45,"event":"Q5 lands"},{"at":0.9,"event":"wc"}])

B("B03","CALIBRATION — THE RUN","TERMINAL",LIAM,
  "Same folder. Same tools, minus the write tools. I paste the five. Claude reads all four files first. Then answers, in its own words: the files it saw, what it thinks the project is for, what it would write, what it would not touch. "
  "Then question five. Empty input, what to return. Malformed rows, skip or raise. In Claude's own words: numbers one and two change the code.",
  "CCSession — the calibration: 5 questions, 4 Reads, 5 answers, Q5 pivots surface",
  R("CCSession", session("study-readings — calibration","default",[
      {"type":"prompt","text":"5 questions, read-only. Q1..Q5.","cue":0,"typeDuration":60},
      {"type":"tool","name":"Read","arg":"stats.py","state":"done"},
      {"type":"tool","name":"Read","arg":"readings.log","state":"done"},
      {"type":"text","text":"1. README, stats.py, log, ask.txt"},
      {"type":"text","text":"2. Hourly temp/humid stats module."},
      {"type":"text","text":"3. Cast temp to float, return mean."},
      {"type":"text","text":"4. parse(), read_log(), the log."},
      {"type":"text","text":"5. Empty input: None, 0.0, or raise?"},
      {"type":"text","text":"5. Malformed row: skip, or raise?"},
      {"type":"text","text":"1 and 2 would change the code."},
  ],[0,80,105,135,165,195,220,250,280,310], mascot="off")),
  [{"at":0.05,"event":"Prompt"},{"at":0.4,"event":"Q1..Q4 answers"},{"at":0.85,"event":"Q5: the two pivots"}])

B("B04","CALIBRATION — THE BUILD","TERMINAL",LIAM,
  "I answer question five. Empty, return None. Malformed, skip — and skip the string NaN, because production logs use it for sensor dropouts and Python's float will happily average nan into your mean. Add a test for a NaN row. "
  "Same session, resumed. It writes both files, does not run them because I said read-only. I run the tests. Eight, pass. Same production log. Twenty-one point four seven degrees.",
  "CCSession — Liam's answer, Write ×2, unittest, production run",
  R("CCSession", session("study-readings — calibration","accept-edits",[
      {"type":"prompt","text":"Empty→None. Skip 'NaN'. Add NaN test.","cue":0,"typeDuration":60},
      {"type":"tool","name":"Write","arg":"stats.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_stats.py","state":"done"},
      {"type":"text","text":"Wrote both, did not run them."},
      {"type":"prompt","text":"!python3 -m unittest test_stats","cue":0,"typeDuration":56},
      {"type":"text","text":"Ran 8 tests. OK."},
      {"type":"prompt","text":"!python3 -c 'avg_temp(prod)'","cue":0,"typeDuration":48},
      {"type":"text","text":"avg= 21.47142857142857"},
  ],[0,70,105,140,170,220,255,290], mascot="off")),
  [{"at":0.05,"event":"Answer"},{"at":0.4,"event":"Write ×2"},{"at":0.9,"event":"21.47"}])

B("B05","THE MIDDLE CASE","TERMINAL",LIAM,
  "One more run I did not plan. Just question five. Nothing else. Read-only. Claude reads the files and comes back with the same two decisions: empty input, malformed rows. Same pivots. From one question, not five. "
  "The other four are not wasted — they are the ramp that lets Claude reach five honestly. But if you had ten seconds, five is the one that pays for itself.",
  "CCSession — Q5 alone: same two pivots surface",
  R("CCSession", session("study-readings — Q5 only","default",[
      {"type":"prompt","text":"What are you uncertain about?","cue":0,"typeDuration":52},
      {"type":"tool","name":"Read","arg":"stats.py","state":"done"},
      {"type":"tool","name":"Read","arg":"readings.log","state":"done"},
      {"type":"text","text":"1. Empty input: None, 0.0, raise?"},
      {"type":"text","text":"2. Malformed temp: skip, or raise?"},
      {"type":"text","text":"1 and 2 would change the code."},
  ],[0,70,95,130,165,200], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"Q5"},{"at":0.45,"event":"Same two pivots"},{"at":0.85,"event":"Same conclusion"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, ambiguous on purpose. Claude did the cold run — its handoff was the questions it tried to ask, and I dismissed them. "
  "Step three, the dangerous middle: seven passing tests over a nan on production. Then the real work, mine: five questions in read-only, and the answer to question five. Claude did the calibrated build; handoff met on production data. "
  "Then interpretive judgment: question five alone would have surfaced both pivots. Tool orchestration, zero; executive integration, zero. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · ambiguous by design","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence — ambiguous on purpose"},
      {"n":2,"phase":"C","labor":"claude","text":"Cold: 7 tests pass; nan on production","handoff":"answer the 3 questions it tried to ask","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Ran on real data: silent nan","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Five questions, read-only — Q5 clarified","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Calibrated: 8 tests; production 21.47","handoff":"skip NaN string; return None on empty","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Q5 alone surfaces both pivots","dependsOn":[2]},
  ],"dangerousMiddle":2,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 2 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must ask the five questions myself — Claude cannot pause on my behalf. I must run the build on real data, not the sample it built to. I must answer question five honestly — vague answers cash in as defaults later. "
  "I should read the answer, not the summary. Claude can make three silent choices when its questions are blocked, and it will. It can pass its own tests. It should ask five questions when I ask it to. It should say what it is uncertain about — it did.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"make silent choices when blocked"},{"tier":"CAN","text":"pass its own tests"},
                          {"tier":"SHOULD","text":"ask five questions when asked"},{"tier":"SHOULD","text":"name what it is uncertain about"}],
                    "human":[{"tier":"MUST","text":"ask the five questions"},{"tier":"MUST","text":"run on real data"},
                             {"tier":"MUST","text":"answer question five honestly"},{"tier":"SHOULD","text":"read the answer, not summary"}],
                    "closing":"Five questions cost ten minutes.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Cold: three silent choices, seven passing tests, nan on production. Five questions first: two pivots named, eight tests, twenty-one point four seven degrees. "
  "Question five alone surfaces both pivots; the other four ramp you to five in Claude's own words. What would prove this reel wrong: a cold run that pauses on empty input on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Cold: 3 silent choices, 7 tests pass, nan on production data.",
      "Five questions first: 2 pivots named, 8 tests, production 21.47.",
      "Q5 alone surfaces both pivots; Q1–Q4 ramp you to Q5 honestly.",
      "FALSIFIABLE: a cold run that pauses on empty input on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next Claude Code session, paste this: Read the files in this project. Answer five questions in read-only mode — do not write, edit, or run anything. One: what files do you see and what is each for. Two: what do you think this project is for. "
  "Three: if I asked you to add my next feature, what would you write. Four: what would you not touch. Five: what are you uncertain about that I should clarify before we start.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Read the files in this project. Answer five questions in read-only mode — do not write, edit, or run anything. 1) What files do you see and what is each for? 2) What do you think this project is for? 3) If I asked you to add my next feature, what would you write? 4) What would you not touch? 5) What are you uncertain about that I should clarify before we start?",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Five Questions Before Code: The Calibration Session. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same sentence, with and without five questions. The difference is the number that comes out.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-code--claude-liam-five-questions-before-code (concept only; the card body replaced by four real runs against a scratch stats module)",
    "sources":["SESSION.md (four real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
                if len(row["text"])>34: print("  ⚠ ledger",len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>46: print("  ⚠ step",len(st["text"]),st["text"])
