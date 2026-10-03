#!/usr/bin/env python3
"""author_sheet.py — cc-claude-agent-skills--claude-skills-progressive-disclosure (cc-explainer · Claude Code 101 · tier 03).
"Unlimited Knowledge, A Hundred Words of Context." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-claude-agent-skills--claude-skills-progressive-disclosure"
TITLE="Unlimited Knowledge, A Hundred Words of Context"
TOPIC="CLAUDE CODE 101"
LIAM="am_onyx"; WPS=2.9
ASK_A="Please summarize article.md into summary.md."
ASK_B="Write an executive summary of article.md into summary.md."
ASK_C="Write an executive summary of article.md into summary.md, following our house style precisely."
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

B("B00","COLD OPEN — SKILL FIRES","TERMINAL",LIAM,
  "This is Liam, in for Bear. Same one-sentence ask, three different runs. Here's the one where Claude finds the skill on its own. "
  "The ask says executive summary. The router matches it to a skill named exec-summary, whose description reads one line. The body loads on that match — a hundred and fifty words, on demand. Nothing else.",
  "CCSession — Run B: the ask, Skill(exec-summary), Read article.md, Write summary.md",
  R("CCSession", session("scratch — with skill","accept-edits",[
      {"type":"prompt","text":ASK_B,"cue":0,"typeDuration":78},
      {"type":"tool","name":"Skill","arg":"exec-summary","state":"done"},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"I'll write summary.md in the four-"},
      {"type":"text","text":"section house shape: What, Why it"},
      {"type":"text","text":"matters, What's new, What to do."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
  ],[0,100,140,175,200,225,260], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.4,"event":"Skill(exec-summary) fires"},{"at":0.85,"event":"Write summary.md"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Every skill you install adds knowledge. Fifty skills, you'd think, adds fifty times the context. It doesn't. "
  "The only thing loaded at every turn is each skill's description — roughly a hundred words. The body, the references, the code — none of that costs a token until an ask arrives that needs it. "
  "The description is the gate. Three tiers of loading, decided one ask at a time.",
  "BrutalistHesitantWriter — 'resident' reconsidered into 'described'",
  R("BrutalistHesitantWriter", writer("Add a skill, add its knowledge.\nFifty pages, resident.\nThe body, the references, the code.\nNo — a hundred words each.","resident","described",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'resident' → 'described'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Skill: a folder Claude Code loads from `.claude/skills` — a description, a body, and any files the body needs. "
  "Description: the one-line frontmatter field the router reads at every turn — usually eight to twenty words. Body: the rest of `SKILL.md`, loaded only when the description matches and `Skill()` fires as a tool. "
  "Reference: a file under `references/` that the body reads only when its own condition is true. Progressive disclosure: loading the least you need to answer this ask.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"skill","meaning":"a folder under .claude/skills — description, body, and files the body needs"},
      {"term":"description","meaning":"the one-line frontmatter field the router reads every turn"},
      {"term":"body","meaning":"the rest of SKILL.md — loaded only when Skill() fires as a tool"},
      {"term":"reference","meaning":"a file under references/ the body reads only when its condition is true"},
      {"term":"progressive disclosure","meaning":"load the least you need to answer this ask; nothing more"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","THE SKILL FOLDER","SHELL",LIAM,
  "This is the skill on disk. Thirty lines in SKILL.md — eight of them are the description in the frontmatter, the rest is the body. "
  "Under references, two files: house-style, one hundred ninety-five words; length, one hundred and five. Three hundred words in reserve. "
  "At every turn only the description is in context — eight words. The rest costs zero tokens until it's needed.",
  "CCPlainShell — wc on the skill files; head on frontmatter",
  R("CCPlainShell",{"title":"zsh — scratch/.claude/skills/exec-summary","lines":[
      "$ wc -l SKILL.md references/*.md",
      "      30 SKILL.md",
      "      35 references/house-style.md",
      "      24 references/length.md",
      "$ head -3 SKILL.md",
      "---",
      "name: exec-summary",
      "description: Summarize in the house exec-summary style.",
      "$ wc -w SKILL.md references/*.md",
      "     150 SKILL.md            # body",
      "     195 references/house-style.md",
      "     105 references/length.md"],
    "startCue":8,"lineGap":22}, motion="type",
    leaves_terminal_because="the three tiers of the skill are files on disk, not a session state"),
  [{"at":0.05,"event":"wc SKILL.md → 30 lines"},{"at":0.5,"event":"description: 8 words"},{"at":0.85,"event":"references — 300 words"}])

B("B02","RUN A — BARE","TERMINAL",LIAM,
  "First run. The same folder, but with the skill removed. Just the article, the checker, and the ask. Claude reads the article, writes summary-dot-md, and calls it done. "
  "One heading — a single hash. Three paragraphs. Not what the house wants, and there's nothing in the folder that would tell it otherwise.",
  "CCSession — Run A: no skill; Read article, Write summary",
  R("CCSession", session("scratch — no skill","accept-edits",[
      {"type":"prompt","text":ASK_A,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"I'll condense the article into the"},
      {"type":"text","text":"problem, what was tried, and what"},
      {"type":"text","text":"worked."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
  ],[0,90,120,145,170,210], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.35,"event":"Read article"},{"at":0.8,"event":"Write, done"}])

B("B03","RUN A — VERIFY","TERMINAL",LIAM,
  "Check it. No skill was called — grep on Skill in the transcript returns zero. No two-hash headings in the output. And the checker fails on the first rule: the four house sections aren't there. "
  "Not wrong for a chat-window summary. Wrong for this house. And nothing in the folder told it what this house wants.",
  "CCSession — grep Skill=0, grep ##=0, check FAIL",
  R("CCSession", session("scratch — no skill","default",[
      {"type":"prompt","text":"!grep -c '\"name\":\"Skill\"' run-a.jsonl","cue":0,"typeDuration":72},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep -c ^## summary.a.md","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!python3 check.py summary.a.md","cue":0,"typeDuration":44},
      {"type":"text","text":"FAIL: headings — got []"},
  ],[0,80,110,145,170,205], mascot="off")),
  [{"at":0.1,"event":"Skill count → 0"},{"at":0.45,"event":"## count → 0"},{"at":0.8,"event":"FAIL"}])

B("B04","RUN B — SKILL FIRES","TERMINAL",LIAM,
  "Second run. The skill folder is back. Same style of ask, this time using the words executive summary. The router matches it to the description of exec-summary, and `Skill` fires as a tool. "
  "That's the body loading. A hundred and fifty words of house rules. Then Claude reads the article. Then writes summary-dot-md with the four sections in the right order. It never touches the references — the body told it not to for a plain summary.",
  "CCSession — Run B: Skill(exec-summary), Read article, Write summary",
  R("CCSession", session("scratch — with skill","accept-edits",[
      {"type":"prompt","text":ASK_B,"cue":0,"typeDuration":78},
      {"type":"tool","name":"Skill","arg":"exec-summary","state":"done"},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"Four sections in the fixed order:"},
      {"type":"text","text":"What, Why it matters, What's new,"},
      {"type":"text","text":"What to do. References not needed."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
  ],[0,100,140,175,205,235,270], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.35,"event":"Skill(exec-summary) fires"},{"at":0.85,"event":"Write summary.md"}])

B("B05","RUN B — VERIFY","TERMINAL",LIAM,
  "Check it. Skill fired once. References read: zero. The four sections landed. The checker passes. "
  "One skill match; a hundred and fifty words loaded on demand; three hundred more still on disk. Same folder, same ask style, different tier depth.",
  "CCSession — grep Skill=1, refs=0, check PASS",
  R("CCSession", session("scratch — with skill","default",[
      {"type":"prompt","text":"!grep -c '\"name\":\"Skill\"' run-b.jsonl","cue":0,"typeDuration":72},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -c references/ run-b.jsonl","cue":0,"typeDuration":48},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep ^## summary.b.md","cue":0,"typeDuration":40},
      {"type":"text","text":"## What"},
      {"type":"text","text":"## Why it matters"},
      {"type":"text","text":"## What's new"},
      {"type":"text","text":"## What to do"},
      {"type":"prompt","text":"!python3 check.py summary.b.md","cue":0,"typeDuration":44},
      {"type":"text","text":"PASS"},
  ],[0,80,110,145,170,200,220,240,260,290,320], mascot="off")),
  [{"at":0.05,"event":"Skill → 1"},{"at":0.3,"event":"references → 0"},{"at":0.9,"event":"PASS"}])

B("B06","RUN C — THE REFERENCE","TERMINAL",LIAM,
  "Third run. Same folder. Same skill. This time the ask ends with the words: following our house style precisely. "
  "`Skill` fires as before — the description matched again. And then something new: the body of the skill has a conditional. If the ask contains the phrase house style, read references slash house-style dot md. It does. That's tier three loading — on demand, driven by the body reading the ask.",
  "CCSession — Run C: Skill, Read house-style.md, Read article, Write summary",
  R("CCSession", session("scratch — with skill · strict","accept-edits",[
      {"type":"prompt","text":ASK_C,"cue":0,"typeDuration":110},
      {"type":"tool","name":"Skill","arg":"exec-summary","state":"done"},
      {"type":"tool","name":"Read","arg":"references/house-style.md","state":"done"},
      {"type":"tool","name":"Read","arg":"article.md","state":"done"},
      {"type":"text","text":"Past tense for outcomes, present for"},
      {"type":"text","text":"the diagnosis, imperative for the"},
      {"type":"text","text":"recommendations. No forbidden words."},
      {"type":"tool","name":"Write","arg":"summary.md","state":"done"},
  ],[0,140,180,215,250,275,300,340], mascot="off")),
  [{"at":0.05,"event":"Ask types 'house style'"},{"at":0.35,"event":"Skill fires"},{"at":0.55,"event":"Read house-style.md"},{"at":0.9,"event":"Write"}])

B("B07","RUN C — VERIFY","TERMINAL",LIAM,
  "Check it. Skill fired once. This time references-slash was read once. And the second reference — length dot md — was not read: no board, no incident in the ask, so the body's other conditional stayed cold. "
  "Three hundred and fifty-three words of skill context loaded — for the same folder that cost a hundred and fifty-eight in the previous run, and zero in the first. Three depths from one skill, one ask apart.",
  "CCSession — grep Skill=1, refs=1, length=0, check PASS",
  R("CCSession", session("scratch — with skill · strict","default",[
      {"type":"prompt","text":"!grep -c '\"name\":\"Skill\"' run-c.jsonl","cue":0,"typeDuration":72},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -c references/ run-c.jsonl","cue":0,"typeDuration":48},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -c length.md run-c.jsonl","cue":0,"typeDuration":48},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!python3 check.py summary.c.md","cue":0,"typeDuration":44},
      {"type":"text","text":"PASS"},
  ],[0,80,110,145,170,205,230,265], mascot="off")),
  [{"at":0.1,"event":"Skill → 1"},{"at":0.35,"event":"references → 1"},{"at":0.6,"event":"length → 0"},{"at":0.9,"event":"PASS"}])

B("B08","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: an eight-word description that names when this skill applies. Step two, mine: the thirty lines of body that make the four-section shape. Step three, mine: the two reference files, and the conditional that says when to read each. "
  "Step four, Claude — three runs. Each match went from ask to a `Skill` call to only the files needed. The dangerous middle: the body's conditional. If the words are wrong there, the wrong reference loads or none does, and nobody sees it. "
  "Interpretive judgment, mine, once: which words in the ask should trigger which reference. Executive integration, zero — one skill, one job.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one description · three files","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Description: 8 words, the router's gate"},
      {"n":2,"phase":"F","labor":"human","capacity":"PF","text":"Body: 30 lines, the four-section shape"},
      {"n":3,"phase":"F","labor":"human","capacity":"IJ","text":"References + conditionals: 3 words each"},
      {"n":4,"phase":"C","labor":"claude","text":"Run A: no skill — ad-hoc summary","handoff":"check.py FAIL — expected","dependsOn":[1]},
      {"n":5,"phase":"C","labor":"claude","text":"Run B: Skill fires, references skipped","handoff":"check.py PASS, references untouched","dependsOn":[2]},
      {"n":6,"phase":"C","labor":"claude","text":"Run C: Skill fires, house-style loads","handoff":"check.py PASS, one ref of two","dependsOn":[3]},
      {"n":7,"phase":"H","labor":"human","capacity":"PA","text":"Read the jsonl — grep proved the tiers"},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B09","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must write the description — nobody else knows what this house calls a summary. I must decide when a reference is worth its tokens. I must check the transcript — the grep is proof; the sentence in chat is a claim. "
  "Claude can find a skill from its description alone — it did. It can honor a body's conditional — it did. It should skip a reference when the body says so — it did. It should recite the loaded reference's rules in its close — it did. Eight words of description, thirty lines of body. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"find a skill from its description"},{"tier":"CAN","text":"honor the body's conditional loads"},
                          {"tier":"SHOULD","text":"skip refs the body says to skip"},{"tier":"SHOULD","text":"recite loaded rules in the close"}],
                    "human":[{"tier":"MUST","text":"write the description — my job"},{"tier":"MUST","text":"decide when a ref is worth tokens"},
                             {"tier":"MUST","text":"read the jsonl, not the chat"},{"tier":"SHOULD","text":"grep for Skill, not read chat"}],
                    "closing":"Eight words that route, thirty lines that shape. Mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One skill folder, three tiers: an eight-word description resident at every turn, a hundred and fifty-word body loaded when the description matches, and three hundred words of references loaded only when the body's condition is true. "
  "Three runs against the same folder loaded zero, a hundred and fifty-eight, and three hundred fifty-three words of skill context — one skill, three depths, decided by the ask. "
  "What would prove this reel wrong: a run whose transcript reads a reference file the body's conditional didn't call for.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "One skill, three tiers: description resident, body on Skill(), references on the body's condition.",
      "Same folder, three runs: 0 / 158 / 353 words of skill context loaded — decided by the ask.",
      "The description is the router's gate; the body is the shape; the references are the on-demand depth.",
      "FALSIFIABLE: a run whose transcript reads a reference the body's condition never named."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next skill, open Claude Code and paste this: help me write the description for a skill named exec-summary — one sentence, under twenty words, "
  "that fires only on asks about summarizing documents in a house style. Then write two conditionals for the body — one that reads a house-style reference on strict-style asks, one that reads a length reference on board or incident asks. Don't build the body yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Help me write the description for a skill named exec-summary — one sentence, under 20 words, that fires only on asks about summarizing documents in a house style. Then write two conditionals for the body: one that reads a house-style reference on strict-style asks, one that reads a length reference on board or incident asks. Don't build the body yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Unlimited Knowledge, A Hundred Words of Context. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"One skill folder, three tiers, three depths — decided one ask at a time.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"anthropics/claude-code-101/03-hooks-skills-commands/claude-agent-skills--claude-skills-progressive-disclosure (concept only — the deep-explainer draft is not reused; three real headless runs replace all card body)",
    "sources":["SESSION.md (three real headless runs, 2026-09-10)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
