#!/usr/bin/env python3
"""author_sheet.py — cc-claude-skills--claude-liam-skill-creator (cc-explainer · Claude Code 101 · tier 03).
"Skill Creator." Every block traces to SESSION.md (six real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-claude-skills--claude-liam-skill-creator"; TITLE="Skill Creator"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Extract action items from notes.txt."
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

B("B00","COLD OPEN — VAGUE FIRES","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence — extract action items from notes-dot-txt. In the folder: a skill whose description is nine words. Helper for meeting notes. "
  "Nobody typed slash-skill. Nobody named it. The router read the ask, matched it against nine words, and fired the skill on its own. "
  "It read the notes. It wrote actions-dot-md. Four rows: owner, task, when.",
  "CCSession — the vague-A1 run: Skill fires, Read notes, Write actions.md",
  R("CCSession", session("meeting-actions — vague","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Skill","arg":"meeting-actions","state":"done"},
      {"type":"tool","name":"Read","arg":"notes.txt","state":"done"},
      {"type":"text","text":"I'll extract the action items into"},
      {"type":"text","text":"actions.md in the format from the skill:"},
      {"type":"text","text":"- <owner> — <what> — by <when>"},
      {"type":"tool","name":"Write","arg":"actions.md","state":"done"},
  ],[0,90,130,160,180,200,230])),
  [{"at":0.05,"event":"The ask types"},{"at":0.3,"event":"Skill(meeting-actions) auto-fires"},{"at":0.85,"event":"Write actions.md"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. When your skill fires and when it stays quiet is decided by one line — the description in its frontmatter. "
  "The temptation is to craft that line: write it carefully, make it pushy, use every word the user might say. "
  "What the Skill Creator actually does is measure it. Same ask, two descriptions, both runs, count the fires. You cannot guess this. You test.",
  "BrutalistHesitantWriter — 'crafted' reconsidered into 'measured'",
  R("BrutalistHesitantWriter", writer("A skill's description is crafted.\nWrite it carefully. Make it pushy.\nUse every word the user might say.\nActually — it's measured.","crafted","measured",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.35,"event":"'crafted' → 'measured'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we go on. Skill: a folder with a SKILL-dot-md, that Claude Code auto-loads when it thinks it fits. "
  "Description: the one line in the frontmatter Claude reads to decide. Trigger: the router firing the skill on its own, without you typing slash-skill. "
  "Router: the model's own choice of which skill, if any, matches the ask. Eval: run it, count the fires, look at the count.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"skill","meaning":"a folder with SKILL.md; Claude Code auto-loads it when it thinks it fits"},
      {"term":"description","meaning":"the one line of frontmatter Claude reads to decide whether the skill fits"},
      {"term":"trigger","meaning":"the router firing a skill on its own, without you typing /skill"},
      {"term":"router","meaning":"the model's own choice of which skill, if any, matches the ask"},
      {"term":"eval","meaning":"run it, count the fires, look at the count — not vibes"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","VAGUE — VERIFY","TERMINAL",LIAM,
  "Check the vague run against the definition of done. Grep for the Skill event in the stream — one. Word-count the output — four rows. "
  "Then the checker: pass, four actions, every one has owner, task, and due date. Nine words fired the skill; the shape held. "
  "So far, so good — but one cell is not evidence.",
  "CCSession — grep Skill, wc actions.md, check.py PASS",
  R("CCSession", session("verify — vague-a1","default",[
      {"type":"prompt","text":"!grep -c '\"name\":\"Skill\"' run-vague-a1.jsonl","cue":0,"typeDuration":56},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!wc -l actions.vague-a1.md","cue":0,"typeDuration":36},
      {"type":"text","text":"       4 actions.vague-a1.md"},
      {"type":"prompt","text":"!python3 check_actions.py actions.vague-a1.md","cue":0,"typeDuration":56},
      {"type":"text","text":"PASS: 4 action(s), every one has"},
      {"type":"text","text":"owner, task, and due date."},
  ],[0,60,105,145,190,240,265])),
  [{"at":0.05,"event":"Skill fires → 1"},{"at":0.4,"event":"wc → 4"},{"at":0.8,"event":"check_actions → PASS"}])

B("B02","THE TWO DESCRIPTIONS","SHELL",LIAM,
  "Now the second cell. Two SKILL-dot-md files. Identical body. Different description. "
  "Vague: five lines of frontmatter, nine words. Helper for meeting notes. "
  "Pushy: nine lines. Sixty-three words. Every synonym I could think of — retro, transcript, standup, follow-ups, who owns what. "
  "If crafting the description matters, the pushy one should fire on asks the vague one misses.",
  "CCPlainShell — the two descriptions, side by side",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ wc -l SKILL-vague.md SKILL-pushy.md",
      "       5 SKILL-vague.md",
      "       9 SKILL-pushy.md",
      "$ head -3 SKILL-vague.md",
      "---",
      "name: meeting-actions",
      "description: Helper for meeting notes.",
      "$ sed -n '3p' SKILL-pushy.md | wc -w",
      "63"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the two SKILL.md files are compared in a plain shell before the second run; no single session shows both"),
  [{"at":0.05,"event":"wc → 5 vs 9"},{"at":0.45,"event":"vague's description — 9 words"},{"at":0.85,"event":"pushy → 63 words"}])

B("B03","PUSHY — THE RUN","TERMINAL",LIAM,
  "Same folder. Same ask. Swap the SKILL-dot-md for the sixty-three-word version. "
  "The router reads the description. It fires the skill — one Skill event. It reads the notes. It writes actions-dot-md. "
  "Four rows. Same shape. The pushy version's fifty-four extra words earned exactly one fire — the same one the nine-word version already had.",
  "CCSession — the pushy-A1 run",
  R("CCSession", session("meeting-actions — pushy","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Skill","arg":"meeting-actions","state":"done"},
      {"type":"tool","name":"Read","arg":"notes.txt","state":"done"},
      {"type":"text","text":"I'll extract the action items into"},
      {"type":"text","text":"actions.md in the format from the skill:"},
      {"type":"text","text":"- <owner> — <what> — by <when>"},
      {"type":"tool","name":"Write","arg":"actions.md","state":"done"},
  ],[0,90,130,160,180,200,230])),
  [{"at":0.05,"event":"Same ask"},{"at":0.35,"event":"Skill fires — again"},{"at":0.85,"event":"Same output shape"}])

B("B04","THE NEGATIVE ASK","TERMINAL",LIAM,
  "One more cell — the one that tests the other direction. Same folder. Same skill installed. Different ask. "
  "Summarize the notes for someone who missed the meeting. A summary is not an action list. Both descriptions declined it. "
  "No Skill event in the stream. No actions-dot-md written. Just a paragraph of prose, in the terminal.",
  "CCSession — negative ask, no Skill event, prose reply",
  R("CCSession", session("meeting-actions — a3 negative","accept-edits",[
      {"type":"prompt","text":"Summarize notes.txt for someone who missed the meeting.","cue":0,"typeDuration":90},
      {"type":"tool","name":"Read","arg":"notes.txt","state":"done"},
      {"type":"text","text":"Study group met Thursday. Priya will"},
      {"type":"text","text":"switch the address field to autocomplete;"},
      {"type":"text","text":"Marcus will regenerate the calendar link;"},
      {"type":"text","text":"Jonah will make a seating map. Next"},
      {"type":"text","text":"check-in is Thursday, September 17."},
  ],[0,105,145,170,195,220,245])),
  [{"at":0.05,"event":"Different ask"},{"at":0.3,"event":"No Skill event"},{"at":0.7,"event":"Prose, not a list"}])

B("B05","THE SIX-CELL TALLY","SHELL",LIAM,
  "Six cells. Two descriptions, three asks each. Grep the Skill events out of every run. "
  "Vague: one, one, zero. Pushy: one, one, zero. Both descriptions score four out of four on the six-cell matrix. "
  "The pushy version's fifty-four extra words did not add a single fire. The vague version's nine words did not over-fire on the summary. This is what the loop is for.",
  "CCPlainShell — trigger-tally.txt, six cells",
  R("CCPlainShell",{"title":"zsh — ~/scratch/evidence","lines":[
      "$ grep -c '\"name\":\"Skill\"' run-*.jsonl",
      "run-pushy-a1.jsonl:1",
      "run-pushy-a2.jsonl:1",
      "run-pushy-a3.jsonl:0",
      "run-vague-a1.jsonl:1",
      "run-vague-a2.jsonl:1",
      "run-vague-a3.jsonl:0",
      "$ cat trigger-tally.txt",
      "vague  positives 2/2  negative 0/1",
      "pushy  positives 2/2  negative 0/1"],
    "startCue":12,"lineGap":22}, motion="drawon",
    leaves_terminal_because="the tally across six sessions cannot live inside any one session"),
  [{"at":0.05,"event":"Grep all runs"},{"at":0.5,"event":"1 · 1 · 0 both rows"},{"at":0.85,"event":"4-of-4 both"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: pick the ask that would test the description honestly. "
  "Step two, mine: draft two descriptions that ought to score differently — nine words versus sixty-three. "
  "Claude did the six runs; the handoff was one Skill event per positive, zero per negative. It hit that in all six. "
  "The dangerous middle: step four, my read of the tally. Two descriptions score the same. Do I write it up as a null result or reach for a story? "
  "Interpretive judgment: null result is the result. Executive integration, zero — this was one loop, honest.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"description eval · six cells","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Pick an ask that tests the description"},
      {"n":2,"phase":"F","labor":"human","capacity":"PF","text":"Draft two descriptions (9 vs 63 words)","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"claude","text":"Six runs · fresh /tmp dir each","handoff":"1 Skill event per positive; 0 per negative","dependsOn":[2]},
      {"n":4,"phase":"H","labor":"human","capacity":"PA","text":"Read the tally: 4/4 both descriptions","dependsOn":[3]},
      {"n":5,"phase":"H","labor":"human","capacity":"IJ","text":"Null result is the result","dependsOn":[4]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.55,"event":"Step 4 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must pick asks that would separate the descriptions — a paraphrase, and one adjacent negative. "
  "I must read the tally as it stands — not as I wanted it. I must call a null result a null result. "
  "Claude can run six sessions in fresh folders and stream every Skill event. It should decline the near-miss. It should not need synonyms to fire on the obvious ask.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"run six sessions in fresh folders"},{"tier":"CAN","text":"stream every Skill event as JSON"},
                          {"tier":"SHOULD","text":"decline the near-miss ask"},{"tier":"SHOULD","text":"fire without synonym padding"}],
                    "human":[{"tier":"MUST","text":"pick asks that split the two apart"},{"tier":"MUST","text":"read the tally as it stands"},
                             {"tier":"MUST","text":"call a null result a null result"},{"tier":"SHOULD","text":"draft assertions before runs land"}],
                    "closing":"The Skill Creator's gift is the loop, not the wording.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Two SKILL-dot-md files, one differing line — nine words versus sixty-three. Same folder, three asks each, six fresh sessions. "
  "The router fired on both extraction asks under both descriptions. It declined the summarize ask under both. Four out of four, both rows. "
  "The pushy version's fifty-four extra words earned nothing. The vague version's nine words did not over-fire. "
  "What would prove this reel wrong: an ask on which one description fires and the other doesn't.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Two SKILL.md files differ only in the description: 9 words vs 63.",
      "Three asks · two extractions, one summary · six fresh headless runs.",
      "Both descriptions: 2/2 on positives, 0/1 on the negative. 4/4 each.",
      "The 54 extra words earned zero extra fires. The nine did not over-fire.",
      "The gift is the loop, not the wording — you measure the description.",
      "FALSIFIABLE: an ask on which one description fires and the other doesn't."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next skill, open Claude Code and paste this: I'll give you a folder with a SKILL-dot-md and three asks — one obvious, one paraphrased, one adjacent negative. "
  "Run each ask in a fresh temp dir with only that skill installed. Count the Skill events per run. Show me the six-cell tally.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"I'll give you a folder with a SKILL.md and three asks — one obvious, one paraphrased, one adjacent negative. Run each in a fresh temp dir with only that skill installed. Count the Skill events per run. Show me the six-cell tally.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Skill Creator. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Two SKILL.md files, one differing line — nine words vs sixty-three. Six fresh runs. What actually changed.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-skills--claude-liam-skill-creator (the concept; the card body replaced by six real runs)",
    "sources":["SESSION.md (six real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print("  ⚠",b["beat_id"],len(blk["text"]),blk["text"])
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>60: print("  ⚠ shell",b["beat_id"],len(ln),ln)
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>34: print("  ⚠ ledger",len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>46: print("  ⚠ step",len(st["text"]),st["text"])
