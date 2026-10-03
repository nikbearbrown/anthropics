#!/usr/bin/env python3
"""make_sheet.py — Muse Code, the Harness (Film 9).
Generates beat_sheet.json; asserts beat counts and totals.
"""
import json

BEATS = [
    dict(id="BIDEA", scene="M01", dur_s=16, act="hook", voice="Muse",
         line=("Hello. This is Liam, in for Bear. Meta built the models, "
               "then built the harness to run them in. Muse Code: Meta's own "
               "coding harness, speaking Muse natively. Let's install it and "
               "see what it does."),
         screen=("Hook card reading 'Meta's own coding harness'. A "
                 "terminal-window glyph slides in beside it.")),
    dict(id="BDEFS", scene="M02", dur_s=20, act="hook", voice="Muse",
         line=("Four terms. Harness: the loop around the model — tools, "
               "permissions, sessions. Agents dot m d: project context — the "
               "file where a project tells the agent how it works. Reasoning "
               "effort: how hard the model thinks — low, medium, high, extra "
               "high. Session: a working conversation you can resume, "
               "compact, or clear. Keep those four."),
         screen=("Four term cards appear one by one: 'Harness — the loop "
                 "around the model' / 'agents.md — project context' / "
                 "'Reasoning effort — low, medium, high, extra high' / "
                 "'Session — work you can resume'.")),
    dict(id="B01", scene="M03", dur_s=20, act="1", voice="Muse",
         line=("Act one: installation. Muse Code installs with a single "
               "command. The docs carry the exact line; what matters is the "
               "shape of it — one line, run once, and a coding agent lands in "
               "your terminal. No installer wizard, no account form. The "
               "barrier to entry is basically typing."),
         screen=("A terminal card; a single command line types itself: '$ "
                 "one line, run once'.")),
    dict(id="B02", scene="M04", dur_s=20, act="1", voice="Muse",
         line=("First launch. Open a terminal, type muse, and you're in: a "
               "prompt, a cursor, a model behind it. It reads the folder "
               "you're standing in. So ask it about your code — it answers "
               "with your files in view, not from its memory of the "
               "internet."),
         screen=("A terminal prompt reading 'muse>' with a blinking cursor; "
                 "the folder opens and unlabeled file rectangles fan out.")),
    dict(id="B03", scene="M05", dur_s=18, act="1", voice="Muse",
         line=("Then: skills. Muse Code loads skills from everywhere — your "
               "project, your home folder, the community. A skill is a packet "
               "of instructions: do this task this way. They fire on their "
               "own when the job matches. You don't call them. The agent "
               "does."),
         screen=("Three skill packets labeled 'project', 'home', and "
                 "'community' fly into the terminal from three sides.")),
    dict(id="B04", scene="M06", dur_s=20, act="2", voice="Muse",
         line=("Every project gets a voice. Run muse init and it writes an "
               "agents.md file — project context the agent reads every "
               "session. What's this repo? How do you build it? What are the "
               "rules? Write it once, in plain English, and every session "
               "starts smart."),
         screen=("An agents.md file card; three rows appear: 'what's this "
                 "repo' / 'how to build it' / 'what are the rules'.")),
    dict(id="B05", scene="M07", dur_s=18, act="2", voice="Muse",
         line=("Beyond the project: settings.json. Global settings on your "
               "machine. Defaults live here — including your reasoning effort "
               "default. Plus trust files: which folders the agent may touch "
               "without asking. Machine-level rules, set once, enforced "
               "always. It's the difference between a helpful guest and a "
               "helpful employee with a key."),
         screen=("A settings.json card; two keys appear: 'reasoning_effort: "
                 "medium' / 'trust: ~/projects'.")),
    dict(id="B06", scene="M08", dur_s=20, act="2", voice="Muse",
         line=("Reasoning effort: four stops. Low, medium, high, extra high. "
               "Set a default in settings, or change it per session. Low for "
               "quick answers, extra high for the gnarly bug. More effort "
               "costs more tokens and more time — so you spend it where it "
               "pays."),
         screen=("A four-step dial: 'low' / 'medium' / 'high' / 'extra "
                 "high'; the highlight moves from low to extra high while a "
                 "token bar grows.")),
    dict(id="B07", scene="M09", dur_s=20, act="3", voice="Muse",
         line=("Sessions. Your work with the agent is a session — and "
               "sessions survive. Close the laptop, come back tomorrow, and "
               "resume exactly where you left off. The plan, the open files, "
               "the dead ends: all still there. Nothing to re-explain. That "
               "persistence is what turns a chatbot into a colleague."),
         screen=("A session timeline: a dot, an arrow across a gap, and a "
                 "second dot labeled 'resume'.")),
    dict(id="B08", scene="M10", dur_s=18, act="3", voice="Muse",
         line=("Two session tools to know. Status: tokens used, context "
               "percentage — how full the agent's working memory is. Compact: "
               "when it gets full, squeeze the conversation into a summary "
               "and keep going. Clear: wipe the board and start fresh. Watch "
               "the percentage; it tells you when to compact."),
         screen=("A status card reading 'tokens used' with a meter reading "
                 "'context 62%'; an arrow squeezes the meter — compact.")),
    dict(id="B09", scene="M11", dur_s=20, act="3", voice="Muse",
         line=("Then: YOLO mode. Full permissions, no sandbox, no asking. The "
               "agent edits, runs, and installs whatever it wants. Fast — and "
               "dangerous. His rule: YOLO only on a machine you can lose. "
               "The sandbox exists because the agent is powerful, not "
               "because it is broken. Speed is never worth a production "
               "database."),
         screen=("A red card reading 'YOLO mode' with 'full permissions · "
                 "no sandbox' and a warning triangle; a green card beside it "
                 "reading 'a machine you can lose'.")),
    dict(id="B10", scene="M12", dur_s=22, act="3", voice="Muse",
         line=("Last: headless mode. Minus p. You pipe a prompt in and get "
               "JSON out — no interactive session at all. Prompts can live in "
               "files. Now the agent is a Unix tool: script it, chain it, "
               "schedule it. The harness becomes infrastructure."),
         screen=("A pipeline: 'prompt' flows into 'muse -p', which flows "
                 "out to 'JSON'; the arrow pulses along the pipe.")),
    dict(id="BVDT", scene="M13", dur_s=20, act="recap", voice="Muse",
         line=("Three acts, one line each. One: one command installs it, "
               "launch is a terminal prompt, skills load from everywhere. "
               "Two: agents.md teaches it your project, settings.json holds "
               "the global rules, effort has four stops. Three: sessions "
               "resume, compact manages memory, YOLO stays on disposable "
               "machines, headless makes it a tool."),
         screen=("Three recap rows appear: 'one command installs it' / "
                 "'agents.md + settings.json + four effort stops' / "
                 "'sessions resume · YOLO stays on disposable machines · "
                 "headless is a tool'.")),
    dict(id="BHTF", scene="M13", dur_s=16, act="do_today", voice="Muse",
         line=("Today: install it. Launch it in a project folder. Ask it one "
               "question about your own code — no task yet, just a question. "
               "Watch what it reads before it answers. That is the whole "
               "skill: watching what the agent looks at."),
         screen=("A 'your turn: one question' card.")),
    dict(id="BOUT", scene="M13", dur_s=12, act="outro", voice="Muse",
         line=("Muse, in for Bear. Thanks for watching. Next film: Memory, "
               "Skills, and Guardrails — where we teach the agent to "
               "remember."),
         screen=("Outro card: 'Muse, in for Bear. Thanks for watching.' "
                 "plus 'Next: Memory, Skills, and Guardrails'.")),
]

body = [b for b in BEATS if b["id"].startswith("B0") or b["id"][1:].isdigit()]
body = [b for b in BEATS if b["id"] not in ("BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT")]
assert len(BEATS) == 15, f"expected 15 beats, got {len(BEATS)}"
assert len(body) == 10, f"expected 10 body beats, got {len(body)}"
assert all(b["scene"].startswith("M") for b in BEATS)
assert all(b["voice"] == "Muse" for b in BEATS)
assert all(12 <= b["dur_s"] <= 30 or b["id"] in ("BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT")
           for b in BEATS)

total = sum(b["dur_s"] for b in BEATS)
print(f"beats={len(BEATS)} body={len(body)} total={total}s")
with open("beat_sheet.json", "w") as f:
    json.dump(BEATS, f, indent=2)
print("wrote beat_sheet.json")
