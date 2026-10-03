#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-legacy-code-in-order.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #24 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: Anthropic's code-modernization plugin, read RAW from GitHub main on 2026-09-27
(anthropics/claude-plugins-official @ fa59bc90, plugin version 1.0.0, last changed 2026-09-25):
README.md, .claude-plugin/plugin.json, all thirteen commands/*.md, agents/test-engineer.md and
agents/business-rules-extractor.md (sources/live_2026-09-27_*). The local copy under
anthropics/claude-plugins-official/plugins/code-modernization/ (pulled 2026-08-27) is an older
version (no front door, no review, no verify; harden last; bare /modernize-* names). The batch
rule is "live docs win", and the viewer's /plugin install gets the live version, so the film
follows the live files: preflight -> assess -> map -> extract-rules -> review -> brief ->
(uplift | transform | reimagine) -> verify -> harden, with the README's six human decision points.
Cast: the legacy CABINET (a tall dark mainframe with two ghost tape reels and a terracotta lamp)
standing in the kraft LEGACY tray, with an ink PADLOCK; the kraft ANALYSIS tray (pages land flat in
it); the kraft MODERNIZED tray (the new kraft BOX lands in it); a HUD of six ghost PIPS ("you
decide") that light terracotta one by one; question card, lenses, circle-pack map, rule cards,
the brief binder and gate, three dark build doors, the comparator, test lamps, verdict stamp, patch.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Legacy Code, in Order"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The plugin is a set of commands you run in Claude Code, in order, and each one stands alone, so you can stop and review after any step. Your old code sits in a legacy folder, and the read me says nothing edits it. The commands write to two other folders: analysis, for what they find, and modernized, for the new code.",
      "B00_Folders", "A tall dark mainframe cabinet drops into a kraft tray ('legacy/'); an ink padlock snaps onto it; a kraft tray slides in at the bottom ('analysis/'), then one at the right ('modernized/').",
      [{"at": 0.1, "event": "the cabinet lands in the legacy tray"}, {"at": 0.45, "event": "a padlock: nothing edits it"}, {"at": 0.75, "event": "the analysis tray"}, {"at": 0.9, "event": "the modernized tray"}]),
 beat("B01", "Step one: pre-flight. It asks you five questions only a person can answer, like whether this is the whole system, and what's off limits, and writes your answers down word for word. Meanwhile it proves a build works on this code, and looks for missing source. Those answers are the first of six points where a person decides. The plugin never decides them for you.",
      "B01_Preflight", "A question card with five lines and five empty boxes pops up beside the cabinet ('preflight'); the cursor ticks each box; a grey probe sweeps the cabinet and its lamp blinks; the card drops into the analysis tray as a page; six ghost pips appear at the top right ('you decide') and the first lights terracotta.",
      [{"at": 0.1, "event": "five questions pop up"}, {"at": 0.35, "event": "you answer them"}, {"at": 0.55, "event": "a build is proved on the code"}, {"at": 0.8, "event": "decision one of six"}]),
 beat("B02", "Step two: assess. Three agents read at once, for structure, tech debt, and security holes, and it recommends a pattern. Step three: map. Calls, data, and entry points become an interactive map, with business flows walked through as the people who use the system.",
      "B02_AssessMap", "Three lenses slide over the cabinet together ('assess'); an assessment page drops into the analysis tray; then a circle-pack map blooms at centre-right (grey domain rings holding kraft module circles of different sizes, 'map'), grey edges draw between modules, and a terracotta dot walks a numbered path across three of them ('flow').",
      [{"at": 0.15, "event": "three agents read at once"}, {"at": 0.4, "event": "the assessment page"}, {"at": 0.6, "event": "the map blooms, edges draw"}, {"at": 0.85, "event": "a business flow is walked"}]),
 beat("B03", "Step four: extract rules. The business rules come out of the code as cards: given, when, then, each citing its file and line, and each re-checked by a second agent. Rules that look wrong go to review, where a person marks each one right, wrong, or not sure. That's decision two.",
      "B03_Rules", "The map folds into a page in the analysis tray; five rule cards rise out of the cabinet into a row ('rule cards'); grey threads draw from each card back to the cabinet; a small check lands on each; one card with a terracotta dot drops to a review spot; the cursor marks it ('review'); the second pip lights.",
      [{"at": 0.15, "event": "rule cards rise from the code"}, {"at": 0.35, "event": "each cites its file and line"}, {"at": 0.5, "event": "each is re-checked"}, {"at": 0.8, "event": "a person reviews the flagged one"}]),
 beat("B04", "Step five: the brief. It reads what discovery found, and stops if a required piece is missing. It writes a phased plan, with a behaviour contract: the critical rules, called P zero, that must be proven equivalent before any phase can ship. Then it stops. Nothing is built until you approve it, and no objection is not approval.",
      "B04_Brief", "Three pages rise from the analysis tray into a kraft binder ('brief'); three phase strips stack on it; the flagged-rule cards clip onto its side ('P0 rules'); a gate bar drops across the way to the right; the cursor presses a check pill ('approve'); the third pip lights; the gate lifts.",
      [{"at": 0.1, "event": "discovery goes into the brief"}, {"at": 0.35, "event": "phases"}, {"at": 0.55, "event": "the P0 rules: the behaviour contract"}, {"at": 0.85, "event": "nothing is built until you approve"}]),
 beat("B05", "Step six: build, by one of three methods the plan recommends. Uplift keeps the same technology, and fixes only what a newer version breaks, like Java eight to seventeen. Transform rewrites one module at a time in a new technology, while the old system keeps running. Reimagine rebuilds on a new architecture. Each one reads the brief, and treats its entry criteria as gates.",
      "B05_Build", "Three dark doors rise ('uplift', 'transform', 'reimagine'); each lamp lights grey as it is named; the brief binder rides to the transform door and its lamp turns terracotta; a new kraft box rolls out into the modernized tray while the cabinet's lamp keeps blinking.",
      [{"at": 0.1, "event": "three doors"}, {"at": 0.3, "event": "uplift"}, {"at": 0.55, "event": "transform: one module, old system still running"}, {"at": 0.75, "event": "reimagine"}, {"at": 0.9, "event": "the brief goes through a door"}]),
 beat("B06", "Step seven: verify, the proof, ideally in a fresh session, because it redoes the work instead of trusting the build's own notes. It reruns the tests from clean. Where the old code can run, old and new get the same inputs, and a script compares every byte. Then it invents at least ten inputs nobody used, and compares again.",
      "B06_Verify", "The new box rises from its tray to face the cabinet ('verify'); input cards drop into both; output slips come out and meet at a grey comparator in the middle ('compare'); a check lands; then a row of ten fresh kraft input tiles slides in ('new inputs') and both run again.",
      [{"at": 0.15, "event": "old and new face each other"}, {"at": 0.45, "event": "same inputs, outputs compared byte for byte"}, {"at": 0.8, "event": "ten inputs nobody used"}]),
 beat("B07", "It also breaks one line on purpose. If no test turns red, the tests don't pin the behaviour. Then each module gets one verdict: proven, partly proven, or not proven. If the old code can't run where you work, the best it can get is partly proven. A person accepts any difference, and signs the proof: decisions four and five.",
      "B07_Verdict", "A row of test lamps sits under the new box; a crack (terracotta dot) is put into one of its lines ('canary') and the lamps flip to ink crosses, then clear when it is mended; a kraft verdict card stamps down with three slots and the first fills ('PROVEN'); the cursor draws a signature line; pips four and five light.",
      [{"at": 0.1, "event": "a deliberate break"}, {"at": 0.25, "event": "the tests must fail"}, {"at": 0.5, "event": "one verdict per module"}, {"at": 0.85, "event": "a person accepts and signs"}]),
 beat("B08", "Last, harden: a security scan of the legacy system. It ranks what it finds, drafts a patch for the critical and high ones, and has the patch reviewed. It still never edits your code. You apply the patch yourself: decision six.",
      "B08_Harden", "A grey scan sweeps the locked cabinet ('harden'); three flags pop up and sort into a ranked stack of grey bars; a patch card is drafted and gets a review check ('patch'); the padlock stays shut; the cursor carries the patch to the cabinet ('you apply'); the sixth pip lights.",
      [{"at": 0.15, "event": "the scan"}, {"at": 0.35, "event": "findings ranked"}, {"at": 0.6, "event": "a reviewed patch"}, {"at": 0.85, "event": "you apply it: decision six"}]),
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
    "Bonjour. This is Liam, in for Bear. Handed an old codebase, it's tempting to ask how to get Claude to rewrite it. But Anthropic's code modernization plugin never starts with a rewrite. So the real question is how to get Claude to modernize legacy code, in order.",
    "BrutalistHesitantWriter",
    {"text": "How do I get Claude\nto rewrite my old code?", "triggerWords": "to rewrite my old code", "replacementWords": "to modernize legacy code in order",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get Claude to rewrite my old code?'"}, {"at": 0.6, "event": "backspaces 'to rewrite my old code' -> 'to modernize legacy code in order' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I get Claude to rewrite my old code) and corrects it to the real one (how do I get Claude to modernize legacy code in order).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Legacy code: old code a business still runs on. A business rule: a calculation, check, or policy the code enforces. The brief: the phased plan you approve. And equivalence: proof that the new code behaves like the old.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "legacy code", "meaning": "old code a business still runs on"},
               {"term": "business rule", "meaning": "a calculation, check or policy the code enforces"},
               {"term": "brief", "meaning": "the phased plan you approve"},
               {"term": "equivalence", "meaning": "proof the new code behaves like the old"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'legacy code' lands"}, {"at": 0.35, "event": "'business rule' lands"}, {"at": 0.6, "event": "'brief' lands"}, {"at": 0.8, "event": "'equivalence' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = "/code-modernization:modernize-preflight billing --source ~/code/billing"
SPOKEN_PROMPT = ("slash code modernization, colon, modernize pre-flight, billing, dash dash source, "
                 "and then the path to one old module of your own")
CHECKS = ["Check: are your five answers in PREFLIGHT.md, word for word?",
          "Check: does readlink legacy/billing point at your code?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Install the code modernization plugin, and run only the first step. In Claude Code, paste this: " + SPOKEN_PROMPT + ". "
    "Answer the five questions yourself. Then check two things. Are your five answers in the pre-flight report, word for word? "
    "And does the legacy billing link point at your code, with nothing copied?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the command types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn cabinet-and-trays scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B02", "B03", "B04", "B05", "B06", "B07", "B08"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.72-0.74 throughout; B00 (0.11-0.51) and B01 (0.54 at 25-60%) keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · CODE MODERNIZATION", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers handed an old codebase who want to see the order Anthropic's code-modernization plugin enforces, and where a person decides",
    "source_doc": "anthropics/claude-plugins-official/plugins/code-modernization/ v1.0.0, read RAW from GitHub main @ fa59bc90 on 2026-09-27: README.md, plugin.json, commands/*.md (13), agents/test-engineer.md, agents/business-rules-extractor.md (sources/live_2026-09-27_*); the older local copy was diffed and differs",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "code modernization", "legacy code", "COBOL", "business rules", "strangler fig",
             "equivalence testing", "characterization tests", "plugins", "human in the loop", "Anthropic", "Nik Bear Brown"]},
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
