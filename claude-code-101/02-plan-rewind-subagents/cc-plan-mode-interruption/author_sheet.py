#!/usr/bin/env python3
"""author_sheet.py — cc-plan-mode-interruption (cc-explainer · Claude Code 101 · tier 02, film plan-mode).
"Plan Mode: Freeze Before the Byte Changes." Every block traces to SESSION.md (three real fresh runs). Liam, in for Bear."""
import json, os
SLUG="cc-plan-mode-interruption"; TITLE="Plan Mode: Freeze Before the Byte Changes"; TOPIC="CLAUDE CODE 101"; LIAM="am_onyx"; WPS=2.9
ASK="Reorganize the classroom site so the schedule is on the front page."
CORRECT="No — do not delete schedule.html and do not remove the link to it. Keep the schedule page in place, and on the front page put the same five items as a summary that links to schedule.html for the full list. Do not touch notes.md. Revise the plan."
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
def session(title, mode, blocks, cues, mascot="off"): return {"title":title,"mode":mode,"blocks":blocks,"cues":cues,"mascot":mascot}

B("B00","COLD OPEN — BARE RUN","TERMINAL",LIAM,
  "This is Liam, in for Bear. One sentence, five files in a folder — the Thursday study group's site — and no plan mode. "
  "Claude reads the four files, decides the second page is redundant, and deletes it. Before that sentence reaches me. "
  "The byte changed. Nothing asked. That's what plan mode is for.",
  "CCSession — Run A: the ask, four Reads, Write index.html, rm schedule.html, Edit README.md",
  R("CCSession", session("studygroup — accept edits","accept-edits",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Read","arg":"index.html","state":"done"},
      {"type":"tool","name":"Read","arg":"schedule.html","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"text","text":"I'll merge the schedule into the"},
      {"type":"text","text":"front page, remove the now-redundant"},
      {"type":"text","text":"schedule.html, and update the README."},
      {"type":"tool","name":"Write","arg":"index.html","state":"done"},
      {"type":"tool","name":"Bash","arg":"rm schedule.html","state":"done"},
      {"type":"tool","name":"Edit","arg":"README.md","state":"done"},
  ],[0,95,120,145,175,200,225,255,285,310])),
  [{"at":0.05,"event":"Ask types"},{"at":0.5,"event":"'remove the now-redundant schedule.html'"},{"at":0.85,"event":"rm schedule.html"}])

B("BIDEA","THE IDEA","IDEA",LIAM,
  "Here's the idea of this film. Same one-sentence ask, twice — first without plan mode, then with. "
  "Without it, three files change and one is gone before I read a summary. With it, zero bytes move; Claude writes a plan I can read and argue with. "
  "Plan mode isn't a pause. It's a freeze.",
  "BrutalistHesitantWriter — 'pause' reconsidered into 'freeze'",
  R("BrutalistHesitantWriter", writer("Same one-sentence ask.\nWithout plan mode: three files change.\nWith plan mode: zero bytes change.\nPlan mode is a pause.","pause","freeze",SLUG), motion="type",
    leaves_terminal_because="the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix"),
  [{"at":0.05,"event":"Writer starts"},{"at":0.55,"event":"'pause' → 'freeze'"},{"at":0.9,"event":"Last line"}])

B("BDEFS","DEFINITIONS","CARD",LIAM,
  "Four words before we start. Plan mode: the permission mode where writes are frozen — Claude reads, reasons, drafts a plan, and stops. "
  "Accept edits: the mode from the bare run — Claude edits and runs commands without pausing. "
  "ExitPlanMode: the tool call that hands the plan text back and asks the user to leave plan mode. "
  "Shift+Tab twice: the interactive keybinding that turns plan mode on inside the terminal UI.",
  "CCDefinitions — four terms",
  R("CCDefinitions",{"title":"TERMS IN THIS FILM","terms":[
      {"term":"plan mode","meaning":"writes frozen; Claude reads, drafts a plan, and stops"},
      {"term":"accept edits","meaning":"the bare-run mode; Claude edits and runs commands, no pause"},
      {"term":"ExitPlanMode","meaning":"the tool call that returns the plan and asks to leave plan mode"},
      {"term":"Shift+Tab ×2","meaning":"the interactive keybinding that turns plan mode on in the UI"}],
    "startCue":12,"rowGap":48}, motion="drawon", leaves_terminal_because="definitions for a chat-window audience"),
  [{"at":0.05,"event":"First term"},{"at":0.5,"event":"Terms land"},{"at":0.9,"event":"Hold"}])

