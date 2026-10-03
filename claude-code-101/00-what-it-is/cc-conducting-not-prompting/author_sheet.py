#!/usr/bin/env python3
"""author_sheet.py — cc-conducting-not-prompting (cc-explainer · Claude Code 101 · tier 00, "what it is")
"Conducting, Not Prompting: The Gru/Minion Split." Two real fresh headless runs; every block traces to SESSION.md. Liam, in for Bear."""
import json, os
SLUG="cc-conducting-not-prompting"; TITLE="Conducting, Not Prompting: The Gru/Minion Split"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Write format_price(cents: int) -> str in format_price.py and add unittest tests in test_format_price.py."
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
  "This is Liam, in for Bear. One sentence in an empty folder: write format_price of cents. No currency named. No format named. No policy on negatives. So it decides. "
  "Dollars. A thousands separator. Negatives allowed, with a minus. Type-error on anything that isn't an int, including a bool. Ten tests, all green. "
  "Every one of those is a decision — and none of them are mine.",
  "CCSession — the bare run: ls, two Writes, unittest OK",
  R("CCSession", session("scratch — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Bash","arg":"ls .","state":"done"},
      {"type":"tool","name":"Write","arg":"format_price.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_format_price.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"Wrote `format_price.py` — int cents →"},
      {"type":"text","text":"`$1,234.56`, negative gets a leading `-`,"},
      {"type":"text","text":"rejects non-ints, including bool."},
      {"type":"text","text":"Ran 10 tests in 0.000s — OK"},
  ],[0,100,140,180,220,260,285,310,335], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.5,"event":"Two Writes"},{"at":0.9,"event":"10 tests OK"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. When you type an ask at Claude and it types back, that is prompting — you asked, and you took what came. "
  "Conducting is the other move: the decisions get made first, in writing, and the prompt is a handoff. Same ask. Same model. Same minute. "
  "Different session — different code. You'll see it in the diff.",
  "BrutalistHesitantWriter — 'prompting' reconsidered into 'conducting'",
  R("BrutalistHesitantWriter", writer("Programming with Claude is prompting.\nThe prompt is the whole job.\nBetter prompt, better output.\nSame prompt, twice — different code.","prompting","conducting",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.35,"event":"'prompting' → 'conducting'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Three words before we start. Prompting: asking Claude, then reacting to whatever it produced — the prompt is a wish. "
  "Conducting: writing your decisions first — cases, rules, what counts as done — and handing them over. The prompt is a handoff, not the whole job. "
  "Spec: those decisions in writing, in one file Claude reads before it runs. That's the whole discipline. Three words. Watch what changes.",
  "CCDefinitions — three terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"Prompting","meaning":"asking Claude, then reacting to whatever came back"},
      {"term":"Conducting","meaning":"writing your decisions before Claude sees the ask"},
      {"term":"Spec","meaning":"the decisions written down — cases, rules, done"}],
    "startCue":10,"rowGap":52}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"Prompting"},{"at":0.4,"event":"Conducting"},{"at":0.85,"event":"Spec"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare run against what I actually wanted. Seven lines, forty-six lines of tests. The suite is green. Ten green tests. "
  "Now the five cases I care about — twelve ninety-nine, zero, ten thousand, twelve thousand three forty-five, minus fifty. "
  "Five for five, FAIL. The suite is green about the wrong thing. Nobody said EUR — so, dollars.",
  "CCSession — wc, unittest OK, spec_check FAIL ×5",
  R("CCSession", session("scratch — bare","default",[
      {"type":"prompt","text":"!wc -l format_price.py test_format_price.py","cue":0,"typeDuration":60},
      {"type":"text","text":"       7 format_price.py"},
      {"type":"text","text":"      46 test_format_price.py"},
      {"type":"prompt","text":"!python3 -m unittest -v 2>&1 | tail -2","cue":0,"typeDuration":56},
      {"type":"text","text":"Ran 10 tests in 0.000s — OK"},
      {"type":"prompt","text":"!python3 ../spec_check.py format_price.py","cue":0,"typeDuration":56},
      {"type":"text","text":"FAIL: format_price(1299) -> '$12.99'"},
      {"type":"text","text":"FAIL: format_price(0) -> '$0.00'"},
      {"type":"text","text":"FAIL: format_price(-50) -> '-$0.50'"},
  ],[0,60,80,115,175,205,265,290,315], mascot="off")),
  [{"at":0.05,"event":"wc → 7, 46"},{"at":0.3,"event":"10 tests OK"},{"at":0.7,"event":"spec_check → five FAILs"}])

