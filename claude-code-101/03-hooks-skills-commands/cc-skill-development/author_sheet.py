#!/usr/bin/env python3
"""author_sheet.py — cc-skill-development (cc-explainer · Claude Code 101 · tier 03)
"Claude, Skill Development." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-skill-development"; TITLE="Claude, Skill Development."; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK_BARE="Create a Claude Code skill at skills/csv-shape/SKILL.md that wraps csv_shape.py so future sessions know when to run it."
ASK_RULES="Same task, plus three rules: third-person description with quoted trigger phrases; imperative body; keep SKILL.md under 400 words by moving detail to references/troubleshooting.md."
ASK_CHK="Create a skill at skills/csv-shape/SKILL.md that PASSES python3 validate_skill.py. Do not read any other guidance."
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
  "This is Liam, in for Bear. Four files in an empty folder, one ask: wrap this csv_shape.py script as a Claude Code skill so future sessions know when to run it. "
  "Watch what it decides on its own. It reads everything, writes one file, runs the checker. Pass. Six hundred thirty words in one file. "
  "Every rule the checker knows: satisfied. And the pattern Anthropic actually teaches: skipped.",
  "CCSession — the bare run: four Reads, mkdir, Write, validate_skill.py PASS",
  R("CCSession", session("csv-shape — bare","accept-edits",[
      {"type":"prompt","text":ASK_BARE,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"csv_shape.py","state":"done"},
      {"type":"tool","name":"Read","arg":"validate_skill.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"mkdir -p skills/csv-shape","state":"done"},
      {"type":"tool","name":"Write","arg":"skills/csv-shape/SKILL.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 validate_skill.py …","state":"done"},
      {"type":"text","text":"PASS — six rules satisfied."},
      {"type":"text","text":"630 words. Third-person description."},
      {"type":"text","text":"References csv_shape.py."},
  ],[0,80,105,130,155,180,215,250,270,290])),
  [{"at":0.05,"event":"Ask types"},{"at":0.55,"event":"Write SKILL.md"},{"at":0.85,"event":"PASS: 630 words"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. You might picture a skill as a prompt Claude reads. It isn't. It's a folder Claude finds — SKILL.md at the root, references and scripts and assets beside it, loaded on demand. "
  "What lives in that folder decides whether Claude reaches for the skill at all, and whether the skill stays cheap to load or bloats every session it fires in.",
  "BrutalistHesitantWriter — 'prompt' reconsidered into 'folder'",
  R("BrutalistHesitantWriter",
    writer("A skill is a prompt Claude reads.\nOne file, loaded every session.\nMore words, more context, always.\nProgressive disclosure needs a folder.","prompt","folder",SLUG),
    motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'prompt' → 'folder'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we go on. SKILL.md: the file at the root of a skill folder — YAML frontmatter, then markdown body. "
  "Frontmatter: the YAML block at the top, with name and description; always in context. "
  "Trigger phrase: a specific quoted phrase in the description that Claude matches user requests against. "
  "Progressive disclosure: metadata always loaded, SKILL.md body when triggered, references only when Claude asks. "
  "Imperative form: verb-first instructions — parse the CSV, not you should parse the CSV.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"SKILL.md","meaning":"file at the root of a skill folder — YAML frontmatter, markdown body"},
      {"term":"frontmatter","meaning":"YAML at the top of SKILL.md; name and description; always loaded"},
      {"term":"trigger phrase","meaning":"quoted phrase Claude matches user requests against"},
      {"term":"prog. disclosure","meaning":"metadata always; body when triggered; refs on demand"},
      {"term":"imperative form","meaning":"verb-first instructions, no 'you should' or 'you can'"}],
    "startCue":12,"rowGap":48}, motion="drawon",
    leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare skill by hand. One file. Six hundred thirty words. Frontmatter opens with 'this skill should be used when' — third person, four quoted trigger phrases. "
  "Body has zero second-person forms. Every rule the checker enforces, satisfied. And ls skills/csv-shape: one file, SKILL.md. No references folder. "
  "The whole skill is in the always-loaded part. Nothing hidden. Nothing deferred.",
  "CCSession — wc, ls, head; the always-loaded body",
  R("CCSession", session("csv-shape — bare","default",[
      {"type":"prompt","text":"!wc -w skills/csv-shape/SKILL.md","cue":0,"typeDuration":40},
      {"type":"text","text":"     630 skills/csv-shape/SKILL.md"},
      {"type":"prompt","text":"!ls skills/csv-shape/","cue":0,"typeDuration":30},
      {"type":"text","text":"SKILL.md"},
      {"type":"prompt","text":"!head -3 skills/csv-shape/SKILL.md","cue":0,"typeDuration":36},
      {"type":"text","text":"---"},
      {"type":"text","text":"name: csv-shape"},
      {"type":"text","text":"description: This skill should be used …"},
      {"type":"prompt","text":"!grep -Ec 'you should|you need' …","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
  ],[0,40,80,105,145,180,200,220,250,290])),
  [{"at":0.05,"event":"wc → 630"},{"at":0.3,"event":"ls → one file"},{"at":0.85,"event":"no you-should"}])

B("B02","THE MIDDLE CASE","TERMINAL",LIAM,
  "One more run I didn't plan for. Give Claude just the checker script and tell it to make the checker pass. Nothing else. "
  "It reads the checker, writes SKILL.md, runs the checker itself. Pass. Six hundred thirty-five words in one file. No references folder. "
  "The exact shape as the bare run. The letters, none of the spirit. The checker cannot see progressive disclosure — it can only count words and grep for 'you should'.",
  "CCSession — the checker-only run: PASS but one monolith",
  R("CCSession", session("csv-shape — checker only","accept-edits",[
      {"type":"prompt","text":ASK_CHK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"validate_skill.py","state":"done"},
      {"type":"tool","name":"Write","arg":"skills/csv-shape/SKILL.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 validate_skill.py","state":"done"},
      {"type":"text","text":"PASS: 635 words, six rules."},
      {"type":"text","text":"Five quoted trigger phrases."},
      {"type":"text","text":"No second-person forms."},
      {"type":"prompt","text":"!ls skills/csv-shape/","cue":0,"typeDuration":30},
      {"type":"text","text":"SKILL.md"},
  ],[0,90,120,170,210,235,255,290,320])),
  [{"at":0.05,"event":"Ask types"},{"at":0.45,"event":"PASS: 635"},{"at":0.85,"event":"ls → one file"}])

B("B03","THREE RULES — THE RUN","TERMINAL",LIAM,
  "Same task. Three rules added. Third-person description with quoted triggers. Imperative body. Keep SKILL.md under four hundred words — move the detail to references-slash-troubleshooting-dot-md, and reference it. "
  "Claude reads the same four files. Mkdir references. Two writes: SKILL.md, then references-slash-troubleshooting-dot-md. Runs the checker itself. Pass. Three hundred sixty-seven words.",
  "CCSession — the rules run: two writes, checker PASS",
  R("CCSession", session("csv-shape — three rules","accept-edits",[
      {"type":"prompt","text":ASK_RULES,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"csv_shape.py","state":"done"},
      {"type":"tool","name":"Read","arg":"validate_skill.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"mkdir -p skills/csv-shape/references","state":"done"},
      {"type":"tool","name":"Write","arg":"skills/csv-shape/SKILL.md","state":"done"},
      {"type":"tool","name":"Write","arg":"references/troubleshooting.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 validate_skill.py","state":"done"},
      {"type":"text","text":"PASS: 367 words, six rules."},
  ],[0,80,105,130,155,190,225,260,290])),
  [{"at":0.05,"event":"Rules ask"},{"at":0.55,"event":"Two writes"},{"at":0.9,"event":"PASS: 367"}])

B("B04","THREE RULES — VERIFY","TERMINAL",LIAM,
  "Check what changed. Three hundred sixty-seven words in SKILL.md — the always-loaded part. Five hundred fifty-two words in references-slash-troubleshooting — loaded only when Claude asks for it. "
  "Two files in the folder now. Same skill, half the context on every session that doesn't trip an edge case. "
  "The frontmatter still passes the checker. The body still points at csv_shape.py. What's different is the shape.",
  "CCSession — wc across both files; the reference pointer in SKILL.md",
  R("CCSession", session("csv-shape — three rules","default",[
      {"type":"prompt","text":"!wc -w SKILL.md references/*.md","cue":0,"typeDuration":50},
      {"type":"text","text":"     367 SKILL.md"},
      {"type":"text","text":"     552 references/troubleshooting.md"},
      {"type":"prompt","text":"!ls skills/csv-shape/","cue":0,"typeDuration":30},
      {"type":"text","text":"SKILL.md   references"},
      {"type":"prompt","text":"!grep -n references SKILL.md","cue":0,"typeDuration":36},
      {"type":"text","text":"46: consult `references/troubleshoot…"},
  ],[0,40,80,120,150,185,220])),
  [{"at":0.05,"event":"wc → 367 + 552"},{"at":0.4,"event":"ls → two files"},{"at":0.85,"event":"points at references/"}])

B("BFLOW1","FOLDER SHAPE","CARD",LIAM,
  "Draw what got built. Skills-slash-csv-shape at the root. Inside it, four things a skill can hold — SKILL.md required, the rest optional. "
  "SKILL.md loads every time the description matches. References load only when Claude opens one. Scripts run without loading at all. Assets go into whatever Claude produces. "
  "Progressive disclosure isn't a rule you follow — it's what this folder shape does for free.",
  "CoworkFolderTree — the skill anatomy",
  R("CoworkFolderTree",{"rootName":"skills/csv-shape","folders":[
      {"name":"SKILL.md","accent":True},
      {"name":"references/","accent":False},
      {"name":"scripts/","accent":False},
      {"name":"assets/","accent":False}],
    "caption":"SKILL.md required · everything else optional",
    "sparkLine":"The folder is the skill.","folderLabel":"@NikBearBrown"}, motion="drawon",
    leaves_terminal_because="BFLOW: the folder anatomy the terminal only implied across two sessions"),
  [{"at":0.05,"event":"Root"},{"at":0.5,"event":"Subfolders land"},{"at":0.9,"event":"Spark"}])

B("BSHOW1","THE FINISHED SKILL","SHELL",LIAM,
  "Read the finished skill. Description, third person, six quoted triggers — the phrases a user would actually say. Body, three hundred sixty-seven words. "
  "Line forty-six points at references-slash-troubleshooting-dot-md — a hand-off. If a session sees 'shape of this csv', it loads SKILL.md. "
  "If it hits a ragged row, it opens the reference. If it never trips an edge case, it never pays for one.",
  "CCPlainShell — the rules skill's frontmatter and the reference pointer",
  R("CCPlainShell",{"title":"zsh — skills/csv-shape","lines":[
      "$ head -3 SKILL.md",
      "---",
      "name: csv-shape",
      "description: This skill should be used …",
      "$ grep -o '\"[^\"]*\"' SKILL.md | head -3",
      '"what\'s in this csv"',
      '"shape of this csv"',
      '"describe this csv"',
      "$ grep -n references SKILL.md",
      "46: consult `references/troubleshooting.md`"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="BSHOW: the finished skill's frontmatter and reference pointer, plain-shell read"),
  [{"at":0.05,"event":"head -3"},{"at":0.5,"event":"trigger phrases"},{"at":0.85,"event":"references pointer"}])

B("BCOND","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one-line task, wrap the helper. Claude did the bare run: six hundred thirty words, one file, checker passes. "
  "Step three, the dangerous middle: reading what Claude wrote — one file, no references — and noticing that the checker passing wasn't enough. "
  "Then the real work, mine: name the three rules a lean skill needs. Claude did the rules run: three hundred sixty-seven words plus a reference file, checker passes. "
  "Then interpretive judgment: the checker-only run passed the letters and missed the shape. Tool orchestration, zero; executive integration, zero. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one-line task · three rules","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One-line task, wrap csv_shape.py"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 630 words, one file","handoff":"validate_skill.py passes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the folder: no references","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Add three rules for a lean skill","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Rules: 367 words + references file","handoff":"checker passes; folder has two files","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Checker-only: letters not shape","dependsOn":[2]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("BHUM","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name the trigger phrases a user would actually type — nobody else knows them. I must decide what belongs in SKILL.md and what belongs in references. "
  "I must read the folder, not just the checker output. Claude can fill a silence with one big file, and it will. It can honour rules once I name them. "
  "It should run the checker itself — and it did. It should point at its own references — and it did. What the folder holds is mine to decide.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"fill silence with one big file"},
      {"tier":"CAN","text":"honour rules once named"},
      {"tier":"SHOULD","text":"run the checker itself"},
      {"tier":"SHOULD","text":"point at its own references"}],
    "human":[
      {"tier":"MUST","text":"name the trigger phrases"},
      {"tier":"MUST","text":"decide what belongs where"},
      {"tier":"MUST","text":"read the folder, not the check"},
      {"tier":"SHOULD","text":"keep SKILL.md lean"}],
    "closing":"The checker sees letters. Folder shape is mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Bare run: six hundred thirty words in one file, checker passes. "
  "Rules run: three hundred sixty-seven words in SKILL.md, five hundred fifty-two in references-slash-troubleshooting, checker passes, folder holds two files. "
  "Checker-only run passes too — six hundred thirty-five words, one file, no references. Same trap. "
  "What would prove this reel wrong: a bare run that writes a references folder on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare: 630 words, one file. Checker passes.",
      "Rules: 367 words + references/troubleshooting.md 552 words. Two-file folder.",
      "Checker-only passes too — 635 words, one file, no references. Same trap.",
      "FALSIFIABLE: a bare run that writes a references/ folder on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.25,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next Claude Code skill, open Claude Code and paste this: For a skill I'll describe in one sentence, ask me what a user would actually type to trigger it. "
  "Draft the frontmatter with those phrases in quotes. Then propose which sections belong in SKILL.md and which belong in references-slash-something-dot-md. Don't write the skill yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"For a skill I'll describe in one sentence, ask me what a user would actually type to trigger it. Draft the frontmatter with those phrases in quotes. Then propose which sections belong in SKILL.md and which in references/. Don't write the skill yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Claude, Skill Development. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same one-line task, three ways. A skill is a folder, not a prompt — and the checker cannot see that.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "build":True,
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-skill-development (the concept; the card body replaced by three real runs building the same skill three ways)",
    "sources":["SESSION.md (three real runs; validate_skill.py; SKILL.{bare,rules,checker}.md)",
               "anthropics/claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md (the rules distilled)",
               "info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md",
               "info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
here=os.path.dirname(os.path.abspath(__file__)); json.dump(sheet,open(os.path.join(here,"beat_sheet.json"),"w"),indent=2,ensure_ascii=False)
print(f"{len(beats)} beats — est {sum(b['estimated_duration_s'] for b in beats):.0f}s")
warn=0
for b in beats:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        assert len(r["props"]["blocks"])==len(r["props"]["cues"]), b["beat_id"]
        for blk in r["props"]["blocks"]:
            if blk["type"]=="text" and len(blk["text"])>44: print(f"  ⚠ {b['beat_id']} text {len(blk['text'])}: {blk['text']}"); warn+=1
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print(f"  ⚠ ledger {c} {len(row['text'])}: {row['text']}"); warn+=1
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>44: print(f"  ⚠ step {len(st['text'])}: {st['text']}"); warn+=1
            if st.get("handoff") and len(st["handoff"])>50: print(f"  ⚠ handoff {len(st['handoff'])}: {st['handoff']}"); warn+=1
    if r["pattern"]=="CCPlainShell":
        for ln in r["props"]["lines"]:
            if len(ln)>62: print(f"  ⚠ shell line {len(ln)}: {ln}"); warn+=1
    if r["pattern"]=="ClaudeVerdictArtifact":
        n=len(r["props"]["artifactLines"])
        if n not in (4,6): print(f"  ⚠ verdict lines={n} (must be 4 or 6)"); warn+=1
    if r["pattern"]=="CCDefinitions":
        for t in r["props"]["terms"]:
            if len(t["term"])>18: print(f"  ⚠ term {len(t['term'])}: {t['term']}"); warn+=1
            if len(t["meaning"])>72: print(f"  ⚠ meaning {len(t['meaning'])}: {t['meaning']}"); warn+=1
print(f"warnings: {warn}")
