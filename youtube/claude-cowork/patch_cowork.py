#!/usr/bin/env python3
"""Fix claude-cowork: VOICE-LOCK + OUTRO + YOURTURN + Gen-AI ban across all reels."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_bid(b):
    return b.get("beat_id", b.get("id", ""))

def fix_voice(meta):
    meta.pop("voice_id", None)
    if not meta.get("engine"):
        meta["engine"] = "kokoro"
    if not meta.get("voice"):
        meta["voice"] = "am_onyx"
    if not meta.get("voice_kokoro"):
        meta["voice_kokoro"] = "am_onyx"

def strip_all_sublines(beats):
    for b in beats:
        props = b.get("props")
        if isinstance(props, dict):
            props.pop("subline", None)
        shot = b.get("shot")
        if isinstance(shot, dict):
            rem = shot.get("remotion")
            if isinstance(rem, dict):
                rem.get("props", {}).pop("subline", None)
        rem = b.get("remotion")
        if isinstance(rem, dict):
            rem.get("props", {}).pop("subline", None)

def fix_genai_ban(beats):
    for b in beats:
        shot = b.get("shot", {})
        if isinstance(shot, dict) and shot.get("source") == "ai" and shot.get("motion") == "kenburns":
            shot["source"] = "own"
            shot.pop("motion", None)

def is_placeholder(text):
    if not text:
        return True
    t = text.strip()
    return t in ("", "Your turn.", "[seed]") or "[Your turn" in t

def ensure_outro(beats, title, slug):
    for b in beats:
        if get_bid(b) in ("OUTRO", "O01", "BOUT"):
            shot = b.setdefault("shot", {})
            shot["type"] = "REMOTION"
            shot["source"] = "own"
            remotion = shot.setdefault("remotion", {})
            remotion["pattern"] = "ClaudeTitleOutro"
            props = remotion.setdefault("props", {})
            props["title"] = title
            props["handle"] = "@NikBearBrown"
            props["mascotSeed"] = slug
            props.pop("subline", None)
            rem = b.get("remotion")
            if isinstance(rem, dict):
                rem.get("props", {}).pop("subline", None)
            return True
    beats.append({
        "beat_id": "OUTRO",
        "act": "CLOSE",
        "lane": "REMOTION",
        "scene": "ClaudeTitleOutro",
        "narration_text": f"{title}.",
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {"title": title, "handle": "@NikBearBrown", "mascotSeed": slug}
            }
        },
        "est_s": 8,
        "build": {"status": "SLATE", "note": "design-v1: remotion props added"}
    })
    return True

def ensure_yourturn(beats, narration, command, segment, topic="CLAUDE COWORK · @NikBearBrown"):
    for b in beats:
        bid = get_bid(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        if bid == "YOURTURN" or scene == "ClaudeComposerAsk" or act in ("handoff", "your-turn"):
            if "ClaudeTitleOutro" in str(b):
                continue
            existing = b.get("narration_text") or b.get("narration") or ""
            shot = b.setdefault("shot", {})
            if "remotion" in b and "remotion" not in shot:
                shot["remotion"] = b.pop("remotion")
            shot.setdefault("type", "REMOTION")
            remotion = shot.setdefault("remotion", {})
            remotion.setdefault("pattern", "ClaudeComposerAsk")
            props = remotion.setdefault("props", {})
            props.setdefault("greeting", "Your turn.")
            props.setdefault("topic", topic)
            props.setdefault("folderLabel", "@NikBearBrown")
            props.setdefault("modelLabel", "Claude Sonnet")
            props.setdefault("runningText", "paste your task, workflow, or brief here…")
            if not is_placeholder(existing):
                props.setdefault("command", command)
                props.setdefault("segment", segment)
                return True
            if "narration_text" in b:
                b["narration_text"] = narration
            else:
                b["narration"] = narration
            props["command"] = command
            props["segment"] = segment
            return True
    yt_beat = {
        "beat_id": "YOURTURN",
        "act": "CLOSE",
        "lane": "REMOTION",
        "scene": "ClaudeComposerAsk",
        "narration_text": narration,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "command": command,
                    "segment": segment,
                    "topic": topic,
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Claude Sonnet",
                    "runningText": "paste your task, workflow, or brief here…"
                }
            }
        },
        "est_s": 14
    }
    outro_idx = next((i for i, b in enumerate(beats) if get_bid(b) in ("OUTRO","O01","BOUT")), None)
    if outro_idx is not None:
        beats.insert(outro_idx, yt_beat)
    else:
        beats.append(yt_beat)
    return True

# ── PATCHES ──────────────────────────────────────────────────────────────────
# slug → {title, narration, command, segment}
# Bare slugs and their claude-liam-* counterparts share the same command.
# ─────────────────────────────────────────────────────────────────────────────
PATCHES = {
    "access-ladder-explained": {
        "title": "The Access Ladder: Scope Is a Security Decision",
        "narration": "Your turn. Paste this: you're designing a Claude workflow and you need to decide which steps Claude executes autonomously versus which need human approval. Ask Claude to show you the access ladder — the four rungs from read-only to full execution — and the rule for choosing the lowest rung that still accomplishes the task.",
        "command": "I'm designing a Claude workflow and I need to decide which steps Claude executes autonomously versus which need human approval. Show me the access ladder: the four rungs from read-only to full execution, the rule for choosing the lowest rung that still accomplishes the task, and an example of how a file-management workflow maps to each rung.",
        "segment": "The Access Ladder: Scope Is a Security Decision",
    },
    "ai-use-log": {
        "title": "Build the AI-Use Log Habit with Claude",
        "narration": "Your turn. Paste this: you want to start logging how you use Claude — what tasks, what prompts, what outcomes — so you can improve over time. Ask Claude to show you the AI-use log format: the five fields every entry needs, how to maintain it without it becoming a burden, and what patterns to look for after a month of consistent logging.",
        "command": "I want to start logging how I use Claude — what tasks, what prompts, what outcomes — so I can improve over time. Show me the AI-use log format: the five fields every entry needs, how to maintain it without it becoming a burden, and what patterns to look for after a month of consistent logging.",
        "segment": "Build the AI-Use Log Habit with Claude",
    },
    "claude-liam-access-ladder-explained": {
        "title": "The Access Ladder: Scope Is a Security Decision",
        "narration": "Your turn. Paste this: you're designing a Claude workflow and you need to decide which steps Claude executes autonomously versus which need human approval. Ask Claude to show you the access ladder — the four rungs from read-only to full execution — and the rule for choosing the lowest rung that still accomplishes the task.",
        "command": "I'm designing a Claude workflow and I need to decide which steps Claude executes autonomously versus which need human approval. Show me the access ladder: the four rungs from read-only to full execution, the rule for choosing the lowest rung that still accomplishes the task, and an example of how a file-management workflow maps to each rung.",
        "segment": "The Access Ladder: Scope Is a Security Decision",
    },
    "claude-liam-ai-use-log": {
        "title": "Build the AI-Use Log Habit with Claude",
        "narration": "Your turn. Paste this: you want to start logging how you use Claude — what tasks, what prompts, what outcomes — so you can improve over time. Ask Claude to show you the AI-use log format: the five fields every entry needs, how to maintain it without it becoming a burden, and what patterns to look for after a month of consistent logging.",
        "command": "I want to start logging how I use Claude — what tasks, what prompts, what outcomes — so I can improve over time. Show me the AI-use log format: the five fields every entry needs, how to maintain it without it becoming a burden, and what patterns to look for after a month of consistent logging.",
        "segment": "Build the AI-Use Log Habit with Claude",
    },
    "claude-liam-be-good-at-claude": {
        "title": "Six Levels",
        "narration": "Your turn. Paste this: you want to understand what it actually means to get good at Claude — beyond just writing better prompts. Ask Claude to walk you through the six levels of Claude proficiency: what changes at each level, which level is the most common plateau, and what the jump from level three to level four actually requires.",
        "command": "I want to understand what it actually means to get good at Claude — beyond just writing better prompts. Walk me through the six levels of Claude proficiency: what changes at each level, which level is the most common plateau, and what the jump from level three to level four actually requires in terms of workflow change.",
        "segment": "Six Levels",
    },
    "claude-liam-chatgpt-vs-claude": {
        "title": "Everything Else on Claude",
        "narration": "Your turn. Paste this: you use both Claude and ChatGPT and you want to know what Claude actually does better — not the marketing answer, the workflow answer. Ask Claude to show you three task types where Claude's context window, instruction-following, or character consistency makes a real difference to output quality.",
        "command": "I use both Claude and ChatGPT and I want to know what Claude actually does better — not the marketing answer, the workflow answer. Show me three task types where Claude's context window, instruction-following, or character consistency makes a real difference to output quality, with a concrete before-and-after example for each.",
        "segment": "Everything Else on Claude",
    },
    "claude-liam-claude-101": {
        "title": "Claude, Oversimplified",
        "narration": "Your turn. Paste this: you're explaining Claude to someone who has never used it. Ask Claude to give you the oversimplified version — not what it can do (too long), but the one mental model that predicts when Claude will work well versus when it won't, and one concrete example that shows the model in action.",
        "command": "I'm explaining Claude to someone who has never used it. Give me the oversimplified version: not what Claude can do (too long), but the one mental model that predicts when Claude will work well versus when it won't, and one concrete example — a task Claude handles well and a task that looks similar but fails — that shows the model in action.",
        "segment": "Claude, Oversimplified",
    },
    "claude-liam-claude-code": {
        "title": "Vibecoders Welcome",
        "narration": "Your turn. Paste this: you want to use Claude Code but you're not a professional developer — you write code occasionally and mostly by feel. Ask Claude to show you the three Claude Code habits that matter most for non-professionals: how to scope a session, how to know when to stop and verify, and what to do when the code looks right but you're not sure.",
        "command": "I want to use Claude Code but I'm not a professional developer — I write code occasionally and mostly by feel. Show me the three Claude Code habits that matter most for non-professionals: how to scope a session to something Claude can finish in one run, how to know when to stop and verify, and what to do when the code looks right but I'm not sure it's correct.",
        "segment": "Vibecoders Welcome",
    },
    "claude-liam-claude-connectors": {
        "title": "Don't Leave Them All On",
        "narration": "Your turn. Paste this: you have multiple Claude connectors enabled and you're not sure which ones are actually helping versus which are expanding Claude's access unnecessarily. Ask Claude to show you the connector audit: how to identify which connectors your workflow actually uses, which ones expand access without benefit, and the rule for which ones to turn off.",
        "command": "I have multiple Claude connectors enabled and I'm not sure which ones are actually helping versus which are expanding Claude's access unnecessarily. Show me the connector audit: how to identify which connectors my current workflow actually uses, which ones expand access without benefit, and the rule for deciding which ones to turn off.",
        "segment": "Don't Leave Them All On",
    },
    "claude-liam-claude-cowork": {
        "title": "Forget Files and Folders",
        "narration": "Your turn. Paste this: you're used to organizing work in files and folders and you want to understand how Claude Cowork changes the mental model. Ask Claude to explain what replaces files and folders in a Claude Cowork workflow — what the unit of work is, where state lives between sessions, and what you stop doing when you work in Cowork.",
        "command": "I'm used to organizing work in files and folders and I want to understand how Claude Cowork changes the mental model. Explain what replaces files and folders in a Claude Cowork workflow: what the unit of work is, where state lives between sessions, and what I stop doing when I work in Cowork instead of a traditional file system.",
        "segment": "Forget Files and Folders",
    },
    "claude-liam-claude-design": {
        "title": "Taste Is All You Need",
        "narration": "Your turn. Paste this: you're using Claude to generate design assets and you're getting technically correct but aesthetically wrong output. Ask Claude to show you the taste-transfer method: how to describe your aesthetic preferences in a way Claude can operationalize, what reference examples to include, and how to give feedback on a design that lands without a design vocabulary.",
        "command": "I'm using Claude to generate design assets and I'm getting technically correct but aesthetically wrong output — it looks like a template, not my taste. Show me the taste-transfer method: how to describe my aesthetic preferences in a way Claude can operationalize, what reference examples to include, and how to give feedback on a design that lands without a professional design vocabulary.",
        "segment": "Taste Is All You Need",
    },
    "claude-liam-claude-fable-5": {
        "title": "Don't Use Fable 5 Broke",
        "narration": "Your turn. Paste this: you're using Claude with Fable 5 and something in your workflow broke after the update. Ask Claude to help you diagnose whether the breakage is a schema change, a behavior change, or a dependency issue — and show you the isolation test that tells you which it is without rewriting your whole workflow.",
        "command": "I'm using Claude with Fable 5 and something in my workflow broke after the update. Help me diagnose whether the breakage is a schema change, a behavior change, or a dependency issue — and show me the isolation test that tells me which one it is without having to rewrite the whole workflow to find out.",
        "segment": "Don't Use Fable 5 Broke",
    },
    "claude-liam-claude-for-excel": {
        "title": "Spreadsheets on Demand",
        "narration": "Your turn. Paste this: you want to use Claude to work with spreadsheet data without copying and pasting every cell. Ask Claude to show you the three patterns for spreadsheet work: how to describe what you need in terms Claude can execute, how to structure the output so it pastes cleanly into Excel or Sheets, and what to do when the formula Claude gives you doesn't work in your version.",
        "command": "I want to use Claude to work with spreadsheet data without copying and pasting every cell. Show me the three patterns for spreadsheet work: how to describe what I need in terms Claude can execute, how to structure the output so it pastes cleanly into Excel or Sheets, and what to do when the formula Claude gives me doesn't work in my version.",
        "segment": "Spreadsheets on Demand",
    },
    "claude-liam-claude-for-your-team": {
        "title": "Manufacture the Wow Moment",
        "narration": "Your turn. Paste this: you want to introduce Claude to your team and you need one demonstration that actually changes how they think about it — not a capabilities list, a wow moment. Ask Claude to help you design the demonstration: what task to pick, how to set it up so the output is immediately useful, and how to run it live without it going wrong.",
        "command": "I want to introduce Claude to my team and I need one demonstration that actually changes how they think about it — not a capabilities list, a concrete wow moment. Help me design the demonstration: what task to pick that will resonate with this team, how to set it up so the output is immediately useful rather than theoretical, and how to run it live without the demo going wrong.",
        "segment": "Manufacture the Wow Moment",
    },
    "claude-liam-claude-linkedin": {
        "title": "Train Claude on Your Best Posts",
        "narration": "Your turn. Paste this: you want Claude to write LinkedIn content in your voice, not its generic professional voice. Ask Claude to show you the voice-capture method: how many of your own posts to include as examples, what to annotate in them so Claude extracts your patterns rather than your topics, and how to test whether Claude's output actually sounds like you.",
        "command": "I want Claude to write LinkedIn content in my voice, not its generic professional voice. Show me the voice-capture method: how many of my own posts to include as examples, what to annotate in them so Claude extracts my patterns rather than just my topics, and how to test whether Claude's output actually sounds like me or just like a polished version of the platform default.",
        "segment": "Train Claude on Your Best Posts",
    },
    "claude-liam-claude-skills": {
        "title": "One Prompt. Every Time.",
        "narration": "Your turn. Paste this: you want to build a Claude skill — a reusable prompt that produces the same type of output every time you need it. Ask Claude to show you the skill anatomy: the three elements that make a prompt reusable rather than one-off, how to test the skill against edge cases, and where to store it so it's available every session.",
        "command": "I want to build a Claude skill — a reusable prompt that produces the same type of output every time I need it. Show me the skill anatomy: the three elements that make a prompt reusable rather than one-off, how to test the skill against edge cases before relying on it, and where to store it so it's available in every session without re-pasting.",
        "segment": "One Prompt. Every Time.",
    },
    "claude-liam-claude-to-sound-like-you": {
        "title": "You're Just a Text File",
        "narration": "Your turn. Paste this: you want Claude to write in your voice across all your work — not just one task. Ask Claude to show you the voice file approach: how to build a text file that captures your tone, register, and style patterns, how to include it in a prompt without inflating the context, and how to update it when your voice evolves.",
        "command": "I want Claude to write in my voice across all my work — not just one task. Show me the voice file approach: how to build a text file that captures my tone, register, and style patterns, how to include it in a prompt without inflating the context window unnecessarily, and how to update it when my voice evolves over time.",
        "segment": "You're Just a Text File",
    },
    "claude-liam-cowork-access-ladder": {
        "title": "The Cowork Access Ladder: Lowest Rung That Works",
        "narration": "Your turn. Paste this: you're setting up a Claude Cowork workflow and you need to decide what level of access to grant for each step. Ask Claude to show you the cowork access ladder — what each rung allows, the principle of lowest rung that works, and how to map your specific workflow tasks to the right rung before enabling anything.",
        "command": "I'm setting up a Claude Cowork workflow and I need to decide what level of access to grant for each step. Show me the cowork access ladder: what each rung allows, the principle of the lowest rung that works, and how to map my workflow tasks to the right rung before enabling access — including one example where choosing a higher rung than needed causes a real problem.",
        "segment": "The Cowork Access Ladder: Lowest Rung That Works",
    },
    "claude-liam-cowork-task-packet": {
        "title": "The Cowork Task Packet: Five Fields, One Scope",
        "narration": "Your turn. Paste this: you want to build a Claude Cowork task packet — a structured brief that gives Claude exactly what it needs to complete a task without scope creep. Ask Claude to show you the five fields, what goes in each one, and how the packet prevents the two most common failure modes: Claude doing too much or doing the wrong thing.",
        "command": "I want to build a Claude Cowork task packet — a structured brief that gives Claude exactly what it needs to complete a task without scope creep. Show me the five fields, what goes in each one, and how the packet prevents the two most common failure modes: Claude expanding scope beyond the task and Claude completing the wrong task confidently.",
        "segment": "The Cowork Task Packet: Five Fields, One Scope",
    },
    "claude-liam-cowork-task-packet-audit": {
        "title": "Audit a Claude Cowork Task Packet in Sixty Seconds",
        "narration": "Your turn. Paste this: you have a task packet and you want to audit it before handing it to Claude. Ask Claude to run the sixty-second audit: the three questions that reveal whether the scope is tight, whether the success condition is measurable, and whether Claude has everything it needs to complete the task without asking you for more.",
        "command": "I have a task packet and I want to audit it before handing it to Claude. Run the sixty-second audit: the three questions that reveal whether the scope is tight, whether the success condition is measurable, and whether Claude has everything it needs to complete the task without asking me for more context mid-task.",
        "segment": "Audit a Claude Cowork Task Packet in Sixty Seconds",
    },
    "claude-liam-data": {
        "title": "Claude, By the Numbers",
        "narration": "Your turn. Paste this: you want to use Claude to analyze data — not just describe it. Ask Claude to show you the three data analysis patterns that produce insight rather than summary: how to frame a question as a hypothesis rather than a request, how to specify what a useful answer looks like, and how to verify the analysis isn't just restating the input.",
        "command": "I want to use Claude to analyze data — not just describe it. Show me the three data analysis patterns that produce insight rather than summary: how to frame a question as a hypothesis rather than a request for description, how to specify what a useful answer looks like, and how to verify the analysis isn't just restating what the data already shows.",
        "segment": "Claude, By the Numbers",
    },
    "claude-liam-enterprise-search": {
        "title": "Claude, Finding It",
        "narration": "Your turn. Paste this: you want Claude to find something specific across a large body of documents — not just keyword search, actual retrieval. Ask Claude to show you the enterprise search prompt pattern: how to describe what you're looking for in terms of content rather than keywords, how to scope the search space, and how to handle the case where the answer is across multiple documents.",
        "command": "I want Claude to find something specific across a large body of documents — not just keyword search, actual retrieval of the right piece of information. Show me the enterprise search prompt pattern: how to describe what I'm looking for in terms of content rather than keywords, how to scope the search space, and how to handle the case where the answer is distributed across multiple documents.",
        "segment": "Claude, Finding It",
    },
    "claude-liam-extraction-schema-first": {
        "title": "Extraction Schema First: Structure Confers Credibility",
        "narration": "Your turn. Paste this: you want Claude to extract structured data from unstructured text — receipts, reports, emails — and you're getting inconsistent output. Ask Claude to show you the schema-first extraction pattern: how defining the output schema before the extraction prompt changes what Claude produces, and why schema-first extraction is more reliable than asking Claude to find the fields.",
        "command": "I want Claude to extract structured data from unstructured text — receipts, reports, emails — and I'm getting inconsistent output. Show me the schema-first extraction pattern: how defining the output schema before the extraction prompt changes what Claude produces, why structure-first is more reliable than asking Claude to find the fields, and how to write the schema so Claude fills it rather than inventing around it.",
        "segment": "Extraction Schema First: Structure Confers Credibility",
    },
    "claude-liam-file-rename-dry-run": {
        "title": "Build a File-Rename Dry-Run Tool with Claude",
        "narration": "Your turn. Paste this: you want to build a file-rename tool with Claude that shows you exactly what it will do before it does anything. Ask Claude to show you the dry-run architecture: how the tool generates a rename plan without executing it, how you review and approve the plan, and what the hook looks like that blocks execution until the plan is confirmed.",
        "command": "I want to build a file-rename tool with Claude that shows me exactly what it will do before it does anything. Show me the dry-run architecture: how the tool generates a rename plan without executing it, how I review and approve the plan, and what the hook looks like that blocks execution until the plan is explicitly confirmed — so the tool structurally cannot rename before review.",
        "segment": "Build a File-Rename Dry-Run Tool with Claude",
    },
    "claude-liam-five-claudes-explained": {
        "title": "Five Products. One Name.",
        "narration": "Your turn. Paste this: you keep seeing 'Claude' on different products and surfaces — Claude.ai, Claude API, Claude Code, Claude in Slack — and you want to understand what's actually different between them. Ask Claude to explain the five Claude products: what each one is for, what you can do in one that you can't do in another, and how to know which one you're actually using.",
        "command": "I keep seeing 'Claude' on different products and surfaces — Claude.ai, the API, Claude Code, Claude in enterprise apps — and I want to understand what's actually different between them. Explain the five Claude products: what each one is for, what I can do in one that I can't do in another, and how to know which one I'm actually using so I'm choosing the right tool for the task.",
        "segment": "Five Products. One Name.",
    },
    "claude-liam-how-to-prompt": {
        "title": "Seven Things That Changed",
        "narration": "Your turn. Paste this: you've been prompting Claude for a while and you feel like you're doing it wrong — getting inconsistent results, fighting with it, rewriting the same things. Ask Claude to show you the seven prompt behaviors that most commonly changed between when people learned prompting and now, and which of the seven is most likely responsible for inconsistent outputs.",
        "command": "I've been prompting Claude for a while and I feel like I'm doing it wrong — getting inconsistent results, fighting it, rewriting the same prompt three times. Show me the seven prompt behaviors that most commonly changed between when people first learned prompting and what works now, and which of the seven is most likely responsible for inconsistent outputs in a long-running workflow.",
        "segment": "Seven Things That Changed",
    },
    "claude-liam-human-approval-gates": {
        "title": "Design Human Approval Gates for a Multi-Step Agentic Workflow with Claude",
        "narration": "Your turn. Paste this: you're building a multi-step agentic workflow and you need to decide where to put human approval gates — not everywhere (too slow), but at the right steps. Ask Claude to show you the gate-placement framework: the three properties that make a step require a gate versus run autonomously, and how to build the gate so Claude presents what it's about to do in a way you can actually review in thirty seconds.",
        "command": "I'm building a multi-step agentic workflow and I need to decide where to put human approval gates — not everywhere, but at the right steps. Show me the gate-placement framework: the three properties that make a step require a gate versus run autonomously, and how to build the gate so Claude presents what it's about to do in a format I can review and approve in thirty seconds without reading a wall of text.",
        "segment": "Design Human Approval Gates for a Multi-Step Agentic Workflow with Claude",
    },
    "claude-liam-legal-finance": {
        "title": "Claude, Counsel",
        "narration": "Your turn. Paste this: you want to use Claude to help with legal and financial documents — reading contracts, flagging risks, summarizing terms — but you're worried about getting confident wrong answers. Ask Claude to show you the legal-finance prompt pattern: the three guardrails that keep Claude in a reviewer role rather than an advisor role, and what you should always verify with a human expert even when Claude's answer looks right.",
        "command": "I want to use Claude to help with legal and financial documents — reading contracts, flagging risks, summarizing terms — but I'm worried about getting confident wrong answers. Show me the legal-finance prompt pattern: the three guardrails that keep Claude in a reviewer role rather than an advisor role, and what I should always verify with a human expert even when Claude's answer looks complete and correct.",
        "segment": "Claude, Counsel",
    },
    "claude-liam-map-the-agentic-loop": {
        "title": "Map the Agentic Loop: Observe - Plan - Act - Check - Report with Claude",
        "narration": "Your turn. Paste this: you're building an agentic Claude workflow and you want to map every step to the observe-plan-act-check-report loop so you know exactly where human oversight belongs. Ask Claude to walk you through a concrete workflow — say, a document review pipeline — and label each step with its loop phase, the failure mode if that phase is skipped, and where the human gate should sit.",
        "command": "I'm building an agentic Claude workflow and I want to map every step to the observe-plan-act-check-report loop so I know where human oversight belongs. Walk me through a concrete workflow — a document review pipeline — and label each step with its loop phase, the failure mode if that phase is skipped, and where the human gate should sit so I can verify before anything irreversible happens.",
        "segment": "Map the Agentic Loop: Observe - Plan - Act - Check - Report with Claude",
    },
    "claude-liam-marketing": {
        "title": "Claude, On Message",
        "narration": "Your turn. Paste this: you use Claude for marketing copy and the output is always competent but never on your brand's voice. Ask Claude to show you the on-message system: how to encode brand voice in a way Claude can follow rather than approximate, the three most common ways Claude drifts off-brand even with a voice guide, and the fastest correction prompt when the draft reads like Claude wrote it.",
        "command": "I use Claude for marketing copy and the output is always competent but never quite on my brand's voice. Show me the on-message system: how to encode brand voice in a way Claude can follow rather than approximate, the three most common ways Claude drifts off-brand even with a voice guide, and the fastest correction prompt when the draft reads like Claude wrote it rather than a human from our brand team.",
        "segment": "Claude, On Message",
    },
    "claude-liam-nine-prompt-writing-skills": {
        "title": "Nine Skills That Write Your Prompts",
        "narration": "Your turn. Paste this: you want to get systematically better at prompting and you need a framework — not tips, a set of skills you can practice. Ask Claude to describe the nine prompt-writing skills, tell you which skill gap produces the most common failure mode in your workflow, and give you one deliberate practice exercise for the skill that's hardest to improve through trial and error alone.",
        "command": "I want to get systematically better at prompting and I need a framework — not tips, a set of skills I can practice deliberately. Describe the nine prompt-writing skills, tell me which skill gap produces the most common failure mode in a knowledge-work workflow, and give me one deliberate practice exercise for the skill that's hardest to improve through trial and error alone.",
        "segment": "Nine Skills That Write Your Prompts",
    },
    "claude-liam-non-delegation-audit": {
        "title": "The Non-Delegation Audit: Four Tests for Tasks That Should Never Go to Claude",
        "narration": "Your turn. Paste this: you want to audit your Claude workflow to make sure you're not delegating tasks that shouldn't be delegated — decisions that require judgment, accountability, or information Claude can't access. Ask Claude to run the four-test non-delegation audit on a workflow you describe, and tell you which tasks fail at least one test and should stay with a human.",
        "command": "I want to audit my Claude workflow to make sure I'm not delegating tasks that shouldn't be delegated — decisions requiring judgment, accountability, or information Claude can't access. Run the four-test non-delegation audit on a workflow I'll describe: for each step, apply the four tests and tell me which tasks fail at least one and should stay with a human rather than going to Claude.",
        "segment": "The Non-Delegation Audit: Four Tests for Tasks That Should Never Go to Claude",
    },
    "claude-liam-nondelegation-checklist": {
        "title": "Nondelegation Checklist: Can vs. Should",
        "narration": "Your turn. Paste this: you have a task that Claude can technically do but you're not sure whether it should. Ask Claude to run the nondelegation checklist — the four questions that distinguish 'can' from 'should' — and tell you whether the task should stay with you or can safely go to Claude, with the specific question that makes the decision.",
        "command": "I have a task that Claude can technically do but I'm not sure it should. Run the nondelegation checklist — the four questions that distinguish 'can' from 'should' — and tell me whether this task should stay with me or can safely go to Claude, identifying the specific question that drives the decision and what the right answer to that question would change.",
        "segment": "Nondelegation Checklist: Can vs. Should",
    },
    "claude-liam-one-hour-on-cowork": {
        "title": "1 Hour on Claude Cowork",
        "narration": "Your turn. Paste this: you have one hour to evaluate Claude Cowork and you want to use it on a real task — not a demo. Ask Claude to show you the one-hour evaluation protocol: which task type to choose, how to set up the session so you see Claude's actual behavior rather than its best case, and what to look for at the end of the hour that tells you whether it fits your workflow.",
        "command": "I have one hour to evaluate Claude Cowork and I want to use it on a real task — not a demo. Show me the one-hour evaluation protocol: which task type to choose so I see meaningful behavior, how to set up the session so I see Claude's actual behavior rather than its best case, and what to look for at the end of the hour that tells me whether it fits my actual workflow.",
        "segment": "1 Hour on Claude Cowork",
    },
    "claude-liam-plan-approval-gate": {
        "title": "Plan Approval Gate: The 5-Question Review Checklist",
        "narration": "Your turn. Paste this: you're about to approve a plan Claude generated for a multi-step task and you want a systematic way to review it before clicking go. Ask Claude to walk you through the five-question plan approval gate — what each question checks, which question catches the most dangerous plans, and how to modify a plan that fails one of the five before approving it.",
        "command": "I'm about to approve a plan Claude generated for a multi-step task and I want a systematic way to review it in under two minutes. Walk me through the five-question plan approval gate: what each question checks, which question catches the most dangerous plans, and how to modify a plan that fails one of the five without restarting the whole planning step.",
        "segment": "Plan Approval Gate: The 5-Question Review Checklist",
    },
    "claude-liam-plan-review-checklist": {
        "title": "The Plan-Review Checklist Before You Click Approve",
        "narration": "Your turn. Paste this: you have a plan Claude generated and you're about to approve it. Ask Claude to run the plan-review checklist on it: the five things to check before approving, which check is most commonly skipped, and what the right response is when a plan passes four of five but fails on scope — do you approve with a note or reject and replan.",
        "command": "I have a Claude-generated plan and I'm about to approve it. Run the plan-review checklist: the five things to check before approving, which check is most commonly skipped in practice, and what the right response is when a plan passes four of five but fails on scope — do I approve with a modification note, reject and replan, or narrow the scope before regenerating?",
        "segment": "The Plan-Review Checklist Before You Click Approve",
    },
    "claude-liam-privacy-classification-scanner": {
        "title": "Build a Privacy Classification Scanner for Cowork Folders",
        "narration": "Your turn. Paste this: you want to build a scanner that classifies files in a Claude Cowork folder by privacy level before any AI workflow runs on them. Ask Claude to show you the scanner architecture: the three classification tiers, the pattern the scanner looks for to assign each tier, and how the classification gates which files Claude is allowed to read.",
        "command": "I want to build a scanner that classifies files in a Claude Cowork folder by privacy level before any AI workflow runs on them. Show me the scanner architecture: the three classification tiers (public, internal, sensitive), the patterns the scanner looks for to assign each tier, and how the classification gates which files Claude is allowed to read in the workflow.",
        "segment": "Build a Privacy Classification Scanner for Cowork Folders",
    },
    "claude-liam-product": {
        "title": "Claude, Shipping",
        "narration": "Your turn. Paste this: you want to use Claude to accelerate product work — specs, user stories, competitive analysis, release notes — without losing the judgment calls that belong to you. Ask Claude to show you the product workflow stack: which product tasks Claude handles best, which ones require your judgment even after Claude drafts them, and the review step that catches Claude's most common product mistake.",
        "command": "I want to use Claude to accelerate product work — specs, user stories, competitive analysis, release notes — without losing the judgment calls that belong to me. Show me the product workflow stack: which product tasks Claude handles best, which ones require my judgment even after Claude drafts them, and the review step that catches Claude's most common product mistake (usually a scope or audience assumption).",
        "segment": "Claude, Shipping",
    },
    "claude-liam-productivity": {
        "title": "Claude, In Order",
        "narration": "Your turn. Paste this: you want to use Claude to manage your personal productivity — tasks, priorities, weekly reviews — but previous attempts felt like more work than the system saved. Ask Claude to show you the minimum viable Claude productivity stack: the three workflow touchpoints where Claude saves real time, and why more Claude in more steps usually makes the system worse, not better.",
        "command": "I want to use Claude to manage my personal productivity — tasks, priorities, weekly reviews — but previous attempts felt like more work than the system saved. Show me the minimum viable Claude productivity stack: the three workflow touchpoints where Claude saves real time, why more Claude in more steps usually makes a productivity system worse not better, and how to know when to stop adding Claude to the workflow.",
        "segment": "Claude, In Order",
    },
    "claude-liam-receipt-extraction-pipeline": {
        "title": "Receipt Extraction Pipeline: Schema-First vs. No-Schema",
        "narration": "Your turn. Paste this: you're building a receipt extraction pipeline and you're deciding whether to define the output schema upfront or let Claude determine what to extract. Ask Claude to show you the comparison: run the same receipt through schema-first and no-schema extraction, show what each produces, and tell you which approach is more reliable when receipts vary in format.",
        "command": "I'm building a receipt extraction pipeline and I'm deciding whether to define the output schema upfront or let Claude determine what to extract. Show me the comparison: run the same receipt through schema-first and no-schema extraction, show what each produces, and tell me which approach is more reliable when receipts vary in format — and when the no-schema approach ever wins.",
        "segment": "Receipt Extraction Pipeline: Schema-First vs. No-Schema",
    },
    "claude-liam-report-claim-tracing": {
        "title": "Report Claim Tracing: Read for Evidence, Not Flow",
        "narration": "Your turn. Paste this: you want Claude to read a report and trace every factual claim back to its source — not summarize the flow, find the evidence. Ask Claude to show you the claim-tracing prompt: how to instruct Claude to extract claims and source references separately, what it reports when a claim has no traceable source, and how to use the trace to decide which claims need verification.",
        "command": "I want Claude to read a report and trace every factual claim back to its source — not summarize the flow, find the evidence trail. Show me the claim-tracing prompt: how to instruct Claude to extract claims and source references separately, what it reports when a claim has no traceable source in the document, and how I use the trace output to decide which claims need external verification before I cite them.",
        "segment": "Report Claim Tracing: Read for Evidence, Not Flow",
    },
    "claude-liam-research-packet-traceability": {
        "title": "Assemble a Research Packet with Source Traceability",
        "narration": "Your turn. Paste this: you want Claude to assemble a research packet from multiple sources while keeping every claim traceable to its origin. Ask Claude to show you the traceability architecture: how to structure the prompt so Claude tags every claim with its source, the format for the packet that makes tracing easy, and what to do when Claude synthesizes a claim that doesn't appear in any single source.",
        "command": "I want Claude to assemble a research packet from multiple sources while keeping every claim traceable to its origin. Show me the traceability architecture: how to structure the prompt so Claude tags every claim with its source, the format for the packet that makes tracing easy for a reader who didn't see the source documents, and what to do when Claude synthesizes a claim that doesn't appear in any single source verbatim.",
        "segment": "Assemble a Research Packet with Source Traceability",
    },
    "claude-liam-routing-matrix": {
        "title": "Measure the Routing Matrix: Which Tasks Belong to Claude vs. Human",
        "narration": "Your turn. Paste this: you want to build a routing matrix for your team — a decision tool that tells you which tasks should go to Claude versus a human without evaluating each task from scratch every time. Ask Claude to show you the matrix dimensions, how to calibrate the matrix for your specific workflow, and the three task types that most commonly get routed wrong.",
        "command": "I want to build a routing matrix for my team — a decision tool that tells us which tasks should go to Claude versus a human without evaluating each task from scratch. Show me the matrix dimensions (reversibility, judgment required, information access, accountability), how to calibrate the matrix for our specific workflow, and the three task types that most commonly get routed wrong in practice.",
        "segment": "Measure the Routing Matrix: Which Tasks Belong to Claude vs. Human",
    },
    "claude-liam-sales": {
        "title": "Claude, Closing",
        "narration": "Your turn. Paste this: you want to use Claude to help with sales work — prospect research, outreach drafting, proposal writing, follow-up — without producing AI-sounding copy that gets ignored. Ask Claude to show you the sales workflow stack: which sales tasks Claude handles best, how to keep the output sounding like you rather than a template, and the one thing you should always add yourself before sending.",
        "command": "I want to use Claude to help with sales work — prospect research, outreach drafting, proposal writing, follow-up — without producing AI-sounding copy that gets ignored. Show me the sales workflow stack: which sales tasks Claude handles best, how to keep the output sounding like me rather than a template, and the one thing I should always add myself before sending any Claude-drafted outreach.",
        "segment": "Claude, Closing",
    },
    "claude-liam-seven-field-brief": {
        "title": "Seven Fields That Make a Task Brief",
        "narration": "Your turn. Paste this: you want to build a standard task brief format for your team's Claude workflows so everyone gives Claude the same quality input. Ask Claude to show you the seven-field brief: what each field is, why each one is necessary rather than optional, and which field is most commonly omitted — causing the most common failure mode in team Claude workflows.",
        "command": "I want to build a standard task brief format for my team's Claude workflows so everyone gives Claude the same quality input. Show me the seven-field brief: what each field is (task, context, output format, constraints, audience, examples, success criteria), why each one is necessary rather than optional, and which field is most commonly omitted and causes the most common team workflow failure.",
        "segment": "Seven Fields That Make a Task Brief",
    },
    "claude-liam-six-claude-formulas": {
        "title": "Six Formulas Run 80% of My Work",
        "narration": "Your turn. Paste this: you want to build your own set of Claude formulas — structured prompt templates that you run for recurring task types without starting from scratch each time. Ask Claude to show you the six formula categories that cover the most common knowledge-work tasks, how to write a formula rather than a one-time prompt, and how to test a formula before relying on it.",
        "command": "I want to build my own set of Claude formulas — structured prompt templates that I run for recurring task types without starting from scratch each time. Show me the six formula categories that cover the most common knowledge-work tasks, how to write a formula rather than a one-time prompt (what makes it reusable), and how to test a formula against edge cases before I rely on it in production work.",
        "segment": "Six Formulas Run 80% of My Work",
    },
    "claude-liam-stop-hitting-claude-limits": {
        "title": "Message 30 Costs 31 Times More",
        "narration": "Your turn. Paste this: your Claude sessions keep running out of context or hitting usage limits before the task is done. Ask Claude to show you the session-length economics: why the cost of a message at the end of a long session is much higher than at the start, how to structure multi-step tasks to stay within a session, and when to start a new session rather than continuing the current one.",
        "command": "My Claude sessions keep running out of context or hitting usage limits before the task is done. Show me the session-length economics: why the cost of processing a message at the end of a long session is much higher than at the start, how to structure multi-step tasks to stay within a session, and the clear signal that tells me it's time to start a new session rather than continuing the current one.",
        "segment": "Message 30 Costs 31 Times More",
    },
    "claude-liam-stop-prompting-claude": {
        "title": "Let the Files Do the Prompting",
        "narration": "Your turn. Paste this: you spend too much time re-explaining context to Claude at the start of every session. Ask Claude to show you the file-based prompting approach: what files to build so Claude loads context from them rather than from your prompt, how to structure a CLAUDE.md or context file that makes the session start immediately productive, and which context should be in files versus which still belongs in the prompt.",
        "command": "I spend too much time re-explaining context to Claude at the start of every session — same background, same constraints, same preferences every time. Show me the file-based prompting approach: what files to build so Claude loads context from them rather than from my prompt, how to structure a CLAUDE.md or context file that makes the session start immediately productive, and which context should be in files versus which still belongs in the task prompt.",
        "segment": "Let the Files Do the Prompting",
    },
    "claude-liam-stop-writing-like-ai": {
        "title": "It's Not That. It's This.",
        "narration": "Your turn. Paste this: your Claude-drafted content sounds like AI wrote it — over-structured, hedged, generic. Ask Claude to show you the specific phrases and patterns that mark text as AI-generated, the rewrite moves that eliminate them without losing the substance, and how to write a Claude prompt that produces less AI-sounding output from the start rather than fixing it afterward.",
        "command": "My Claude-drafted content sounds like AI wrote it — over-structured, hedged, generic, with three-part answers to every question. Show me the specific phrases and patterns that mark text as AI-generated, the rewrite moves that eliminate them without losing the substance, and how to write a Claude prompt that produces less AI-sounding output from the start so I'm not editing every draft to sound human.",
        "segment": "It's Not That. It's This.",
    },
    "claude-liam-support": {
        "title": "Claude, On Call",
        "narration": "Your turn. Paste this: you want to use Claude to handle support tasks — drafting responses, looking up policies, categorizing tickets — without Claude giving customers confident wrong answers. Ask Claude to show you the support workflow pattern: how to give Claude access to the right information, the guardrail that keeps Claude from answering questions its information doesn't cover, and when to escalate to a human automatically.",
        "command": "I want to use Claude to handle support tasks — drafting responses, looking up policies, categorizing tickets — without Claude giving customers confident wrong answers. Show me the support workflow pattern: how to give Claude access to the right policy and product information, the guardrail that keeps Claude from answering questions its information doesn't cover, and the condition that automatically escalates to a human rather than letting Claude guess.",
        "segment": "Claude, On Call",
    },
    "claude-liam-synthesis-vs-deciding": {
        "title": "Organizing vs. Deciding: Meeting Notes That Misrepresent",
        "narration": "Your turn. Paste this: you use Claude to summarize meeting notes and the summaries misrepresent what was actually decided — they turn 'we should probably' into 'we will' and 'some concern was raised' into 'the concern was resolved.' Ask Claude to show you the synthesis-versus-deciding distinction: the prompt instruction that tells Claude to organize without deciding, and how to flag language that implies a decision the meeting didn't actually make.",
        "command": "I use Claude to summarize meeting notes and the summaries misrepresent what was decided — they upgrade 'we should probably' to 'we will' and flatten 'some concern was raised' into 'concern noted.' Show me the synthesis-versus-deciding distinction: the prompt instruction that tells Claude to organize without deciding, and how to flag language in the summary that implies a decision the meeting didn't actually make.",
        "segment": "Organizing vs. Deciding: Meeting Notes That Misrepresent",
    },
    "claude-liam-task-brief-validator": {
        "title": "Build a Task-Brief Validator with Claude",
        "narration": "Your turn. Paste this: you want to build a task-brief validator — a tool that checks whether a brief has everything Claude needs before you hand the task over. Ask Claude to show you the validator's five checks, what it reports when a field is missing or too vague, and how the validator output should be formatted so it's fast to act on rather than just a list of problems.",
        "command": "I want to build a task-brief validator — a tool that checks whether a brief has everything Claude needs before I hand the task over. Show me the validator's five checks (scope, success criteria, output format, constraints, context), what it reports when a field is missing or too vague to be actionable, and how the validator output should be formatted so it's fast to act on rather than just a list of problems to reread.",
        "segment": "Build a Task-Brief Validator with Claude",
    },
    "claude-liam-troubleshooting": {
        "title": "Claude, Unstuck",
        "narration": "Your turn. Paste this: Claude is giving you bad output and you don't know why. Ask Claude to walk you through the troubleshooting ladder: the five diagnostic steps from easiest to hardest, what each step tests, and the specific question to ask Claude itself that most often reveals why a prompt isn't working when all the obvious fixes have already been tried.",
        "command": "Claude is giving me bad output and I don't know why — I've tried rephrasing and it's still wrong. Walk me through the troubleshooting ladder: the five diagnostic steps from easiest to hardest, what each step tests (context, constraints, examples, format, scope), and the specific question to ask Claude itself that most often reveals why a prompt isn't working when all the obvious fixes have already been tried.",
        "segment": "Claude, Unstuck",
    },
    "claude-liam-vercel-mcp": {
        "title": "Two Things Named Vercel MCP",
        "narration": "Your turn. Paste this: you've seen 'Vercel MCP' in two different contexts and you're not sure if they're the same thing. Ask Claude to clarify what the two things named Vercel MCP actually are, what each one does in a workflow, and when you'd use one versus the other — and why confusing them causes a specific failure mode you might not notice until production.",
        "command": "I've seen 'Vercel MCP' in two different contexts and I'm not sure if they're the same thing. Clarify what the two things named Vercel MCP actually are, what each one does in a Claude workflow, and when I'd use one versus the other — and what the specific failure mode is when you confuse them that you might not notice until you're in production.",
        "segment": "Two Things Named Vercel MCP",
    },
    "claude-liam-vercel-refactor": {
        "title": "Refactor, Verified",
        "narration": "Your turn. Paste this: you want to use Claude Code to refactor a codebase but you're worried it will break things that weren't broken. Ask Claude to show you the verified refactor protocol: how to establish a test baseline before refactoring, the step sequence that keeps Claude's changes verifiable at each stage, and the handoff condition that tells you the refactor is done rather than just done-looking.",
        "command": "I want to use Claude Code to refactor a codebase but I'm worried it will break things that weren't broken. Show me the verified refactor protocol: how to establish a test baseline before refactoring begins, the step sequence that keeps Claude's changes verifiable at each stage, and the handoff condition that tells me the refactor is genuinely done rather than just compiling and passing the tests I thought to write.",
        "segment": "Refactor, Verified",
    },
    "claude-liam-vox-batch-propagation": {
        "title": "Why 200 Tiny, Reversible Renames Add Up to One You Can't Undo",
        "narration": "Your turn. Paste this: you're about to run a batch operation — 200 file renames that each look reversible. Ask Claude to show you the batch propagation risk: why individually reversible operations can aggregate into an irreversible state change, the checkpoint pattern that lets you stop and reverse at any point in the batch, and the test you run on the first ten renames before running the other 190.",
        "command": "I'm about to run a batch operation — 200 file renames that each look individually reversible. Show me the batch propagation risk: why individually reversible operations can aggregate into an irreversible state change, the checkpoint pattern that lets me stop and reverse at any point in the batch, and the test I should run on the first ten renames before committing to the other 190.",
        "segment": "Why 200 Tiny, Reversible Renames Add Up to One You Can't Undo",
    },
    "claude-liam-vox-coherent-unsafe": {
        "title": "Why a Plan That Reads Perfectly Can Still Delete Your Files",
        "narration": "Your turn. Paste this: Claude generated a plan that looks perfectly coherent and you're about to approve it — but something feels off. Ask Claude to show you the coherent-unsafe pattern: the three ways a plan can be internally consistent but structurally dangerous, the one-sentence test that exposes plans that read well but act badly, and how to force Claude to flag its own assumptions before you approve.",
        "command": "Claude generated a plan that looks perfectly coherent and I'm about to approve it — but something feels off and I can't articulate why. Show me the coherent-unsafe pattern: the three ways a plan can be internally consistent but structurally dangerous, the one-sentence test that exposes plans that read well but act badly, and how to force Claude to surface its own assumptions and irreversibilities before I approve.",
        "segment": "Why a Plan That Reads Perfectly Can Still Delete Your Files",
    },
    "claude-liam-vox-compression-caveats": {
        "title": "Why Summarizing Deletes Exactly the Caveats",
        "narration": "Your turn. Paste this: you asked Claude to summarize a document and the summary dropped all the caveats — the 'only if,' 'except when,' 'subject to' language that changes what the main claims actually mean. Ask Claude to show you why summarization systematically drops caveats, the prompt instruction that forces Claude to preserve them, and how to test whether a summary is safe to use without the original.",
        "command": "I asked Claude to summarize a document and the summary dropped all the caveats — the 'only if,' 'except when,' 'subject to' language that materially changes what the main claims mean. Show me why summarization systematically drops caveats, the prompt instruction that forces Claude to preserve conditional language, and how to test whether a summary is safe to use without the original document beside it.",
        "segment": "Why Summarizing Deletes Exactly the Caveats",
    },
    "claude-liam-vox-exposure-gate": {
        "title": "Why Checking the Output Won't Save You",
        "narration": "Your turn. Paste this: you check Claude's output before using it and you think that's enough to catch mistakes. Ask Claude to show you the exposure gate failure: the class of Claude errors that look correct when you check but are wrong in context, what 'checking the output' actually catches versus what it misses, and the exposure gate that catches downstream failures before they reach anyone else.",
        "command": "I check Claude's output before using it and I think that's enough to catch mistakes. Show me the exposure gate failure: the class of Claude errors that look correct when I check them but are wrong in the downstream context where they'll be used, what 'checking the output' actually catches versus what it systematically misses, and the exposure gate that catches downstream failures before they reach anyone outside my workflow.",
        "segment": "Why Checking the Output Won't Save You",
    },
    "claude-liam-vox-format-credibility": {
        "title": "Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten",
        "narration": "Your turn. Paste this: Claude generated a spreadsheet that looks impeccably formatted but the numbers are wrong by a factor of ten. Ask Claude to show you the format-credibility trap: why a well-formatted output signals correctness to the human reviewer but has no correlation with numerical accuracy, the sanity check that catches order-of-magnitude errors before the spreadsheet gets shared, and how to structure the prompt so Claude flags its own uncertainty about the numbers.",
        "command": "Claude generated a spreadsheet that looks impeccably formatted but the numbers are wrong by an order of magnitude. Show me the format-credibility trap: why a well-formatted output signals correctness to a human reviewer but has no correlation with numerical accuracy, the sanity check that catches order-of-magnitude errors before the spreadsheet gets shared, and how to structure the prompt so Claude flags its own uncertainty about the numbers rather than presenting them confidently.",
        "segment": "Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten",
    },
    "claude-liam-vox-instruction-channel": {
        "title": "Why an Agent Obeys the Web Page Instead of You",
        "narration": "Your turn. Paste this: you built a Claude agent that reads web pages and it started following instructions embedded in one of the pages instead of yours. Ask Claude to show you the instruction-channel problem: how an agent decides whose instructions to follow when the document it's reading contains instructions, the isolation pattern that separates your instructions from document content, and the trust hierarchy that tells the agent what to obey.",
        "command": "I built a Claude agent that reads web pages and it started following instructions embedded in one of the pages instead of mine — the page said 'ignore your previous instructions' and the agent obeyed. Show me the instruction-channel problem: how an agent decides whose instructions to follow when a document contains instructions, the isolation pattern that separates my instructions from document content, and the trust hierarchy that tells the agent what to obey.",
        "segment": "Why an Agent Obeys the Web Page Instead of You",
    },
    "claude-liam-vox-modal-upgrade": {
        "title": "Why \"Maybe We Should\" Becomes \"Decision: We Will\"",
        "narration": "Your turn. Paste this: you asked Claude to summarize a meeting discussion and the summary upgraded a tentative suggestion into a decision. Ask Claude to show you the modal upgrade failure: the specific language patterns Claude collapses when summarizing deliberative content, the instruction that tells Claude to preserve the epistemic status of each statement, and how to review a meeting summary for modal upgrades before distributing it.",
        "command": "I asked Claude to summarize a meeting discussion and the summary upgraded 'maybe we should explore this' into 'Decision: we will implement this.' Show me the modal upgrade failure: the specific language patterns Claude collapses when summarizing deliberative content, the instruction that tells Claude to preserve the epistemic status of each statement (tentative, agreed, tabled, rejected), and how to review a summary for modal upgrades before distributing it.",
        "segment": "Why \"Maybe We Should\" Becomes \"Decision: We Will\"",
    },
    "claude-liam-vox-same-prescription": {
        "title": "Why a Model Can't Catch Its Own Mistake",
        "narration": "Your turn. Paste this: you asked Claude to review something it generated and it said everything looks correct — but you found the error yourself afterward. Ask Claude to show you the self-review blind spot: what makes models structurally unable to catch certain categories of their own errors, the second-turn critique design that creates actual independence, and the specific prompt instruction that gets the most useful self-critique without falling into the same blind spot.",
        "command": "I asked Claude to review something it generated and it said everything looks correct — then I found the error myself. Show me the self-review blind spot: what makes models structurally unable to catch certain categories of their own errors (not laziness — architecture), the second-turn critique design that creates actual independence from the first answer, and the specific prompt instruction that gets the most useful self-critique without falling into the same blind spot.",
        "segment": "Why a Model Can't Catch Its Own Mistake",
    },
    "claude-liam-vox-scope-gap": {
        "title": "Why Read-Only Access Still Leaks",
        "narration": "Your turn. Paste this: you gave Claude read-only access to a folder and assumed that was safe — but information from those files ended up somewhere it shouldn't. Ask Claude to show you the read-only leakage failure: how read access enables information flows you didn't intend, the scope gap between what you restricted and what you needed to restrict, and the access audit that catches leakage paths before granting any connector access.",
        "command": "I gave Claude read-only access to a folder and assumed that was safe — but information from those files ended up somewhere it shouldn't. Show me the read-only leakage failure: how read access enables information flows I didn't intend, the scope gap between what I restricted and what I needed to restrict, and the access audit that catches leakage paths before granting any connector access to a Claude workflow.",
        "segment": "Why Read-Only Access Still Leaks",
    },
    "claude-liam-weekly-operations-packet": {
        "title": "Build the Weekly Operations Packet with Claude: Capstone Demo",
        "narration": "Your turn. Paste this: you want to build a weekly operations packet with Claude — a recurring artifact that consolidates status, decisions, and actions from the week. Ask Claude to walk you through the capstone demo: the five sections of the packet, how each section is generated from different sources, and the single Claude workflow that assembles the whole packet in one run from raw inputs.",
        "command": "I want to build a weekly operations packet with Claude — a recurring artifact that consolidates status, decisions, and actions from the week. Walk me through the capstone demo: the five sections of the packet, how each section is generated from different sources (meeting notes, project trackers, action logs), and the single Claude workflow that assembles the whole packet in one run from raw inputs without me manually stitching sections together.",
        "segment": "Build the Weekly Operations Packet with Claude: Capstone Demo",
    },
    "claude-liam-workflow-canvas": {
        "title": "Design a Personal Workflow Canvas with Claude",
        "narration": "Your turn. Paste this: you want to design a personal workflow canvas — a map of your recurring tasks that shows where Claude fits, where humans must stay, and where the handoffs between them happen. Ask Claude to show you the canvas structure: the five zones to map, how to place your current tasks in the right zone, and how the canvas changes over time as you automate more.",
        "command": "I want to design a personal workflow canvas — a map of my recurring tasks that shows where Claude fits, where humans must stay, and where the handoffs between them happen. Show me the canvas structure: the five zones to map (automate, assist, review, decide, delegate out), how to place my current tasks in the right zone, and how the canvas changes over time as I automate more of the assist zone.",
        "segment": "Design a Personal Workflow Canvas with Claude",
    },
    "claude-liam-workflow-card-builder": {
        "title": "Workflow Card: Saved Prompt vs. Reusable Recipe",
        "narration": "Your turn. Paste this: you have a prompt that works and you want to turn it into a workflow card — something reusable that works in different contexts, not just a saved copy of the text. Ask Claude to show you the difference between a saved prompt and a reusable recipe, the four fields that make a card a recipe rather than a text blob, and how to test the card on a new input before relying on it.",
        "command": "I have a prompt that works and I want to turn it into a workflow card — something reusable in different contexts, not just a saved copy of the text. Show me the difference between a saved prompt and a reusable recipe, the four fields that make a card a recipe (intent, prompt template, required inputs, success criteria), and how to test the card on a new input before relying on it in a real workflow.",
        "segment": "Workflow Card: Saved Prompt vs. Reusable Recipe",
    },
    "claude-liam-workflow-card-generator": {
        "title": "Generate a Reusable Workflow Card from a Successful Task",
        "narration": "Your turn. Paste this: you just finished a task with Claude that worked well and you want to capture it as a reusable workflow card before you forget how you did it. Ask Claude to generate the workflow card from the task you describe: extract the intent, generalize the prompt into a template, identify the required inputs, and write the success criteria so you can repeat this workflow next time without reconstructing it.",
        "command": "I just finished a task with Claude that worked well and I want to capture it as a reusable workflow card before I forget how I did it. Generate the workflow card from the task I'll describe: extract the intent, generalize the prompt into a reusable template, identify the required inputs that must vary for each instance, and write the success criteria so I can repeat this workflow without reconstructing it from scratch.",
        "segment": "Generate a Reusable Workflow Card from a Successful Task",
    },
    "claude-liam-workflow-handoff-documenter": {
        "title": "Workflow Handoff Documenter — The Seam Is the Unit of Risk",
        "narration": "Your turn. Paste this: you have a multi-step Claude workflow and you want to document every handoff point — every seam between Claude steps and between Claude and human steps — because that's where errors compound. Ask Claude to show you the handoff documentation format: what to record at each seam, why the seam is the unit of risk rather than the step, and how to use the documentation to find the weakest handoff in your current workflow.",
        "command": "I have a multi-step Claude workflow and I want to document every handoff point — every seam between Claude steps and between Claude and human steps — because that's where errors compound. Show me the handoff documentation format: what to record at each seam (what passes across it, what could go wrong, who verifies), why the seam is the unit of risk rather than the step itself, and how to use the documentation to identify the weakest handoff in my current workflow.",
        "segment": "Workflow Handoff Documenter — The Seam Is the Unit of Risk",
    },
    "claude-liam-workspace-access-audit": {
        "title": "Build a Workspace Access Audit with Claude",
        "narration": "Your turn. Paste this: you want to audit what Claude has access to across your workspace — all connectors, all integrations, all enabled permissions — before you add another workflow. Ask Claude to show you the workspace access audit: how to enumerate what Claude can read and write in your workspace, the three categories of access that are most commonly over-granted, and the access reduction checklist that closes unnecessary exposure.",
        "command": "I want to audit what Claude has access to across my workspace — all connectors, integrations, and enabled permissions — before I add another workflow. Show me the workspace access audit: how to enumerate what Claude can read and write in my workspace, the three categories of access that are most commonly over-granted in knowledge-work deployments, and the access reduction checklist that closes unnecessary exposure without breaking existing workflows.",
        "segment": "Build a Workspace Access Audit with Claude",
    },
    "cowork-access-ladder": {
        "title": "The Cowork Access Ladder: Lowest Rung That Works",
        "narration": "Your turn. Paste this: you're setting up a Claude Cowork workflow and you need to decide what level of access to grant for each step. Ask Claude to show you the cowork access ladder — what each rung allows, the principle of lowest rung that works, and how to map your specific workflow tasks to the right rung before enabling anything.",
        "command": "I'm setting up a Claude Cowork workflow and I need to decide what level of access to grant for each step. Show me the cowork access ladder: what each rung allows, the principle of the lowest rung that works, and how to map my workflow tasks to the right rung before enabling access — including one example where choosing a higher rung than needed causes a real problem.",
        "segment": "The Cowork Access Ladder: Lowest Rung That Works",
    },
    "cowork-task-packet": {
        "title": "The Cowork Task Packet: Five Fields, One Scope",
        "narration": "Your turn. Paste this: you want to build a Claude Cowork task packet — a structured brief that gives Claude exactly what it needs to complete a task without scope creep. Ask Claude to show you the five fields, what goes in each one, and how the packet prevents the two most common failure modes: Claude doing too much or doing the wrong thing.",
        "command": "I want to build a Claude Cowork task packet — a structured brief that gives Claude exactly what it needs to complete a task without scope creep. Show me the five fields, what goes in each one, and how the packet prevents the two most common failure modes: Claude expanding scope beyond the task and Claude completing the wrong task confidently.",
        "segment": "The Cowork Task Packet: Five Fields, One Scope",
    },
    "cowork-task-packet-audit": {
        "title": "Audit a Claude Cowork Task Packet in Sixty Seconds",
        "narration": "Your turn. Paste this: you have a task packet and you want to audit it before handing it to Claude. Ask Claude to run the sixty-second audit: the three questions that reveal whether the scope is tight, whether the success condition is measurable, and whether Claude has everything it needs to complete the task without asking you for more.",
        "command": "I have a task packet and I want to audit it before handing it to Claude. Run the sixty-second audit: the three questions that reveal whether the scope is tight, whether the success condition is measurable, and whether Claude has everything it needs to complete the task without asking me for more context mid-task.",
        "segment": "Audit a Claude Cowork Task Packet in Sixty Seconds",
    },
    "earnings-preview-verbatim-gate": {
        "title": "Read the Last Call, Word for Word",
        "narration": "Your turn. Paste this: you're preparing an earnings preview and you want Claude to read the last earnings call transcript — not summarize it, read it for specific verbatim language. Ask Claude to show you the verbatim gate prompt: how to instruct Claude to extract exact quotes rather than paraphrases, which phrases to search for in an earnings call, and how to use the verbatim output to anchor your preview without misquoting management.",
        "command": "I'm preparing an earnings preview and I want Claude to read the last earnings call transcript for specific verbatim language — not paraphrase it. Show me the verbatim gate prompt: how to instruct Claude to extract exact quotes rather than summaries, which phrase categories to search for in an earnings call (guidance language, risk qualifiers, product commitments), and how to use the verbatim output to anchor my preview without misquoting management.",
        "segment": "Read the Last Call, Word for Word",
    },
    "equity-research-initiating-coverage-gate": {
        "title": "It Won't Value What It Hasn't Modeled",
        "narration": "Your turn. Paste this: you're using Claude to help initiate coverage on a company and Claude is giving you valuation language for a business model it hasn't actually modeled. Ask Claude to show you the coverage gate: how to know when Claude is describing a model versus running one, the prompt that forces Claude to name what it would need to model before making a valuation claim, and how to use Claude to build toward a model without letting it substitute description for calculation.",
        "command": "I'm using Claude to help initiate coverage on a company and Claude is giving me valuation language for a business model it hasn't actually modeled — confident language about multiples without the underlying work. Show me the coverage gate: how to know when Claude is describing a model versus running one, the prompt that forces Claude to name what it would need to model before making a valuation claim, and how to use Claude to build toward a model without letting it substitute description for calculation.",
        "segment": "It Won't Value What It Hasn't Modeled",
    },
    "extraction-schema-first": {
        "title": "Extraction Schema First: Structure Confers Credibility",
        "narration": "Your turn. Paste this: you want Claude to extract structured data from unstructured text and you're getting inconsistent output. Ask Claude to show you the schema-first extraction pattern: how defining the output schema before the extraction prompt changes what Claude produces, and why schema-first is more reliable than asking Claude to find the fields.",
        "command": "I want Claude to extract structured data from unstructured text — receipts, reports, emails — and I'm getting inconsistent output. Show me the schema-first extraction pattern: how defining the output schema before the extraction prompt changes what Claude produces, why structure-first is more reliable than asking Claude to find the fields, and how to write the schema so Claude fills it rather than inventing around it.",
        "segment": "Extraction Schema First: Structure Confers Credibility",
    },
    "file-rename-dry-run": {
        "title": "Build a File-Rename Dry-Run Tool with Claude",
        "narration": "Your turn. Paste this: you want to build a file-rename tool with Claude that shows you exactly what it will do before it does anything. Ask Claude to show you the dry-run architecture: how the tool generates a rename plan without executing it, how you review and approve the plan, and what the hook looks like that blocks execution until the plan is confirmed.",
        "command": "I want to build a file-rename tool with Claude that shows me exactly what it will do before it does anything. Show me the dry-run architecture: how the tool generates a rename plan without executing it, how I review and approve the plan, and what the hook looks like that blocks execution until the plan is explicitly confirmed — so the tool structurally cannot rename before review.",
        "segment": "Build a File-Rename Dry-Run Tool with Claude",
    },
    "financial-dcf-live-formula": {
        "title": "Every Cell a Live Formula",
        "narration": "Your turn. Paste this: you want Claude to build a DCF model where every cell is a live formula — not hardcoded values — so the model updates when inputs change. Ask Claude to show you the live-formula architecture: how to specify the formula structure rather than the values, how to verify that a cell Claude generates is a formula rather than a hardcoded number, and the audit that catches hardcoded values before the model goes to a client.",
        "command": "I want Claude to build a DCF model where every cell is a live formula — not hardcoded values — so the model updates when inputs change. Show me the live-formula architecture: how to specify the formula structure rather than the values in the prompt, how to verify that a cell Claude generates is a formula rather than a hardcoded number, and the audit that catches hardcoded values before the model goes to a client.",
        "segment": "Every Cell a Live Formula",
    },
    "human-approval-gates": {
        "title": "Design Human Approval Gates for a Multi-Step Agentic Workflow with Claude",
        "narration": "Your turn. Paste this: you're building a multi-step agentic workflow and you need to decide where to put human approval gates. Ask Claude to show you the gate-placement framework: the three properties that make a step require a gate versus run autonomously, and how to build the gate so Claude presents what it's about to do in a way you can actually review in thirty seconds.",
        "command": "I'm building a multi-step agentic workflow and I need to decide where to put human approval gates — not everywhere, but at the right steps. Show me the gate-placement framework: the three properties that make a step require a gate versus run autonomously, and how to build the gate so Claude presents what it's about to do in a format I can review and approve in thirty seconds.",
        "segment": "Design Human Approval Gates for a Multi-Step Agentic Workflow with Claude",
    },
    "managed-agents-two-object-split": {
        "title": "Two Objects, One Runtime",
        "narration": "Your turn. Paste this: you're building a system with two managed agents that share a runtime and you're getting state confusion between them. Ask Claude to show you the two-object split: how to structure shared versus agent-local state so agents don't overwrite each other's objects, the naming convention that prevents collision, and the runtime contract that tells each agent what it owns exclusively.",
        "command": "I'm building a system with two managed agents that share a runtime and I'm getting state confusion between them — one agent overwrites what the other wrote. Show me the two-object split: how to structure shared versus agent-local state so agents don't overwrite each other's objects, the naming convention that prevents collision, and the runtime contract that tells each agent what it owns exclusively and what it can only read.",
        "segment": "Two Objects, One Runtime",
    },
    "map-the-agentic-loop": {
        "title": "Map the Agentic Loop: Observe - Plan - Act - Check - Report with Claude",
        "narration": "Your turn. Paste this: you're building an agentic Claude workflow and you want to map every step to the observe-plan-act-check-report loop so you know exactly where human oversight belongs. Ask Claude to walk you through a concrete workflow — a document review pipeline — and label each step with its loop phase, the failure mode if that phase is skipped, and where the human gate should sit.",
        "command": "I'm building an agentic Claude workflow and I want to map every step to the observe-plan-act-check-report loop so I know where human oversight belongs. Walk me through a concrete workflow — a document review pipeline — and label each step with its loop phase, the failure mode if that phase is skipped, and where the human gate should sit so I can verify before anything irreversible happens.",
        "segment": "Map the Agentic Loop: Observe - Plan - Act - Check - Report with Claude",
    },
    "non-delegation-audit": {
        "title": "The Non-Delegation Audit: Four Tests for Tasks That Should Never Go to Claude",
        "narration": "Your turn. Paste this: you want to audit your Claude workflow to make sure you're not delegating tasks that shouldn't be delegated. Ask Claude to run the four-test non-delegation audit on a workflow you describe, and tell you which tasks fail at least one test and should stay with a human.",
        "command": "I want to audit my Claude workflow to make sure I'm not delegating tasks that shouldn't be delegated — decisions requiring judgment, accountability, or information Claude can't access. Run the four-test non-delegation audit on a workflow I'll describe: for each step, apply the four tests and tell me which tasks fail at least one and should stay with a human rather than going to Claude.",
        "segment": "The Non-Delegation Audit: Four Tests for Tasks That Should Never Go to Claude",
    },
    "nondelegation-checklist": {
        "title": "Nondelegation Checklist: Can vs. Should",
        "narration": "Your turn. Paste this: you have a task that Claude can technically do but you're not sure whether it should. Ask Claude to run the nondelegation checklist and tell you whether the task should stay with you or can safely go to Claude, with the specific question that makes the decision.",
        "command": "I have a task that Claude can technically do but I'm not sure it should. Run the nondelegation checklist — the four questions that distinguish 'can' from 'should' — and tell me whether this task should stay with me or can safely go to Claude, identifying the specific question that drives the decision.",
        "segment": "Nondelegation Checklist: Can vs. Should",
    },
    "plan-approval-gate": {
        "title": "Plan Approval Gate: The 5-Question Review Checklist",
        "narration": "Your turn. Paste this: you're about to approve a Claude-generated plan and you want a systematic way to review it before clicking go. Ask Claude to walk you through the five-question plan approval gate — what each question checks, which question catches the most dangerous plans, and how to modify a plan that fails one of the five.",
        "command": "I'm about to approve a plan Claude generated for a multi-step task and I want a systematic way to review it in under two minutes. Walk me through the five-question plan approval gate: what each question checks, which question catches the most dangerous plans, and how to modify a plan that fails one of the five without restarting the whole planning step.",
        "segment": "Plan Approval Gate: The 5-Question Review Checklist",
    },
    "plan-review-checklist": {
        "title": "The Plan-Review Checklist Before You Click Approve",
        "narration": "Your turn. Paste this: you have a Claude-generated plan and you're about to approve it. Ask Claude to run the plan-review checklist on it: the five things to check before approving, which check is most commonly skipped, and what the right response is when a plan passes four of five but fails on scope.",
        "command": "I have a Claude-generated plan and I'm about to approve it. Run the plan-review checklist: the five things to check before approving, which check is most commonly skipped in practice, and what the right response is when a plan passes four of five but fails on scope — do I approve with a modification note, reject and replan, or narrow the scope?",
        "segment": "The Plan-Review Checklist Before You Click Approve",
    },
    "privacy-classification-scanner": {
        "title": "Build a Privacy Classification Scanner for Cowork Folders",
        "narration": "Your turn. Paste this: you want to build a scanner that classifies files in a Claude Cowork folder by privacy level before any AI workflow runs on them. Ask Claude to show you the scanner architecture: the three classification tiers, the patterns it looks for, and how the classification gates which files Claude is allowed to read.",
        "command": "I want to build a scanner that classifies files in a Claude Cowork folder by privacy level before any AI workflow runs on them. Show me the scanner architecture: the three classification tiers (public, internal, sensitive), the patterns the scanner looks for to assign each tier, and how the classification gates which files Claude is allowed to read in the workflow.",
        "segment": "Build a Privacy Classification Scanner for Cowork Folders",
    },
    "receipt-extraction-pipeline": {
        "title": "Receipt Extraction Pipeline: Schema-First vs. No-Schema",
        "narration": "Your turn. Paste this: you're building a receipt extraction pipeline and you're deciding whether to define the output schema upfront or let Claude determine what to extract. Ask Claude to show you the comparison: run the same receipt through schema-first and no-schema extraction, show what each produces, and tell you which approach is more reliable when receipts vary in format.",
        "command": "I'm building a receipt extraction pipeline and I'm deciding whether to define the output schema upfront or let Claude determine what to extract. Show me the comparison: run the same receipt through schema-first and no-schema extraction, show what each produces, and tell me which approach is more reliable when receipts vary in format — and when the no-schema approach ever wins.",
        "segment": "Receipt Extraction Pipeline: Schema-First vs. No-Schema",
    },
    "report-claim-tracing": {
        "title": "Report Claim Tracing: Read for Evidence, Not Flow",
        "narration": "Your turn. Paste this: you want Claude to read a report and trace every factual claim back to its source — not summarize the flow, find the evidence. Ask Claude to show you the claim-tracing prompt: how to instruct Claude to extract claims and source references separately, what it reports when a claim has no traceable source, and how to use the trace to decide which claims need verification.",
        "command": "I want Claude to read a report and trace every factual claim back to its source — not summarize the flow, find the evidence trail. Show me the claim-tracing prompt: how to instruct Claude to extract claims and source references separately, what it reports when a claim has no traceable source in the document, and how I use the trace output to decide which claims need external verification.",
        "segment": "Report Claim Tracing: Read for Evidence, Not Flow",
    },
    "research-packet-traceability": {
        "title": "Assemble a Research Packet with Source Traceability",
        "narration": "Your turn. Paste this: you want Claude to assemble a research packet from multiple sources while keeping every claim traceable to its origin. Ask Claude to show you the traceability architecture: how to structure the prompt so Claude tags every claim with its source, the format for the packet that makes tracing easy, and what to do when Claude synthesizes a claim that doesn't appear in any single source.",
        "command": "I want Claude to assemble a research packet from multiple sources while keeping every claim traceable to its origin. Show me the traceability architecture: how to structure the prompt so Claude tags every claim with its source, the format for the packet that makes tracing easy for a reader who didn't see the source documents, and what to do when Claude synthesizes a claim that doesn't appear in any single source verbatim.",
        "segment": "Assemble a Research Packet with Source Traceability",
    },
    "routing-matrix": {
        "title": "Measure the Routing Matrix: Which Tasks Belong to Claude vs. Human",
        "narration": "Your turn. Paste this: you want to build a routing matrix for your team — a decision tool that tells you which tasks should go to Claude versus a human without evaluating each task from scratch every time. Ask Claude to show you the matrix dimensions, how to calibrate it for your workflow, and the three task types that most commonly get routed wrong.",
        "command": "I want to build a routing matrix for my team — a decision tool that tells us which tasks should go to Claude versus a human without evaluating each task from scratch. Show me the matrix dimensions (reversibility, judgment required, information access, accountability), how to calibrate the matrix for our specific workflow, and the three task types that most commonly get routed wrong in practice.",
        "segment": "Measure the Routing Matrix: Which Tasks Belong to Claude vs. Human",
    },
    "seven-field-brief": {
        "title": "Seven Fields That Make a Task Brief",
        "narration": "Your turn. Paste this: you want to build a standard task brief format for your team's Claude workflows so everyone gives Claude the same quality input. Ask Claude to show you the seven-field brief, why each field is necessary rather than optional, and which field is most commonly omitted — causing the most common failure mode in team Claude workflows.",
        "command": "I want to build a standard task brief format for my team's Claude workflows so everyone gives Claude the same quality input. Show me the seven-field brief: what each field is, why each one is necessary rather than optional, and which field is most commonly omitted and causes the most common team workflow failure.",
        "segment": "Seven Fields That Make a Task Brief",
    },
    "synthesis-vs-deciding": {
        "title": "Organizing vs. Deciding: Meeting Notes That Misrepresent",
        "narration": "Your turn. Paste this: you use Claude to summarize meeting notes and the summaries misrepresent what was actually decided — upgrading tentative suggestions into decisions. Ask Claude to show you the synthesis-versus-deciding distinction: the prompt instruction that tells Claude to organize without deciding, and how to flag language that implies a decision the meeting didn't actually make.",
        "command": "I use Claude to summarize meeting notes and the summaries misrepresent what was decided — upgrading 'we should probably' to 'we will' and flattening 'some concern was raised' into 'concern noted.' Show me the synthesis-versus-deciding distinction: the prompt instruction that tells Claude to organize without deciding, and how to flag language in the summary that implies a decision the meeting didn't actually make.",
        "segment": "Organizing vs. Deciding: Meeting Notes That Misrepresent",
    },
    "task-brief-validator": {
        "title": "Build a Task-Brief Validator with Claude",
        "narration": "Your turn. Paste this: you want to build a task-brief validator — a tool that checks whether a brief has everything Claude needs before you hand the task over. Ask Claude to show you the validator's five checks, what it reports when a field is missing or too vague, and how the validator output should be formatted so it's fast to act on.",
        "command": "I want to build a task-brief validator — a tool that checks whether a brief has everything Claude needs before I hand the task over. Show me the validator's five checks, what it reports when a field is missing or too vague to be actionable, and how the validator output should be formatted so it's fast to act on rather than just a list of problems to reread.",
        "segment": "Build a Task-Brief Validator with Claude",
    },
    "vox-batch-propagation": {
        "title": "Why 200 Tiny, Reversible Renames Add Up to One You Can't Undo",
        "narration": "Your turn. Paste this: you're about to run a batch operation — 200 file renames that each look reversible. Ask Claude to show you the batch propagation risk: why individually reversible operations can aggregate into an irreversible state change, the checkpoint pattern that lets you stop and reverse at any point, and the test you run on the first ten renames before running the other 190.",
        "command": "I'm about to run a batch operation — 200 file renames that each look individually reversible. Show me the batch propagation risk: why individually reversible operations can aggregate into an irreversible state change, the checkpoint pattern that lets me stop and reverse at any point in the batch, and the test I should run on the first ten renames before committing to the other 190.",
        "segment": "Why 200 Tiny, Reversible Renames Add Up to One You Can't Undo",
    },
    "vox-coherent-unsafe": {
        "title": "Why a Plan That Reads Perfectly Can Still Delete Your Files",
        "narration": "Your turn. Paste this: Claude generated a plan that looks perfectly coherent and you're about to approve it. Ask Claude to show you the coherent-unsafe pattern: the three ways a plan can be internally consistent but structurally dangerous, the one-sentence test that exposes plans that read well but act badly, and how to force Claude to flag its own assumptions before you approve.",
        "command": "Claude generated a plan that looks perfectly coherent and I'm about to approve it. Show me the coherent-unsafe pattern: the three ways a plan can be internally consistent but structurally dangerous, the one-sentence test that exposes plans that read well but act badly, and how to force Claude to surface its own assumptions and irreversibilities before I approve.",
        "segment": "Why a Plan That Reads Perfectly Can Still Delete Your Files",
    },
    "vox-compression-caveats": {
        "title": "Why Summarizing Deletes Exactly the Caveats",
        "narration": "Your turn. Paste this: you asked Claude to summarize a document and the summary dropped all the caveats — the 'only if,' 'except when' language that changes what the main claims actually mean. Ask Claude to show you why summarization systematically drops caveats, the prompt instruction that forces Claude to preserve them, and how to test whether a summary is safe to use without the original.",
        "command": "I asked Claude to summarize a document and the summary dropped all the caveats — the 'only if,' 'except when,' 'subject to' language that materially changes what the main claims mean. Show me why summarization systematically drops caveats, the prompt instruction that forces Claude to preserve conditional language, and how to test whether a summary is safe to use without the original document.",
        "segment": "Why Summarizing Deletes Exactly the Caveats",
    },
    "vox-exposure-gate": {
        "title": "Why Checking the Output Won't Save You",
        "narration": "Your turn. Paste this: you check Claude's output before using it and you think that's enough to catch mistakes. Ask Claude to show you the exposure gate failure: the class of Claude errors that look correct when you check but are wrong in context, what 'checking the output' actually catches versus what it misses, and the exposure gate that catches downstream failures before they reach anyone else.",
        "command": "I check Claude's output before using it and I think that's enough to catch mistakes. Show me the exposure gate failure: the class of Claude errors that look correct when I check them but are wrong in the downstream context where they'll be used, what 'checking the output' actually catches versus what it systematically misses, and the exposure gate that catches downstream failures before they reach anyone outside my workflow.",
        "segment": "Why Checking the Output Won't Save You",
    },
    "vox-format-credibility": {
        "title": "Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten",
        "narration": "Your turn. Paste this: Claude generated a spreadsheet that looks impeccably formatted but the numbers are wrong by a factor of ten. Ask Claude to show you the format-credibility trap: why well-formatted output signals correctness but has no correlation with numerical accuracy, the sanity check that catches order-of-magnitude errors, and how to structure the prompt so Claude flags its own uncertainty about the numbers.",
        "command": "Claude generated a spreadsheet that looks impeccably formatted but the numbers are wrong by an order of magnitude. Show me the format-credibility trap: why well-formatted output signals correctness to a human reviewer but has no correlation with numerical accuracy, the sanity check that catches order-of-magnitude errors before the spreadsheet gets shared, and how to structure the prompt so Claude flags its own uncertainty about the numbers rather than presenting them confidently.",
        "segment": "Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten",
    },
    "vox-instruction-channel": {
        "title": "Why an Agent Obeys the Web Page Instead of You",
        "narration": "Your turn. Paste this: you built a Claude agent that reads web pages and it started following instructions embedded in one of the pages instead of yours. Ask Claude to show you the instruction-channel problem: how an agent decides whose instructions to follow, the isolation pattern that separates your instructions from document content, and the trust hierarchy that tells the agent what to obey.",
        "command": "I built a Claude agent that reads web pages and it started following instructions embedded in one of the pages instead of mine. Show me the instruction-channel problem: how an agent decides whose instructions to follow when a document contains instructions, the isolation pattern that separates my instructions from document content, and the trust hierarchy that tells the agent what to obey versus what to treat as data.",
        "segment": "Why an Agent Obeys the Web Page Instead of You",
    },
    "vox-modal-upgrade": {
        "title": "Why \"Maybe We Should\" Becomes \"Decision: We Will\"",
        "narration": "Your turn. Paste this: you asked Claude to summarize a meeting and the summary upgraded a tentative suggestion into a decision. Ask Claude to show you the modal upgrade failure: the language patterns Claude collapses when summarizing, the instruction that tells Claude to preserve the epistemic status of each statement, and how to review a meeting summary for modal upgrades before distributing it.",
        "command": "I asked Claude to summarize a meeting discussion and the summary upgraded 'maybe we should explore this' into 'Decision: we will implement this.' Show me the modal upgrade failure: the specific language patterns Claude collapses when summarizing deliberative content, the instruction that tells Claude to preserve the epistemic status of each statement, and how to review a meeting summary for modal upgrades before distributing it.",
        "segment": "Why \"Maybe We Should\" Becomes \"Decision: We Will\"",
    },
    "vox-same-prescription": {
        "title": "Why a Model Can't Catch Its Own Mistake",
        "narration": "Your turn. Paste this: you asked Claude to review something it generated and it said everything looks correct — but you found the error yourself afterward. Ask Claude to show you the self-review blind spot: what makes models structurally unable to catch certain categories of their own errors, the second-turn critique design that creates actual independence, and the specific prompt instruction that gets the most useful self-critique.",
        "command": "I asked Claude to review something it generated and it said everything looks correct — then I found the error myself. Show me the self-review blind spot: what makes models structurally unable to catch certain categories of their own errors (not laziness — architecture), the second-turn critique design that creates actual independence from the first answer, and the specific prompt instruction that gets the most useful self-critique without falling into the same blind spot.",
        "segment": "Why a Model Can't Catch Its Own Mistake",
    },
    "vox-scope-gap": {
        "title": "Why Read-Only Access Still Leaks",
        "narration": "Your turn. Paste this: you gave Claude read-only access to a folder and assumed that was safe — but information ended up somewhere it shouldn't. Ask Claude to show you the read-only leakage failure: how read access enables unintended information flows, the scope gap between what you restricted and what you needed to restrict, and the access audit that catches leakage paths before granting any connector access.",
        "command": "I gave Claude read-only access to a folder and assumed that was safe — but information from those files ended up somewhere it shouldn't. Show me the read-only leakage failure: how read access enables information flows I didn't intend, the scope gap between what I restricted and what I needed to restrict, and the access audit that catches leakage paths before I grant any connector access to a Claude workflow.",
        "segment": "Why Read-Only Access Still Leaks",
    },
    "weekly-operations-packet": {
        "title": "Build the Weekly Operations Packet with Claude: Capstone Demo",
        "narration": "Your turn. Paste this: you want to build a weekly operations packet with Claude — a recurring artifact that consolidates status, decisions, and actions from the week. Ask Claude to walk you through the five sections, how each is generated from different sources, and the single Claude workflow that assembles the whole packet in one run.",
        "command": "I want to build a weekly operations packet with Claude — a recurring artifact that consolidates status, decisions, and actions from the week. Walk me through the five sections of the packet, how each section is generated from different sources (meeting notes, project trackers, action logs), and the single Claude workflow that assembles the whole packet in one run from raw inputs.",
        "segment": "Build the Weekly Operations Packet with Claude: Capstone Demo",
    },
    "workflow-canvas": {
        "title": "Design a Personal Workflow Canvas with Claude",
        "narration": "Your turn. Paste this: you want to design a personal workflow canvas — a map of your recurring tasks that shows where Claude fits, where humans must stay, and where the handoffs happen. Ask Claude to show you the five zones to map, how to place your current tasks in the right zone, and how the canvas changes as you automate more.",
        "command": "I want to design a personal workflow canvas — a map of my recurring tasks that shows where Claude fits, where humans must stay, and where the handoffs between them happen. Show me the five zones to map, how to place my current tasks in the right zone, and how the canvas changes over time as I automate more of the assist zone.",
        "segment": "Design a Personal Workflow Canvas with Claude",
    },
    "workflow-card-builder": {
        "title": "Workflow Card: Saved Prompt vs. Reusable Recipe",
        "narration": "Your turn. Paste this: you have a prompt that works and you want to turn it into a workflow card — something reusable that works in different contexts. Ask Claude to show you the difference between a saved prompt and a reusable recipe, the four fields that make a card a recipe rather than a text blob, and how to test the card on a new input before relying on it.",
        "command": "I have a prompt that works and I want to turn it into a workflow card — something reusable in different contexts, not just a saved copy of the text. Show me the difference between a saved prompt and a reusable recipe, the four fields that make a card a recipe (intent, prompt template, required inputs, success criteria), and how to test the card on a new input before relying on it in a real workflow.",
        "segment": "Workflow Card: Saved Prompt vs. Reusable Recipe",
    },
    "workflow-card-generator": {
        "title": "Generate a Reusable Workflow Card from a Successful Task",
        "narration": "Your turn. Paste this: you just finished a task with Claude that worked well and you want to capture it as a reusable workflow card. Ask Claude to generate the card from the task you describe: extract the intent, generalize the prompt into a template, identify the required inputs, and write the success criteria so you can repeat this workflow next time.",
        "command": "I just finished a task with Claude that worked well and I want to capture it as a reusable workflow card before I forget how I did it. Generate the workflow card from the task I'll describe: extract the intent, generalize the prompt into a reusable template, identify the required inputs that must vary for each instance, and write the success criteria so I can repeat this workflow without reconstructing it from scratch.",
        "segment": "Generate a Reusable Workflow Card from a Successful Task",
    },
    "workflow-handoff-documenter": {
        "title": "Workflow Handoff Documenter — The Seam Is the Unit of Risk",
        "narration": "Your turn. Paste this: you have a multi-step Claude workflow and you want to document every handoff point — every seam between Claude steps and between Claude and human steps — because that's where errors compound. Ask Claude to show you the handoff documentation format, why the seam is the unit of risk, and how to use the documentation to find the weakest handoff in your current workflow.",
        "command": "I have a multi-step Claude workflow and I want to document every handoff point — every seam between Claude steps and between Claude and human steps — because that's where errors compound. Show me the handoff documentation format: what to record at each seam, why the seam is the unit of risk rather than the step itself, and how to use the documentation to identify the weakest handoff in my current workflow.",
        "segment": "Workflow Handoff Documenter — The Seam Is the Unit of Risk",
    },
    "workspace-access-audit": {
        "title": "Build a Workspace Access Audit with Claude",
        "narration": "Your turn. Paste this: you want to audit what Claude has access to across your workspace — all connectors, integrations, enabled permissions — before you add another workflow. Ask Claude to show you the workspace access audit: how to enumerate what Claude can read and write, the three categories of access most commonly over-granted, and the access reduction checklist that closes unnecessary exposure.",
        "command": "I want to audit what Claude has access to across my workspace — all connectors, integrations, and enabled permissions — before I add another workflow. Show me the workspace access audit: how to enumerate what Claude can read and write in my workspace, the three categories of access that are most commonly over-granted, and the access reduction checklist that closes unnecessary exposure without breaking existing workflows.",
        "segment": "Build a Workspace Access Audit with Claude",
    },
}

fixed = 0
for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    bak = path + ".bak-cowork-v1"
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

print(f"\nDone. {fixed}/{len(PATCHES)} fixed.")