B("B02","THE SPEC","SHELL",LIAM,
  "Eleven lines, written by me, before the second run. Five example inputs, and their outputs, in EUR. Four rules: no dollar sign, no separator, two decimals, minus is a ValueError. "
  "Every decision Claude made in the bare run — currency, format, negatives — this file makes instead. Eleven lines. That's the whole spec.",
  "CCPlainShell — wc SPEC.md; cat SPEC.md's decisions",
  R("CCPlainShell",{"title":"zsh — scratch/conducting","lines":[
      "$ wc -l SPEC.md",
      "      11 SPEC.md",
      "$ cat SPEC.md",
      "# SPEC — format_price",
      "",
      "format_price(cents: int) -> str. Cases:",
      "- 1299   -> '12.99 EUR'",
      "- 0      -> '0.00 EUR'",
      "- 10000  -> '100.00 EUR'",
      "- 12345  -> '123.45 EUR'",
      "- -50    -> raises ValueError",
      "",
      "No $. No separator. Two decimals. ' EUR'."],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the spec is read in a plain shell before any session; no session contains this"),
  [{"at":0.05,"event":"wc → 11"},{"at":0.35,"event":"Five cases"},{"at":0.85,"event":"Four rules"}])

B("B03","CONDUCTING — THE RUN","TERMINAL",LIAM,
  "Same sentence. This time it reads SPEC first. And its plan sentence is the file: split cents into euros and remainder, zero-pad the decimals, raise on negatives. "
  "Four lines of implementation. Twenty-five lines of tests, one for each case. Then it runs the suite. Five tests. Green. Every choice traces to a line.",
  "CCSession — the conducting run: Read SPEC, Writes, unittest OK",
  R("CCSession", session("scratch — conducting","accept-edits",[
      {"type":"prompt","text":ASK+" Read SPEC.md first.","cue":0,"typeDuration":90},
      {"type":"tool","name":"Read","arg":"SPEC.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"ls .","state":"done"},
      {"type":"text","text":"Splits cents into euros and remainder,"},
      {"type":"text","text":"zero-pads decimals, raises on negatives."},
      {"type":"tool","name":"Write","arg":"format_price.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_format_price.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest -v","state":"done"},
      {"type":"text","text":"All 5 tests pass — one per SPEC case."},
  ],[0,110,140,170,200,235,270,305,335], mascot="off")),
  [{"at":0.05,"event":"Same ask + Read SPEC"},{"at":0.45,"event":"Plan traces to the file"},{"at":0.9,"event":"5 tests OK"}])

B("B04","CONDUCTING — VERIFY","TERMINAL",LIAM,
  "Check it. Four lines against seven. Twenty-five lines of tests against forty-six. No dollar sign. One EUR. And the five cases from SPEC — PASS. "
  "Same one sentence. Same model. Eleven lines of mine, first. That's the difference.",
  "CCSession — wc, grep, spec_check → PASS",
  R("CCSession", session("scratch — conducting","default",[
      {"type":"prompt","text":"!wc -l format_price.py","cue":0,"typeDuration":40},
      {"type":"text","text":"       4 format_price.py"},
      {"type":"prompt","text":"!grep -c '\\$' format_price.py","cue":0,"typeDuration":52},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep -c EUR format_price.py","cue":0,"typeDuration":48},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!python3 ../spec_check.py format_price.py","cue":0,"typeDuration":56},
      {"type":"text","text":"PASS"},
  ],[0,50,80,130,160,205,235,290], mascot="off")),
  [{"at":0.05,"event":"wc → 4"},{"at":0.35,"event":"grep $ → 0"},{"at":0.6,"event":"grep EUR → 1"},{"at":0.85,"event":"PASS"}])

B("B05","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, in an empty folder. Claude did the bare run — seven lines, dollars, thousands separator, minus-fifty allowed. Handoff met — its own suite passed. "
  "Step three, the dangerous middle: I read the file. Ten green tests, testing something that isn't the thing. That was mine to catch. "
  "Then the real work, mine: eleven lines of SPEC. Claude did the conducting run — four lines. Handoff: the SPEC checker passes. "
  "Interpretive judgment: a green suite is not proof. It's proof that what you asked for is what you got. Ask better — or decide first.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"same sentence · two conditions","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence in an empty folder"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 7 lines, $, separator, -$ negatives","handoff":"unittest passes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the file: green suite, wrong thing","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write SPEC.md — 11 lines, mine","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Conducting: 4 lines, EUR, ValueError","handoff":"spec_check.py PASS; every line traces","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Green suite proves what you asked for","dependsOn":[3,5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name the currency and the format — Claude will not, and it will not know it didn't. "
  "I must write done as a check I can run. I must read the code, not the summary — a green suite lies about the wrong thing. "
  "I should write the spec before the ask, not after the failure. Claude can pick a plausible default and it will. "
  "It can produce four lines instead of seven when the decisions are named. It should read the spec first — it did. Eleven lines. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"pick a plausible default silently"},{"tier":"CAN","text":"write four lines from a spec"},
                          {"tier":"SHOULD","text":"read the spec before the ask"},{"tier":"SHOULD","text":"trace each line to a rule"}],
                    "human":[{"tier":"MUST","text":"name currency, format, negatives"},{"tier":"MUST","text":"write done as a check I run"},
                             {"tier":"MUST","text":"read the code, not the summary"},{"tier":"SHOULD","text":"write the spec before the ask"}],
                    "closing":"Same sentence. Eleven lines of mine, first. That's it.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same one sentence, empty folder: seven lines, dollars, a thousands separator, minus fifty becomes minus zero point five zero. Ten green tests, testing the wrong thing. "
  "Same sentence, eleven lines of mine first: four lines, EUR, ValueError on the minus, five tests, five passes. Conducting is not a better prompt. It is the decisions before the prompt. "
  "What would prove this reel wrong: a bare run that names the currency without being asked.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare: 7 lines, $, thousands separator, -$0.50 for a negative; 10 tests green, wrong thing.",
      "Conducting: 4 lines, EUR, ValueError on negatives; 5 tests, one per SPEC case; PASS.",
      "Conducting is not a better prompt. It is the decisions before the prompt.",
      "FALSIFIABLE: a bare run that names the currency without being asked."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next Claude Code session, open a text file, name it SPEC dot md, and write three things: five example inputs and their exact outputs, four rules that make those outputs the only right answers, and one line for what done means as a check you can run. Then paste your usual ask, followed by 'Read SPEC.md first.' See the diff.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Open SPEC.md. Write five example inputs and their exact outputs, four rules that make those the only right answers, and one line for done as a check you can run. Then paste your usual ask, followed by 'Read SPEC.md first.' See the diff.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Conducting, Not Prompting: The Gru/Minion Split. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same one sentence, twice. Eleven lines of yours, once. The difference is the whole job.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-code--claude-liam-conducting-not-prompting (the concept and title; card body replaced by two real fresh headless runs of one sentence)",
    "sources":["SESSION.md (two real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
