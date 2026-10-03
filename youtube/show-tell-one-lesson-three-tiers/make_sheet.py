#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-one-lesson-three-tiers.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #30 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B15 drawn -> BHTF composer -> BOUT.

Source: anthropics/k12-teacher-skills — plugin/skills/k12-lesson-differentiation/SKILL.md and the repo README.md, read in
full 2026-09-27, plus the files the skill makes mandatory (references/output.md, references/math.md; ela/science/
social_studies/learning-commons-kg read for the cross-subject rules) and references/example_differentiation.json (the
film's example lesson). The LOCAL copy (anthropics/k12-teacher-skills/, commit 47ebd6a) is OLDER than upstream
(github.com/anthropics/k12-teacher-skills main @ 281eb8d, 2026-08-28): the live SKILL.md is 267 lines (local 502), moves
the output rules into references/output.md, renames the sibling skill k12-lesson-plan-creation, and the live README lists
four skills. The LIVE raw files win (sources/live_*). No WebFetch summary used.
Cast: THE LESSON (a white upright page, grey lines, one terracotta dot); THE THREE TRAYS (kraft open boxes: below, at,
above); THE SPINE (a deep-kraft rod through all three trays and their worksheets: the shared core); WORKSHEETS (white
pages standing in the trays, later tagged Group A/B/C); THE PLAN (a larger page with a grey header band); grey SCAFFOLD
chips; a kraft EXTENSION block; the rulebook binders; the Knowledge Graph connector (a dark MCP block); the source box.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "One Lesson, Three Tiers"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's skills for K through twelve teachers include one called lesson differentiation. It starts from a lesson you already teach. You share it, or you name it. It doesn't write a new lesson from scratch. A separate lesson creation skill does that.",
      "B00_Lesson", "A white lesson page drops onto the stage ('your lesson'); a dashed ghost page fades in beside it and an ink cross lands on it ('new lesson').",
      [{"at": 0.1, "event": "the lesson differentiation skill"}, {"at": 0.45, "event": "a lesson you already teach"}, {"at": 0.8, "event": "not a new lesson"}]),
 beat("B01", "It splits that one lesson into three tiers: below, at, and above grade level. A core runs through all three: the same standard, the same context, the same core tasks. Only the supports change.",
      "B01_Tiers", "The page lifts; three kraft trays drop in a row ('below', 'at', 'above'); a deep-kraft rod slides through all three (the shared core); grey support chips appear in the below tray only.",
      [{"at": 0.1, "event": "three tiers"}, {"at": 0.5, "event": "one core through all three"}, {"at": 0.85, "event": "only the supports change"}]),
 beat("B02", "What comes back, in one turn, is four editable Word documents: one plan for you, the teacher, and a student worksheet for each tier.",
      "B02_FourDocs", "A white worksheet rises in each tray, pierced by the rod ('worksheets'); a larger plan page with a grey header band drops in at the left ('plan').",
      [{"at": 0.2, "event": "four Word documents"}, {"at": 0.5, "event": "one plan"}, {"at": 0.85, "event": "a worksheet per tier"}]),
 beat("B03", "Before any of that, a silent routing step. It works out the subject: math, English language arts, science, or social studies. Then it reads that subject's own rulebook. The skill calls loading it mandatory.",
      "B03_Subject", "The trays clear; the lesson page stands at the left; four kraft binders stand on a dark shelf; one slides out and opens ('math'); a thread runs from it to the page ('rulebook').",
      [{"at": 0.1, "event": "a silent routing step"}, {"at": 0.45, "event": "four subjects"}, {"at": 0.85, "event": "the subject's rulebook, mandatory"}]),
 beat("B04", "Next, it grounds the lesson in its standard. The Learning Commons Knowledge Graph connector holds academic standards for all fifty states. When it's connected, the skill must look the standard up before drafting. Without it, the skill still works, and the plan says so in a footer.",
      "B04_Standards", "The binders clear; a dark connector block lands at the right ('Knowledge Graph'); a cable draws to the page and a tag lands on it ('standard'); a grey footer line draws at the page foot ('footer').",
      [{"at": 0.1, "event": "ground it in its standard"}, {"at": 0.5, "event": "look the standard up before drafting"}, {"at": 0.85, "event": "without it, a footer says so"}]),
 beat("B05", "It also checks where you teach. Name your state, and it uses your state's standards. Say nothing, and math and English language arts default to the Common Core, science to the Next Generation Science Standards. For social studies, it asks you first.",
      "B05_State", "The connector clears; a grey tag hangs on the page ('default'); a kraft pin drops onto a second tag that swings in over it ('your state').",
      [{"at": 0.1, "event": "where you teach"}, {"at": 0.35, "event": "your state's standards"}, {"at": 0.75, "event": "or national defaults"}]),
 beat("B06", "Then it scans what you've said about your students: English learners, I E P goals, five oh four plans. Those shape the tiers, especially below. If you've said nothing, every tier gets sentence supports and vocabulary by default, and it tells you so.",
      "B06_Needs", "The three trays return with the rod; a white note card slides in ('learner needs') and drops a grey chip into the below tray; then one chip drops into every tray ('all tiers').",
      [{"at": 0.1, "event": "what you said about your students"}, {"at": 0.5, "event": "shapes the tiers, below most"}, {"at": 0.85, "event": "defaults on every tier"}]),
 beat("B07", "Before it builds, it asks you one question: build the full set now, or see a quick draft first, what changes in each tier, right in chat. The full set is the default. A draft lets you change things before any document is made.",
      "B07_Draft", "Two white pills slide in ('build it', 'quick draft'); a cursor clicks 'quick draft'; a small chat card rises with three grey lines, one per tier.",
      [{"at": 0.1, "event": "one question"}, {"at": 0.5, "event": "build it, or a quick draft"}, {"at": 0.85, "event": "change it before anything is made"}]),
 beat("B08", "The below tier isn't handed easier work. Instead, supports route its students up to the grade level task. In the example the skill ships with, three eighths of a pizza plus two eighths, the below worksheet adds a pizza to shade, then asks the same question.",
      "B08_TeachUp", "The below tray fills the stage with its worksheet and the rod; grey steps rise from the tray floor up to the rod ('teach up'); a pizza cut in eight slices lands beside it and five slices shade ('same task').",
      [{"at": 0.1, "event": "not easier work"}, {"at": 0.4, "event": "routes up to grade level"}, {"at": 0.85, "event": "a pizza to shade, the same question"}]),
 beat("B09", "A scaffold helps the thinking without giving the answer: no keyword tricks, no templates with only the answer left blank. The rules cap them at one or two per problem, and they fade: up to two on the first problem, one on the second, none from the third on.",
      "B09_Fade", "A worksheet fills the stage with three numbered problem rows; two grey chips land beside problem 1, one beside problem 2, none beside problem 3 ('fade').",
      [{"at": 0.1, "event": "helps, never answers"}, {"at": 0.5, "event": "one or two per problem"}, {"at": 0.85, "event": "two, one, none"}]),
 beat("B10", "The above tier gets an extension, and it has to ask for new thinking, not more of the same. In the example: write your own fraction story whose answer is seven eighths.",
      "B10_Extension", "The above tray fills the stage; a stack of identical grey blocks slides in and is crossed out ('more of the same'); one kraft block lands on top of the rod and rises ('new thinking').",
      [{"at": 0.2, "event": "an extension"}, {"at": 0.5, "event": "new thinking, not more of the same"}, {"at": 0.85, "event": "write your own story"}]),
 beat("B11", "On the student pages, nobody reads below or above. The worksheets are just Group A, B, and C, and the supports look like part of the task, with no label saying who needs help.",
      "B11_Groups", "Back to the three trays with their worksheets; the tray labels fade; ink tags land on the sheets ('Group A', 'Group B', 'Group C').",
      [{"at": 0.1, "event": "nobody reads below or above"}, {"at": 0.5, "event": "Group A, B and C"}, {"at": 0.85, "event": "supports look like the task"}]),
 beat("B12", "Everything the tiers share is written once: the standard, the tasks, the exit ticket, the vocabulary. All four documents pull from that one source, so the plan and the worksheets can't drift apart.",
      "B12_Shared", "A kraft source box with terracotta tape drops in at the top ('written once'); four threads draw from it down to the plan and the three worksheets ('one source').",
      [{"at": 0.1, "event": "written once"}, {"at": 0.5, "event": "four documents pull from it"}, {"at": 0.85, "event": "can't drift apart"}]),
 beat("B13", "So an edit to a shared task updates all four documents at once. A change aimed at one tier, like more support for below, goes only into that tier's worksheet.",
      "B13_Edit", "A new grey line draws on the source box's page; a terracotta dot runs down all four threads and each document gains the same new line ('all four'); then one grey chip drops onto the Group A sheet only ('one tier').",
      [{"at": 0.1, "event": "edit a shared task"}, {"at": 0.45, "event": "all four update"}, {"at": 0.85, "event": "a one-tier change stays there"}]),
 beat("B14", "Who goes in which group? The plan says what each group is based on, like a prior exit ticket, or that no data was given. And it says the groups can change after this lesson's check. It's not a standing track.",
      "B14_Grouping", "The three trays with small kraft student figures in each; a white exit-ticket slip lands ('evidence'); one figure hops from the below tray into the at tray ('can change').",
      [{"at": 0.1, "event": "who goes in which group"}, {"at": 0.45, "event": "the evidence behind it"}, {"at": 0.85, "event": "groups can change"}]),
 beat("B15", "The skill ends by asking if you're happy with all four documents, and what your exit tickets showed, because that can change which support fits. It's finished when you say so.",
      "B15_Close", "The plan and the three worksheets stand in a row; a question card rises ('happy?'); the cursor clicks and an ink check lands under each document ('your OK').",
      [{"at": 0.1, "event": "are you happy with all four?"}, {"at": 0.5, "event": "what your exit tickets showed"}, {"at": 0.85, "event": "finished when you say so"}]),
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
    "Salaam. This is Liam, in for Bear. When one class sits at three levels, it's tempting to write three different lessons. Anthropic's lesson differentiation skill doesn't do that. So the real question is how to split one lesson for three levels.",
    "BrutalistHesitantWriter",
    {"text": "How do I write three lessons\nfor three levels?", "triggerWords": "write three lessons", "replacementWords": "split one lesson",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I write three lessons for three levels?'"}, {"at": 0.6, "event": "backspaces 'write three lessons' -> 'split one lesson' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (write three lessons for three levels) and corrects it to the real one (split one lesson for three levels).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A tier: one version of the lesson, for students below, at, or above grade level. A scaffold: a support printed with a task, which helps the thinking but never gives the answer. An extension: added work that asks for new thinking. And a standard: the learning goal the lesson is written to.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "tier", "meaning": "one version of the lesson: below, at or above grade level"},
               {"term": "scaffold", "meaning": "a support printed with a task; it helps, never answers"},
               {"term": "extension", "meaning": "added work that asks for new thinking"},
               {"term": "standard", "meaning": "the learning goal the lesson is written to"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'tier' lands"}, {"at": 0.3, "event": "'scaffold' lands"}, {"at": 0.55, "event": "'extension' lands"}, {"at": 0.8, "event": "'standard' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Here is a lesson I teach: [paste your lesson]. Differentiate it into three tiers, below, at and above grade "
             "level, that share one core objective and the same core tasks. Show me a quick draft first: for each tier, "
             "what changes and why, and what all three share.")
SPOKEN_PROMPT = ("Here is a lesson I teach, and then paste your lesson. Differentiate it into three tiers, below, at, and above "
                 "grade level, that share one core objective and the same core tasks. Show me a quick draft first: for each "
                 "tier, what changes and why, and what all three share.")
CHECKS = ["Check: same core task on all three tiers?",
          "Check: does any scaffold give away the answer?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude. " + SPOKEN_PROMPT +
    " Then check it yourself. Is the core task the same on all three tiers? And does any scaffold give away the answer?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "K-12 TEACHERS · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the lesson page, the three trays and their shared "
                 "rod, the worksheets and the plan) on a cream stage per beat, minimal labels, with the voice carrying the "
                 "explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, "
                 "empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B06", "B12", "B13", "B14"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): no defects without the waiver; the rest keep it
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
    "slug": SLUG, "title": TITLE, "topic": "K-12 · LESSON DIFFERENTIATION", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Arabic (Salaam)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "K-12 teachers: how Anthropic's k12-lesson-differentiation skill splits one existing lesson into below / at / above grade-level tiers that share one core (same standard, context and core tasks), with scaffolds that fade, an extension that asks for new thinking, student pages named Group A/B/C, shared content written once, and the teacher deciding groups and signing off",
    "source_doc": "github.com/anthropics/k12-teacher-skills main @ 281eb8d (2026-08-28): plugin/skills/k12-lesson-differentiation/SKILL.md, references/output.md, references/math.md (+ ela, science, social_studies, learning-commons-kg), references/example_differentiation.json, README.md; fetched raw 2026-09-27 (sources/live_*); the local copy is older",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude for Teachers", "K-12", "differentiation", "differentiated instruction", "tiered lessons", "scaffolding",
             "lesson planning", "teachers", "Learning Commons", "Knowledge Graph", "Claude skills", "Anthropic", "Nik Bear Brown"]},
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
