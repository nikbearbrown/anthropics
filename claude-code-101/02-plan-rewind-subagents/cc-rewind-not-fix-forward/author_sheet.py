#!/usr/bin/env python3
"""author_sheet.py — cc-rewind-not-fix-forward (cc-explainer · Claude Code 101 · tier 02, film 04)
"Rewind, Not Fix-Forward: The Andon Cord." Every block traces to SESSION.md (four real headless runs). Liam, in for Bear."""
import json, os
SLUG="cc-rewind-not-fix-forward"; TITLE="Rewind, Not Fix-Forward: The Andon Cord"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Write a small Python module todos.py with two functions: remove_completed and mark_all_done. Include unittest tests."
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

B("B00","COLD OPEN — DRIFT","TERMINAL",LIAM,
  "This is Liam, in for Bear. Look at the function on the left — remove_completed, taking a keep predicate. And the test on the right: call it with keep by length, and the result keeps a completed one. "
  "That's what a fix-forward session leaves behind: a function whose name lies about what it does, because each correction joined a context that already contained the misunderstanding. "
  "Two-and-a-half times the cost of the alternative. Same requirements. Different transcript.",
  "CCSession — the fix-forward drift: the misnamed def next to the test that documents it",
  R("CCSession", session("bare — after two corrections","default",[
      {"type":"prompt","text":"!grep -n 'def ' todos.py","cue":0,"typeDuration":36},
      {"type":"text","text":"10:def remove_completed(todos, keep=None):"},
      {"type":"text","text":"16:def mark_all_done(todos):"},
      {"type":"prompt","text":"!grep -n keep=lambda test_todos.py","cue":0,"typeDuration":44},
      {"type":"text","text":"43:  remove_completed(todos,"},
      {"type":"text","text":"     keep=lambda t: len(t.text) > 1),"},
      {"type":"text","text":"# expects to KEEP a done Todo"},
  ],[0,45,80,120,175,205,240], mascot="off")),
  [{"at":0.05,"event":"grep def"},{"at":0.4,"event":"grep keep=lambda"},{"at":0.85,"event":"# expects to KEEP"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Fix-forward looks simple. Type the correction, hit send, keep going. It isn't simple — it's expensive. The correction joins a context that still contains the shape it was correcting; "
  "Claude's next output is conditioned on both. Rewind removes the mistake from the conversation — Esc-Esc in Claude Code, or the /rewind command. Then you respecify, from a fresh state, with the sentence you now know you meant. "
  "The tally at the end tells you which one was cheaper.",
  "BrutalistHesitantWriter — 'simple' reconsidered into 'expensive'",
  R("BrutalistHesitantWriter", writer("Fix-forward looks simple.\nPaste the correction.\nBut it joins the misunderstanding.\nRewind removes it — then you respec.","simple","expensive",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.22,"event":"'simple' → 'expensive'"},{"at":0.85,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Five words before we start. Fix-forward: pasting a correction after a failed prompt; the correction joins the same conversation. "
  "Rewind: Esc-Esc in Claude Code, or the slash-rewind command — restores conversation and files to the state before the last prompt. "
  "Context: everything Claude sees on the next turn — the running transcript. It grows every turn and shortens on rewind. "
  "Andon cord: Toyota's line-stop cable; here, the keystroke that stops the line before you build more on a wrong move. "
  "Respecify: rewrite the ask with the missing sentence you now know you meant. Fresh state, no residue.",
  "CCDefinitions — five terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"fix-forward","meaning":"paste a correction; it joins the same context"},
      {"term":"rewind","meaning":"Esc-Esc or /rewind — restore state to before the last prompt"},
      {"term":"context","meaning":"the running transcript; everything Claude sees next turn"},
      {"term":"andon cord","meaning":"Toyota's line-stop cable; the metaphor for rewind"},
      {"term":"respecify","meaning":"rewrite the ask with the sentence you now know you meant"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","THE BARE RUN","TERMINAL",LIAM,
  "First run. Fresh session, the ask I actually typed: two functions, tests. Claude reads what's in the folder, writes six lines, then writes sixty-three lines of tests. Non-mutating, dict-based, nine cases green. "
  "That's the default I got. Not wrong. Not everything I meant.",
  "CCSession — bare: Bash, Read, Write, Write, unittest",
  R("CCSession", session("bare — fresh session","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Bash","arg":"pwd && ls","state":"done"},
      {"type":"tool","name":"Read","arg":"check_immutable.py","state":"done"},
      {"type":"tool","name":"Read","arg":"ask.txt","state":"done"},
      {"type":"tool","name":"Write","arg":"todos.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_todos.py","state":"done"},
      {"type":"text","text":"Both files. Non-mutating (new list"},
      {"type":"text","text":"+ new dicts) — 9 tests, all green."},
  ],[0,95,120,140,165,200,225,255], mascot="off")),
  [{"at":0.05,"event":"The ask"},{"at":0.45,"event":"Write ×2"},{"at":0.85,"event":"9 tests green"}])

B("B02","CORRECTION 1 — FIX-FORWARD","TERMINAL",LIAM,
  "Now I change my mind. Switch to a dataclass Todo — resume the session, paste the change. Claude rewrites todos.py and the tests, keeps immutability, drops the field-preservation test because the fields are now fixed. "
  "Then, unprompted, it flags what fix-forward strands: the external check script that was written to the old dict shape now errors out. The correction joined; the old contract didn't leave with it.",
  "CCSession — --resume + dataclass; Claude flags the stranded external check",
  R("CCSession", session("bare — --resume 727cb81b…","accept-edits",[
      {"type":"prompt","text":"switch todos.py to a Todo dataclass","cue":0,"typeDuration":60},
      {"type":"tool","name":"Write","arg":"todos.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_todos.py","state":"done"},
      {"type":"text","text":"Done. Both files use Todo;"},
      {"type":"text","text":"mark_all_done uses replace so it"},
      {"type":"text","text":"stays non-mutating."},
      {"type":"text","text":"Heads-up: check_immutable.py feeds"},
      {"type":"text","text":"dicts — it will now AttributeError."},
  ],[0,70,110,145,170,195,225,255], mascot="off")),
  [{"at":0.05,"event":"--resume prompt"},{"at":0.5,"event":"Writes"},{"at":0.85,"event":"'the checker will now AttributeError'"}])

B("B03","CORRECTION 2 — THE DRIFT","TERMINAL",LIAM,
  "One more correction, narrow on purpose — the way real sessions grow. Add an optional keep predicate to remove_completed. Leave mark_all_done alone. Claude does exactly what I asked, and adds a test — where it calls "
  "remove_completed with a keep-by-length predicate, and the expected result keeps a completed one. The narrow scope is the smell. The name doesn't lie yet; the tests already do.",
  "CCSession — --resume + Edit; the drift on line 43",
  R("CCSession", session("bare — --resume 727cb81b…","accept-edits",[
      {"type":"prompt","text":"add optional keep(t) predicate","cue":0,"typeDuration":50},
      {"type":"tool","name":"Edit","arg":"todos.py","state":"done"},
      {"type":"tool","name":"Edit","arg":"test_todos.py","state":"done"},
      {"type":"text","text":"Added keep as optional predicate,"},
      {"type":"text","text":"default lambda t: not t.done."},
      {"type":"text","text":"mark_all_done untouched."},
      {"type":"text","text":"test on L43 uses keep by length —"},
      {"type":"text","text":"expected result KEEPS a done one."},
  ],[0,55,80,115,140,165,205,240], mascot="off")),
  [{"at":0.05,"event":"narrow prompt"},{"at":0.5,"event":"Edits"},{"at":0.85,"event":"the L43 note"}])

B("B04","VERIFY THE DRIFT","TERMINAL",LIAM,
  "Verify it. Seventeen lines of module, sixty-seven lines of tests, nine cases pass. grep 'def' shows a function called remove_completed that takes a keep predicate. Two corrections turned an honest name into a lie the tests already document. "
  "Everything is green. Nothing is right.",
  "CCSession — wc, grep def, grep keep=lambda",
  R("CCSession", session("bare — final","default",[
      {"type":"prompt","text":"!wc -l todos.py test_todos.py","cue":0,"typeDuration":38},
      {"type":"text","text":"      17 todos.py"},
      {"type":"text","text":"      67 test_todos.py"},
      {"type":"prompt","text":"!python3 -m unittest test_todos","cue":0,"typeDuration":44},
      {"type":"text","text":"Ran 9 tests in 0.000s"},
      {"type":"text","text":"OK"},
      {"type":"prompt","text":"!grep -n 'def ' todos.py","cue":0,"typeDuration":36},
      {"type":"text","text":"10:def remove_completed(todos, keep=None):"},
  ],[0,45,75,115,165,190,220,260], mascot="off")),
  [{"at":0.05,"event":"wc → 17/67"},{"at":0.5,"event":"unittest → 9/9"},{"at":0.85,"event":"the misnamed def"}])

B("B05","REWIND — THE HEADLESS EQUIVALENT","SHELL",LIAM,
  "So what's the alternative. In the interactive UI it's one keystroke: press Escape twice, or type slash-rewind. The last prompt disappears from the conversation, and any file Claude wrote for it disappears from disk. "
  "Then you respecify — the same intent with the sentence you now know you meant. This is a headless session, so I do what rewind does: a new session-id, no --resume, the improved ask from the start. Fresh context. No residue.",
  "CCPlainShell — the Esc-Esc gesture and the headless equivalent",
  R("CCPlainShell",{"title":"zsh — rewind ≡ new session","lines":[
      "# interactive UI:",
      "# ⎋ ⎋   or   /rewind",
      "# → last prompt gone; files gone; respec.",
      "",
      "# headless equivalent — no --resume:",
      "$ claude -p \"<the respecified ask>\" \\",
      "    --session-id 5f9cb45f-…",
      "# fresh conversation. shorter context.",
      "# no misunderstanding to carry."],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the Esc-Esc mechanic isn't in the transcript; the plain shell states it before the run"),
  [{"at":0.05,"event":"Esc-Esc gesture"},{"at":0.55,"event":"new session-id"},{"at":0.9,"event":"no residue"}])

B("B06","THE RESPEC RUN","TERMINAL",LIAM,
  "Same intent, respecified. A todo is a dataclass. Filter_todos takes a keep predicate — named for what it does. Mark_all_done stays. The tests assert the original list is unchanged and cover a general filter, not one done-shaped case. "
  "Claude writes both files, five turns, one shot. Ten tests green. The function name no longer lies.",
  "CCSession — rewind: fresh session-id, respecified ask, Write, Write",
  R("CCSession", session("rewind — fresh session","accept-edits",[
      {"type":"prompt","text":"filter_todos(todos, keep) + mark_all_done, immutable","cue":0,"typeDuration":90},
      {"type":"tool","name":"Write","arg":"todos.py","state":"done"},
      {"type":"tool","name":"Write","arg":"test_todos.py","state":"done"},
      {"type":"text","text":"todos.py defines Todo as a"},
      {"type":"text","text":"dataclass and provides filter_todos"},
      {"type":"text","text":"and mark_all_done. 10 tests: cover"},
      {"type":"text","text":"filter cases + immutability."},
  ],[0,110,150,185,215,245,275], mascot="off")),
  [{"at":0.05,"event":"the respec ask"},{"at":0.5,"event":"Writes"},{"at":0.9,"event":"'10 tests'"}])

B("B07","THE TWO PATHS, COUNTED","SHELL",LIAM,
  "Count what each path cost. Fix-forward — bare plus two corrections, one session: fourteen turns, ninety-eight seconds, eighty-nine cents. End state — remove_completed taking a keep predicate. "
  "Rewind — one fresh session with the respecified ask: five turns, twenty-seven seconds, thirty-six cents. End state — filter_todos taking a keep predicate. Two-and-a-half times cheaper. And the name matches the behaviour.",
  "CCPlainShell — turns / seconds / cost, both paths",
  R("CCPlainShell",{"title":"zsh — two paths, counted","lines":[
      "# fix-forward · bare + 2 --resume",
      "  turns   14",
      "  time    97.9 s",
      "  cost   $0.888",
      "  end    remove_completed(keep=None)",
      "",
      "# rewind · fresh session · respec",
      "  turns    5",
      "  time    26.6 s",
      "  cost   $0.359",
      "  end    filter_todos(keep)"],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="a comparison across two sessions is not inside either session"),
  [{"at":0.05,"event":"fix-forward: 14 turns"},{"at":0.5,"event":"rewind: 5 turns"},{"at":0.9,"event":"2.5× cheaper"}])

B("B08","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: a one-sentence ask, underspecified. Claude ran the bare turn; the handoff was tests green, and it met that — the code was fine. "
  "Step three, the dangerous middle: I saw what I actually wanted and paste-corrected, twice, without rewinding. The first correction stranded the external check script. The second let a function name drift from its behaviour. "
  "Step five, mine, interpretive judgment: I noticed the drift only because I opened the test file. Then the real work: a respecified prompt in a fresh session. Claude did the respec run; handoff met, and the name matches. "
  "Tool orchestration, zero; executive integration, zero. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · two paths","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence — underspecified"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 5-line immutable module, 9 tests","handoff":"tests pass","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Paste-correct twice — no rewind","dependsOn":[2]},
      {"n":4,"phase":"C","labor":"claude","text":"Correction 1 + 2: name drifts on L10","handoff":"tests pass; the name is a lie","dependsOn":[3]},
      {"n":5,"phase":"H","labor":"human","capacity":"IJ","text":"Opened test file — saw the drift","dependsOn":[4]},
      {"n":6,"phase":"F","labor":"human","capacity":"PF","text":"Respecify — new session, no residue","dependsOn":[5]},
      {"n":7,"phase":"C","labor":"claude","text":"Rewind: filter_todos, 10 tests","handoff":"tests pass; name matches","dependsOn":[6]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.45,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B09","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must decide when to stop and rewind — nobody else can. I must read the diff and the tests before the next prompt; the drift lives there. I must name a function for what it does, not what it did. "
  "I should paste one correction, not three. Claude can accept a resume and produce plausible code — it did. It can flag its own collateral damage — it did, unprompted. It should keep the transcript shorter — rewind is what shortens it. "
  "It should refuse a fourth correction and ask me to respec.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"accept resume, guess plausibly"},{"tier":"CAN","text":"call out stranded contracts"},
                          {"tier":"SHOULD","text":"keep the transcript shorter"},{"tier":"SHOULD","text":"ask me to respec, not chain fixes"}],
                    "human":[{"tier":"MUST","text":"decide when to stop and rewind"},{"tier":"MUST","text":"read diff, tests, then prompt"},
                             {"tier":"MUST","text":"name a function for what it does"},{"tier":"SHOULD","text":"paste one correction, not three"}],
                    "closing":"Rewind — the andon cord for a session.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Fix-forward: one bare turn and two --resume corrections; fourteen turns, ninety-eight seconds, eighty-nine cents; end state — a function called remove_completed that takes a keep predicate. "
  "Rewind: one fresh session with the respecified ask; five turns, twenty-seven seconds, thirty-six cents; end state — filter_todos, where the name matches the behaviour. "
  "Same requirements. Two-and-a-half times cheaper. And a name I don't have to apologize for. "
  "What would prove this reel wrong: a fix-forward session that converges to a shorter transcript than the respec.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Fix-forward: bare + 2 --resume — 14 turns, 97.9 s, $0.888.",
      "End state — remove_completed(keep=None). The name lies; the tests document the drift on line 43.",
      "Rewind: one fresh session, respecified ask — 5 turns, 26.6 s, $0.359.",
      "End state — filter_todos(keep). Same requirements. 2.5× cheaper. Name matches behaviour.",
      "Rewind is the andon cord for a session — stop the line, respec, resume.",
      "FALSIFIABLE: a fix-forward session that converges to a shorter transcript than the respec."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Next time a prompt gives you something almost right, don't paste the fix. Open Claude Code and paste this: I'm about to paste a correction. Ask me three questions first — what was missing from the original ask, "
  "what would the ask look like with that sentence added, and would rewinding cost less than fix-forwarding. Then wait — do not touch any file.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"I'm about to paste a correction. Before I do, ask me three questions: what was missing from the original ask, what would the ask look like with that sentence added, and would rewinding cost less than fix-forwarding. Then wait — don't touch any file.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Rewind, Not Fix-Forward: The Andon Cord. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same requirements, two paths — 14 turns of fix-forward or 5 of rewind. The name matches only one.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"02-plan-rewind-subagents","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-rewind-not-fix-forward (the concept; the card body replaced by four real headless runs)",
    "sources":["SESSION.md (four real headless runs)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