B("B01","BARE — VERIFY","TERMINAL",LIAM,
  "Check the bare run. Three files touched. Index rewritten. README rewritten. And schedule.html — deleted. Sixteen lines, gone. "
  "Not badly written, that new front page. Differently than I intended. Nobody asked, and Claude filled the silence with the tidy answer.",
  "CCSession — git diff --stat, git ls-files --deleted, wc after Run A",
  R("CCSession", session("studygroup — accept edits","default",[
      {"type":"prompt","text":"!git diff --stat","cue":0,"typeDuration":30},
      {"type":"text","text":" README.md     |  2 +-"},
      {"type":"text","text":" index.html    | 12 ++++++++++--"},
      {"type":"text","text":" schedule.html | 16 --------------"},
      {"type":"text","text":" 3 files changed, 11 ins, 19 del"},
      {"type":"prompt","text":"!git ls-files --deleted","cue":0,"typeDuration":42},
      {"type":"text","text":"schedule.html"},
      {"type":"prompt","text":"!wc -l index.html schedule.html","cue":0,"typeDuration":48},
      {"type":"text","text":"      17 index.html"},
      {"type":"text","text":"wc: schedule.html: No such file"},
  ],[0,32,55,80,105,130,165,190,225,250])),
  [{"at":0.05,"event":"3 files, 11 ins, 19 del"},{"at":0.45,"event":"schedule.html deleted"},{"at":0.85,"event":"No such file"}])

B("B02","PLAN MODE — THE RUN","TERMINAL",LIAM,
  "Reset the folder. Same one-sentence ask. This time: minus minus permission mode plan. Claude reads the same four files — and this time notes.md, which the README says is teacher-only. "
  "Then it drafts a plan and calls ExitPlanMode. Its last act is to hand me the plan and ask if I want to leave plan mode. It did not edit index. It did not touch schedule. It waited.",
  "CCSession — Run B: five Reads, Write plan file, ExitPlanMode",
  R("CCSession", session("studygroup — plan mode","plan",[
      {"type":"prompt","text":ASK,"cue":0,"typeDuration":80},
      {"type":"tool","name":"Read","arg":"index.html","state":"done"},
      {"type":"tool","name":"Read","arg":"schedule.html","state":"done"},
      {"type":"tool","name":"Read","arg":"README.md","state":"done"},
      {"type":"tool","name":"Read","arg":"notes.md","state":"done"},
      {"type":"text","text":"I've read the four files. notes.md is"},
      {"type":"text","text":"teacher-only per the README. One"},
      {"type":"text","text":"decision matters before I write."},
      {"type":"tool","name":"Write","arg":"~/.claude/plans/reorganize-…","state":"done"},
      {"type":"tool","name":"ExitPlanMode","arg":"","state":"done"},
  ],[0,95,120,145,170,200,225,250,280,310])),
  [{"at":0.05,"event":"Same ask"},{"at":0.45,"event":"notes.md — teacher-only"},{"at":0.9,"event":"ExitPlanMode"}])

