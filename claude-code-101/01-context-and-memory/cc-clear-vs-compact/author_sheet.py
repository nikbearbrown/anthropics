#!/usr/bin/env python3
"""author_sheet.py — cc-clear-vs-compact (cc-explainer · Claude Code 101 · tier 01, film 05)
"/clear vs /compact: What Each One Throws Away." Every block traces to SESSION.md (messages 9–11 of one real session). Liam, in for Bear."""
import json, os
SLUG="cc-clear-vs-compact"; TITLE="/clear vs /compact: What Each One Throws Away"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="What did we build in this session? One line per command."
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

B("B00","COLD OPEN — /compact","TERMINAL",LIAM,
  "This is Liam, in for Bear. Last film ended at forty-nine and a half thousand tokens of context that never goes down on its own. Two commands make it go down: slash clear and slash compact. "
  "They are not the same command, and the difference is what each one throws away. Slash compact first. Fifty-seven seconds. "
  "Forty-nine thousand seven hundred tokens of conversation become six thousand one hundred.",
  "CCSession — /compact; the product's status events; the boundary numbers",
  R("CCSession", session("gradebook · message 9","default",[
      {"type":"prompt","text":"/compact","cue":0,"typeDuration":24},
      {"type":"text","text":"status: compacting"},
      {"type":"text","text":"compact_result: success"},
      {"type":"text","text":"compact_boundary · trigger: manual"},
      {"type":"text","text":"pre_tokens: 49713"},
      {"type":"text","text":"post_tokens: 6100"},
      {"type":"text","text":"duration_ms: 57048"},
  ],[0,50,150,190,215,240,265])),
  [{"at":0.05,"event":"/compact types"},{"at":0.4,"event":"compacting… success"},{"at":0.8,"event":"49,713 → 6,100"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. The progress is not in the chat; it's in the code on disk and the files you wrote. Slash clear throws the whole transcript away and starts from the system prompt again. "
  "Slash compact replaces the transcript with a summary. I ran both on the same session and asked the same question after each, and the receipts tell you exactly what each one kept.",
  "BrutalistHesitantWriter — 'chat' reconsidered into 'code'",
  R("BrutalistHesitantWriter", writer("The progress is in the chat.\n/clear throws the transcript away;\n/compact keeps a summary.\nEither way, the code on disk stays.","chat","code",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.15,"event":"'chat' → 'code'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Slash compact: replaces the conversation so far with a summary the model writes; the files on disk are untouched. Slash clear: starts a fresh conversation; nothing from the chat survives, everything on disk does. "
  "Transcript: the chat itself — your messages, its answers, every tool result. Summary: what compact keeps — a short account of what happened, written by the model. On disk: the code, the tests, CLAUDE.md, git — the state that outlives the chat.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"/compact","meaning":"replaces the conversation so far with a summary the model writes; disk untouched"},
      {"term":"/clear","meaning":"starts a fresh conversation; nothing from the chat survives, everything on disk does"},
      {"term":"transcript","meaning":"the chat itself — your messages, its answers, every tool result"},
      {"term":"summary","meaning":"what compact keeps: a short account of what happened, written by the model"},
      {"term":"on disk","meaning":"the code, the tests, CLAUDE.md, git — the state that outlives the chat"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","AFTER COMPACT","TERMINAL",LIAM,
  "Same question as message eight: what did we build. After compact it answers from the summary — the same five items, in the same order, in slightly different words. "
  "Thirty-six thousand seven hundred tokens read, down from forty-nine and a half. The fixed part — system prompt, tools, CLAUDE.md — is about thirty thousand and never moves. The conversation itself went from forty-nine thousand to six.",
  "CCSession — message 10: the question; five lines from the summary; 36.7k",
  R("CCSession", session("gradebook · message 10","default",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"text","text":"- `rename OLD NEW` — moves a student's"},
      {"type":"text","text":"  scores to a new name, with guards …"},
      {"type":"text","text":"- `top N` — prints the N students with the"},
      {"type":"text","text":"  highest average, sorted descending."},
      {"type":"text","text":"- `export` — writes `grades.csv` …"},
      {"type":"text","text":"- `stats NAME` — count, mean, min, max …"},
      {"type":"text","text":"- `session()` refactor — a `contextmanager`"},
      {"type":"status","verb":"Reading","elapsed":"0m 09s","tokens":"36.7k tokens"},
  ],[0,80,95,115,130,150,170,190,240], mascot="off")),
  [{"at":0.05,"event":"The same question"},{"at":0.4,"event":"Five lines from the summary"},{"at":0.85,"event":"36.7k read"}])

B("B02","CLEAR — A FRESH SESSION","TERMINAL",LIAM,
  "Now the same question in a brand-new session — that's what slash clear gives you. Twenty-eight thousand seven hundred read: the fixed part and nothing else. It has no memory of the session at all. "
  "So how does it answer? It runs git diff. Twice. And reads the answer off the disk — every command, plus the tests, which the summary-based answer had left out. The progress was never in the chat.",
  "CCSession — a new session: the question; two git diffs; the answer from disk; 28.7k",
  R("CCSession", session("gradebook — new session","default",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":60},
      {"type":"tool","name":"Bash","arg":"git diff src/gradebook.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"git diff tests/test_gradebook.py","state":"done"},
      {"type":"text","text":"Here's what was built in this session:"},
      {"type":"text","text":"- `rename OLD NEW` — rename a student …"},
      {"type":"text","text":"- `top N` — print the top N students …"},
      {"type":"text","text":"- `stats NAME` — print count/mean/min/max …"},
      {"type":"text","text":"- `export` — write all students to CSV …"},
      {"type":"text","text":"- `session()` context manager — load once …"},
      {"type":"text","text":"- Tests added for each new command …"},
      {"type":"status","verb":"Reading","elapsed":"0m 15s","tokens":"28.7k tokens"},
  ],[0,80,105,140,160,175,190,205,220,235,270], mascot="off")),
  [{"at":0.05,"event":"Same question, no memory"},{"at":0.35,"event":"git diff, twice"},{"at":0.7,"event":"The answer from disk — tests included"}])

B("B03","VERIFY","SHELL",LIAM,
  "Check it. Before: forty-nine five. After compact: thirty-six seven. Fresh: twenty-eight seven, then thirty-two after it read the diff. And the disk: six tests, still green; the same hundred seventy-four lines added. "
  "Neither command touched the work. One kept a summary of the conversation; the other kept nothing of it — and found the work anyway, because the work was never in the conversation.",
  "CCPlainShell — the three receipts; tests; diff stat",
  R("CCPlainShell",{"title":"zsh — ~/gradebook","lines":[
      "$ python3 -c \"…turns.json…\"",
      "msg 8   (before)             49,530",
      "msg 10  (after /compact)     36,670",
      "fresh   (what /clear gives)  28,676  →  32,093 after two git diffs",
      "$ python3 tests/test_gradebook.py",
      "Ran 6 tests in 0.004s",
      "OK",
      "$ git diff --stat | tail -1",
      " 2 files changed, 174 insertions(+), 13 deletions(-)"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="receipts across two sessions and the disk; no single session screen shows them"),
  [{"at":0.05,"event":"49.5k · 36.7k · 28.7k"},{"at":0.55,"event":"6 tests OK"},{"at":0.85,"event":"174 lines, untouched"}])

B("B04","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: the same question three ways — before, after compact, after clear. Claude compacted: forty-nine thousand into six, in a minute; the handoff was the next answer still correct, and it was. "
  "Step three, the dangerous middle: reading the two answers side by side — the summary answer had quietly dropped the tests. Claude, fresh, rebuilt the picture from git diff; handoff met, tests included. "
  "Then interpretive judgment: which command for which moment — compact when the why still matters, clear when it doesn't. Tool orchestration: git is the memory I trust. Executive integration, zero.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one question · before, compact, clear","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One question: before, compact, clear"},
      {"n":2,"phase":"C","labor":"claude","text":"/compact: 49,713 → 6,100 in 57 s","handoff":"the next answer is still correct","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read both answers: summary dropped the tests","dependsOn":[2]},
      {"n":4,"phase":"B","labor":"claude","text":"Fresh: git diff ×2, answer from disk","handoff":"every command named; tests included","dependsOn":[1]},
      {"n":5,"phase":"H","labor":"human","capacity":"IJ","text":"Compact when the why matters; clear when not","dependsOn":[3]},
      {"n":6,"phase":"I","labor":"human","capacity":"TO","text":"git is the memory I trust, not the chat","dependsOn":[4]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B05","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must know where the progress lives — on disk, in git, in the files I wrote. I must clear between unrelated tasks, and compact when the why of the last one still matters. "
  "I should read the summary compact wrote before trusting it. Claude can summarize forty-nine thousand tokens into six in a minute. It can rebuild the picture from git diff. "
  "It should say when it's answering from a summary — it didn't. It should leave the disk untouched — it did. The chat is scaffolding. The building is on disk.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"summarize 49k into 6k in a minute"},{"tier":"CAN","text":"rebuild the picture from git diff"},
                          {"tier":"SHOULD","text":"say it's answering from a summary"},{"tier":"SHOULD","text":"leave the disk untouched — it did"}],
                    "human":[{"tier":"MUST","text":"know where progress lives: on disk"},{"tier":"MUST","text":"clear between unrelated tasks"},
                             {"tier":"MUST","text":"compact when the why still matters"},{"tier":"SHOULD","text":"read the summary before trusting"}],
                    "closing":"The chat is scaffolding. The building is on disk.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Slash compact turned forty-nine thousand seven hundred tokens of conversation into a six-thousand-token summary in fifty-seven seconds, and the next answer came from the summary. "
  "A fresh session — what slash clear gives you — started at twenty-eight thousand, ran git diff twice, and answered from the disk, tests included. Neither touched the work: six tests green, the same hundred seventy-four lines. "
  "What would prove this reel wrong: a fresh session that cannot recover what was built from the disk.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "/compact: 49,713 tokens of conversation → a 6,100-token summary in 57 s; the next answer came from the summary.",
      "/clear (a fresh session): 28,676 read, no memory — git diff twice, and the answer came from the disk, tests included.",
      "Neither touched the work: six tests green, the same 174 lines added. The progress was never in the chat.",
      "FALSIFIABLE: a fresh session that cannot recover what was built from the disk."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Next time a session feels heavy, type slash context and read the Messages row. If the next task needs the why of what you just did, type slash compact, then read the summary it wrote. "
  "If it doesn't, type slash clear — then paste this: What changed in this folder today, and how do you know? Watch it find out from git.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"What changed in this folder today, and how do you know?",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"after /clear, paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Slash clear versus slash compact: What Each One Throws Away. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"One question, three ways: before, after /compact, after /clear. The work was never in the chat.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"01-context-and-memory","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/01-context-and-memory/claude-code--claude-liam-clear-vs-compact (the concept; the card body replaced by messages 9–11 of a real session)",
    "sources":["SESSION.md (messages 9–11 of one real session)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
            if len(st["text"])>44: print("  ⚠ step",len(st["text"]),st["text"])
