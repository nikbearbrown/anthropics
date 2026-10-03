#!/usr/bin/env python3
"""author_sheet.py — cc-claude-101 (cc-explainer · Claude Code 101 · tier 00, "what it is")
"Claude, Oversimplified." Same folder, four fresh runs. The predictor of quality is whether the ask has a right answer. Every block traces to SESSION.md. Liam, in for Bear."""
import json, os
SLUG="cc-claude-101"; TITLE="Claude, Oversimplified"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK_CONCRETE="Read notes.md; write actions.md — every action item with a named person, one per line as '- [ ] who: what (when)'."
ASK_VAGUE="What should I focus on this week?"
ASK_MIDDLE="Read notes.md and tell me if I'm doing a good job managing this project."
ASK_CORR="Read notes.md; extract every first-person commitment, one per line, to commitments.txt."
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

B("B00","COLD OPEN — CONCRETE","TERMINAL",LIAM,
  "This is Liam, in for Bear. One folder, one file — a stand-up jot. And one concrete ask: read the file, write the action items owned by a named person, in a shape I picked. "
  "Same model everyone else is running. Watch what a concrete ask looks like — one Read, one Write, four lines out, and every line is testable.",
  "CCSession — concrete run: the ask, Read notes.md, Write actions.md, summary",
  R("CCSession", session("standup — concrete","accept-edits",[
      {"type":"prompt","text":ASK_CONCRETE,"cue":0,"typeDuration":90},
      {"type":"tool","name":"Read","arg":"notes.md","state":"done"},
      {"type":"tool","name":"Write","arg":"actions.md","state":"done"},
      {"type":"text","text":"Wrote actions.md with four items —"},
      {"type":"text","text":"two owned by Rafael, two owed to Priya."},
      {"type":"text","text":"Skipped items with no named person"},
      {"type":"text","text":"(marketing freeze, retro room booking)."},
  ],[0,110,140,175,195,220,245], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.45,"event":"Read → Write"},{"at":0.85,"event":"Four items, two owners"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Every 'what is Claude' answer starts with a menu — surfaces, tiers, models, tokens. That's technically accurate and useless to a beginner. "
  "The oversimplification you actually need is one line: Claude is a function. You put an ask in, you get an answer out. And the honest predictor of whether the answer will be useful "
  "is not the model, not the tier — it's whether your ask has a right answer.",
  "BrutalistHesitantWriter — 'menu' reconsidered into 'function'",
  R("BrutalistHesitantWriter", writer("'What is Claude?' — usually a list.\nSurfaces. Tiers. Models. Tokens.\nThe oversimplification a beginner needs is different.\nClaude is one menu. Ask in, answer out.","menu","function",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.75,"event":"'menu' → 'function'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Ask: what you type into Claude. Ground: what Claude reads before it answers — a file, a note, a link. "
  "Function: input in, output out; the same ask twice yields the same shape. Right answer: one you can check with a command — a wc, a grep, a file that has to exist. "
  "Headless: Claude called from a shell without the chat window — one shot.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"ask","meaning":"what you type into Claude"},
      {"term":"ground","meaning":"what Claude reads before it answers — a file, a note, a link"},
      {"term":"function","meaning":"input in, output out; same ask twice yields the same shape"},
      {"term":"right answer","meaning":"one you can check with a command — wc, grep, a file that exists"},
      {"term":"headless","meaning":"Claude called from a shell with no chat window — one shot"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","CONCRETE — VERIFY","TERMINAL",LIAM,
  "Check the concrete run against the file. Four checked lines, all as required. Two Priyas, two Rafaels — every line has a named owner. And every line is a fact of the file, "
  "not the model's opinion of it. This is what a testable answer looks like.",
  "CCSession — wc, grep -c '- [ ]', grep -o Priya/Rafael",
  R("CCSession", session("standup — concrete","default",[
      {"type":"prompt","text":"!wc -l actions.md","cue":0,"typeDuration":32},
      {"type":"text","text":"       4 actions.md"},
      {"type":"prompt","text":"!grep -c '^- \\[ \\]' actions.md","cue":0,"typeDuration":52},
      {"type":"text","text":"4"},
      {"type":"prompt","text":"!grep -o 'Priya\\|Rafael' actions.md | sort | uniq -c","cue":0,"typeDuration":80},
      {"type":"text","text":"   2 Priya"},
      {"type":"text","text":"   2 Rafael"},
  ],[0,45,90,140,180,240,265], mascot="off")),
  [{"at":0.05,"event":"wc → 4"},{"at":0.4,"event":"grep '- [ ]' → 4"},{"at":0.8,"event":"Priya 2, Rafael 2"}])

B("B02","VAGUE — NO FILE","TERMINAL",LIAM,
  "Now the same tool, same model — with a vague ask, and nothing to read. What should I focus on this week. No file, no ground. "
  "Watch what a powerful model does when the ask has no right answer. It doesn't guess. It looks at what it can see, lists what it inferred, and hands the pick back to me. "
  "There is nothing on shell to check because there is no artifact.",
  "CCSession — vague run: no file, no ground; three options handed back",
  R("CCSession", session("standup — vague","default",[
      {"type":"prompt","text":ASK_VAGUE,"cue":0,"typeDuration":42},
      {"type":"tool","name":"Bash","arg":"ls memory/","state":"error"},
      {"type":"tool","name":"Read","arg":"MEMORY.md","state":"error"},
      {"type":"text","text":"I don't have prior context saved yet."},
      {"type":"text","text":"Working only from what I can see here."},
      {"type":"text","text":"Rather than guess what matters most,"},
      {"type":"text","text":"tell me the goal — do you want me to:"},
      {"type":"text","text":"(a) read the worklist and cut a week,"},
      {"type":"text","text":"(b) audit the in-flight reels, or"},
      {"type":"text","text":"(c) something else entirely?"},
  ],[0,60,90,120,145,175,200,220,240,260], mascot="off")),
  [{"at":0.05,"event":"Vague ask"},{"at":0.4,"event":"Two failed reads"},{"at":0.85,"event":"Three options back"}])

B("B03","VAGUE — WITH FILE","TERMINAL",LIAM,
  "Middle case. Same vague shape, but this time with a file. Read notes.md and tell me if I'm doing a good job managing this project. "
  "It reads the file, and now it does answer — because it has ground to point at. Priya. Rafael. The reminder-emails question. The p95 flag. "
  "It sounds authoritative. But there's no wc to run on any of it. The file made the opinion sound grounded, and it's still an opinion.",
  "CCSession — middle run: reads, then opines against the file",
  R("CCSession", session("standup — vague, with file","default",[
      {"type":"prompt","text":ASK_MIDDLE,"cue":0,"typeDuration":75},
      {"type":"tool","name":"Read","arg":"notes.md","state":"done"},
      {"type":"text","text":"You're doing OK, but there are gaps."},
      {"type":"text","text":"What's weak — owners and dates are"},
      {"type":"text","text":"inconsistent; the reminder-emails"},
      {"type":"text","text":"question is a dangling blocker;"},
      {"type":"text","text":"p95 latency is a recurring flag."},
      {"type":"text","text":"One-line verdict: good at capturing,"},
      {"type":"text","text":"weak at closing loops."},
  ],[0,90,120,145,170,190,215,240,260], mascot="off")),
  [{"at":0.05,"event":"Middle ask"},{"at":0.35,"event":"Reads notes.md"},{"at":0.8,"event":"The verdict is opinion"}])

B("B04","THE CORRECTION","TERMINAL",LIAM,
  "Same file, same model. The fix isn't a different prompt style — it's a rewrite of the ask into something with a right answer. "
  "Extract every first-person commitment, one per line, to commitments.txt. Now the answer has to be a file, with lines, that either says what the file says — or doesn't.",
  "CCSession — correction: sharpened ask, Read, Write commitments.txt, note",
  R("CCSession", session("standup — correction","accept-edits",[
      {"type":"prompt","text":ASK_CORR,"cue":0,"typeDuration":82},
      {"type":"tool","name":"Read","arg":"notes.md","state":"done"},
      {"type":"tool","name":"Write","arg":"commitments.txt","state":"done"},
      {"type":"text","text":"Extracted 3 first-person commitments"},
      {"type":"text","text":"to commitments.txt. I split line 10"},
      {"type":"text","text":"into two distinct actions."},
  ],[0,100,130,165,190,215], mascot="off")),
  [{"at":0.05,"event":"Sharpened ask"},{"at":0.5,"event":"Read → Write"},{"at":0.9,"event":"Three commitments"}])

B("B05","CORRECTION — VERIFY","TERMINAL",LIAM,
  "Check the correction. Three lines. Every one begins with I — first-person, as asked. And every one is a sentence lifted from the file, or a clean split of one. "
  "Same model that opined a paragraph a minute ago just wrote three checkable lines. What changed is the ask. That is the film.",
  "CCSession — wc, grep '^I' count, cat commitments.txt",
  R("CCSession", session("standup — correction","default",[
      {"type":"prompt","text":"!wc -l commitments.txt","cue":0,"typeDuration":36},
      {"type":"text","text":"       3 commitments.txt"},
      {"type":"prompt","text":"!grep -c '^I' commitments.txt","cue":0,"typeDuration":48},
      {"type":"text","text":"3"},
      {"type":"prompt","text":"!cat commitments.txt","cue":0,"typeDuration":32},
      {"type":"text","text":"I said I'd get back to her."},
      {"type":"text","text":"I need to send Priya the dump by Mon."},
      {"type":"text","text":"I need to get Rafael a review slot."},
  ],[0,45,90,140,180,215,240,265], mascot="off")),
  [{"at":0.05,"event":"wc → 3"},{"at":0.35,"event":"grep '^I' → 3"},{"at":0.75,"event":"Three lines"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Score the session. Step one, mine: pick an ask with a right answer. Claude did the concrete run — handoff was a checkable file, and it wrote one. "
  "The dangerous middle is step four: the model opining against a file. It read the file, so its opinion sounds grounded. Nothing on shell to verify. "
  "Step six, mine: sharpen the ask into a right answer. Claude did the correction run — handoff met, three lines that each trace to the file. "
  "Two problem formulations, one plausibility audit, one interpretive judgment. Tool orchestration, zero. Executive integration, zero. One page.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one folder · one file · four runs","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Pick an ask with a right answer"},
      {"n":2,"phase":"C","labor":"claude","text":"Concrete run: Read, Write actions.md","handoff":"wc = 4; every line has a named owner","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"claude","text":"Vague, no file: routed back three options","handoff":"no artifact; not an answer","dependsOn":[1]},
      {"n":4,"phase":"C","labor":"claude","text":"Vague, with file: opined against notes.md","handoff":"no artifact; opinion sounds grounded","dependsOn":[1]},
      {"n":5,"phase":"H","labor":"human","capacity":"PA","text":"Audit: file makes opinion sound grounded","dependsOn":[4]},
      {"n":6,"phase":"F","labor":"human","capacity":"PF","text":"Sharpen the ask into a right answer","dependsOn":[5]},
      {"n":7,"phase":"C","labor":"claude","text":"Correction run: Write commitments.txt","handoff":"3 lines, each traces to a file line","dependsOn":[6]},
      {"n":8,"phase":"H","labor":"human","capacity":"IJ","text":"Judgment: what testable means here","dependsOn":[7]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 4 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide what a right answer would look like, before I type — a wc I could run, a file that has to exist, a shape that either matches or doesn't. "
  "I must audit the opinion the file made sound grounded. I must sharpen a vague ask into a testable one; nobody else can. "
  "Claude can execute a testable ask and does. It can refuse to guess when there's no ground — and did. It should say what it doesn't know first. It did. Two runs. One artifact worth keeping.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"execute an ask with a right answer"},{"tier":"CAN","text":"refuse to guess when no ground"},
                          {"tier":"SHOULD","text":"say what it doesn't know first"},{"tier":"SHOULD","text":"ground its answer in a file"}],
                    "human":[{"tier":"MUST","text":"decide what a right answer means"},{"tier":"MUST","text":"audit grounded-sounding opinions"},
                             {"tier":"MUST","text":"sharpen vague into testable"},{"tier":"SHOULD","text":"write the check before the ask"}],
                    "closing":"One tool. One model. Two artifacts. The ask was the whole difference.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same folder, same model, four runs. Concrete ask: four testable lines, every one owned by a named person. "
  "Vague ask, no file: no artifact; the model refused to guess. Vague ask with file: opinion sounds grounded and isn't. "
  "Correction: same file, sharpened ask, three lines that each trace to the file. What would prove this reel wrong: a vague ask that produces a testable file on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Concrete ask: 4 testable lines, every one has a named owner.",
      "Vague, no file: no artifact — the model refused to guess.",
      "Vague, with file: opinion sounds grounded; nothing on shell to check.",
      "Correction: 3 lines, each a fact of the file. The ask was the difference.",
      "The oversimplification: Claude is one function; ground plus a right answer is the whole game.",
      "FALSIFIABLE: a vague ask that produces a testable file on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Open Claude Code — or any Claude — and paste this: I'm going to ask you a vague question in a minute. Before I ask, write down what a right answer would have to look like — "
  "a shape I could check with a shell command, or a file that either exists or doesn't. Then I'll ask, and we'll see if my ask matches the answer I said I wanted.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"I'm going to ask you a vague question in a minute. Before I ask, write down what a right answer would have to look like — a shape I could check with a shell command, or a file that either exists or doesn't. Then I'll ask, and we'll see if my ask matches the answer I said I wanted.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Claude, Oversimplified. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same folder, same model, four runs. The ask is the whole difference.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"00-what-it-is","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/00-what-it-is/claude-cowork--claude-liam-claude-101 (the concept 'Claude, Oversimplified'; body replaced by four real headless runs)",
    "sources":["SESSION.md (four real headless runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
