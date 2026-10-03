#!/usr/bin/env python3
"""make_sheet.py — Agents and Frameworks (Film 8).
Generates beat_sheet.json; asserts beat counts and totals.
"""
import json

BEATS = [
    dict(id="BIDEA", scene="M01", dur_s=18, act="hook", voice="Muse",
         line=("Hallo. This is Liam, in for Bear. You don't have to abandon "
               "your tools to use Muse. Today: drop the model into the agent "
               "tools you already use — SDKs, frameworks, even a harness "
               "built for someone else's models."),
         screen=("Hook card reading 'drop Muse into tools you already use'. "
                 "Three small cards appear one by one: 'SDKs', 'frameworks', "
                 "'a harness'.")),
    dict(id="BDEFS", scene="M02", dur_s=22, act="hook", voice="Muse",
         line=("Four terms. Agent SDK: code that runs an agentic loop for "
               "you — it plans, calls tools, and keeps going. Framework: a "
               "bigger toolkit — chains, memory, tools. Harness: the outer "
               "program driving the model, the cockpit around the model. "
               "Wrapper: a script that adapts one tool to someone else's "
               "expectations. Keep all four in your pocket."),
         screen=("Four term cards appear one by one: 'Agent SDK — runs an "
                 "agentic loop for you' / 'Framework — chains, memory, tools' "
                 "/ 'Harness — the cockpit around the model' / 'Wrapper — a "
                 "script that adapts one tool'.")),
    dict(id="B01", scene="M03", dur_s=20, act="1", voice="Muse",
         line=("First stop: the agent SDK. It's the loop Anthropic wrote for "
               "its own models — plan, call tools, iterate. Pointed at Muse, "
               "it doesn't care whose name is on the SDK. An agent loop is "
               "an agent loop. So he handed it a coding task and let it drive."),
         screen=("A card reading 'the agent SDK'. Below, three loop nodes "
                 "appear one by one with arrows: 'plan', 'call tools', "
                 "'iterate'.")),
    dict(id="B02", scene="M04", dur_s=22, act="1", voice="Muse",
         line=("The task: tic-tac-toe, in Ruby. Small enough to read in one "
               "sitting, big enough to need real decisions — game state, win "
               "checking, a game loop that doesn't fall over. He didn't write "
               "the code. He described the job and let the loop drive: try "
               "it, check it, fix it, repeat."),
         screen=("A terminal card reading 'tic-tac-toe, in Ruby'. Three "
                 "checklist rows appear one by one: 'game state', 'win "
                 "checking', 'game loop'.")),
    dict(id="B03", scene="M05", dur_s=20, act="1", voice="Muse",
         line=("And it worked. The loop played its own game to the end: a "
               "finished game, from a description — tic-tac-toe, in Ruby. "
               "That's the SDK's whole pitch: you name the destination and "
               "the loop handles the driving. The model was interchangeable. "
               "The harness did the work."),
         screen=("A tic-tac-toe grid draws itself; X and O marks land in "
                 "turn. A green check appears beside it, captioned 'a "
                 "finished game, from a description'.")),
    dict(id="B04", scene="M06", dur_s=18, act="2", voice="Muse",
         line=("Second stop: LangChain, in TypeScript. LangChain speaks to "
               "models through an OpenAI-compatible integration, and Muse "
               "ships one too. Same calls, same shapes — so the framework "
               "that expects OpenAI just works, pointed somewhere else. No "
               "rewrite of your chains. Just a different address."),
         screen=("Three cards with arrows between: 'LangChain' arrow "
                 "'OpenAI-compatible integration' arrow 'Muse'.")),
    dict(id="B05", scene="M07", dur_s=20, act="2", voice="Muse",
         line=("The move is one config block: base URL, API key, model name. "
               "Point the integration at Muse's address, hand it your key, "
               "name the model. Everything downstream — chains, prompts, "
               "memory — stays exactly as it was. That's the trick of "
               "compatibility: the plumbing doesn't know the difference."),
         screen=("A config card; three rows appear one by one: 'base URL', "
                 "'API key', 'model name'. An arrow points from the card to a "
                 "'Muse' card.")),
    dict(id="B06", scene="M08", dur_s=22, act="2", voice="Muse",
         line=("When it broke, he debugged it with the agent SDK's help. "
               "Same loop that ran the coding task, now reading the error "
               "and pointing at the fix. The debugger and the patient were "
               "the same machine — paste the failure in, get the repair out. "
               "That's the part people miss: the loop doesn't just write, "
               "it reads."),
         screen=("A red-bordered card reading 'the error'; a speech bubble; "
                 "then a green check beside a card reading 'the fix'.")),
    dict(id="B07", scene="M09", dur_s=20, act="3", voice="Muse",
         line=("Third stop: the boldest one. Claude Code is Anthropic's "
               "harness, built for Anthropic's models. A small wrapper "
               "script injects the Meta API key through the environment and "
               "launches Claude Code pointed at Muse Spark one point two. "
               "A foreign harness, driving a Meta model."),
         screen=("Two cards, 'Claude Code' and 'wrapper script', with an "
                 "arrow to a card reading 'Muse Spark 1.2'.")),
    dict(id="B08", scene="M10", dur_s=20, act="3", voice="Muse",
         line=("He launched it and gave it a small refactor task — nothing "
               "heroic, just real work. The harness booted, the model "
               "answered, the loop ran. It edited files, it ran checks, it "
               "reported back. From the inside, the harness couldn't tell "
               "the model wasn't the one it was built for."),
         screen=("A terminal card reading 'a small refactor task'; three "
                 "progress dots fill in; a green check lands beside the "
                 "caption 'the harness couldn't tell'.")),
    dict(id="B09", scene="M11", dur_s=22, act="3", voice="Muse",
         line=("And his verdict was honest: it works, but it looks odd. The "
               "harness assumes things about the model behind it — its "
               "habits, its phrasing, its pace — and when a different model "
               "sits in the chair, you feel the mismatch. Compatibility gets "
               "you running. It doesn't get you native. Know which one "
               "you've got."),
         screen=("Two cards side by side: 'it works' with a green check; "
                 "'it looks odd', tilted, with a wavy line.")),
    dict(id="BVDT", scene="M12", dur_s=22, act="recap", voice="Muse",
         line=("Let's recap. Act one: the agent SDK drove a coding task end "
               "to end — a finished game, from a description. Act two: "
               "LangChain, pointed at Muse with one config block, debugged "
               "with the agent SDK's help. Act three: a wrapper launched "
               "Claude Code on Muse Spark — compatible, not native."),
         screen=("A recap card; three lines appear one by one: 'act one — "
                 "the SDK drove the task' / 'act two — one config block' / "
                 "'act three — compatible, not native'.")),
    dict(id="BHTF", scene="M12", dur_s=22, act="do_today", voice="Muse",
         line=("Your turn. Take one tool you already use — a framework, a "
               "harness, anything that talks to a model — and point it at "
               "the Muse base URL. Run the smallest real task it can do. "
               "Then ask: did it just work, or did it look odd? That answer "
               "tells you what you've actually bought."),
         screen=("A your-turn card: 'point one tool you already use' / 'at "
                 "the Muse base URL'. Below: 'did it just work,' / 'or did "
                 "it look odd?'")),
    dict(id="BOUT", scene="M12", dur_s=12, act="outro", voice="Muse",
         line=("Muse, in for Bear. Thanks for watching. Next film: Muse "
               "Code, the Harness — the cockpit Meta built for its own "
               "models. Agents and Frameworks. At Nik Bear Brown."),
         screen=("Outro title card: 'Agents and Frameworks', "
                 "'@NikBearBrown', and 'Next: Muse Code, the Harness'.")),
]


def main():
    assert len(BEATS) == 14, f"expected 14 beats, got {len(BEATS)}"
    # body beats are B01..B09
    body = [b for b in BEATS if len(b["id"]) == 3 and b["id"][1:].isdigit()]
    assert len(body) == 9, f"expected 9 body beats, got {len(body)}"
    for b in BEATS:
        assert b["scene"].startswith("M"), b["id"]
        assert b["voice"] == "Muse", b["id"]
        assert 12 <= b["dur_s"] <= 30, (b["id"], b["dur_s"])
    total = sum(b["dur_s"] for b in BEATS)
    assert 280 <= total <= 330, f"total {total}s outside 280-330s"
    with open("beat_sheet.json", "w") as f:
        json.dump(BEATS, f, indent=2)
        f.write("\n")
    print(f"beats={len(BEATS)} body={len(body)} total={total}s")


if __name__ == "__main__":
    main()
