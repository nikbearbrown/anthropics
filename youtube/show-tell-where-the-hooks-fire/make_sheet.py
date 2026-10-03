#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-where-the-hooks-fire.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #25 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md ("Hook Events", "Exit Codes",
"Hook Input Format", "Matchers") and anthropics/claude-code/examples/hooks/bash_command_validator_example.py, read in
full; every event, input field and exit-code claim confirmed against Anthropic's hooks reference
(code.claude.com/docs/en/hooks, fetched 2026-09-27), which wins where the SKILL.md copy is out of date.
A plain primer: ~10 deep films already touch hooks. #13 (the Ralph loop) builds on the Stop hook, so B08 ends on
Stop but stands alone.
Cast: the SESSION as a pale BELT (dark-kraft edges) running right-up; Claude as a dark BLOCK on it; the tool as a
dark MACHINE at the end of a spur belt running toward the viewer; hooks as ink GATE arches across the belts, each with
a lamp (ghost, terracotta when it fires) and a kraft DOOR that drops to block; a script PAGE clipped beside a gate;
prompt, call and result SLIPS riding the belts; a kraft PRESS behind the belt (compaction); a settings CARD; a JSON CARD.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Where the Hooks Fire"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.4, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Picture a Claude Code session as a belt. Your prompt rides in to Claude. Claude calls a tool, like Bash, and the result rides back. Then Claude answers, and the turn stops.",
      "B00_Belt", "A pale belt draws in, running right-up ('session'); Claude's dark block drops onto it ('Claude'); a spur belt runs toward the viewer to a dark tool machine ('tool'); a prompt slip rides in to Claude; a call slip rides down the spur, the machine's lights come on, and a result slip rides back; an answer slip rides on to the belt's far end.",
      [{"at": 0.1, "event": "the session is a belt"}, {"at": 0.3, "event": "a prompt rides in to Claude"}, {"at": 0.55, "event": "a tool call and its result"}, {"at": 0.85, "event": "Claude answers and stops"}]),
 beat("B01", "A hook is a checkpoint on that belt: a command you attach to a named point, called an event. Every time the session passes that point, Claude Code runs your command. Claude doesn't choose.",
      "B01_Checkpoint", "An ink gate arch rises across the spur ('hook'); a script page clips on beside it ('your command'); a call slip rides through and the gate's lamp flashes terracotta; a second slip rides through and it flashes again; Claude's block stays still.",
      [{"at": 0.1, "event": "a hook: a checkpoint"}, {"at": 0.35, "event": "a command at a named point"}, {"at": 0.65, "event": "every pass, it runs"}, {"at": 0.9, "event": "Claude doesn't choose"}]),
 beat("B02", "Three events follow the turn. Session start, when a session begins or resumes. User prompt submit, when you send a prompt, before Claude reads it. And stop, when Claude finishes responding.",
      "B02_Turn", "Three gates rise on the main belt in turn: at its start ('SessionStart'), before Claude ('UserPromptSubmit'), and after Claude ('Stop'); a slip rides through each as it is named and its lamp lights.",
      [{"at": 0.1, "event": "events that follow the turn"}, {"at": 0.3, "event": "SessionStart"}, {"at": 0.55, "event": "UserPromptSubmit"}, {"at": 0.85, "event": "Stop"}]),
 beat("B03", "Two fire on every tool call: pre tool use, before the call runs, and post tool use, after it succeeds. Pre compact fires just before a long conversation is compacted. The docs list more.",
      "B03_Tools", "The spur gets two gates: one before the machine ('PreToolUse') and one after it on the way back ('PostToolUse'); a call and its result ride through them; a kraft press behind the belt lowers its plate onto a tray of slips ('PreCompact') and its lamp lights; two pale ghost gates appear at the belt's end (the docs list more).",
      [{"at": 0.1, "event": "every tool call"}, {"at": 0.25, "event": "PreToolUse"}, {"at": 0.45, "event": "PostToolUse"}, {"at": 0.75, "event": "PreCompact"}, {"at": 0.92, "event": "more in the docs"}]),
 beat("B04", "Hooks live in a settings file, under their event. A matcher picks which tools a hook watches. With the matcher Bash, a Bash call trips it. An Edit call rides straight past.",
      "B04_Matcher", "A settings card slides in ('settings.json'); the PreToolUse gate's label lands and its lamp flashes; a matcher line on the card gets a terracotta dot and an ink underline; a Bash slip rides in ('Bash') and the lamp flashes; an Edit slip rides in ('Edit') and passes with the lamp dark.",
      [{"at": 0.1, "event": "a settings file"}, {"at": 0.35, "event": "a matcher"}, {"at": 0.6, "event": "Bash trips it"}, {"at": 0.85, "event": "Edit rides past"}]),
 beat("B05", "When a hook fires, Claude Code hands your command a JSON note on standard input: the session, the event's name, and for a tool call, the tool's name and its input. Here, the exact command.",
      "B05_Stdin", "A call slip stops at the PreToolUse gate; a JSON card grows out of it into the open lower right ('stdin'); its rows fill one by one; the tool-name row and the input row get ink ticks ('tool_name', 'tool_input'); the input row's bar lengthens (the exact command).",
      [{"at": 0.1, "event": "a JSON note on stdin"}, {"at": 0.4, "event": "session, event name"}, {"at": 0.7, "event": "tool name and input"}, {"at": 0.9, "event": "the exact command"}]),
 beat("B06", "Your command answers with an exit code. Zero: carry on. Two: block. At pre tool use, two stops the call, and what you print to standard error goes to Claude as the reason. Other codes don't block.",
      "B06_Exit", "A slip reaches the gate ('exit 0'): the lamp lights and it rides through. A second slip ('exit 2'): the kraft door drops, the slip stops, and a small note flies back up the spur to Claude. A third ('other'): the door stays up and it rides through.",
      [{"at": 0.1, "event": "an exit code"}, {"at": 0.25, "event": "0: carry on"}, {"at": 0.45, "event": "2: block, stderr to Claude"}, {"at": 0.85, "event": "other codes don't block"}]),
 beat("B07", "Anthropic's example hook watches Bash. If a command starts with grep, it prints, use r g instead, and exits two. The call never runs. Claude reads the note, and can try again with r g.",
      "B07_Grep", "A slip labelled 'grep' rides to the PreToolUse gate; the door drops ('exit 2') and the slip fades where it stopped; a note flies back to Claude; Claude sends a new slip labelled 'rg'; the door lifts, it rides through, and the machine's lights come on.",
      [{"at": 0.1, "event": "Anthropic's example watches Bash"}, {"at": 0.35, "event": "grep: exit 2"}, {"at": 0.6, "event": "the call never runs"}, {"at": 0.85, "event": "Claude can retry with rg"}]),
 beat("B08", "Exit code two means something different at each event. At user prompt submit, it blocks the prompt and erases it. At post tool use, the tool already ran, so Claude just sees the note. Session start can't block. And stop keeps Claude working, with your note as the reason.",
      "B08_Stop", "The UserPromptSubmit door drops and a prompt slip vanishes; at PostToolUse the machine's lights are already on as a note flies to Claude; at SessionStart the lamp lights but no door drops; at Stop the door drops, and the answer slip turns back to Claude, whose light comes on again.",
      [{"at": 0.1, "event": "exit 2 differs by event"}, {"at": 0.25, "event": "UserPromptSubmit: erased"}, {"at": 0.5, "event": "PostToolUse: the tool already ran"}, {"at": 0.7, "event": "SessionStart can't block"}, {"at": 0.9, "event": "Stop keeps Claude working"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 3.4, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Ciao. This is Liam, in for Bear. It's easy to think Claude decides when to run a hook. It doesn't. Claude Code runs your hook each time the session passes a set point. So the real question is when Claude passes a hook checkpoint.",
    "BrutalistHesitantWriter",
    {"text": "When does Claude\ndecide to run a hook?", "triggerWords": "decide to run a hook", "replacementWords": "pass a hook checkpoint",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'When does Claude decide to run a hook?'"}, {"at": 0.6, "event": "backspaces 'decide to run a hook' -> 'pass a hook checkpoint' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (when does Claude decide to run a hook) and corrects it to the real one (when does Claude pass a hook checkpoint).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A hook: a command Claude Code runs for you at a set point. An event: that named point, like pre tool use. A matcher: which tools a hook watches. And an exit code: the number your command ends with. Two means block.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "hook", "meaning": "a command Claude Code runs for you at a set point"},
               {"term": "event", "meaning": "the named point where it runs, like PreToolUse"},
               {"term": "matcher", "meaning": "which tools a hook watches, like Bash"},
               {"term": "exit code", "meaning": "the number your command ends with; 2 blocks"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'hook' lands"}, {"at": 0.35, "event": "'event' lands"}, {"at": 0.6, "event": "'matcher' lands"}, {"at": 0.8, "event": "'exit code' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Add a PreToolUse hook to this project's .claude/settings.json with the matcher Bash. It runs a Python script "
             "that reads the JSON on stdin. If tool_input.command starts with rm -rf, it prints a reason to stderr and exits 2. "
             "Otherwise it exits 0. Then give me a one-line test that pipes a fake rm -rf call into the script and prints the exit code.")
SPOKEN_PROMPT = (YT_PROMPT.replace("PreToolUse", "pre tool use").replace(".claude/settings.json", "dot claude slash settings dot json")
                 .replace(".claude/hooks", "dot claude slash hooks").replace("tool_input.command", "tool input dot command")
                 .replace("rm -rf", "R M dash R F").replace("stdin", "standard input").replace("stderr", "standard error"))
CHECKS = ["Check: the fake rm -rf call exits 2?",
          "Check: /hooks lists it under PreToolUse?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + SPOKEN_PROMPT + " Then check two things yourself. Does the fake call "
    "exit with code two? And does the slash hooks menu list your hook under pre tool use?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": "Where the Hooks Fire", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn belt-and-gates scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {f"B0{i}" for i in range(1, 9)}   # B01-B08 measured 0.65-0.79 fill with no Gate V defect (local pre-check, 2026-09-27); B00 opens at 0.53, so it keeps the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · HOOKS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Claude Code users and students who have heard of hooks and want the plain mechanism: where they fire, what they receive, and what exit code 2 does",
    "source_doc": "anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md and anthropics/claude-code/examples/hooks/bash_command_validator_example.py (read in full 2026-09-27); code.claude.com/docs/en/hooks (fetched 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude Code", "hooks", "PreToolUse", "PostToolUse", "UserPromptSubmit", "SessionStart", "Stop hook", "PreCompact",
             "exit code 2", "matcher", "settings.json", "bash command validator", "Anthropic", "Claude", "Nik Bear Brown"]},
    "beats": B}

# keep measured audio fields across re-runs (audio-first: never lose the clock)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in B:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in B)), "s")
