#!/usr/bin/env python3
"""author_sheet.py — cc-claude-skills (cc-explainer · Claude Code 101 · tier 03)
"One Prompt. Every Time." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-claude-skills"; TITLE="One Prompt. Every Time."; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Please summarize article.md."
ASK2="Wrap article.md for a leadership audience — the CEO reads this Friday."
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
  "This is Liam, in for Bear. One sentence, an empty folder: summarise this article. "
  "Watch what it decides on its own. No shape asked for. No file to write to — so it prints to the window. "
  "Five sentences, a bolded takeaways list. Not wrong. But nothing pinned it down.",
  "CCSession — bare run: the ask, Read, an ad-hoc summary printed to the terminal",
  R("CCSession", session("scratch — bare","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":50},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"Q3 API p95 drifted from 180 ms to 340 ms."},
      {"type":"text","text":"Root cause wasn't the shipped features."},
      {"type":"text","text":"The team shipped a cache in two weeks."},
      {"type":"text","text":"p95 recovered to 190 ms."},
      {"type":"text","text":"**Two takeaways:**"},
      {"type":"text","text":"- Instrument dependencies you didn't write"},
      {"type":"text","text":"- When a debate stalls, run the small test"},
  ],[0,70,100,130,160,190,215,240,265], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.35,"event":"Read article.md"},{"at":0.75,"event":"Two takeaways: bolded"}])

# ─── BIDEA · THE IDEA (BrutalistHesitantWriter) ─────────────────────────────
B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Chat-window users think a skill is a slash command they type. "
  "In the terminal, a skill is a folder with a description that finds you. "
  "You never type its name. Claude reads the description and auto-launches it. Same folder, different asks, same output shape. That is what one prompt, every time actually is.",
  "BrutalistHesitantWriter — 'slash command' reconsidered into 'description'",
  R("BrutalistHesitantWriter", writer("A skill is a slash command.\nYou save it. You type slash.\nWrong shape — it is a folder.\nAnd the description is the router.","slash command","description",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.4,"event":"'slash command' → 'description'"},{"at":0.9,"event":"Last line"}])

# ─── BDEFS · DEFINITIONS (CCDefinitions) ────────────────────────────────────
B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. SKILL dot m-d: a markdown file Claude Code loads on demand, zero cost until it fires. "
  "Frontmatter: the YAML block at the top — a name and a description. Description: the sentence in the frontmatter that tells Claude when to auto-launch this skill; the router. "
  "Auto-launch: Claude reading your ask, matching the description, and starting the skill without a slash. Semantic match: matching by meaning, not by exact word.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"SKILL.md","meaning":"a markdown file Claude Code loads on demand — zero cost until fired"},
      {"term":"frontmatter","meaning":"the YAML block at the top — `name` and `description`"},
      {"term":"description","meaning":"the router — tells Claude when to auto-launch this skill"},
      {"term":"auto-launch","meaning":"Claude firing the skill on ask-match — no slash typed"},
      {"term":"semantic match","meaning":"matching by meaning, not exact word — 'wrap' can hit 'summarise'"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

# ─── B01 · BARE — VERIFY (CCPlainShell) ────────────────────────────────────
B("B01","BARE — VERIFY","SHELL",LIAM,
  "Verify what the bare run did. No summary dot m-d in the folder. And zero Skill tool calls in the transcript. "
  "Whatever shape it picked, it picked. Nothing routed. Different day, different shape.",
  "CCPlainShell — ls, grep Skill in the bare run's transcript",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ ls scratch/",
      "README.md    article.md",
      "$ grep -c '\"name\":\"Skill\"' run-bare.jsonl",
      "0",
      "# no summary.md written; no Skill() fired"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="post-hoc verification in a plain shell — the bare run's window is already closed"),
  [{"at":0.05,"event":"ls → no summary"},{"at":0.5,"event":"grep Skill → 0"},{"at":0.85,"event":"the comment"}])

# ─── B02 · THE FOLDER (CCPlainShell) ────────────────────────────────────────
B("B02","THE FOLDER","SHELL",LIAM,
  "The folder. Two files, written once. SKILL dot m-d, twenty-seven lines. Check summary dot p-y, thirty-one lines. "
  "Under dot claude slash skills slash exec-summary. Frontmatter names it and describes when to fire. "
  "Then Format, Rules, and Done. The description is deliberately vague. We'll see what that costs.",
  "CCPlainShell — the SKILL.md folder and its frontmatter",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ ls .claude/skills/exec-summary/",
      "SKILL.md          check_summary.py",
      "$ wc -l .claude/skills/exec-summary/*",
      "      27 SKILL.md",
      "      31 check_summary.py",
      "$ head -3 .claude/skills/exec-summary/SKILL.md",
      "---",
      "name: exec-summary",
      "description: Utility for summarizing documents",
      "$ grep '^## ' .claude/skills/exec-summary/SKILL.md",
      "## Format",
      "## Rules",
      "## Done"],
    "startCue":12,"lineGap":18}, motion="type",
    leaves_terminal_because="reading the built skill folder — no session contains this view"),
  [{"at":0.05,"event":"ls → two files"},{"at":0.4,"event":"wc → 27 · 31"},{"at":0.7,"event":"frontmatter"},{"at":0.9,"event":"three sections"}])

# ─── B03 · SKILL — THE RUN (CCSession) ─────────────────────────────────────
B("B03","SKILL — THE RUN","TERMINAL",LIAM,
  "Same sentence. Fresh session. This time Claude sees the description match — summarise — and auto-launches the skill. "
  "Skill exec-summary shows up in the transcript, right there beside Read. Then Read, then Write summary dot m-d, then it runs the checker itself. PASS. No slash typed.",
  "CCSession — Skill(exec-summary) fires, Read, Write, check_summary.py PASS",
  R("CCSession", session("scratch — with skill","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":50},
      {"type":"tool","name":"Skill","arg":"exec-summary","state":"done"},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"I'll follow exec-summary — four sections,"},
      {"type":"text","text":"write to `summary.md`, run the checker."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_summary.py summary.md","state":"done"},
      {"type":"text","text":"PASS. Four sections written."},
  ],[0,70,105,140,170,205,245,275], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.3,"event":"Skill(exec-summary) fires"},{"at":0.85,"event":"check → PASS"}])

# ─── B04 · SKILL — VERIFY (CCPlainShell) ───────────────────────────────────
B("B04","SKILL — VERIFY","SHELL",LIAM,
  "Verify what the skill built. One Skill call in the transcript. Four headings in summary dot m-d, in the fixed order. "
  "Zero grades, zero percents, zero emoji. And check summary dot p-y — the file's own definition of done — passes.",
  "CCPlainShell — Skill count, four headings, checker PASS",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ grep -c '\"name\":\"Skill\"' run-skill.jsonl",
      "1",
      "$ grep '^## ' summary.md",
      "## What",
      "## Why it matters",
      "## What's new",
      "## What to do",
      "$ CHK=.claude/skills/exec-summary/check_summary.py",
      "$ python3 $CHK summary.md",
      "PASS"],
    "startCue":12,"lineGap":20}, motion="type",
    leaves_terminal_because="post-hoc verification in a plain shell — the skill run's window is already closed"),
  [{"at":0.05,"event":"Skill count → 1"},{"at":0.4,"event":"Four headings"},{"at":0.85,"event":"PASS"}])

# ─── B05 · THE OTHER ASK — correction cycle (CCSession) ────────────────────
B("B05","THE OTHER ASK","TERMINAL",LIAM,
  "One more ask I did not plan. Same folder, same skill. But the word summarise is not in this ask. "
  "Wrap article dot m-d for a leadership audience — the CEO reads this Friday. If routing were literal, the skill would not fire. "
  "It fires. It matches wrap for a leadership audience against summarising documents in a house style. Same four sections, same PASS. That is semantic match.",
  "CCSession — pressure ask, Skill still fires on semantic match, same shape",
  R("CCSession", session("scratch — the other ask","accept-edits",[
      {"type":"prompt","text":ASK2,"cue":0,"typeDuration":90},
      {"type":"tool","name":"Skill","arg":"exec-summary","state":"done"},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"tool","name":"Read","arg":"check_summary.py","state":"done"},
      {"type":"text","text":"I read the check. Writing four sections,"},
      {"type":"text","text":"tuned for a CEO reader."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 check_summary.py summary.md","state":"done"},
      {"type":"text","text":"PASS. Same four sections."},
  ],[0,110,150,190,220,255,290,325,355], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"the other ask"},{"at":0.35,"event":"Skill fires anyway"},{"at":0.9,"event":"PASS — same shape"}])

# ─── BFLOW · WHERE THE SKILL SITS (CCHarnessMap) ────────────────────────────
B("BFLOW","BFLOW — WHERE THE SKILL SITS","DIAGRAM",LIAM,
  "Where the skill sits. At the core, the model — it can only talk. Around it, your ask, whatever words you happened to pick. "
  "Around that, the description match — Claude scans every skill's description and only fires one whose meaning fits. "
  "Then the skill loads on demand — zero cost until now. Then your loop: Read, Write, check the definition of done. "
  "The rings are what the transcript already showed.",
  "CCHarnessMap — model at the core; ASK, DESCRIPTION MATCH, SKILL LOAD, YOUR LOOP as rings",
  R("CCHarnessMap",{"core":"MODEL","coreSub":"can only talk",
      "rings":[
        {"label":"YOUR ASK","sub":"whatever words you typed","items":["'summarise' or 'wrap for leadership'"],"cue":22,"accent":"ink"},
        {"label":"DESCRIPTION MATCH","sub":"which skill fires, if any","items":["ask ≈ description → exec-summary"],"cue":56,"accent":"violet"},
        {"label":"SKILL LOAD","sub":"on demand, zero cost until now","items":[".claude/skills/exec-summary/SKILL.md"],"cue":92,"accent":"spark"},
        {"label":"YOUR LOOP","sub":"Read · Write · check","items":["Read · Write summary.md · check → PASS"],"cue":128,"accent":"add"}],
      "caption":"Every ring is something the transcript already showed.","captionCue":170,"itemGap":10}, motion="drawon",
    leaves_terminal_because="BFLOW: the ask→description→skill→loop chain is implied by the session but never drawn inside it"),
  [{"at":0.05,"event":"MODEL"},{"at":0.35,"event":"DESCRIPTION MATCH"},{"at":0.7,"event":"SKILL LOAD"},{"at":0.9,"event":"YOUR LOOP"}])

# ─── BSHOW · THE BUILT FILE (CCPlainShell) ─────────────────────────────────
B("BSHOW","BSHOW — THE BUILT FILE","SHELL",LIAM,
  "The built thing, running — summary dot m-d itself. Four headings. Each a paragraph. "
  "What: the p-ninety-five drift and its real cause. Why it matters: three days invisible on dashboards. "
  "What's new: the cache in a week, the invalidation contract in another. What to do: audit third-party clients next quarter. "
  "This is what the skill produced. This is the shape it produces every time.",
  "CCPlainShell — cat summary.md, the real output the skill wrote",
  R("CCPlainShell",{"title":"zsh — ~/scratch — summary.md","lines":[
      "$ cat summary.md",
      "## What",
      "  Q3 API p95 drifted from 180 ms to 340 ms —",
      "  cause was the flag evaluator's config …",
      "## Why it matters",
      "  Three days invisible on dashboards; the",
      "  six-week debate cost more than the fix.",
      "## What's new",
      "  Cache in a week, invalidation contract in",
      "  a second week; p95 back at 190 ms.",
      "## What to do",
      "  Audit every third-party client next",
      "  quarter for hidden per-request work."],
    "startCue":12,"lineGap":18}, motion="type",
    leaves_terminal_because="BSHOW: the built file being read is what the skill actually produced"),
  [{"at":0.05,"event":"cat"},{"at":0.25,"event":"## What"},{"at":0.5,"event":"## Why it matters"},{"at":0.75,"event":"## What's new"},{"at":0.9,"event":"## What to do"}])

# ─── BCOND · CONDUCT — the Boondoggle Score (CCBoondoggleScore) ─────────────
B("BCOND","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: pick the output shape — four sections, in that order. "
  "Step two, mine again: write SKILL dot m-d and the checker. Twenty-seven and thirty-one lines. Once. "
  "Step three, Claude: the bare run — an invented shape and no file at all. "
  "Step four, the dangerous middle — reading the bare output and noticing nothing was pinned. "
  "Step five, Claude: the skill run — Skill fires, Read, Write, check, PASS. "
  "Step six, Claude again on the other ask: skill fires by meaning, not word. Same shape.",
  "CCBoondoggleScore — six steps",
  R("CCBoondoggleScore",{"system":"exec-summary · fresh sessions","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Pick the output shape — 4 sections"},
      {"n":2,"phase":"F","labor":"human","capacity":"PF","text":"Write SKILL.md + checker — 58 lines"},
      {"n":3,"phase":"C","labor":"claude","text":"Bare: ad-hoc summary, no file","handoff":"nothing pinned the shape","dependsOn":[]},
      {"n":4,"phase":"H","labor":"human","capacity":"PA","text":"Read bare: nothing was pinned","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Skill run: fires, Write, check PASS","handoff":"check_summary.py prints PASS","dependsOn":[2,4]},
      {"n":6,"phase":"C","labor":"claude","text":"Other ask: fires by meaning, PASS","handoff":"same four sections, same PASS","dependsOn":[2]},
  ],"dangerousMiddle":4,"distribution":True,"stepGap":22}, motion="drawon",
    leaves_terminal_because="the score of the session, not shown in the session"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 4 rings"},{"at":0.9,"event":"Tally"}])

# ─── BHUM · HUMAN — the ledger (CCHumanLedger) ──────────────────────────────
B("BHUM","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide the output shape — nobody else can. I must write done as a check a script can run. "
  "I must write a description that is a router, not a name. And I should test the routing on asks that do not use my trigger word. "
  "Claude can auto-launch a skill from a description match. Can Write the file and run the checker itself. "
  "Should route by meaning, not exact word. Should cite the skill in its output. Fifty-eight lines. Written once. That is what I would not delegate.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"auto-launch on description match"},
      {"tier":"CAN","text":"Write the file, run the checker"},
      {"tier":"SHOULD","text":"route by meaning, not word"},
      {"tier":"SHOULD","text":"cite the skill in its output"}],
    "human":[
      {"tier":"MUST","text":"decide the output shape"},
      {"tier":"MUST","text":"write done as a check"},
      {"tier":"MUST","text":"write the description as a router"},
      {"tier":"SHOULD","text":"test asks without the trigger word"}],
    "closing":"58 lines, written once. Same shape every ask.","humanCue":70,"rowGap":12}, motion="drawon",
    leaves_terminal_because="the ledger of what is the human's, not shown in the session"),
  [{"at":0.05,"event":"THE AI"},{"at":0.4,"event":"THE HUMAN"},{"at":0.9,"event":"Closing"}])

# ─── BVDT · VERDICT (ClaudeVerdictArtifact) ─────────────────────────────────
B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Bare: no skill in the folder, an ad-hoc summary printed to the window, no file. Zero Skill calls in the transcript. "
  "With SKILL dot m-d — twenty-seven lines written once: skill auto-launches on ask-match, writes the fixed four-section file, runs the checker itself, PASS. No slash typed. "
  "Different ask, no trigger word: skill still fires — semantic match — same shape, same PASS. "
  "What would prove this reel wrong: a skill run where changing the ask changed the output shape.",
  "ClaudeVerdictArtifact — four lines",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare, empty folder: ad-hoc summary, no file. Zero Skill() calls in the transcript.",
      "SKILL.md, 27 lines written once: auto-launches on ask, writes summary.md, checker PASS. No slash.",
      "Different ask, no trigger word: skill fires by semantic match. Same four sections. Same PASS.",
      "FALSIFIABLE: a skill run where changing the ask changed the output shape."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.25,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

# ─── BHTF · YOUR TURN (ClaudeComposerAsk) ───────────────────────────────────
B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next repeated workflow, open Claude Code and paste this: "
  "Ask me the four questions I need to answer before you can turn this into a SKILL dot m-d — "
  "what the description trigger should say, what the four output sections are, what the rules the skill must refuse are, and what a passing run looks like as a Python script. "
  "Then write the SKILL dot m-d and the checker. Don't run anything yet.",
  "ClaudeComposerAsk — the viewer's prompt",
  R("ClaudeComposerAsk",{"greeting":"Your turn.",
      "command":"Ask me the four questions I need before you can turn this workflow into a SKILL.md — description trigger, output sections, refusal rules, definition-of-done script — one at a time. Then write the SKILL.md and the checker. Don't run anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],
      "folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

# ─── BOUT · OUTRO (ClaudeTitleOutro) ────────────────────────────────────────
B("BOUT","OUTRO","BOOKEND",LIAM,
  "One Prompt. Every Time. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,
    "subtitle":"A skill is a description that finds you — no slash typed, same shape every ask.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands",
    "audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},
    "aspect":"16:9","fps":30,"session":"SESSION.md","build":True,
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-cowork--claude-liam-claude-skills (the concept; three fresh runs replace the chat-window framing)",
    "sources":["SESSION.md (three real runs, Claude Code 2.1.150)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},
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
