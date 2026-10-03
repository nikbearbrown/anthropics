#!/usr/bin/env python3
"""author_sheet.py — cc-command-development (cc-explainer · Claude Code 101 · tier 03)
"A Slash Command Is a Spec, Not a Shortcut." Every block traces to SESSION.md (two real headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-command-development"; TITLE="A Slash Command Is a Spec, Not a Shortcut."; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="/review-v1"
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

B("B00","COLD OPEN — V1","TERMINAL",LIAM,
  "This is Liam, in for Bear. Same repo, one small file with planted bugs, one slash command. Watch what pours out — ninety-two lines Claude decided on its own. "
  "Three severity emoji, twelve code blocks, a summary table, and a closing question. All from three sentences in a Markdown file.",
  "CCSession — review-v1 running: the ask, two Reads, an essay pouring out",
  R("CCSession", session("review-v1 — bare prose","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":40},
      {"type":"tool","name":"Bash","arg":"pwd && ls -la","state":"done"},
      {"type":"tool","name":"Read","arg":"inventory.py","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"text","text":"# Python Code Review —"},
      {"type":"text","text":"`inventory.py`"},
      {"type":"text","text":"Found 6 issues across bugs"},
      {"type":"text","text":"and security concerns."},
      {"type":"text","text":"## 🔴 CRITICAL — Security"},
      {"type":"text","text":"1. SQL injection (line 14)"},
      {"type":"text","text":"… 82 more lines, a table, …"},
      {"type":"text","text":"Want me to apply the fixes?"},
  ],[0, 30, 60, 90, 130, 160, 200, 230, 270, 310, 380, 450], mascot="off")),
  [{"at":0.05,"event":"The ask lands"},{"at":0.5,"event":"The essay begins"},{"at":0.9,"event":"Ends on a question"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea. A slash command isn't a shortcut and it isn't for you. It's the instruction Claude reads — the words you write are the spec for the output. "
  "Say what to look for and how the output should look. Same input, same shape, every run.",
  "BrutalistHesitantWriter — 'shortcut' reconsidered into 'spec'",
  R("BrutalistHesitantWriter", writer("A slash command is a shortcut.\nIt IS the instruction Claude reads.\nThe words you write ARE the spec.\nSame input, same shape — every run.","shortcut","spec",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'shortcut' → 'spec'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words. A slash command is a Markdown file whose text becomes Claude's next instruction. "
  "Dot-claude-slash-commands: the project folder — every .md here becomes one command. "
  "Frontmatter: YAML at the top — description, allowed-tools, and an argument hint. "
  "Allowed-tools: what the command intends to use — Read, Grep, or Bash fenced to git. "
  "Dollar-arguments, or dollar-one: everything typed after the slash name; dollar-one grabs the first argument.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"slash command","meaning":"a Markdown file whose text becomes Claude's next instruction"},
      {"term":".claude/commands/","meaning":"the project folder; every .md here becomes one command"},
      {"term":"frontmatter","meaning":"YAML at the top — description, allowed-tools, argument-hint"},
      {"term":"allowed-tools","meaning":"which tools the command intends to use, e.g. Read, Grep"},
      {"term":"$ARGUMENTS / $1","meaning":"everything typed after /name; $1 grabs the first argument"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","V1 — VERIFY","TERMINAL",LIAM,
  "Count it. Ninety-two lines. Three emoji — one red, one orange, one yellow — because Claude picked three severity buckets on its own. "
  "Twenty-four code-fence lines: twelve code blocks. Two question marks. Ends on a question — want me to apply the fixes? "
  "A markdown essay in the style Claude decided a review should be.",
  "CCSession — Liam's checks against v1's output: wc, grep, tail",
  R("CCSession", session("review-v1 — verify","default",[
      {"type":"prompt","text":"!wc -l out-v1.md","cue":0,"typeDuration":32},
      {"type":"text","text":"      92 out-v1.md"},
      {"type":"prompt","text":"!grep -c '🔴' out-v1.md","cue":0,"typeDuration":40},
      {"type":"text","text":"1"},
      {"type":"prompt","text":"!grep -c '```' out-v1.md","cue":0,"typeDuration":40},
      {"type":"text","text":"24"},
      {"type":"prompt","text":"!tail -1 out-v1.md","cue":0,"typeDuration":32},
      {"type":"text","text":"Want me to apply the fixes?"},
  ],[0, 40, 80, 140, 180, 250, 320, 400], mascot="off")),
  [{"at":0.05,"event":"wc → 92"},{"at":0.4,"event":"grep emoji → 1 red"},{"at":0.85,"event":"the closing question"}])

B("B02","THE REWRITE — V1 → V2","TERMINAL",LIAM,
  "Rewrite the file. Three sentences out — the message-to-user prose. Frontmatter in: description, allowed-tools, argument-hint. "
  "Then the instructions themselves — read every .py at dollar-arguments, list each bug as path colon line, dash severity, dash description, "
  "and end with a one-line count. Same slash name — different spec for the output shape.",
  "CCDiff — .claude/commands/review.md, v1 → v2",
  R("CCDiff",{"file":".claude/commands/review.md","addCount":11,"delCount":3,"lines":[
      {"gutter":"-","kind":"del","text":"This command reviews Python code…"},
      {"gutter":"-","kind":"del","text":"You will receive a report…"},
      {"gutter":"-","kind":"del","text":"…severity ratings and suggested fixes."},
      {"gutter":"+","kind":"add","text":"---"},
      {"gutter":"+","kind":"add","text":"description: Review every .py …"},
      {"gutter":"+","kind":"add","text":"allowed-tools: Read, Glob, Grep"},
      {"gutter":"+","kind":"add","text":"argument-hint: [path]"},
      {"gutter":"+","kind":"add","text":"---"},
      {"gutter":"+","kind":"add","text":"Read every .py at $ARGUMENTS."},
      {"gutter":"+","kind":"add","text":"Output: path:line — SEV — desc"},
      {"gutter":"+","kind":"add","text":"End with a one-line count."},
  ]}, motion="type", leaves_terminal_because="the diff is a file rewrite; it lives in the editor, not the session"),
  [{"at":0.05,"event":"Three deletions"},{"at":0.4,"event":"Frontmatter added"},{"at":0.85,"event":"The format spec"}])

B("B03","V2 — RUN","TERMINAL",LIAM,
  "Run it. Same tool calls — find, then Read. But the output. Five rows in the exact format the file asked for: file, colon, line, dash, severity, dash, one-sentence description. "
  "Then a blank line, then five issues found. No essay. No emoji. No follow-up question. The file was the spec, and Claude produced the spec's shape.",
  "CCSession — review-v2 running: find, Read, five rows, count",
  R("CCSession", session("review-v2 — imperative","accept-edits",[
      {"type":"prompt","text":"/review-v2","cue":0,"typeDuration":40},
      {"type":"tool","name":"Bash","arg":"find . -name '*.py'","state":"done"},
      {"type":"tool","name":"Read","arg":"inventory.py","state":"done"},
      {"type":"text","text":"inventory.py:6 — HIGH — Mutable"},
      {"type":"text","text":"inventory.py:14 — HIGH — SQL"},
      {"type":"text","text":"inventory.py:30 — MED — bare"},
      {"type":"text","text":"inventory.py:35 — LOW — slice"},
      {"type":"text","text":"inventory.py:39 — HIGH — shell"},
      {"type":"text","text":"5 issues found."},
  ],[0, 30, 70, 130, 170, 210, 250, 290, 360], mascot="off")),
  [{"at":0.05,"event":"Same ask, different file"},{"at":0.5,"event":"Rows land in the spec's format"},{"at":0.9,"event":"'5 issues found.'"}])

B("B04","V2 — VERIFY","TERMINAL",LIAM,
  "Count it. Six lines against ninety-two. Zero emoji. Zero code fences. Ends on the count line — five issues found. "
  "Same repo, same bugs, same model. Every line I got back is a line I asked for.",
  "CCSession — Liam's checks against v2's output",
  R("CCSession", session("review-v2 — verify","default",[
      {"type":"prompt","text":"!wc -l out-v2.md","cue":0,"typeDuration":32},
      {"type":"text","text":"       6 out-v2.md"},
      {"type":"prompt","text":"!grep -c '🔴' out-v2.md","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!grep -c '```' out-v2.md","cue":0,"typeDuration":40},
      {"type":"text","text":"0"},
      {"type":"prompt","text":"!tail -1 out-v2.md","cue":0,"typeDuration":32},
      {"type":"text","text":"5 issues found."},
  ],[0, 40, 80, 140, 180, 240, 300, 380], mascot="off")),
  [{"at":0.05,"event":"wc → 6"},{"at":0.35,"event":"grep emoji → 0"},{"at":0.85,"event":"count line"}])

B("B05","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence — what a good review shape is. Claude did the bare run — ninety-two lines Claude picked. "
  "The dangerous middle: I could have called that done. Step three, mine: read the output and see it's an essay, not a scannable list. "
  "Step four, mine: rewrite — frontmatter, imperative body, format spec. Step five, Claude's: five rows, no chrome, ends on the count. "
  "Step six, mine: notice the fifth bug is one I asked for, not one Claude added on its own.",
  "CCBoondoggleScore — six steps, dangerousMiddle at 2",
  R("CCBoondoggleScore",{"system":"one repo, two commands","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence: what good review shape is"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare command: 92-line essay Claude picked","handoff":"output matches the file's spec","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read output: essay, not a scannable list","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Rewrite: frontmatter + imperative body","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"New command: 5 rows, ends on the count","handoff":"spec followed exactly, nothing added","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Judged: the fifth bug is one I asked for","dependsOn":[5]},
  ],"dangerousMiddle":2,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.3,"event":"Step 2 rings"},{"at":0.9,"event":"Tally"}])

B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name the output shape myself — nobody else can. I must spec the format, not the topic. I must read what Claude decided, and see it. "
  "Should: put the format IN the file, not in my head. Claude can fill silence with its default style; it can run the tools and list the bugs. "
  "Should: follow the file's spec exactly, and not add what wasn't asked for. Nine lines of Markdown decide the shape.",
  "CCHumanLedger — four MUST/SHOULD, four CAN/SHOULD",
  R("CCHumanLedger",{"ai":[
      {"tier":"CAN","text":"fill silence with default style"},
      {"tier":"CAN","text":"run the tools, list the bugs"},
      {"tier":"SHOULD","text":"follow the file's spec exactly"},
      {"tier":"SHOULD","text":"not add what wasn't asked for"}],
                    "human":[
      {"tier":"MUST","text":"name the output shape myself"},
      {"tier":"MUST","text":"spec the format, not the topic"},
      {"tier":"MUST","text":"read what Claude decided"},
      {"tier":"SHOULD","text":"put the format IN the file"}],
                    "closing":"The spec is the file. That's the whole trick.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One command, two files. The first — three sentences of prose about what the command will do — produced ninety-two lines of Claude's default essay style, "
  "six findings including one Claude added on its own. The second — frontmatter plus imperative instructions plus a format spec — produced six lines: five rows in the shape I asked for, and a count line. "
  "What would prove this reel wrong: an imperative command that still gave back an emoji essay.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "One command, two files: 92 lines of essay against 6 lines of spec.",
      "Same repo, same bugs — different output, because the file was different.",
      "v2 didn't add the float bug — that's the point: it produced the spec, nothing more.",
      "FALSIFIABLE: an imperative command that still returns an emoji essay."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Take your last slash command — or write your first — and rewrite it as a spec. Frontmatter first: description, argument-hint, allowed-tools. "
  "Then the imperative body: what to read, what to look for, and the exact shape of the output. Test it on one file. Show me the diff.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Take one slash command in .claude/commands/ (or write your first) and rewrite it as a spec: frontmatter with description, argument-hint, allowed-tools; then an imperative body saying what to read, what to look for, and the exact shape of the output. Test it on one file. Show me the diff.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"A Slash Command Is a Spec, Not a Shortcut. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same repo, same bugs. Rewrite the file, and the output changes shape.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"03-hooks-skills-commands","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-command-development (the concept; the card body replaced by two real headless runs)",
    "sources":["SESSION.md (two real /review-v1 and /review-v2 runs)","anthropics/claude-code/plugins/plugin-dev/skills/command-development/SKILL.md","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
