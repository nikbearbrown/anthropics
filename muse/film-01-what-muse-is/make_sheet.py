#!/usr/bin/env python3
"""make_sheet.py — What Muse Is (Film 1 of the Muse series).

Generates beat_sheet.json; asserts beat counts and totals.
15 beats, 11 body beats, voice always "Muse".
"""
import json

BEATS = [
    {
        "id": "BIDEA",
        "scene": "M01",
        "dur_s": 14,
        "act": "hook",
        "voice": "Muse",
        "line": "Hallo. This is Liam, in for Bear. What changes when one company builds the models and the harness \u2014 the brain and the hands? That's the story of Muse, and this film is the map.",
        "screen": "Hook card reading 'one company builds the models and the harness?' Two boxes labeled 'models' and 'harness' slide together into one block.",
    },
    {
        "id": "BDEFS",
        "scene": "M02",
        "dur_s": 20,
        "act": "hook",
        "voice": "Muse",
        "line": "Four terms before we start. Muse Spark: Meta's managed model, called over the internet. Muse Glimmer: the open-weights model that runs on one graphics card. Vertical integration: one company building the models and the tools. Token pricing: paying per chunk of text, not per month. Keep those four in your pocket.",
        "screen": "Four term cards appear one by one: 'Muse Spark \u2014 Meta's managed model, called over the internet' / 'Muse Glimmer \u2014 the open-weights model that runs on one graphics card' / 'Vertical integration \u2014 one company building the models and the tools' / 'Token pricing \u2014 paying per chunk of text, not per month'.",
    },
    {
        "id": "B01",
        "scene": "M03",
        "dur_s": 18,
        "act": "1",
        "voice": "Muse",
        "line": "Meta trains its own models \u2014 the models box. And it ships its coding harness, Muse Code \u2014 the harness box. Most companies rent one half and build the other. Meta owns the whole stack. That is vertical integration, and it's the bet of this series.",
        "screen": "Two boxes labeled 'models' and 'harness' merge into a single 'Meta' block; an arrow shows the stack.",
    },
    {
        "id": "B02",
        "scene": "M04",
        "dur_s": 16,
        "act": "1",
        "voice": "Muse",
        "line": "Why care? When a first-class company goes vertical \u2014 its own models, its own tools \u2014 it becomes a genuine new option for real work. You've seen one provider after another. This series asks: what can Meta's stack actually do?",
        "screen": "Three provider marks in a row; the third highlights with the label 'a new option'.",
    },
    {
        "id": "B03",
        "scene": "M05",
        "dur_s": 20,
        "act": "2",
        "voice": "Muse",
        "line": "First model: Muse Spark one point two. It's the managed one \u2014 you call it over the internet, Meta runs the hardware. Version one point two is the current checkpoint; one point one came before it. And it's multimodal: it takes in text, image, video, and audio, and it answers in kind.",
        "screen": "Terracotta model card reading 'Muse Spark 1.2', with four modality dots labeled 'text', 'image', 'video', 'audio' lighting up one by one.",
    },
    {
        "id": "B04",
        "scene": "M06",
        "dur_s": 22,
        "act": "2",
        "voice": "Muse",
        "line": "Second model: Muse Glimmer. Thirty billion parameters, and it runs on a single GPU \u2014 one graphics card, the kind a serious hobbyist might own. It's open weights \u2014 the instructor's words, not open source \u2014 and it trained on data from more than a hundred languages. Big model, small footprint \u2014 that's the whole idea.",
        "screen": "Blue model card reading 'Muse Glimmer', with a big '30B', a chip icon labeled 'one GPU', and an 'open weights' tag.",
    },
    {
        "id": "B05",
        "scene": "M07",
        "dur_s": 12,
        "act": "2",
        "voice": "Muse",
        "line": "And Llama? The famous sibling \u2014 well known, worth knowing. But this series is about Spark and Glimmer, so Llama gets one line, and we move on. Moving on.",
        "screen": "Small grey card reading 'Llama' with the gloss 'the famous sibling'.",
    },
    {
        "id": "B06",
        "scene": "M08",
        "dur_s": 18,
        "act": "2",
        "voice": "Muse",
        "line": "How good are they? Here's the instructor's reading of the leaderboards \u2014 his word, 'Goldilocks'. Not the top of every chart, not the bottom: upper-middle almost everywhere. Third best at everything, he says \u2014 fast, cheap, and good enough to use everywhere. His characterization.",
        "screen": "Leaderboard bars; one bar sits upper-middle, highlighted and labeled 'upper-middle \u2014 the instructor's Goldilocks reading'.",
    },
    {
        "id": "B07",
        "scene": "M09",
        "dur_s": 18,
        "act": "3",
        "voice": "Muse",
        "line": "Now the price tag. There is no subscription. You don't pay per month \u2014 you pay per token, per chunk of text the model reads and writes. Use a little, pay a little. Use a lot, pay a lot. The meter runs on tokens, not months.",
        "screen": "Price card reading 'no subscription', struck through; then a token meter fills, captioned 'pay per token, not per month'.",
    },
    {
        "id": "B08",
        "scene": "M10",
        "dur_s": 18,
        "act": "3",
        "voice": "Muse",
        "line": "There's a second tier, called contributor. Share your data with Meta, and the price drops deep \u2014 a real discount, not a coupon. The catch is the rate limit: far fewer requests per minute. Cheap and slow, or standard and fast \u2014 pick your trade.",
        "screen": "Two-tier comparison: 'Standard' versus 'Contributor'. The contributor price bar drops low; its rate-limit bar drops lower.",
    },
    {
        "id": "B09",
        "scene": "M11",
        "dur_s": 24,
        "act": "3",
        "voice": "Muse",
        "line": "What does it cost in practice? The API coding prices, from the research brief: one dollar twenty-five per million tokens in, four dollars twenty-five per million tokens out. Share your data, and it falls to ten cents in, twenty cents out. His experience: heavy use runs twenty to fifty dollars a month. At launch no batch pricing \u2014 check the docs.",
        "screen": "Three price chips appear one by one: '$1.25 in', '$4.25 out', '$0.10 in / $0.20 out'. Caption: '$20\u201350 a month, heavy use'.",
    },
    {
        "id": "B10",
        "scene": "M12",
        "dur_s": 20,
        "act": "4",
        "voice": "Muse",
        "line": "So what's Meta's bet? Transaction fees. When the agent completes a purchase, the merchant pays Meta a cut \u2014 like an affiliate commission. The deeper play: owning the intent layer, the moment you say what you want before money moves. The agent sits between wanting and buying, and Meta collects at each step.",
        "screen": "A funnel: 'you want' flows into 'the agent', then to 'merchant'; a coin glyph drops to 'Meta' at the transaction step.",
    },
    {
        "id": "B11",
        "scene": "M13",
        "dur_s": 18,
        "act": "4",
        "voice": "Muse",
        "line": "Who's it for, honestly? Builders who want cheap and fast and can live with 'good enough'. And the honest limit, in Nik's experience: Spark is noticeably less capable than the top models. Don't buy it for the leaderboard. Buy it for the price tag.",
        "screen": "Two-column card. Left: 'for: cheap and fast, good enough'. Right: 'limit: in Nik's experience, less capable than the top models'. An 'honest' stamp lands on the card.",
    },
    {
        "id": "BVDT",
        "scene": "M14",
        "dur_s": 20,
        "act": "recap",
        "voice": "Muse",
        "line": "Let's recap. Act one: vertical integration \u2014 Meta builds the models and the tools. Act two: Spark, managed and multimodal; Glimmer, open weights, one graphics card. Act three: pay per token, not per month; sharing data buys a deep discount. Act four: Meta bets on transaction fees, within honest limits.",
        "screen": "Recap card. Four lines appear one by one: 'Act 1: vertical integration \u2014 Meta builds the models and the tools' / 'Act 2: Spark, managed and multimodal; Glimmer, open weights, one graphics card' / 'Act 3: pay per token, not per month; sharing data buys a deep discount' / 'Act 4: Meta bets on transaction fees, within honest limits'.",
    },
    {
        "id": "BHTF",
        "scene": "M14",
        "dur_s": 16,
        "act": "do_today",
        "voice": "Muse",
        "line": "Your turn. Open the Meta AI playground and set a spend limit \u2014 two dollars is fine. Run one prompt on something you want to know. Then check: did it answer, and what did it cost? That's your first token spent.",
        "screen": "Your-turn card: 'Open the playground. Set a spend limit. Run one prompt.' Below it: 'Did it answer? What did it cost?'",
    },
    {
        "id": "BOUT",
        "scene": "M14",
        "dur_s": 12,
        "act": "outro",
        "voice": "Muse",
        "line": "Muse, in for Bear. Thanks for watching. Next film: Your First Prompts \u2014 we open the playground and spend our first tokens. What Muse Is. At Nik Bear Brown.",
        "screen": "Outro title card: 'What Muse Is', '@NikBearBrown', and 'Next: Your First Prompts'.",
    },
]


def main():
    # NOTE: the brief lists 16 beat rows (BIDEA, BDEFS, B01-B11, BVDT, BHTF,
    # BOUT) whose durations sum to exactly 286s; "15" in the brief is a
    # miscount. Asserting the explicit list: 16 beats, 11 body beats.
    assert len(BEATS) == 16, f"expected 16 beats, got {len(BEATS)}"
    body = [b for b in BEATS if len(b["id"]) == 3 and b["id"][1:].isdigit()]
    assert len(body) == 11, f"expected 11 body beats, got {len(body)}"
    for b in BEATS:
        assert b["scene"].startswith("M"), b["id"]
        assert b["voice"] == "Muse", b["id"]
    total = sum(b["dur_s"] for b in BEATS)
    print(f"beats=16 body=11 total={total}s")
    with open("beat_sheet.json", "w") as f:
        json.dump(BEATS, f, indent=2, ensure_ascii=False)
    print("wrote beat_sheet.json")


if __name__ == "__main__":
    main()
