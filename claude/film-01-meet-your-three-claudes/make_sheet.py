#!/usr/bin/env python3
"""make_sheet.py — Meet Your Three Claudes (Film 1 of the Claude at Work series).

Generates beat_sheet.json; asserts beat counts and totals.
16 beats, 11 body beats, voice always "Claude" (Liam, in for Bear).
"""
import json

BEATS = [
    {
        "id": "BIDEA",
        "scene": "M01",
        "dur_s": 14,
        "act": "hook",
        "voice": "Claude",
        "line": "Hallo. This is Liam, in for Bear. One name, three places you meet it. A chat that thinks with you. A coder that ships with you. A teammate that takes the whole task. This film is the map.",
        "screen": "Hook card reading 'one name, three places you meet it?' Three boxes labeled 'chat', 'code', 'teammate' slide in side by side.",
    },
    {
        "id": "BDEFS",
        "scene": "M02",
        "dur_s": 18,
        "act": "hook",
        "voice": "Claude",
        "line": "Three terms before we start. Conversation: Claude in chat \u2014 you talk, it answers. Claude Code: the coding agent, living in your terminal. Cowork: the teammate \u2014 you delegate the outcome, it does the work. Keep those three in your pocket.",
        "screen": "Three term cards appear one by one: 'Conversation \u2014 Claude in chat, you talk, it answers' / 'Claude Code \u2014 the coding agent, living in your terminal' / 'Cowork \u2014 the teammate, you delegate the outcome, it does the work'.",
    },
    {
        "id": "B01",
        "scene": "M03",
        "dur_s": 18,
        "act": "1",
        "voice": "Claude",
        "line": "First surface: conversation. Claude in chat \u2014 the app, the website. You ask, it answers. It's where you think out loud: questions, drafts, decisions. The fastest way to meet Claude, and for most people, the first.",
        "screen": "Chat card labeled 'chat': a question bubble appears, then an answer bubble. Caption: 'thinks with you'.",
    },
    {
        "id": "B02",
        "scene": "M04",
        "dur_s": 22,
        "act": "1",
        "voice": "Claude",
        "line": "Second surface: Claude Code. It lives where the code lives \u2014 the terminal, the editor, the desktop app. It reads your repo, writes the code, runs the tests, opens the pull request. Cat Woo, who leads the product, states its mission in one line: bridge the difference between an idea and a shipped product.",
        "screen": "Terminal window card labeled 'code': a prompt line appears, then code lines, then a check mark. Quote chip: 'bridge the difference between an idea and a shipped product \u2014 Cat Woo'.",
    },
    {
        "id": "B03",
        "scene": "M05",
        "dur_s": 26,
        "act": "1",
        "voice": "Claude",
        "line": "Third surface: Cowork. Not a chat, not a terminal \u2014 a teammate. You hand it the outcome, not the steps. Then it works while you're away. Angela Jang, who leads the platform, names the difference: a harness gives the model tools, an environment, and the permission to act. It doesn't just tell you about the fix \u2014 it makes it happen.",
        "screen": "Task card labeled 'teammate': an arrow 'you hand over the outcome' points into the card; inside, small task rows check off. Quote chip: 'it doesn't just tell you about the fix \u2014 it makes it happen \u2014 Angela Jang'.",
    },
    {
        "id": "B04",
        "scene": "M06",
        "dur_s": 18,
        "act": "2",
        "voice": "Claude",
        "line": "Where does chat win? Thinking. A question with no clean answer, a draft that needs a second mind, a decision you want to argue out. It's instant, it's conversational, and it never touches your files. When you do the doing and Claude advises \u2014 that's chat.",
        "screen": "Thought bubble: three question marks collapse into one answer line. Label: 'thinks with you'.",
    },
    {
        "id": "B05",
        "scene": "M07",
        "dur_s": 20,
        "act": "2",
        "voice": "Claude",
        "line": "Where does Code win? Building. The repo is its home turf. It reads the code, writes the code, runs the tests. At Spotify, a background agent built on the same kit opens the pull requests \u2014 over a thousand a month, and migration time down ninety percent. When the doing is code, Code does it.",
        "screen": "Code file card labeled 'builds in your repo': lines appear with check marks. Stat chips: '1,000+ PRs a month', 'migration time \u221290%'.",
    },
    {
        "id": "B06",
        "scene": "M08",
        "dur_s": 24,
        "act": "2",
        "voice": "Claude",
        "line": "Where does Cowork win? Owning. Multi-step work with a finish line: research the account, draft the brief, schedule the follow-up. At Rakuten, one product manager coordinates teams of agents the way a leader manages teams of humans \u2014 and major releases ship every two weeks instead of once a quarter. You set the outcome; it runs the errands.",
        "screen": "Outcome card labeled 'owns the outcome': a progress bar fills while three task rows check off. Caption: 'while you're away'.",
    },
    {
        "id": "B07",
        "scene": "M09",
        "dur_s": 18,
        "act": "3",
        "voice": "Claude",
        "line": "So which Claude for which task? One question decides: who does the doing? If you do the doing and Claude advises \u2014 chat. If the doing is code \u2014 Claude Code. If you hand over the whole outcome \u2014 Cowork. Three surfaces, one question.",
        "screen": "Decision card: 'who does the doing?' Three branches: 'you do it \u2192 chat' / 'the doing is code \u2192 Claude Code' / 'hand over the outcome \u2192 Cowork'.",
    },
    {
        "id": "B08",
        "scene": "M10",
        "dur_s": 18,
        "act": "3",
        "voice": "Claude",
        "line": "And the mistakes, so you can skip them. Don't delegate to chat \u2014 it can advise, but it can't act. Don't brainstorm in Code \u2014 it's a builder, not a sounding board. And don't hand Cowork a vague wish \u2014 it needs the outcome, not the steps. Right surface, right job.",
        "screen": "Three crossed-out pairings with red X marks: 'delegate \u2192 chat: it can't act' / 'brainstorm \u2192 Code: it's a builder' / 'vague wish \u2192 Cowork: needs the outcome'.",
    },
    {
        "id": "B09",
        "scene": "M11",
        "dur_s": 20,
        "act": "3",
        "voice": "Claude",
        "line": "Here's the part people miss: the three stack. One task can touch all three. Think it through in chat, build it in Code, hand the rollout to Cowork. The handoff between them is the skill \u2014 and it's the subject of this whole series.",
        "screen": "Three boxes chained with arrows: 'chat' \u2192 'Code' \u2192 'Cowork'. One task token travels the chain.",
    },
    {
        "id": "B10",
        "scene": "M12",
        "dur_s": 22,
        "act": "3",
        "voice": "Claude",
        "line": "This isn't our invention. At Anthropic's Tokyo keynote, Cat Woo closed the day with the same picture: the models, the platform agents, and Claude Code \u2014 her words \u2014 three layers to one story. One assistant. Three places you meet it. Now you know which door to knock on.",
        "screen": "Quote card: 'three layers to one story' \u2014 Cat Woo, Anthropic Tokyo keynote.",
    },
    {
        "id": "B11",
        "scene": "M13",
        "dur_s": 22,
        "act": "3",
        "voice": "Claude",
        "line": "And this series walks the map in order. Next film: Delegate It \u2014 we hand Cowork its first real task and steer it mid-flight. Then scheduled tasks, tagging Claude into your team channel, the verification loop, all the way to the AI-native company. Ten films. This was the map. The walking starts now.",
        "screen": "Series map card: ten dots in a row, the first highlighted; caption 'Next: Delegate It'.",
    },
    {
        "id": "BVDT",
        "scene": "M14",
        "dur_s": 16,
        "act": "recap",
        "voice": "Claude",
        "line": "Let's recap. Chat thinks with you \u2014 you do the doing. Code builds in your repo \u2014 the doing is code. Cowork owns delegated outcomes \u2014 you hand over the finish line. One question picks the surface: who does the doing?",
        "screen": "Recap card. Four lines appear one by one: 'Chat: thinks with you \u2014 you do the doing' / 'Code: builds in your repo \u2014 the doing is code' / 'Cowork: owns outcomes \u2014 you hand over the finish line' / 'One question: who does the doing?'",
    },
    {
        "id": "BHTF",
        "scene": "M14",
        "dur_s": 18,
        "act": "do_today",
        "voice": "Claude",
        "line": "Your turn. Pick one real task on your list \u2014 something small, something this week. Ask the one question: who does the doing? Write down which Claude gets it, and why. Then check: did the surface match the job?",
        "screen": "Your-turn card: 'Pick one task. Ask: who does the doing?' Below it: 'Which Claude gets it \u2014 and why?'",
    },
    {
        "id": "BOUT",
        "scene": "M14",
        "dur_s": 14,
        "act": "outro",
        "voice": "Claude",
        "line": "Claude, in for Bear. Thanks for watching. Next film: Delegate It \u2014 we hand Cowork its first real task and steer it mid-flight. Meet Your Three Claudes. At Nik Bear Brown.",
        "screen": "Outro title card: 'Meet Your Three Claudes', '@NikBearBrown', and 'Next: Delegate It'.",
    },
]

if __name__ == "__main__":
    body = len([b for b in BEATS if b["act"] not in ("hook", "recap", "do_today", "outro")])
    total = sum(b["dur_s"] for b in BEATS)
    assert len(BEATS) == 16, f"expected 16 beats, got {len(BEATS)}"
    assert body == 11, f"expected 11 body beats, got {body}"
    assert all(b["voice"] == "Claude" for b in BEATS), "all beats voice Claude"
    with open("beat_sheet.json", "w") as f:
        json.dump(BEATS, f, indent=2, ensure_ascii=False)
    print(f"wrote beat_sheet.json: {len(BEATS)} beats, {body} body, {total}s planned")
