#!/usr/bin/env python3
"""make_sheet.py — Delegate It: Your First Cowork Task (Film 2 of the Claude at Work series).

Generates beat_sheet.json; asserts beat counts and totals.
15 beats, 10 body beats, voice always "Claude" (Liam, in for Bear).
Teardown register. Numbers written as spoken words.
"""
import json

BEATS = [
    {
        "id": "BIDEA",
        "scene": "M01",
        "dur_s": 14,
        "act": "hook",
        "voice": "Claude",
        "line": "Hallo. This is Liam, in for Bear. It is five minutes to one, and you have a call with Acme Corp at one. Zero prep done. This film is about the move you make instead of panicking: you delegate the prep.",
        "screen": "Hook card: a clock reading '1:00 PM', an 'Acme Corp call' chip, and a terracotta stamp reading 'prep: none'. An arrow points from the stamp to a terracotta task card reading 'delegate the prep'.",
    },
    {
        "id": "BDEFS",
        "scene": "M02",
        "dur_s": 15,
        "act": "hook",
        "voice": "Claude",
        "line": "The terms. Cowork is the Claude surface that takes the whole task. You connect your calendar, Slack, and email once. Then you hand it the outcome, not the steps. This film: your first delegation, and how you steer it while it runs.",
        "screen": "Terracotta 'Cowork' card in the center; three chips labeled 'calendar', 'Slack', 'email' slide in and plug into it. Caption: 'you delegate the outcome, not the steps'.",
    },
    {
        "id": "B01",
        "scene": "M03",
        "dur_s": 24,
        "act": "1",
        "voice": "Claude",
        "line": "Here is the delegation, word for word. Prep me for today's call with Acme Corp at one. Search the calendar for the meeting. Research who I'm meeting with. Check Slack for recent threads about the account. Review my previous meeting notes. Create an agenda \u2014 and match the format of the docs already in the folder.",
        "screen": "Instruction card reading 'Prep me for today's call with Acme Corp at one'. Five directive chips appear below it: 'calendar search', 'attendee research', 'Slack threads', 'meeting notes', 'match folder format'.",
    },
    {
        "id": "B02",
        "scene": "M04",
        "dur_s": 18,
        "act": "1",
        "voice": "Claude",
        "line": "Claude makes a plan exactly as directed. Calendar search. Attendee research. Slack and previous-notes review. A task list, worked top to bottom. And here is the part chat cannot give you: it starts working while you go do something else.",
        "screen": "A task list with four rows; each row gains a green check mark in sequence. Caption: 'it starts working while you do something else'.",
    },
    {
        "id": "B03",
        "scene": "M05",
        "dur_s": 22,
        "act": "2",
        "voice": "Claude",
        "line": "Halfway through, you realize you forgot a source. You tell Claude: check my email for additional context on this account. In chat, you would have to stop the action, wait, and regenerate from scratch. Here, Claude pivots mid-task and keeps going. Nothing is thrown away.",
        "screen": "The task list returns with two rows checked; a new row 'check email' slides into the middle and the remaining rows keep their progress. Beside it, a 'chat' panel reading 'stop, wait, start over' is crossed out; a terracotta panel reads 'pivot mid-task'.",
    },
    {
        "id": "B04",
        "scene": "M06",
        "dur_s": 18,
        "act": "2",
        "voice": "Claude",
        "line": "Claude finishes and shares the agenda. But it does not just hand you a doc. It calls out the decisions to push for during the meeting, your biggest win to lead with, and the watch items to keep an eye on. Prep, plus judgment.",
        "screen": "A document card titled 'Acme Corp \u2014 agenda'. Three callout chips slide in beside it: 'push for: decisions', 'lead with: biggest win', 'watch: watch items'.",
    },
    {
        "id": "B05",
        "scene": "M07",
        "dur_s": 24,
        "act": "2",
        "voice": "Claude",
        "line": "Open the file. It read the existing agendas in your folder and matched the structure \u2014 same headings, same bullet hierarchy. Attendees came from the calendar, contacts from Slack, and the feedback it found in email. There is even a blank action-items section, ready to fill in during the call.",
        "screen": "Two document outlines side by side: 'existing format' with three heading bars, an arrow, and 'your agenda' with matching heading bars. Below, three source arrows: 'calendar \u2192 attendees', 'Slack \u2192 contacts', 'email \u2192 feedback'. A dashed box reads 'action items (blank)'.",
    },
    {
        "id": "B06",
        "scene": "M08",
        "dur_s": 20,
        "act": "2",
        "voice": "Claude",
        "line": "Then you spot what is missing: the pricing conversation from last Tuesday. You tell Claude: add the pricing update from last Tuesday's Slack thread \u2014 that is going to come up. It finds the thread and folds it into the brief. Second steer, same file, no restart.",
        "screen": "A Slack thread card reading 'last Tuesday \u2014 pricing' with an arrow folding it into the agenda document card. A stamp reads 'no restart'.",
    },
    {
        "id": "B07",
        "scene": "M09",
        "dur_s": 20,
        "act": "3",
        "voice": "Claude",
        "line": "Now the handoff. You can make your final edits through Claude, or open the file and change it yourself. Either way works. Claude does the prep work, but the final document is yours to own. That is the line: it prepares, you decide.",
        "screen": "The agenda document card with a terracotta stamp reading 'yours to own'. Two arrows leave it: 'via Claude' and 'yourself'. Caption: 'it prepares, you decide'.",
    },
    {
        "id": "B08",
        "scene": "M10",
        "dur_s": 22,
        "act": "3",
        "voice": "Claude",
        "line": "Name the move, because you will use it everywhere. Delegate the outcome. Connect your tools once. Steer mid-flight \u2014 never start over. Chat gives you answers; Cowork takes the task. The difference is who does the doing while you do something else.",
        "screen": "A rule card with four lines: 'delegate the outcome', 'connect tools once', 'steer mid-flight', 'never start over'. Below, two panels: 'chat \u2014 answers' in grey, 'Cowork \u2014 takes the task' in terracotta.",
    },
    {
        "id": "B09",
        "scene": "M11",
        "dur_s": 18,
        "act": "3",
        "voice": "Claude",
        "line": "Make your first delegation a bounded one. Something with a clear output \u2014 a brief, a summary, a draft. Something with a deadline, so you can check the work. Meeting prep is the perfect first task: it has a shape, a clock, and you own the final version.",
        "screen": "A 'good first task' card with three checked rows: 'clear output', 'a deadline', 'you own the final'. A terracotta chip reads 'meeting prep' with a check mark.",
    },
    {
        "id": "B10",
        "scene": "M12",
        "dur_s": 22,
        "act": "3",
        "voice": "Claude",
        "line": "The boring part that makes it all work: connect your calendar, Slack, and email once. Point Claude at the folder where your meeting notes live. After that, delegating is one sentence. Do the setup today, so the next one-pm call is already handled.",
        "screen": "Three connector chips \u2014 'calendar', 'Slack', 'email' \u2014 merge into one 'connected once' card; an arrow leads to a card reading 'one sentence to delegate'. Caption: 'do the setup today'.",
    },
    {
        "id": "BVDT",
        "scene": "M13",
        "dur_s": 13,
        "act": "recap",
        "voice": "Claude",
        "line": "Four lines to keep. Delegate the outcome, not the steps. Connect your tools once. Steer mid-flight \u2014 never start over. Own the final document.",
        "screen": "Recap card with the four rule lines, each appearing in turn.",
    },
    {
        "id": "BHTF",
        "scene": "M13",
        "dur_s": 17,
        "act": "do_today",
        "voice": "Claude",
        "line": "Your turn. Pick one meeting this week and hand Cowork the prep. Calendar, Slack, email, one sentence: prep me for this call. See what comes back, then steer it once and watch what happens.",
        "screen": "A 'your turn' card: 'pick one meeting this week', 'hand Cowork the prep', 'steer it once'.",
    },
    {
        "id": "BOUT",
        "scene": "M13",
        "dur_s": 15,
        "act": "outro",
        "voice": "Claude",
        "line": "Claude, in for Bear. Thanks for watching. Next film: While You Were Away \u2014 we set a task to run on its own schedule, and it catches up while you sleep. Delegate It. At Nik Bear Brown.",
        "screen": "Outro title card: 'Delegate It', '@NikBearBrown', and 'Next: While You Were Away'.",
    },
]

BEAT_IDS = ["BIDEA", "BDEFS", "B01", "B02", "B03", "B04", "B05", "B06", "B07",
            "B08", "B09", "B10", "BVDT", "BHTF", "BOUT"]
SCENES = ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09",
          "M10", "M11", "M12", "M13"]

if __name__ == "__main__":
    assert [b["id"] for b in BEATS] == BEAT_IDS, "beat ids mismatch"
    assert len(BEATS) == 15, "must be 15 beats"
    assert all(b["voice"] == "Claude" for b in BEATS), "voice must be Claude"
    assert all(b["scene"] in SCENES for b in BEATS), "unknown scene"
    body = [b for b in BEATS if b["act"] not in ("hook", "recap", "do_today", "outro")]
    assert len(body) == 10, f"must be 10 body beats, got {len(body)}"
    total = sum(b["dur_s"] for b in BEATS)
    print(f"15 beats, 10 body, planned {total}s ({total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BEATS, f, indent=2, ensure_ascii=False)
    print("wrote beat_sheet.json")
