#!/usr/bin/env python3
"""Fix claude-code: voice_id + OUTRO (NikBearBrownOutro → ClaudeTitleOutro) + YOURTURN."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_beat_id(b):
    return b.get("beat_id", b.get("id", ""))

def fix_voice(meta):
    meta.pop("voice_id", None)
    meta.pop("voice", None)   # strip "NikBearBrown" etc.
    meta["engine"] = "kokoro"
    meta["voice"] = "am_onyx"
    meta["voice_kokoro"] = "am_onyx"

def strip_all_sublines(beats):
    for b in beats:
        props = b.get("props")
        if isinstance(props, dict): props.pop("subline", None)
        shot = b.get("shot")
        if isinstance(shot, dict):
            rem = shot.get("remotion")
            if isinstance(rem, dict): rem.get("props", {}).pop("subline", None)
        rem = b.get("remotion")
        if isinstance(rem, dict): rem.get("props", {}).pop("subline", None)

def fix_genai_ban(beats):
    for b in beats:
        shot = b.get("shot", {})
        if isinstance(shot, dict) and shot.get("source") == "ai" and shot.get("motion") == "kenburns":
            shot["source"] = "own"
            shot.pop("motion", None)

def is_placeholder(text):
    if not text: return True
    t = text.strip()
    return t in ("", "Your turn.", "[seed]") or "[Your turn" in t or t == "Your turn. [seed]"

def ensure_outro(beats, title, slug):
    """Find OUTRO beat (any pattern) and upgrade to ClaudeTitleOutro; or append one."""
    outro_idx = None
    for i, b in enumerate(beats):
        bid = get_beat_id(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        shot = b.get("shot", {})
        rem_shot = shot.get("remotion", {}) if isinstance(shot, dict) else {}
        pat_shot = rem_shot.get("pattern", "") if isinstance(rem_shot, dict) else ""
        top_rem = b.get("remotion", {})
        pat_top = top_rem.get("pattern", "") if isinstance(top_rem, dict) else ""
        if (bid in ("OUTRO", "BOUT", "B07", "O01")
                or act == "OUTRO"
                or scene in ("ClaudeTitleOutro", "NikBearBrownOutro")
                or "Outro" in pat_shot or "Outro" in pat_top
                or "outro" in bid.lower()):
            outro_idx = i
            break
    correct_props = {
        "title": title,
        "handle": "@NikBearBrown",
        "mascotSeed": slug,
    }
    if outro_idx is not None:
        b = beats[outro_idx]
        shot = b.setdefault("shot", {})
        shot["type"] = "REMOTION"
        shot["source"] = "own"
        shot.pop("motion", None)
        remotion = shot.setdefault("remotion", {})
        remotion["pattern"] = "ClaudeTitleOutro"
        props = remotion.setdefault("props", {})
        props.update(correct_props)
        props.pop("subline", None)
        props.pop("brand", None)
        props.pop("tagline", None)
        props.pop("url", None)
        # remove stale top-level remotion block if it existed
        if "remotion" in b:
            b.pop("remotion", None)
        return True
    else:
        beats.append({
            "beat_id": "OUTRO",
            "act": "OUTRO",
            "narration_text": "Nik Bear Brown. Claude Code.",
            "shot": {
                "type": "REMOTION",
                "source": "own",
                "remotion": {
                    "pattern": "ClaudeTitleOutro",
                    "props": correct_props,
                },
            },
        })
        return True

def ensure_yourturn(beats, narration, command, segment,
                    topic="CLAUDE CODE · @NikBearBrown"):
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
        pat_top = top_rem.get("pattern", "") if isinstance(top_rem, dict) else ""
        if (bid in ("YOURTURN", "BHTF", "H01")
                or scene == "ClaudeComposerAsk"
                or pat == "ClaudeComposerAsk"
                or pat_top == "ClaudeComposerAsk"
                or act in ("handoff", "your-turn")):
            if "Outro" not in str(b):
                yt_idx = i
        if (bid in ("OUTRO", "BOUT", "B07", "O01")
                or act == "OUTRO"
                or scene in ("ClaudeTitleOutro", "NikBearBrownOutro")
                or "Outro" in pat or "Outro" in pat_top
                or "outro" in bid.lower()):
            outro_idx = i

    yt_props = {
        "greeting": "Your turn.",
        "command": command,
        "segment": segment,
        "topic": topic,
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Claude Sonnet",
        "runningText": "paste your spec, CLAUDE.md, or build plan here…",
    }

    if yt_idx is not None:
        b = beats[yt_idx]
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
        remotion["pattern"] = "ClaudeComposerAsk"
        props = remotion.setdefault("props", {})
        props.update(yt_props)
        return True

    # Insert before OUTRO
    new_beat = {
        "beat_id": "YOURTURN",
        "act": "your-turn",
        "narration_text": narration,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": yt_props,
            },
        },
    }
    if outro_idx is not None:
        beats.insert(outro_idx, new_beat)
    else:
        beats.append(new_beat)
    return True

# ── PATCHES ───────────────────────────────────────────────────────────────────
PATCHES = {
    "agentic-loop-not-chatgpt": {
        "title": "Agentic Loop vs. Chatbot: Why the First Session Is Calibration",
        "narration": "Your turn. Paste this: you want to run your first agentic Claude Code session but you're not sure what to calibrate. Ask Claude for the five questions you must answer before giving it any task — and explain why a chatbot prompt fails when the loop has multiple steps and tool calls.",
        "command": "I want to run my first Claude Code agentic session but I keep treating it like a chatbot. Give me the five calibration questions I need to answer before I hand any task to the loop — and explain what breaks when I give the loop a chatbot-style prompt.",
        "segment": "Agentic Loop vs. Chatbot: Why the First Session Is Calibration",
    },
    "ai-creative-work-belongs-to-nobody": {
        "title": "Why AI Creative Work Is Beautiful and Belongs to Nobody",
        "narration": "Your turn. Paste this: you want to understand what it means to author work when AI generates the draft. Ask Claude to explain the difference between authorship and generation — and where human judgment is the only thing that makes the work yours.",
        "command": "I use AI to generate creative drafts and I want to understand what it means to be the author. Explain the difference between authorship and generation — where does my judgment become the thing that makes the work mine versus a product that belongs to nobody?",
        "segment": "Why AI Creative Work Is Beautiful and Belongs to Nobody",
    },
    "ai-homework-fluency-trap": {
        "title": "Why Doing Homework With AI Makes You Worse at the Test",
        "narration": "Your turn. Paste this: your students complete AI-assisted assignments fluently but score poorly on exams. Ask Claude to explain the fluency trap — what cognitive process the student skips when AI fills the gap — and how to redesign one assignment so practice builds the skill instead of bypassing it.",
        "command": "My students complete AI-assisted homework fluently but perform worse on exams. Explain the fluency trap: what cognitive process does the student skip when AI fills in the gap, and how do I redesign one typical homework assignment so that using AI builds the underlying skill instead of bypassing it?",
        "segment": "Why Doing Homework With AI Makes You Worse at the Test",
    },
    "boondoggle-score": {
        "title": "Score a Build Plan Using the Boondoggle Score with Claude Code",
        "narration": "Your turn. Paste this: you have a build plan and you want to score it before writing a single line of code. Ask Claude to apply the Boondoggle Score — label who does each step, flag which steps could be eliminated if a requirement changed, and identify the highest-risk row.",
        "command": "I have a build plan and I want to score it with the Boondoggle Score before writing any code. Apply the Boondoggle Score to my plan: label who does each step, flag steps that could be eliminated if a requirement changed, and identify the highest-risk row — the one every other row inherits from.",
        "segment": "Score a Build Plan Using the Boondoggle Score with Claude Code",
    },
    "boondoggle-score-anatomy": {
        "title": "The Boondoggle Score: Label Who Does Each Step",
        "narration": "Your turn. Paste this: you want to understand the Boondoggle Score anatomy before applying it. Ask Claude to walk you through each column — what it measures, what a red flag looks like in that column, and what a score above eight means for the build.",
        "command": "Walk me through the anatomy of the Boondoggle Score: what does each column measure, what does a red flag look like in each column, and what does a total score above eight mean for whether I should proceed with this build plan?",
        "segment": "The Boondoggle Score: Label Who Does Each Step",
    },
    "brutalist-three-file": {
        "title": "Three Files Before Claude Touches Anything",
        "narration": "Your turn. Paste this: you're about to start a Claude Code session on a new project. Ask Claude to help you write the three files — CLAUDE.md, spec.md, and test plan — before any code is written, and explain what breaks if you skip any one of them.",
        "command": "I'm about to start a Claude Code session on a new project. Help me write the three files I need before Claude touches any code: CLAUDE.md, a spec file, and a test plan. Explain what breaks in the session if I skip any one of these three.",
        "segment": "Three Files Before Claude Touches Anything",
    },
    "build-chapter-mapping": {
        "title": "Map Your Build Decisions to What Students Are Reading with Claude Code",
        "narration": "Your turn. Paste this: you want to trace your Claude Code build decisions back to the course material your students are reading. Ask Claude to create a chapter-to-build-decision mapping for a given chapter — which spec choices, handoff conditions, and verification steps connect directly to what the chapter teaches.",
        "command": "I want to map my Claude Code build decisions back to the course reading so students can see the connection. For a given chapter topic I describe, create a chapter-to-build-decision mapping: which spec choices, handoff conditions, and verification steps connect directly to what the chapter teaches.",
        "segment": "Map Your Build Decisions to What Students Are Reading with Claude Code",
    },
    "claude-api-one-endpoint-ladder": {
        "title": "One Door, Four Tiers",
        "narration": "Your turn. Paste this: you want to understand the Claude API tier structure before writing your first API call. Ask Claude to walk you through the four tiers — what each one gives you, when you move up, and what the single endpoint pattern looks like at each tier.",
        "command": "I want to understand the Claude API tier structure before I write my first API call. Walk me through the four tiers: what does each tier give me, when do I move up, and what does the single endpoint pattern look like at each tier?",
        "segment": "One Door, Four Tiers",
    },
    "claude-code-action-natural-trigger-review-counting-check": {
        "title": "Why the 'natural' trigger for a review-counting check is the one that lets the author bypass it",
        "narration": "Your turn. Paste this: you're designing a review-counting check and you want to find the trigger that can't be bypassed. Ask Claude to walk through the natural trigger that authors can sidestep, then show you the design pattern that closes the bypass — and why the gate has to fire before the author's action, not after.",
        "command": "I'm designing a review-counting check and I want to find the trigger that can't be bypassed by the author. Walk me through the natural trigger that authors can sidestep, then show me the design pattern that closes that bypass — and explain why the gate has to fire before the author's action, not after.",
        "segment": "Why the 'natural' trigger for a review-counting check is the one that lets the author bypass it",
    },
    "claude-code-base-action-turn-budget-stops-runaway-agent": {
        "title": "Why a turn budget stops a runaway agent more cleanly than a stopwatch",
        "narration": "Your turn. Paste this: your Claude Code agent sometimes runs far longer than expected and you want a clean stop mechanism. Ask Claude to explain why a turn budget is more reliable than a timeout — and show you the base action pattern that enforces the budget without cutting a task mid-operation.",
        "command": "My Claude Code agent sometimes runs far longer than expected. Explain why a turn budget is more reliable than a timeout for stopping a runaway agent — and show me the base action pattern that enforces the budget without cutting a task in the middle of an operation.",
        "segment": "Why a turn budget stops a runaway agent more cleanly than a stopwatch",
    },
    "claude-code-coding-assistant-deliberately-refuses-write": {
        "title": "Why a coding assistant deliberately refuses to write the 6 lines that matter",
        "narration": "Your turn. Paste this: you asked Claude Code to write a specific function and it stopped short of the six lines that actually matter. Ask Claude to explain why a deliberate refusal is correct here — what those six lines require that the assistant cannot supply — and what you need to provide before it can proceed.",
        "command": "I asked Claude Code to write a specific function and it stopped just before the six lines that actually matter. Explain why deliberately refusing to write those lines is the correct behavior — what do those lines require that the assistant cannot supply — and tell me what I need to provide before it can proceed.",
        "segment": "Why a coding assistant deliberately refuses to write the 6 lines that matter",
    },
    "claude-code-four-agents-scoring-same-bug": {
        "title": "Why four agents scoring the same bug beats one strong reviewer",
        "narration": "Your turn. Paste this: you want to use multiple Claude Code agents to review a bug and you're not sure why parallel scoring is better than one thorough review. Ask Claude to explain the variance reduction argument — and give you the prompt structure that sends the same bug to four agents with independent contexts.",
        "command": "I want to use multiple Claude Code agents to score the same bug but I'm not sure why that beats one thorough review. Explain the variance reduction argument for parallel agent scoring — and give me the prompt structure that sends the same bug to four agents with genuinely independent contexts.",
        "segment": "Why four agents scoring the same bug beats one strong reviewer",
    },
    "claude-code-monitoring-guide-doubling-claude-code-session-time": {
        "title": "Why doubling your Claude Code session time doesn't double your output",
        "narration": "Your turn. Paste this: you're spending twice as long in Claude Code sessions but your output hasn't improved. Ask Claude to diagnose the monitoring failure — what signals you should be watching that show diminishing returns before you waste the session — and what checkpoints keep a session productive.",
        "command": "I'm spending twice as long in Claude Code sessions but my output isn't improving. Diagnose the monitoring failure: what signals should I be watching that indicate diminishing returns before I waste the entire session — and what monitoring checkpoints keep a long Claude Code session productive?",
        "segment": "Why doubling your Claude Code session time doesn't double your output",
    },
    "claude-code-monitoring-guide-typing-one-word-multiply-api": {
        "title": "Why typing one word can multiply your API bill 100×",
        "narration": "Your turn. Paste this: you want to understand what Claude Code operations are expensive before you accidentally run them in a loop. Ask Claude to explain the context-window cost model — which single-word commands can trigger massive token usage — and how to monitor your session before the bill arrives.",
        "command": "I want to understand which Claude Code operations are expensive before I accidentally run them in a loop. Explain the context-window cost model: which single-word commands or operations can multiply my token usage dramatically — and how do I monitor my session cost in real time before the bill arrives?",
        "segment": "Why typing one word can multiply your API bill 100×",
    },
    "claude-code-security-review-same-eval-real-bug-one": {
        "title": "Why the same eval() is a real bug in one file and noise in another",
        "narration": "Your turn. Paste this: your security scan flagged eval() in two places but only one is a real vulnerability. Ask Claude to explain the context-dependent severity model — what makes eval() dangerous in one location and acceptable in another — and how to write a security review prompt that distinguishes the two.",
        "command": "My security scan flagged eval() in two places but I think only one is a real vulnerability. Explain the context-dependent severity model: what makes eval() dangerous in one location and acceptable in another — and show me how to write a Claude Code security review prompt that distinguishes real bugs from noise.",
        "segment": "Why the same eval() is a real bug in one file and noise in another",
    },
    "claudemd-constitution": {
        "title": "Write a CLAUDE.md Constitution for a Classroom Project with Claude Code",
        "narration": "Your turn. Paste this: you want to write a CLAUDE.md file that acts as a constitution for a classroom Claude Code project. Ask Claude for the five clauses every classroom CLAUDE.md needs — what constraints to write, what behaviors to prohibit, and how to make the file short enough that Claude actually reads and follows it.",
        "command": "I want to write a CLAUDE.md file that acts as a constitution for a classroom Claude Code project. Give me the five clauses every classroom CLAUDE.md needs: what constraints to write, what behaviors to explicitly prohibit, and how to keep the file short enough that Claude actually reads and follows it.",
        "segment": "Write a CLAUDE.md Constitution for a Classroom Project with Claude Code",
    },
    "clear-vs-compact": {
        "title": "/clear vs. /compact: Context Window Hygiene",
        "narration": "Your turn. Paste this: you're midway through a Claude Code session and your context window is filling up. Ask Claude when to use /clear versus /compact — what each command actually does to the window, which one loses your work, and what signals tell you it's time to act before the session degrades.",
        "command": "I'm midway through a Claude Code session and the context window is filling up. Tell me when to use /clear versus /compact: what does each command actually do to the context window, which one loses my work, and what signals should I watch for before the session degrades?",
        "segment": "/clear vs. /compact: Context Window Hygiene",
    },
    "code-runs-ships-wrong": {
        "title": "Why the Code Runs Fine and Still Ships Wrong",
        "narration": "Your turn. Paste this: your Claude Code build passed all tests but the shipped version failed in production. Ask Claude to name the gap between test-passing and user-serving — what verification step catches the class of bugs that tests cannot see — and give you a three-question checklist to run before every deploy.",
        "command": "My Claude Code build passed all tests but the shipped version failed in production. Name the gap between test-passing and user-serving: what verification step catches the class of bugs that tests cannot see — and give me a three-question checklist I can run before every deploy to catch this category of failure.",
        "segment": "Why the Code Runs Fine and Still Ships Wrong",
    },
    "command-development": {
        "title": "Command Development",
        "narration": "Your turn. Paste this: you want to build a custom Claude Code slash command for a workflow you run repeatedly. Ask Claude for the anatomy of a command definition — what fields are required, how the command receives context, and what makes a command reusable across projects versus one-off.",
        "command": "I want to build a custom Claude Code slash command for a workflow I run repeatedly. Give me the anatomy of a command definition: what fields are required, how the command receives context from the session, and what makes a command reusable across projects versus a one-off.",
        "segment": "Command Development",
    },
    "conducting-not-prompting": {
        "title": "Conducting, Not Prompting: The Gru/Minion Split",
        "narration": "Your turn. Paste this: you want to shift from writing prompts to conducting Claude Code like an orchestra — making decisions the model can't make while delegating execution the model can handle. Ask Claude for the Gru/Minion split: what the conductor decides versus what the minion executes, and how to restructure your next session around that split.",
        "command": "I want to shift from writing prompts to conducting Claude Code like a director — making decisions the model can't make while delegating execution to it. Explain the Gru/Minion split: what does the conductor decide versus what does the minion execute, and how do I restructure my next Claude Code session around that split?",
        "segment": "Conducting, Not Prompting: The Gru/Minion Split",
    },
    "cwc-how-we-claude-code": {
        "title": "How Anthropic Uses Claude Code",
        "narration": "Your turn. Paste this: you want to understand how Anthropic's own engineers use Claude Code internally. Ask Claude to walk you through the internal workflow pattern — how they use Claude Code for their own builds, what guardrails they apply, and what that implies for how you should structure your own sessions.",
        "command": "I want to understand how Anthropic's own engineers use Claude Code internally. Walk me through the internal workflow pattern: how do they use Claude Code for their own builds, what guardrails do they apply, and what does that imply for how I should structure my own sessions?",
        "segment": "How Anthropic Uses Claude Code",
    },
    "cwc-workshop-agent-battle-minecraft": {
        "title": "Agent Battle: Minecraft as an AI Benchmark",
        "narration": "Your turn. Paste this: you want to understand what the Minecraft agent benchmark reveals about agentic AI capability that traditional benchmarks miss. Ask Claude to explain the benchmark design — why Minecraft as an environment surfaces agent limitations that code tasks don't — and what it tells you about where agentic Claude Code will fail first.",
        "command": "I want to understand what the Minecraft agent benchmark reveals about agentic AI that traditional benchmarks miss. Explain the benchmark design: why does Minecraft as an environment surface agent limitations that code tasks don't — and what does it tell me about where agentic Claude Code will most likely fail first?",
        "segment": "Agent Battle: Minecraft as an AI Benchmark",
    },
    "dangerous-middle-activity": {
        "title": "Design a Classroom Activity Around the Dangerous Middle with Claude Code",
        "narration": "Your turn. Paste this: you want to design a classroom activity that helps students recognize when they're in the dangerous middle — where output looks correct but verification was skipped. Ask Claude for an activity structure that puts students in a dangerous-middle scenario, forces them to name it, and teaches the exit protocol.",
        "command": "I want to design a classroom activity that helps students recognize when they're in the dangerous middle — output looks correct but verification was skipped. Give me an activity structure that puts students inside a dangerous-middle scenario, forces them to identify it by name, and teaches the protocol for getting out.",
        "segment": "Design a Classroom Activity Around the Dangerous Middle with Claude Code",
    },
    "dangerous-middle-detection": {
        "title": "Detect and Name Dangerous Middle Tasks Before Delegating",
        "narration": "Your turn. Paste this: you have a task you're about to delegate to Claude Code and you want to check whether it falls into the dangerous middle before you hand it over. Ask Claude for the detection checklist — what properties make a task dangerous-middle, and what you must add to the spec before delegating safely.",
        "command": "I have a task I'm about to delegate to Claude Code and I want to check whether it's a dangerous-middle task before I hand it over. Give me the detection checklist: what properties make a task fall into the dangerous middle, and what do I need to add to my spec before I can delegate it safely?",
        "segment": "Detect and Name Dangerous Middle Tasks Before Delegating",
    },
    "defending-code-reference-harness-count-field-checked-one-pass": {
        "title": "Why a 'count field' checked in one pass and used in another is a buffer overflow waiting between them",
        "narration": "Your turn. Paste this: you're reviewing code where a count field is validated in one function and consumed in another. Ask Claude to explain the time-of-check to time-of-use vulnerability — why the gap between the check pass and the use pass is where the overflow lives — and how to write the harness that catches it.",
        "command": "I'm reviewing code where a count field is validated in one function and consumed in another. Explain the time-of-check to time-of-use vulnerability: why is the gap between the check pass and the use pass where the overflow lives — and how do I write the test harness that catches this class of bug before it ships?",
        "segment": "Why a 'count field' checked in one pass and used in another is a buffer overflow waiting between them",
    },
    "defending-code-reference-harness-pipeline-runs-same-crash-three": {
        "title": "Why the pipeline runs the same crash three times before it believes it",
        "narration": "Your turn. Paste this: your CI pipeline reruns the same failing test multiple times before marking the build as failed. Ask Claude to explain the retry-before-fail design pattern — why three runs is the minimum reliable signal — and how to write the reference harness that distinguishes a flaky test from a deterministic crash.",
        "command": "My CI pipeline reruns the same failing test three times before marking the build as failed. Explain the retry-before-fail design pattern: why is three runs the minimum reliable signal, and how do I write the reference harness that distinguishes a flaky test from a deterministic crash?",
        "segment": "Why the pipeline runs the same crash three times before it believes it",
    },
    "engineering-partner-loop": {
        "title": "Run the Engineering Partner Loop with Claude Code",
        "narration": "Your turn. Paste this: you want to run Claude Code as an engineering partner, not just a code generator. Ask Claude to walk you through the engineering partner loop — the cycle of propose, review, commit that keeps you in the conductor role — and show you what the loop looks like on a real three-step task.",
        "command": "I want to run Claude Code as an engineering partner, not just a code generator. Walk me through the engineering partner loop: the propose-review-commit cycle that keeps me in the conductor role — and show me what that loop looks like running on a real three-step task.",
        "segment": "Run the Engineering Partner Loop with Claude Code",
    },
    "five-questions-before-code": {
        "title": "Five Questions Before Code: The Calibration Session",
        "narration": "Your turn. Paste this: you're about to start a Claude Code session and you want to run a calibration first. Ask Claude to give you the five questions — and explain why answering all five before the first tool call determines whether the session succeeds or wastes your time.",
        "command": "I'm about to start a Claude Code session and I want to run a calibration first. Give me the five questions I need to answer before the first tool call — and explain why each one determines whether the session succeeds or wastes my time.",
        "segment": "Five Questions Before Code: The Calibration Session",
    },
    "five-supervisory-capacities": {
        "title": "Label the Five Supervisory Capacities in a Build Session with Claude Code",
        "narration": "Your turn. Paste this: you want to audit your Claude Code build session against the five supervisory capacities. Ask Claude to name each capacity, give you a one-sentence test for whether you're exercising it, and flag which capacity is most often skipped in a fast-moving session.",
        "command": "I want to audit my Claude Code build session against the five supervisory capacities. Name each capacity, give me a one-sentence test for whether I'm exercising it during a live session, and flag which capacity is most often skipped when a session is moving fast.",
        "segment": "Label the Five Supervisory Capacities in a Build Session with Claude Code",
    },
    "fluency-correctness-gap": {
        "title": "Measure the Fluency vs. Correctness Gap with Claude Code",
        "narration": "Your turn. Paste this: you suspect your Claude Code output is fluent but not correct. Ask Claude to design a measurement protocol — how to run the same task with and without verification, what the gap between fluent and correct looks like, and how large the gap has to be before you change your workflow.",
        "command": "I suspect my Claude Code output is fluent but not correct. Design a measurement protocol: how do I run the same task with and without verification, what does the gap between fluent and correct look like, and how large does the gap have to be before I need to change my workflow?",
        "segment": "Measure the Fluency vs. Correctness Gap with Claude Code",
    },
    "fluency-trap-danger-zone": {
        "title": "Why the Student Who Knows More Than the Teacher Is in the Most Danger",
        "narration": "Your turn. Paste this: you have students who are more technically fluent with AI than their instructor but are making more errors on graded work. Ask Claude to explain why fluency advantage is a danger zone — what the student stops doing because they can generate answers so easily — and how to design an assignment that breaks the fluency trap.",
        "command": "I have students who are more fluent with AI than I am but making more errors on graded work. Explain why technical fluency is a danger zone: what does the fluent student stop doing because they can generate answers so easily — and how do I design an assignment that breaks the fluency trap for advanced students?",
        "segment": "Why the Student Who Knows More Than the Teacher Is in the Most Danger",
    },
    "grading-skill-definition": {
        "title": "Define a Reusable Skill for Common Teacher Workflows with Claude Code",
        "narration": "Your turn. Paste this: you want to build a Claude Code skill file for a grading workflow you run every semester. Ask Claude for the anatomy of a skill definition — what fields make a skill reusable across courses, how to version it, and what test you run to confirm the skill still works after a Claude update.",
        "command": "I want to build a Claude Code skill file for a grading workflow I run every semester. Give me the anatomy of a skill definition: what fields make a skill reusable across courses, how do I version it, and what test do I run to confirm the skill still produces correct output after a Claude model update?",
        "segment": "Define a Reusable Skill for Common Teacher Workflows with Claude Code",
    },
    "gru-slash-v0-gate": {
        "title": "Gru's v0 Gate: One Sentence or You Don't Build",
        "narration": "Your turn. Paste this: you want to apply Gru's v0 gate — the rule that you can't start a build until you can state the problem in one sentence. Ask Claude to help you write the one-sentence problem statement for a project you're working on, and explain what's wrong with the sentence if it takes more than one.",
        "command": "I want to apply Gru's v0 gate to a project before I start building. Help me write the one-sentence problem statement for the project I describe — and explain what is wrong with my statement if it takes more than one sentence to say what the build actually does.",
        "segment": "Gru's v0 Gate: One Sentence or You Don't Build",
    },
    "handoff-condition-protocol": {
        "title": "Build and Test a Handoff Condition Protocol with Claude Code",
        "narration": "Your turn. Paste this: you want to write handoff conditions that actually stop Claude from handing off a broken task. Ask Claude for the handoff condition protocol — what a condition must specify to be testable, how to write a failing condition test, and what 'looks good' tells Claude versus what an explicit condition tells it.",
        "command": "I want to write handoff conditions that actually stop Claude from handing off a broken task. Give me the handoff condition protocol: what must a condition specify to be testable, how do I write a failing condition test, and what does 'looks good' tell Claude versus what an explicit written condition tells it?",
        "segment": "Build and Test a Handoff Condition Protocol with Claude Code",
    },
    "hook-advisory-vs-deterministic": {
        "title": "Hook vs. CLAUDE.md: Cannot, Not Do Not",
        "narration": "Your turn. Paste this: you need Claude to never generate grades automatically, but you're not sure whether to put that rule in CLAUDE.md or enforce it with a hook. Ask Claude to explain the difference between advisory and deterministic enforcement — what CLAUDE.md says versus what a hook enforces — and when to use each.",
        "command": "I need Claude to never generate grades automatically and I'm deciding whether to write the rule in CLAUDE.md or enforce it with a hook. Explain the difference between advisory and deterministic enforcement: what does CLAUDE.md say versus what does a hook actually enforce — and how do I know which one to use for a given rule?",
        "segment": "Hook vs. CLAUDE.md: Cannot, Not Do Not",
    },
    "hook-development": {
        "title": "Hook Development",
        "narration": "Your turn. Paste this: you want to build a Claude Code hook that fires before a specific tool use and blocks it under defined conditions. Ask Claude for the hook development pattern — the PreToolUse structure, how to write the condition, and how to test that the hook fires correctly without running the tool.",
        "command": "I want to build a Claude Code hook that fires before a specific tool use and blocks it under defined conditions. Give me the hook development pattern: the PreToolUse structure, how to write the blocking condition, and how to test that the hook fires correctly without actually running the tool.",
        "segment": "Hook Development",
    },
    "intent-layer-authorship": {
        "title": "Intent Layer: The Five Questions Claude Cannot Answer for You",
        "narration": "Your turn. Paste this: you want to identify which decisions in your Claude Code session belong to you and cannot be delegated. Ask Claude for the five intent-layer questions — the ones where Claude's answer is always wrong because it requires your specific context, goals, and accountability — and how to answer each before the session starts.",
        "command": "I want to identify which decisions in my Claude Code session belong to me and cannot be delegated to the model. Give me the five intent-layer questions — the ones where Claude's answer is always wrong because they require my specific context, goals, and accountability — and walk me through how to answer each one before my session starts.",
        "segment": "Intent Layer: The Five Questions Claude Cannot Answer for You",
    },
    "one-sentence-problem-statement": {
        "title": "Why the One-Sentence Problem Statement Is the Most Expensive Thing You Write",
        "narration": "Your turn. Paste this: you want to understand why a vague problem statement costs more than a precise one. Ask Claude to show you a vague problem statement and a precise one for the same project — what changes in the Claude Code session when you start with each — and what the cost difference looks like after ten hours of build time.",
        "command": "I want to understand why a vague problem statement costs more than a precise one when working with Claude Code. Show me a vague problem statement and a precise one for the same project: what changes in the Claude Code session when I start with each — and what does the cost difference look like after ten hours of build time?",
        "segment": "Why the One-Sentence Problem Statement Is the Most Expensive Thing You Write",
    },
    "package-hallucination-scanner": {
        "title": "Catch a Package Hallucination Before It Becomes a Slopsquatting Attack",
        "narration": "Your turn. Paste this: Claude Code just suggested a package name and you want to verify it's real before you install it. Ask Claude to build you a package hallucination scanner — the exact verification steps to run before npm install — and explain what slopsquatting is and how the hallucinated name becomes an attack vector.",
        "command": "Claude Code just suggested a package name and I want to verify it's real before I install it. Build me a package hallucination scanner: the exact verification steps I should run before npm install — and explain what slopsquatting is and how a hallucinated package name becomes an attack vector that targets my project.",
        "segment": "Catch a Package Hallucination Before It Becomes a Slopsquatting Attack",
    },
    "pagination-bug-dangerous-middle": {
        "title": "Why the Most Dangerous Claude Output Is the One That Passes Every Test",
        "narration": "Your turn. Paste this: you have a pagination bug that passed every test but failed in production. Ask Claude to walk you through why tests cannot catch this category of bug — what the dangerous middle looks like for pagination logic — and what verification step would have caught it before deploy.",
        "command": "I have a pagination bug that passed every test but failed in production. Walk me through why tests cannot catch this category of bug: what does the dangerous middle look like for pagination logic — and what specific verification step would have caught the bug before it reached production?",
        "segment": "Why the Most Dangerous Claude Output Is the One That Passes Every Test",
    },
    "pattern-analysis-subagent": {
        "title": "Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code",
        "narration": "Your turn. Paste this: you want to deploy a Claude Code subagent that analyzes patterns in student work across a batch of submissions. Ask Claude for the subagent deployment structure — how to define the subagent's task, how to give it isolated context, and how to aggregate its output back into the grading tool.",
        "command": "I want to deploy a Claude Code subagent that analyzes patterns in student submissions across a batch. Give me the subagent deployment structure: how do I define the subagent's analysis task, how do I give it isolated context for each submission, and how do I aggregate its pattern output back into my grading tool?",
        "segment": "Deploy a Pattern-Analysis Subagent for a Grading Tool with Claude Code",
    },
    "plan-mode-interruption": {
        "title": "Plan Mode: Freeze Before the Byte Changes",
        "narration": "Your turn. Paste this: you want to use Claude Code's plan mode to review the plan before any files change. Ask Claude when to trigger plan mode, what to look for in the plan before you approve it, and how to interrupt a running plan if you see something wrong mid-execution.",
        "command": "I want to use Claude Code's plan mode to review what it intends to do before any files change. Tell me when to trigger plan mode, what to look for in the plan before I approve it, and how to interrupt a running plan mid-execution if I see something wrong.",
        "segment": "Plan Mode: Freeze Before the Byte Changes",
    },
    "post-build-document": {
        "title": "Write the Post-Build Document for a Classroom Tool with Claude Code",
        "narration": "Your turn. Paste this: you just finished a Claude Code build for a classroom tool and you need to write the post-build document. Ask Claude for the five sections every post-build document needs — what went wrong, what the spec missed, what the handoff conditions were, what the tests prove, and what the next builder needs to know.",
        "command": "I just finished a Claude Code build for a classroom tool and I need to write the post-build document. Give me the five sections every post-build document needs: what went wrong, what the spec missed, what the handoff conditions were, what the tests prove, and what the next person who touches this build needs to know before they start.",
        "segment": "Write the Post-Build Document for a Classroom Tool with Claude Code",
    },
    "pretooluse-grade-blocker": {
        "title": "Build a PreToolUse Hook That Blocks Grade Generation with Claude Code",
        "narration": "Your turn. Paste this: you want to build a PreToolUse hook that prevents Claude Code from writing or outputting a grade under any circumstance. Ask Claude for the full hook implementation — the condition that fires, the block action, and the test that confirms the hook cannot be bypassed by rephrasing the request.",
        "command": "I want to build a PreToolUse hook that prevents Claude Code from writing or outputting a grade under any circumstance. Give me the full hook implementation: the condition that fires before grade-related tool use, the block action, and the test that confirms this hook cannot be bypassed by rephrasing or reframing the grade request.",
        "segment": "Build a PreToolUse Hook That Blocks Grade Generation with Claude Code",
    },
    "prompt-is-a-wish-spec-is-a-contract": {
        "title": "Why 'Write Me a Login Function' Is Not a Prompt",
        "narration": "Your turn. Paste this: you've been writing prompts when you should be writing specs. Ask Claude to convert 'Write me a login function' into a specification — and show you the three things a spec has that a prompt doesn't: verifiable behavior, explicit scope, and a rejection condition.",
        "command": "I've been writing prompts to Claude Code when I should be writing specs. Convert 'Write me a login function' into a specification — and show me the three things a spec has that a prompt doesn't: verifiable behavior, explicit scope, and a rejection condition Claude can use to stop and ask instead of guessing.",
        "segment": "Why 'Write Me a Login Function' Is Not a Prompt",
    },
    "rewind-not-fix-forward": {
        "title": "Rewind, Not Fix-Forward: The Andon Cord",
        "narration": "Your turn. Paste this: your Claude Code session went wrong and you're deciding whether to fix the current broken state or rewind to the last known-good checkpoint. Ask Claude for the Andon cord rule — when rewinding is always cheaper than fixing forward — and what the rewind protocol looks like in a live Claude Code session.",
        "command": "My Claude Code session went wrong and I'm deciding whether to fix the broken state or rewind to the last known-good checkpoint. Give me the Andon cord rule: when is rewinding always cheaper than fixing forward — and what does the rewind protocol look like in a live Claude Code session with multiple tool calls already made?",
        "segment": "Rewind, Not Fix-Forward: The Andon Cord",
    },
    "riv2025-long-horizon-coding-agent-demo-backend-test-passes-reali": {
        "title": "Why a backend test that passes in reality stays permanently 'failing'",
        "narration": "Your turn. Paste this: you have a backend test that passes when you run it manually but your CI marks it as failing. Ask Claude to explain the environment-divergence failure mode — why a test that passes in reality stays permanently failing in a specific environment — and how to write the diagnostic that identifies which layer is lying.",
        "command": "I have a backend test that passes when I run it manually but CI consistently marks it as failing. Explain the environment-divergence failure mode: why does a test that passes in reality stay permanently failing in a specific environment — and how do I write the diagnostic that identifies which layer — CI config, environment variables, or test harness — is the source of the discrepancy?",
        "segment": "Why a backend test that passes in reality stays permanently 'failing'",
    },
    "riv2025-long-horizon-coding-agent-demo-wildcard-covering-every-a": {
        "title": "Why a wildcard covering every Anthropic model still denies every cross-region call",
        "narration": "Your turn. Paste this: you wrote a wildcard IAM policy that covers every Anthropic model but your cross-region API calls are still being denied. Ask Claude to explain the wildcard scope problem — why a model-level wildcard doesn't cover cross-region routing — and what the corrected policy pattern looks like.",
        "command": "I wrote a wildcard IAM policy covering every Anthropic model but cross-region API calls are still being denied. Explain the wildcard scope problem: why doesn't a model-level wildcard cover cross-region routing — and what does the corrected policy pattern look like for an account that needs to call Claude across multiple regions?",
        "segment": "Why a wildcard covering every Anthropic model still denies every cross-region call",
    },
    "skill-build-once": {
        "title": "Skill File Anatomy: Build Once, Invoke Every Semester",
        "narration": "Your turn. Paste this: you want to build a Claude Code skill file that you write once and invoke every semester without rewriting it. Ask Claude for the skill file anatomy — the five fields that make a skill stable across model updates — and how to test that the skill still works when Claude changes.",
        "command": "I want to build a Claude Code skill file I write once and invoke every semester without rewriting it. Give me the skill file anatomy: the five fields that make a skill stable across model updates, how to version the skill, and how to test that the skill still produces correct output when Claude's underlying model changes.",
        "segment": "Skill File Anatomy: Build Once, Invoke Every Semester",
    },
    "slash-context-window-check": {
        "title": "/context Check: Read Your Window Before It Fills",
        "narration": "Your turn. Paste this: you want to know when to run /context and what to do with the output before your Claude Code session degrades. Ask Claude to explain what the context window check shows, what the threshold is where you need to act, and what the three options are once you hit that threshold.",
        "command": "I want to know when to run /context in Claude Code and what to do with the output before my session degrades. Explain what the context window check shows, what the threshold is where I need to act, and what my three options are once I hit that threshold.",
        "segment": "/context Check: Read Your Window Before It Fills",
    },
    "slopsquatting-hallucinated-package": {
        "title": "Why Slopsquatting Turns Claude's Wrong Answer Into a Security Hole",
        "narration": "Your turn. Paste this: you want to understand how a hallucinated package name becomes a real attack vector. Ask Claude to walk through the slopsquatting attack chain — how the hallucination creates the name, how an attacker registers it, and what the code looks like when the malicious package is installed.",
        "command": "I want to understand how a hallucinated package name becomes a real attack vector. Walk me through the slopsquatting attack chain: how does the hallucination create the package name, how does an attacker register a malicious package under that name, and what does my code look like when the malicious package is silently installed?",
        "segment": "Why Slopsquatting Turns Claude's Wrong Answer Into a Security Hole",
    },
    "software-design-document": {
        "title": "Write a Five-Artifact Software Design Document with Claude Code",
        "narration": "Your turn. Paste this: you want to write a software design document for a Claude Code project before any code is written. Ask Claude for the five-artifact structure — what each artifact covers, in what order to write them, and which artifact Claude Code will read first when the build session starts.",
        "command": "I want to write a software design document for a Claude Code project before any code is written. Give me the five-artifact structure: what does each artifact cover, in what order should I write them, and which artifact will Claude Code read first when the build session starts?",
        "segment": "Write a Five-Artifact Software Design Document with Claude Code",
    },
    "solve-verify-asymmetry": {
        "title": "Demonstrate the Solve-Verify Asymmetry with Claude Code",
        "narration": "Your turn. Paste this: you've noticed Claude Code solves problems faster than you can verify the solution. Ask Claude to demonstrate the solve-verify asymmetry — run a problem, then run the same problem through a verification protocol — and show you how long each step takes and what the ratio implies for your workflow.",
        "command": "I've noticed Claude Code solves problems faster than I can verify the solutions. Demonstrate the solve-verify asymmetry for me: run a problem, then run the solution through a verification protocol — show me how long each step takes and what that ratio implies for how I should structure my verification workflow going forward.",
        "segment": "Demonstrate the Solve-Verify Asymmetry with Claude Code",
    },
    "spec-prompt-audit": {
        "title": "Build and Audit a Specification Prompt with Claude Code",
        "narration": "Your turn. Paste this: you want to audit an existing spec prompt for Claude Code to find what's ambiguous or missing. Ask Claude to run an audit on the spec you paste — flag every sentence that could be interpreted multiple ways, mark every missing rejection condition, and return a corrected spec.",
        "command": "I want to audit a spec prompt I've been using with Claude Code to find what's ambiguous or missing. Run an audit on the spec I paste: flag every sentence that could be interpreted more than one way, mark every missing rejection condition, and return a corrected version of the spec that closes the ambiguities.",
        "segment": "Build and Audit a Specification Prompt with Claude Code",
    },
    "spec-prompt-template": {
        "title": "Build a Specification Prompt Template for Student Assignments with Claude Code",
        "narration": "Your turn. Paste this: you want a specification prompt template your students can fill in for any Claude Code assignment. Ask Claude for the template — the seven fields every student spec needs — and explain what happens to the Claude Code session when a student leaves any field blank.",
        "command": "I want a specification prompt template my students can fill in for any Claude Code assignment. Give me the template: the seven fields every student spec needs to contain — and explain what happens to the Claude Code session when a student leaves any one of those fields blank or vague.",
        "segment": "Build a Specification Prompt Template for Student Assignments with Claude Code",
    },
    "spec-vs-prompt-live": {
        "title": "Spec vs. Prompt: Same Claude, Different Login",
        "narration": "Your turn. Paste this: you want to see the same task run as a prompt and then as a spec on the same Claude session. Ask Claude to take a task you describe, run it first as a casual prompt, then run it as a formal spec — and show you what changes in the output, the number of clarifying questions, and the session length.",
        "command": "I want to see the same task run as a prompt and then as a spec in the same Claude Code session. Take a task I describe, run it first as a casual prompt, then run it as a formal spec — and show me what changes in the output quality, the number of clarifying questions Claude asks, and the total session length.",
        "segment": "Spec vs. Prompt: Same Claude, Different Login",
    },
    "spec-writing-is-cs-ed": {
        "title": "Spec Writing IS CS Education: What Changes When AI Codes",
        "narration": "Your turn. Paste this: you want to teach spec writing as the core CS skill when AI does the coding. Ask Claude to explain what changes about CS education when AI writes code fluently — what cognitive work moves from 'writing code' to 'specifying what the code must do' — and how to redesign one programming assignment around spec writing instead of coding.",
        "command": "I want to teach spec writing as the core CS skill now that AI writes code fluently. Explain what changes about CS education when AI codes: what cognitive work moves from writing code to specifying what the code must do — and show me how to redesign one traditional programming assignment so spec writing is the graded skill.",
        "segment": "Spec Writing IS CS Education: What Changes When AI Codes",
    },
    "string-similarity-semantic-gap": {
        "title": "Why String Similarity Is Not Semantic Equivalence (and How to Catch the Difference Before You Ship)",
        "narration": "Your turn. Paste this: you have a string matching function that passes tests but returns wrong results on semantically equivalent inputs. Ask Claude to explain the string similarity versus semantic equivalence gap — what test cases expose the failure — and how to write the verification that catches this before deployment.",
        "command": "I have a string matching function that passes tests but returns wrong results on semantically equivalent inputs. Explain the string similarity versus semantic equivalence gap: what test cases expose this failure mode — and how do I write the verification protocol that catches semantic mismatches before the function ships?",
        "segment": "Why String Similarity Is Not Semantic Equivalence (and How to Catch the Difference Before You Ship)",
    },
    "tests-pass-user-fails": {
        "title": "Why the Build Passes Its Tests and Fails Its User",
        "narration": "Your turn. Paste this: your Claude Code build passed all automated tests but failed the first time a real user touched it. Ask Claude to explain the test-user gap — what automated tests cannot represent — and how to write a user-facing verification step that catches this class of failure before you hand off the build.",
        "command": "My Claude Code build passed all automated tests but failed the first time a real user touched it. Explain the test-user gap: what do automated tests fundamentally fail to represent — and how do I write a user-facing verification step that catches this class of failure before I hand off the build?",
        "segment": "Why the Build Passes Its Tests and Fails Its User",
    },
    "three-check-deployment": {
        "title": "Run the Three-Check Deployment Verification Protocol with Claude Code",
        "narration": "Your turn. Paste this: you're about to deploy a Claude Code build and you want to run the three-check protocol before it goes live. Ask Claude to walk you through the three checks — what each one verifies, in what order to run them, and what a fail on check two means for whether you proceed.",
        "command": "I'm about to deploy a Claude Code build and I want to run the three-check verification protocol before it goes live. Walk me through the three checks: what does each one verify, in what order do I run them, and what does a failure on check two mean for whether I should proceed with the deployment?",
        "segment": "Run the Three-Check Deployment Verification Protocol with Claude Code",
    },
    "three-file-system-simulator": {
        "title": "Build a Simulation with the Three-File System with Claude Code",
        "narration": "Your turn. Paste this: you want to build a simulation using the three-file system — CLAUDE.md, spec, test plan — before Claude touches a single line of code. Ask Claude to walk you through building the three files for a simulation you describe, and explain what the simulation would fail to do if any file is incomplete.",
        "command": "I want to build a simulation using the three-file system with Claude Code: CLAUDE.md, spec, and test plan written before Claude touches any code. Walk me through building the three files for a simulation I describe — and explain what the simulation would fail to do correctly if any one of the three files is left incomplete.",
        "segment": "Build a Simulation with the Three-File System with Claude Code",
    },
    "three-pass-verification": {
        "title": "Run the Three-Pass Verification Protocol with Claude Code",
        "narration": "Your turn. Paste this: you want to run a three-pass verification protocol on a Claude Code build before you sign off on it. Ask Claude to walk you through what each pass checks, why the order matters, and what you write in the post-build document after each pass — pass or fail.",
        "command": "I want to run a three-pass verification protocol on a Claude Code build before I sign off on it. Walk me through what each pass checks, why the order of the three passes matters, and what I write in the post-build document after each pass — whether it passes or fails.",
        "segment": "Run the Three-Pass Verification Protocol with Claude Code",
    },
    "vox-agentic-loop": {
        "title": "Why the Agentic Loop Can Delete Your Files Before You Finish Reading the Plan",
        "narration": "Your turn. Paste this: you want to understand how an agentic Claude Code session can act before you've finished reviewing the plan. Ask Claude to explain the read-execute gap — why approval of the plan doesn't gate each tool call — and what the safeguard pattern looks like for a session that touches production files.",
        "command": "I want to understand how an agentic Claude Code session can act before I finish reviewing the plan. Explain the read-execute gap: why doesn't my approval of the plan gate each individual tool call — and what does the safeguard pattern look like for a session that has write access to production files?",
        "segment": "Why the Agentic Loop Can Delete Your Files Before You Finish Reading the Plan",
    },
    "vox-ai-feedback-bias": {
        "title": "Why AI Feedback That Passes Every Check Can Still Harm Your Students",
        "narration": "Your turn. Paste this: you're using Claude to generate student feedback and it passes every rubric check but you're worried it's causing harm. Ask Claude to explain the feedback bias that passes rubrics — what systemic pattern in AI feedback teaches the wrong thing even when every individual comment is technically correct.",
        "command": "I'm using Claude to generate student feedback and it passes every rubric check, but I'm worried it's causing harm. Explain the feedback bias that passes rubrics: what systemic pattern in AI-generated feedback teaches the wrong thing even when every individual comment is technically correct?",
        "segment": "Why AI Feedback That Passes Every Check Can Still Harm Your Students",
    },
    "vox-buildlog-assessment": {
        "title": "Why Your Students' CLAUDE.md Is the Best Evidence They Conducted the Build",
        "narration": "Your turn. Paste this: you want to use students' CLAUDE.md files as evidence of conducted build sessions rather than relying on submitted code alone. Ask Claude to explain what a CLAUDE.md file reveals about how the student ran the session — and design a rubric that grades the CLAUDE.md as a build log.",
        "command": "I want to use students' CLAUDE.md files as evidence that they conducted a real build session, not just submitted generated code. Explain what a CLAUDE.md file reveals about how the student ran the session — and design a rubric that grades the CLAUDE.md as a build log, not just as configuration.",
        "segment": "Why Your Students' CLAUDE.md Is the Best Evidence They Conducted the Build",
    },
    "vox-claudemd-length": {
        "title": "Why CLAUDE.md Breaks When It Gets Too Long",
        "narration": "Your turn. Paste this: your CLAUDE.md is long and Claude isn't following some of the rules in it. Ask Claude to explain the length failure mode — what happens to rule adherence as CLAUDE.md grows — and give you the rule for what to cut, what to keep, and how short is short enough.",
        "command": "My CLAUDE.md is long and Claude is no longer following some of the rules in it. Explain the length failure mode: what happens to rule adherence as CLAUDE.md grows — and give me the rule for what to cut, what to keep, and how short the file needs to be for Claude to reliably follow every rule.",
        "segment": "Why CLAUDE.md Breaks When It Gets Too Long",
    },
    "vox-code-oracle": {
        "title": "Why Code That Looks Correct Can Still Be Wrong",
        "narration": "Your turn. Paste this: you have code that looks correct to every reviewer but behaves wrong at runtime. Ask Claude to explain the oracle problem — why static review cannot catch the category of bug that requires execution to surface — and what the minimum verification step is that catches it.",
        "command": "I have code that looks correct to every reviewer but behaves wrong at runtime. Explain the oracle problem: why can't static review catch the category of bug that requires execution to surface — and what is the minimum verification step that catches this class of error before it reaches production?",
        "segment": "Why Code That Looks Correct Can Still Be Wrong",
    },
    "vox-handoff-conditions": {
        "title": "Why 'Looks Good' Fails as a Gate and What to Write Instead",
        "narration": "Your turn. Paste this: your Claude Code handoff condition says 'looks good' and it keeps passing broken work. Ask Claude to show you what 'looks good' actually communicates to the model — and rewrite it as a testable handoff condition that catches the specific failure you keep seeing.",
        "command": "My Claude Code handoff condition says 'looks good' and it keeps passing broken work. Show me what 'looks good' actually communicates to Claude — and rewrite it as a testable handoff condition that catches the specific failure mode I describe so the gate can no longer be passed by a fluent but broken output.",
        "segment": "Why 'Looks Good' Fails as a Gate and What to Write Instead",
    },
    "vox-hook-enforcement": {
        "title": "Why 'Never Generate a Grade' Fails Until You Write a Hook",
        "narration": "Your turn. Paste this: you wrote 'never generate a grade' in your CLAUDE.md but Claude still generates grades sometimes. Ask Claude to explain why advisory instructions in CLAUDE.md fail under pressure — and show you the hook implementation that enforces the rule deterministically so it cannot be overridden.",
        "command": "I wrote 'never generate a grade' in my CLAUDE.md but Claude still generates grades in certain situations. Explain why an advisory instruction in CLAUDE.md fails under pressure — and show me the hook implementation that enforces the rule deterministically so it cannot be overridden by a rephrased request.",
        "segment": "Why 'Never Generate a Grade' Fails Until You Write a Hook",
    },
    "vox-rewind-respec": {
        "title": "Why Rewriting the Wrong Fix Makes the Build Worse, Not Better",
        "narration": "Your turn. Paste this: your Claude Code session went wrong and you're tempted to fix it by rewriting the broken section. Ask Claude to explain the fix-forward failure — why each iteration of fixing the wrong thing compounds the debt — and when rewinding to the last known-good checkpoint and rewriting the spec is the only correct move.",
        "command": "My Claude Code session went wrong and I'm tempted to fix it by rewriting the broken section iteratively. Explain the fix-forward failure: why does each iteration of fixing the wrong thing compound the technical debt — and how do I identify the point where rewinding to the last known-good checkpoint and rewriting the spec is the only correct move?",
        "segment": "Why Rewriting the Wrong Fix Makes the Build Worse, Not Better",
    },
    "vox-simulation-ownership": {
        "title": "Why the Simulation That Took 8 Minutes to Generate Wasn't Theirs",
        "narration": "Your turn. Paste this: your students generated a simulation in eight minutes and submitted it, but you're not sure they understand what it does. Ask Claude to explain the generation-ownership gap — what cognitive work the student skips when AI generates the artifact — and design an activity that proves the student owns the simulation, not just the output.",
        "command": "My students generated a simulation in eight minutes and submitted it, but I'm not sure they understand what it does. Explain the generation-ownership gap: what cognitive work does the student skip when AI generates the artifact — and design an activity that proves the student owns the simulation and not just the generated output.",
        "segment": "Why the Simulation That Took 8 Minutes to Generate Wasn't Theirs",
    },
    "vox-spec-saves-time": {
        "title": "Why the 90-Second Request Takes 12 Minutes and the 8-Second Request Takes 45",
        "narration": "Your turn. Paste this: you've noticed that quick requests to Claude Code consistently take longer than deliberate requests. Ask Claude to explain the spec-time paradox — why the time you invest in a specification is always less than the time Claude wastes on an ambiguous request — and show you the calculation for a real task.",
        "command": "I've noticed that quick requests to Claude Code consistently take longer to resolve than deliberate well-specified requests. Explain the spec-time paradox: why is the time I invest in writing a specification always less than the time Claude wastes on an ambiguous request — and show me the calculation for a real task where the paradox is most visible.",
        "segment": "Why the 90-Second Request Takes 12 Minutes and the 8-Second Request Takes 45",
    },
    "vox-subagent-context": {
        "title": "Why One Subagent Query Saved 48% of the Context Window",
        "narration": "Your turn. Paste this: you want to understand why using a subagent with isolated context is more efficient than one large session. Ask Claude to explain the subagent context isolation benefit — why giving each subagent its own clean window saves more context than it costs — and show you the prompt structure that implements it.",
        "command": "I want to understand why using a Claude Code subagent with isolated context is more efficient than running everything in one session. Explain the subagent context isolation benefit: why does giving each subagent its own clean window save more context than it costs — and show me the prompt structure that implements subagent context isolation correctly.",
        "segment": "Why One Subagent Query Saved 48% of the Context Window",
    },
    "writer-reviewer-pattern": {
        "title": "Writer/Reviewer: Same Model, Clean Context",
        "narration": "Your turn. Paste this: you want to run a writer/reviewer pattern where two Claude instances review the same code with clean context. Ask Claude to set up the writer/reviewer split — what the writer session produces, what the reviewer session receives, and why the clean context makes the review more reliable than a single session.",
        "command": "I want to run a writer/reviewer pattern where Claude writes code in one context and reviews it in a clean second context. Set up the writer/reviewer split: what does the writer session produce, what exactly does the reviewer session receive, and why does the clean context in the reviewer session make the review more reliable than reviewing in the same session that wrote the code?",
        "segment": "Writer/Reviewer: Same Model, Clean Context",
    },
    "writing-rules": {
        "title": "Writing Hookify Rules",
        "narration": "Your turn. Paste this: you want to write Hookify rules that are specific enough for Claude Code to enforce deterministically. Ask Claude for the rule-writing pattern — what a Hookify rule must specify, what a vague rule looks like versus a precise one, and how to test that the rule fires correctly.",
        "command": "I want to write Hookify rules that Claude Code can enforce deterministically. Give me the rule-writing pattern: what must a Hookify rule specify to be enforceable, show me a vague rule versus a precise one for the same behavior, and tell me how to test that the rule fires correctly without triggering it on false positives.",
        "segment": "Writing Hookify Rules",
    },
    "claudes-c-compiler": {
        "title": "Claude Wrote a C Compiler",
        "narration": "Your turn. Paste this: you want to understand what it means for Claude to write a C compiler — what the limits of that build are. Ask Claude to walk you through the architecture of a Claude-generated compiler, where the generated code is reliable, and what the human must verify before the compiler handles untrusted input.",
        "command": "I want to understand what it means for Claude to write a C compiler and where the limits of that build are. Walk me through the architecture of a Claude-generated compiler: where is the generated code reliable, where does it require human verification, and what must I check before the compiler handles untrusted input?",
        "segment": "Claude Wrote a C Compiler",
    },
    "claudes-c-compiler-assembly-shrinks-through-13-sequential": {
        "title": "Why assembly shrinks through 13 sequential filters, not one",
        "narration": "Your turn. Paste this: you're trying to understand why a compiler optimization pass uses 13 sequential filters instead of one combined filter. Ask Claude to explain the sequential filter design — why composing thirteen small passes is more reliable and debuggable than one combined optimization — and what breaks if you merge two of the thirteen.",
        "command": "I'm trying to understand why a compiler optimization uses 13 sequential filters instead of one combined pass. Explain the sequential filter design: why is composing thirteen small passes more reliable and debuggable than one combined optimization — and what breaks or becomes harder to debug if you merge any two of the thirteen filters?",
        "segment": "Why assembly shrinks through 13 sequential filters, not one",
    },
}

fixed = 0

for base_slug, patch in PATCHES.items():
    for slug in [base_slug, f"claude-liam-{base_slug}"]:
        path = os.path.join(BASE, slug, "beat_sheet.json")
        if not os.path.exists(path):
            continue
        bak = path + ".bak-code-v1"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        with open(path) as f:
            d = json.load(f)
        meta = d.get("metadata", {})
        fix_voice(meta)
        beats = d.get("beats", d.get("scenes", []))
        strip_all_sublines(beats)
        fix_genai_ban(beats)
        ensure_outro(beats, patch["title"], slug)
        ensure_yourturn(beats, patch["narration"], patch["command"], patch["segment"])
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed += 1
        print(f"FIXED: {slug}")

print(f"\nDone. {fixed} files fixed.")
