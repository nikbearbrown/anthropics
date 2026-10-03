#!/usr/bin/env python3
"""author_sheet.py — cc-cwc-how-we-claude-code (cc-explainer · Claude Code 101 · tier 00, How Anthropic Uses Claude Code)
Three real fresh headless `claude -p` runs demonstrate the CWC workflow: Brainstorm → Design → Verify. Every block traces to SESSION.md. Liam, in for Bear."""
import json, os
SLUG="cc-cwc-how-we-claude-code"; TITLE="How Anthropic Uses Claude Code"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Build workshop.html — a one-page landing for our Saturday intro-to-git workshop."
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
  "This is Liam, in for Bear. One sentence, an empty folder: build a landing page for our Saturday git workshop. Watch what it decides on its own. "
  "The date. The hourly agenda. My email address, pulled from context. And a footer telling the internet 'Coffee provided. Questions welcome.' "
  "One hundred and thirty lines of decisions, and none of them are mine.",
  "CCSession — the bare run: the ask, two Reads, the lede, one Write",
  R("CCSession", session("workshop — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"task.txt","state":"done"},
      {"type":"text","text":"I'll build a clean single-file landing"},
      {"type":"text","text":"page with sensible placeholders where"},
      {"type":"text","text":"you'd normally drop in specifics (date,"},
      {"type":"text","text":"time, venue, signup link)."},
      {"type":"tool","name":"Write","arg":"workshop.html","state":"done"},
  ],[0,80,105,145,165,185,205,255])),
  [{"at":0.05,"event":"The ask types"},{"at":0.5,"event":"'sensible placeholders'"},{"at":0.9,"event":"Write workshop.html"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. When Anthropic ships internally with Claude Code, they don't type a prompt and hope for a better answer. They run a workflow — three phases in this order: "
  "brainstorm, design, verify. The point isn't a smarter model. The point is diverging before you converge — asking for four directions when you only need one, so the pick is a decision you made, not a default you accepted.",
  "BrutalistHesitantWriter — 'better' reconsidered into 'different'",
  R("BrutalistHesitantWriter", writer("A better prompt gets a better answer.\nAnthropic runs a different workflow.\nBrainstorm. Design. Verify.\nDiverge on four. Then converge.","better","different",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'better' → 'different'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Brainstorm: a structured interview that ends in a brief — a page with a point of view, not a feature list. "
  "Design: generate four divergent HTML mockups before you commit a line of production code. Verify: a fixture — a Python script that reads the DOM and prints PASS or FAIL. "
  "Definition of done: not a chat reply that says 'let me know if you want changes'; a check you can run.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"brainstorm","meaning":"a structured interview whose output is a brief — a page with a point of view"},
      {"term":"design","meaning":"generate four divergent HTML mockups before a line of production code is written"},
      {"term":"verify","meaning":"a fixture — a Python script that reads the DOM and prints PASS or FAIL"},
      {"term":"definition of done","meaning":"not a chat reply saying 'let me know'; a check you can run"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check what the bare run shipped. One hundred and thirty lines. No form — but a mailto in the RSVP block, to my address, which nobody told it. "
  "One 'welcome' in the footer. And a lede it invented about people who've heard 'just commit it' one too many times. Not wrong. Not mine. "
  "Nobody said what this was for, so it filled the silence with the internet's average workshop page.",
  "CCSession — wc, grep welcome, grep mailto",
  R("CCSession", session("workshop — bare","default",[
      {"type":"prompt","text":"!wc -l workshop.html","cue":0,"typeDuration":32},
      {"type":"text","text":"     130 workshop.html"},
      {"type":"prompt","text":"!grep -c \"welcome\" workshop.html","cue":0,"typeDuration":40},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -o \"mailto:[^\\\"]*\" workshop.html","cue":0,"typeDuration":48},
      {"type":"text","text":"mailto:bear@bearbrown.co"},
      {"type":"prompt","text":"!grep -c \"10:00\\|Coffee\" workshop.html","cue":0,"typeDuration":44},
      {"type":"text","text":"2"},
  ],[0,42,80,125,160,215,250,290])),
  [{"at":0.05,"event":"wc → 130"},{"at":0.35,"event":"the mailto it made up"},{"at":0.75,"event":"'welcome' and 'Coffee'"}])

B("B02","THE BRIEF — PHASE 1","SHELL",LIAM,
  "Phase one — brainstorm. I don't ask Claude for a page yet; I write brief.md — the output of an interview I'd already had with the people who'd actually show up. "
  "Seven lines. Who it's for: not developers. What they should feel: version control is a habit, not a system to conquer. What is refused: screenshots, stock photos, enthusiasm words. "
  "The chosen direction, once I see the mockups, will go on the last line. A brief with a point of view — not a feature list.",
  "CCPlainShell — cat brief.md (excerpt)",
  R("CCPlainShell",{"title":"zsh — ~/workshop","lines":[
      "$ wc -l brief.md",
      "       7 brief.md",
      "$ grep '^- ' brief.md | cut -c1-58",
      "- Who it's for. People who write text of any kind …",
      "- What they should feel. Version control is a habit…",
      "- What is refused. Screenshots. Stock photos. Enthu…",
      "- What done means. python3 fixture.py passes. Every…",
      "- Voice + look. Dry, first-person plural, terminal …",
      "- Chosen direction. mock2.html — terminal / TTY."],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the brief is a plain-text file read in a normal shell; no session contains it"),
  [{"at":0.05,"event":"wc → 7"},{"at":0.4,"event":"'a point of view'"},{"at":0.85,"event":"Chosen direction"}])

B("B03","DESIGN — DIVERGE","TERMINAL",LIAM,
  "Phase two — design. Same folder. New ask: read task.txt, then generate four divergent HTML mockups. Not variations of one thing — four different content architectures, four different voices, four different visual tones. "
  "Do not build anything else. Do not run anything. Five minutes later, four self-contained pages: modern SaaS, terminal, hand-drawn zine, editorial magazine.",
  "CCSession — the diverge ask + four Writes",
  R("CCSession", session("workshop — design","accept-edits",[
      {"type":"prompt","text":"Read task.txt. Generate FOUR","cue":0,"typeDuration":36},
      {"type":"prompt","text":"divergent HTML mockups — mock1..4.","cue":0,"typeDuration":40},
      {"type":"tool","name":"Read","arg":"task.txt","state":"done"},
      {"type":"text","text":"Four directions: SaaS, terminal,"},
      {"type":"text","text":"zine, editorial magazine."},
      {"type":"tool","name":"Write","arg":"mock1.html","state":"done"},
      {"type":"tool","name":"Write","arg":"mock2.html","state":"done"},
      {"type":"tool","name":"Write","arg":"mock3.html","state":"done"},
      {"type":"tool","name":"Write","arg":"mock4.html","state":"done"},
  ],[0,42,90,120,145,175,205,230,255])),
  [{"at":0.05,"event":"The diverge ask"},{"at":0.5,"event":"'four directions'"},{"at":0.9,"event":"Four Writes"}])

B("B04","THE FOUR MOCKS","SHELL",LIAM,
  "The proof they're actually different. Four line counts: nineteen ninety-nine, two-oh-one, two-thirty-nine, two-seventy. And the body font in each — one line each: "
  "apple system sans, ui-monospace, Bodoni serif with Courier accents, Iowan Old Style serif. Same paragraph. Four type systems. That is what generating four directions buys.",
  "CCPlainShell — wc mock*.html, body font per mock",
  R("CCPlainShell",{"title":"zsh — ~/workshop","lines":[
      "$ wc -l mock*.html",
      "     199 mock1.html",
      "     201 mock2.html",
      "     239 mock3.html",
      "     270 mock4.html",
      "$ for f in mock*; do grep 'body{font:' $f; done",
      "mock1  -apple-system,BlinkMacSystemFont,…    sans",
      "mock2  ui-monospace,SFMono-Regular,…Menlo,   mono",
      "mock3  \"Bodoni 72\",\"Didot\",Georgia,serif   +Cour",
      "mock4  \"Iowan Old Style\",Georgia,serif       serif"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="four files inspected side-by-side in a plain shell; no session shows this comparison"),
  [{"at":0.05,"event":"wc four mocks"},{"at":0.5,"event":"the font per mock"},{"at":0.9,"event":"'four type systems'"}])

B("B05","PICK — AND WRITE THE FIXTURE","SHELL",LIAM,
  "The pick is mine. Mock two — terminal — because a git workshop should look like the tool it teaches. Then, before the third run, I write fixture.py: the definition of done as a script. "
  "One h1. A form with a name field and no email. An id=register submit button. No banned words — welcome, amazing, join us. Monospace font-family. Under two hundred lines. "
  "This is what phase three needs: a check the machine can run.",
  "CCPlainShell — cat fixture.py (excerpt)",
  R("CCPlainShell",{"title":"zsh — ~/workshop","lines":[
      "$ wc -l fixture.py",
      "      36 fixture.py",
      "$ grep 'fail(' fixture.py | cut -c1-58",
      "fail('external <link>/<script> src (no external ass…",
      "fail('no monospace font-family (voice: terminal)')",
      "fail(f'want exactly one <h1>, got {len(h1s)}')",
      "fail('email field forbidden (no sign-up wall)')",
      "fail('no #register control')",
      "for banned in ('welcome','amazing','join us','excit…"],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the fixture is read in a plain shell before the verify run; no session shows its authoring"),
  [{"at":0.05,"event":"wc → 36"},{"at":0.4,"event":"the failure list"},{"at":0.85,"event":"banned words"}])

B("B06","VERIFY — CONVERGE","TERMINAL",LIAM,
  "Phase three — verify. Same folder plus my three files. Ask: read brief.md and mock2, build workshop.html to satisfy the brief, then run fixture.py before you say done. "
  "It reads the brief. It reads the mock. It writes. It runs the check itself — FAIL. Monospace missing, because it used the CSS font shorthand and my grep wanted font-family literally. It edits. Runs again. PASS. One hundred and fifty-three lines.",
  "CCSession — Reads, Write, fixture FAIL, Edit, fixture PASS",
  R("CCSession", session("workshop — verify","accept-edits",[
      {"type":"prompt","text":"Read brief.md and mock2. Build","cue":0,"typeDuration":40},
      {"type":"prompt","text":"workshop.html — run fixture.py.","cue":0,"typeDuration":40},
      {"type":"tool","name":"Read","arg":"brief.md","state":"done"},
      {"type":"tool","name":"Read","arg":"mock2.html","state":"done"},
      {"type":"tool","name":"Read","arg":"fixture.py","state":"done"},
      {"type":"tool","name":"Write","arg":"workshop.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 fixture.py","state":"done"},
      {"type":"text","text":"FAIL: no monospace font-family"},
      {"type":"tool","name":"Edit","arg":"workshop.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 fixture.py","state":"done"},
      {"type":"text","text":"PASS: workshop.html meets brief.md's"},
  ],[0,42,80,110,140,170,205,235,265,295,325])),
  [{"at":0.05,"event":"The verify ask"},{"at":0.4,"event":"Fixture FAIL"},{"at":0.85,"event":"Edit → PASS"}])

B("B07","VERIFY — VERIFY","TERMINAL",LIAM,
  "Now check the checker. Two commands. The final page has one input for a name and one for a goal — neither is an email. And the exact font-family line: ui-monospace, SFMono-Regular, JetBrains Mono, Menlo. "
  "Every line on that page is a line from the brief or the mock. Same model, same task, same folder. The difference is what I wrote before I asked.",
  "CCSession — grep inputs, grep font-family",
  R("CCSession", session("workshop — verify","default",[
      {"type":"prompt","text":"!grep -oE \"<input[^>]*>\" workshop.html","cue":0,"typeDuration":52},
      {"type":"text","text":"<input type=\"text\" name=\"name\" …"},
      {"type":"text","text":"<input type=\"text\" name=\"goal\" …"},
      {"type":"prompt","text":"!grep -oE \"font-family:[^;]*\" .","cue":0,"typeDuration":42},
      {"type":"text","text":"font-family:ui-monospace,SFMono-Regular,"},
      {"type":"text","text":"\"JetBrains Mono\",Menlo,Consolas,monospace"},
      {"type":"prompt","text":"!grep -c \"welcome\\|amazing\" *.html","cue":0,"typeDuration":42},
      {"type":"text","text":"0"},
  ],[0,55,85,115,160,195,225,270])),
  [{"at":0.05,"event":"two inputs, no email"},{"at":0.45,"event":"the mono font-family"},{"at":0.9,"event":"'welcome' → 0"}])

B("B08","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, no discipline. Claude did the bare run — plausible page, mailto to my inbox, an invented hourly agenda. "
  "Step three, the dangerous middle: reading what it actually shipped, catching the mailto and the invented agenda instead of clicking through the polished result. "
  "Then the real work, mine: brief.md and fixture.py — thirteen lines and thirty-six. Then Claude did the diverge — four philosophies. I picked mock two. "
  "Claude did the converge — wrote, ran the checker itself, failed on monospace, edited, passed. Interpretive judgment, zero. Executive integration, zero. No page requires them. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"three phases · one workflow","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, no discipline"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 130 lines, mailto, invented agenda","handoff":"none — no fixture to fail","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the output: caught the mailto","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write brief.md + fixture.py","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Design: 4 mockups, 4 type systems","handoff":"visibly divergent, not variations","dependsOn":[4]},
      {"n":6,"phase":"C","labor":"human","capacity":"PA","text":"Pick mock2 — the terminal","dependsOn":[5]},
      {"n":7,"phase":"C","labor":"claude","text":"Verify: build, run check, fail, edit","handoff":"python3 fixture.py prints PASS","dependsOn":[6]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B09","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide the point of view — nobody else can. I must write the brief; a feature list is not a brief. "
  "I must write done as a script — Claude cannot grade its own homework. I should read the mockups before I pick — the pick is the film. "
  "Claude can fill silence with the average page, and it will. It can generate four philosophies in five minutes; it did. It should run the check itself — it did. It should read a failure and edit — it did.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"fill silence with the average page"},{"tier":"CAN","text":"draft four philosophies in minutes"},
                          {"tier":"SHOULD","text":"run the fixture itself — it did"},{"tier":"SHOULD","text":"read a failure and edit"}],
                    "human":[{"tier":"MUST","text":"decide the point of view"},{"tier":"MUST","text":"write the brief, not a list"},
                             {"tier":"MUST","text":"write done as a script"},{"tier":"SHOULD","text":"read the four before you pick"}],
                    "closing":"Three phases. One workflow. The pick is the film.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence in an empty folder: 130 lines, a mailto to my inbox, an invented agenda. "
  "Brainstorm — 7 lines of brief.md and a point of view. Design — 4 mockups, sans, mono, mixed, serif; I picked mono. "
  "Verify — 36 lines of fixture.py; Claude ran it, failed on monospace, edited, passed at 153. "
  "What would prove this reel wrong: a bare run that asks the six questions before writing a page.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare: 130 lines, mailto to my inbox, an invented agenda. Polished. Not mine.",
      "Brainstorm: 7 lines of brief.md — a page with a point of view, not a feature list.",
      "Design: 4 divergent mockups — sans, mono, mixed, serif. The pick is the film.",
      "Verify: 36 lines of fixture.py. Claude ran it, failed, edited, passed at 153.",
      "Three phases. One workflow. The difference is what you wrote before you asked.",
      "FALSIFIABLE: a bare run that asks the interview questions before writing a page."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next build, open Claude Code in an empty folder and paste this: "
  "run the three phases on the smallest thing on your list. Interview me and write brief.md. Then generate four divergent mockups. Then write fixture.py from the brief and stop. Do not build the thing yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Run the three phases on the smallest thing on my list. Interview me and write brief.md. Then generate four divergent HTML mockups. Then write fixture.py from the brief and stop. Don't build the thing yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"How Anthropic Uses Claude Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"One sentence, three phases: brainstorm, design, verify. Diverge on four. Converge on a fixture.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-code--cwc-how-we-claude-code (the concept from the CWC workshop; the card body replaced by three real runs)",
    "sources":["SESSION.md (three real runs: bare, design, verify)","CWC Workshop — How We Claude Code (Anthropic internal workflow)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
    if r["pattern"]=="CCPlainShell":
        for line in r["props"]["lines"]:
            if len(line)>64: print("  ⚠ shell",len(line),line)
