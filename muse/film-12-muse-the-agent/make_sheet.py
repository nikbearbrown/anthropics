"""make_sheet.py — Muse the Agent (Film 12).
Embeds the beat dict, asserts counts, prints totals, writes beat_sheet.json.
"""
import json

BEATS = [
    {
        "id": "BIDEA",
        "scene": "M01_Bidea",
        "dur_s": 20,
        "act": "hook",
        "voice": "Muse",
        "line": "This is the other Muse. Not the models you rent, not the harness you drive \u2014 the agent that runs errands. You give it a goal, it builds a plan, and it runs your errands. Here\u2019s what it is, who pays, and how you survive it.",
        "screen": "Title card: \u201cthe other Muse\u201d / sub \u201cthe agent that runs errands\u201d. Then three small cards appear one by one with arrows: goal \u2192 plan \u2192 errands.",
    },
    {
        "id": "BDEFS",
        "scene": "M02_Bdefs",
        "dur_s": 22,
        "act": "hook",
        "voice": "Muse",
        "line": "Four terms. Agent: software that acts toward a goal, not just answers. Intent layer: the point where you say what you want before money moves \u2014 the want, then money. Blast radius: how far one failure can spread. Allow-list: deny unless allowed \u2014 everything else is out.",
        "screen": "Four term cards appear one by one: Agent / Intent layer / Blast radius / Allow-list, one-line gloss each.",
    },
    {
        "id": "B01",
        "scene": "M03_B01Loop",
        "dur_s": 24,
        "act": "1",
        "voice": "Muse",
        "line": "Here\u2019s the machine. You hand Muse a goal. It builds a plan. Then it acts \u2014 inside its own cloud computer, with its own browser, terminal, and files \u2014 and it keeps working after you close the app. Before a consequential action, it checks in: approval. Goal in, plan out, action taken. That loop is the whole product.",
        "screen": "Loop diagram: goal \u2192 plan \u2192 act cards with cycling arrows; a diamond gate \u201capproval\u201d on the act edge; a terminal glyph labeled \u201cits own cloud computer\u201d.",
    },
    {
        "id": "B02",
        "scene": "M04_B02Errands",
        "dur_s": 24,
        "act": "1",
        "voice": "Muse",
        "line": "What does it actually do? Consumer errands. Book travel. Shop. Fill in forms. Find tickets. Manage subscriptions. It plugs in through connectors \u2014 Gmail, Notion, Slack, GitHub \u2014 commerce first, productivity second. And if a service has an API, it can build its own connector.",
        "screen": "Errand rows appear one by one: book travel / shop / forms / tickets / subscriptions. Then a row of connector dots labeled \u201cconnectors\u201d.",
    },
    {
        "id": "B03",
        "scene": "M05_B03Tiers",
        "dur_s": 20,
        "act": "1",
        "voice": "Muse",
        "line": "Three tiers. Free: one hundred million Muse tokens a week. Power: twenty dollars a month, five hundred million. Maximum: a hundred a month, three billion. Same features on every tier \u2014 you pay only for volume. And a card is required, even for the free one.",
        "screen": "Three tier cards: Free \u201c100M / week\u201d / Power \u201c$20 / mo \u00b7 500M / week\u201d / Maximum \u201c$100 / mo \u00b7 3B / week\u201d. Footnote: \u201ccard required, even free\u201d.",
    },
    {
        "id": "B04",
        "scene": "M06_B04Endure",
        "dur_s": 22,
        "act": "1",
        "voice": "Muse",
        "line": "One honest thing from the research notes: its real strength is endurance, not intelligence. Waiting. Refreshing. Grinding through tedious steps. In the instructor\u2019s experience these models are noticeably less capable than the frontier \u2014 but they don\u2019t get bored, and they don\u2019t quit. It saves time, not thought.",
        "screen": "Two bars grow: \u201cendurance\u201d (full, green) vs \u201cintelligence\u201d (partial, grey). Caption: \u201csaves time, not thought\u201d.",
    },
    {
        "id": "B05",
        "scene": "M07_B05Fees",
        "dur_s": 24,
        "act": "2",
        "voice": "Muse",
        "line": "So who pays? The stated model: transaction fees. Muse books your flight or checks out your cart, and the merchant pays Meta a small cut \u2014 like an affiliate commission. You never see a charge. But merchant costs tend to work their way into prices eventually. Subscriptions and API sales are the secondary revenue.",
        "screen": "Flow: you \u2192 Muse \u2192 merchant; a terracotta arrow loops back \u201cmerchant pays Meta a cut\u201d. Caption: \u201cyou never see a charge\u201d.",
    },
    {
        "id": "B06",
        "scene": "M08_B06Intent",
        "dur_s": 26,
        "act": "2",
        "voice": "Muse",
        "line": "The deeper play is the intent layer: the moment you say what you want, before money changes hands. Own that moment \u2014 the want, the choice, the buy \u2014 and you own the transaction. Meta says there are no ads inside Muse. But what Muse browses at merchants can still shape the ads you see elsewhere on Meta\u2019s apps. The profile is worth more than any single fee.",
        "screen": "Three nodes: want \u2192 choose \u2192 buy; a bracket over \u201cwant\u201d labeled \u201cthe intent layer\u201d; a Meta dot at the bracket.",
    },
    {
        "id": "B07",
        "scene": "M09_B07Queues",
        "dur_s": 26,
        "act": "2",
        "voice": "Muse",
        "line": "What do agents do to queues? A line only signals devotion because waiting costs something. Once an agent waits for you for free, waiting signals nothing. Agents quietly turn the queue into a market \u2014 and the surplus goes to subscriptions and reseller fleets, not the artists. Price-based allocation resists agents. Queues don\u2019t.",
        "screen": "A line of waiting figures dissolves; a market stall with price tags appears. Arrow: \u201csurplus \u2192 subscriptions + resellers\u201d.",
    },
    {
        "id": "B08",
        "scene": "M10_B08Loyalty",
        "dur_s": 26,
        "act": "2",
        "voice": "Muse",
        "line": "So devotion signals move: fan history, proof of personhood, in-person rituals, sanctioned agent channels. And watch the drift \u2014 airline loyalty started by rewarding frequent flyers and ended up tracking spending. The visible unfairness of a line becomes the invisible unfairness of a score you can\u2019t see and can\u2019t challenge.",
        "screen": "Drift arrow: \u201cfrequent flyers \u2192 spending\u201d. Two cards: \u201cvisible line\u201d (figures) vs \u201cinvisible score\u201d (card with \u201c?\u201d).",
    },
    {
        "id": "B09",
        "scene": "M11_B09Access",
        "dur_s": 26,
        "act": "3",
        "voice": "Muse",
        "line": "Now the sharp edges. The Mac app asks for Full Disk Access \u2014 the whole disk, not a folder. A behavioral promise, not a technical boundary. And it runs a deny-list, not an allow-list: you name what it can\u2019t touch instead of what it can. That breaks fail-safe defaults \u2014 Saltzer and Schroeder, nineteen seventy-five: deny unless explicitly allowed.",
        "screen": "Contrast pair: big circle \u201cthe whole disk\u201d with a red cross vs small circle \u201callow-list\u201d with a green check. Caption: \u201cSaltzer and Schroeder, 1975\u201d.",
    },
    {
        "id": "B10",
        "scene": "M12_B10Inject",
        "dur_s": 24,
        "act": "3",
        "voice": "Muse",
        "line": "Then prompt injection. An agent reads untrusted content \u2014 pages, messages, PR text \u2014 and that content can steer it. So the failure probability isn\u2019t random, it\u2019s adversarial: steered toward the highest-impact action. Add approval fatigue \u2014 after the twentieth prompt, approval becomes reflex. And the friendly mascot is a deliberate trust shortcut.",
        "screen": "A page glyph with a hidden dashed arrow steering the agent dot toward a big red button. Caption: \u201cadversarial, not random\u201d.",
    },
    {
        "id": "B11",
        "scene": "M13_B11Setup",
        "dur_s": 26,
        "act": "3",
        "voice": "Muse",
        "line": "The fix is compartmentalization. Assume breach, bound the blast radius, enforce limits outside the agent. Cross impact against recoverability \u2014 low impact to high, recoverable to unrecoverable. The cell that matters: high impact, unrecoverable. Email. Money. Credentials. Public voice. That\u2019s the short list, and it gets real walls. Everything else gets backups.",
        "screen": "2\u00d72 matrix: axes \u201crecoverability\u201d (recoverable \u2192 unrecoverable) and \u201cimpact\u201d (low \u2192 high). Top-right cell highlighted: \u201cthe short list \u2014 email \u00b7 money \u00b7 credentials \u00b7 public voice\u201d.",
    },
    {
        "id": "B12",
        "scene": "M14_B12Rules",
        "dur_s": 26,
        "act": "3",
        "voice": "Muse",
        "line": "Five rules for the agent era. One: an agent\u2019s access is the attacker\u2019s access. Two: ask how bad it gets, not how likely. Three: caps belong outside the agent. Four: irreversible actions get a human. Five: protect the short list \u2014 email, money, credentials, public voice \u2014 with real walls.",
        "screen": "Five numbered rule cards appear one by one: 1 an agent\u2019s access is the attacker\u2019s access / 2 ask how bad it gets, not how likely / 3 caps belong outside the agent / 4 irreversible actions get a human / 5 protect the short list with real walls.",
    },
    {
        "id": "BVDT",
        "scene": "M15_BvdtHtfOut",
        "dur_s": 20,
        "act": "recap",
        "voice": "Muse",
        "line": "The agent: goal in, plan out, errands done \u2014 endurance, not intelligence. Who pays: transaction fees now, the intent layer forever. Survive it: allow-lists, caps outside the agent, the five rules.",
        "screen": "Recap card: 3 lines appear one by one: \u201cThe agent: goal in, plan out, errands done \u2014 endurance, not intelligence.\u201d / \u201cWho pays: transaction fees now, the intent layer forever.\u201d / \u201cSurvive it: allow-lists, caps outside the agent, the five rules.\u201d",
    },
    {
        "id": "BHTF",
        "scene": "M15_BvdtHtfOut",
        "dur_s": 16,
        "act": "do_today",
        "voice": "Muse",
        "line": "Audit one agent you use. What can it touch? What can it spend? What can it never do? Write the answers down \u2014 and put a cap where it belongs: outside the agent.",
        "screen": "Your-turn card: \u201caudit one agent \u2014 what can it touch? what can it spend? what can it never do?\u201d",
    },
    {
        "id": "BOUT",
        "scene": "M15_BvdtHtfOut",
        "dur_s": 14,
        "act": "outro",
        "voice": "Muse",
        "line": "Muse, in for Bear. Thanks for watching the series.",
        "screen": "Outro title card: \u201c@NikBearBrown\u201d + \u201cThanks for watching the series\u201d. Series finale \u2014 no next-film teaser.",
    },
]

EXPECTED_BEATS = 17
EXPECTED_BODY = 12

for b in BEATS:
    assert b["scene"].startswith("M"), b["id"]
    assert b["voice"] == "Muse", b["id"]

assert len(BEATS) == EXPECTED_BEATS, len(BEATS)
body = [b for b in BEATS if b["act"] in ("1", "2", "3")]
assert len(body) == EXPECTED_BODY, len(body)
for b in body:
    assert 12 <= b["dur_s"] <= 30, (b["id"], b["dur_s"])

total = sum(b["dur_s"] for b in BEATS)
print(f"beats={len(BEATS)} body={len(body)} total={total}s")

with open("beat_sheet.json", "w") as f:
    json.dump(BEATS, f, indent=2, ensure_ascii=False)
print("wrote beat_sheet.json")