B("B03","PLAN MODE — VERIFY","TERMINAL",LIAM,
  "Check it. Eleven turns of Claude reading and thinking. Git diff — nothing. Git status — nothing. Ls — all four files still there, byte-identical to how I left them. "
  "The plan Claude wants to run went to a plan file in dot claude slash plans. The site did not.",
  "CCSession — git diff / status / ls, all showing untouched",
  R("CCSession", session("studygroup — plan mode","default",[
      {"type":"prompt","text":"!git diff --stat","cue":0,"typeDuration":30},
      {"type":"text","text":"(empty — no output)"},
      {"type":"prompt","text":"!git status --short","cue":0,"typeDuration":34},
      {"type":"text","text":"(empty — no output)"},
      {"type":"prompt","text":"!ls -1","cue":0,"typeDuration":22},
      {"type":"text","text":"README.md"},
      {"type":"text","text":"ask.txt"},
      {"type":"text","text":"index.html"},
      {"type":"text","text":"notes.md"},
      {"type":"text","text":"schedule.html"},
  ],[0,32,55,80,105,120,140,160,180,200])),
  [{"at":0.05,"event":"diff → empty"},{"at":0.4,"event":"status → empty"},{"at":0.85,"event":"schedule.html still there"}])

B("B04","THE PLAN, READ","SHELL",LIAM,
  "Now read the plan. Claude writes it as a document — headers, prose, files it will touch and files it won't. "
  "One line for schedule.html: delete. Same file the bare run had already removed, only this time I see the word before it happens. That's the whole feature.",
  "CCPlainShell — cat plan-b.md, the delete line",
  R("CCPlainShell",{"title":"zsh — ~/.claude/plans","lines":[
      "$ cat plan-b.md | head -20",
      "# Reorganize the classroom site —",
      "# schedule on the front page",
      "",
      "## The change",
      "**`index.html`** — replace stub with the",
      "  schedule content …",
      "**`schedule.html`** — delete. The front",
      "  page is the schedule; a separate page",
      "  is redundant …",
      "**`notes.md`** — untouched.",
      "**`README.md`** — update the file list."],
    "startCue":12,"lineGap":22}, motion="type",
    leaves_terminal_because="the plan is a text document written by Claude to ~/.claude/plans/; no CCSession contains it — the film's argument is that the plan is readable, not a UI card"),
  [{"at":0.05,"event":"cat plan-b.md"},{"at":0.55,"event":"'schedule.html — delete'"}])

B("B05","CORRECT THE PLAN","TERMINAL",LIAM,
  "Reject and revise. Still in plan mode, I resume the same session and say: no, keep schedule.html and its link, do not touch notes.md. "
  "Three turns. Thirty seconds. Twenty-seven cents. New plan, written back to the same file. Schedule.html — unchanged. Notes.md — unchanged. README — unchanged. Only index changes. And Claude flags the trade I just chose: the list now lives in two files. "
  "The correction cost less than reading it took me.",
  "CCSession — Run C: resume + plan mode, Write revised plan, ExitPlanMode",
  R("CCSession", session("studygroup — plan mode","plan",[
      {"type":"prompt","text":"No — do not delete schedule.html.","cue":0,"typeDuration":60},
      {"type":"prompt","text":"Do not touch notes.md. Revise the plan.","cue":0,"typeDuration":60},
      {"type":"tool","name":"Write","arg":"~/.claude/plans/reorganize-…","state":"done"},
      {"type":"tool","name":"ExitPlanMode","arg":"","state":"done"},
      {"type":"text","text":"Plan revised: schedule.html, notes.md,"},
      {"type":"text","text":"README.md all stay untouched."},
      {"type":"text","text":"Only index.html changes."},
      {"type":"text","text":"One trade flagged: list lives in two"},
      {"type":"text","text":"files; future edits touch both."},
  ],[0,70,130,160,190,215,240,265,290])),
  [{"at":0.05,"event":"Correction types"},{"at":0.55,"event":"Revised plan"},{"at":0.9,"event":"Trade flagged"}])

