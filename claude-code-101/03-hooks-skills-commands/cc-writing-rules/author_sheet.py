#!/usr/bin/env python3
"""author_sheet.py — cc-writing-rules (cc-explainer · Claude Code 101 · tier 03)
"The SKILL.md That Made 'Hookify' A Real Word." Every block traces to SESSION.md (two real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-writing-rules"; TITLE="The SKILL.md That Made Hookify A Real Word"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Add a hookify rule to this project that BLOCKS any edit or write to a `.env` file. Save it in `.claude/`."
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
  "This is Liam, in for Bear. One sentence: add a hookify rule that blocks writes to a dot-env file. Two runs, same sentence, one difference — whether the plugin's SKILL is on disk. "
  "Watch what happens when it isn't. Claude reaches for the nearest word it knows: a native Claude Code hook. Not the plugin.",
  "CCSession — the bare run: the ask, the wrong skill, a settings.json write",
  R("CCSession", session("hookify — bare","bypass-permissions",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Skill","arg":"update-config","state":"done"},
      {"type":"tool","name":"Bash","arg":"ls -la .claude/","state":"done"},
      {"type":"text","text":"No existing `.claude/` directory."},
      {"type":"text","text":"I'll design the hook, pipe-test the"},
      {"type":"text","text":"command, then write the settings file."},
      {"type":"tool","name":"Write","arg":".claude/settings.json","state":"done"},
  ],[0,90,140,175,205,235,265], mascot="off")),
  [{"at":0.05,"event":"Ask types"},{"at":0.4,"event":"'update-config' — the wrong skill"},{"at":0.85,"event":"Write settings.json"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. A plugin is not a word Claude knows until the plugin tells it. Hookify is a plugin — its own file format, its own rule shape. "
  "Without its SKILL on disk, Claude reaches for the nearest hook it does know. Same sentence, same model — the SKILL.md is the difference between a working rule and a plausible guess.",
  "BrutalistHesitantWriter — 'plausible' reconsidered into 'wrong'",
  R("BrutalistHesitantWriter", writer("Claude knows hooks.\nSo it guesses.\nHookify is not a hook — it is a plugin.\nThe SKILL.md is the difference.","plausible","wrong",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.5,"event":"'plausible' → 'wrong'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Hookify: a Claude Code plugin whose rules are files, not code — one markdown file per rule. "
  "Hookify rule: a markdown file with YAML frontmatter, saved at dot-claude slash hookify dot the-name dot local dot md. "
  "SKILL.md: the plugin's own instruction sheet — Claude reads it before writing a rule. "
  "PreToolUse hook: the native Claude Code feature, wired in settings.json, that Claude reaches for when it hasn't read the plugin's SKILL.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"hookify","meaning":"a Claude Code plugin whose rules are files, not code — one per rule"},
      {"term":"hookify rule","meaning":"a markdown file with YAML frontmatter at .claude/hookify.<name>.local.md"},
      {"term":"SKILL.md","meaning":"the plugin's instruction sheet — Claude reads it before writing a rule"},
      {"term":"PreToolUse hook","meaning":"the native CC feature in settings.json — the nearby wrong answer"}],
    "startCue":10,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare run. Sixteen lines of JSON at dot-claude slash settings dot json — not a hookify rule at all. Zero name-colon lines. It's a native PreToolUse hook, matcher for Edit and Write, "
  "a shell one-liner that pipes through jq. Ran the pipe-tests, validated the schema — and then tried to write a dot-env file to prove it worked, and the write went through. "
  "The hook didn't fire because settings was written mid-session and the watcher wasn't watching yet. Wrong file format. Wrong path. Not the plugin.",
  "CCSession — wc, no name-colon, live proof not blocked",
  R("CCSession", session("hookify — bare","default",[
      {"type":"prompt","text":"!wc -l .claude/settings.json","cue":0,"typeDuration":36},
      {"type":"text","text":"      16 .claude/settings.json"},
      {"type":"prompt","text":"!grep -c '^name:' .claude/settings.json","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!head -3 .claude/settings.json","cue":0,"typeDuration":34},
      {"type":"text","text":"{"},
      {"type":"text","text":"  \"$schema\": \"https://json…\","},
      {"type":"text","text":"  \"hooks\": { \"PreToolUse\": [ …"},
  ],[0,45,90,130,160,200,225,250], mascot="off")),
  [{"at":0.05,"event":"wc → 16"},{"at":0.35,"event":"^name: → 0"},{"at":0.75,"event":"JSON, not markdown"}])

B("B02","THE SKILL.MD","SHELL",LIAM,
  "Now stage the plugin's SKILL. Copy the hookify writing-rules SKILL.md into dot-claude slash skills slash writing-rules — the SKILL.md is what Claude reads. "
  "It says: rules are markdown files with YAML frontmatter at dot-claude slash hookify dot the-name dot local dot md. Required — name, enabled, event. A pattern regex, or a conditions list. And a message body Claude reads when the rule triggers. "
  "Same one-sentence ask. This time the SKILL is on disk.",
  "CCPlainShell — cp SKILL.md into place, wc, grep the required fields",
  R("CCPlainShell",{"title":"zsh — scratch/skill","lines":[
      "$ cp hookify/skills/writing-rules/SKILL.md \\",
      "     .claude/skills/writing-rules/",
      "$ wc -l .claude/skills/writing-rules/SKILL.md",
      "     374 .claude/skills/writing-rules/SKILL.md",
      "$ grep -E '^\\*\\*(name|enabled|event)' SKILL.md",
      "**name** (required): Unique identifier for the rule",
      "**enabled** (required): Boolean to activate/deactivate",
      "**event** (required): Which hook event to trigger on"],
    "startCue":10,"lineGap":22}, motion="type",
    leaves_terminal_because="the SKILL.md is a file on disk read before any session; not itself a session"),
  [{"at":0.05,"event":"cp SKILL.md"},{"at":0.45,"event":"grep the required fields"}])

B("B03","SKILL — THE RUN","TERMINAL",LIAM,
  "Same sentence. This time Claude launches the plugin's own skill — writing-rules, not update-config — because the SKILL is on disk. "
  "It writes one file, at the right path — dot-claude slash hookify dot block-env-file-edits dot local dot md. YAML frontmatter, event file, action block, conditions with a regex on file underscore path. Message body underneath.",
  "CCSession — the skill run: Skill launch, one Write at the right path",
  R("CCSession", session("hookify — skill","bypass-permissions",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Skill","arg":"writing-rules","state":"done"},
      {"type":"tool","name":"Bash","arg":"ls -la .claude/","state":"done"},
      {"type":"text","text":"total 0"},
      {"type":"text","text":"drwxr-xr-x  skills/"},
      {"type":"tool","name":"Write","arg":".claude/hookify.block-env-file-edits.local.md","state":"done"},
  ],[0,80,120,155,175,220], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.35,"event":"'writing-rules' — the right skill"},{"at":0.85,"event":"Write at the hookify path"}])

B("B04","SKILL — VERIFY","TERMINAL",LIAM,
  "Check the skill run. Twenty-one lines. Frontmatter reads name block-env-file-edits, enabled true, event file, action block. One name-colon line. The pattern regex, tested with Python's re, matches slash dot-env dot production. "
  "And the schema checker — a script I wrote that parses the frontmatter and validates the filename — passes. Same model, same sentence. The difference is which SKILL was on disk.",
  "CCSession — wc, head, check_rule PASS, re.search match",
  R("CCSession", session("hookify — skill","default",[
      {"type":"prompt","text":"!wc -l hookify.*.local.md","cue":0,"typeDuration":42},
      {"type":"text","text":"      21 hookify.block-env-…local.md"},
      {"type":"prompt","text":"!head -5 hookify.*.local.md","cue":0,"typeDuration":44},
      {"type":"text","text":"---"},
      {"type":"text","text":"name: block-env-file-edits"},
      {"type":"text","text":"enabled: true"},
      {"type":"text","text":"event: file"},
      {"type":"prompt","text":"!python3 check_rule.py hookify.*.local.md","cue":0,"typeDuration":56},
      {"type":"text","text":"PASS: hookify rule 'block-env-…"},
  ],[0,60,105,145,155,175,195,235,275], mascot="off")),
  [{"at":0.05,"event":"wc → 21"},{"at":0.3,"event":"head → frontmatter"},{"at":0.85,"event":"check_rule → PASS"}])

B("B05","THE PATTERN, TESTED","TERMINAL",LIAM,
  "Take the pattern the skill run produced — parens caret pipe forward-slash close-paren dot env dot brackets and hyphen, close bracket, plus, close paren, question mark, dollar. "
  "Python's re dot search finds a match at slash dot-env dot production. That is the difference between a rule that fires on the paths that matter, and a settings dot json that doesn't fire at all.",
  "CCSession — re.search against three paths",
  R("CCSession", session("hookify — skill","default",[
      {"type":"prompt","text":"!python3 -c \"re.search(P, '.env')\"","cue":0,"typeDuration":54},
      {"type":"text","text":"<re.Match match='.env'>"},
      {"type":"prompt","text":"!python3 -c \"re.search(P, '/a/.env.prod')\"","cue":0,"typeDuration":62},
      {"type":"text","text":"<re.Match match='/.env.prod'>"},
      {"type":"prompt","text":"!python3 -c \"re.search(P, 'env-var.txt')\"","cue":0,"typeDuration":58},
      {"type":"text","text":"None"},
  ],[0,120,180,250,310,370], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":".env — match"},{"at":0.45,"event":".env.production — match"},{"at":0.85,"event":"env-var.txt — no match"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, one difference — the SKILL.md on disk. "
  "Claude did the bare run; the handoff was is-this-hookify — and it wasn't; a native settings.json, and its own live proof wasn't blocked. "
  "Step three, the dangerous middle: Claude launched a nearby skill — update-config — and everything after that was internally consistent with the wrong abstraction. "
  "Then the real work, mine: cp the SKILL.md into place. Claude did the skill run; handoff met — check_rule passes, filename is right, frontmatter has the required fields. "
  "Interpretive judgment: the pattern is a regex, and it matches the paths I care about — I ran re.search, not Claude. Tool orchestration, zero — no plan mode, no subagents. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · one SKILL.md","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, one difference: SKILL on disk"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 16-line settings.json; live proof passed","handoff":"check_rule PASSes","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Wrong skill launched: update-config","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"cp SKILL.md into .claude/skills/","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Skill: 21-line hookify.<name>.local.md","handoff":"check_rule PASSes; frontmatter complete","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Pattern hits .env.prod, misses env-var.txt","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide which plugin this is — hookify is a word, not a hook. I must put the SKILL.md where Claude will find it. "
  "I must run the pattern against the paths I care about — a passing schema check doesn't prove the regex catches what I meant. Claude can guess a nearby hook — it will. "
  "It can launch the right skill when the SKILL is on disk. It should write to the file path the SKILL names. It should refuse to invent a schema that isn't in the SKILL. One line. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"guess a nearby hook — it will"},{"tier":"CAN","text":"launch the skill on disk"},
                          {"tier":"SHOULD","text":"write to the path the SKILL names"},{"tier":"SHOULD","text":"refuse to invent a schema"}],
                    "human":[{"tier":"MUST","text":"pick the plugin — not a hook"},{"tier":"MUST","text":"put the SKILL on the path"},
                             {"tier":"MUST","text":"test the pattern on real paths"},{"tier":"SHOULD","text":"read the SKILL before you ask"}],
                    "closing":"One SKILL.md. One line copied. The difference in the diff.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence, no SKILL on disk: sixteen lines of JSON at settings dot json, the wrong hook, the live proof unblocked. "
  "Same sentence, SKILL on disk: twenty-one lines at dot-claude slash hookify dot the-name dot local dot md — the right filename, the right frontmatter, a regex that matches the paths that matter. "
  "The difference is one copied file. What would prove this reel wrong: a bare run that reads a SKILL it wasn't shown.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Bare — no SKILL: 16-line settings.json, wrong path, live proof passed.",
      "Skill — SKILL on disk: 21-line hookify.<name>.local.md, right shape.",
      "Same sentence, same model. The difference is the SKILL on disk.",
      "FALSIFIABLE: a bare run that reads a SKILL it wasn't shown."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next plugin task, open Claude Code and paste this: Read the plugin's SKILL.md at dot-claude slash skills slash the-skill slash SKILL dot md and quote the required frontmatter fields. Then write me one example rule, using the exact filename convention the SKILL names. Don't run anything yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Read the plugin's SKILL.md at .claude/skills/<skill>/SKILL.md and quote the required frontmatter fields. Then write me one example rule, using the exact filename convention the SKILL names. Don't run anything yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,TITLE+". Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same sentence, one SKILL.md. The difference is in the diff.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-writing-rules (the concept; the card body replaced by two real runs)",
    "sources":["SESSION.md (two real runs)","anthropics/claude-code/plugins/hookify/skills/writing-rules/SKILL.md","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
