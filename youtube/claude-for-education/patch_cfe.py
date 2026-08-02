#!/usr/bin/env python3
"""Fix claude-for-education: Pattern A (OUTRO props) + Pattern B (voice_id + YOURTURN)."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_beat_id(b):
    return b.get("beat_id", b.get("id", ""))

def get_remotion(b):
    shot = b.get("shot", {})
    if "remotion" in shot:
        return shot["remotion"]
    return b.get("remotion", None)

def ensure_outro_props(beats, title, mascotSeed):
    for b in beats:
        bid = get_beat_id(b)
        scene = b.get("scene", "")
        rem = get_remotion(b)
        pat = (rem or {}).get("pattern", "")
        if bid in ("OUTRO", "BOUT", "B07", "O01") or scene == "ClaudeTitleOutro" or pat == "ClaudeTitleOutro":
            shot = b.setdefault("shot", {})
            shot["type"] = "REMOTION"
            shot["source"] = "own"
            remotion = shot.setdefault("remotion", {})
            remotion.setdefault("pattern", "ClaudeTitleOutro")
            props = remotion.setdefault("props", {})
            props["title"] = title
            props["handle"] = "@NikBearBrown"
            props["mascotSeed"] = mascotSeed
            props.pop("subline", None)
            # also strip old top-level remotion props
            if "remotion" in b:
                b["remotion"].get("props", {}).pop("subline", None)
                b["remotion"].get("props", {}).update({"title": title, "handle": "@NikBearBrown", "mascotSeed": mascotSeed})
            b.get("props", {}).pop("subline", None)
            return True
    return False

def strip_all_sublines(beats):
    for b in beats:
        b.get("props", {}).pop("subline", None)
        shot = b.get("shot", {})
        shot.get("remotion", {}).get("props", {}).pop("subline", None)
        b.get("remotion", {}).get("props", {}).pop("subline", None)

def fix_voice(meta):
    meta.pop("voice_id", None)
    if not meta.get("engine"):
        meta["engine"] = "kokoro"
    if not meta.get("voice"):
        meta["voice"] = "am_onyx"
    if not meta.get("voice_kokoro"):
        meta["voice_kokoro"] = "am_onyx"

def patch_yourturn(beats, narration, command, segment):
    for b in beats:
        bid = get_beat_id(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        rem = get_remotion(b)
        pat = (rem or {}).get("pattern", "")
        if bid in ("YOURTURN", "BHTF", "H01") or scene == "ClaudeComposerAsk" or pat == "ClaudeComposerAsk" or act in ("handoff", "your-turn"):
            if "ClaudeTitleOutro" in str(b):
                continue
            if "narration_text" in b:
                b["narration_text"] = narration
            elif "narration" in b:
                b["narration"] = narration
            else:
                b["narration_text"] = narration
            shot = b.setdefault("shot", {})
            if "remotion" in b and "remotion" not in shot:
                shot["remotion"] = b.pop("remotion")
            shot.setdefault("type", "REMOTION")
            remotion = shot.setdefault("remotion", {})
            remotion.setdefault("pattern", "ClaudeComposerAsk")
            props = remotion.setdefault("props", {})
            props["greeting"] = "Your turn."
            props["command"] = command
            props["segment"] = segment
            props.setdefault("topic", "CLAUDE FOR EDUCATION · @NikBearBrown")
            props.setdefault("folderLabel", "@NikBearBrown")
            props.setdefault("modelLabel", "Claude Sonnet")
            props.setdefault("runningText", "paste your lesson, prompt, or rubric here…")
            return True
    return False

# ── Pattern A: OUTRO props only ───────────────────────────────────────────────
PATTERN_A = {
    "advising-privacy-gate": "Advising Privacy Gate: Anonymize Before Prompting",
    "assignment-stress-test": "Stress-Test the Assignment Before Students Do",
    "capstone-unit-builder": "Capstone Unit Builder: Coherence Is the Human's Job",
    "differentiation-audit": "Differentiation Audit: Preserving the Intellectual Target",
    "faculty-literature-lead": "Literature Leads Are Not Citations",
    "instructional-brief-eight-fields": "The Eight-Field Instructional Brief",
    "manuscript-reviewer-response": "Manuscript Reviewer Response: Claude as Adversarial Reader",
    "udl-choice-board": "UDL Choice Board Audit: Same Demand, Different Path",
}

# ── Pattern B: voice_id + YOURTURN ───────────────────────────────────────────
PATTERN_B = {
    "ai-ban-design-failure": {
        "title": "Why Banning AI from Assignments Usually Teaches the Wrong Lesson",
        "narration": "Your turn. Paste this: you're deciding whether to ban AI from your assignments or redesign them. Ask Claude for the framework to decide which assignments are worth redesigning versus which become meaningless with AI — and what a redesigned AI-resistant assignment actually looks like for a specific type.",
        "command": "I teach and I'm deciding whether to ban AI from my assignments or redesign them. Give me the framework for which assignments are worth redesigning versus which become meaningless with AI — and show me what 'redesigned to be AI-resistant without banning AI' actually looks like for a specific assignment type.",
        "segment": "Why Banning AI from Assignments Usually Teaches the Wrong Lesson",
    },
    "artifact-vs-learning": {
        "title": "Why a Polished Lesson Plan Can Fail Every Student in the Room",
        "narration": "Your turn. Paste this: you used Claude to generate a professional-looking lesson plan but you're worried it's optimized for appearance rather than learning. Ask Claude to audit it — flag every place where the artifact satisfies a bureaucratic requirement but does nothing for actual student learning.",
        "command": "I used Claude to generate a lesson plan and it looks professional — learning objectives, activities, assessment. But I'm worried the plan is optimized for how a lesson should look rather than how students actually learn. Audit this lesson plan for me: flag every place where the artifact satisfies a bureaucratic requirement but does nothing for student learning.",
        "segment": "Why a Polished Lesson Plan Can Fail Every Student in the Room",
    },
    "assessment-by-design": {
        "title": "Why AI Makes Assessment Cheat-Proof or Irrelevant — There Is No Middle Ground",
        "narration": "Your turn. Paste this: you want to eliminate the middle ground where AI use is cheating but not really. Ask Claude for the two design patterns that make assessment AI-irrelevant — and the two that make AI use visible and gradeable as a skill.",
        "command": "I want to redesign my assessments so that using AI either doesn't help or is part of the skill being assessed — I want to eliminate the middle ground where using AI is cheating but not really cheating. Give me the two design patterns that make assessment AI-irrelevant, and the two that make AI use visible and gradeable.",
        "segment": "Why AI Makes Assessment Cheat-Proof or Irrelevant — There Is No Middle Ground",
    },
    "cognitive-friction-loop": {
        "title": "Why Students Who Practice With AI Score Lower on the Exam",
        "narration": "Your turn. Paste this: your students use AI to practice problems before exams and their scores are going down. Ask Claude to walk you through the cognitive friction loop — what load is supposed to happen during practice that AI short-circuits — and how to redesign practice so AI use builds the skill rather than replacing it.",
        "command": "My students use AI to practice problems before an exam and their scores are going down. Walk me through the cognitive friction loop: what cognitive load is supposed to happen during practice that AI short-circuits, and how I should redesign practice sessions so that using AI builds the skill rather than replacing the practice.",
        "segment": "Why Students Who Practice With AI Score Lower on the Exam",
    },
    "data-minimization-prompt": {
        "title": "Why Pasting a Student's Name into Claude Is a Privacy Decision, Not a Prompt",
        "narration": "Your turn. Paste this: you write student feedback using Claude. Ask Claude to show you the data minimization principle applied to educational prompts — what information to never include, what you can include with redaction, and what anonymization pattern makes feedback useful without pasting real student data.",
        "command": "I use Claude to write feedback on student work. Show me the data minimization principle applied to educational prompts: what student information I should never include in a Claude prompt, what I can include with redaction, and what anonymization pattern makes the feedback genuinely useful without pasting real student data.",
        "segment": "Why Pasting a Student's Name into Claude Is a Privacy Decision, Not a Prompt",
    },
    "feedback-that-replaces": {
        "title": "Why Helpful Feedback Can Steal the Student's Own Learning",
        "narration": "Your turn. Paste this: you want to write feedback that teaches rather than corrects. Ask Claude for the rule for when feedback is too helpful — when it takes over cognitive work the student needs to do — and show you how to convert over-helpful feedback into feedback that returns the work to the student.",
        "command": "I want to write feedback that teaches rather than corrects. Give me the rule for when feedback is too helpful — when it takes over the cognitive work the student needs to do — versus when it scaffolds correctly. Then show me how to convert three examples of over-helpful feedback into feedback that returns the work to the student.",
        "segment": "Why Helpful Feedback Can Steal the Student's Own Learning",
    },
    "outcome-before-topic": {
        "title": "Why Telling Claude the Topic Is the Wrong First Step",
        "narration": "Your turn. Paste this: you're using Claude to build a lesson. Ask Claude to show you the difference between starting with a topic versus starting with a learning outcome — and what it produces differently when you give it the outcome first instead of the subject name.",
        "command": "I want to use Claude to build a lesson. Show me the difference between starting with 'I'm teaching photosynthesis' versus starting with 'By the end of class students will be able to explain why a plant in a dark room stops producing sugar' — and walk me through what Claude produces differently when I give it the outcome instead of the topic.",
        "segment": "Why Telling Claude the Topic Is the Wrong First Step",
    },
    "receiving-vs-producing": {
        "title": "Why AI Produces Lesson Plans Where the Teacher Does All the Thinking",
        "narration": "Your turn. Paste this: you ask Claude for a lesson plan and it gives you one where you explain and students receive. Ask Claude how to rewrite the plan so students do the intellectual work — specifically what prompts flip the cognitive load from teacher to student.",
        "command": "I ask Claude to generate a lesson plan and it gives me a plan where I explain, model, and demonstrate — and students receive. Show me how to rewrite a given lesson plan so students are doing the intellectual work: what questions to ask Claude to flip the cognitive load from teacher to student.",
        "segment": "Why AI Produces Lesson Plans Where the Teacher Does All the Thinking",
    },
    "rubric-adjective-trap": {
        "title": "Why 'Good' in a Rubric Teaches Students Nothing About Quality",
        "narration": "Your turn. Paste this: your rubric uses adjectives like excellent, good, developing, beginning. Ask Claude to explain why these teach students nothing about actual quality — and then convert one of your rubric rows into a behavioral rubric that shows the difference between levels without evaluative adjectives.",
        "command": "My rubric uses adjectives like 'excellent,' 'good,' 'developing,' and 'beginning.' Show me why these teach students nothing about what quality actually looks like — and then convert one of my rubric rows into a behavioral rubric that shows students the difference between levels without using any evaluative adjectives.",
        "segment": "Why 'Good' in a Rubric Teaches Students Nothing About Quality",
    },
    "vox-phase-gate": {
        "title": "Why the Same AI Tool Helps a Teacher and Harms a Student",
        "narration": "Your turn. Paste this: you want to understand the phase-gate principle — why the same Claude prompt that helps a teacher prepare is harmful when given to a student working through the material. Ask Claude for the framework: where in the learning sequence AI helps teachers, where it helps students, and where neither should use it.",
        "command": "I want to understand the phase-gate principle: why the same Claude prompt that helps a teacher prepare is harmful when given to a student working through the same material. Give me the framework for drawing the phase gate — where in the learning sequence AI should be used by teachers, where students should engage with AI, and where neither should use it.",
        "segment": "Why the Same AI Tool Helps a Teacher and Harms a Student",
    },
}

fixed = 0

# Pattern A — base slugs
for base_slug, correct_title in PATTERN_A.items():
    for slug in [base_slug, f"claude-liam-{base_slug}"]:
        path = os.path.join(BASE, slug, "beat_sheet.json")
        if not os.path.exists(path):
            continue
        bak = path + ".bak-cfe-v1"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        with open(path) as f:
            d = json.load(f)
        beats = d.get("beats", d.get("scenes", []))
        strip_all_sublines(beats)
        ok = ensure_outro_props(beats, correct_title, slug)
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed += 1
        status = "OK" if ok else "WARN(no OUTRO beat)"
        print(f"FIXED(A) [{status}]: {slug}")

# Pattern B — base slugs + claude-liam-* copies
for base_slug, patch in PATTERN_B.items():
    for slug in [base_slug, f"claude-liam-{base_slug}"]:
        path = os.path.join(BASE, slug, "beat_sheet.json")
        if not os.path.exists(path):
            continue
        bak = path + ".bak-cfe-v1"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        with open(path) as f:
            d = json.load(f)
        meta = d.get("metadata", {})
        fix_voice(meta)
        beats = d.get("beats", d.get("scenes", []))
        strip_all_sublines(beats)
        # Also ensure OUTRO props are correct
        ensure_outro_props(beats, patch["title"], slug)
        # Patch YOURTURN
        ok = patch_yourturn(beats, patch["narration"], patch["command"], patch["segment"])
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed += 1
        status = "OK" if ok else "WARN(no YT beat)"
        print(f"FIXED(B) [{status}]: {slug}")

print(f"\nDone. {fixed} files fixed.")
