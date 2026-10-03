#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-green-yellow-red.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #27 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B15 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-for-legal/ — commercial-legal/skills/nda-review/SKILL.md (the triage), commercial-legal/skills/
cold-start-interview/SKILL.md (how the playbook is written), commercial-legal/README.md and the repo README.md (the
"draft for attorney review — not legal advice" line). All four read in full 2026-09-27 and byte-compared with the raw
upstream files (raw.githubusercontent.com/anthropics/claude-for-legal/main/): identical (sources/live_*).
No real company names; the one sample clause (Your Turn) is generic. No numbers beyond the files' own ("five to ten"
signed agreements). The output is a draft for attorney review, not legal advice, said in the repo's own words (B14).
Palette note: the tiers are LABELLED "green", "yellow", "red" in ink; the chutes and bins stay in the kit's palette
(no green or red tints, no terracotta text).
Cast: the BELT of inbound NDA pages (white, grey lines); the SORTER (a grey machine with a terracotta lamp and scan
line) with THE PLAYBOOK binder (kraft, on a dark plinth) on top; three CHUTES dropping into three kraft BINS
(green / yellow / red); in the lower-left work area: the TEAM (kraft figures), Claude's question cards, the SIGNED
AGREEMENTS (pages with ink signatures), the practice-profile pages and two side tabs, grey FLAGS, a padlock and an
attorney STAMP, the signature card, a gate arm, and the output page with its header band.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Green, Yellow, Red"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's Claude for Legal repo has a commercial legal plugin, and inside it, an NDA review skill. Its premise is simple. Most inbound NDAs are fine. A few have landmines. The skill sorts them, so legal only reads the ones that matter.",
      "B00_Belt", "A pale belt draws across the upper left; white NDA pages ride in along it one by one ('inbound NDAs'); on 'landmines' one page gets a terracotta dot.",
      [{"at": 0.1, "event": "the NDA review skill"}, {"at": 0.5, "event": "most NDAs are fine"}, {"at": 0.75, "event": "a few have landmines"}]),
 beat("B01", "Every NDA leaves down one of three chutes. Green should need nothing more than a signature. Yellow needs a lawyer's eyes on one or two specific things. Red stops, before anyone wastes time. It's built for sales and business development to use themselves, before they ping legal.",
      "B01_Chutes", "A grey sorter rises at the belt's end ('NDA review'); three chutes drop from it into three kraft bins, labelled in ink 'green', 'yellow', 'red'; one page falls into each bin as its tier is named.",
      [{"at": 0.1, "event": "three chutes"}, {"at": 0.3, "event": "green: a signature"}, {"at": 0.5, "event": "yellow: a lawyer's eyes"}, {"at": 0.7, "event": "red: stop"}]),
 beat("B02", "Sorted against what? The skill ships with no default positions on NDA terms. It says the law, the market, and each team's risk tolerance all vary too much for hardcoded defaults to be safe. The positions live in your team's playbook, and the skill reads it before triaging anything.",
      "B02_NoDefaults", "A kraft binder on a dark plinth lands on top of the sorter ('playbook'); it opens beside the belt: its pages are blank, dashed outlines ('no defaults'); a grey thread draws from the binder into the sorter.",
      [{"at": 0.1, "event": "sorted against what?"}, {"at": 0.3, "event": "no default positions"}, {"at": 0.8, "event": "the team's playbook, read first"}]),
 beat("B03", "That playbook is written by the cold-start interview. The first time you use the plugin, it interviews your team, like a sharp new paralegal asking the right questions: your positions, your escalation rules, and the one thing that would make you refuse to sign.",
      "B03_Interview", "In the lower-left work area three kraft team figures stand; question cards (white, grey lines) pop from the sorter toward them one at a time ('cold-start interview'); answer cards come back and land as pages in the binder.",
      [{"at": 0.1, "event": "the cold-start interview"}, {"at": 0.45, "event": "it interviews the team"}, {"at": 0.8, "event": "positions, escalation, the one thing"}]),
 beat("B04", "Then it asks for recent signed agreements, five to ten, and reads them. What a team says it accepts and what it actually signs can differ. Where they differ, the skill's own words are: the delta is the real playbook.",
      "B04_Delta", "A stack of signed agreements (pages with ink signatures) slides in ('signed'); a stated-position bar and a signed-position bar stand side by side; the gap between them is marked in ink ('delta'); a page carrying the gap flies into the binder.",
      [{"at": 0.1, "event": "five to ten signed agreements"}, {"at": 0.5, "event": "stated vs signed"}, {"at": 0.85, "event": "the delta is the real playbook"}]),
 beat("B05", "It writes what it learns into a plain-English practice profile, a Claude dot M D file that every skill in the plugin reads before it does anything. You edit the document, not a config file.",
      "B05_Profile", "The team clears; a white profile page opens large in the work area ('CLAUDE.md') and its grey lines fill in one by one; a grey thread runs from the page up into the binder.",
      [{"at": 0.1, "event": "a plain-English practice profile"}, {"at": 0.5, "event": "every skill reads it first"}, {"at": 0.85, "event": "edit the document"}]),
 beat("B06", "The profile keeps two playbooks: sales-side, for when you're the vendor, and purchasing-side, for when you're the customer. The NDA review reads the side that matches, and stops if that side isn't set up.",
      "B06_Sides", "Two kraft tabs slide out of the binder ('sales', 'purchasing'); one tab lifts and a grey thread runs from it into the sorter; the other stays down.",
      [{"at": 0.1, "event": "two playbooks"}, {"at": 0.5, "event": "sales side, purchasing side"}, {"at": 0.85, "event": "reads the matching side"}]),
 beat("B07", "Now an NDA arrives. First, a scope check: is the document doing more than its name suggests? A non-solicit, exclusivity, an IP assignment, a license grant. If it carries obligations beyond confidentiality, it goes to yellow automatically, whatever the rest says, and is routed for attorney review.",
      "B07_Scope", "A page rides to the sorter; it is lifted into the work area and enlarged; a terracotta scan line sweeps it and reveals a dark extra clause band ('more than an NDA'); the page drops straight down the yellow chute.",
      [{"at": 0.1, "event": "an NDA arrives"}, {"at": 0.4, "event": "more than an NDA?"}, {"at": 0.85, "event": "auto-yellow"}]),
 beat("B08", "Then the checks. The playbook typically covers things like mutuality, the term, the survival period, the carve-outs and governing law. Each one is checked against your team's position, for the side you're on.",
      "B08_Checks", "A fresh page stands enlarged in the work area beside a column of five check rows ('checks'); as each is named, its row lights and an ink check lands, matched by a grey tick on the binder.",
      [{"at": 0.1, "event": "the checks"}, {"at": 0.5, "event": "mutuality, term, survival, carve-outs, governing law"}, {"at": 0.9, "event": "each against the team's position"}]),
 beat("B09", "If the NDA satisfies every position, and nothing triggers a red flag, it's green: route to signature. A clean NDA gets no long report. The summary says only: No red flags identified. Route for signature per standard process.",
      "B09_Green", "All five rows checked; the page drops down the green chute; a white signature card rises beside the green bin and an ink signature draws on its line ('signature'); a one-line summary slip lands.",
      [{"at": 0.1, "event": "every position satisfied"}, {"at": 0.35, "event": "green: route to signature"}, {"at": 0.8, "event": "one line for a clean NDA"}]),
 beat("B10", "If a term deviates from the playbook but isn't a deal-breaker, or the playbook doesn't address it, it's yellow. Each flagged item is listed on its own, with the position it hits and a likely resolution, for a named approver. The skill doesn't make the call on yellow items. It surfaces them for a human.",
      "B10_Yellow", "A page in the work area; two of its rows get grey flags; it drops down the yellow chute; a kraft approver figure stands by the yellow bin ('approver') and the two flags line up in front of it, one by one.",
      [{"at": 0.1, "event": "a deviation, or a gap"}, {"at": 0.45, "event": "each item on its own"}, {"at": 0.85, "event": "a human makes the call"}]),
 beat("B11", "And when the playbook is silent on a term, say, a residuals clause, the skill asks you for your default position: when it should be green, when yellow, when red. Then it records your answer in the playbook, so the next review is consistent.",
      "B11_Silent", "A page with one blank, dashed row ('residuals'); a question card pops from the sorter to a team figure; three short answer bars come back; the answer page flies into the binder, which grows by one page.",
      [{"at": 0.1, "event": "the playbook is silent"}, {"at": 0.5, "event": "it asks for your position"}, {"at": 0.85, "event": "recorded for next time"}]),
 beat("B12", "Red means the NDA hits the playbook's never-accept list, or its structure doesn't fit: say, a one-way NDA where your playbook requires mutual, or a perpetual term where your playbook caps it. Stop, and talk to legal first. No contract record is created, and nobody tells the other side you'll sign.",
      "B12_Red", "A page with a one-way arrow ('one-way') drops down the red chute; a grey gate arm swings down across the red bin ('legal first'); a ghost record card beside it stays empty.",
      [{"at": 0.1, "event": "never-accept list"}, {"at": 0.45, "event": "one-way, or perpetual"}, {"at": 0.75, "event": "stop: legal first"}]),
 beat("B13", "One rule guards the green chute. Green is the only path to signature without a lawyer's review, so it can't be issued against default or missing positions. It needs attorney-reviewed positions in the playbook. Without them, yellow is the right call. In the skill's words: issuing green against defaults means a non-lawyer set the positions the next non-lawyer relies on.",
      "B13_Lock", "A kraft padlock closes on the green chute ('locked'); a page heading for green is turned to yellow; an attorney figure presses a stamp onto the binder, leaving a terracotta seal ('attorney-reviewed'); the padlock opens.",
      [{"at": 0.1, "event": "one rule guards green"}, {"at": 0.4, "event": "no green on defaults"}, {"at": 0.6, "event": "attorney-reviewed positions"}, {"at": 0.85, "event": "the skill's own words"}]),
 beat("B14", "Even after green, if the person using it isn't a lawyer, it pauses before signature. Countersigning an NDA binds the company. So it asks: have you reviewed this with an attorney? If not, it writes a one-page brief to bring to one, and it won't go past that gate without an explicit yes.",
      "B14_Gate", "The signature card stands by the green bin, its line blank; a grey gate arm drops in front of it ('attorney?'); a one-page brief slides out toward a kraft attorney figure; an ink check ('yes') lands and the arm lifts.",
      [{"at": 0.1, "event": "a non-lawyer pauses at signature"}, {"at": 0.45, "event": "reviewed with an attorney?"}, {"at": 0.75, "event": "a one-page brief"}, {"at": 0.9, "event": "an explicit yes"}]),
 beat("B15", "Every output carries the same limit. In the repo's own words, every output from these plugins is a draft for attorney review, not legal advice. A non-lawyer's triage opens with the header: research notes, not legal advice. The skill sorts. A lawyer decides.",
      "B15_Draft", "An output page opens large in the work area with a grey header band ('draft for attorney review'); a second label lands by the band ('not legal advice'); the whole belt, sorter, chutes and bins settle, and an attorney figure stands at the end.",
      [{"at": 0.1, "event": "every output"}, {"at": 0.4, "event": "a draft for attorney review"}, {"at": 0.7, "event": "research notes, not legal advice"}, {"at": 0.9, "event": "the skill sorts, a lawyer decides"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Ciao. This is Liam, in for Bear. You might hope Claude can tell you whether to sign an NDA. But Anthropic's NDA review skill has a narrower job. It doesn't negotiate. It sorts. So the real question is: can Claude tell you which NDAs need a lawyer?",
    "BrutalistHesitantWriter",
    {"text": "Can Claude tell me\nwhether to sign this NDA?", "triggerWords": "whether to sign this NDA", "replacementWords": "which NDAs need a lawyer",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can Claude tell me whether to sign this NDA?'"}, {"at": 0.6, "event": "backspaces 'whether to sign this NDA' -> 'which NDAs need a lawyer' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (can Claude tell me whether to sign this NDA) and corrects it to the real one (which NDAs need a lawyer).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "An NDA: a non-disclosure agreement, a contract to keep shared information confidential. A playbook: your team's written positions on each contract term. The cold-start interview: the plugin's first-run setup, which writes that playbook. And triage: sorting by urgency, here into green, yellow and red.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "NDA", "meaning": "a contract to keep shared information confidential"},
               {"term": "playbook", "meaning": "your team's written positions on each term"},
               {"term": "cold-start", "meaning": "the first-run interview that writes the playbook"},
               {"term": "triage", "meaning": "sorting by urgency: green, yellow, red"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'NDA' lands"}, {"at": 0.3, "event": "'playbook' lands"}, {"at": 0.55, "event": "'cold-start' lands"}, {"at": 0.8, "event": "'triage' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

CLAUSE = "The receiving party may use information retained in the unaided memory of its employees."
YT_PROMPT = ("Write three playbook positions for a residuals clause in an NDA: what makes it GREEN, what makes it YELLOW, "
             "and what makes it RED. Then triage this sample clause against them: \"" + CLAUSE + "\" Say GREEN, YELLOW or RED, "
             "name the position it hits, and flag what an attorney should decide. Mark it all as a draft for attorney review.")
SPOKEN_PROMPT = ("Write three playbook positions for a residuals clause in an NDA: what makes it green, what makes it yellow, "
                 "and what makes it red. Then triage this sample clause against them: " + CLAUSE + " Say green, yellow or red, "
                 "name the position it hits, and flag what an attorney should decide. Mark it all as a draft for attorney review.")
CHECKS = ["Check: does each flag name its position?",
          "Check: have an attorney review the positions."]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude. " + SPOKEN_PROMPT +
    " Then check: does every flag name the position it hits, or say the playbook is silent? And before anyone relies on a green, have an attorney review your three positions.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the belt of NDA pages, the sorter with its playbook "
                 "binder, three chutes into three bins, and one object in the work area) on a cream stage per beat, minimal "
                 "labels, with the voice carrying the explanation. The negative space is the style, so only underfill and "
                 "clustered are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {f"B{n:02d}" for n in range(2, 16)}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): B02-B15 fill 0.62-0.80 throughout; B00 (0.18) and B01 (belt only before the sorter rises) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "LEGAL AI · NDA TRIAGE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "In-house legal teams, contracts managers, sales and BD staff, law students and developers who want to see how Anthropic's open NDA-review skill (claude-for-legal, commercial-legal plugin) triages NDAs into green, yellow and red against a playbook the cold-start interview writes, and why green needs attorney-reviewed positions; the output is a draft for attorney review, not legal advice",
    "source_doc": "anthropics/claude-for-legal/commercial-legal/skills/nda-review/SKILL.md, commercial-legal/skills/cold-start-interview/SKILL.md, commercial-legal/README.md and README.md, read in full 2026-09-27 and byte-compared with the raw upstream files (sources/live_*)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["NDA review", "NDA triage", "legal AI", "Claude for Legal", "contract review", "playbook", "cold-start interview",
             "commercial contracts", "in-house legal", "attorney review", "not legal advice", "Claude", "Anthropic",
             "Nik Bear Brown"]},
    "beats": B}

# keep measured audio fields across re-runs (audio-first: never lose the clock)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in B:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in B)), "s")
