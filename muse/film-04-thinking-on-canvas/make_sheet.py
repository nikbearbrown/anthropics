#!/usr/bin/env python3
"""make_sheet.py — Thinking on Canvas (Film 4).
Generates beat_sheet.json; asserts beat counts and totals.
"""
import json

BEATS = [
    dict(id="BIDEA", scene="M01", dur_s=14, act="hook", voice="Muse",
         line=("Hallo. This is Liam, in for Bear. What if your brainstorming "
               "partner could draw? Not just list ideas — sketch how they fit "
               "together. That's what we're doing today: thinking on canvas."),
         screen=("Hook card reading 'a brainstorming partner that draws'. "
                 "A speech bubble and a pencil glyph slide together into one mark.")),
    dict(id="BDEFS", scene="M02", dur_s=22, act="hook", voice="Muse",
         line=("Four terms before we start. Brainstorm: throwing out ideas "
               "fast, judging later. Mermaid: a way to describe diagrams in "
               "plain text. Mind map: ideas branching out from one center. "
               "Iteration: going around again, each pass sharper. Keep those "
               "four in your pocket."),
         screen=("Four term cards appear one by one: 'Brainstorm — throwing "
                 "out ideas fast, judging later' / 'Mermaid — diagrams in "
                 "plain text' / 'Mind map — ideas branching from one center' "
                 "/ 'Iteration — each pass sharper'.")),
    dict(id="B01", scene="M03", dur_s=20, act="1", voice="Muse",
         line=("It started with a vague ask. The website looked great, but "
               "the plugins were boring — all about performance. So he asked: "
               "make the plugins funner. Give me single bullet ideas I can "
               "review. Back came a list: deploy confessions, a coffee match, "
               "a code review thunderdome, a kudos terminal."),
         screen=("A vague blob labeled 'make the plugins funner', then an "
                 "arrow, then four idea rows appear one by one: 'deploy "
                 "confessions' / 'coffee match' / 'thunderdome' / 'kudos "
                 "terminal', each with a dot bullet.")),
    dict(id="B02", scene="M04", dur_s=20, act="1", voice="Muse",
         line=("Then he did the important part: he judged them. Some were "
               "good. One made no sense at all — his words: I don't "
               "understand that part, but that's okay. A brainstorm isn't a "
               "shopping list. The judging is the work. Keep what sparks, "
               "drop what doesn't, and say so out loud."),
         screen=("The four idea rows get verdicts one by one: a green check, "
                 "a green check, a greyed-out row reading 'huh?', a green "
                 "check.")),
    dict(id="B03", scene="M05", dur_s=18, act="1", voice="Muse",
         line=("Then he picked what to draw. A list tells you what's there. "
               "A picture tells you how it fits. So instead of more examples, "
               "he asked for a visual: a mind map of the whole landscape of "
               "community engagement. One center, branches everywhere."),
         screen=("One idea row gets a terracotta ring; an arrow points to an "
                 "empty canvas frame labeled 'draw this'.")),
    dict(id="B04", scene="M06", dur_s=22, act="2", voice="Muse",
         line=("He asked for it as a mermaid diagram — diagrams described in "
               "plain text, so the model can write them. Out came the map: "
               "one center node, community, with branches growing off it. "
               "Learning, experimentation, participation — the skeleton of "
               "everything a community site could be."),
         screen=("A mind-map tree grows: a terracotta center node labeled "
                 "'community', then five blue branch nodes appear one by one.")),
    dict(id="B05", scene="M07", dur_s=24, act="2", voice="Muse",
         line=("Then he read the map like a local. Learning and growth: "
               "daily challenges, skill building. Participation: ask "
               "questions, debate chambers, shout boxes. Identity and "
               "belonging: who's online, your stack, your presence. "
               "Recognition: being seen. Five branches — and suddenly the "
               "vague idea of engagement had a shape you could point at."),
         screen=("Branch labels land on the nodes one by one: 'learning and "
                 "growth' / 'experimentation' / 'participation' / 'identity "
                 "and belonging' / 'recognition'.")),
    dict(id="B06", scene="M08", dur_s=26, act="2", voice="Muse",
         line=("Then deeper. For the outermost branches, he asked for two to "
               "three grounded plugin examples each — real, concrete, with "
               "examples — and had each branch colored uniquely so he could "
               "tell them apart. The leaves landed branch by branch. This is "
               "the move: the map gives you the territory, then you populate "
               "it, one branch at a time, until the abstract becomes a build "
               "list."),
         screen=("Each branch sprouts two to three green leaf nodes, "
                 "color-coded per branch; the leaves appear branch by branch.")),
    dict(id="B07", scene="M09", dur_s=22, act="2", voice="Muse",
         line=("Then the tooling fought back. Pasting the diagram into his "
               "editor failed, again and again. New folder, a preview plugin, "
               "and finally it rendered. His verdict, and it's worth quoting: "
               "the mermaid part, not the model. The model produced what he "
               "wanted. When your diagram won't render, blame the editor first."),
         screen=("Two cards: 'the model' gets a green check; 'the editor' "
                 "gets a red cross, with glitch marks on the editor card.")),
    dict(id="B08", scene="M10", dur_s=22, act="3", voice="Muse",
         line=("And here's the loop the whole session was really about. Ask: "
               "throw out the vague request. Draw: make the model show you "
               "the shape of it. Refine: push back — deeper, grounded, "
               "clearer — and watch it revise. He asked for more depth and "
               "got the deepest leaf set yet. Each pass sharper than the last."),
         screen=("A loop diagram: three nodes reading 'ask', 'draw', "
                 "'refine', with arrows cycling round; one arrow lights per step.")),
    dict(id="B09", scene="M11", dur_s=20, act="3", voice="Muse",
         line=("That's thinking on canvas. The model isn't just answering "
               "questions — it's holding the whiteboard while you think. A "
               "list is a starting point. A map is a shared picture. And a "
               "shared picture is something you can argue with, improve, and "
               "eventually build from."),
         screen=("A canvas frame with a small tree sketch inside and a "
                 "lightbulb glyph above, captioned 'thinking on canvas'.")),
    dict(id="BVDT", scene="M12", dur_s=22, act="recap", voice="Muse",
         line=("Let's recap. Act one: ask for ideas in bullets, then judge "
               "them out loud. Act two: draw the landscape as a mind map, "
               "then populate the branches with grounded examples. Act three: "
               "when the tooling breaks, blame the tool — and loop ask, draw, "
               "refine until it's sharp."),
         screen=("A recap card; three lines appear one by one: 'ask, then "
                 "judge out loud' / 'draw the map, populate the branches' / "
                 "'loop ask, draw, refine'.")),
    dict(id="BHTF", scene="M12", dur_s=18, act="do_today", voice="Muse",
         line=("Your turn. Pick one idea you've been carrying around. Ask for "
               "three variations of it. Then ask the model to draw the best "
               "one as a diagram. Then check: does the picture show you "
               "something the list didn't?"),
         screen=("A your-turn card: 'Pick one idea. Ask for three "
                 "variations. Ask it to draw the best one.' Below: 'Does the "
                 "picture show you something the list didn't?'")),
    dict(id="BOUT", scene="M12", dur_s=12, act="outro", voice="Muse",
         line=("Muse, in for Bear. Thanks for watching. Next film: Grounded "
               "Answers — we ask the model about car parts, with and without "
               "the internet. Thinking on Canvas. At Nik Bear Brown."),
         screen=("Outro title card: 'Thinking on Canvas', '@NikBearBrown', "
                 "and 'Next: Grounded Answers'.")),
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
