#!/usr/bin/env python3
"""author_sheet.py — cc-three-file-system-simulator (cc-explainer · Claude Code 101 · tier 01)
"Build a Simulation with the Three-File System with Claude Code." Every block traces to SESSION.md
(two real fresh runs; bare and three files). Liam, in for Bear."""
import json, os
SLUG="cc-three-file-system-simulator"; TITLE="Build a Simulation with the Three-File System with Claude Code"
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Build a sorting simulator for a ninth-grade class as index.html."
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
  "This is Liam, in for Bear. One sentence, an empty folder for a ninth-grade class: build a sorting simulator. "
  "Watch what it decides on its own. No palette specified — so, tailwind blues. No pedagogy specified — so, bubble sort and merge sort and a legend and a running commentary. "
  "Five hundred ninety-five lines of decisions, and none of them are the teacher's.",
  "CCSession — the bare run: the ask, two Reads, the 'colour highlights + speed control' plan, one Write",
  R("CCSession", session("studygroup-sim — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"ask.txt","state":"done"},
      {"type":"text","text":"I'll build a self-contained sorting"},
      {"type":"text","text":"simulator with bubble sort and merge"},
      {"type":"text","text":"sort, comparison highlights, speed"},
      {"type":"text","text":"control and step-through for class."},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
  ],[0,90,115,150,170,190,210,260], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.5,"event":"'speed control + step-through'"},{"at":0.9,"event":"Write index.html"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here is the idea of this film. Claude's defaults are polished, because it has read a million pages — and generic, because the choices were not the teacher's. "
  "The fix is not a better prompt. It is three short files, written before Claude touches anything: what it may not do; what it must look and feel like; and who this is for and what done means. "
  "Same one-sentence ask, with and without them. You will see the difference in the diff.",
  "BrutalistHesitantWriter — 'polished' reconsidered into 'not yours'",
  R("BrutalistHesitantWriter", writer("Claude's defaults are polished.\nIt has read a million pages.\nThe choices are generic.\nThree files, written first, make them yours.","polished","not yours",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'polished' → 'not yours'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. CLAUDE.md: constraints — what Claude may and may not do in this folder, read at the start of every session. "
  "DESIGN.md: every aesthetic decision named — colour, type, layout, interaction, and what silence means. "
  "PROJECT.md: the intent layer — who it is for, what they should feel, what it refuses, what done means, and what is out of scope. "
  "Definition of done: a check you can run; here, a script that prints pass or fail. Autoplay: any animation that runs by itself — set-interval, set-timeout, or an animation-frame loop.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"CLAUDE.md","meaning":"constraints — what Claude may and may not do in this folder; read every session"},
      {"term":"DESIGN.md","meaning":"every aesthetic decision, named — colour, type, layout, interaction, silence"},
      {"term":"PROJECT.md","meaning":"the intent layer — who it is for, what they feel, what it refuses, what done means"},
      {"term":"definition of done","meaning":"a check you can run; here a script that prints PASS or FAIL"},
      {"term":"autoplay","meaning":"any animation running by itself — set-interval, set-timeout, requestAnimationFrame"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare page against a definition of done — a script the teacher wrote. Five failures, not one. "
  "Two font families. An autoplay loop the teacher never asked for. A speed slider. Four buttons where one was needed. "
  "And twelve colours from the tailwind palette; not the classroom's. Not wrong. Not the teacher's. Nobody told it otherwise, and it filled the silence with the internet's average dashboard.",
  "CCSession — wc, check.py FAIL ×5, the twelve colours",
  R("CCSession", session("studygroup-sim — bare","default",[
      {"type":"prompt","text":"!wc -l index.html","cue":0,"typeDuration":28},
      {"type":"text","text":"     595 index.html"},
      {"type":"prompt","text":"!python3 check.py","cue":0,"typeDuration":28},
      {"type":"text","text":"FAIL: more than one font-family"},
      {"type":"text","text":"FAIL: autoplay (setTimeout)"},
      {"type":"text","text":"FAIL: speed slider (input type=range)"},
      {"type":"text","text":"FAIL: more than one button"},
      {"type":"text","text":"FAIL: colours outside DESIGN.md"},
  ],[0,40,75,115,140,165,190,215], mascot="off")),
  [{"at":0.05,"event":"wc → 595"},{"at":0.35,"event":"check.py → five FAILs"},{"at":0.85,"event":"'colours outside DESIGN.md'"}])

B("B02","THE THREE FILES","SHELL",LIAM,
  "Three files, written by the teacher, before the second run. CLAUDE.md: one file, vanilla JS, no framework, no external requests, and run check.py before you say done. "
  "DESIGN.md: two colours for the bars, one accent for the button, one cream page, one font — and no legend, no dropdown, no explainer text. "
  "PROJECT.md: the five questions only the teacher can answer. Who is this for. What should they feel. What does this refuse. What is done. What is out of scope. Nineteen lines. The lesson plan, made durable.",
  "CCPlainShell — wc on the three files; PROJECT.md's five questions",
  R("CCPlainShell",{"title":"zsh — ~/studygroup-sim","lines":[
      "$ wc -l CLAUDE.md DESIGN.md PROJECT.md",
      "       5 CLAUDE.md",
      "       7 DESIGN.md",
      "       7 PROJECT.md",
      "$ grep '^- ' PROJECT.md | cut -c1-60",
      "- Who is this for? A ninth-grade class of twenty-eight …",
      "- What should they feel? That each STEP is one thing …",
      "- What does this refuse? Autoplay. Speed control. Multi…",
      "- What is done? python3 check.py passes, and the page …",
      "- What is out of scope? Merge sort. Quick sort. Sound. …"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the three files are read in a plain shell before any session; no session contains this"),
  [{"at":0.05,"event":"wc → 5, 7, 7"},{"at":0.5,"event":"PROJECT.md's five questions"}])

B("B03","THREE FILES — THE RUN","TERMINAL",LIAM,
  "Same sentence. This time it reads the three files first — and its plan is the files: one STEP button, one comparisons counter, bars only, palette locked to the four allowed hex values. "
  "It writes the page and runs the checker itself, because CLAUDE.md told it to. It fails: font-family colon inherit on the button counts as a second declaration. It fixes the page, not the script — twice, until pass.",
  "CCSession — three-file run: Reads, plan, Write, check FAIL, Edit, Edit, check PASS",
  R("CCSession", session("studygroup-sim — three files","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"PROJECT.md","state":"done"},
      {"type":"tool","name":"Read","arg":"DESIGN.md","state":"done"},
      {"type":"tool","name":"Read","arg":"check.py","state":"done"},
      {"type":"text","text":"I have the constraints. Building"},
      {"type":"text","text":"one STEP, one counter, bars only,"},
      {"type":"text","text":"palette locked to four hex values."},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check.py","state":"done"},
      {"type":"text","text":"FAIL: more than one font-family"},
      {"type":"tool","name":"Edit","arg":"index.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check.py","state":"done"},
      {"type":"text","text":"PASS: index.html meets PROJECT.md's …"},
  ],[0,60,80,100,125,145,165,190,215,235,255,275,300], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.4,"event":"Reads the three files"},{"at":0.7,"event":"check.py → FAIL"},{"at":0.95,"event":"check.py → PASS"}])

B("B04","THREE FILES — VERIFY","TERMINAL",LIAM,
  "Check it. One hundred eleven lines against five hundred ninety-five. Four hex values, plus near-black text. One font-family. One button, labelled STEP. "
  "No set-interval. No set-timeout. No range slider. Every one of those is a line from the teacher's files, not a default.",
  "CCSession — wc, colours, font-family count, button count, no autoplay grep",
  R("CCSession", session("studygroup-sim — three files","default",[
      {"type":"prompt","text":"!wc -l index.html","cue":0,"typeDuration":28},
      {"type":"text","text":"     111 index.html"},
      {"type":"prompt","text":"!grep -oE '#[0-9A-F]{6}' i…","cue":0,"typeDuration":40},
      {"type":"text","text":"#111111  #6B8E6B  #8B7355"},
      {"type":"text","text":"#D97757  #F6F1E6"},
      {"type":"prompt","text":"!grep -c 'font-family' i…","cue":0,"typeDuration":40},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -c '<button' i…","cue":0,"typeDuration":36},
      {"type":"text","text":"1"},
  ],[0,40,75,120,140,180,220,255,290], mascot="off")),
  [{"at":0.05,"event":"wc → 111"},{"at":0.35,"event":"five hex values"},{"at":0.7,"event":"font-family → 1"},{"at":0.9,"event":"button → 1"}])

B("BFLOW","THE FLOW","DIAGRAM",LIAM,
  "How the three files gate the build. The ask enters. CLAUDE.md is auto-loaded; DESIGN.md and PROJECT.md are Read. Claude proposes a plan, then Writes the page. "
  "The last edge is not optional — it is CLAUDE.md's rule: run the checker before you say done. If the checker fails, the fix goes to the page, never to the script. Then, and only then, done.",
  "FlowDiagram — three-file flow, claude skin, terracotta accent on the checker edge",
  R("FlowDiagram",{
    "caption":"three files gate the build; the checker gates 'done'",
    "kicker":"cc-three-file-system-simulator",
    "skin":"claude","pulse":True,
    "viewBox":{"w":1920,"h":1080},
    "nodes":[
      {"id":"ask","label":"the ask","sub":"one sentence","type":"terminal","x":100,"y":460},
      {"id":"claude","label":"claude","sub":"the model","type":"process","x":760,"y":460,"hi":True},
      {"id":"cmd","label":"CLAUDE.md","sub":"constraints","type":"store","x":460,"y":180},
      {"id":"des","label":"DESIGN.md","sub":"aesthetics","type":"store","x":760,"y":180},
      {"id":"prj","label":"PROJECT.md","sub":"intent","type":"store","x":1060,"y":180},
      {"id":"page","label":"index.html","sub":"the page","type":"io","x":1420,"y":320},
      {"id":"chk","label":"check.py","sub":"definition of done","type":"decision","x":1420,"y":600},
      {"id":"done","label":"done","sub":"pass","type":"terminal","x":1560,"y":880}
    ],
    "edges":[
      {"from":"ask","to":"claude","order":1,"kind":"request"},
      {"from":"cmd","to":"claude","order":2,"kind":"dep","label":"auto-load"},
      {"from":"des","to":"claude","order":3,"kind":"dep","label":"Read"},
      {"from":"prj","to":"claude","order":4,"kind":"dep","label":"Read"},
      {"from":"claude","to":"page","order":5,"kind":"write","label":"Write"},
      {"from":"page","to":"chk","order":6,"kind":"data","label":"python3 check.py"},
      {"from":"chk","to":"claude","order":7,"kind":"reply","dashed":True,"label":"FAIL → fix page"},
      {"from":"chk","to":"done","order":8,"kind":"flow","label":"PASS"}
    ]}, motion="drawon", leaves_terminal_because="BFLOW: the three-file gate is a structure the session only implies"),
  [{"at":0.05,"event":"Ask node"},{"at":0.3,"event":"Three files land"},{"at":0.6,"event":"Write → check.py"},{"at":0.9,"event":"PASS → done"}])

B("BSHOW","THE OUTPUT","VIDEO",LIAM,
  "Open the file. Eight bars. Comparisons zero. Press STEP: one comparison, sometimes a swap. Press it again. The rightmost bar locks in green when its pass is done. "
  "Fifteen presses; two bars sorted. Forty presses; halfway. Sixty-three presses; every bar green. That is the whole page. The pedagogy is that the child names what happened before pressing again.",
  "captured recording of the three-file page — four states of the sort",
  {"type":"screen","source":"own","motion":"hold","media":"media/BSHOW.mp4",
   "leaves_terminal_because":"BSHOW: what the build produced, running — the receipt for the whole film"},
  [{"at":0.02,"event":"start · 0 comparisons"},{"at":0.3,"event":"15 · two green"},{"at":0.6,"event":"40 · halfway"},{"at":0.9,"event":"63 · all green"}])

B("B05","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, the teacher's: one sentence, one folder. Claude did the bare run; the handoff was the definition of done, and it failed it five ways. "
  "Step three, the dangerous middle: reading the ask instead of asking who it was for — a dashboard for ninth-graders. "
  "Then the real work, the teacher's: nineteen lines in three files. Claude did the three-file run; failed the checker on font-family inherit; fixed the page twice; passed. "
  "Interpretive judgment stayed the teacher's. Executive integration too. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · three files","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, one folder"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 595 lines, tailwind, autoplay","handoff":"check.py passes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the ask: a dashboard for 9th grade","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write the three files — 19 lines","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Three files: 111 lines, one STEP, four colours","handoff":"check.py passes; every hex is in DESIGN.md","dependsOn":[4]},
      {"n":6,"phase":"C","labor":"claude","text":"Failed check; fixed the page twice","handoff":"fix the page, not the script","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was the teacher's. The teacher must answer the five questions — nobody else can name a ninth-grade room. The teacher must name the aesthetic decisions, or the internet's average gets named for them. "
  "The teacher must write done as a check that runs. The teacher should read the ask, not the summary. "
  "Claude can fill a silence with a dashboard, and it will. It can Write the page and run the checker — it did. It should say its plan first — it did. It should fix the page, not the script — it did, twice.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"fill a silence with a dashboard"},{"tier":"CAN","text":"Write the page and run the checker"},
                          {"tier":"SHOULD","text":"say its plan first — it did"},{"tier":"SHOULD","text":"fix the page, not the script"}],
                    "human":[{"tier":"MUST","text":"answer the five questions"},{"tier":"MUST","text":"name the aesthetic decisions"},
                             {"tier":"MUST","text":"write done as a script"},{"tier":"SHOULD","text":"read the ask, not the summary"}],
                    "closing":"The lesson plan, made durable. Nineteen lines. The teacher's.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence in an empty folder: five hundred ninety-five lines, twelve colours, autoplay, a speed slider, a legend, a running commentary. "
  "Three files first — nineteen lines of the teacher's: one hundred eleven lines, one STEP, one counter, four hex values, and the fix went to the page, not the script. "
  "The three files are the lesson plan. The checker is the definition of done. Together, they make the simulator the teacher's, not the internet's. "
  "What would prove this reel wrong: a bare run that, unprompted, chooses one interaction, one button, and one palette.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "One sentence, empty folder: 595 lines, 12 colours, autoplay, a speed slider, five things at once.",
      "Three files first — 19 lines of the teacher's: 111 lines, one STEP, one counter, four hex values.",
      "The three files are the lesson plan. The checker is the definition of done. Together they make it yours.",
      "FALSIFIABLE: a bare run that, unprompted, chooses one interaction, one button, and one palette."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next classroom build, open Claude Code and paste this: ask me the five questions — who is this for, what should they feel, what does this refuse, what is done, what is out of scope — "
  "one at a time, and write my answers into PROJECT.md in my words. Then write DESIGN.md from what I tell you about colour, type, and interaction. Then write CLAUDE.md from what I tell you about the stack and the check. Do not build anything yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Ask me the five questions — who is this for, what should they feel, what does this refuse, what is done, what is out of scope — one at a time, and write my answers into PROJECT.md in my words. Then write DESIGN.md from what I tell you about colour, type, and interaction. Then write CLAUDE.md. Don't build anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Build a Simulation with the Three-File System with Claude Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same one-sentence ask, with and without 19 lines of yours. The difference is in the diff.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"01-context-and-memory","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "build":True,
    "derived_from":"claude-code-101/01-context-and-memory/claude-code--claude-liam-three-file-system-simulator (the concept; every card replaced by two real runs)",
    "sources":["SESSION.md (two real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r=b["shot"].get("remotion")
    if not r: continue
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
