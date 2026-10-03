#!/usr/bin/env python3
"""author_sheet.py — cc-context-cost (cc-explainer · Claude Code 101 · tier 01, film 04)
"Every Message Re-reads the Whole Session." Every block traces to SESSION.md (one real eight-message session). Liam, in for Bear."""
import json, os
SLUG="cc-context-cost"; TITLE="Every Message Re-reads the Whole Session"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
A1="Read src/gradebook.py and tell me in two sentences what it does."
A2="Add a \"rename OLD NEW\" command following the repo's conventions, with a test. Run the tests."
A8="What did we build in this session? One line per command."
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

B("B00","COLD OPEN — MESSAGE ONE","TERMINAL",LIAM,
  "This is Liam, in for Bear. There's a line going around: message thirty costs thirty-one times more, because every message re-reads the whole conversation. "
  "I wanted the receipt. So: one session, eight messages of real work — four new commands and a refactor on a small gradebook — and after every message I read the number the product prints: "
  "how many tokens went in. Message one: read the file, two sentences. Twenty-eight thousand tokens read, before I'd said anything real.",
  "CCSession — message one; the answer; the first receipt",
  R("CCSession", session("gradebook · message 1","default",[
      {"type":"prompt","text":A1,"cue":0,"typeDuration":70},
      {"type":"tool","name":"Read","arg":"src/gradebook.py","state":"done"},
      {"type":"text","text":"A tiny CLI gradebook that persists students"},
      {"type":"text","text":"and their scores to a `grades.json` file …"},
      {"type":"status","verb":"Reading","elapsed":"0m 07s","tokens":"28.4k tokens"},
  ],[0,90,130,150,200])),
  [{"at":0.05,"event":"Message one types"},{"at":0.5,"event":"Two sentences back"},{"at":0.85,"event":"28.4k tokens read"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Each message doesn't cost the same. Every message you send, the model re-reads the whole session from the top — your asks, its answers, every file it opened, every test it ran — before it reads your new line. "
  "So the context only grows. I ran eight messages of real work and read the receipt after each one. Then I checked whether it's really thirty-one times more.",
  "BrutalistHesitantWriter — 'same' reconsidered into 'more'",
  R("BrutalistHesitantWriter", writer("Each message costs the same.\nNo — each message re-reads the whole session.\nI ran eight and read the receipts.\nMessage eight read 49,530 tokens.","same","more",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'same' → 'more'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Context: everything the model has read this session — and it's sent again with every message. Token: the unit the model reads and writes; roughly three-quarters of a word. "
  "Input tokens: what one call read — the whole context, plus your new line. Cache: text the service has seen before and re-reads cheaply; most of a growing session is cache. "
  "Turn: one message from you, plus every tool call it takes to answer it.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"context","meaning":"everything the model has read this session — sent again with every message"},
      {"term":"token","meaning":"the unit the model reads and writes; roughly three-quarters of a word"},
      {"term":"input tokens","meaning":"what one call read: the whole context, plus your new line"},
      {"term":"cache","meaning":"text the service has seen before and re-reads cheaply; most of a growing session"},
      {"term":"turn","meaning":"one message from you, plus every tool call it takes to answer it"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","THE WORK — MESSAGES 2 TO 7","TERMINAL",LIAM,
  "Messages two to seven are the work: rename, top N, export, a refactor question, the refactor, stats. Each one reads files, edits two, runs the tests. Three tests, four, five, six. "
  "That's a real build, not a toy prompt. Now watch the number under each one.",
  "CCSession — message two's loop, then the test counts rising",
  R("CCSession", session("gradebook · messages 2–7","accept-edits",[
      {"type":"prompt","text":A2,"cue":0,"typeDuration":90},
      {"type":"tool","name":"Read","arg":"src/gradebook.py","state":"done"},
      {"type":"tool","name":"Edit","arg":"src/gradebook.py","state":"done"},
      {"type":"tool","name":"Edit","arg":"tests/test_gradebook.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 tests/test_gradebook.py","state":"done"},
      {"type":"text","text":"All 3 tests pass. Added `rename(old, new)`"},
      {"type":"text","text":"All 4 tests pass. Added `top(n)` …"},
      {"type":"text","text":"All 5 tests pass. … `export()` …"},
      {"type":"text","text":"All 5 tests still pass. … `session()` …"},
      {"type":"text","text":"All 6 tests pass. Added `stats(name)` …"},
  ],[0,100,125,150,175,205,235,260,285,310], mascot="off")),
  [{"at":0.05,"event":"Message two"},{"at":0.4,"event":"Read · Edit · Edit · tests"},{"at":0.7,"event":"3, 4, 5, 6 tests"}])

B("B02","THE RECEIPTS","SHELL",LIAM,
  "The receipt: tokens read at the first call of each message. Twenty-eight thousand before I'd said anything real — that's the system prompt, the tool list, CLAUDE.md. "
  "Twenty-nine. Thirty-two. Thirty-four. Thirty-eight. Forty-seven after the refactor — it wrote seven thousand tokens of code that turn, and every one of them is now re-read by every message after it. "
  "Forty-nine and a half thousand by message eight. It never went down. Nothing makes it go down unless you do.",
  "CCPlainShell — first-call context per message, from turns.json",
  R("CCPlainShell",{"title":"zsh — ~/evidence","lines":[
      "$ python3 -c \"…turns.json…\"   # tokens read at each message's first call",
      "msg 1   28,450",
      "msg 2   29,283",
      "msg 3   32,237",
      "msg 4   34,576",
      "msg 5   38,311",
      "msg 6   38,964     # the refactor: 7,897 tokens written this turn",
      "msg 7   47,283",
      "msg 8   49,530"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="a table read across eight resumed sessions' receipts; no single session screen shows it"),
  [{"at":0.05,"event":"msg 1 → 28,450"},{"at":0.55,"event":"msg 6 → 38,964; msg 7 → 47,283"},{"at":0.9,"event":"msg 8 → 49,530"}])

B("B03","MESSAGE EIGHT","TERMINAL",LIAM,
  "Message eight is one line: what did we build. The answer is a hundred and eighty-three tokens. To write it, the model read forty-nine thousand five hundred and thirty. "
  "One question, the whole session in front of it — the files, the diffs, six test runs, the refactor. That's the mechanism the line is about, and it's real.",
  "CCSession — the one-line question; the five-line answer; the receipt",
  R("CCSession", session("gradebook · message 8","default",[
      {"type":"prompt","text":A8,"cue":0,"typeDuration":60},
      {"type":"text","text":"- `rename OLD NEW` — moves a student's"},
      {"type":"text","text":"  scores to a new name …"},
      {"type":"text","text":"- `top N` — prints the N students with the"},
      {"type":"text","text":"  highest averages …"},
      {"type":"text","text":"- `export` — writes `grades.csv` …"},
      {"type":"text","text":"- `stats NAME` — count, mean, min, max"},
      {"type":"text","text":"- Refactor: introduced a `session()` …"},
      {"type":"status","verb":"Reading","elapsed":"0m 06s","tokens":"49.5k tokens"},
  ],[0,80,95,115,130,150,170,190,240], mascot="off")),
  [{"at":0.05,"event":"One line in"},{"at":0.4,"event":"Five lines out — 183 tokens"},{"at":0.85,"event":"49.5k tokens read"}])

B("B04","IS IT THIRTY-ONE TIMES?","SHELL",LIAM,
  "Is it thirty-one times? Not here. Message eight read one point seven times what message one read, and cost about twice as much — because most of a growing session is cache: "
  "text the service has seen before and re-reads cheaply. Fifteen thousand of that forty-nine came from cache. The line overstates the bill. It does not overstate the mechanism. "
  "Every message re-reads everything, the transcript only grows, and nothing shrinks it unless you do. That's the next film.",
  "CCPlainShell — the ratio, and the cache split on message 8",
  R("CCPlainShell",{"title":"zsh — ~/evidence","lines":[
      "$ python3 -c \"…\"   # message 8 vs message 1",
      "context read:  49,530 / 28,450  =  1.74×",
      "cost:          $0.224 / $0.113  =  1.98×",
      "$ python3 -c \"…\"   # message 8, the single call",
      "cache_read      15,744",
      "cache_creation  33,780",
      "input                6",
      "output             183"],
    "startCue":12,"lineGap":24}, motion="type",
    leaves_terminal_because="arithmetic on the receipts; no session screen shows it"),
  [{"at":0.05,"event":"1.74× read · 1.98× cost"},{"at":0.6,"event":"cache_read 15,744 of 49,530"}])

B("B05","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: eight messages of real work, one receipt each — the experiment. Claude built four commands and a refactor and kept six tests green; the handoff was tests pass and a receipt per call, met. "
  "Step three, the dangerous middle: reading the receipts instead of the slogan — twenty-eight to forty-nine and a half. Claude answered message eight in one line from forty-nine thousand tokens. "
  "Then interpretive judgment: one point seven, not thirty-one, and cache is why. Tool orchestration: I kept the tool list fenced; everything else in that context, I put there. Executive integration, zero. One session.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"eight messages · one receipt each","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Eight messages of work, one receipt each"},
      {"n":2,"phase":"B","labor":"claude","text":"Four commands + a refactor; 6 tests green","handoff":"tests pass; a receipt on every call","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the receipts: 28k → 49.5k, never down","dependsOn":[2]},
      {"n":4,"phase":"B","labor":"claude","text":"Message 8: one line from 49,530 tokens","handoff":"the answer matches the diff","dependsOn":[3]},
      {"n":5,"phase":"H","labor":"human","capacity":"IJ","text":"1.7×, not 31× — cache is why","dependsOn":[4]},
      {"n":6,"phase":"I","labor":"human","capacity":"TO","text":"Tools fenced; the rest of the context, mine","dependsOn":[1]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B06","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must read the receipt, not the slogan. I must know what's in the context I'm paying to re-read — most of it I put there. I must decide when a session is done, because it never decides that itself. "
  "I should ask for the diff, not a summary — the summary re-reads everything to say less. Claude can carry fifty thousand tokens and answer in one line. It can keep six tests green across a refactor. "
  "It should say what it built — it did. It can't re-read only what it needs — that's the design. The context only grows. Shrinking it is mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"carry 49k tokens, answer in a line"},{"tier":"CAN","text":"keep six tests green in a refactor"},
                          {"tier":"SHOULD","text":"say what it built — it did"},{"tier":"SHOULD","text":"re-read only what it needs — no"}],
                    "human":[{"tier":"MUST","text":"read the receipt, not the slogan"},{"tier":"MUST","text":"know what fills the context I pay for"},
                             {"tier":"MUST","text":"decide when the session is done"},{"tier":"SHOULD","text":"ask for the diff, not a summary"}],
                    "closing":"The context only grows. Shrinking it is mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Eight messages of real work, and the context read grew from twenty-eight thousand to forty-nine and a half. Message eight was one line in, a hundred and eighty-three tokens out, and forty-nine thousand read. "
  "Not thirty-one times: one point seven times the read and twice the cost, because most of it is cache. The slogan overstates the bill and gets the mechanism right — every message re-reads everything, and nothing shrinks it unless you do. "
  "What would prove this reel wrong: a message whose first call reads fewer tokens than the one before it, with no compact and no clear.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Eight messages of real work: the context read grew 28,450 → 49,530 tokens, and never went down.",
      "Message 8: one line in, 183 tokens out, 49,530 read. Every message re-reads everything.",
      "Not 31×: 1.7× the read, 2× the cost — most of it is cache. The slogan overstates the bill, not the mechanism.",
      "FALSIFIABLE: a message whose first call reads fewer tokens than the one before it, with no /compact or /clear."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. In a session you've been in for a while, type slash context and read the Messages row — that's what every new message re-reads. Then paste this: "
  "List the three largest things in this session's context and tell me which of them the next task still needs. I'll decide what to do about the rest.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"List the three largest things in this session's context and tell me which of them the next task still needs. I'll decide what to do about the rest.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Every Message Re-reads the Whole Session. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Eight messages, eight receipts: 28k → 49.5k. Not 31×, but it never goes down.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"01-context-and-memory","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/01-context-and-memory/claude-cowork--claude-liam-stop-hitting-claude-limits ('Message 30 Costs 31 Times More' — the claim is measured, not repeated)",
    "sources":["SESSION.md (one real eight-message session)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