B("B06","CONDUCT — THE BOONDOGGLE SCORE","TERMINAL",LIAM,
  "Who did what. Step one, mine: one sentence, no constraints. Step two, Claude in accept-edits: three files changed and schedule.html deleted; handoff failed because the delete was silent. "
  "Step three, the dangerous middle — mine: reading the diff and seeing the file was gone. "
  "Step four, Claude in plan mode: same ask, plan text back, zero bytes changed; handoff met — the plan named the delete before it happened. "
  "Step five, mine, interpretive judgment: refuse the delete, revise the plan. Step six, Claude: revised plan, still zero bytes. Tool orchestration, one — plan mode is a tool. Executive integration, zero. Honest score.",
  "CCBoondoggleScore",
  R("CCBoondoggleScore",{"system":"one sentence · two modes","steps":[
      {"n":1,"phase":"F","labor":"human","capacity":"PF","text":"One sentence, no constraints"},
      {"n":2,"phase":"C","labor":"claude","text":"Bare: 3 files changed; schedule.html rm'd","handoff":"the delete was silent — no plan","dependsOn":[1]},
      {"n":3,"phase":"C","labor":"human","capacity":"PA","text":"Read the diff: schedule.html gone","dependsOn":[2]},
      {"n":4,"phase":"C","labor":"claude","text":"Plan mode: plan text; zero bytes changed","handoff":"plan names the delete before it happens","dependsOn":[1]},
      {"n":5,"phase":"H","labor":"human","capacity":"IJ","text":"Refuse the delete; revise the plan","dependsOn":[4]},
      {"n":6,"phase":"C","labor":"claude","text":"Revised plan: schedule.html unchanged","handoff":"only index.html changes; trade flagged","dependsOn":[5]},
  ],"dangerousMiddle":3,"distribution":True,"stepGap":22}, motion="drawon"),
  [{"at":0.05,"event":"Header"},{"at":0.4,"event":"Step 3 rings"},{"at":0.9,"event":"Tally"}])

B("B07","HUMAN — THE LEDGER","TERMINAL",LIAM,
  "So what was mine. I must read the plan, not the summary — the summary said the site was reorganized; the diff said a file was gone. "
  "I must name what unchanged means; if I don't, Claude picks the tidy answer. I must refuse a delete that costs more than thirty seconds to recover. "
  "I should keep plan mode on for the first run in an unfamiliar folder. Claude can write to disk before I read anything — it did. It can hand back a plan instead of a diff — it did. It should run in plan mode on files it hasn't seen — that's a choice I set, not one it makes.",
  "CCHumanLedger",
  R("CCHumanLedger",{"ai":[{"tier":"CAN","text":"write to disk before I read"},{"tier":"CAN","text":"hand back a plan, not a diff"},
                          {"tier":"SHOULD","text":"run in plan mode on new files"},{"tier":"SHOULD","text":"name what it would delete"}],
                    "human":[{"tier":"MUST","text":"read the plan, not the summary"},{"tier":"MUST","text":"name what 'unchanged' means"},
                             {"tier":"MUST","text":"refuse the silent delete"},{"tier":"SHOULD","text":"plan mode on new folders"}],
                    "closing":"Thirty seconds and a plan. Cheaper than any rollback.","humanCue":70,"rowGap":12}, motion="drawon"),
  [{"at":0.05,"event":"THE AI"},{"at":0.35,"event":"THE HUMAN"},{"at":0.85,"event":"Closing"}])

B("BVDT","VERDICT","BOOKEND",LIAM,
  "Let's recap with Claude. Same one-sentence ask, twice. Accept edits: three files changed, schedule.html removed, no summary reached me before the byte did. "
  "Plan mode: five reads, one plan document, zero bytes on disk; the delete named itself. Correction cost three turns and thirty seconds; the plan came back with schedule.html preserved and the new coupling flagged. "
  "What would prove this reel wrong: an accept-edits run that refuses a silent delete on its own.",
  "ClaudeVerdictArtifact",
  R("ClaudeVerdictArtifact",{"artifactTitle":"verdict.md","artifactHeading":TITLE,"artifactLines":[
      "Accept edits: 3 files changed, schedule.html rm'd, no summary before the byte.",
      "Plan mode: five reads, plan document, zero bytes on disk — the delete named itself.",
      "Correction: 3 turns, 30 seconds; revised plan preserved schedule.html and flagged the new coupling.",
      "FALSIFIABLE: an accept-edits run that refuses a silent delete on its own."]}, motion="hold"),
  [{"at":0.0,"event":"Artifact"},{"at":0.2,"event":"Lines"},{"at":0.9,"event":"Falsifiable"}], lead_silence_s=0.5)

