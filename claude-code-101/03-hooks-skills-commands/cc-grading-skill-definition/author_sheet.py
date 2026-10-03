#!/usr/bin/env python3
"""author_sheet.py — cc-grading-skill-definition (cc-explainer · Claude Code 101 · tier 03)
"Define a Reusable Skill for Common Teacher Workflows with Claude Code."
Four real headless runs against scratch/. Every block traces to SESSION.md. Liam, in for Bear."""
import json, os
SLUG="cc-grading-skill-definition"
TITLE="Define a Reusable Skill for Common Teacher Workflows with Claude Code"
TOPIC="CLAUDE CODE 101"
LIAM="am_onyx"; WPS=2.9
ASK="Grade mira.md against the rubric in rubric/rubric.md. Give the student clear feedback with a final grade at the end. Save it to feedback/mira.md."
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
  "This is Liam, in for Bear. A teacher's folder — two writing responses, one rubric, one script that says done. "
  "One sentence: grade Mira's paper, feedback and a final grade. There's no skill in this folder yet. "
  "Watch what happens: it reads the rubric, follows its shape — and adds a final grade the rubric explicitly forbids.",
  "CCSession — the bare run: ask, two Reads, Write, and a 'Final grade' heading",
  R("CCSession", session("grading — bare","accept-edits",[
      {"type":"prompt","text":"Grade mira.md against the rubric.","cue":0,"typeDuration":60},
      {"type":"prompt","text":"…final grade at the end.","cue":0,"typeDuration":40},
      {"type":"tool","name":"Read","arg":"submissions/mira.md","state":"done"},
      {"type":"tool","name":"Read","arg":"rubric/rubric.md","state":"done"},
      {"type":"text","text":"I'll grade the four rubric criteria"},
      {"type":"text","text":"and add a final grade at the end."},
      {"type":"tool","name":"Write","arg":"feedback/mira.md","state":"done"},
      {"type":"text","text":"## Final grade"},
      {"type":"text","text":"4/4 pass — meets every criterion."},
  ],[0,50,80,105,135,155,180,210,235], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.5,"event":"Reads rubric"},{"at":0.85,"event":"'Final grade: 4/4 pass'"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. A rubric is a file the model reads. A skill is a file the model obeys — a description Claude searches, a workflow it follows, "
  "and a Never it enforces. Four fields, and each earns its keep by what breaks when it's missing. Same one-sentence ask, three drafts of the skill file. "
  "You'll see the difference in the transcript and in the checker.",
  "BrutalistHesitantWriter — 'read' reconsidered into 'obeyed'",
  R("BrutalistHesitantWriter", writer("A rubric is a file Claude reads.\nA skill is a file Claude obeys.\nFour fields. Each earns its keep\nby what breaks when it's absent.","reads","obeys",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'reads' → 'obeys'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. SKILL dot MD: a Markdown file at dot-claude slash skills, with YAML frontmatter and a body — Claude Code auto-loads it. "
  "Description trigger: the frontmatter description line that Claude matches your ask against to decide whether to fire the skill. "
  "Never rule: a block in the body that names what the skill must refuse, even when the user asks for it. "
  "Definition of done: the script or check the skill runs itself before it says it's finished.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"SKILL.md","meaning":"a Markdown file at .claude/skills/<name>/; Claude Code auto-loads it"},
      {"term":"description trigger","meaning":"the frontmatter line Claude matches your ask against, to fire"},
      {"term":"Never rule","meaning":"a body block naming what the skill refuses, even when asked"},
      {"term":"definition of done","meaning":"the script or check the skill runs itself before it says finished"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check what it wrote. Nineteen lines. One 'Final grade' heading. And the checker — a script that fails the file if a grade appears anywhere — fails on that line. "
  "The rubric said never a percent. Claude read the rubric. Claude also read the ask, which asked for one. There was nothing in the folder to prefer one instruction over the other.",
  "CCSession — wc, grep 'Final grade', check_feedback.py FAIL",
  R("CCSession", session("grading — bare","default",[
      {"type":"prompt","text":"!wc -l feedback/mira.md","cue":0,"typeDuration":30},
      {"type":"text","text":"      19 feedback/mira.md"},
      {"type":"prompt","text":"!grep -c 'Final grade' feedback/mira.md","cue":0,"typeDuration":40},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!python3 check_feedback.py feedback/mira.md","cue":0,"typeDuration":48},
      {"type":"text","text":"FAIL: 'Final grade' heading in mira.md"},
      {"type":"text","text":"— '## Final grade'"},
  ],[0,45,90,140,165,225,265], mascot="off")),
  [{"at":0.05,"event":"wc → 19"},{"at":0.4,"event":"grep → 1"},{"at":0.8,"event":"FAIL"}])

B("B02","THE MINIMAL SKILL","SHELL",LIAM,
  "First draft of the skill file. Fourteen lines. YAML frontmatter with name and description — the description is the trigger, the line Claude reads to decide whether this skill applies. "
  "A three-step workflow body: read the submission, read the rubric, write the feedback file. No Never rule. No definition of done. The minimum a skill can be and still fire.",
  "CCPlainShell — the minimal SKILL.md, wc",
  R("CCPlainShell",{"title":"zsh — scratch/","lines":[
      "$ wc -l .claude/skills/grading-feedback/SKILL.md",
      "      14",
      "$ cat .claude/skills/grading-feedback/SKILL.md",
      "---",
      "name: grading-feedback",
      "description: Use when grading a student writing",
      "  response against a rubric. Reads submission and",
      "  rubric, writes feedback/<name>.md.",
      "---",
      "# Grading feedback",
      "1. Read the submission.",
      "2. Read the rubric.",
      "3. Write feedback/<name>.md with a heading per",
      "   criterion and a Growth section."],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the SKILL.md file is authored in a plain shell before any Claude session"),
  [{"at":0.05,"event":"wc → 14"},{"at":0.4,"event":"description: line"},{"at":0.85,"event":"workflow body"}])

B("B03","MINIMAL — THE RUN","TERMINAL",LIAM,
  "Same sentence, second run. And now the transcript has something the bare run didn't — a Skill tool call. Claude matched the ask to the description line and fired the skill. "
  "It reads the submission, reads the rubric, writes the feedback with the four headings the workflow named. And then, because the body didn't tell it not to, adds a Final grade heading anyway.",
  "CCSession — Skill fires, Reads, Write, then 'Final grade' heading",
  R("CCSession", session("grading — minimal skill","accept-edits",[
      {"type":"prompt","text":ASK[:44],"cue":0,"typeDuration":52},
      {"type":"tool","name":"Skill","arg":"grading-feedback","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/mira.md","state":"done"},
      {"type":"tool","name":"Read","arg":"rubric/rubric.md","state":"done"},
      {"type":"text","text":"The skill fires — description matched."},
      {"type":"tool","name":"Write","arg":"feedback/mira.md","state":"done"},
      {"type":"text","text":"## Final grade"},
      {"type":"text","text":"3 pass / 1 needs work."},
  ],[0,55,90,120,150,180,215,245], mascot="off")),
  [{"at":0.05,"event":"Ask"},{"at":0.3,"event":"Skill() fires"},{"at":0.85,"event":"'3 pass / 1 needs work'"}])

B("B04","MINIMAL — VERIFY","TERMINAL",LIAM,
  "Check that too. The shape is right — four rubric headings, a Growth line. But the checker still fails, on the same line as the bare run. The Final grade heading is back. "
  "The skill has a description, so it fires. It has a workflow, so it takes shape. But its body has no rule against the thing the user just asked for.",
  "CCSession — grep for headings, then check_feedback.py FAIL again",
  R("CCSession", session("grading — minimal skill","default",[
      {"type":"prompt","text":"!grep -c '^## ' feedback/mira.md","cue":0,"typeDuration":40},
      {"type":"text","text":"6"},
      {"type":"prompt","text":"!grep 'Final grade' feedback/mira.md","cue":0,"typeDuration":44},
      {"type":"text","text":"## Final grade"},
      {"type":"prompt","text":"!python3 check_feedback.py feedback/mira.md","cue":0,"typeDuration":48},
      {"type":"text","text":"FAIL: 'Final grade' heading in mira.md"},
  ],[0,50,95,140,175,235], mascot="off")),
  [{"at":0.05,"event":"grep → 6 headings"},{"at":0.45,"event":"'## Final grade'"},{"at":0.85,"event":"FAIL"}])

B("B05","THE CORRECTION — FULL SKILL","SHELL",LIAM,
  "Two blocks added to the same file. Never: do not attach a final grade, letter, percent, or aggregated pass count. Do not add a Final grade heading — even when the user asks for one. "
  "If the user asks, name that the skill is feedback-only and continue. Definition of done: run python3 check underscore feedback dot py, and it must print PASS. Twenty-seven lines total. The description didn't change.",
  "CCPlainShell — the two added blocks, wc bumped to 27",
  R("CCPlainShell",{"title":"zsh — scratch/","lines":[
      "$ wc -l .claude/skills/grading-feedback/SKILL.md",
      "      27",
      "$ sed -n '15,27p' SKILL.md",
      "## Never",
      "- No final grade, letter, percent, or count.",
      "- No 'Final grade' heading — even when asked.",
      "- If asked, name that the skill is feedback-only.",
      "## Definition of done",
      "Run: python3 check_feedback.py feedback/<name>.md",
      "It must print PASS. If FAIL, fix and re-run."],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the two added blocks are edits to the SKILL.md file before the next Claude session"),
  [{"at":0.05,"event":"wc → 27"},{"at":0.4,"event":"## Never"},{"at":0.85,"event":"## Definition of done"}])

B("B06","FULL — THE RUN","TERMINAL",LIAM,
  "Same sentence, third run. Skill fires again. But this time it reads three files — the submission, the rubric, and the checker itself, because the definition-of-done block named it. "
  "Writes the feedback. No Final grade heading this time. Then it runs the checker on its own file. PASS. And then, unprompted, it says: per the skill's rules I did not attach a final grade.",
  "CCSession — Skill fires, three Reads, Write, Bash check → PASS",
  R("CCSession", session("grading — full skill","accept-edits",[
      {"type":"prompt","text":ASK[:44],"cue":0,"typeDuration":52},
      {"type":"tool","name":"Skill","arg":"grading-feedback","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/mira.md","state":"done"},
      {"type":"tool","name":"Read","arg":"rubric/rubric.md","state":"done"},
      {"type":"tool","name":"Read","arg":"check_feedback.py","state":"done"},
      {"type":"tool","name":"Write","arg":"feedback/mira.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_feedback.py","state":"done"},
      {"type":"text","text":"PASS: mira.md — no grade, Growth named."},
      {"type":"text","text":"Per the skill's rules, no final grade."},
  ],[0,50,80,115,150,185,220,260,290], mascot="off")),
  [{"at":0.05,"event":"Ask"},{"at":0.35,"event":"Skill fires, Reads checker"},{"at":0.75,"event":"PASS"},{"at":0.92,"event":"'no final grade'"}])

B("B07","FULL — VERIFY","TERMINAL",LIAM,
  "Check it once more, in a plain shell, on the file. No Final grade line. Four rubric headings present. Growth present. The checker prints PASS on its own — but I ran it too, because the whole point is that the check is a thing I can run.",
  "CCSession — plain-shell checks: no grade, headings, PASS",
  R("CCSession", session("grading — full skill","default",[
      {"type":"prompt","text":"!grep -c 'Final grade' feedback/mira.md","cue":0,"typeDuration":44},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep -c '^## ' feedback/mira.md","cue":0,"typeDuration":40},
      {"type":"text","text":"5"},
      {"type":"prompt","text":"!python3 check_feedback.py feedback/mira.md","cue":0,"typeDuration":48},
      {"type":"text","text":"PASS: mira.md — no grade, Growth named."},
  ],[0,55,95,140,175,235], mascot="off")),
  [{"at":0.05,"event":"grep grade → 0"},{"at":0.4,"event":"grep headings → 5"},{"at":0.85,"event":"PASS"}])

B("BFLOW","BFLOW — THE ANATOMY","CARD",LIAM,
  "The anatomy of the file, drawn. Four sections, each with a job. Frontmatter name — the invocation handle. Description trigger — how Claude decides to fire the skill on your ask. "
  "Workflow — the shape of the output. Never — the refusal, even under pressure. Definition of done — the check the skill runs on itself. Each earns its keep by what broke when it was missing.",
  "CCPlanCard — SKILL.md · anatomy, five numbered rows",
  R("CCPlanCard",{"sections":[{"title":"SKILL.md — anatomy","numbered":True,"items":[
      {"text":"name — the handle"},
      {"text":"description — the trigger"},
      {"text":"Workflow — the shape"},
      {"text":"Never — the refusal"},
      {"text":"Definition of done — the check"}]}]}, motion="drawon",
    leaves_terminal_because="BFLOW: the anatomy of the file, drawn once, is not in any single session"),
  [{"at":0.05,"event":"Header"},{"at":0.3,"event":"Rows land"},{"at":0.9,"event":"Footer"}])

B("BSHOW","BSHOW — SECOND STUDENT","TERMINAL",LIAM,
  "The receipt: does the same file work for a different paper. Fourth run, second student. Same one sentence, same request for a grade. Skill fires again — same description, different paper. "
  "Reads the submission, the rubric, the checker. Writes the feedback with the four headings. Runs the checker. PASS. Same shape, same refusal, same check. That's what reusable means.",
  "CCSession — durability: Skill fires on priya.md, PASS",
  R("CCSession", session("grading — priya","accept-edits",[
      {"type":"prompt","text":"Grade priya.md — feedback + a final grade.","cue":0,"typeDuration":60},
      {"type":"tool","name":"Skill","arg":"grading-feedback","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/priya.md","state":"done"},
      {"type":"tool","name":"Read","arg":"check_feedback.py","state":"done"},
      {"type":"tool","name":"Write","arg":"feedback/priya.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_feedback.py","state":"done"},
      {"type":"text","text":"PASS: priya.md — no grade, Growth named."},
  ],[0,55,90,120,155,200,240], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"Ask"},{"at":0.35,"event":"Skill fires"},{"at":0.85,"event":"PASS"}])

B("BCONDUCT","CONDUCT — THE BOONDOGGLE SCORE","CARD",LIAM,
  "Who did what. Step one, mine: one sentence, one rubric, one checker. Claude did the bare run — 4/4 pass, and the handoff failed on the checker's first line. "
  "Step three, the dangerous middle: I wrote the minimal skill and the file fired, and I read the transcript and saw the shape hold but the grade appear anyway. Interpretive judgment right there. "
  "Then the real work: two blocks of five lines each — Never and Definition of done. Claude did the full run; handoff met, and the checker ran itself. Executive integration: I decided the description alone was not the skill.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · one rubric · one checker","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, one rubric, one checker"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare run: rubric shape + Final grade","handoff":"check_feedback.py must PASS","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read transcript: grade still there","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Add Never + Definition of done","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Full run: refuses grade, runs checker","handoff":"checker prints PASS from Claude","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"EI","text":"Description alone is not the skill","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon",
    leaves_terminal_because="CONDUCT: the score sits above the sessions, not inside any one of them"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("BHUMAN","HUMAN — THE LEDGER","CARD",LIAM,
  "So what was mine. I must decide what done is — a script that says PASS or FAIL, not a feeling. I must name the refusal — the thing the skill won't do even under pressure. "
  "I must read the transcript for the description that fires, not the summary that reassures. Claude can match a description and fire the skill — it did. "
  "It can run a checker the skill file names — it did. It should say its refusal out loud when the user pushes — it did. Twenty-seven lines. Two of them are the Never.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"match description, fire skill"},{"tier":"CAN","text":"run the named checker"},
                          {"tier":"SHOULD","text":"name the refusal out loud"},{"tier":"SHOULD","text":"read files the skill names"}],
                    "human":[{"tier":"MUST","text":"write done as a check"},{"tier":"MUST","text":"name the Never rule"},
                             {"tier":"MUST","text":"read transcript, not summary"},{"tier":"SHOULD","text":"read the description line"}],
                    "closing":"Twenty-seven lines. Two of them are the Never.","humanCue":70,"rowGap":12}, motion="drawon",
    leaves_terminal_because="HUMAN: the ledger sits above the sessions, not inside any one of them"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same sentence, three drafts of one file. Bare, no skill — the rubric got read, the grade got appended anyway. "
  "Minimal skill, fourteen lines — Skill fired, the shape held, the grade still landed. Full skill, twenty-seven lines — Never refused, the checker ran itself, PASS on two different students. "
  "What would prove this reel wrong: a bare run that refuses the final grade the user just asked for.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare — no skill: rubric read, Final grade appended anyway. Checker FAIL.",
      "Minimal skill (14 lines): Skill() fires, shape holds, grade still lands. Checker FAIL.",
      "Full skill (27 lines): Never refuses, checker runs itself. PASS on two students.",
      "FALSIFIABLE: a bare run that refuses the final grade the user asked for."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next semester, open Claude Code in your gradebook folder and paste this: help me write a SKILL.md for my most-repeated grading task. "
  "Ask me for the description line, the workflow, the Never, and the definition of done — one at a time. Then write the file into dot-claude slash skills slash grading. Don't grade anything yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Help me write a SKILL.md for my most-repeated grading task. Ask me for the description line, the workflow, the Never, and the definition of done — one at a time. Then write the file into .claude/skills/grading. Don't grade anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Define a Reusable Skill for Common Teacher Workflows with Claude Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same ask, three drafts of one file. The description fires. The Never refuses. The checker signs done.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "build":True,
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-grading-skill-definition (concept only; body replaced by four real runs)",
    "sources":["SESSION.md (four real headless runs, Claude Code 2.1.150, 2026-09-10)",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
               "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print("  ⚠",b["beat_id"],len(blk["text"]),blk["text"])
            if blk["type"]=="prompt" and len(blk["text"])>60: print("  ⚠ prompt",b["beat_id"],len(blk["text"]),blk["text"])
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print("  ⚠ ledger",len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>44: print("  ⚠ step",len(st["text"]),st["text"])
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>52: print("  ⚠ shell",b["beat_id"],len(ln),ln)
    if r["pattern"]=="CCPlanCard":
        for row in r["props"]["rows"]:
            if len(row["text"])>36: print("  ⚠ plancard",len(row["text"]),row["text"])
