#!/usr/bin/env python3
"""author_sheet.py — cc-context-check (cc-explainer · Claude Code 101 · tier 01, film 06)
"/context: Read Your Window Before It Fills." Every block traces to SESSION.md (message 12 of one real session). Liam, in for Bear."""
import json, os
SLUG="cc-context-check"; TITLE="/context: Read Your Window Before It Fills"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
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

B("B00","COLD OPEN — /context","TERMINAL",LIAM,
  "This is Liam, in for Bear. Two films ago the receipts said the context only grows. One film ago, compact and clear shrank it. This one is the gauge: slash context. "
  "Same session, right after the compact. One command, and the product tells you what's in the window — thirty-six point seven thousand tokens of a million, four percent — and what each part is.",
  "CCSession — /context; the headline",
  R("CCSession", session("gradebook · message 12","default",[
      {"type":"prompt","text":"/context","cue":0,"typeDuration":22},
      {"type":"text","text":"## Context Usage"},
      {"type":"text","text":"**Model:** claude-opus-4-7"},
      {"type":"text","text":"**Tokens:** 36.7k / 1m (4%)"},
      {"type":"text","text":"### Estimated usage by category"},
  ],[0,60,90,120,170])),
  [{"at":0.05,"event":"/context types"},{"at":0.5,"event":"36.7k / 1m (4%)"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. You can't manage what you can't see, and the context window is invisible until you ask. Slash context asks. It shows what's in the window right now — "
  "the fixed part you pay for before you type a word, and the conversation you've added — and how much room is left before the product compacts on its own. Read it before a new task, not after the session degrades.",
  "BrutalistHesitantWriter — 'invisible' reconsidered into 'a command away'",
  R("BrutalistHesitantWriter", writer("The context window is invisible.\n/context shows what's in it right now:\nthe fixed part, the conversation,\nand how much room is left.","invisible","a command away",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.2,"event":"'invisible' → 'a command away'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Context window: the fixed amount the model can read at once — here, a million tokens. System prompt: the product's own standing instructions, loaded before yours. "
  "Tools: the descriptions of every tool the model may call; they take space whether or not it calls them. Messages: the conversation — your asks, its answers, every tool result. "
  "Autocompact buffer: room the product keeps in reserve so it can compact before the window fills.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"context window","meaning":"the fixed amount the model can read at once — here, a million tokens"},
      {"term":"system prompt","meaning":"the product's own standing instructions, loaded before yours"},
      {"term":"tools","meaning":"descriptions of every tool the model may call; they take space either way"},
      {"term":"messages","meaning":"the conversation: your asks, its answers, every tool result"},
      {"term":"autocompact buffer","meaning":"room the product keeps in reserve so it can compact before the window fills"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","THE BREAKDOWN","TERMINAL",LIAM,
  "The breakdown, in the product's own table. System prompt: nine thousand. Tools: nearly nine thousand, plus nineteen thousand more listed but not loaded until needed. Skills: four thousand. "
  "CLAUDE.md: four hundred sixty-five — the file from three films ago, still riding along. Messages: fourteen thousand — that's the conversation, after compact. And free space: nine hundred thirty thousand. "
  "Read the fixed part once and remember it: it's there before you type anything, every session.",
  "CCSession — the category table, verbatim rows",
  R("CCSession", session("gradebook · message 12","default",[
      {"type":"text","text":"| System prompt           |  9k    | 0.9% |"},
      {"type":"text","text":"| System tools            |  8.9k  | 0.9% |"},
      {"type":"text","text":"| System tools (deferred) | 19.2k  | 1.9% |"},
      {"type":"text","text":"| Memory files            |  465   | 0.0% |"},
      {"type":"text","text":"| Skills                  |  4.2k  | 0.4% |"},
      {"type":"text","text":"| Messages                | 14.2k  | 1.4% |"},
      {"type":"text","text":"| Free space              | 930k   | 93.0% |"},
      {"type":"text","text":"| Autocompact buffer      | 33k    | 3.3% |"},
  ],[0,25,50,75,100,130,160,190], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"System prompt 9k"},{"at":0.35,"event":"Tools 8.9k + 19.2k deferred"},{"at":0.65,"event":"Messages 14.2k"},{"at":0.9,"event":"Free space 930k"}])

B("B02","VERIFY","SHELL",LIAM,
  "Check it against the receipts. The headline says thirty-six point seven thousand. One message earlier, the stream said thirty-six thousand six hundred seventy tokens read. Same number, two instruments. "
  "And CLAUDE.md is in the table at four hundred sixty-five tokens: the file you write is part of what every message re-reads. Small here. Keep it that way.",
  "CCPlainShell — the headline vs the receipt; the CLAUDE.md row",
  R("CCPlainShell",{"title":"zsh — ~/evidence","lines":[
      "$ grep '^\\*\\*Tokens' context-output.md",
      "**Tokens:** 36.7k / 1m (4%)",
      "$ python3 -c \"…turns.json…\"     # message 10, one message earlier",
      "msg 10 (after /compact)  36,670 tokens read",
      "$ grep 'CLAUDE.md' context-output.md",
      "| Project | …/context-cost-session/CLAUDE.md | 465 |"],
    "startCue":12,"lineGap":24}, motion="type",
    leaves_terminal_because="two instruments compared in a plain shell; no session screen shows both"),
  [{"at":0.05,"event":"36.7k on the gauge"},{"at":0.4,"event":"36,670 on the receipt"},{"at":0.8,"event":"CLAUDE.md: 465"}])

B("B03","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: run the gauge right after the compact, so it shows something worth reading. Claude printed the report; the handoff was the headline matching the receipt, and it did. "
  "Step three, the dangerous middle: reading the fixed part — thirty-odd thousand before I typed a word — instead of assuming the window is empty when I start. Then interpretive judgment: which rows are mine to shrink — messages and CLAUDE.md — and which aren't — the system prompt, the tools. "
  "Tool orchestration: this is the tool. Executive integration, zero.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one command · one table","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"Run the gauge right after the compact"},
      {"n":2,"phase":"C","labor":"claude","text":"/context: the table, 36.7k / 1m","handoff":"the headline matches the receipt","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the fixed part: ~30k before I type","dependsOn":[2]},
      {"n":4,"phase":"H","labor":"human","capacity":"IJ","text":"Mine to shrink: messages, CLAUDE.md","dependsOn":[3]},
      {"n":5,"phase":"I","labor":"human","capacity":"TO","text":"/context before a new task, not after","dependsOn":[4]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B04","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must read the gauge before a new task, not after the answers get worse. I must know the fixed part — it's paid before I type. I must decide what to compact and what to clear; the gauge only shows, it doesn't choose. "
  "I should keep CLAUDE.md small, because it's in that table every session. Claude can print the window to the token. It can compact when the buffer runs out — on its own. "
  "It should tell me the window is filling — it will, at the edge, by compacting. It should keep the receipt honest — it did; two instruments, one number.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"print the window to the token"},{"tier":"CAN","text":"compact on its own at the edge"},
                          {"tier":"SHOULD","text":"keep the receipt honest — it did"},{"tier":"SHOULD","text":"show the fixed part — it did"}],
                    "human":[{"tier":"MUST","text":"read the gauge before a new task"},{"tier":"MUST","text":"know the fixed part I pay first"},
                             {"tier":"MUST","text":"choose: compact or clear"},{"tier":"SHOULD","text":"keep CLAUDE.md small"}],
                    "closing":"The gauge shows. Choosing what to do about it is mine.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Slash context is the gauge: thirty-six point seven thousand of a million tokens, four percent, right after a compact. The fixed part — system prompt, tools, skills, CLAUDE.md — is there before you type a word. "
  "Messages, fourteen thousand, is the part you grow. The headline matched the receipt from one message earlier to the token. "
  "What would prove this reel wrong: a slash context headline that disagrees with the stream's own usage numbers.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "/context is the gauge: 36.7k of 1M tokens (4%) right after a compact.",
      "The fixed part — system prompt 9k, tools 8.9k (+19.2k deferred), skills 4.2k, CLAUDE.md 465 — is there before you type.",
      "Messages, 14.2k, is the part you grow. The headline matched the stream's receipt (36,670) to the token.",
      "FALSIFIABLE: a /context headline that disagrees with the stream's own usage numbers."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Open a session you've used for a while and type slash context. Write down two rows: Messages, and your CLAUDE.md. Then paste this: "
  "Which of the messages in this session does the next task still need? List them, and tell me what you'd summarize if I ran slash compact right now.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Which of the messages in this session does the next task still need? List them, and tell me what you'd summarize if I ran /compact right now.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"after /context, paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Slash context: Read Your Window Before It Fills. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"The gauge: 36.7k of 1M, and what each row is.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"01-context-and-memory","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/01-context-and-memory/claude-code--claude-liam-slash-context-window-check (the concept; the card body replaced by message 12 of a real session)",
    "sources":["SESSION.md (message 12 of one real session)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
