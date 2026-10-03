#!/usr/bin/env python3
"""author_sheet.py — cc-three-files (cc-explainer · Claude Code 101 · tier 01, film 03)
"Three Files Before Claude Touches Anything." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-three-files"; TITLE="Three Files Before Claude Touches Anything"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Build the sign-up page for our Thursday study group as index.html."
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
  "This is Liam, in for Bear. One sentence, an empty folder: build the sign-up page for our Thursday study group. Watch what it decides on its own. "
  "No backend specified — so, mailto. Nobody said who this is for, what it should feel like, or what it must refuse. So it decides. "
  "Two hundred and twelve lines of decisions, and none of them are mine.",
  "CCSession — the bare run: the ask, two Reads, the mailto decision, one Write",
  R("CCSession", session("studygroup — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"ask.txt","state":"done"},
      {"type":"text","text":"I'll create a self-contained `index.html`"},
      {"type":"text","text":"sign-up page. Since there's no backend"},
      {"type":"text","text":"specified, I'll use `mailto:` as the"},
      {"type":"text","text":"submission target so it works …"},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
  ],[0,90,115,150,170,190,210,260], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.5,"event":"'no backend specified — mailto'"},{"at":0.9,"event":"Write index.html"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Claude's defaults are polished, because it has read a million pages — and generic, because the choices weren't yours. "
  "The fix isn't a better prompt. It's three short files written before Claude touches anything: what it may not do, what it should look and sound like, "
  "and who it's for and what done means. Same one-sentence ask, with and without them. You'll see the difference in the diff.",
  "BrutalistHesitantWriter — 'fine' reconsidered into 'not yours'",
  R("BrutalistHesitantWriter", writer("Claude's defaults are fine.\nPolished — it has read a million pages.\nGeneric — the choices weren't yours.\nThree files, written first, make them yours.","fine","not yours",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'fine' → 'not yours'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. CLAUDE.md: constraints — what Claude may and may not do in this folder, read at the start of every session. "
  "DESIGN.md: every aesthetic decision, named — tone, type, colour, layout, and what silence means. PROJECT.md: the intent layer — who it's for, what they should feel, what it refuses, what done means. "
  "Definition of done: a check you can run; here, a script that prints pass or fail. Sign-up wall: asking for an account or an email before letting someone in.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"CLAUDE.md","meaning":"constraints — what Claude may and may not do in this folder; read every session"},
      {"term":"DESIGN.md","meaning":"every aesthetic decision, named — tone, type, colour, layout, what silence means"},
      {"term":"PROJECT.md","meaning":"the intent layer — who it's for, what they feel, what it refuses, what done means"},
      {"term":"definition of done","meaning":"a check you can run; here a script that prints PASS or FAIL"},
      {"term":"sign-up wall","meaning":"asking for an account or an email before letting someone in"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare page against a definition of done I wrote — a script. Two failures. Emoji: a calendar, a clock, a pin. And an email field: a sign-up wall, for twelve people who already know each other. "
  "Not wrong. Not mine. Nobody told it otherwise, and it filled the silence with the internet's average sign-up page.",
  "CCSession — wc, check.py FAIL ×2, the two inputs",
  R("CCSession", session("studygroup — bare","default",[
      {"type":"prompt","text":"!wc -l index.html","cue":0,"typeDuration":28},
      {"type":"text","text":"     212 index.html"},
      {"type":"prompt","text":"!python3 check.py","cue":0,"typeDuration":28},
      {"type":"text","text":"FAIL: emoji"},
      {"type":"text","text":"FAIL: email/password field (sign-up wall)"},
      {"type":"prompt","text":"!grep -o \"<input[^>]*>\" index.html | head -2","cue":0,"typeDuration":56},
      {"type":"text","text":"<input type=\"text\" name=\"name\" … required />"},
      {"type":"text","text":"<input type=\"email\" name=\"email\" …"},
  ],[0,40,75,115,135,180,230,250], mascot="off")),
  [{"at":0.05,"event":"wc → 212"},{"at":0.35,"event":"check.py → two FAILs"},{"at":0.75,"event":"an email input"}])

B("B02","THE THREE FILES","SHELL",LIAM,
  "Three files, written by me, before the second run. CLAUDE.md: one file, no frameworks, no external requests, and run check.py before you say done. "
  "DESIGN.md: every aesthetic decision named — one typeface, black on off-white, one accent, no exclamation marks, no emoji, never the word welcome; and what silence means: no tagline, no FAQ. "
  "PROJECT.md: the five questions only I can answer. Who is this for. What should they feel. What does this refuse. What is done. What's out of scope. Nineteen lines. The design session, made durable.",
  "CCPlainShell — wc on the three files; PROJECT.md's five questions",
  R("CCPlainShell",{"title":"zsh — ~/studygroup","lines":[
      "$ wc -l CLAUDE.md DESIGN.md PROJECT.md",
      "       5 CLAUDE.md",
      "       7 DESIGN.md",
      "       7 PROJECT.md",
      "$ grep '^- ' PROJECT.md | cut -c1-60",
      "- Who is this for? Twelve people who already know each other …",
      "- What should they feel? That this took thirty seconds and ask…",
      "- What does this refuse? Accounts. Emails. Passwords. Anyone's…",
      "- What is done? `python3 check.py` passes, and the page shows …",
      "- What is out of scope? Reminders, calendars, attendance histo…"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the three files are read in a plain shell before any session; no session contains this"),
  [{"at":0.05,"event":"wc → 5, 7, 7"},{"at":0.45,"event":"PROJECT.md's five questions"}])

B("B03","THREE FILES — THE RUN","TERMINAL",LIAM,
  "Same sentence. This time it reads the three files first — and its plan is my plan: one column, system font, name field only, next Thursday computed in the browser. "
  "Ninety-five lines. Then it runs the definition of done itself, because CLAUDE.md told it to. Pass.",
  "CCSession — the three-file run: Reads, the plan sentence, Write, check.py PASS",
  R("CCSession", session("studygroup — three files","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"check.py","state":"done"},
      {"type":"tool","name":"Read","arg":"PROJECT.md","state":"done"},
      {"type":"tool","name":"Read","arg":"DESIGN.md","state":"done"},
      {"type":"text","text":"I have the constraints. Let me build"},
      {"type":"text","text":"`index.html` — one column, system font,"},
      {"type":"text","text":"name field only, next-Thursday computed"},
      {"type":"text","text":"in the browser."},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check.py","state":"done"},
      {"type":"text","text":"PASS: index.html meets PROJECT.md's …"},
  ],[0,85,105,125,150,170,190,210,240,265,290], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.4,"event":"Reads the three files; the plan is the files"},{"at":0.85,"event":"check.py → PASS"}])

B("B04","THREE FILES — VERIFY","TERMINAL",LIAM,
  "Check it. Ninety-five lines against two hundred twelve. One input: a first name. The accent colour, once. And the next Thursday, computed — line seventy-five. "
  "Every one of those is a line from my files, not a default. Same model, same sentence. The difference is what I wrote first.",
  "CCSession — wc, the one input, the accent once, getDay on line 75",
  R("CCSession", session("studygroup — three files","default",[
      {"type":"prompt","text":"!wc -l index.html","cue":0,"typeDuration":28},
      {"type":"text","text":"      95 index.html"},
      {"type":"prompt","text":"!grep -o \"<input[^>]*>\" index.html","cue":0,"typeDuration":46},
      {"type":"text","text":"<input class=\"field\" type=\"text\" id=\"name\" …"},
      {"type":"prompt","text":"!grep -c \"#D97757\" index.html","cue":0,"typeDuration":40},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -n getDay index.html","cue":0,"typeDuration":36},
      {"type":"text","text":"75: var offset = (4 - now.getDay() + 7) % 7;"},
  ],[0,40,75,120,155,190,225,265], mascot="off")),
  [{"at":0.05,"event":"wc → 95"},{"at":0.35,"event":"one input"},{"at":0.6,"event":"#D97757 → 1"},{"at":0.85,"event":"getDay, line 75"}])

B("B05","THE MIDDLE CASE","TERMINAL",LIAM,
  "One more run I didn't plan. The bare folder — but with the check script left in it by accident. It found the script, read it, and built to pass it. And it passed. "
  "Then it added a contact field, a date, an expected frequency, and a reminder opt-in, in a serif face. The checker can't see intent. It passed the test and missed the point. "
  "That's why PROJECT.md exists: done is a script, but who it's for isn't.",
  "CCSession — check.py alone: PASS, then the extras",
  R("CCSession", session("studygroup — check.py only","accept-edits",[
      {"type":"tool","name":"Read","arg":"check.py","state":"done"},
      {"type":"text","text":"I'll build a self-contained index.html …"},
      {"type":"text","text":"following the constraints in check.py"},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check.py","state":"done"},
      {"type":"text","text":"PASS: index.html meets PROJECT.md's …"},
      {"type":"text","text":"a sign-up form (name, free-form contact"},
      {"type":"text","text":"field, date, what you're working on,"},
      {"type":"text","text":"expected frequency, reminder opt-in)"},
  ],[0,30,50,90,120,150,200,220,240], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"Read check.py"},{"at":0.45,"event":"PASS"},{"at":0.75,"event":"'reminder opt-in'"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, three conditions. Claude did the bare run; the handoff was the definition of done, and it failed it twice. "
  "Step three, the dangerous middle: reading the inputs — an email field for twelve friends — instead of the summary that said mobile-responsive. "
  "Then the real work, mine: nineteen lines in three files. Claude did the three-file run; handoff met, and every choice traces to a line. "
  "Then interpretive judgment: the check-only run passed the test and missed the point. Tool orchestration, zero; executive integration, zero. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · three conditions","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, three conditions"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 212 lines, emoji, email, mailto","handoff":"check.py passes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the inputs: an email field for friends","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write the three files — 19 lines, mine","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Three files: 95 lines, one input, next Thursday","handoff":"check.py passes; every choice traces to a file","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Check-only run: passed test, missed point","dependsOn":[2]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must answer the five questions myself — nobody else can. I must name the aesthetic decisions, or the internet's average gets named for me. "
  "I must write done as a check I can run. I should read the inputs, not the summary. Claude can fill a silence with the average page, and it will. "
  "It can build to a file and run the check — it did. It should say its plan first — it did. It should refuse what the file refuses — it did. Nineteen lines. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"fill silence with the average page"},{"tier":"CAN","text":"build to a file and run the check"},
                          {"tier":"SHOULD","text":"say its plan first — it did"},{"tier":"SHOULD","text":"refuse what the file refuses"}],
                    "human":[{"tier":"MUST","text":"answer the five questions myself"},{"tier":"MUST","text":"name the aesthetic decisions"},
                             {"tier":"MUST","text":"write done as a check I can run"},{"tier":"SHOULD","text":"read the inputs, not the summary"}],
                    "closing":"The design session, made durable. Nineteen lines. Mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence in an empty folder: two hundred twelve lines, emoji, an email wall, a mailto to a placeholder address. "
  "Three files first — nineteen lines of mine: ninety-five lines, a first name, one accent colour, and next Thursday computed. The checker alone passed the test and missed the point; done is a script, who it's for is not. "
  "What would prove this reel wrong: a bare run that refuses the email field on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "One sentence, empty folder: 212 lines, emoji, an email wall, mailto to a placeholder.",
      "Three files first — 19 lines of mine: 95 lines, a first name, one accent, next Thursday computed.",
      "The check script alone passed the test and missed the point. Done is a script; who it's for is not.",
      "FALSIFIABLE: a bare run that refuses the email field on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next build, open Claude Code and paste this: Ask me the five questions — who is this for, what should they feel, what does this refuse, what is done, what is out of scope — "
  "one at a time, and write my answers into PROJECT.md in my words. Then write DESIGN.md from what I tell you about tone and type. Don't build anything yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Ask me the five questions — who is this for, what should they feel, what does this refuse, what is done, what is out of scope — one at a time, and write my answers into PROJECT.md in my words. Don't build anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Three Files Before Claude Touches Anything. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same sentence, with and without 19 lines of yours. The difference is in the diff.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"01-context-and-memory","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/01-context-and-memory/claude-code--claude-liam-brutalist-three-file (the concept; the card body replaced by three real runs)",
    "sources":["SESSION.md (three real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
