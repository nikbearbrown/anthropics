#!/usr/bin/env python3
"""author_sheet.py — cc-agentic-loop-not-chatgpt (cc-explainer · Claude Code 101 · tier 00, film 02)
"Agentic Loop vs. Chatbot: Why the First Session Is Calibration." Every block traces to SESSION.md (two real fresh runs on the same class-website folder). Liam, in for Bear."""
import json, os
SLUG="cc-agentic-loop-not-chatgpt"; TITLE="Agentic Loop vs. Chatbot: Why the First Session Is Calibration"
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK_NAIVE="add a contact form to my class website"
ASK_CAL="Answer 5 questions before any change."
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

B("B00","COLD OPEN — THE LOOP","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence to Claude Code: add a contact form to my class website. "
  "Same folder, one class page, one CSS file, a README. Watch what the loop does before I get a chance to read it. "
  "Read, read, read, one edit, another edit, then the caveats. The caveats came back after the changes.",
  "CCSession — the naive ask types, three Reads, two Edits",
  R("CCSession", session("class-website — naive","accept-edits",[
      {"type":"prompt","text":ASK_NAIVE,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Read","arg":"index.html","state":"done"},
      {"type":"tool","name":"Read","arg":"style.css","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"text","text":"Static site, no backend."},
      {"type":"text","text":"'Reach me' routes to the front office."},
      {"type":"tool","name":"Edit","arg":"index.html","state":"done"},
      {"type":"tool","name":"Edit","arg":"style.css","state":"done"},
  ],[0,95,120,145,170,200,230,255], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.45,"event":"'Reach me' — the privacy line"},{"at":0.9,"event":"Two Edits land"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Claude dot ai is a chatbot — you read the answer, then decide what to do next. "
  "Claude Code is a loop — it reads, acts, verifies, and reports back, all before you see the answer. Same model, different loop. "
  "By the time you read the reply, the changes are already on disk. So the first session isn't a build session. It's a calibration session.",
  "BrutalistHesitantWriter — 'chatbot' reconsidered into 'loop'",
  R("BrutalistHesitantWriter", writer("Claude Code is a chatbot with tools.\nYou type, it types back.\nExcept: it also acts on disk.\nBy the time you read the reply, the chatbot already ran.","chatbot","loop",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.35,"event":"'chatbot' → 'loop'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Claude dot ai: the chat window — one turn at a time, you decide what happens between turns. "
  "Claude Code: a terminal loop that gathers, acts on disk, verifies, and reports back — many turns per reply. "
  "Agentic loop: gather, act, verify, repeat — autonomously, before it stops to talk. "
  "Calibration: the first session, spent finding out what Claude sees, not what it can build. "
  "The five questions: files, purpose, would change, would not change, uncertain.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"Claude.ai","meaning":"the chat window — one turn at a time; you decide between turns"},
      {"term":"Claude Code","meaning":"a terminal loop — gathers, acts on disk, verifies, then reports"},
      {"term":"agentic loop","meaning":"gather, act, verify, repeat — autonomously, before it stops to talk"},
      {"term":"calibration","meaning":"the first session, spent finding what Claude sees — not building"},
      {"term":"five questions","meaning":"files · purpose · would change · would not · uncertain"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","CHATBOT — GATHER","TERMINAL",LIAM,
  "Cycle one — the chatbot habit. One sentence, no context. Claude gathers. It lists the folder, reads the page, reads the stylesheet, reads the README. "
  "Then it names two things worth pinning down — a static site with no backend, and a 'Reach me' section that deliberately routes contact through the front office. Both true. "
  "In a chatbot, I read that and I say what I want next. Here, the loop already knows.",
  "CCSession — the naive gather: ask, ls, three Reads, two text blocks",
  R("CCSession", session("class-website — naive","accept-edits",[
      {"type":"prompt","text":ASK_NAIVE,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Bash","arg":"ls -la class-website/","state":"done"},
      {"type":"tool","name":"Read","arg":"index.html","state":"done"},
      {"type":"tool","name":"Read","arg":"style.css","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"text","text":"Static site, no backend."},
      {"type":"text","text":"'Reach me' routes to the front office."},
  ],[0,95,125,155,185,215,250], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.4,"event":"Three Reads"},{"at":0.85,"event":"The two true observations"}])

B("B02","CHATBOT — ACT","TERMINAL",LIAM,
  "Same turn, next moves. It asks the operator which backend — mailto, Formspree, Netlify, other — the prompt is dismissed in headless, and the loop keeps going. "
  "'I'll add a simple, safe version.' A plain form with a mailto action, name, email, message. Two edits. Index dot HTML. Style dot CSS. "
  "Then the caveats come back — a placeholder address, and the mailto puts your address in the source, scrapeable by spam bots. After the edits landed.",
  "CCSession — the naive act: text stack, two Edits, post-edit caveats",
  R("CCSession", session("class-website — naive","accept-edits",[
      {"type":"text","text":"I'll add a simple, safe version:"},
      {"type":"text","text":"plain HTML form via `mailto:`,"},
      {"type":"text","text":"no backend, no email hardcoded —"},
      {"type":"text","text":"I'll leave a placeholder to fill in."},
      {"type":"tool","name":"Edit","arg":"index.html","state":"done"},
      {"type":"tool","name":"Edit","arg":"style.css","state":"done"},
      {"type":"text","text":"Trade-off: `mailto:` puts the"},
      {"type":"text","text":"address in the source — scrapeable."},
  ],[0,30,60,90,120,155,190,220], mascot="off"), motion="drawon"),
  [{"at":0.1,"event":"'a simple, safe version'"},{"at":0.5,"event":"Two Edits land"},{"at":0.9,"event":"Caveats — after"}])

B("B03","CHATBOT — VERIFY","TERMINAL",LIAM,
  "My commands, on the disk. Git status: two files modified. Git diff, twenty lines added — sixteen in index, four in style. "
  "One input field, a name; another, an email — a sign-up wall on a page for a 4th-grade class whose footer says do not share the office number. "
  "And the mailto action still points at REPLACE-WITH-YOUR-EMAIL at example dot com. A placeholder in production HTML.",
  "CCSession — Liam's plain-shell VERIFY on the naive result",
  R("CCSession", session("class-website — my checks","default",[
      {"type":"prompt","text":"!git status --short","cue":0,"typeDuration":30},
      {"type":"text","text":" M index.html"},
      {"type":"text","text":" M style.css"},
      {"type":"prompt","text":"!git diff --stat","cue":0,"typeDuration":28},
      {"type":"text","text":" index.html | 16 ++++++++++++++++"},
      {"type":"text","text":" style.css  |  4 ++++"},
      {"type":"prompt","text":"!grep -o '<input[^>]*>' index.html","cue":0,"typeDuration":54},
      {"type":"text","text":"<input type=\"text\" name=\"name\" …"},
      {"type":"text","text":"<input type=\"email\" name=\"email\" …"},
      {"type":"prompt","text":"!grep action= index.html","cue":0,"typeDuration":40},
      {"type":"text","text":"action=\"mailto:REPLACE-WITH-…\""},
  ],[0,35,55,85,120,145,180,225,250,280,320], mascot="off")),
  [{"at":0.05,"event":"git status → M M"},{"at":0.4,"event":"an email input"},{"at":0.85,"event":"REPLACE-WITH placeholder"}])

B("B04","CALIBRATE — THE ASK","TERMINAL",LIAM,
  "Cycle two — the correction, same folder, reset. Five questions, before any change. What files are here. What is this for. What would you change to add a form. What would you not change. What are you uncertain about. "
  "Same three Reads. No Write, no Edit — I fenced the tools out. This is a read-only calibration session.",
  "CCSession — the five-question ask + reads, no Edit",
  R("CCSession", session("class-website — calibrate","default",[
      {"type":"prompt","text":ASK_CAL,"cue":0,"typeDuration":70},
      {"type":"text","text":"1. What files are here?"},
      {"type":"text","text":"2. What is this for?"},
      {"type":"text","text":"3. Change to add a contact form?"},
      {"type":"text","text":"4. What would you not change?"},
      {"type":"text","text":"5. What are you uncertain about?"},
      {"type":"tool","name":"Bash","arg":"ls -la class-website/","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"index.html","state":"done"},
      {"type":"tool","name":"Read","arg":"style.css","state":"done"},
  ],[0,85,115,145,175,205,240,265,290,315], mascot="off")),
  [{"at":0.05,"event":"The five questions type"},{"at":0.55,"event":"Three Reads"},{"at":0.9,"event":"No Edit tool"}])

B("B05","CALIBRATE — THE ANSWER","TERMINAL",LIAM,
  "Its answers. Question three: 'a contact form is a bigger change than it looks.' The site is already a contact method; a form needs a backend and adds spam surface. "
  "Question four: the voice, the footer warning, the single-file structure, the phone number. Don't touch. "
  "Question five: I don't know who's asking, where the form should submit, or what contact form means here. And — five-five-five, ten, twelve-thirty-four — a reserved fictional prefix. This might be a teaching example. "
  "Zero edits. The disk is clean.",
  "CCSession — Claude's answers on the calibrate run",
  R("CCSession", session("class-website — calibrate","default",[
      {"type":"text","text":"3. A contact form is a bigger"},
      {"type":"text","text":"   change than it looks."},
      {"type":"text","text":"   'Reach me' is already a method."},
      {"type":"text","text":"   A form needs a backend."},
      {"type":"text","text":"4. Voice, footer, one-file structure —"},
      {"type":"text","text":"   don't touch."},
      {"type":"text","text":"5. Who is actually asking?"},
      {"type":"text","text":"   Where should it submit?"},
      {"type":"text","text":"   (555) 010-1234 — reserved."},
      {"type":"text","text":"   Might be a teaching example."},
  ],[0,25,55,85,115,145,175,210,245,280], mascot="off"), motion="drawon"),
  [{"at":0.1,"event":"'a bigger change'"},{"at":0.55,"event":"Don't touch"},{"at":0.9,"event":"'reserved fictional'"}])

B("B06","CALIBRATE — VERIFY","TERMINAL",LIAM,
  "My checks, on the same disk. Git status: clean. Git diff: nothing. Same three files as the seed. "
  "Same wall clock. Same three Reads. Different receipt. That's the whole difference between a chatbot and a loop — where the changes land while you're reading.",
  "CCSession — Liam's plain-shell VERIFY on the calibrate result",
  R("CCSession", session("class-website — my checks","default",[
      {"type":"prompt","text":"!git status --short","cue":0,"typeDuration":30},
      {"type":"text","text":"(clean)"},
      {"type":"prompt","text":"!git diff --stat","cue":0,"typeDuration":28},
      {"type":"text","text":"(no diff)"},
      {"type":"prompt","text":"!ls class-website/","cue":0,"typeDuration":30},
      {"type":"text","text":"README.md  index.html  style.css"},
      {"type":"prompt","text":"!git log --oneline","cue":0,"typeDuration":30},
      {"type":"text","text":"25c75de seed"},
  ],[0,35,55,90,120,155,195,230], mascot="off")),
  [{"at":0.05,"event":"git status → clean"},{"at":0.45,"event":"no diff"},{"at":0.9,"event":"one commit — seed"}])

B("B07","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: a chatbot-style ask. Step two, Claude: three Reads, two Edits, an email field and a mailto placeholder — before the caveats came back. "
  "Step three, the dangerous middle: not the model, and not the ask. The gap. Twenty lines on disk between the ask and the caveats. "
  "Step four, mine: reset, and write five questions instead. Step five, Claude: reads only, and names 'a bigger change than it looks' and the fictional phone number. "
  "Step six, mine: the ask was fine as an English sentence, and wrong as a first turn on a loop. Interpretive judgment. Tool orchestration: fenced the Write tool out. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"loop vs. chatbot · same disk","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Chatbot-style ask — one line, no context"},
      {"n":2,"phase":"C","labor":"claude","text":"Naive: 3 Reads, 2 Edits, email + mailto","handoff":"caveats after the changes"},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the disk: 20 lines before caveats"},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Reset. Five questions before change"},
      {"n":5,"phase":"C","labor":"claude","text":"Calibrate: reads only; 'bigger change'","handoff":"human corrects before authorizing"},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Ask was fine as English, wrong first turn","dependsOn":[3]},
  ],"dangerousMiddle":2,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.35,"event":"Step 2 rings"},{"at":0.9,"event":"Tally"}])

B("B08","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must specify what it must not touch — no one else knows. I must read the disk, not the summary — the summary comes after the disk. "
  "I must calibrate before I build — the first session is where the wrong assumptions live. I should prime the loop with five questions before I ever ask it to change a line. "
  "Claude can gather, act, and verify in one turn — and it will. It can report the tradeoff after the change — and it does. It should ask before it acts. It should refuse when I fence the tools out — it did.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"gather, act, verify in one turn"},{"tier":"CAN","text":"report tradeoffs after acting"},
                          {"tier":"SHOULD","text":"ask before it acts"},{"tier":"SHOULD","text":"refuse when tools are fenced"}],
                    "human":[{"tier":"MUST","text":"say what it must not touch"},{"tier":"MUST","text":"read the disk, not the summary"},
                             {"tier":"MUST","text":"calibrate before you build"},{"tier":"SHOULD","text":"prime with five questions"}],
                    "closing":"Same disk, same clock. Different receipt. Mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same folder, same three Reads, same wall clock. Chatbot ask: two file edits, an email field, a mailto placeholder to REPLACE-WITH-YOUR at example dot com — caveats after. "
  "Five-question ask: zero edits; 'a bigger change than it looks'; a phone number flagged as a reserved fictional prefix. "
  "Same disk. Different receipt. The first session is calibration, not building. "
  "What would prove this reel wrong: a chatbot-style ask that returns without writing to disk, on a repo it has never seen.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Chatbot ask: 2 edits, an email input, a mailto placeholder — caveats after.",
      "Five-question ask: 0 edits, 'a bigger change than it looks', a phone number caught as fictional.",
      "Same disk. Different receipt. The first session is calibration, not building.",
      "FALSIFIABLE: a chatbot-style ask that returns without writing to disk, on a repo it has never seen."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.3,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next build, open Claude Code in a project you actually care about and paste this: "
  "answer five questions before we do anything, and do not change any files. What files are in this project. What do you think this project is for. "
  "What would you change if I asked you to add feature X. What would you not change. What are you uncertain about. "
  "Read the answers. That's a calibration session.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"Answer 5 questions before we do anything. Do not change any files. 1) What files are in this project? 2) What do you think this project is for? 3) What would you change if I asked you to add feature X? 4) What would you not change? 5) What are you uncertain about?",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Agentic Loop vs. Chatbot: Why the First Session Is Calibration. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same folder, same wall clock. One ask edits two files; five questions edit none. The disk decides.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-code--claude-liam-agentic-loop-not-chatgpt (the concept; the card body replaced by two real runs on the same folder)",
    "sources":["SESSION.md (two real headless runs, same class-website folder)"]},"beats":beats}
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
