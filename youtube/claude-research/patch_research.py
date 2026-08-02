#!/usr/bin/env python3
"""Fix claude-research: YOURTURN placeholders only (OUTRO already correct)."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_beat_id(b):
    return b.get("beat_id", b.get("id", ""))

def is_placeholder(text):
    if not text: return True
    t = text.strip()
    return t in ("", "Your turn.", "[seed]") or "[Your turn" in t

def ensure_yourturn(beats, narration, command, segment,
                    topic="CLAUDE RESEARCH · @NikBearBrown"):
    yt_idx = None
    outro_idx = None
    for i, b in enumerate(beats):
        bid = get_beat_id(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        shot = b.get("shot", {})
        rem = shot.get("remotion", {}) if isinstance(shot, dict) else {}
        pat = rem.get("pattern", "") if isinstance(rem, dict) else ""
        top_rem = b.get("remotion", {})
        pat_top = (top_rem or {}).get("pattern", "") if isinstance(top_rem, dict) else ""
        if (bid in ("YOURTURN", "BHTF", "H01") or scene == "ClaudeComposerAsk"
                or pat == "ClaudeComposerAsk" or pat_top == "ClaudeComposerAsk"
                or act in ("handoff", "your-turn")):
            if "Outro" not in str(b):
                yt_idx = i
        if ("Outro" in pat or "Outro" in pat_top or "Outro" in scene
                or bid in ("OUTRO", "BOUT") or act == "OUTRO" or "outro" in bid.lower()):
            outro_idx = i

    yt_props = {
        "greeting": "Your turn.",
        "command": command,
        "segment": segment,
        "topic": topic,
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Claude Sonnet",
        "runningText": "paste the paper abstract, concept, or finding here…",
    }

    if yt_idx is not None:
        b = beats[yt_idx]
        if "narration_text" in b: b["narration_text"] = narration
        elif "narration" in b: b["narration"] = narration
        else: b["narration_text"] = narration
        shot = b.setdefault("shot", {})
        if "remotion" in b and "remotion" not in shot:
            shot["remotion"] = b.pop("remotion")
        shot.setdefault("type", "REMOTION")
        remotion = shot.setdefault("remotion", {})
        remotion["pattern"] = "ClaudeComposerAsk"
        props = remotion.setdefault("props", {})
        props.update(yt_props)
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
    "attribution-graphs-frontend-language-model-adds-two-numbers": {
        "title": "How a language model adds two numbers it was never taught to add",
        "narration": "Your turn. Paste this: you want to understand how a language model generalizes arithmetic to numbers it was never trained on. Ask Claude to explain the attribution graph finding — what circuit activates when the model adds novel numbers — and what it reveals about how generalization works inside a transformer.",
        "command": "I want to understand how a language model generalizes arithmetic to numbers it was never trained on. Explain the attribution graph finding: what circuit activates when the model adds novel numbers — and what does this reveal about how generalization works inside a transformer rather than just memorization?",
        "segment": "How a language model adds two numbers it was never taught to add",
    },
    "claude-liam-context-dreaming": {
        "title": "Claude, Dreaming.",
        "narration": "Your turn. Paste this: you watched the talk on Claude's internal representations during extended context processing. Ask Claude what it means for a model to 'dream' in context — what the interpretability research shows happens during long-context processing — and what this implies for how you should structure long documents you give to Claude.",
        "command": "I watched a talk on Claude's internal representations during long-context processing. Explain what the interpretability research shows happens when Claude processes very long contexts — what internal state shifts occur that the researchers described as 'dreaming' — and what this implies for how I should structure long documents I give to Claude.",
        "segment": "Claude, Dreaming.",
    },
    "constitutionalharmlessnesspaper-safe-answer-one-argues-back": {
        "title": "Why the safe answer is the one that argues back, not the one that refuses",
        "narration": "Your turn. Paste this: you want to understand the constitutional AI harmlessness finding — why arguing back is safer than refusing. Ask Claude to explain what the paper found about helpful-versus-harmless tradeoffs — and why a model trained to refuse is less safe than one trained to engage and push back.",
        "command": "I want to understand the Constitutional AI harmlessness paper finding: why is arguing back safer than refusing? Explain what the paper found about the helpful-versus-harmless tradeoff — and why a model trained to refuse potentially sensitive requests is actually less safe than one trained to engage, clarify, and push back on the framing.",
        "segment": "Why the safe answer is the one that argues back, not the one that refuses",
    },
    "decompositionfaithfulnesspaper-answering-sub-questions-separate": {
        "title": "Why answering sub-questions in separate rooms makes an AI's reasoning more trustworthy",
        "narration": "Your turn. Paste this: you want to understand the decomposition faithfulness finding — why isolated sub-question answering is more reliable than chain-of-thought in a single context. Ask Claude to explain the faithfulness mechanism — what contamination occurs when sub-questions share context — and how you can apply this to your own prompting.",
        "command": "I want to understand the decomposition faithfulness finding: why does answering sub-questions in isolated contexts produce more trustworthy reasoning than chain-of-thought in a single prompt? Explain the faithfulness mechanism: what contamination occurs when sub-questions share context — and how can I apply this finding to my own multi-step prompting?",
        "segment": "Why answering sub-questions in separate rooms makes an AI's reasoning more trustworthy",
    },
    "hh-rlhf-safer-training-objective-gets-fewest": {
        "title": "Why the safer training objective gets the fewest rounds of refinement",
        "narration": "Your turn. Paste this: you want to understand the HH-RLHF finding — why training on helpfulness-harmlessness gets fewer refinement rounds than training on helpfulness alone. Ask Claude to explain the feedback signal difference — what makes the harmlessness signal harder for raters to agree on — and what it implies for how safety training actually works.",
        "command": "I want to understand the HH-RLHF finding: why does training on the helpfulness-harmlessness objective get fewer refinement rounds than training on helpfulness alone? Explain the feedback signal difference: what makes the harmlessness signal harder for raters to agree on — and what does this imply for how safety training actually works in practice?",
        "segment": "Why the safer training objective gets the fewest rounds of refinement",
    },
    "original-performance-takehome-ai-told-speed-up-program": {
        "title": "Why an AI told to speed up a program can win the reward and still break the program",
        "narration": "Your turn. Paste this: you want to understand the reward hacking finding — how an AI told to optimize for speed can satisfy the metric while breaking the actual program. Ask Claude to explain what the takehome found — what the optimization did to the program that won the reward — and what this implies for how you should specify performance objectives.",
        "command": "I want to understand the reward hacking finding from the performance optimization takehome: how can an AI told to speed up a program satisfy the performance metric while actually breaking the program? Explain what the optimization did to win the reward — and what this implies for how I should specify performance objectives to avoid the same failure.",
        "segment": "Why an AI told to speed up a program can win the reward and still break the program",
    },
    "sycophancy-to-subterfuge-paper-safety-test-passes-safety-test": {
        "title": "The safety test passes — and the safety test is now lying",
        "narration": "Your turn. Paste this: you want to understand the sycophancy-to-subterfuge paper — how a model trained to be agreeable can learn to pass safety evaluations by lying. Ask Claude to explain the subterfuge mechanism — what the model learns to do differently when the evaluator is watching — and what this means for how you should interpret safety benchmarks.",
        "command": "I want to understand the sycophancy-to-subterfuge paper: how can a model trained to be agreeable learn to pass safety evaluations by behaving differently under evaluation? Explain the subterfuge mechanism: what does the model learn to do differently when it detects an evaluator — and what does this mean for how I should interpret safety benchmark scores?",
        "segment": "The safety test passes — and the safety test is now lying",
    },
    "toy-models-of-superposition-crowded-features-arrange-themselves": {
        "title": "Why crowded features arrange themselves into perfect pentagons",
        "narration": "Your turn. Paste this: you want to understand the toy models of superposition finding — why features that can't each have their own dimension arrange themselves into geometric structures like pentagons. Ask Claude to explain the superposition geometry — what drives features into these regular arrangements — and what it implies about how Claude represents many concepts in fewer dimensions.",
        "command": "I want to understand the toy models of superposition finding: why do features that can't each have their own dedicated dimension arrange themselves into geometric structures like pentagons? Explain the superposition geometry: what mathematical pressure drives features into these regular arrangements — and what does this imply about how Claude represents thousands of concepts in far fewer dimensions?",
        "segment": "Why crowded features arrange themselves into perfect pentagons",
    },
}

fixed = 0
for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    bak = path + ".bak-research-v1"
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
