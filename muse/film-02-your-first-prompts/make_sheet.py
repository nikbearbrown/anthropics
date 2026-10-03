#!/usr/bin/env python3
"""make_sheet.py — Your First Prompts (Film 2 of the Muse series).

Generates beat_sheet.json; asserts beat counts and totals.
"""
import json

BEATS = [
    {
        "id": "BIDEA",
        "scene": "M01",
        "dur_s": 14,
        "act": "hook",
        "voice": "Muse",
        "line": "Hallo. This is Liam, in for Bear. You've met the models \u2014 now meet the place where you talk to them: the playground, at dev dot meta dot ai. You are here.",
        "screen": "Browser card 'dev.meta.ai' with cursor; tag 'you are here'.",
    },
    {
        "id": "BDEFS",
        "scene": "M02",
        "dur_s": 20,
        "act": "hook",
        "voice": "Muse",
        "line": "Four terms before we start. Playground: the web app where you prompt the model. Spend limit: the cap you set on your card. Reasoning effort: how hard the model thinks, from low to extra high. Prompt: the text you send it. Keep those four in your pocket.",
        "screen": "Four term cards appear one by one: 'Playground \u2014 the web app where you prompt the model' / 'Spend limit \u2014 the cap you set on your card' / 'Reasoning effort \u2014 how hard the model thinks, from low to extra high' / 'Prompt \u2014 the text you send it'.",
    },
    {
        "id": "B01",
        "scene": "M03",
        "dur_s": 18,
        "act": "1",
        "voice": "Muse",
        "line": "First, the account. You connect, you attach a card, and you set a spend limit. Not a deposit \u2014 a cap. Thirty dollars, five dollars, whatever you're comfortable with. The meter runs against that cap, and that's the whole setup.",
        "screen": "Account card: card chip plus spend-limit slider at '$30'; tag 'a cap, not a deposit'.",
    },
    {
        "id": "B02",
        "scene": "M04",
        "dur_s": 16,
        "act": "1",
        "voice": "Muse",
        "line": "Here's the friendly part: no five-dollar minimum, unlike other providers. Nothing is charged until you've spent about a dollar. Want to experiment with two dollars? You absolutely can \u2014 no minimum at all.",
        "screen": "'$5 minimum' struck through; '$1' coin; tag 'no minimum'.",
    },
    {
        "id": "B03",
        "scene": "M05",
        "dur_s": 18,
        "act": "2",
        "voice": "Muse",
        "line": "Inside the playground, four controls matter. The model picker \u2014 one point two or one point one. Reasoning effort. Streaming. And the toggles: grounded search, JSON schema. Learn these four and the playground is yours. Everything else is decoration.",
        "screen": "Control panel: four dials light up one by one \u2014 'model picker', 'effort', 'streaming', 'toggles'.",
    },
    {
        "id": "B04",
        "scene": "M06",
        "dur_s": 26,
        "act": "2",
        "voice": "Muse",
        "line": "Your first prompt should test something you already know. His test: the grammar points for the J L P T N five exam. The model came back with forty grammar points \u2014 particles, sentence structures \u2014 clean and well formatted. He saved that list. That's the move: ask about something you can judge, and judge it hard.",
        "screen": "Prompt card 'JLPT N5 grammar points?' \u2014 forty rows appear in two waves; check_mark stamp.",
    },
    {
        "id": "B05",
        "scene": "M07",
        "dur_s": 22,
        "act": "2",
        "voice": "Muse",
        "line": "Reasoning effort is the dial. Low for quick questions, medium for everyday work, high and extra high when the problem is genuinely hard. He runs extra high for fun \u2014 and admits medium would have done. Turn the dial to match the problem, not your mood.",
        "screen": "Dial arc 'low \u2192 medium \u2192 high \u2192 extra high'; needle moves; tag 'match the problem'.",
    },
    {
        "id": "B06",
        "scene": "M08",
        "dur_s": 18,
        "act": "2",
        "voice": "Muse",
        "line": "Read the output like a practitioner, not a fan. Does it answer what you asked? Is the formatting actually good? He kept that grammar list \u2014 not because it was perfect, but because it earned a second look. Keep what earns it.",
        "screen": "Practitioner checklist: 'answer?', 'formatting?', 'second look?' \u2014 check_marks one by one.",
    },
    {
        "id": "B07",
        "scene": "M09",
        "dur_s": 24,
        "act": "3",
        "voice": "Muse",
        "line": "So what does five dollars buy? His experience: he ran the whole course \u2014 hours of extra-high reasoning \u2014 and barely dented a hundred dollars. Five dollars is hundreds of prompts at normal effort. The cheapest lab bench in AI, and it's not close. Experiment freely.",
        "screen": "Big '$5'; prompt-count bars grow tall; tag 'hundreds of prompts'.",
    },
    {
        "id": "B08",
        "scene": "M10",
        "dur_s": 18,
        "act": "3",
        "voice": "Muse",
        "line": "Watch the meter. Every prompt costs tokens in and tokens out, and extra-high reasoning multiplies both. His habit: don't track every cent \u2014 know the shape of it. The expensive habit isn't prompting. It's prompting at extra high by default.",
        "screen": "Token meter: 'in' bar and 'out' bar; 'extra high' chip triples both bars.",
    },
    {
        "id": "B09",
        "scene": "M11",
        "dur_s": 18,
        "act": "4",
        "voice": "Muse",
        "line": "The playground has friction, and it's honest friction. No copy button \u2014 you copy by hand. No pasting images directly \u2014 you save the file and attach it. It's a lab bench, not a chat app. Know the edges before they annoy you.",
        "screen": "Friction list, greyed rows: 'no copy button', 'save and attach', 'lab bench, not chat app'.",
    },
    {
        "id": "B10",
        "scene": "M12",
        "dur_s": 20,
        "act": "4",
        "voice": "Muse",
        "line": "And know when to leave. The playground is for learning what the model can do. When you want the same call inside your own code, you take an API key and go programmatic. That's later films' territory. This one ends at the playground door.",
        "screen": "'API key' card \u2192 arrow \u2192 'your code' card.",
    },
    {
        "id": "BVDT",
        "scene": "M13",
        "dur_s": 20,
        "act": "recap",
        "voice": "Muse",
        "line": "Let's recap. One: the account \u2014 card on file, spend limit set, no minimum. Two: the controls \u2014 model, effort, streaming, toggles. Three: the meter \u2014 tokens in and out, and five dollars goes a long way. Four: the edges \u2014 honest friction, and code comes next.",
        "screen": "Recap card, four lines one by one: '1 card on file \u00b7 spend limit \u00b7 no minimum' / '2 model \u00b7 effort \u00b7 streaming \u00b7 toggles' / '3 tokens in and out \u00b7 five dollars goes a long way' / '4 honest friction \u00b7 code comes next'.",
    },
    {
        "id": "BHTF",
        "scene": "M13",
        "dur_s": 16,
        "act": "do_today",
        "voice": "Muse",
        "line": "Your turn. Open the playground. Set a two-dollar spend limit. Run one prompt on something you actually know. Then check: did it answer well, and what did the meter say? That's your first real experiment.",
        "screen": "Your-turn card: 'Open the playground. Set a spend limit. Run one prompt.' Below: 'Did it answer well? What did the meter say?'",
    },
    {
        "id": "BOUT",
        "scene": "M13",
        "dur_s": 12,
        "act": "outro",
        "voice": "Muse",
        "line": "Muse, in for Bear. Thanks for watching. Next film: Muse Can See \u2014 we feed it images and make it build a website. Your First Prompts. At Nik Bear Brown.",
        "screen": "Outro title card: 'Your First Prompts', '@NikBearBrown', 'Next: Muse Can See'.",
    },
]


def main():
    assert len(BEATS) == 15, f"expected 15 beats, got {len(BEATS)}"
    body = [b for b in BEATS if len(b["id"]) == 3 and b["id"][1:].isdigit()]
    assert len(body) == 10, f"expected 10 body beats, got {len(body)}"
    for b in BEATS:
        assert b["scene"].startswith("M"), b["id"]
        assert b["voice"] == "Muse", b["id"]
        assert 12 <= b["dur_s"] <= 30 or b["id"] in ("BIDEA", "BDEFS"), b["id"]
    total = sum(b["dur_s"] for b in BEATS)
    assert 280 <= total <= 330, f"total {total}s out of envelope"
    print(f"beats=15 body=10 total={total}s")
    with open("beat_sheet.json", "w") as f:
        json.dump(BEATS, f, indent=2, ensure_ascii=False)
    print("wrote beat_sheet.json")


if __name__ == "__main__":
    main()
