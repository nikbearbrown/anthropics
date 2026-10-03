#!/usr/bin/env python3
"""author_sheet.py — cc-pattern-analysis-subagent (cc-explainer · Claude Code 101 · tier 02, subagents)
"Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code." Every block traces to SESSION.md (two real fresh headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-pattern-analysis-subagent"
TITLE="Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code"
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="For the binary-search rubric, find the top three misconceptions the batch is showing. Write them to feedback_focus.md."
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

B("B00","COLD OPEN — INLINE","TERMINAL",LIAM,
  "This is Liam, in for Bear. One ask, one folder — five student answers to the binary-search rubric, and a request for the top three things the batch is getting wrong. "
  "Watch what Claude reads. The rubric. Every submission. All five of them, one after another. Every student's answer is now sitting in the main session's window. "
  "Eight reads to answer a question about a batch that has nothing to do with the build I'm going to make next.",
  "CCSession — the inline run: the ask, Read rubric, Read five submissions, Write",
  R("CCSession", session("grading — inline","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":72},
      {"type":"tool","name":"Read","arg":"rubric.md","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/01-mira.md","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/02-jules.md","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/03-priya.md","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/04-omar.md","state":"done"},
      {"type":"tool","name":"Read","arg":"submissions/05-tao.md","state":"done"},
      {"type":"tool","name":"Write","arg":"feedback_focus.md","state":"done"},
  ],[0,95,125,150,175,200,225,255], mascot="off")),
  [{"at":0.05,"event":"The ask types"},{"at":0.4,"event":"Five submissions land"},{"at":0.9,"event":"Write feedback_focus.md"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. A batch of student work is context-heavy — five, fifty, five hundred files that the build has no reason to remember. "
  "The right move isn't a smarter prompt. It's a subagent — its own Claude, its own window, its own three-tool whitelist — deployed once in a file, invoked per batch. "
  "The main session's tool sequence goes from eight reads and a write down to two: dispatch the subagent, write the summary it returns.",
  "BrutalistHesitantWriter — 'prompt' reconsidered into 'subagent'",
  R("BrutalistHesitantWriter", writer("A batch needs a bigger prompt.\nBigger — reads more, remembers more.\nEight reads, five in main context.\nA pattern-analyzer is a subagent.","prompt","subagent",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'prompt' → 'subagent'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Subagent: a separate Claude with its own context window and its own tool whitelist, invoked from the main session. "
  "YAML frontmatter: the fenced block at the top of a Markdown file — a name, a description, a tool list — that Claude Code reads as configuration. "
  "Tool whitelist: the exact list of tools that subagent is allowed to touch; anything else is refused. "
  "Main context: the tokens the main session is holding right now; every file it reads goes in here and stays.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"subagent","meaning":"a separate Claude with its own context and tool whitelist, called from the main session"},
      {"term":"YAML frontmatter","meaning":"the fenced block at the top of a Markdown file — machine-readable configuration"},
      {"term":"tool whitelist","meaning":"the exact tools this subagent may use; anything else is refused"},
      {"term":"main context","meaning":"the tokens the main session is holding now — every read goes in and stays"}],
    "startCue":12,"rowGap":52}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","INLINE — VERIFY","TERMINAL",LIAM,
  "Check the inline run against what I actually asked for. Five lines in the output — one more than I asked for; it added a title heading. "
  "Eight reads in the main session's history. And thirty-five thousand tokens landed in the main session's window — every submission, every criterion, now living in the same context as anything I do next.",
  "CCSession — wc, tool sequence, cache_creation",
  R("CCSession", session("grading — inline","default",[
      {"type":"prompt","text":"!wc -l feedback_focus.md","cue":0,"typeDuration":32},
      {"type":"text","text":"       5 feedback_focus.md"},
      {"type":"prompt","text":"!grep -c '^Read' history.txt","cue":0,"typeDuration":34},
      {"type":"text","text":"8"},
      {"type":"prompt","text":"!jq .usage.cache_creation_input_tokens","cue":0,"typeDuration":48},
      {"type":"text","text":"35572"},
      {"type":"text","text":"# every submission, in main context"},
  ],[0,44,80,130,165,215,250], mascot="off")),
  [{"at":0.05,"event":"wc → 5"},{"at":0.4,"event":"grep → 8 Reads"},{"at":0.85,"event":"35,572 tokens"}])

B("B02","THE DEPLOYMENT","SHELL",LIAM,
  "Here's the deployment — one Markdown file at a specific path, written by me before the next run. "
  "Dot-claude, agents, pattern-analyzer dot md. Thirty-nine lines. YAML frontmatter first — a name, a description of when to use it, and a tool whitelist: Read, Grep, Glob, and nothing else. "
  "Then a prompt for the subagent itself: scan submissions against the rubric, aggregate the batch, return three sections — common misconceptions, severity by criterion, recommended focus. Return only that block.",
  "CCPlainShell — cat .claude/agents/pattern-analyzer.md",
  R("CCPlainShell",{"title":"zsh — ~/grading","lines":[
      "$ cat .claude/agents/pattern-analyzer.md",
      "---",
      "name: pattern-analyzer",
      "description: Scans a batch of student submissions",
      "  in submissions/ against rubric.md — WITHOUT",
      "  loading a submission into the main session.",
      "tools: Read, Grep, Glob",
      "---",
      "# pattern-analyzer",
      "Return COMMON_MISCONCEPTIONS, SEVERITY_BY_CRITERION,",
      "and RECOMMENDED_FOCUS. Do not write files.",
      "$ wc -l .claude/agents/pattern-analyzer.md",
      "      39 .claude/agents/pattern-analyzer.md"],
    "startCue":10,"lineGap":20}, motion="type",
    leaves_terminal_because="the deployment file is read outside any session — it configures Claude Code, it is not spoken by it"),
  [{"at":0.05,"event":"cat starts"},{"at":0.35,"event":"tools whitelist"},{"at":0.85,"event":"39 lines"}])

B("B03","SUBAGENT — THE RUN","TERMINAL",LIAM,
  "Same ask, same folder — this time with the deployment file in place. "
  "The main session doesn't read a submission. It dispatches the pattern-analyzer subagent with one Task call. Inside its own window, the subagent Globs the folder and reads every submission — over there, not in here. "
  "It returns three findings and a short summary — and it says, out loud, that it can't write files because its whitelist doesn't include Write. So the main session writes feedback_focus.md itself. Two tool calls: dispatch, write.",
  "CCSession — the subagent run: Task, the summary landing, Write",
  R("CCSession", session("grading — subagent","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":72},
      {"type":"tool","name":"Task","arg":"pattern-analyzer","state":"done"},
      {"type":"text","text":"1. Students compute the midpoint as"},
      {"type":"text","text":"(lo + hi) // 2, unaware of overflow."},
      {"type":"text","text":"2. Students describe shrinking the"},
      {"type":"text","text":"range but state no loop invariant."},
      {"type":"text","text":"3. Complexity is incomplete or wrong."},
      {"type":"text","text":"Note: I do not have Write access."},
      {"type":"tool","name":"Write","arg":"feedback_focus.md","state":"done"},
  ],[0,95,145,170,195,220,245,275,305], mascot="off")),
  [{"at":0.05,"event":"Same ask"},{"at":0.35,"event":"Task pattern-analyzer"},{"at":0.75,"event":"Whitelist self-enforces"},{"at":0.95,"event":"Write"}])

B("B04","SUBAGENT — VERIFY","TERMINAL",LIAM,
  "Check it. Three lines in the output — one line per finding, no title, exactly what I asked for. "
  "Two tools in the main session's history: Task, and Write. Zero reads. And thirty-two thousand tokens in the main session's window — a little smaller than the inline run, but that's not the point. The point is what's inside those tokens. "
  "The five submissions are not. They lived in the subagent's window, and its window closed when it returned.",
  "CCSession — wc, tool sequence (Task, Write), cache_creation",
  R("CCSession", session("grading — subagent","default",[
      {"type":"prompt","text":"!wc -l feedback_focus.md","cue":0,"typeDuration":32},
      {"type":"text","text":"       3 feedback_focus.md"},
      {"type":"prompt","text":"!grep -oE 'Task|Write' history.txt","cue":0,"typeDuration":46},
      {"type":"text","text":"Task"},
      {"type":"text","text":"Write"},
      {"type":"prompt","text":"!jq .usage.cache_creation_input_tokens","cue":0,"typeDuration":48},
      {"type":"text","text":"31942"},
      {"type":"text","text":"# no submission in main context"},
  ],[0,44,80,130,155,185,235,270], mascot="off")),
  [{"at":0.05,"event":"wc → 3"},{"at":0.35,"event":"Task, Write"},{"at":0.75,"event":"31,942"},{"at":0.95,"event":"no submissions in main"}])

B("BFLOW","THE FLOW","DIAGRAM",LIAM,
  "Drawn out, the flow is this. The main session has the ask. It calls the Task tool, naming the pattern-analyzer subagent. "
  "The subagent opens its own window, with its own whitelist — Read, Grep, Glob — and reads the rubric and every submission in there. "
  "It returns one thing: a structured summary — under a thousand words — into the main session. The main session takes that summary and writes feedback_focus.md. The batch never crosses back.",
  "FlowDiagram — MAIN → TASK → SUBAGENT (Read/Grep/Glob) → SUMMARY → MAIN → WRITE",
  R("FlowDiagram",{"skin":"claude","kicker":"PATTERN-ANALYZER SUBAGENT","caption":"Two calls in main. All the reading, over there.",
      "pulse":True,
      "nodes":[
          {"id":"main","label":"MAIN","sub":"the build session","tier":"client","x":80,"y":460,"w":300,"h":160,"hi":True},
          {"id":"task","label":"TASK","sub":"dispatch call","tier":"edge","x":460,"y":460,"w":300,"h":160},
          {"id":"sub","label":"SUBAGENT","sub":"Read · Grep · Glob","tier":"compute","x":840,"y":320,"w":320,"h":180,"hi":True},
          {"id":"batch","label":"BATCH","sub":"rubric + 5 files","tier":"data","x":840,"y":600,"w":320,"h":160},
          {"id":"sum","label":"SUMMARY","sub":"~1k tokens back","tier":"data","x":1240,"y":460,"w":300,"h":160},
          {"id":"write","label":"WRITE","sub":"feedback_focus.md","tier":"compute","x":1600,"y":460,"w":260,"h":160,"hi":True},
      ],
      "edges":[
          {"from":"main","to":"task","order":1,"kind":"flow"},
          {"from":"task","to":"sub","order":2,"kind":"flow"},
          {"from":"batch","to":"sub","order":3,"kind":"data"},
          {"from":"sub","to":"sum","order":4,"kind":"reply"},
          {"from":"sum","to":"main","order":5,"kind":"flow","dashed":True},
          {"from":"main","to":"write","order":6,"kind":"flow"},
      ],
      "viewBox":{"w":1920,"h":1080}}, motion="drawon",
    leaves_terminal_because="BFLOW: the topology across two windows is not visible in either window; the terminal only shows Task then Write"),
  [{"at":0.05,"event":"MAIN"},{"at":0.35,"event":"TASK → SUBAGENT"},{"at":0.7,"event":"SUMMARY back"},{"at":0.9,"event":"WRITE"}])

B("BSHOW","THE OUTPUT — SHOWN","SHELL",LIAM,
  "And here it is — the actual file the subagent run wrote. Three lines, most severe first. Midpoint overflow. No loop invariant. Complexity omitted or wrong. "
  "That is what I take into next week's session. Not the five submissions; not the rubric. Three sentences.",
  "CCPlainShell — cat feedback_focus.md (the subagent run's output)",
  R("CCPlainShell",{"title":"zsh — ~/grading","lines":[
      "$ cat feedback_focus.md",
      "1. Students compute the midpoint as (lo + hi) // 2",
      "and treat it as the correct form, unaware it can",
      "overflow on large inputs.",
      "2. Students describe shrinking the range but do not",
      "state a loop invariant — that the target, if present,",
      "lies within [lo, hi) at every step.",
      "3. Students report complexity incompletely — omitting",
      "O(1) extra space, and one case wrong on Big-O.",
      "$ wc -l feedback_focus.md",
      "       3 feedback_focus.md"],
    "startCue":12,"lineGap":18}, motion="type",
    leaves_terminal_because="BSHOW: the produced artifact must be shown in the plain shell, not implied by the session"),
  [{"at":0.05,"event":"cat starts"},{"at":0.5,"event":"three findings"},{"at":0.95,"event":"3 lines"}])

B("B05","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: the one-sentence ask, and a rubric that names five criteria. "
  "Claude did the inline run — the handoff was a written feedback file; it wrote one, but eight reads landed in the main session. "
  "Step three, the dangerous middle: writing the deployment file. Thirty-nine lines with a whitelist of three tools, before any run. "
  "Claude did the subagent run; the handoff was two main-session tool calls, and that is what the trace shows. "
  "Interpretive judgment at the end: the subagent said its whitelist would not let it Write, and I let the main session write instead of loosening the whitelist. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one ask · five criteria","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Ask + rubric with five criteria"},
      {"n":2,"phase":"C","labor":"claude","text":"Inline: 8 Reads, 35,572 in main","handoff":"a feedback file, one finding per line","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the tool sequence: batch in main","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Deploy .claude/agents/pattern-analyzer.md","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Subagent: Task, Write — two calls","handoff":"summary in; batch out of main context","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Whitelist self-enforced; let it","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name what a batch is for — teaching focus for next week, not a graded artifact for right now. "
  "I must write the whitelist myself; nobody else can decide the tools this subagent should not touch. "
  "I must read the tool sequence, not the summary — that is where the receipt lives. I should reject a loosened whitelist when it self-enforces. "
  "Claude can dispatch a subagent by description alone — it did. It can honor a whitelist and say so — it did. It should return a structured summary, not full quotes — it did. It should not write when it has no Write — it didn't.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"dispatch subagent by description"},{"tier":"CAN","text":"honor a whitelist and say so"},
                          {"tier":"SHOULD","text":"return structured, not quotes"},{"tier":"SHOULD","text":"not write without Write access"}],
                    "human":[{"tier":"MUST","text":"name what the batch is for"},{"tier":"MUST","text":"write the whitelist myself"},
                             {"tier":"MUST","text":"read the tools, not the summary"},{"tier":"SHOULD","text":"reject a loosened whitelist"}],
                    "closing":"The deployment, made durable. 39 lines. Mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Inline run: eight reads, five submissions in main context, thirty-five thousand tokens the build has no reason to remember. "
  "Subagent run: one Task, one Write, and thirty-two thousand tokens with no submission in them — the batch lived over there. "
  "Deployment is one Markdown file: name, description, three-tool whitelist. The whitelist enforced itself: the subagent noticed it could not Write and said so; the main session wrote. "
  "What would prove this reel wrong: a subagent invocation whose main session Reads a batch file after the summary returns.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Inline: 8 Reads, 35,572 tokens in main, five submissions carried into the build session.",
      "Subagent: 1 Task, 1 Write, 31,942 tokens in main, no submission crossed back.",
      "Deployment is one Markdown file — name, description, Read/Grep/Glob whitelist. The whitelist enforced itself.",
      "FALSIFIABLE: a subagent invocation whose main session Reads a batch file after the summary returns."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next batch job — a pile of submissions, a folder of tickets, a stack of resumes — open Claude Code and paste this: "
  "Write me a subagent for triage. Ask me what the batch is, what the rubric or criterion file is, and what three-section structured summary I want back. Then write dot-claude, agents, triage dot md — YAML frontmatter, a Read-Grep-Glob whitelist, and the prompt. Don't dispatch it yet.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Write me a subagent for triage. Ask me what the batch is, what the rubric or criterion file is, and what three-section structured summary I want back. Then write .claude/agents/triage.md — YAML frontmatter, a Read-Grep-Glob whitelist, and the prompt. Don't dispatch it yet.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same ask, once inline and once through a deployed subagent. The main session's tool sequence goes from eight-reads-and-a-write to two calls.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"02-plan-rewind-subagents","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,"build":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-pattern-analysis-subagent (the concept card; body replaced by two real headless runs)",
    "sources":["SESSION.md (two real runs, 2026-09-09)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
        if len(r["props"]["lines"])>14: print("  ⚠ plain-shell lines",b["beat_id"],len(r["props"]["lines"]))
