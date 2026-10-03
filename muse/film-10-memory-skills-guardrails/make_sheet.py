"""make_sheet.py — Memory, Skills, and Guardrails (Film 10).
Embeds the beat dict, asserts counts, prints totals, writes beat_sheet.json."""
import json

BEATS = [
    {"id": "BIDEA", "scene": "M01_Bidea", "dur_s": 14, "act": "hook",
     "voice": "Muse",
     "line": "Here's the thing about a coding agent. Every new session, it's a stranger. It doesn't know your preferences, your rules, your project. Unless you teach it once. And it remembers.",
     "screen": "Hook card: 'teach it once. it remembers.' — a notebook card merges with a session dot inside a ring"},
    {"id": "BDEFS", "scene": "M02_Bdefs", "dur_s": 20, "act": "hook",
     "voice": "Muse",
     "line": "Four terms. Memory — notes the harness reads every session, so you stop repeating yourself. Skill — a reusable bundle of instructions the agent can call on. Approval mode — who says yes before a risky action. MCP — Model Context Protocol, plugs that connect the agent to outside tools.",
     "screen": "Four term cards appear one by one: Memory / Skill / Approval mode / MCP, one-line gloss each"},
    {"id": "B01", "scene": "M03_B01Memory", "dur_s": 18, "act": "1",
     "voice": "Muse",
     "line": "Act one: memory. Muse Code keeps project memory in a memory dot md file, sitting in your project. Every session, the harness reads it first. Your preferences, your conventions, your hard rules — loaded before the first prompt. Teach once, applied always.",
     "screen": "A 'memory.md' file card; three session dots appear one by one, each with an arrow from the card"},
    {"id": "B02", "scene": "M04_B02Css", "dur_s": 22, "act": "1",
     "voice": "Muse",
     "line": "The example from the transcript: one CSS rule. He taught the project how he wants his CSS written. Done right, he said — one line in memory, and every future session writes CSS his way. That is the pitch of project memory: small rules, compounded over every session you will ever run.",
     "screen": "The memory.md card gains the line 'the CSS rule'; an arrow leads to a plate of written-line glyphs with a green check"},
    {"id": "B03", "scene": "M05_B03Where", "dur_s": 20, "act": "1",
     "voice": "Muse",
     "line": "Where does memory live? Project memory travels with the repo — memory dot md, checked in, shared with the team. Global memory follows you instead. The rule of thumb: memory is for things that are always true. True only today? Put it in the prompt.",
     "screen": "Two plates: 'project: memory.md' and 'global'; the project plate gets a check"},
    {"id": "B04", "scene": "M06_B04Skill", "dur_s": 22, "act": "2",
     "voice": "Muse",
     "line": "Act two: skills. A skill is a bundle of instructions you write once, and the agent triggers on its own. You create it like any other file — name, description, the steps. And the harness loads skills from everywhere: yours, the project's, the community's. Your own private toolbelt.",
     "screen": "Three mini-cards 'name', 'description', 'steps' stack one by one, then slide into a frame labeled 'toolbelt'"},
    {"id": "B05", "scene": "M07_B05Trigger", "dur_s": 20, "act": "2",
     "voice": "Muse",
     "line": "Triggering is the magic part. You never call the skill — the agent notices when it fits and pulls it in. The description is the trigger: write it well, and the skill fires exactly when it should. Write it badly, and it never fires at all.",
     "screen": "The 'description' card lights up; a bell labeled 'trigger' rings; an arrow fires into the agent dot with a check"},
    {"id": "B06", "scene": "M08_B06Plugin", "dur_s": 20, "act": "2",
     "voice": "Muse",
     "line": "And here is the bigger idea hiding inside skills. If anyone can write one, and the harness loads them from everywhere, then a skill is basically a plugin. The community's best workflows, packaged and shared. The ecosystem grows without the vendor lifting a finger.",
     "screen": "Skill cards slide in from the left one by one into a frame labeled 'plugin'"},
    {"id": "B07", "scene": "M09_B07Approvals", "dur_s": 22, "act": "3",
     "voice": "Muse",
     "line": "Act three: guardrails. An agent that runs code needs a leash. Approval modes decide who says yes. On request — it asks before the risky stuff. Untrusted — it asks when the input looks shady. Never — and you had better know what you are doing, because it will not ask at all.",
     "screen": "Header 'approval modes'; three cards appear one by one: 'on request', 'untrusted', 'never'"},
    {"id": "B08", "scene": "M10_B08Sandbox", "dur_s": 22, "act": "3",
     "voice": "Muse",
     "line": "Then the sandbox. Muse Code runs inside bubblewrap — a container around every command. The agent can work, but it cannot wander. The contrast case: YOLO mode. Full permissions, no sandbox, no questions. Fast — and exactly as dangerous as it sounds. Learn where the off switch is before you need it.",
     "screen": "A terminal plate inside a 'sandbox' box; beside it a 'YOLO mode' card gets a red cross"},
    {"id": "B09", "scene": "M11_B09Mcp", "dur_s": 18, "act": "3",
     "voice": "Muse",
     "line": "MCP servers are how the agent reaches outside tools. Model Context Protocol — one standard plug. You add a server in settings, restart the harness, and new tools appear. The promise: any tool, one protocol, no custom wiring.",
     "screen": "Header 'MCP'; a plug slides into a socket; three tool dots pop out one by one"},
    {"id": "B10", "scene": "M12_B10Duck", "dur_s": 22, "act": "3",
     "voice": "Muse",
     "line": "But the DuckDuckGo lesson. He wired up a search server, it connected fine — and the source still would not cooperate. Bot walls, token walls, the works. The lesson: MCP working is not the same as the source working. The plug is connected; the faucet is dry. Debug the source, not the protocol.",
     "screen": "Two cards: 'MCP' with a green check, 'the source' with a red cross and a dry droplet"},
    {"id": "BVDT", "scene": "M13_BvdtHtfOut", "dur_s": 20, "act": "recap",
     "voice": "Muse",
     "line": "Recap. Act one: project memory — teach it once in memory dot md, applied every session. Act two: skills — bundles the agent triggers itself, and the description is the trigger. Act three: guardrails — approval modes, the bubblewrap sandbox, and MCP. The plug is not the faucet.",
     "screen": "Recap card: 3 lines appear one by one"},
    {"id": "BHTF", "scene": "M13_BvdtHtfOut", "dur_s": 16, "act": "do_today",
     "voice": "Muse",
     "line": "Your turn. Two small jobs. One: add a single memory rule to your project — something that is always true. Two: write one skill for a task you repeat. Then watch the agent trigger it without being asked.",
     "screen": "Your-turn card: 'one memory rule. one skill. watch it trigger.'"},
    {"id": "BOUT", "scene": "M13_BvdtHtfOut", "dur_s": 12, "act": "outro",
     "voice": "Muse",
     "line": "Muse, in for Bear. Thanks for watching. Next film: Capstone — Ship a Full-Stack App.",
     "screen": "Outro card '@NikBearBrown' + 'Next film: Capstone — Ship a Full-Stack App'"},
]

BODY_IDS = {"B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10"}

assert len(BEATS) == 15, f"expected 15 beats, got {len(BEATS)}"
body = [b for b in BEATS if b["id"] in BODY_IDS]
assert len(body) == 10, f"expected 10 body beats, got {len(body)}"
assert all(b["scene"].startswith("M") for b in BEATS), "scene ids must start with M"
assert all(b["voice"] == "Muse" for b in BEATS), "voice must be Muse"
assert all(12 <= b["dur_s"] <= 30 for b in body), "body beats must be 12-30s"
total = sum(b["dur_s"] for b in BEATS)
assert 280 <= total <= 330, f"total {total}s outside 280-330s envelope"

with open("beat_sheet.json", "w") as f:
    json.dump(BEATS, f, indent=2)
    f.write("\n")

print(f"beats={len(BEATS)} body={len(body)} total={total}s")
print("wrote beat_sheet.json")
