#!/usr/bin/env python3
"""Fix claude-for-education: YOURTURN content only (voice + OUTRO already fixed by pass2)."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_beat_id(b):
    return b.get("beat_id", b.get("id", ""))

def is_outro(b):
    bid = get_beat_id(b); act = b.get("act", "")
    shot = b.get("shot") or {}
    rem = shot.get("remotion") if isinstance(shot, dict) else None
    if not isinstance(rem, dict): rem = {}
    pat = rem.get("pattern", "")
    top_rem = b.get("remotion") or {}
    if not isinstance(top_rem, dict): top_rem = {}
    pat_top = top_rem.get("pattern", "")
    return (act == "OUTRO" or "outro" in bid.lower()
            or "Outro" in pat or "Outro" in pat_top or bid in ("OUTRO", "BOUT"))

def ensure_yourturn(beats, narration, command, segment,
                    topic="CLAUDE FOR EDUCATION · @NikBearBrown"):
    yt_idx = None; outro_idx = None
    for i, b in enumerate(beats):
        bid = get_beat_id(b); act = b.get("act", "").lower()
        shot = b.get("shot") or {}
        rem = shot.get("remotion") if isinstance(shot, dict) else None
        if not isinstance(rem, dict): rem = {}
        pat = rem.get("pattern", "")
        narr = b.get("narration_text", b.get("narration", "")) or ""
        if (bid in ("YOURTURN", "BHTF", "H01")
                or (act in ("handoff", "your-turn") and pat == "ClaudeComposerAsk")
                or (pat == "ClaudeComposerAsk" and bid not in ("B00", "B01") and "Your turn." in narr)):
            yt_idx = i
        if is_outro(b):
            outro_idx = i

    yt_props = {
        "greeting": "Your turn.",
        "command": command,
        "segment": segment,
        "topic": topic,
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Claude Sonnet",
        "runningText": "paste your course materials, rubric, or learning objective here…",
    }

    if yt_idx is not None:
        b = beats[yt_idx]
        b["narration_text"] = narration
        b["beat_id"] = "YOURTURN"
        b["act"] = "your-turn"
        shot = b.setdefault("shot", {})
        shot["type"] = "REMOTION"
        shot["source"] = "own"
        shot["remotion"] = {"pattern": "ClaudeComposerAsk", "props": yt_props}
        b.pop("remotion", None)
        return True

    new_beat = {
        "beat_id": "YOURTURN",
        "act": "your-turn",
        "narration_text": narration,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {"pattern": "ClaudeComposerAsk", "props": yt_props},
        },
    }
    if outro_idx is not None:
        beats.insert(outro_idx, new_beat)
    else:
        beats.append(new_beat)
    return True

PATCHES = {
    "advising-privacy-gate": {
        "narration": "Your turn. Paste this: you want to anonymize student information before prompting an AI in an advising context. Ask Claude to help you design the advising privacy gate — what fields must be stripped or generalized before the prompt is sent, what gets kept because it's necessary for the advice, and how to verify the gate is working without seeing the original data.",
        "command": "I want to design an advising privacy gate — a process for anonymizing student information before sending it to an AI model. What fields must be stripped or generalized before the prompt (identifiers, enrollment status, grades), what information is safe to keep because it's necessary for the advice to be useful, and how do I verify the gate is working correctly?",
        "segment": "Advising Privacy Gate: Anonymize Before Prompting",
    },
    "ai-feedback-evidence-review": {
        "narration": "Your turn. Paste this: you want to know what the research actually says about whether AI feedback improves student learning. Ask Claude to synthesize the evidence on AI feedback effectiveness — what studies have found, what conditions make AI feedback more or less useful, and what the gaps in the current research are.",
        "command": "I want to know what the research actually says about whether AI feedback improves student learning. Synthesize the evidence on AI feedback effectiveness: what have studies found about its impact on learning outcomes, under what conditions is AI feedback more or less useful than human feedback, and what are the significant gaps in the current research?",
        "segment": "Research What Makes AI Feedback Effective: Evidence Review",
    },
    "ai-policy-classifier": {
        "narration": "Your turn. Paste this: you want to build a student AI policy classifier — a tool that takes a course policy statement and classifies it as permissive, restrictive, or ambiguous, with a rationale. Ask Claude to help you design the classifier: what categories to use, what signals in the policy text drive each classification, and how to flag policies that leave the most common student questions unanswered.",
        "command": "I want to build a student AI policy classifier that takes a course policy statement and classifies it as permissive, restrictive, or ambiguous — with a rationale. Help me design the classifier: what categories should I use, what signals in the policy text drive each classification, and how should it flag policies that leave the most common student questions unanswered?",
        "segment": "Build a Student AI Policy Classifier with Claude",
    },
    "assessment-vulnerability-map": {
        "narration": "Your turn. Paste this: you want to build an assessment vulnerability map — a structured analysis of which parts of an existing assessment are most at risk from AI-assisted completion. Ask Claude to run the analysis on an assessment you describe: what tasks can be trivially completed by AI, what requires genuine student work, and what design changes would reduce the vulnerability without reducing the rigor.",
        "command": "I want to build an assessment vulnerability map for an existing assignment. Run the analysis: which tasks can be trivially completed by AI with no meaningful student engagement, which require genuine student work that AI cannot substitute for, and what specific design changes would reduce the AI-completion risk without reducing the intellectual rigor of the assessment?",
        "segment": "Build an Assessment Vulnerability Map with Claude",
    },
    "assignment-stress-test": {
        "narration": "Your turn. Paste this: you want to stress-test an assignment before students see it — finding the gaps, ambiguities, and AI-bypass routes before they do. Ask Claude to run a full stress test on an assignment you paste in: what a motivated student exploiting AI would do, what an anxious student would misread, and what changes would close the most serious gaps.",
        "command": "I want to stress-test an assignment before students see it. Run a full stress test: what would a motivated student exploiting AI do to complete this with minimal learning, what would an anxious student misread or misinterpret in the instructions, and what specific changes would close the most serious gaps before I release it?",
        "segment": "Stress-Test the Assignment Before Students Do",
    },
    "backward-design-lesson": {
        "narration": "Your turn. Paste this: you want to backward-design a lesson outcome — starting from what students need to demonstrate, then designing back to instruction and assessment. Ask Claude to walk you through the backward design process for a specific topic: what the performance outcome should be, what evidence would prove mastery, and what instruction sequence leads to that evidence.",
        "command": "I want to backward-design a lesson outcome — starting from what students need to demonstrate, then designing back to instruction and assessment. Walk me through the backward design process for a specific topic I give you: what should the performance outcome be, what evidence would prove that a student has genuinely achieved it, and what instruction sequence leads to generating that evidence?",
        "segment": "Backward-Design a Lesson Outcome with Claude",
    },
    "capstone-unit-builder": {
        "narration": "Your turn. Paste this: you want to build a capstone unit that holds together coherently — not a collection of disconnected activities, but a unit where each element builds toward a single integrated outcome. Ask Claude to help you design the unit architecture: what the unifying outcome is, what sequence of activities builds toward it, and where the human teacher's judgment is load-bearing in holding it together.",
        "command": "I want to build a capstone unit that holds together coherently — not a collection of disconnected activities, but a unit where each element builds toward a single integrated outcome. Help me design the unit architecture: what should the unifying outcome be, what sequence of activities builds toward it progressively, and where is the human teacher's judgment load-bearing in holding the coherence together?",
        "segment": "Capstone Unit Builder: Coherence Is the Human's Job",
    },
    "cognitive-labor-audit": {
        "narration": "Your turn. Paste this: you want to audit a prompt for cognitive labor transfer — finding out how much of the thinking the AI does versus how much the student does. Ask Claude to run the audit on a prompt you provide: what cognitive operations the AI performs, what the student is left doing, and how to rewrite the prompt so the student carries more of the intellectual load.",
        "command": "I want to audit a prompt for cognitive labor transfer: how much of the thinking does the AI do versus how much does the student do? Run the audit on a prompt I provide: what cognitive operations does the AI perform when it responds, what is the student actually left doing, and how should I rewrite the prompt so the student carries more of the intellectual load?",
        "segment": "Audit a Prompt for Cognitive Labor Transfer with Claude",
    },
    "differentiation-audit": {
        "narration": "Your turn. Paste this: you want to audit a differentiated activity for intellectual target integrity — checking whether accommodations actually lower the cognitive demand rather than just changing the format. Ask Claude to run the differentiation audit on a lesson activity: which accommodations preserve the intellectual target, which ones accidentally remove the cognitive challenge, and how to redesign the at-risk ones.",
        "command": "I want to audit a differentiated activity for intellectual target integrity — checking whether accommodations preserve the cognitive demand or accidentally remove it. Run the differentiation audit on a lesson activity I describe: which accommodations preserve the intellectual target, which ones accidentally lower the cognitive challenge rather than just changing the format, and how should I redesign the at-risk accommodations?",
        "segment": "Differentiation Audit: Preserving the Intellectual Target",
    },
    "faculty-literature-lead": {
        "narration": "Your turn. Paste this: you want to find the right starting point in a literature, not just a list of citations. Ask Claude to give you a literature lead for a topic you're investigating — the foundational paper or theoretical framework that everything else builds on — and explain what makes it the right entry point rather than a different paper.",
        "command": "I want to find the right starting point in a literature, not just a list of citations. Give me a literature lead for a topic I'm investigating: identify the foundational paper or theoretical framework that everything else in this area builds on — and explain what makes it the right entry point rather than a different influential paper in the same space.",
        "segment": "Literature Leads Are Not Citations",
    },
    "feedback-type-classifier": {
        "narration": "Your turn. Paste this: you want to build a feedback type classifier — a tool that takes a piece of written feedback and classifies it as evaluative, descriptive, or directive, with implications for how the student will likely receive it. Ask Claude to help you design the classifier: what signals in the text drive each classification, and what the research says about which feedback type produces the most learning.",
        "command": "I want to build a feedback type classifier that takes a piece of written feedback and classifies it as evaluative, descriptive, or directive — with implications for how students will likely receive it. Help me design the classifier: what signals in the feedback text drive each classification, and what does the research say about which feedback type produces the most durable learning versus the most student compliance?",
        "segment": "Build a Feedback Type Classifier with Claude",
    },
    "instructional-brief-eight-fields": {
        "narration": "Your turn. Paste this: you want to fill out the eight-field instructional brief for a unit or lesson you're designing. Ask Claude to walk you through each field — learning objective, prior knowledge required, assessment evidence, instructional sequence, differentiation approach, AI integration policy, materials needed, and success criteria — and help you tighten each one so the brief is actually actionable.",
        "command": "I want to fill out the eight-field instructional brief for a unit or lesson I'm designing. Walk me through each field: learning objective, prior knowledge required, assessment evidence, instructional sequence, differentiation approach, AI integration policy, materials needed, and success criteria. For each one, help me tighten my draft so the brief is actually actionable rather than vague.",
        "segment": "The Eight-Field Instructional Brief",
    },
    "instructional-brief-generator": {
        "narration": "Your turn. Paste this: you want to build an instructional brief generator — a tool that takes a topic and grade level and produces a draft eight-field instructional brief. Ask Claude to help you design the generator: what inputs it needs, what each of the eight fields should contain for the output to be useful, and how to structure the prompt so the output is a starting point for revision, not a final product.",
        "command": "I want to build an instructional brief generator that takes a topic and grade level and produces a draft eight-field instructional brief. Help me design the generator: what inputs does it need beyond topic and grade level, what should each of the eight fields contain for the output to be a useful starting point, and how should I structure the prompt so the output invites revision rather than presenting itself as finished?",
        "segment": "Build an Instructional Brief Generator with Claude",
    },
    "k12-teacher-skills-missing-math-prerequisite-t-scaffolded": {
        "narration": "Your turn. Paste this: you want to understand why a missing math prerequisite can't be scaffolded around — it has to be routed through. Ask Claude to explain the difference between scaffolding and routing in mathematics prerequisite gaps — what scaffolding attempts to do and why it fails when the prerequisite is genuinely missing — and how to diagnose which situation a struggling student is in.",
        "command": "I want to understand why a missing math prerequisite can't be scaffolded around — it has to be routed through. Explain the difference between scaffolding and routing in prerequisite gaps: what does scaffolding attempt to do and why does it fail when the prerequisite knowledge is genuinely absent rather than just inaccessible? And how do I diagnose which situation a struggling student is actually in?",
        "segment": "Why a missing math prerequisite can't be scaffolded around — only routed through",
    },
    "lesson-ai-integration-audit": {
        "narration": "Your turn. Paste this: you want to audit an existing lesson for AI integration quality — not whether AI is present, but whether it's integrated in a way that serves learning rather than replacing it. Ask Claude to run the audit on a lesson you describe: where AI is currently used, whether each use increases or decreases student cognitive engagement, and what changes would make the integration defensible.",
        "command": "I want to audit an existing lesson for AI integration quality — not whether AI is present, but whether each use serves learning rather than replacing it. Run the audit on a lesson I describe: identify where AI is currently used, assess whether each use increases or decreases meaningful student cognitive engagement, and specify what changes would make the integration pedagogically defensible.",
        "segment": "Build a Lesson AI-Integration Audit with Claude",
    },
    "manuscript-reviewer-response": {
        "narration": "Your turn. Paste this: you want to use Claude as an adversarial reader for a manuscript reviewer response — finding the weakest points in your rebuttal before you submit it. Ask Claude to read your reviewer response and flag the three places where a skeptical editor is most likely to remain unconvinced — and suggest how to strengthen each one.",
        "command": "I want to use Claude as an adversarial reader for a manuscript reviewer response. Read my reviewer response and flag the three places where a skeptical editor is most likely to remain unconvinced — where the rebuttal is vague, concedes too much, or fails to address the reviewer's actual concern — and suggest specifically how to strengthen each one before I submit.",
        "segment": "Manuscript Reviewer Response: Claude as Adversarial Reader",
    },
    "rubric-adjective-detector": {
        "narration": "Your turn. Paste this: you want to build a rubric adjective detector — a tool that finds vague quality adjectives in a rubric and flags them as ungraded. Ask Claude to run the detector on a rubric you paste in: which adjectives are doing grading work without defining a standard, what a student cannot figure out from them, and how to replace each one with an observable criterion.",
        "command": "I want to build a rubric adjective detector that finds vague quality adjectives and flags them as ungraded. Run the detector on a rubric I paste in: which adjectives are doing grading work without defining an observable standard (words like 'clear,' 'appropriate,' 'thorough'), what a student cannot figure out from each flagged term, and how to replace each one with a criterion a student could actually verify before submitting?",
        "segment": "Build a Rubric Adjective Detector with Claude",
    },
    "udl-choice-board": {
        "narration": "Your turn. Paste this: you want to audit a UDL choice board for cognitive demand consistency — making sure all paths maintain the same intellectual target even as the format varies. Ask Claude to run the audit on a choice board you describe: which options preserve the core cognitive demand, which ones quietly lower it, and how to redesign the lower-demand options so all paths are genuinely equivalent.",
        "command": "I want to audit a UDL choice board for cognitive demand consistency — ensuring all paths maintain the same intellectual target even as the format varies. Run the audit on a choice board I describe: which options preserve the core cognitive demand of the learning objective, which ones quietly lower it by allowing surface-level completion, and how should I redesign the lower-demand options so all paths are genuinely equivalent?",
        "segment": "UDL Choice Board Audit: Same Demand, Different Path",
    },
}

fixed = 0
for base_slug, patch in PATCHES.items():
    for slug in [base_slug, f"claude-liam-{base_slug}"]:
        path = os.path.join(BASE, slug, "beat_sheet.json")
        if not os.path.exists(path):
            continue
        bak = path + ".bak-edu-v1"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        with open(path) as f:
            d = json.load(f)
        beats = d.get("beats", d.get("scenes", []))
        ensure_yourturn(beats, patch["narration"], patch["command"], patch["segment"])
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed += 1
        print(f"FIXED: {slug}")

print(f"\nDone. {fixed} files fixed.")
