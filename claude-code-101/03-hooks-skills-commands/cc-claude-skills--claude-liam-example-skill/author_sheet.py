#!/usr/bin/env python3
"""author_sheet.py — cc-claude-skills--claude-liam-example-skill (cc-explainer · Claude Code 101 · tier 03)
"The Template Under Every Skill." Every block traces to SESSION.md (three real headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-claude-skills--claude-liam-example-skill"; TITLE="The Template Under Every Skill"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Peek at sales.csv and write the result to peek.md."
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

B("B00","COLD OPEN — THE TEMPLATE","TERMINAL",LIAM,
  "This is Liam, in for Bear. On my screen: the reference template every Claude Code skill starts from. "
  "Eighty-four lines of guidance about skills — but the parser only requires two frontmatter fields, and the description does the work. "
  "One sentence, three shapes, one honest question: what does copying this template actually buy you.",
  "CCSession — reading the reference example-skill/SKILL.md",
  R("CCSession", session("~/example-plugin — reading the template","default",[
      {"type":"prompt","text":"!head -6 skills/example-skill/SKILL.md","cue":0,"typeDuration":50},
      {"type":"text","text":"---"},
      {"type":"text","text":"name: example-skill"},
      {"type":"text","text":"description: This skill should be"},
      {"type":"text","text":"used when the user asks to"},
      {"type":"text","text":"\"demonstrate skills\", \"show skill"},
      {"type":"text","text":"format\", \"create a skill template\"…"},
      {"type":"text","text":"version: 1.0.0"},
      {"type":"text","text":"---"},
  ],[0,60,80,110,140,170,200,225,250], mascot="off")),
  [{"at":0.05,"event":"head -6"},{"at":0.35,"event":"description = trigger"},{"at":0.9,"event":"---"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Claude Code's reference template is eighty-four lines that teach one thing — the description is the trigger. "
  "That's true. It also implies everything else is decoration. That's not quite true. "
  "Same ask, same folder, in three shapes: no skill, the full template, and the template gutted to its frontmatter. You'll see where the description ends and the body begins.",
  "BrutalistHesitantWriter — 'decoration' reconsidered into 'the shape'",
  R("BrutalistHesitantWriter", writer("The description is the trigger.\nEverything else looks like decoration.\nSame ask. Two runs. Two different shapes.\nThe body is where two runs match.","decoration","the shape",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.3,"event":"'decoration' → 'the shape'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Skill: a folder Claude opens on its own, based on what you ask. "
  "Frontmatter: the fenced block at the top of a markdown file — key colon value pairs, four fields the template names. "
  "Description: the trigger — the sentence that tells Claude when the skill should fire. "
  "Definition of done: a check you can run — here, a script that reads the output file and prints pass or fail.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"skill","meaning":"a folder Claude opens on its own, based on what you ask"},
      {"term":"frontmatter","meaning":"the fenced block at the top — key: value pairs; four fields"},
      {"term":"description","meaning":"the trigger — tells Claude when this skill should fire"},
      {"term":"definition of done","meaning":"a check you can run; a script that prints PASS or FAIL"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — NO SKILL","TERMINAL",LIAM,
  "First run. No skill folder in this scratch. One sentence: peek at sales.csv and write the result to peek.md. "
  "Read the file, count the lines, write a shape it picked itself — a title, a bullet block, a first-rows table, a last-rows table, quick notes. "
  "Nice page. Not the same page anyone else would get.",
  "CCSession — Run A: ad-hoc shape, no Skill() call",
  R("CCSession", session("~/scratch — bare (no .claude/skills/)","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Bash","arg":"ls","state":"done"},
      {"type":"tool","name":"Read","arg":"sales.csv","state":"done"},
      {"type":"tool","name":"Bash","arg":"wc -l sales.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"peek.md","state":"done"},
      {"type":"text","text":"Wrote peek.md — 6 columns,"},
      {"type":"text","text":"9 data rows, head and tail"},
      {"type":"text","text":"samples, and a few notes."},
  ],[0,70,95,120,145,175,195,215], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.4,"event":"Read + Write"},{"at":0.85,"event":"Claude's chosen shape"}])

B("B02","BARE — VERIFY","TERMINAL",LIAM,
  "Check what it wrote. Twenty-eight lines. Grep for the four headings my checker expects — nothing. Run the checker: fail. "
  "Not because Claude did poorly. Because nobody told it what shape to use, so it used the internet's average.",
  "CCSession — wc, grep for the four headings, check_peek.py FAIL",
  R("CCSession", session("~/scratch — bare","default",[
      {"type":"prompt","text":"!wc -l peek.md","cue":0,"typeDuration":28},
      {"type":"text","text":"      28 peek.md"},
      {"type":"prompt","text":"!grep -c '^## FILE:' peek.md","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!python3 check_peek.py peek.md","cue":0,"typeDuration":45},
      {"type":"text","text":"FAIL: heading order [] !="},
      {"type":"text","text":"['FILE', 'ROWS', 'COLUMNS', 'HEAD']"},
  ],[0,40,75,120,150,200,225], mascot="off")),
  [{"at":0.05,"event":"wc → 28"},{"at":0.35,"event":"grep → 0"},{"at":0.8,"event":"check_peek → FAIL"}])

B("B03","THE FULL TEMPLATE","SHELL",LIAM,
  "So I write a skill for it. Copy the template's description pattern verbatim — specific phrases, keywords, topic area. "
  "Then a body: the four headings — file, rows, columns, head — with three rows in HEAD. And a check script as the definition of done. Forty lines. "
  "The description tells Claude when to fire. The body tells Claude what to write.",
  "CCPlainShell — wc + head of the full csv-peek/SKILL.md",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ wc -l .claude/skills/csv-peek/SKILL.md",
      "      40 .claude/skills/csv-peek/SKILL.md",
      "$ head -4 .claude/skills/csv-peek/SKILL.md",
      "---",
      "name: csv-peek",
      "description: This skill should be used",
      "when the user asks to \"peek at a CSV\"…",
      "$ grep -c '^## ' .claude/skills/csv-peek/SKILL.md",
      "6"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the skill file itself, read in a plain shell before any session; no session contains this"),
  [{"at":0.05,"event":"wc → 40"},{"at":0.4,"event":"the pattern, copied"},{"at":0.85,"event":"6 body sections"}])

B("B04","FULL — THE RUN","TERMINAL",LIAM,
  "Same one sentence. This time the router matches peek-at-a-CSV in the ask against peek-at-a-CSV in the description, and fires the skill on its own. "
  "It reads sales.csv, writes peek.md in the exact four-heading shape — file, rows, columns, head with three rows — then runs the definition of done because the body told it to. Pass.",
  "CCSession — Run B: Skill(csv-peek), Write, check_peek.py PASS",
  R("CCSession", session("~/scratch — full skill","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Skill","arg":"csv-peek","state":"done"},
      {"type":"tool","name":"Read","arg":"sales.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"peek.md","state":"done"},
      {"type":"text","text":"## FILE: sales.csv"},
      {"type":"text","text":"## ROWS: 9"},
      {"type":"text","text":"## COLUMNS: rep, region, quarter…"},
      {"type":"text","text":"## HEAD:"},
      {"type":"tool","name":"Bash","arg":"python3 check_peek.py peek.md","state":"done"},
      {"type":"text","text":"PASS"},
  ],[0,70,95,120,150,175,200,225,250,280], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.25,"event":"Skill(csv-peek) fires"},{"at":0.9,"event":"PASS"}])

B("B05","BARE FRONTMATTER — GUT THE BODY","TERMINAL",LIAM,
  "One more shape. Same folder — I delete the body of SKILL.md. Four lines left: the fence, the name, the description, the fence. "
  "The parser is fine with this. The template says version and license are optional. The three-mode text, the file-structure block, the good-practices list — all of it is prose. Same ask.",
  "CCSession — cat the 4-line SKILL.md",
  R("CCSession", session("~/scratch — bare frontmatter","default",[
      {"type":"prompt","text":"!wc -l .claude/skills/csv-peek/SKILL.md","cue":0,"typeDuration":55},
      {"type":"text","text":"       4"},
      {"type":"prompt","text":"!cat .claude/skills/csv-peek/SKILL.md","cue":0,"typeDuration":50},
      {"type":"text","text":"---"},
      {"type":"text","text":"name: csv-peek"},
      {"type":"text","text":"description: This skill should be"},
      {"type":"text","text":"used when the user asks to \"peek"},
      {"type":"text","text":"at a CSV\", \"inspect columns\"…"},
      {"type":"text","text":"---"},
  ],[0,55,85,120,140,160,185,210,230], mascot="off")),
  [{"at":0.05,"event":"wc → 4"},{"at":0.5,"event":"cat"},{"at":0.9,"event":"just frontmatter"}])

B("B06","BARE FRONT — THE RUN","TERMINAL",LIAM,
  "Router still fires — the description was all it needed. Reads the four-line skill file, reads sales.csv, writes peek.md. "
  "Same information. Different shape: lowercase headings, no double-hash, no automatic checker call. Because the definition of done was in the body I just deleted.",
  "CCSession — Run C: Skill(csv-peek) fires, different shape",
  R("CCSession", session("~/scratch — bare frontmatter","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Skill","arg":"csv-peek","state":"done"},
      {"type":"tool","name":"Read","arg":"csv-peek/SKILL.md","state":"done"},
      {"type":"tool","name":"Read","arg":"sales.csv","state":"done"},
      {"type":"tool","name":"Write","arg":"peek.md","state":"done"},
      {"type":"text","text":"file: sales.csv"},
      {"type":"text","text":"rows: 9"},
      {"type":"text","text":"columns: rep, region, quarter…"},
      {"type":"text","text":"first 3 data rows:"},
  ],[0,70,95,120,150,180,205,230,260], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.25,"event":"Skill fires anyway"},{"at":0.8,"event":"lowercase headings"}])

B("B07","BARE FRONT — VERIFY","TERMINAL",LIAM,
  "Check it. Seven lines instead of five. Same information, but grep for the four capital headings — nothing. Run the checker — fail. "
  "Same skill folder, same description, same ask. Different shape, because the body was the shape.",
  "CCSession — grep, check_peek FAIL on run C's peek.md",
  R("CCSession", session("~/scratch — bare frontmatter","default",[
      {"type":"prompt","text":"!wc -l peek.md","cue":0,"typeDuration":28},
      {"type":"text","text":"       7 peek.md"},
      {"type":"prompt","text":"!grep -c '^## FILE:' peek.md","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!python3 check_peek.py peek.md","cue":0,"typeDuration":45},
      {"type":"text","text":"FAIL: heading order [] !="},
      {"type":"text","text":"['FILE', 'ROWS', 'COLUMNS', 'HEAD']"},
  ],[0,40,75,120,150,200,225], mascot="off")),
  [{"at":0.05,"event":"wc → 7"},{"at":0.35,"event":"grep → 0"},{"at":0.85,"event":"FAIL"}])

B("B08","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one-sentence ask, three shapes as the plan. Claude did the bare run — twenty-eight lines, its own shape; the handoff was the checker, and it failed. "
  "Then the dangerous middle: reading the template as instructions rather than as guidance about instructions. The template is prose ABOUT skills. The skill is what you write. "
  "Step four, mine: forty lines with the description pattern and a body that names the shape. Claude did the full run — PASS on the checker it ran itself. "
  "Then interpretive judgment: the gutted skill fired but drifted. That's the tell — router-hit is not shape-hit.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one ask · three skill shapes","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One ask; three shapes as the plan"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 28 lines, ad-hoc shape","handoff":"check_peek.py passes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Template is prose about skills — not the skill","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write the 40-line skill — pattern plus body"},
      {"n":5,"phase":"C","labor":"claude","text":"Full run: 5-line peek, four headings","handoff":"check_peek.py passes; ran it itself","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Gutted skill fires but drifts — not the shape","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B09","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide what shape counts as done — nobody else can. I must write that shape down in the body, or the router hits and the shape drifts. "
  "I must write the definition of done as a check I can run. I should read the template as prose, not as the skill. "
  "Claude can route to a skill from the description alone — it did, twice. It can write the exact shape when the body names it — it did. It should run the checker when the body says to. It should say which skill it took.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"route from the description alone"},{"tier":"CAN","text":"write the shape the body names"},
                          {"tier":"SHOULD","text":"run the checker when told to"},{"tier":"SHOULD","text":"say which skill it took"}],
                    "human":[{"tier":"MUST","text":"decide what shape counts as done"},{"tier":"MUST","text":"write the shape in the body"},
                             {"tier":"MUST","text":"write done as a check I can run"},{"tier":"SHOULD","text":"read the template as prose"}],
                    "closing":"Description hits the router. The body locks the shape.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. The template is eighty-four lines that teach one thing well: the description is the trigger — verified twice, once on a paraphrased ask. "
  "It implies the body is decoration. It isn't: same skill folder, same description; body deleted, output drifted, checker failed. "
  "What would prove this reel wrong: a bare-frontmatter skill that produces the exact same shape as the full skill, on a fresh run, from the description alone.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "The template's central claim is verified: description-as-trigger routes the skill on its own.",
      "Its silent claim is not: bare frontmatter fires, but the shape drifts and the checker fails.",
      "The body is where two runs of the same skill produce the same page. The description gets you invoked.",
      "FALSIFIABLE: a bare-frontmatter skill that produces the exact shape from the description alone."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Open the reference example-skill file, copy the description pattern verbatim into a new skill of yours, then paste this into Claude Code: "
  "Read my SKILL.md and write a five-line definition-of-done script for its output shape. Don't run it yet — I want to read the script first.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Read my SKILL.md and write a five-line definition-of-done script for its output shape. Don't run it yet — I want to read the script first.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"The Template Under Every Skill. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Description hits the router. The body locks the shape. Same skill folder, three shapes.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-skills--claude-liam-example-skill (the concept; the card body replaced by three real runs)",
    "sources":["SESSION.md (three real headless runs)","anthropics/claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
            if len(line)>60: print("  ⚠ plainshell",len(line),line)
