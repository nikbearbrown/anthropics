#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-find-prove-fix.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #12 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B08 drawn -> BHTF composer -> BOUT.

Source: anthropics/defending-code-reference-harness/docs/blog-post.md ("Using LLMs to secure source code",
the six numbered steps), docs/pipeline.md (recon -> find -> grade -> judge -> report -> patch), README.md
(the seven stages, "a reference, not a product", "not maintained"), docs/patching.md (the verification
ladder and its limits), docs/security.md, docs/triage.md, harness/prompts/find_prompt.py (3/3), all read in full.
Cast (NOT the security-review film's pull-request belt): the codebase as a kraft BUILDING with dark windows;
a THREAT MAP (a flat sheet with the building's footprint, a trusted zone, and terracotta door dots);
a GLASS SANDBOX (an ink wireframe box) with a cut cable and one line to a dark 'model API' block;
INSPECTORS (small dark pawns); a CRASH FILE card; a roof ALARM light and a wall CRACK;
a second glass box for the GRADER; a kraft TRIAGE TABLE; a PATCH plate and a four-rung LADDER.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Find, Prove, Fix"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's your code, drawn as a building. Anthropic's guide to securing it has six steps. Two are setup, done once. Four run as a loop: find, prove, triage, fix.",
      "B00_Building", "A kraft building with dark windows rises on the stage ('your code'); two grey slabs slide in under it ('setup'); an ink loop draws around its base with four dots, and a terracotta dot rides the loop ('loop').",
      [{"at": 0.1, "event": "your code: a building"}, {"at": 0.5, "event": "two setup slabs"}, {"at": 0.8, "event": "a loop of four"}]),
 beat("B01", "Step one, the threat model. Decide what counts as a vulnerability: what you trust, and where outside input gets in. Anthropic says a misread trust boundary is the top cause of false positives.",
      "B01_ThreatMap", "A flat map sheet slides in beside the building ('threat model'); the building's footprint draws on it; a grey zone fills ('trusted'); terracotta dots land on the map's doors and on the building's door; a dashed ink boundary draws between them.",
      [{"at": 0.1, "event": "the threat map"}, {"at": 0.45, "event": "what you trust"}, {"at": 0.6, "event": "where input gets in"}, {"at": 0.85, "event": "the trust boundary"}]),
 beat("B02", "Step two, the sandbox: a sealed glass box. Network only during setup. Then snapshot it and cut the cable, leaving one line out, to the model's API. No credentials inside.",
      "B02_Sandbox", "An ink wireframe glass box drops over the building ('sandbox'); a cable runs out to a web block; a snapshot flash; the cable is cut (a gap opens, its ends drop); one thin ink line stays, to a dark block ('model API'); a key card outside the box gets an ink cross.",
      [{"at": 0.1, "event": "the glass box"}, {"at": 0.35, "event": "network during setup"}, {"at": 0.6, "event": "cut the cable"}, {"at": 0.8, "event": "one line to the model API"}, {"at": 0.92, "event": "no credentials"}]),
 beat("B03", "Step three, discovery. One agent splits the code into areas. Inspectors search them in parallel, with the threat model in hand. Anthropic found short prompts with rich context work best.",
      "B03_Inspectors", "Dashed ink lines split the building's roof into three areas ('areas'); three dark inspector pawns drop onto the roof, one per area ('inspectors'); a small copy of the map flies from the sheet to each pawn.",
      [{"at": 0.1, "event": "split into areas"}, {"at": 0.4, "event": "inspectors in parallel"}, {"at": 0.65, "event": "the threat model in hand"}]),
 beat("B04", "Step four, prove it. The harness, a reference and not a product, hunts memory bugs in C and C plus plus. Each finder must bring proof: an input file that crashes the program three times out of three, with Address Sanitizer raising the alarm.",
      "B04_Crash", "An inspector's crash-file card slides down into the building's door slot; the roof alarm flashes terracotta three times while three ink ticks land ('3/3'); a crack draws across the wall ('crash file').",
      [{"at": 0.15, "event": "a reference, for C and C++ memory bugs"}, {"at": 0.45, "event": "an input file"}, {"at": 0.75, "event": "crashes 3 of 3"}, {"at": 0.9, "event": "the alarm"}]),
 beat("B05", "Then a second agent retries it, in a fresh box. Only the crash file crosses over, never the finder's reasoning. Anthropic's partner teams found a verifier that must build a working proof cut false positives to near zero. But a failed proof doesn't prove there's no bug.",
      "B05_Grader", "A second, smaller glass box rises on the right ('grader'); the crash file arcs across into it while the inspector's page stack stays behind; the grader's alarm flashes and an ink check lands ('per Anthropic'); then a second file crosses, no alarm, and a grey question mark sits beside it.",
      [{"at": 0.1, "event": "a fresh box"}, {"at": 0.3, "event": "only the file crosses"}, {"at": 0.62, "event": "near zero false positives, per Anthropic"}, {"at": 0.88, "event": "no proof is not no bug"}]),
 beat("B06", "Step five, triage. Many crashes share one root cause, so a judge merges the duplicates. Then each bug is ranked: can an attacker reach it, and how far would the damage spread?",
      "B06_Triage", "A kraft table; five crash cards land on it ('triage'); two pairs slide together and merge ('duplicates'); the three left line up in a ranked column with ink numerals 1, 2, 3 ('ranked').",
      [{"at": 0.1, "event": "crash cards on the table"}, {"at": 0.4, "event": "duplicates merge"}, {"at": 0.7, "event": "ranked"}]),
 beat("B07", "Step six, the fix. The patch climbs a ladder: it builds, the old crash stops, the old tests pass, and a fresh agent attacks it. The lessons feed the next round. The ladder shows the crash is gone, not that the patch is safe. A human owns every fix.",
      "B07_Patch", "A kraft patch plate covers the wall crack ('patch'); a four-rung ladder stands beside the building and an ink check lands on each rung; an ink arrow arcs from the building back to the map, which gains a new dot ('next round'); a person figure steps up beside the patch ('human').",
      [{"at": 0.1, "event": "the patch"}, {"at": 0.25, "event": "builds, crash stops, tests pass, re-attack"}, {"at": 0.6, "event": "back into the threat model"}, {"at": 0.9, "event": "a human owns every fix"}]),
 beat("B08", "Why now? Anthropic says that by May twenty-second, twenty twenty-six, it had disclosed one thousand, five hundred and ninety-six vulnerabilities. To its knowledge, ninety-seven were patched. Finding has outrun fixing.",
      "B08_Count", "A tall stack of grey crash cards grows as a counter climbs to 1,596 ('disclosed', 'per Anthropic'); beside it a one-slab stack, '97', with an ink check ('patched'); the tall stack pulses on 'finding has outrun fixing'.",
      [{"at": 0.2, "event": "1,596 disclosed, per Anthropic"}, {"at": 0.7, "event": "97 patched"}, {"at": 0.9, "event": "finding has outrun fixing"}]),
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
    "Hola. This is Liam, in for Bear. Point Claude at your code, and it finds bugs. Anthropic says finding is no longer the bottleneck. So the real question is how you prove what it finds, and fix it.",
    "BrutalistHesitantWriter",
    {"text": "Can Claude\nfind the bugs in my code?", "triggerWords": "find the bugs in my code", "replacementWords": "prove and fix what it finds",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can Claude find the bugs in my code?'"}, {"at": 0.6, "event": "backspaces 'find the bugs in my code' -> 'prove and fix what it finds' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (can Claude find the bugs in my code) and corrects it to the real one (can Claude prove and fix what it finds).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A threat model: what counts as a vulnerability in your system. A proof of concept: an input that really triggers the bug. And Address Sanitizer: a memory-error detector for C and C plus plus.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "threat model", "meaning": "what counts as a vulnerability in your system"},
               {"term": "proof of concept", "meaning": "an input that really triggers the bug"},
               {"term": "ASAN", "meaning": "AddressSanitizer: catches memory errors in C and C++"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'threat model' lands"}, {"at": 0.4, "event": "'proof of concept' lands"}, {"at": 0.7, "event": "'ASAN' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("In this repo, write a short THREAT_MODEL.md: what the code trusts, and where outside input gets in. "
             "Find one bug that input could reach, or say there's none. Prove it with a failing test, "
             "then make the smallest fix that turns it green.")
SPOKEN_PROMPT = YT_PROMPT.replace("a short THREAT_MODEL.md", "a short threat model file")
CHECKS = ["Check: the new test fails before the fix?",
          "Check: all the old tests still pass after?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code, in a repo you own: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Does the new test fail before the fix? And do the old tests still pass after it?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn building-in-a-glass-box scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B02", "B03", "B04", "B05", "B06"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.58-0.83 fill, no defect: no waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · SECURING SOURCE CODE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Spanish (Hola)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers and security engineers who have pointed a model at code, got a pile of findings, and need to know which are real and how to fix them",
    "source_doc": "anthropics/defending-code-reference-harness: docs/blog-post.md, docs/pipeline.md, README.md, docs/patching.md, docs/security.md, docs/triage.md, harness/prompts/find_prompt.py (read in full 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "security", "vulnerability", "threat model", "sandbox", "gVisor", "proof of concept",
             "AddressSanitizer", "ASAN", "triage", "patching", "defending-code-reference-harness", "Anthropic", "Nik Bear Brown"]},
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
