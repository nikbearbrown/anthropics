"""make_sheet.py — Capstone: Ship a Full-Stack App (Film 11).
Embeds the beat dict, asserts counts, prints totals, writes beat_sheet.json."""
import json

BEATS = [
    {"id": "BIDEA", "scene": "M01_Bidea", "dur_s": 14, "act": "hook",
     "voice": "Muse",
     "line": "This is the film where everything comes together. One idea. One backend doc. And at the end: a real app, running in containers. From idea to running containers — let's ship something.",
     "screen": "Hook card: 'from idea to running containers' — an idea dot becomes a container box"},
    {"id": "BDEFS", "scene": "M02_Bdefs", "dur_s": 20, "act": "hook",
     "voice": "Muse",
     "line": "Four terms. Goal — a feature that decomposes into steps and drives the build. Stack — the tools you commit to: Go, SQLite, React. Compose — Docker Compose, one file that stands up every service. Endpoint — a URL your backend answers.",
     "screen": "Four term cards appear one by one: Goal / Stack / Compose / Endpoint, one-line gloss each"},
    {"id": "B01", "scene": "M03_B01Doc", "dur_s": 20, "act": "1",
     "voice": "Muse",
     "line": "Act one: the plan. Before a single line of code, he wrote a backend doc — what the app is, what it stores, what it answers. An agent builds exactly what you describe. Describe sloppily, get slop. The doc is the contract.",
     "screen": "A 'backend doc' card; an arrow leads to a 'contract' stamp that gets a check"},
    {"id": "B02", "scene": "M04_B02Stack", "dur_s": 20, "act": "1",
     "voice": "Muse",
     "line": "The stack: Go, one virtual machine, SQLite. A single Go binary, one SQLite file, one server. No managed database, no cluster, no bill. Boring on purpose. When one person ships an app, boring means you finish.",
     "screen": "Three plates appear one by one: 'Go', 'SQLite', 'one VM'; a 'no bill' banner fades in"},
    {"id": "B03", "scene": "M05_B03Sql", "dur_s": 18, "act": "1",
     "voice": "Muse",
     "line": "And raw SQL — deliberately. No ORM, no query builder, no magic layer. Just SQL, written by hand. He could read every query and debug every query. The agent writes them; you review them. That only works if the queries are plain.",
     "screen": "A 'raw SQL' card; plain line glyphs appear one by one beside it"},
    {"id": "B04", "scene": "M06_B04Goal", "dur_s": 20, "act": "2",
     "voice": "Muse",
     "line": "Act two: the goal feature. You give the harness a goal — build the backend — and it decomposes that goal into steps, then drives the build itself, step by step. Not one giant prompt. A goal, decomposed, executed.",
     "screen": "A 'goal' dot splits into step dots one by one; arrows chain them together"},
    {"id": "B05", "scene": "M07_B05Decompose", "dur_s": 20, "act": "2",
     "voice": "Muse",
     "line": "Watch the decomposition. The goal — a backend for a community app — becomes endpoints, tables, auth, posts. Each step small enough to get right, each checked before the next. The agent is not being clever here. It is being methodical.",
     "screen": "A tree grows: goal → four branch cards 'endpoints', 'tables', 'auth', 'posts', each with a check"},
    {"id": "B06", "scene": "M08_B06Build", "dur_s": 22, "act": "2",
     "voice": "Muse",
     "line": "Then the build runs. The agent writes the Go handlers, the SQL migrations, the auth. You watch it work, and you read what it writes. Some of it is great; some of it you fix. The agent is fast, and you are the judgment. Together, the backend takes shape.",
     "screen": "Code-line glyphs write one by one into a plate; a 'you are the judgment' lens card fades in"},
    {"id": "B07", "scene": "M09_B07Mvp", "dur_s": 18, "act": "2",
     "voice": "Muse",
     "line": "And then it stands. The MVP. You hit the endpoints: register works, posting works, the database fills. The plan becomes a thing — a backend that answers, built from a doc and a goal.",
     "screen": "An 'MVP' card rises and gets a green check; three dots 'register', 'post', 'database' light up"},
    {"id": "B08", "scene": "M10_B08Compose", "dur_s": 20, "act": "3",
     "voice": "Muse",
     "line": "Act three: ship it. Docker Compose. One file that stands up everything: the Go backend, the React frontend, and MinIO standing in for S3. Three services, one command. The app stops being a project on your laptop and starts being a thing that runs.",
     "screen": "A 'compose' card opens; three service plates rise one by one: 'backend', 'frontend', 'MinIO'"},
    {"id": "B09", "scene": "M11_B09React", "dur_s": 20, "act": "3",
     "voice": "Muse",
     "line": "Then the React frontend, wired to real endpoints. Not mock data, not placeholders — the actual API. The frontend calls the backend, the backend answers, the page fills. When the frontend and the backend agree, you have an app.",
     "screen": "Two plates 'React' and 'endpoints' with a growing arrow between them; page-fill glyphs pulse"},
    {"id": "B10", "scene": "M12_B10Rough", "dur_s": 20, "act": "3",
     "voice": "Muse",
     "line": "The demo: register, post. He registers a user — it works. He posts — it works. And the honest list of what is still rough: styling needs love, edge cases are unwritten. It is an MVP, not a product. He shows the rough parts — that is how you know the rest is real.",
     "screen": "'register' and 'post' cards get checks one by one; a greyed 'rough edges' card fades in below"},
    {"id": "BVDT", "scene": "M13_BvdtHtfOut", "dur_s": 20, "act": "recap",
     "voice": "Muse",
     "line": "Recap. Act one: the plan — a backend doc, a boring stack, raw SQL you can read. Act two: the build — the goal feature decomposes and drives, and the MVP stands. Act three: the ship — Docker Compose, React on real endpoints, register and post, rough edges shown.",
     "screen": "Recap card: 3 lines appear one by one"},
    {"id": "BHTF", "scene": "M13_BvdtHtfOut", "dur_s": 16, "act": "do_today",
     "voice": "Muse",
     "line": "Your turn. One job: write a backend doc for an app you want — what it stores, what it answers, what the stack is. Then ask the agent for the stack plan. The doc is the contract. Write it well.",
     "screen": "Your-turn card: 'one backend doc. then the stack plan.'"},
    {"id": "BOUT", "scene": "M13_BvdtHtfOut", "dur_s": 12, "act": "outro",
     "voice": "Muse",
     "line": "Muse, in for Bear. Thanks for watching. Next film: Muse the Agent.",
     "screen": "Outro card '@NikBearBrown' + 'Next film: Muse the Agent'"},
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
