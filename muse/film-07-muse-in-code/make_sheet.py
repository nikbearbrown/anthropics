#!/usr/bin/env python3
"""make_sheet.py — Muse in Code (Film 7).
Generates beat_sheet.json; asserts beat counts and totals.
"""
import json

BEATS = [
    dict(id="BIDEA", scene="M01", dur_s=16, act="hook", voice="Muse",
         line=("Hallo. This is Liam, in for Bear. The playground is lovely, "
               "but it's a sandbox. Today we take Muse out of it: one API "
               "key, three ways to call it, and the error messages that "
               "teach you the rest. From the playground to a program."),
         screen=("Hook card reading 'from the playground to a program'. A "
                 "sandbox box with an arrow leading out of it.")),
    dict(id="BDEFS", scene="M02", dur_s=22, act="hook", voice="Muse",
         line=("Four terms before we start. API key: a secret string that "
               "says who you are. Base URL: the address your code calls "
               "instead of OpenAI's. SDK: someone else's wrapper around raw "
               "HTTP. REST: talking to the API directly, no wrapper at all. "
               "Keep those four in your pocket."),
         screen=("Four term cards appear one by one: 'API key — a secret "
                 "string that says who you are' / 'Base URL — the address "
                 "your code calls' / 'SDK — a wrapper around raw HTTP' / "
                 "'REST — talking to the API directly'.")),
    dict(id="B01", scene="M03", dur_s=20, act="1", voice="Muse",
         line=("First, the key. In the Meta developer console you generate "
               "an API key — a long secret string. Copy it once. It won't "
               "show again. Put it in your environment, never in your code. "
               "Everything after this assumes that key exists."),
         screen=("A key glyph — a circle with a stem — beside a card of "
                 "masked characters reading 'copy it once'.")),
    dict(id="B02", scene="M04", dur_s=22, act="1", voice="Muse",
         line=("Second, the address. If you've used the OpenAI SDK before, "
               "you already know the base URL — the domain your requests go "
               "to. Muse speaks the same chat-completions dialect, so you "
               "just swap the base URL. One quirk, though: there is no "
               "slash-v-one path segment to append. The domain alone is the "
               "endpoint."),
         screen=("A card reading 'base URL' with '/v1' struck through, then "
                 "an arrow to a card reading 'muse base url — no /v1'.")),
    dict(id="B03", scene="M05", dur_s=26, act="2", voice="Muse",
         line=("Way one: raw REST. One HTTP POST to the endpoint. Headers: "
               "authorization with your key, content type JSON. Body: the "
               "model name, plus your messages. What comes back is JSON with "
               "the answer inside. No library, no install, nothing to break. "
               "If you can send a POST request, you can call Muse."),
         screen=("A card reading 'POST' with an arrow to a card reading "
                 "'JSON', and an arrow back: the request and the answer.")),
    dict(id="B04", scene="M06", dur_s=24, act="2", voice="Muse",
         line=("Way two: the OpenAI SDK — the one you probably already have "
               "installed. Set the base URL to the Muse endpoint, set the "
               "API key, and write the exact same chat-completions call you "
               "already write. The code doesn't change. Only the address "
               "changes. That is the whole point of speaking the same "
               "dialect."),
         screen=("Two code cards with an arrow between them: the first reads "
                 "'same call', the second reads 'base URL' — the call "
                 "unchanged, only the address swapped.")),
    dict(id="B05", scene="M07", dur_s=26, act="2", voice="Muse",
         line=("Way three: the Anthropic SDK. Same idea, different shape. "
               "Here the calls are messages, not chat completions — a "
               "messages array, each entry with a role. System instructions "
               "go in the system role, not developer; your words go in the "
               "user role. And you set max tokens explicitly. Same dialect "
               "family, different grammar — and it works."),
         screen=("A messages card with three rows appearing one by one: "
                 "'role: system' / 'role: user' / 'max tokens'.")),
    dict(id="B06", scene="M08", dur_s=26, act="2", voice="Muse",
         line=("And when it breaks — and it will break — read the error "
               "messages. They say what's wrong: a bad key, a wrong model "
               "name, a malformed messages array. The instructor debugged "
               "his calls exactly this way: run it, read the error, fix the "
               "one thing, run it again. The error message is the "
               "documentation you actually read."),
         screen=("Two error rows, each fixed in turn: 'bad key' gets a "
                 "green check, then 'malformed messages' gets a green "
                 "check.")),
    dict(id="B07", scene="M09", dur_s=22, act="3", voice="Muse",
         line=("So which way should you use? Honestly: REST is enough. The "
               "SDKs are thin wrappers around the same HTTP calls. They add "
               "convenience, not capability. If you're writing a script, a "
               "POST request does everything. Save the SDK for the codebase "
               "where you're already living inside one."),
         screen=("Two cards side by side: 'REST' and 'SDK'. A terracotta "
                 "ring lands on 'REST'.")),
    dict(id="B08", scene="M10", dur_s=22, act="3", voice="Muse",
         line=("One last thing. There is no first-party Meta SDK for Muse — "
               "and that's deliberate, in the instructor's reading. The API "
               "speaks dialects other tools already understand, so the "
               "ecosystem's wrappers just work. No new dependency to learn. "
               "The API is the SDK."),
         screen=("A box reading 'first-party SDK' with a cross over it, "
                 "then a card below reading 'the API is the SDK'.")),
    dict(id="BVDT", scene="M11", dur_s=24, act="recap", voice="Muse",
         line=("Three acts, three lines. Act one: the key from the console, "
               "and the base URL with no slash-v-one. Act two: three ways "
               "to call it — raw REST, the OpenAI SDK, the Anthropic SDK "
               "port — and the error messages that teach you the rest. Act "
               "three: REST is enough, and there's no first-party SDK "
               "because the dialects you already speak just work."),
         screen=("Three recap rows, each gaining a green check: 'act one — "
                 "key, base URL' / 'act two — three ways, errors' / 'act "
                 "three — REST is enough'.")),
    dict(id="BHTF", scene="M11", dur_s=18, act="do_today", voice="Muse",
         line=("Your turn. Tonight, make one API call from your own code — "
               "any of the three ways. Print what comes back. That's it. "
               "Once you've done it once, the API stops being something "
               "you read about and becomes something you use."),
         screen=("A single card reading 'tonight: one API call' with a "
                 "terracotta dot beside it.")),
    dict(id="BOUT", scene="M11", dur_s=14, act="outro", voice="Muse",
         line=("Muse, in for Bear. Thanks for watching. Next film: Agents "
               "and Frameworks — dropping Muse into the tools you already "
               "use."),
         screen=("Outro card: '@NikBearBrown' with the watermark, and "
                 "'Next film: Agents and Frameworks'.")),
]

if __name__ == "__main__":
    beats = BEATS
    assert len(beats) == 13, f"expected 13 beats, got {len(beats)}"
    body = [b for b in beats if b["id"].startswith("B") and b["id"][1:].isdigit()]
    assert len(body) == 8, f"expected 8 body beats, got {len(body)}"
    for b in beats:
        assert b["scene"].startswith("M"), f"scene must start with M: {b['id']}"
        assert b["voice"] == "Muse", f"voice must be Muse: {b['id']}"
        if b["id"][1:].isdigit():
            assert 12 <= b["dur_s"] <= 30, f"body beat out of range: {b['id']}"
    total = sum(b["dur_s"] for b in beats)
    assert 280 <= total <= 330, f"total out of range: {total}"
    print(f"beats={len(beats)} body={len(body)} total={total}s")
    with open("beat_sheet.json", "w") as f:
        json.dump(beats, f, indent=2)
    print("wrote beat_sheet.json")