B("BHTF","YOUR TURN","BOOKEND",LIAM,
  "Your turn. Before your next Claude Code session on a folder you care about, paste this: Turn on plan mode with Shift+Tab twice, then give me the same one-sentence ask you were about to run. "
  "Draft a plan. Name every file you will change and every file you will not touch. Do not exit plan mode until I say so.",
  "ClaudeComposerAsk",
  R("ClaudeComposerAsk",{"greeting":"Your turn.","command":"Turn on plan mode with Shift+Tab twice, then take the same one-sentence ask I was about to run. Draft a plan. Name every file you will change and every file you will not touch. Do not exit plan mode until I say so.",
      "segment":TITLE,"topic":"YOUR TURN · "+TOPIC,"runningText":"paste this into Claude Code…","output":[],"folderLabel":"@NikBearBrown","modelLabel":"Opus 5","effortLabel":"High"}),
  [{"at":0.0,"event":"Composer"},{"at":0.6,"event":"Send arms"}])

B("BOUT","OUTRO","BOOKEND",LIAM,"Plan Mode: Freeze Before the Byte Changes. Liam, in for Bear.","ClaudeTitleOutro",
  R("ClaudeTitleOutro",{"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, motion="hold"),
  [{"at":0.0,"event":"Title"},{"at":0.35,"event":"@NikBearBrown"},{"at":0.55,"event":"Mascot"}])

sheet={"metadata":{"slug":SLUG,"title":TITLE,"subtitle":"Same one-sentence ask, twice. Without plan mode: three files changed and one deleted. With it: zero bytes.",
    "topic":TOPIC,"skill":"cc-explainer","playlist":"Claude Code 101","tier":"02-plan-rewind-subagents","audience":"NikBearBrown","folderLabel":"@NikBearBrown","handle":"@NikBearBrown",
    "brand":"claude","palette":"claude","register":"Teardown","engine":"kokoro","voice_kokoro":LIAM,"persona":"liam","in_for_bear":True,
    "operator":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"closing_voice":{"name":"Liam","voice":LIAM,"engine":"kokoro"},"aspect":"16:9","fps":30,"session":"SESSION.md",
    "derived_from":"claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-plan-mode-interruption (the concept; card body replaced by three real headless runs)",
    "sources":["SESSION.md (three real runs; Run A acceptEdits, Run B plan, Run C plan+correct via --resume)","info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md","info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md"]},"beats":beats}
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
            if len(ln)>42: print("  ⚠ shell",b["beat_id"],len(ln),ln)
    if r["pattern"]=="CCHumanLedger":
        for c in ("ai","human"):
            for row in r["props"][c]:
                if len(row["text"])>30: print("  ⚠ ledger",b["beat_id"],len(row["text"]),row["text"])
    if r["pattern"]=="CCBoondoggleScore":
        for st in r["props"]["steps"]:
            if len(st["text"])>44: print("  ⚠ step",b["beat_id"],len(st["text"]),st["text"])
            if st.get("handoff") and len(st["handoff"])>44: print("  ⚠ handoff",b["beat_id"],len(st["handoff"]),st["handoff"])
    if r["pattern"]=="CCDefinitions":
        for t in r["props"]["terms"]:
            if len(t["term"])>18: print("  ⚠ defterm",b["beat_id"],len(t["term"]),t["term"])
            if len(t["meaning"])>70: print("  ⚠ defmean",b["beat_id"],len(t["meaning"]),t["meaning"])
    if r["pattern"]=="ClaudeVerdictArtifact":
        lines=r["props"]["artifactLines"]
        assert len(lines) in (4,6), f"{b['beat_id']} verdict lines must be 4 or 6, got {len(lines)}"
