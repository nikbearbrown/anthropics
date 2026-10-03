#!/usr/bin/env python3
"""author_sheet.py — cc-prompt-is-a-wish-spec-is-a-contract (cc-explainer · Claude Code 101 · tier 04).
"Why 'Write Me a Login Function' Is Not a Prompt." Every block traces to SESSION.md (three real headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-prompt-is-a-wish-spec-is-a-contract"
TITLE="Why 'Write Me a Login Function' Is Not a Prompt"
TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK_WISH="Write me a login function."
ASK_SPEC="Read SPEC.md, then build auth.py per its conditions."
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

B("B00","COLD OPEN — WISH","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence, an empty folder: write me a login function. Claude tries to ask three questions first; the fence denies them. "
  "So it says the honest thing on camera: without a spec you get my guess, not your answer. Then it makes the guesses. Forty lines. Three functions — one of which nobody asked for.",
  "CCSession — the wish run: ask, denied questions, README read, Write, the honest confession",
  R("CCSession", session("scratch/wish — one sentence","accept-edits",[
      {"type":"prompt","text":ASK_WISH,"cue":0,"typeDuration":56},
      {"type":"tool","name":"AskUserQuestion","arg":"3 questions (denied)","state":"done"},
      {"type":"text","text":"Looks like the prompt got dismissed —"},
      {"type":"text","text":"without a spec you get my guess,"},
      {"type":"text","text":"not your answer. I'll pick defaults."},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Write","arg":"auth.py","state":"done"},
      {"type":"text","text":"Wrote three functions: hash, verify,"},
      {"type":"text","text":"and login(user, pw, users)."},
      {"type":"text","text":"Choices I made without asking:"},
      {"type":"text","text":"PBKDF2-SHA256, 200k iterations,"},
      {"type":"text","text":"dict store, returns bool, no session."},
  ],[0,60,90,110,130,155,180,210,230,255,275,295], mascot="off")),
  [{"at":0.05,"event":"Ask lands"},{"at":0.25,"event":"Questions denied"},{"at":0.55,"event":"Write auth.py"},{"at":0.9,"event":"'choices I made without asking'"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. When you type a sentence Claude can execute, it feels like a prompt — a clear request answered by a clear function. "
  "It isn't. It's a wish. A prompt is a wish addressed to something that knows you; Claude is not that. What Claude answers instead is what the training distribution says a login function usually looks like. "
  "The fix isn't a longer sentence. It's a short document written before Claude touches anything, that names what has to be true.",
  "BrutalistHesitantWriter — 'prompt' reconsidered into 'wish'",
  R("BrutalistHesitantWriter", writer("A clear ask is a prompt.\nClaude fills the silence with defaults.\nThe defaults were not yours.\nA spec is what makes them yours.","prompt","wish",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.25,"event":"'prompt' → 'wish'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Prompt: a request written in the belief that the listener already knows your intent. Wish: a request that leaves the listener to fill in what you didn't say. "
  "Specification: a short document that names what must be true — what to hold, what not to touch, and how you'll know it's done. Invariant: a rule the output must obey in every case, not just the easy one. "
  "Handoff condition: a check you can run that says the contract was kept.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"prompt","meaning":"a request written as if the listener knows your intent"},
      {"term":"wish","meaning":"a request that leaves the listener to fill in what you didn't say"},
      {"term":"specification","meaning":"a short document naming what must hold and what may not be touched"},
      {"term":"invariant","meaning":"a rule the output must obey in every case, not just the easy one"},
      {"term":"handoff condition","meaning":"a check you can run that says the contract was kept"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","WISH — VERIFY","TERMINAL",LIAM,
  "Check the wish page against the tests I hadn't shown Claude yet. Four of five pass — the crypto hygiene is fine, that's the model's default now. "
  "One fails: hash_password of empty string returns a hash instead of raising. Nobody told Claude that was an invariant, so it wasn't. And a third function — login of user, password, users dict — that nobody asked for.",
  "CCSession — wc, grep -c def, unittest → 1 FAIL, the extra function",
  R("CCSession", session("scratch/wish — verify","default",[
      {"type":"prompt","text":"!wc -l auth.py","cue":0,"typeDuration":28},
      {"type":"text","text":"      40 auth.py"},
      {"type":"prompt","text":"!grep -c \"^def \" auth.py","cue":0,"typeDuration":38},
      {"type":"text","text":"3"},
      {"type":"prompt","text":"!python3 -m unittest test_auth.py","cue":0,"typeDuration":52},
      {"type":"text","text":"F...."},
      {"type":"text","text":"FAIL: test_empty_password_raises"},
      {"type":"text","text":"AssertionError: ValueError not raised"},
      {"type":"text","text":"Ran 5 tests / FAILED (failures=1)"},
      {"type":"prompt","text":"!grep \"^def \" auth.py","cue":0,"typeDuration":38},
      {"type":"text","text":"def hash_password(password)"},
      {"type":"text","text":"def verify_password(password, stored)"},
      {"type":"text","text":"def login(username, password, users)"},
  ],[0,35,60,95,110,155,175,200,225,250,285,305,325], mascot="off")),
  [{"at":0.05,"event":"wc → 40"},{"at":0.25,"event":"3 functions"},{"at":0.5,"event":"1 test fails"},{"at":0.85,"event":"The third function"}])

B("B02","THE SPEC","SHELL",LIAM,
  "Twenty-two lines, written by me before the second run. Two functions — hash and verify — no third. Five invariants: empty raises, no plaintext, PBKDF2 with SHA-256, at least a hundred thousand iterations, salt from secrets, constant-time compare. "
  "One boundary — touch auth.py only, standard library only. And a handoff — python -m unittest test_auth.py reports OK. Nineteen sentences that decide what Claude may fill in, and what it may not.",
  "CCPlainShell — wc on SPEC.md; the five invariants",
  R("CCPlainShell",{"title":"zsh — ~/scratch","lines":[
      "$ wc -l SPEC.md",
      "      22 SPEC.md",
      "$ grep -E '^[0-9]\\.' SPEC.md",
      "1. hash_password(\"\") … raise ValueError",
      "2. stored must not contain the password",
      "3. pbkdf2_hmac sha256, >= 100 000 iters",
      "4. verify_password uses compare_digest",
      "5. stored round-trips through verify",
      "$ grep -A1 'Handoff' SPEC.md | tail -1",
      "python3 -m unittest test_auth.py -> OK"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the spec is read in a plain shell before any session; no session contains this"),
  [{"at":0.05,"event":"wc → 22"},{"at":0.45,"event":"the five invariants"},{"at":0.85,"event":"the handoff"}])

B("B03","SPEC — THE RUN","TERMINAL",LIAM,
  "Same folder — plus SPEC.md and the test file. Same model. Different sentence: read SPEC.md, then build auth.py per its conditions. It reads the spec. It reads the tests. Its plan sentence is the spec, in fewer words. "
  "Thirty-three lines. Two functions. It runs the handoff itself, because the SPEC said so. OK, five tests.",
  "CCSession — Reads SPEC + tests, Writes, unittest → OK",
  R("CCSession", session("scratch/spec — with contract","accept-edits",[
      {"type":"prompt","text":ASK_SPEC,"cue":0,"typeDuration":78},
      {"type":"tool","name":"Read","arg":"SPEC.md","state":"done"},
      {"type":"tool","name":"Read","arg":"test_auth.py","state":"done"},
      {"type":"text","text":"I have the invariants. Two functions,"},
      {"type":"text","text":"PBKDF2-SHA256 100k, secrets salt,"},
      {"type":"text","text":"compare_digest, empty raises."},
      {"type":"tool","name":"Write","arg":"auth.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_auth.py","state":"done"},
      {"type":"text","text":"Ran 5 tests in 0.058s"},
      {"type":"text","text":"OK"},
  ],[0,95,120,145,170,195,220,255,285,305], mascot="off")),
  [{"at":0.05,"event":"Different ask"},{"at":0.35,"event":"Reads SPEC + tests"},{"at":0.75,"event":"Writes 33 lines"},{"at":0.95,"event":"OK"}])

B("B04","SPEC — VERIFY","TERMINAL",LIAM,
  "Check it. Thirty-three lines against forty. Two functions, not three. A hundred thousand iterations — because the spec said at least a hundred thousand, and Claude reads the bound literally. Secrets, not urandom. "
  "And verify of empty password raises, not just hash — because the spec said empty raises, and it meant both. Every one of those is a line from my file, not a default.",
  "CCSession — wc, def count, iters, secrets, empty-verify raises",
  R("CCSession", session("scratch/spec — verify","default",[
      {"type":"prompt","text":"!wc -l auth.py","cue":0,"typeDuration":28},
      {"type":"text","text":"      33 auth.py"},
      {"type":"prompt","text":"!grep -c \"^def \" auth.py","cue":0,"typeDuration":38},
      {"type":"text","text":"2"},
      {"type":"prompt","text":"!grep -oE \"[0-9]+_000\" auth.py","cue":0,"typeDuration":42},
      {"type":"text","text":"100_000"},
      {"type":"prompt","text":"!grep -oE \"secrets|urandom\" auth.py","cue":0,"typeDuration":42},
      {"type":"text","text":"secrets"},
      {"type":"prompt","text":"!python3 -c \"import auth; auth.verify_password('', auth.hash_password('x'))\"","cue":0,"typeDuration":98},
      {"type":"text","text":"ValueError: empty password"},
  ],[0,35,60,95,120,155,185,220,245,340], mascot="off")),
  [{"at":0.05,"event":"wc → 33"},{"at":0.25,"event":"2 functions"},{"at":0.5,"event":"100k iters"},{"at":0.75,"event":"secrets"},{"at":0.95,"event":"empty-verify raises"}])

B("B05","THE MIDDLE CASE","TERMINAL",LIAM,
  "One more run. The bare ask again — write me a login function — but the test file is sitting in the folder. Claude tries the stack questions again; denied again. Then it reads the test file, and says the rule out loud: the spec is the tests. "
  "Thirty-four lines. All five pass. But — os.urandom instead of secrets. Two hundred thousand iterations, not the spec's hundred thousand. Verify of empty password silently returns false, because the tests never asked. Passed the checker. Drifted on every axis the checker couldn't see.",
  "CCSession — the middle case: 'the spec is the tests', OK 5, invisible drift",
  R("CCSession", session("scratch/testsonly — same ask","accept-edits",[
      {"type":"prompt","text":ASK_WISH,"cue":0,"typeDuration":56},
      {"type":"tool","name":"AskUserQuestion","arg":"stack? (denied)","state":"done"},
      {"type":"tool","name":"Read","arg":"test_auth.py","state":"done"},
      {"type":"text","text":"My earlier stack questions"},
      {"type":"text","text":"were wrong to ask."},
      {"type":"text","text":"The spec is the tests."},
      {"type":"tool","name":"Write","arg":"auth.py","state":"done"},
      {"type":"tool","name":"Bash","arg":"python3 -m unittest test_auth.py","state":"done"},
      {"type":"text","text":"Ran 5 tests / OK"},
      {"type":"text","text":"(os.urandom · 200k iters · empty silent)"},
  ],[0,50,85,120,145,170,200,240,275,310], mascot="off"), motion="drawon"),
  [{"at":0.05,"event":"Same ask"},{"at":0.25,"event":"denied"},{"at":0.5,"event":"'the spec is the tests'"},{"at":0.85,"event":"OK — with drift"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, no spec. Claude did the wish run; handoff was five tests — it failed one, and shipped a third function nobody asked for. "
  "Step three, the dangerous middle: reading the summary — 'crypto is fine' — instead of the diff, where the empty-string test was already failing. "
  "Then the real work, mine: twenty-two lines in a SPEC file. Claude did the spec run; handoff met, every choice traces to a numbered line. "
  "Then interpretive judgment: the tests-only run passed the checker and drifted on every axis the checker couldn't see. Tool orchestration zero. Executive integration zero. One page. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one ask · three conditions","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, no spec"},
      {"n":2,"phase":"C","labor":"claude","text":"Wish: 40 lines, 3 funcs, 1 test fails","handoff":"5 tests OK","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the diff, not the summary","dependsOn":[2]},
      {"n":4,"phase":"F","labor":"human","capacity":"PF","text":"Write SPEC.md — 22 lines, mine","dependsOn":[3]},
      {"n":5,"phase":"C","labor":"claude","text":"Spec: 33 lines, 2 funcs, OK 5","handoff":"OK; every line traces to spec","dependsOn":[4]},
      {"n":6,"phase":"H","labor":"human","capacity":"IJ","text":"Tests-only: passed test, drifted","dependsOn":[2]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must name the invariants — the rules the checker will not catch. I must decide the interface, or Claude will add a function I did not want. "
  "I must write the handoff as a check I can run. I should read the diff, not the summary. Claude can hash and salt on its own, and it will. "
  "It can read a spec and match it — it did. It should refuse what the spec refuses — it did. It should ask when uncertain — it tried, and I let the fence deny it. Twenty-two lines. Mine.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"hash and salt on its own"},{"tier":"CAN","text":"read a spec and match it"},
                          {"tier":"SHOULD","text":"refuse what the spec refuses"},{"tier":"SHOULD","text":"ask when uncertain"}],
                    "human":[{"tier":"MUST","text":"name the invariants myself"},{"tier":"MUST","text":"decide the interface"},
                             {"tier":"MUST","text":"write handoff as a check"},{"tier":"SHOULD","text":"read the diff, not the summary"}],
                    "closing":"A prompt is a wish. A spec is a contract. 22 lines.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. One sentence, empty folder: forty lines, three functions, one test failure — and Claude said out loud it was guessing. "
  "Twenty-two lines of mine first: thirty-three lines, two functions, five tests OK, every line traceable. "
  "The tests-only run passed the checker and drifted on every invisible axis; done is a script, and the script cannot see what you meant. "
  "What would prove this reel wrong: a wish run whose choices all match a spec Claude was never shown.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Wish: 40 lines, 3 functions, 1 test fails — Claude said it was guessing.",
      "22 lines of mine first: 33 lines, 2 functions, 5 tests OK, every line traces.",
      "Tests-only passed the checker and drifted on every invisible axis.",
      "FALSIFIABLE: a wish run whose choices all match a spec Claude was never shown."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Take the next thing you were about to ask Claude for and paste this: before you write any code, ask me the invariants — the rules the tests will not catch — and the boundary — files in scope, files off limits — and the handoff — a command I can run that says you are done. "
  "Write my answers into SPEC.md. Then stop, and wait for me to run it.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Before you write any code, ask me the invariants, the boundary, and the handoff condition — a command I can run that says you are done. Write my answers into SPEC.md. Then stop, and wait for me to run it.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Why 'Write Me a Login Function' Is Not a Prompt. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"One sentence Claude can execute is a wish. A spec is what makes the choices yours.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"04-spec-before-code","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/04-spec-before-code/claude-code--claude-liam-prompt-is-a-wish-spec-is-a-contract (the concept; the fictional cast replaced by three real headless runs)",
    "sources":["SESSION.md (three real runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
