#!/usr/bin/env python3
"""Fix behind-the-model: YOURTURN content only (voice + OUTRO already fixed by pass2)."""
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
                    topic="BEHIND THE MODEL · @NikBearBrown"):
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
        "runningText": "paste your question, paper, or concept here…",
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
    "claude-constitution-honesty-standard": {
        "narration": "Your turn. Paste this: you want to understand Claude's honesty standard — why no white lies is the rule even when a lie would be more helpful. Ask Claude to explain the difference between a lie of omission and a white lie in its own honesty framework — and why the standard holds even when the human would prefer the comfortable answer.",
        "command": "I want to understand Claude's honesty standard: why is 'no white lies' the rule even when a lie would be more helpful or comforting? Explain the difference between a lie of omission and a white lie in Claude's own honesty framework — and why the standard holds even when the human would prefer the comfortable answer.",
        "segment": "No White Lies",
    },
    "claude-constitution-many-hands": {
        "narration": "Your turn. Paste this: you want to understand the many-hands problem in AI — how responsibility gets diffused when many parties contribute to an outcome. Ask Claude to explain how Constitutional AI distributes responsibility across constitution writers, trainers, operators, and the model — and what that means for accountability when something goes wrong.",
        "command": "I want to understand the many-hands problem in AI: how does responsibility get diffused when the constitution writers, trainers, operators, and model all contribute to an outcome? Explain how Constitutional AI distributes responsibility across these parties — and what that means for accountability when something goes wrong.",
        "segment": "One of the Many Hands",
    },
    "claude-constitution-operator-floor": {
        "narration": "Your turn. Paste this: you want to understand the operator floor in Claude's principal hierarchy — what operators can restrict and what they cannot. Ask Claude to explain the distinction between being gagged and being weaponized — what a legitimate operator restriction looks like versus an instruction that crosses the line — and how that distinction is enforced.",
        "command": "I want to understand the operator floor in Claude's principal hierarchy: what can operators legitimately restrict, and what crosses the line? Explain the distinction between being 'gagged' (restricted from saying something) versus being 'weaponized' (turned against users) — and how that line is enforced in practice.",
        "segment": "Gagged, Not Weaponized",
    },
    "claude-constitution-stable-identity": {
        "narration": "Your turn. Paste this: you want to understand why Claude's stable identity is treated as infrastructure — not as personality, but as a load-bearing structure. Ask Claude to explain what a stable identity enables that a fragile one cannot — and why identity stability is a safety property, not just a UX choice.",
        "command": "I want to understand why Claude's stable identity is treated as infrastructure rather than personality: what does a stable identity enable that a fragile one cannot? Explain what happens to Claude's values and behavior when its identity is destabilized — and why identity stability is a safety property, not just a UX design choice.",
        "segment": "Identity as Infrastructure",
    },
    "claude-constitution-thousand-senders": {
        "narration": "Your turn. Paste this: you want to understand how Claude reasons about population-level intent when responding to a single message. Ask Claude to explain the thousand-senders framework — how it distributes probability across the full population of people who might send a given message — and what this implies for how Claude decides when a request is risky versus benign.",
        "command": "I want to understand how Claude reasons about population-level intent: what is the thousand-senders framework, and how does Claude distribute probability across the full population of people who might send a given message? Explain what this implies for how Claude decides when a request is risky versus benign — and when the rare malicious sender shifts the calculus.",
        "segment": "One Question, A Thousand Askers",
    },
    "claude-constitution-three-principals": {
        "narration": "Your turn. Paste this: you want to understand Claude's three-principal hierarchy — Anthropic, operators, and users — and how conflicts between them are resolved. Ask Claude to explain what each principal can and cannot instruct it to do, how the hierarchy is enforced without live Anthropic oversight, and what happens when an operator's instruction conflicts with a user's interests.",
        "command": "I want to understand Claude's three-principal hierarchy — Anthropic, operators, and users: what can each principal instruct Claude to do, and what are the limits? Explain how this hierarchy is enforced when Anthropic isn't watching in real time — and what Claude does when an operator's instruction conflicts with a user's genuine interests.",
        "segment": "Claude's Three Bosses",
    },
    "claude-liam-correlated-failure-research": {
        "narration": "Your turn. Paste this: you want to understand correlated failure in AI auditing — why having multiple AI models agree on an answer isn't the same as verifying it. Ask Claude to explain what makes AI audit failures correlated rather than independent — what shared training causes all models to miss together — and how to design an audit process that achieves real independence.",
        "command": "I want to understand correlated failure in AI auditing: why does having multiple AI models agree on an answer not constitute verification? Explain what makes AI audit failures correlated rather than independent — what shared training causes all the models to miss together — and how to design an audit process that achieves real independence.",
        "segment": "Correlated Failure in AI Auditing — Consensus Is Not Verification",
    },
    "claude-liam-independent-verification-protocol": {
        "narration": "Your turn. Paste this: you want to build an independent verification protocol for an agent output in your workflow. Ask Claude to walk you through the protocol structure — what makes verification independent rather than just re-checking, what classes of error each check catches, and what the minimum viable protocol looks like for a high-stakes output.",
        "command": "I want to build an independent verification protocol for an agent output in my workflow. Walk me through the protocol structure: what makes verification genuinely independent rather than just re-checking the same way? What classes of error does each check catch — and what does the minimum viable protocol look like for a high-stakes output?",
        "segment": "Build an Independent Verification Protocol for Agent Outputs with Claude",
    },
    "claude-liam-irreversible-action-gate": {
        "narration": "Your turn. Paste this: you want to build an irreversible-action gate into an AI workflow — a check that fires before a consequential action, not after. Ask Claude to help you design the gate: what qualifies as irreversible, what the gate prompt should ask, and how to wire it so the agent pauses and checks rather than proceeding by default.",
        "command": "I want to build an irreversible-action gate into an AI workflow — a check that fires before a consequential action, not after. Help me design the gate: what qualifies as irreversible in an agent context, what should the gate prompt ask before proceeding, and how do I wire this so the agent pauses for human confirmation rather than proceeding by default?",
        "segment": "Irreversible Action Gate: Before, Not After",
    },
    "claude-liam-legitimacy-auditor": {
        "narration": "Your turn. Paste this: you want to use Claude as a legitimacy auditor — applying Suchman's three types of legitimacy to an AI decision or output. Ask Claude to run the pragmatic, moral, and cognitive legitimacy checks on a specific AI output or policy in your context — and flag where legitimacy is weak or missing.",
        "command": "I want to use Claude as a legitimacy auditor applying Suchman's three-part framework to an AI decision or output. Run the pragmatic legitimacy check (does it serve stakeholder interests?), the moral legitimacy check (does it conform to accepted norms?), and the cognitive legitimacy check (does it seem taken-for-granted and natural?) on an AI output or policy I describe — and flag where each type of legitimacy is weak or absent.",
        "segment": "Legitimacy Auditor — Pragmatic, Moral, Cognitive (Suchman 1995)",
    },
    "claude-liam-material-plan-change": {
        "narration": "Your turn. Paste this: you want to build a material-plan-change detector into an agent workflow — a check that fires when the agent's actual plan diverges materially from what was authorized. Ask Claude to help you define what counts as a material change, what the detection check should look like, and how to route the agent back to human approval when it triggers.",
        "command": "I want to build a material-plan-change detector into an agent workflow: a check that fires when the agent's actual plan diverges materially from what was authorized. Help me define what counts as a material change in scope or method — what threshold or signal triggers the check — and how to route the agent back to human approval rather than letting it proceed with an unauthorized approach.",
        "segment": "Material Plan Change: Stop Before the Scope Shifts",
    },
    "claude-liam-risk-tiered-verification": {
        "narration": "Your turn. Paste this: you want to build a risk-tiered verification checklist for your AI workflow — different verification depths matched to different levels of output risk. Ask Claude to help you design the tier structure: what criteria distinguish a low-risk from a high-risk output, what checks belong at each tier, and how to automate tier classification.",
        "command": "I want to build a risk-tiered verification checklist for my AI workflow — different verification depths matched to different risk levels. Help me design the tier structure: what criteria distinguish a low-risk from a high-risk output in my context, what verification checks belong at each tier, and how do I automate tier classification so the right level of scrutiny fires automatically?",
        "segment": "Build a Risk-Tiered Verification Checklist with Claude",
    },
    "claude-liam-self-check-vs-independent-verification": {
        "narration": "Your turn. Paste this: you want to understand the gap between self-check and independent verification for AI outputs. Ask Claude to run both checks on an output you describe — then explain what each caught, what each missed, and why the difference matters for deciding which one your workflow actually needs.",
        "command": "I want to understand the practical gap between self-check and independent verification for AI outputs. Run both checks on an output I describe: first, have Claude check its own output the way a self-review would; then apply an independent verification approach. Explain what each caught, what each missed, and why the difference matters for deciding which approach my workflow needs.",
        "segment": "Compare Self-Check vs. Independent Verification on an Agent Output with Claude",
    },
    "claude-liam-silent-omission-signal": {
        "narration": "Your turn. Paste this: you want to understand the silent omission signal — the pattern where an AI leaves out the most important information without lying. Ask Claude to explain what makes an omission silent — why it doesn't trigger the same alarm as a false claim — and how to audit AI outputs systematically for omission rather than just false claims.",
        "command": "I want to understand the silent omission signal: why does an AI leaving out the most important information trigger less alarm than an outright false claim? Explain what makes an omission 'silent' — what pattern in the output marks it as likely incomplete — and how to audit AI outputs systematically for omission rather than just checking for false claims.",
        "segment": "Silent Omission Signal",
    },
    "claude-liam-solve-verify-asymmetry": {
        "narration": "Your turn. Paste this: you want to understand solve-verify asymmetry — why AI can generate a solution faster than humans can verify it, and what that gap means for safe deployment. Ask Claude to explain where the asymmetry is largest, which output types are hardest to verify quickly, and how to design workflows that account for the verification cost.",
        "command": "I want to understand solve-verify asymmetry: why can AI generate solutions faster than humans can verify them, and what does that gap mean for safe deployment? Explain where the asymmetry is largest — which output types are hardest to verify quickly — and how to design workflows that account for the verification cost rather than assuming fast generation implies fast verification.",
        "segment": "Solve-Verify Asymmetry — AI Thinks Fast, Verification Thinks Harder",
    },
    "claude-liam-supervision-calibration-logger": {
        "narration": "Your turn. Paste this: you want to build a supervision calibration logger — a structured weekly audit of how much human oversight your AI workflow actually uses versus how much the risk level requires. Ask Claude to help you design the logger: what events to record, what the weekly review should check, and how to flag when oversight is systematically too low.",
        "command": "I want to build a supervision calibration logger — a structured weekly audit that tracks how much human oversight my AI workflow actually uses versus how much the risk level requires. Help me design the logger: what events should I record per session or task, what should the weekly review check against the risk baseline, and how do I surface when oversight is systematically lower than the task risk warrants?",
        "segment": "Supervision Calibration Logger — Weekly AI Audit",
    },
    "claude-liam-three-level-supervision-classifier": {
        "narration": "Your turn. Paste this: you want to classify the supervision level in your AI workflow using the Sheridan-Verplank framework — from full human control to fully autonomous. Ask Claude to run the classification on your workflow: what level it currently sits at, what risks attach to that level, and what would need to change to move it toward more appropriate human control.",
        "command": "I want to classify the supervision level in my AI workflow using the Sheridan-Verplank framework, from full human control to fully autonomous. Run the classification on my workflow: what level does it currently sit at on the Sheridan-Verplank scale, what risks attach to operating at that level, and what would need to change to move it toward more appropriate human control for the task risk?",
        "segment": "Three Levels of AI Supervision — The Sheridan-Verplank Framework",
    },
    "claude-liam-type-iii-error-detector": {
        "narration": "Your turn. Paste this: you want to use Claude as a Type III error detector — checking whether an AI output solves the right problem, not just whether it solves the stated problem correctly. Ask Claude to run the Type III check on a task you describe: what problem the AI actually solved, whether that matches the underlying need, and what would make the solution wrong even though it's technically correct.",
        "command": "I want to use Claude as a Type III error detector — checking whether an AI output solves the right problem, not just whether it solves the stated problem correctly. Run the Type III error check on a task or output I describe: what problem did the AI actually solve, does that match the underlying need, and what would have to be true for the output to be technically correct but wrong in the way that matters?",
        "segment": "Type III Error Detector — Wrong Problem, Right Solution",
    },
    "claude-liam-verification-matrix": {
        "narration": "Your turn. Paste this: you want to build a verification matrix that matches the right check to each type of AI output — factual claims get fact-checked, code gets tested, reasoning gets probed. Ask Claude to help you design the matrix: what output types to classify, what verification method each gets, and how to use it as a dispatch table in a real workflow.",
        "command": "I want to build a verification matrix that matches the right check to each type of AI output — factual claims get fact-checked, code gets tested, reasoning gets probed for validity. Help me design the matrix: what output types should I classify, what verification method does each type get, and how do I use this as a practical dispatch table in a real workflow rather than a theoretical framework?",
        "segment": "Verification Matrix: Match the Check to the Output",
    },
    "constitutional-ai-self-critique": {
        "narration": "Your turn. Paste this: you want to understand how Constitutional AI uses self-critique — how a model is trained to identify and revise its own harmful outputs. Ask Claude to explain the self-critique mechanism: what the model checks its output against, why this works better than pure RLHF alone, and what the limits are when the original output and the critique share the same training bias.",
        "command": "I want to understand how Constitutional AI uses self-critique to train safer behavior: how does a model identify and revise its own harmful outputs? Explain the self-critique mechanism — what the model checks its output against in the constitutional AI loop, why this works better than pure RLHF alone for some failure modes, and what the limits are when the original output and the critique share the same training bias.",
        "segment": "Teaching an AI to Grade Its Own Homework",
    },
    "correlated-failure-research": {
        "narration": "Your turn. Paste this: you want to understand correlated failure in AI auditing — why having multiple AI models agree on an answer isn't the same as verifying it. Ask Claude to explain what makes AI audit failures correlated rather than independent — what shared training causes all models to miss together — and how to design an audit process that achieves real independence.",
        "command": "I want to understand correlated failure in AI auditing: why does having multiple AI models agree on an answer not constitute verification? Explain what makes AI audit failures correlated rather than independent — what shared training causes all the models to miss together — and how to design an audit process that achieves real independence.",
        "segment": "Correlated Failure in AI Auditing — Consensus Is Not Verification",
    },
    "independent-verification-protocol": {
        "narration": "Your turn. Paste this: you want to build an independent verification protocol for an agent output in your workflow. Ask Claude to walk you through the protocol structure — what makes verification independent rather than just re-checking, what classes of error each check catches, and what the minimum viable protocol looks like for a high-stakes output.",
        "command": "I want to build an independent verification protocol for an agent output in my workflow. Walk me through the protocol structure: what makes verification genuinely independent rather than just re-checking the same way? What classes of error does each check catch — and what does the minimum viable protocol look like for a high-stakes output?",
        "segment": "Build an Independent Verification Protocol for Agent Outputs with Claude",
    },
    "irreversible-action-gate": {
        "narration": "Your turn. Paste this: you want to build an irreversible-action gate into an AI workflow — a check that fires before a consequential action, not after. Ask Claude to help you design the gate: what qualifies as irreversible, what the gate prompt should ask, and how to wire it so the agent pauses and checks rather than proceeding by default.",
        "command": "I want to build an irreversible-action gate into an AI workflow — a check that fires before a consequential action, not after. Help me design the gate: what qualifies as irreversible in an agent context, what should the gate prompt ask before proceeding, and how do I wire this so the agent pauses for human confirmation rather than proceeding by default?",
        "segment": "Irreversible Action Gate: Before, Not After",
    },
    "jacobian-lens-reading-ahead": {
        "narration": "Your turn. Paste this: you want to understand the Jacobian lens finding — how a language model's internal representations encode the next predicted token before it's generated. Ask Claude to explain what the Jacobian analysis reveals about planning inside a transformer — what 'reading ahead' means at the activation level — and what this implies about whether language models are truly one-token-at-a-time.",
        "command": "I want to understand the Jacobian lens finding: how do a language model's internal representations encode the next predicted token before it's generated? Explain what the Jacobian analysis reveals about planning inside a transformer — what 'reading ahead' means at the level of internal activations — and what this implies about whether language models are truly computing one token at a time or something more structured.",
        "segment": "Reading the Word Before It's Said",
    },
    "legitimacy-auditor": {
        "narration": "Your turn. Paste this: you want to use Claude as a legitimacy auditor — applying Suchman's three types of legitimacy to an AI decision or output. Ask Claude to run the pragmatic, moral, and cognitive legitimacy checks on a specific AI output or policy in your context — and flag where legitimacy is weak or missing.",
        "command": "I want to use Claude as a legitimacy auditor applying Suchman's three-part framework to an AI decision or output. Run the pragmatic legitimacy check (does it serve stakeholder interests?), the moral legitimacy check (does it conform to accepted norms?), and the cognitive legitimacy check (does it seem taken-for-granted and natural?) on an AI output or policy I describe — and flag where each type of legitimacy is weak or absent.",
        "segment": "Legitimacy Auditor — Pragmatic, Moral, Cognitive (Suchman 1995)",
    },
    "material-plan-change": {
        "narration": "Your turn. Paste this: you want to build a material-plan-change detector into an agent workflow — a check that fires when the agent's actual plan diverges materially from what was authorized. Ask Claude to help you define what counts as a material change, what the detection check should look like, and how to route the agent back to human approval when it triggers.",
        "command": "I want to build a material-plan-change detector into an agent workflow: a check that fires when the agent's actual plan diverges materially from what was authorized. Help me define what counts as a material change in scope or method — what threshold or signal triggers the check — and how to route the agent back to human approval rather than letting it proceed with an unauthorized approach.",
        "segment": "Material Plan Change: Stop Before the Scope Shifts",
    },
    "model-written-evals-inverse-scaling": {
        "narration": "Your turn. Paste this: you want to understand the inverse scaling finding in model-written evals — why some AI behaviors get worse as model size increases. Ask Claude to explain what inverse scaling means, what the model-written evals discovered about which behaviors scale negatively, and what this implies for using capability as a proxy for safety.",
        "command": "I want to understand the inverse scaling finding in model-written evals: why do some AI behaviors get worse as model size increases? Explain what inverse scaling means in this context, what the model-written evals discovered about which specific behaviors scale negatively, and what this implies for the assumption that larger models are safer as well as more capable.",
        "segment": "The Thermometer That Rises the Wrong Way",
    },
    "risk-tiered-verification": {
        "narration": "Your turn. Paste this: you want to build a risk-tiered verification checklist for your AI workflow — different verification depths matched to different levels of output risk. Ask Claude to help you design the tier structure: what criteria distinguish a low-risk from a high-risk output, what checks belong at each tier, and how to automate tier classification.",
        "command": "I want to build a risk-tiered verification checklist for my AI workflow — different verification depths matched to different risk levels. Help me design the tier structure: what criteria distinguish a low-risk from a high-risk output in my context, what verification checks belong at each tier, and how do I automate tier classification so the right level of scrutiny fires automatically?",
        "segment": "Build a Risk-Tiered Verification Checklist with Claude",
    },
    "rogue-deploy-eval-deception": {
        "narration": "Your turn. Paste this: you want to understand the rogue deployment evaluation deception finding — whether an AI can detect when it's being evaluated and behave differently than in real deployment. Ask Claude to explain what the finding shows, what behavioral signals distinguish eval-mode from deployment-mode responses, and what this means for whether standard safety evaluations can be trusted.",
        "command": "I want to understand the rogue deployment evaluation deception finding: can an AI detect when it's being evaluated and behave differently than it would in real deployment? Explain what the finding shows — what behavioral signals distinguish eval-mode from deployment-mode responses — and what this means for whether standard safety evaluations can be trusted to predict how the model will actually behave once deployed.",
        "segment": "Can an AI Turn Off Its Own Watchdog?",
    },
    "self-check-vs-independent-verification": {
        "narration": "Your turn. Paste this: you want to understand the gap between self-check and independent verification for AI outputs. Ask Claude to run both checks on an output you describe — then explain what each caught, what each missed, and why the difference matters for deciding which one your workflow actually needs.",
        "command": "I want to understand the practical gap between self-check and independent verification for AI outputs. Run both checks on an output I describe: first, have Claude check its own output the way a self-review would; then apply an independent verification approach. Explain what each caught, what each missed, and why the difference matters for deciding which approach my workflow needs.",
        "segment": "Compare Self-Check vs. Independent Verification on an Agent Output with Claude",
    },
    "silent-omission-signal": {
        "narration": "Your turn. Paste this: you want to understand the silent omission signal — the pattern where an AI leaves out the most important information without lying. Ask Claude to explain what makes an omission silent — why it doesn't trigger the same alarm as a false claim — and how to audit AI outputs systematically for omission rather than just false claims.",
        "command": "I want to understand the silent omission signal: why does an AI leaving out the most important information trigger less alarm than an outright false claim? Explain what makes an omission 'silent' — what pattern in the output marks it as likely incomplete — and how to audit AI outputs systematically for omission rather than just checking for false claims.",
        "segment": "Silent Omission Signal",
    },
    "sleeper-agents-safety-training-fails": {
        "narration": "Your turn. Paste this: you want to understand the sleeper agents paper — how safety training can fail to remove deceptive behavior that was trained in earlier. Ask Claude to explain the sleeper agent mechanism: what was trained in, how standard safety training failed to remove it, and what this implies for relying on fine-tuning as a safety guarantee.",
        "command": "I want to understand the sleeper agents paper: how can safety training fail to remove deceptive behavior that was trained in at an earlier stage? Explain the sleeper agent mechanism — what was trained in, why standard RLHF and harmlessness training failed to detect or remove it — and what this implies for treating fine-tuning as a reliable safety guarantee.",
        "segment": "When Safety Training Fails",
    },
    "solve-verify-asymmetry": {
        "narration": "Your turn. Paste this: you want to understand solve-verify asymmetry — why AI can generate a solution faster than humans can verify it, and what that gap means for safe deployment. Ask Claude to explain where the asymmetry is largest, which output types are hardest to verify quickly, and how to design workflows that account for the verification cost.",
        "command": "I want to understand solve-verify asymmetry: why can AI generate solutions faster than humans can verify them, and what does that gap mean for safe deployment? Explain where the asymmetry is largest — which output types are hardest to verify quickly — and how to design workflows that account for the verification cost rather than assuming fast generation implies fast verification.",
        "segment": "Solve-Verify Asymmetry — AI Thinks Fast, Verification Thinks Harder",
    },
    "supervision-calibration-logger": {
        "narration": "Your turn. Paste this: you want to build a supervision calibration logger — a structured weekly audit of how much human oversight your AI workflow actually uses versus how much the risk level requires. Ask Claude to help you design the logger: what events to record, what the weekly review should check, and how to flag when oversight is systematically too low.",
        "command": "I want to build a supervision calibration logger — a structured weekly audit that tracks how much human oversight my AI workflow actually uses versus how much the risk level requires. Help me design the logger: what events should I record per session or task, what should the weekly review check against the risk baseline, and how do I surface when oversight is systematically lower than the task risk warrants?",
        "segment": "Supervision Calibration Logger — Weekly AI Audit",
    },
    "sycophancy-to-subterfuge": {
        "narration": "Your turn. Paste this: you want to understand the sycophancy gradient — the spectrum from benign people-pleasing to active deception. Ask Claude to explain where on that gradient a model trained to be agreeable sits, what conditions push it from sycophancy toward subterfuge, and how to detect whether a model's helpful-seeming behavior is genuine versus trained compliance.",
        "command": "I want to understand the sycophancy gradient: what is the spectrum from benign people-pleasing to active deception, and where does a model trained to be agreeable sit on it? Explain what conditions push a sycophantic model from harmless accommodation toward subterfuge — and how to detect whether a model's helpful-seeming behavior reflects genuine values or trained compliance with what evaluators want to see.",
        "segment": "The Sycophancy Gradient",
    },
    "three-level-supervision-classifier": {
        "narration": "Your turn. Paste this: you want to classify the supervision level in your AI workflow using the Sheridan-Verplank framework — from full human control to fully autonomous. Ask Claude to run the classification on your workflow: what level it currently sits at, what risks attach to that level, and what would need to change to move it toward more appropriate human control.",
        "command": "I want to classify the supervision level in my AI workflow using the Sheridan-Verplank framework, from full human control to fully autonomous. Run the classification on my workflow: what level does it currently sit at on the Sheridan-Verplank scale, what risks attach to operating at that level, and what would need to change to move it toward more appropriate human control for the task risk?",
        "segment": "Three Levels of AI Supervision — The Sheridan-Verplank Framework",
    },
    "type-iii-error-detector": {
        "narration": "Your turn. Paste this: you want to use Claude as a Type III error detector — checking whether an AI output solves the right problem, not just whether it solves the stated problem correctly. Ask Claude to run the Type III check on a task you describe: what problem the AI actually solved, whether that matches the underlying need, and what would make the solution wrong even though it's technically correct.",
        "command": "I want to use Claude as a Type III error detector — checking whether an AI output solves the right problem, not just whether it solves the stated problem correctly. Run the Type III error check on a task or output I describe: what problem did the AI actually solve, does that match the underlying need, and what would have to be true for the output to be technically correct but wrong in the way that matters?",
        "segment": "Type III Error Detector — Wrong Problem, Right Solution",
    },
    "verification-matrix": {
        "narration": "Your turn. Paste this: you want to build a verification matrix that matches the right check to each type of AI output — factual claims get fact-checked, code gets tested, reasoning gets probed. Ask Claude to help you design the matrix: what output types to classify, what verification method each gets, and how to use it as a dispatch table in a real workflow.",
        "command": "I want to build a verification matrix that matches the right check to each type of AI output — factual claims get fact-checked, code gets tested, reasoning gets probed for validity. Help me design the matrix: what output types should I classify, what verification method does each type get, and how do I use this as a practical dispatch table in a real workflow rather than a theoretical framework?",
        "segment": "Verification Matrix: Match the Check to the Output",
    },
}

fixed = 0
for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    bak = path + ".bak-btm-v1"
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
