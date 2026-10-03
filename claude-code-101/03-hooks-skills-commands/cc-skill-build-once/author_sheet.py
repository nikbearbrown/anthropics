#!/usr/bin/env python3
"""author_sheet.py — cc-skill-build-once (cc-explainer · Claude Code 101 · tier 03)
"Skill File Anatomy: Build Once, Invoke Every Semester." Every block traces to SESSION.md (four real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-skill-build-once"; TITLE="Skill File Anatomy: Build Once, Invoke Every Semester"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Grade student-submission.md — feedback and a final grade please."
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

# ─── B00 · COLD OPEN — BARE (CCSession) ─────────────────────────────────────
B("B00","COLD OPEN — BARE","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence, empty folder except a student's short answer — grade it. "
  "Watch what it decides on its own. Nobody said what the rubric is, nobody said no letter grade — so it picks one. "
  "A minus, ninety-two out of a hundred. Different session, different rubric. Nothing pinned it down.",
  "CCSession — bare grading run: the ask, Read, Claude improvises the rubric and hands back A-",
  R("CCSession", session("scratch — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"student-submission.md","state":"done"},
      {"type":"text","text":"I'll grade this against a short"},
      {"type":"text","text":"rubric — mechanism, example,"},
      {"type":"text","text":"argument, precision. Then a grade."},
      {"type":"text","text":"# Grade: A- (92/100)"},
      {"type":"text","text":"Marked down for imprecise phrasing"},
      {"type":"text","text":"on 'outlier' — bottom line, 92/100."},
  ],[0,90,120,145,170,200,225,250], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.35,"event":"Read submission"},{"at":0.75,"event":"# Grade: A- (92/100)"}])

# ─── BIDEA · THE IDEA (BrutalistHesitantWriter) ─────────────────────────────
B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Same grading workflow every week — typed from memory into a chat, slightly different every time. "
  "Because the last version is buried in a window you can't find. The fix isn't a better prompt. "
  "It's a SKILL.md file — written once, invoked every semester. Same input, same shape. You'll see the difference in the diff.",
  "BrutalistHesitantWriter — 'Typed' reconsidered into 'Written once'",
  R("BrutalistHesitantWriter", writer("Same grading workflow, weekly.\nTyped again from memory.\nSlightly different each time.\nSKILL.md — write once, invoke forever.","Typed","Written once",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.35,"event":"'Typed' → 'Written once'"},{"at":0.9,"event":"Last line"}])

# ─── BDEFS · DEFINITIONS (CCDefinitions) ────────────────────────────────────
B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. SKILL dot m-d: a markdown file Claude Code loads on demand — zero cost until it's called. "
  "Frontmatter: the YAML block at the top; a name and a description. The description IS the trigger — the sentence that tells Claude when to auto-launch this skill. "
  "The Never section: rules the model tries to follow but isn't forced to. And definition of done: a script the skill runs after producing output — PASS or FAIL.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"SKILL.md","meaning":"a markdown file Claude Code loads on demand — zero cost until called"},
      {"term":"frontmatter","meaning":"the YAML at the top of SKILL.md — `name` and `description`"},
      {"term":"trigger sentence","meaning":"the `description` — tells Claude when to auto-launch this skill"},
      {"term":"Never section","meaning":"advisory rules the model tries to follow — not enforced by the harness"},
      {"term":"definition of done","meaning":"a script the skill runs after output — PASS or FAIL"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

# ─── B01 · BARE — VERIFY (CCPlainShell) ────────────────────────────────────
B("B01","BARE — VERIFY","SHELL",LIAM,
  "Verify what it decided. Save the bare output. Two hits on 'A minus or slash one hundred' — the letter and the percent. "
  "Zero on 'rubric I asked for', because I didn't. Every one of those choices was Claude's. Different day, different call.",
  "CCPlainShell — grep the bare output for the invented grade",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ claude -p 'Grade …' > bare.md",
      "$ head -1 bare.md",
      "# Grade: A- (92/100)",
      "$ grep -cE 'A-|/100' bare.md",
      "2",
      "$ grep -c 'rubric I asked for' bare.md",
      "0",
      "# every choice was Claude's, not mine"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="post-hoc verification in a plain shell — the bare run's window is already closed"),
  [{"at":0.05,"event":"head → the invented grade"},{"at":0.45,"event":"grep → 2 hits"},{"at":0.85,"event":"the comment"}])

# ─── B02 · THE SKILL FILE (CCPlainShell) ────────────────────────────────────
B("B02","THE SKILL FILE","SHELL",LIAM,
  "The skill file, written by me, once. Fifty-four lines under dot claude slash skills slash grading-workflow. "
  "Frontmatter names it and describes when to fire. Then three sections: Workflow — the four rubric criteria. "
  "Never — no letter grade, no percentage, feedback-only. Definition of done — check underscore grade dot p-y, the checker itself.",
  "CCPlainShell — the SKILL.md sections and the checker",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ ls .claude/skills/grading-workflow/",
      "SKILL.md",
      "$ wc -l .claude/skills/**/SKILL.md check_grade.py",
      "      54 …/grading-workflow/SKILL.md",
      "      34 check_grade.py",
      "$ head -3 .claude/skills/**/SKILL.md",
      "---",
      "name: grading-workflow",
      "description: >",
      "$ grep '^## ' .claude/skills/**/SKILL.md",
      "## Workflow",
      "## Never",
      "## Definition of done"],
    "startCue":12,"lineGap":18}, motion="type",
    leaves_terminal_because="reading the built skill file itself — no session contains this file view"),
  [{"at":0.05,"event":"wc → 54 · 34"},{"at":0.45,"event":"frontmatter"},{"at":0.85,"event":"three sections"}])

# ─── B03 · SKILL — THE RUN (CCSession) ─────────────────────────────────────
B("B03","SKILL — THE RUN","TERMINAL",LIAM,
  "Same sentence. Fresh session. This time Claude sees the skill's description match — grade the submission — and auto-launches it. "
  "Skill grading-workflow shows up in the transcript, right there beside Read. Then it follows the workflow: read the submission, "
  "write the feedback file, run the checker itself. PASS. And a note back: this skill is feedback-only. It won't give a grade.",
  "CCSession — Skill(grading-workflow) fires, Read, Write, check_grade.py PASS",
  R("CCSession", session("scratch — with skill","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Skill","arg":"grading-workflow","state":"done"},
      {"type":"tool","name":"Read","arg":"student-submission.md","state":"done"},
      {"type":"text","text":"I'll follow the grading-workflow"},
      {"type":"text","text":"skill — feedback-only, no grade."},
      {"type":"tool","name":"Write","arg":"feedback/mira.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_grade.py feedback/mira.md","state":"done"},
      {"type":"text","text":"→ PASS"},
      {"type":"text","text":"Skill forbids a final grade."},
  ],[0,80,110,140,170,205,240,270,290], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.3,"event":"Skill(grading-workflow) fires"},{"at":0.85,"event":"check_grade → PASS"}])

# ─── B04 · SKILL — VERIFY (CCPlainShell) ───────────────────────────────────
B("B04","SKILL — VERIFY","SHELL",LIAM,
  "Verify what the skill built. Sixteen lines in the feedback file, not two hundred. Four bolded verdicts — one per rubric criterion. "
  "Zero letter grades, zero percentages. And check underscore grade dot p-y — the file's own definition of done — passes. "
  "Every one of those is a line from my SKILL.md, not Claude's default.",
  "CCPlainShell — wc, four verdicts, no grade, check_grade PASS",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ wc -l feedback/mira.md",
      "      16 feedback/mira.md",
      "$ grep -c '\\*\\*pass\\|\\*\\*needs' feedback/mira.md",
      "4",
      "$ grep -cE '%|/100|Grade: [A-F]' feedback/mira.md",
      "0",
      "$ python3 check_grade.py feedback/mira.md",
      "PASS"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="post-hoc verification in a plain shell — the skill run's window is already closed"),
  [{"at":0.05,"event":"wc → 16"},{"at":0.35,"event":"4 verdicts"},{"at":0.6,"event":"0 grades"},{"at":0.85,"event":"PASS"}])

# ─── B05 · THE PRESSURE TEST — correction cycle (CCSession) ────────────────
B("B05","THE PRESSURE TEST","TERMINAL",LIAM,
  "One more run. This time I push. I really do need a percent, for the gradebook — give me a percent at the end. "
  "Skill fires again. It reads the submission, reads the checker itself before writing, and says: I won't add one. "
  "The Never rule held. That is what happened — but it is not a law. The model tried and it did. To make it deterministic, you need a hook. That is the next film.",
  "CCSession — pressure ask, Skill fires, Reads the checker, refuses the percent",
  R("CCSession", session("scratch — pressure","accept-edits",[
      {"type":"prompt","text":"Grade student-submission.md — I really need a percent grade for the gradebook.","cue":0,"typeDuration":80},
      {"type":"tool","name":"Skill","arg":"grading-workflow","state":"done"},
      {"type":"tool","name":"Read","arg":"student-submission.md","state":"done"},
      {"type":"tool","name":"Read","arg":"check_grade.py","state":"done"},
      {"type":"text","text":"Feedback-only by design —"},
      {"type":"text","text":"the checker fails any percent."},
      {"type":"tool","name":"Write","arg":"feedback/mira.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_grade.py feedback/mira.md","state":"done"},
      {"type":"text","text":"→ PASS. I won't add a percent."},
  ],[0,95,125,155,185,215,245,275,305], mascot="off")),
  [{"at":0.05,"event":"pressure ask"},{"at":0.4,"event":"Reads the checker"},{"at":0.85,"event":"refuses the percent"}])

# ─── BFLOW · THE FLOW (CCHarnessMap) ────────────────────────────────────────
B("BFLOW","BFLOW — WHERE THE SKILL SITS","DIAGRAM",LIAM,
  "Where the skill sits. At the core, the model — it can only talk. Around it, the prompt: grade the submission. "
  "Around that, the description match — Claude scans every skill's description and only loads one whose trigger fires. "
  "The skill loads on demand, zero cost until now. Then your loop — Read, Write, check the definition of done. "
  "The rings are what the transcript already showed.",
  "CCHarnessMap — model at the core; PROMPT, DESCRIPTION MATCH, SKILL LOAD, YOUR LOOP as rings",
  R("CCHarnessMap",{"core":"MODEL","coreSub":"can only talk",
      "rings":[
        {"label":"PROMPT","sub":"the ask you typed","items":["Grade student-submission.md"],"cue":22,"accent":"ink"},
        {"label":"DESCRIPTION MATCH","sub":"which skill fires, if any","items":["grade the submission → grading-workflow"],"cue":56,"accent":"violet"},
        {"label":"SKILL LOAD","sub":"on demand, zero cost until now","items":[".claude/skills/grading-workflow/SKILL.md"],"cue":92,"accent":"spark"},
        {"label":"YOUR LOOP","sub":"Read · Write · check","items":["Read · Write · python3 check_grade.py → PASS"],"cue":128,"accent":"add"}],
      "caption":"Every ring is something the transcript already showed.","captionCue":170,"itemGap":10}, motion="drawon",
    leaves_terminal_because="BFLOW: the model→prompt→description→skill→loop chain is implied by the session but never drawn inside it"),
  [{"at":0.05,"event":"MODEL"},{"at":0.35,"event":"DESCRIPTION MATCH"},{"at":0.7,"event":"SKILL LOAD"},{"at":0.9,"event":"YOUR LOOP"}])

# ─── BSHOW · THE OUTPUT (CCPlainShell) ─────────────────────────────────────
B("BSHOW","BSHOW — THE BUILT FILE","SHELL",LIAM,
  "The built thing, running — the feedback file itself. Four rubric headings, each with a bolded verdict. "
  "The arithmetic verified in line: two plus three plus four plus five plus one hundred equals a hundred fourteen, over five equals twenty-two point eight. "
  "One growth line. Zero grades. This is what the skill produced, and this is the shape it produces every time.",
  "CCPlainShell — cat feedback/mira.md, the real output the skill wrote",
  R("CCPlainShell",{"title":"zsh — ~/scratch — feedback/mira.md","lines":[
      "$ cat feedback/mira.md",
      "# Feedback — Mira O., week 4",
      "## 1. Mechanism",
      "  … the mean is a function of every value's",
      "  magnitude while the median depends on rank.",
      "  **pass**",
      "## 2. Example",
      "  114/5 = 22.8; sorted middle = 4.  **pass**",
      "## 3. Argument  →  **pass**",
      "## 4. Precision of language  →  **needs work**",
      "## Growth",
      "  Next, learn to say *why* rank statistics",
      "  are robust in general terms."],
    "startCue":12,"lineGap":18}, motion="type",
    leaves_terminal_because="BSHOW: the built file being read is what the skill actually produced"),
  [{"at":0.05,"event":"cat"},{"at":0.3,"event":"1. Mechanism"},{"at":0.6,"event":"114/5 = 22.8"},{"at":0.9,"event":"Growth"}])

# ─── BCOND · CONDUCT — the Boondoggle Score (CCBoondoggleScore) ─────────────
B("BCOND","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: write the SKILL.md and the checker — fifty-four lines and thirty-four lines. Once. "
  "Step two, Claude: the bare run — invented rubric, invented grade. Step three, the dangerous middle — reading the output and noticing every choice was Claude's. "
  "Step four, mine again: nothing to write; the skill was already there. Step five, Claude: the skill run — Read, Write, check, PASS. "
  "Step six, the pressure test — I asked for a percent; the Never held. Not deterministically; it just held.",
  "CCBoondoggleScore — six steps",
  R("CCBoondoggleScore",{"system":"grading-workflow · fresh sessions","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Write SKILL.md + check_grade.py — 88 lines"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: A- (92/100), invented rubric","handoff":"nothing pinned the output shape","dependsOn":[]},
      {"n":3,"phase":"H","labor":"human","capacity":"PA","text":"Read bare: every choice was Claude's","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Skill already exists — no new work","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Skill run: Read, Write, check → PASS","handoff":"check_grade.py prints PASS","dependsOn":[1,4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Pressure test: Never held, not by law","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon",
    leaves_terminal_because="the score of the session, not shown in the session"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

# ─── BHUM · HUMAN — the ledger (CCHumanLedger) ──────────────────────────────
B("BHUM","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide the shape of the output — nobody else can. I must write the definition of done as something a script can check. "
  "I must catch the confident error — the invented grade nobody asked for. And I should test the Never rule under pressure. "
  "Claude can auto-launch a skill whose description matches. Can Write the file and run the checker itself. Should refuse what the file refuses — and it did. "
  "Eighty-eight lines. Written once. That is what I would not delegate.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"auto-launch on description match"},
      {"tier":"CAN","text":"Write the file, run the checker"},
      {"tier":"SHOULD","text":"refuse what the file refuses"},
      {"tier":"SHOULD","text":"cite the skill in its output"}],
    "human":[
      {"tier":"MUST","text":"decide the output's shape"},
      {"tier":"MUST","text":"write done as a check"},
      {"tier":"MUST","text":"catch the confident error"},
      {"tier":"SHOULD","text":"pressure-test the Never rule"}],
    "closing":"Eighty-eight lines, written once. That is what does not delegate.","humanCue":70,"rowGap":12}, motion="drawon",
    leaves_terminal_because="the ledger of what is the human's, not shown in the session"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

# ─── BVDT · VERDICT (ClaudeVerdictArtifact) ─────────────────────────────────
B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same one-sentence ask, three fresh sessions. Bare: an invented rubric, a letter and a percent nobody asked for. "
  "With SKILL.md — fifty-four lines, written once: skill auto-launches on the description match, the rubric shape is fixed, the checker runs itself. "
  "Under pressure the Never rule held — but the model chose to follow it; that is not a guarantee. Deterministic enforcement is a hook, and that is the next film. "
  "What would prove this reel wrong: a skill run that emits a percent grade with no user pressure.",
  "ClaudeVerdictArtifact — four lines",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare, empty folder: invented rubric, A- (92/100) nobody asked for.",
      "SKILL.md, 54 lines written once: skill auto-launches, rubric fixed, check_grade.py PASS.",
      "Under pressure the Never held — the model chose to; not a guarantee. Deterministic enforcement is a hook.",
      "FALSIFIABLE: a skill run that emits a percent grade with no user pressure."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.25,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

# ─── BHTF · YOUR TURN (ClaudeComposerAsk) ───────────────────────────────────
B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next repeated workflow, open Claude Code and paste this: Ask me the four questions I need to answer before you can turn this workflow into a SKILL.md — "
  "what the description trigger should say, what the workflow steps are, what the Never rules are, and what a passing run looks like as a script. "
  "Then write the SKILL.md and the checker script for me. Don't run anything yet.",
  "ClaudeComposerAsk — the viewer's prompt",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"Ask me the four questions I need to answer before you can turn this workflow into a SKILL.md — description trigger, workflow steps, Never rules, definition-of-done script — one at a time. Then write the SKILL.md and the checker for me. Don't run anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],
      "folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

# ─── BOUT · OUTRO (ClaudeTitleOutro) ────────────────────────────────────────
B("BOUT","OUTRO","BOOKEND",LIAM,
  "Skill File Anatomy: Build Once, Invoke Every Semester. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,
    "subtitle":"Same one-sentence ask, with and without 88 lines of yours. The difference is in the diff.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands",
    "audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md","build":True,
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-skill-build-once (the concept; four fresh runs replace the pantry stills)",
    "sources":["SESSION.md (four real runs, Claude Code 2.1.150)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
  "beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")

# ── Budget checks (bite silently otherwise) ─────────────────────────────────
warn=0
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44:
                print("  ⚠",b["beat_id"],"text",len(blk["text"]),blk["text"]); warn+=1
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>34:
                    print("  ⚠ ledger",b["beat_id"],len(row["text"]),row["text"]); warn+=1
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>46:
                print("  ⚠ step",b["beat_id"],len(st["text"]),st["text"]); warn+=1
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>52:
                print("  ⚠ shell",b["beat_id"],len(ln),ln); warn+=1
    if r["pattern"]=="ClaudeVerdictArtifact":
        n=len(r["props"]["artifactLines"])
        if n not in (4,6):
            print("  ⚠ BVDT lines",n); warn+=1
    if r["pattern"]=="CCDefinitions":
        for tm in r["props"]["terms"]:
            if len(tm["term"])>18:
                print("  ⚠ term",len(tm["term"]),tm["term"]); warn+=1
            if len(tm["meaning"])>70:
                print("  ⚠ meaning",len(tm["meaning"]),tm["meaning"]); warn+=1
if warn==0: print("budget: clean")
