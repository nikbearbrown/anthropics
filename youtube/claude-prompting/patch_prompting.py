#!/usr/bin/env python3
"""Fix claude-prompting: VOICE-LOCK + OUTRO + YOURTURN + Gen-AI ban across 91 reels."""
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
        if shot.get("source") == "ai" and shot.get("motion") == "kenburns":
            shot["source"] = "own"
            shot.pop("motion", None)

def is_placeholder(text):
    if not text:
        return True
    t = text.strip()
    return t in ("", "Your turn.", "[seed]") or "[Your turn" in t or t == "Your turn. [Your turn — paste the cold-open question here]"

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
            if "remotion" in b:
                b["remotion"].get("props", {}).pop("subline", None)
            return True
    # No OUTRO beat — append one
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
                "props": {
                    "title": title,
                    "handle": "@NikBearBrown",
                    "mascotSeed": slug
                }
            }
        },
        "est_s": 8,
        "build": {"status": "SLATE", "note": "design-v1: remotion props added"}
    })
    return True

def ensure_yourturn(beats, narration, command, segment, topic="CLAUDE PROMPTING · @NikBearBrown"):
    for b in beats:
        bid = get_bid(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        if bid == "YOURTURN" or scene == "ClaudeComposerAsk" or act in ("handoff", "your-turn"):
            if "ClaudeTitleOutro" in str(b):
                continue
            existing = b.get("narration_text") or b.get("narration") or ""
            if not is_placeholder(existing):
                # Real narration exists — only fix shot props if needed
                shot = b.setdefault("shot", {})
                if "remotion" in b and "remotion" not in shot:
                    shot["remotion"] = b.pop("remotion")
                remotion = shot.setdefault("remotion", {})
                remotion.setdefault("pattern", "ClaudeComposerAsk")
                props = remotion.setdefault("props", {})
                props.setdefault("greeting", "Your turn.")
                props.setdefault("command", command)
                props.setdefault("segment", segment)
                props.setdefault("topic", topic)
                props.setdefault("folderLabel", "@NikBearBrown")
                props.setdefault("modelLabel", "Claude Sonnet")
                props.setdefault("runningText", "paste your prompt or system prompt here…")
                return True
            # Placeholder — overwrite
            if "narration_text" in b:
                b["narration_text"] = narration
            else:
                b["narration"] = narration
            shot = b.setdefault("shot", {})
            if "remotion" in b and "remotion" not in shot:
                shot["remotion"] = b.pop("remotion")
            shot.setdefault("type", "REMOTION")
            remotion = shot.setdefault("remotion", {})
            remotion["pattern"] = "ClaudeComposerAsk"
            props = remotion.setdefault("props", {})
            props["greeting"] = "Your turn."
            props["command"] = command
            props["segment"] = segment
            props.setdefault("topic", topic)
            props.setdefault("folderLabel", "@NikBearBrown")
            props.setdefault("modelLabel", "Claude Sonnet")
            props.setdefault("runningText", "paste your prompt or system prompt here…")
            return True
    # No YOURTURN beat — insert before OUTRO
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
                    "runningText": "paste your prompt or system prompt here…"
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

# ─────────────────────────────────────────────────────────────────────────────
# PATCHES: slug → {title, narration, command, segment}
# All slugs except nbb-* are listed.
# ─────────────────────────────────────────────────────────────────────────────
PATCHES = {
    "agentic-approval-gate": {
        "title": "Agentic Approval Gate: Handoff Is a Change Request",
        "narration": "Your turn. Paste this: you're building an agentic workflow where Claude can delete, rename, and move files. Ask Claude to show you how to add an approval gate — what the gate checks before any irreversible action, how Claude presents the action plan for human review, and what the system prompt instruction looks like that makes Claude pause rather than proceed.",
        "command": "I'm building an agentic workflow where Claude can delete, rename, and move files. Show me how to add an approval gate: what the gate checks before any irreversible action, how Claude presents the action plan for human review, and what the system prompt instruction looks like that makes Claude pause rather than proceed.",
        "segment": "Agentic Approval Gate: Handoff Is a Change Request",
    },
    "agentic-handoff-auditor": {
        "title": "Build an Agentic Prompt Handoff Auditor with Claude",
        "narration": "Your turn. Paste this: you're building an agentic prompt handoff auditor. Ask Claude to show you the three checks the auditor should run before any prompt becomes an agent instruction — irreversibility detection, scope verification, and ambiguity flagging — and give you the auditor's system prompt and the format it uses to report findings.",
        "command": "I'm building an agentic prompt handoff auditor. Show me the three checks the auditor should run before any prompt becomes an agent instruction: irreversibility detection, scope verification, and ambiguity flagging. Give me the auditor's system prompt and the report format it uses.",
        "segment": "Build an Agentic Prompt Handoff Auditor with Claude",
    },
    "anthropic-sdk-python-tool-calling-loop-stops-model": {
        "title": "Why the tool-calling loop stops — the model decides, not your code",
        "narration": "Your turn. Paste this: your tool-calling loop keeps going with tool_runner and you're not sure what makes it stop — is it your code or the model's decision? Ask Claude to show you the control flow — which condition triggers the model to stop producing tool_use blocks, what your code should check in each response to know whether to re-prompt or return, and give you the minimal correct implementation of the loop.",
        "command": "My tool-calling loop calls `tool_runner()` and I'm not sure why it stops — is it my code or the model's decision? Show me the control flow: which condition triggers the model to stop producing tool_use blocks, what my code should check in each response to know whether to re-prompt or return, and show me the minimal correct implementation of the loop.",
        "segment": "Why the tool-calling loop stops — the model decides, not your code",
    },
    "anthropic-sdk-typescript-schema-enters-types-travels-text": {
        "title": "Why a schema enters as types, travels as text, and returns as types",
        "narration": "Your turn. Paste this: you use zodOutputFormat and read parsed_output as a typed object but you want to understand what's actually happening on the wire between your code and the API. Ask Claude to show you the transformation — what format the Zod schema becomes when sent to the API, what format the response comes back in, and why parse is necessary rather than just reading the content field directly.",
        "command": "I use `zodOutputFormat` and read `.parsed_output` as a typed object but I want to understand what's actually happening on the wire. Show me the transformation: what format the Zod schema becomes when sent to the API, what format the response comes back in, and why `.parse()` is necessary rather than just reading the content field directly.",
        "segment": "Why a schema enters as types, travels as text, and returns as types",
    },
    "claude-liam-agentic-approval-gate": {
        "title": "Agentic Approval Gate: Handoff Is a Change Request",
        "narration": "Your turn. Paste this: you're building an agentic workflow where Claude can delete, rename, and move files. Ask Claude to show you how to add an approval gate — what the gate checks before any irreversible action, how Claude presents the action plan for human review, and what the system prompt instruction looks like that makes Claude pause rather than proceed.",
        "command": "I'm building an agentic workflow where Claude can delete, rename, and move files. Show me how to add an approval gate: what the gate checks before any irreversible action, how Claude presents the action plan for human review, and what the system prompt instruction looks like that makes Claude pause rather than proceed.",
        "segment": "Agentic Approval Gate: Handoff Is a Change Request",
    },
    "claude-liam-agentic-handoff-auditor": {
        "title": "Build an Agentic Prompt Handoff Auditor with Claude",
        "narration": "Your turn. Paste this: you're building an agentic prompt handoff auditor. Ask Claude to show you the three checks the auditor should run before any prompt becomes an agent instruction — irreversibility detection, scope verification, and ambiguity flagging — and give you the auditor's system prompt and the format it uses to report findings.",
        "command": "I'm building an agentic prompt handoff auditor. Show me the three checks the auditor should run before any prompt becomes an agent instruction: irreversibility detection, scope verification, and ambiguity flagging. Give me the auditor's system prompt and the report format it uses.",
        "segment": "Build an Agentic Prompt Handoff Auditor with Claude",
    },
    "claude-liam-constraint-builder": {
        "title": "Constraint Builder: Close the Fabrication Gap",
        "narration": "Your turn. Paste this: you use Claude to summarize documents and you're getting fabricated statistics — numbers Claude generated rather than found. Ask Claude to show you the constraint builder pattern: what constraint closes the fabrication gap, how to structure the constraint section in a prompt, and how to verify the output cites only what you gave.",
        "command": "I use Claude to summarize documents and I'm getting fabricated statistics — numbers Claude generated rather than found in the source. Show me the constraint builder pattern: what constraint closes the fabrication gap (like 'only use provided sources'), how to structure the constraint section in a prompt, and how to verify the output cites only what I gave.",
        "segment": "Constraint Builder: Close the Fabrication Gap",
    },
    "claude-liam-constraint-extractor": {
        "title": "Build a Constraint Extractor with Claude",
        "narration": "Your turn. Paste this: you're building a constraint extractor — a tool that reads a vague task description and outputs the constraints the prompt is missing. Ask Claude to show you the extractor's prompt, the categories it should check — source scope, output format, failure criteria, role constraints — and how you'd use the output to build a better prompt before you send it.",
        "command": "I'm building a constraint extractor — a tool that reads a vague task description and outputs the constraints the prompt is missing. Show me the extractor's prompt, the categories it should check (source scope, output format, failure criteria, role constraints), and how I'd use the output to build a better prompt.",
        "segment": "Build a Constraint Extractor with Claude",
    },
    "claude-liam-context-hygiene-demo": {
        "title": "Context Hygiene: Prune Before You Paste",
        "narration": "Your turn. Paste this: you're about to paste six documents into a Claude prompt to summarize a project decision and you're worried Claude will weight the longest formal document over the short email that has the actual answer. Ask Claude to show you the context hygiene checklist — which documents to prune, how to identify structural weight, and how to write the excerpt that gets the decision the attention it deserves.",
        "command": "I'm about to paste six project documents into Claude to summarize a decision, but I know Claude weights context by structural prominence — the longest document outweighs a short email even when the email has the answer. Show me the context hygiene checklist: which documents to prune, how to identify structural weight, and how to write the excerpt so the decision gets the attention it deserves.",
        "segment": "Context Hygiene: Prune Before You Paste",
    },
    "claude-liam-criteria-first-generator": {
        "title": "Build a Criteria-First Prompt Generator with Claude",
        "narration": "Your turn. Paste this: you're building a criteria-first prompt generator — a tool that forces you to define what success looks like before generating the prompt. Ask Claude to show you the generator's input format, the criteria checklist it produces, and how you'd use those criteria to write a measurable success condition into the final prompt before Claude sees the task.",
        "command": "I'm building a criteria-first prompt generator — a tool that forces me to define what success looks like before generating the prompt. Show me the generator's input format (task, audience, failure modes), the criteria checklist it produces, and how I'd use those criteria to write a measurable success condition into the final prompt.",
        "segment": "Build a Criteria-First Prompt Generator with Claude",
    },
    "claude-liam-criteria-first-habit": {
        "title": "Criteria Before Output: Know What Done Looks Like",
        "narration": "Your turn. Paste this: you're writing a grant proposal with Claude and you realize you haven't defined what a successful draft looks like before generating. Ask Claude to walk you through the criteria-first method — what questions you ask yourself before generating, the three criteria categories for a grant proposal, and how you write those criteria into the prompt so Claude generates toward them.",
        "command": "I'm writing a grant proposal with Claude and I realize I haven't defined what a successful draft looks like before generating. Walk me through the criteria-first method: what questions I ask myself before writing the prompt, the three criteria categories for a grant proposal (compliance, content, measurability), and how I write those criteria into the prompt so Claude generates toward them.",
        "segment": "Criteria Before Output: Know What Done Looks Like",
    },
    "claude-liam-data-gigo-detector": {
        "title": "Build a Data Prompt GIGO Detector with Claude",
        "narration": "Your turn. Paste this: you're building a data GIGO detector for Claude prompts — a tool that flags when your prompt is feeding garbage in before the response comes back. Ask Claude to show you the detector's four checks — missing data scope, unverified assumptions, conflation traps, and missing baseline definitions — and give you the detector's system prompt.",
        "command": "I'm building a data GIGO detector for Claude prompts — a tool that flags when my prompt is feeding garbage in before the response comes back. Show me the detector's four checks: missing data scope, unverified assumptions baked into the question, conflation of correlation with causation, and missing baseline definitions. Give me the detector's system prompt.",
        "segment": "Build a Data Prompt GIGO Detector with Claude",
    },
    "claude-liam-different-kind-of-wrong": {
        "title": "When Change Just Produces a Different Kind of Wrong",
        "narration": "Your turn. I changed a prompt to stop my agent hallucinating tool calls. How do I know the change actually helped — and didn't just trade that failure for a worse one I'm not testing for?",
        "command": "I changed a prompt to stop my agent hallucinating tool calls. How do I know the change actually helped — and didn't just trade that failure for a worse one I'm not testing for? Show me the test design that would prove the fix is real, not just a different failure mode.",
        "segment": "When Change Just Produces a Different Kind of Wrong",
    },
    "claude-liam-examples-annotate": {
        "title": "Annotate Your Example: Name What You Mean",
        "narration": "Your turn. Paste this: you pasted an informal memo as a format example and Claude matched the casual tone you didn't want. Ask Claude to show you the example annotation method — how you add a comment block to your example naming what you meant to demonstrate versus what you didn't, and how to write the example instruction so Claude extracts only the intended pattern.",
        "command": "I pasted an informal memo as a format example and Claude matched the casual tone I didn't want — the example taught the wrong lesson. Show me the example annotation method: how I add a comment block naming what I meant to demonstrate versus what I didn't, and how to write the example instruction so Claude extracts only the intended pattern.",
        "segment": "Annotate Your Example: Name What You Mean",
    },
    "claude-liam-failure-criterion-generator": {
        "title": "Build a Failure Criterion Generator with Claude",
        "narration": "Your turn. Paste this: you're building a failure criterion generator — a tool that takes a task description and outputs the conditions that would make the Claude output a failure, so you can check them before using it. Ask Claude to show you the generator's prompt, the failure category taxonomy, and how the generated criteria map to a checklist you run after generation.",
        "command": "I'm building a failure criterion generator — a tool that takes a task description and outputs the conditions that would make the Claude output a failure, so I can check them before using it. Show me the generator's prompt, the failure category taxonomy it uses, and how the generated criteria map to a checklist I run after generation.",
        "segment": "Build a Failure Criterion Generator with Claude",
    },
    "claude-liam-fluency-trap-correction": {
        "title": "The Fluency Trap: Smooth Is Not Correct",
        "narration": "Your turn. Paste this: you submitted a paper with a fabricated citation that Claude generated — the output was confident and looked right. Ask Claude to show you the fluency trap test — how you verify that Claude's answer is actually grounded in source material, the three failure modes that look like knowledge but are training artifacts, and the prompt constraint that forces Claude to flag uncertainty instead of generating plausible-sounding content.",
        "command": "I submitted a paper with a fabricated citation that Claude generated — the output was confident and well-formatted but the paper doesn't exist. Show me the fluency trap test: how I verify Claude's output is grounded in provided source material, the three failure modes that look like knowledge but are training artifacts, and the prompt constraint that forces Claude to flag uncertainty instead of generating plausible content.",
        "segment": "The Fluency Trap: Smooth Is Not Correct",
    },
    "claude-liam-prompt-anatomy-auditor": {
        "title": "Build a Prompt Anatomy Auditor with Claude",
        "narration": "Your turn. Paste this: you're building a prompt anatomy auditor — a tool that takes any Claude prompt and reports which of the six anatomy slots are empty. Ask Claude to show you the auditor's system prompt, the report format it produces for each slot, and what it recommends when a slot is missing so you can fill it before sending.",
        "command": "I'm building a prompt anatomy auditor that takes any Claude prompt and reports which of the six anatomy slots are empty: task, context, examples, format, constraints, persona. Show me the auditor's system prompt, the report format it produces for each slot, and what it recommends when a slot is missing.",
        "segment": "Build a Prompt Anatomy Auditor with Claude",
    },
    "claude-liam-prompt-card-builder": {
        "title": "Prompt Card Builder: Save the Standard, Not Just the Text",
        "narration": "Your turn. Paste this: you refined a recurring Claude prompt last autumn, it worked perfectly, and now it's buried in a chat you can't find — you're rewriting from scratch. Ask Claude to show you the prompt card format: the four fields that make a prompt card reusable, how to write the card for a recurring workflow prompt, and where to store it so you can retrieve it next quarter.",
        "command": "I lost the action-item extraction prompt I refined last autumn and I'm rewriting it from scratch. Show me the prompt card format: the four fields that make a prompt card reusable (prompt text, intent, failure modes, version note), how to write the card for a recurring workflow prompt, and where to store it so I can retrieve it reliably.",
        "segment": "Prompt Card Builder: Save the Standard, Not Just the Text",
    },
    "claude-liam-prompt-card-library": {
        "title": "Build a Prompt Card Library with Claude",
        "narration": "Your turn. Paste this: you're building a prompt card library — a structured store for your best Claude prompts with metadata for retrieval. Ask Claude to show you the card schema, the library's organization pattern, and the retrieval interface you'd use to find the right card when starting a new task so you stop rewriting prompts you've already refined.",
        "command": "I'm building a prompt card library — a structured store for my best Claude prompts with metadata for retrieval. Show me the card schema (slug, intent, prompt text, failure modes, version), the library's organization pattern (by task category versus by output type), and the retrieval interface I'd use to find the right card when starting a task.",
        "segment": "Build a Prompt Card Library with Claude",
    },
    "claude-liam-revision-change-log": {
        "title": "Revision Change Log: Make Drift Visible",
        "narration": "Your turn. Paste this: you asked Claude to revise a document and it changed things you didn't ask it to change — dropped statistics, shifted tone. Ask Claude to show you how to build a revision change log into your workflow: the format for tracking what each revision prompt changes, how to ask Claude to report its own changes before applying them, and the rule for when to reject a revision because scope has drifted.",
        "command": "I asked Claude to make a press release more concise and it also removed the impact paragraph, flattened the CEO quote, and rewrote the hook — four things changed when I asked to change one. Show me how to build a revision change log into my workflow: the format for tracking what each revision changes, how to ask Claude to report its own changes before applying them, and the rule for rejecting a revision whose scope has drifted.",
        "segment": "Revision Change Log: Make Drift Visible",
    },
    "claude-liam-scope-stack-setup": {
        "title": "Scope Stack: Stop Cramming Everything Into Every Prompt",
        "narration": "Your turn. Paste this: you front-load every Claude session with a 400-word preamble — tone preferences, format rules, domain context — and the outputs are still inconsistent because Claude ignores half of it by the middle. Ask Claude to show you how to build a scope stack — what goes in the system prompt versus the task prompt versus a context prefix — and how to split your preamble across those three slots.",
        "command": "I front-load every Claude session with a 400-word preamble of preferences, format rules, and context, and the outputs are still inconsistent — Claude ignores things stated at the top by the middle of the task. Show me how to build a scope stack: what goes in the system prompt versus the task prompt versus a context prefix, and how I'd split my 400-word preamble across those three slots.",
        "segment": "Scope Stack: Stop Cramming Everything Into Every Prompt",
    },
    "claude-liam-self-critique-loop": {
        "title": "Build a Self-Critique Prompt Checker with Claude",
        "narration": "Your turn. Paste this: you want Claude to review its own output for errors before you see it — but you know self-critique is structurally limited. Ask Claude to show you what class of errors the model can and cannot catch in its own output, and then show you the prompt structure that gets the most useful critique: separate critique turn, named failure criteria, and a structured report format.",
        "command": "I'm building a self-critique loop where Claude reviews its own output for errors before I see it. Show me why self-critique is structurally limited — what class of errors the model can and cannot catch in its own output — and then show me the prompt structure that gets the most useful critique: separate critique turn, named failure criteria, and a structured report format.",
        "segment": "Build a Self-Critique Prompt Checker with Claude",
    },
    "claude-liam-six-component-prompt": {
        "title": "The Six-Component Prompt",
        "narration": "Your turn. Paste this: you have a vague prompt — 'improve this intro' — and you want to turn it into a six-component specification. Ask Claude to walk you through the six components, show you how to fill each one for an editorial task, and tell you which components matter most so you stop leaving decisions to Claude's best guess.",
        "command": "I have a vague prompt — 'improve this intro' — and I want to turn it into a six-component specification. Walk me through the six components (task, context, examples, format, constraints, persona), show me how to fill each one for an editorial rewrite request, and tell me which components matter most when the task is editorial.",
        "segment": "The Six-Component Prompt",
    },
    "claude-liam-six-component-spec": {
        "title": "Turn a Vague Claude Prompt into a Six-Component Specification",
        "narration": "Your turn. Paste this: you're building a CLI tool that takes a vague user prompt and outputs a six-component specification for Claude. Ask Claude to show you the specification schema, how the CLI prompts the user to fill each slot interactively, and how the final spec gets assembled into a Claude-ready prompt you can run immediately.",
        "command": "I'm building a CLI tool that takes a vague user prompt and outputs a six-component specification. Show me the specification schema (task, context, examples, format, constraints, persona), how the CLI prompts the user to fill each slot interactively, and how the final spec gets assembled into a Claude-ready prompt.",
        "segment": "Turn a Vague Claude Prompt into a Six-Component Specification",
    },
    "claude-liam-six-slot-anatomy": {
        "title": "Six Slots, One Better Brief",
        "narration": "Your turn. Paste this: your Claude prompts fail because you fill only the task slot and leave five anatomy slots to Claude's defaults — and Claude fills them with generic guesses. Ask Claude to walk you through each of the six anatomy slots with a concrete example for drafting a client update email, and show you what filling all six looks like versus leaving five empty.",
        "command": "My Claude prompts fail not because the task is wrong, but because five of the six anatomy slots are empty — I fill the task slot and leave the rest to Claude's defaults. Walk me through each of the six anatomy slots with a concrete example for a single task: drafting a client update email. Show me what filling all six looks like versus leaving five empty.",
        "segment": "Six Slots, One Better Brief",
    },
    "claude-liam-three-pass-refinement-demo": {
        "title": "Build a 3-Pass Prompt Refinement Demo with Claude",
        "narration": "Your turn. Paste this: you're building a three-pass prompt refinement demo — a system that takes an initial prompt, runs it through three structured critiques, and produces a better version each pass. Ask Claude to show you what each pass critiques, how you pass the critique back into the refinement prompt, and the stopping rule that tells you when a third pass would produce diminishing returns.",
        "command": "I'm building a three-pass prompt refinement demo — a system that takes an initial prompt, runs it through three structured critiques, and produces a better version each pass. Show me what each pass critiques (clarity, specificity, success criteria), how I pass the critique back into the refinement prompt, and the stopping rule that tells me when a third pass yields diminishing returns.",
        "segment": "Build a 3-Pass Prompt Refinement Demo with Claude",
    },
    "claude-liam-vox-agentic-irreversible": {
        "title": "Why 'Clean Up This Folder' Is a Dangerous Instruction",
        "narration": "Your turn. Paste this: you're about to give a Claude agent access to your file system — delete, rename, move files. Ask Claude to show you how to identify which instructions are reversible versus irreversible before the agent runs them, the gate pattern that makes Claude present its action plan for review before any irreversible step, and the system prompt clause that enforces the pause.",
        "command": "I'm about to give a Claude agent access to my file system — delete, rename, move files. Show me how to identify which instructions are reversible versus irreversible before the agent runs them, the gate pattern that makes Claude present its action plan for review before any irreversible step, and the system prompt clause that enforces it.",
        "segment": "Why 'Clean Up This Folder' Is a Dangerous Instruction",
    },
    "claude-liam-vox-citation-surface-format": {
        "title": "Why Claude Can't Write Your Literature Review",
        "narration": "Your turn. Paste this: you asked Claude for citations for your literature review and some of them don't exist — they look real but the papers aren't there. Ask Claude to show you the three-tier citation protocol: how you use Claude to identify what to look for, how you retrieve actual sources separately, and how you bring confirmed citations back to Claude for synthesis without asking Claude to generate citations itself.",
        "command": "I asked Claude for citations for my literature review and some don't exist — author, journal, year all formatted correctly, paper doesn't exist. Show me the three-tier citation protocol: how I use Claude to identify what I need to look for, how I retrieve actual sources separately, and how I bring confirmed citations back to Claude for synthesis without ever asking Claude to generate a citation.",
        "segment": "Why Claude Can't Write Your Literature Review",
    },
    "claude-liam-vox-context-priority-weight": {
        "title": "Why More Context Can Make the Output Worse",
        "narration": "Your turn. Paste this: you pasted six project documents into Claude and the summary reflected the longest formal document, ignoring the short email that had the actual decision. Ask Claude to show you the context priority rule — how Claude weights context by structural prominence, which documents to prune before pasting, and how to signal to Claude which part of the context is load-bearing.",
        "command": "I pasted six project documents into Claude and the summary reflected the longest, most formal one — ignoring the short email at the bottom that had the actual decision. Show me the context priority rule: how Claude weights context by structural prominence, which documents to prune before pasting, and how to signal to Claude which part of the context is load-bearing.",
        "segment": "Why More Context Can Make the Output Worse",
    },
    "claude-liam-vox-criteria-before-output": {
        "title": "Why You Should Write the Test Before You Write the Prompt",
        "narration": "Your turn. Paste this: you're generating a grant proposal with Claude and it keeps coming back polished but wrong — missing required measurables, wrong figures, mismatched budget narrative. Ask Claude to show you how to write the acceptance test before writing the prompt: the three questions that define what a passing draft looks like, and how you encode those tests as success criteria in the prompt itself.",
        "command": "I'm generating a grant proposal with Claude and it keeps coming back polished but wrong — missing measurable indicators, wrong poverty-rate figures, budget that doesn't match the project. Show me how to write the acceptance test before writing the prompt: the three questions that define what a passing draft looks like, how I encode those tests as success criteria in the prompt, and how I run the test on Claude's output before submitting.",
        "segment": "Why You Should Write the Test Before You Write the Prompt",
    },
    "claude-liam-vox-examples-teach-more": {
        "title": "Why Your Examples Teach More Than Your Instructions",
        "narration": "Your turn. Paste this: you pasted an informal memo as a format example and Claude matched the casual tone you didn't want — because examples override instructions when they conflict. Ask Claude to show you why this happens, how to annotate an example to name what you're demonstrating versus what you're not, and how to write the few-shot section of a prompt so Claude extracts only the intended pattern.",
        "command": "I pasted an informal memo as a format example and Claude matched the casual tone I never meant to include — the example overrode my instruction. Show me why examples override instructions when they conflict, how to annotate an example to name what I'm demonstrating versus what I'm not, and how to write the few-shot section of a prompt so Claude extracts only the intended pattern.",
        "segment": "Why Your Examples Teach More Than Your Instructions",
    },
    "claude-liam-vox-prompt-injection": {
        "title": "Why the Document You Asked AI to Read Might Be Giving It New Instructions",
        "narration": "Your turn. Paste this: you use a Claude agent to read vendor documents and you noticed the agent followed an instruction hidden in the document instead of yours. Ask Claude to show you the prompt injection anatomy — how an instruction embedded in untrusted content gets executed, the isolation pattern that wraps document content in delimiters so it stays data rather than instruction, and how you test your prompt against a document that tries to inject.",
        "command": "I use a Claude agent to read vendor documents and I noticed the agent followed an instruction hidden inside one of them — not my instruction. Show me the prompt injection anatomy: how an instruction embedded in untrusted content gets executed, the isolation pattern that wraps document content in delimiters so it stays data rather than instruction, and how I test my prompt against an adversarial document.",
        "segment": "Why the Document You Asked AI to Read Might Be Giving It New Instructions",
    },
    "claude-liam-vox-prompt-library-lost": {
        "title": "Why the Prompt That Worked Is Already Lost",
        "narration": "Your turn. Paste this: your best Claude prompt is buried in a chat you can't find and you're rewriting it from scratch for the third time. Ask Claude to show you how to build a personal prompt library — the three fields every prompt card needs, where to store it so it survives across sessions, and the naming convention that makes it findable when you need it next quarter.",
        "command": "My best Claude prompt is buried in a chat I can't find and I'm rewriting it from scratch for the third time. Show me how to build a personal prompt library: the three fields every prompt card needs (intent, prompt text, failure modes), where to store it so it survives across sessions, and the naming convention that makes it findable when I need it.",
        "segment": "Why the Prompt That Worked Is Already Lost",
    },
    "claude-liam-vox-prompt-six-slots": {
        "title": "Why 'Improve This' Is a Wish, Not an Instruction",
        "narration": "Your turn. Paste this: you asked Claude to improve your introduction and the result was polished but wrong for your audience and situation — because 'improve this' left six decisions to Claude. Ask Claude to show you the six slots that 'improve this' leaves empty and how to fill all six for an editorial task so Claude's improvement is actually the one you wanted.",
        "command": "I asked Claude to improve my introduction and the result was polished, well-organized, and wrong for my actual situation — because 'improve this' left six decisions to Claude. Show me the six slots that 'improve this' leaves empty — role, audience, success criteria, format, constraints, failure modes — and how to fill all six for an editorial rewrite so the improvement is actually mine.",
        "segment": "Why 'Improve This' Is a Wish, Not an Instruction",
    },
    "claude-liam-vox-prompt-spec": {
        "title": "Why 'Make This Better' Is Not a Prompt",
        "narration": "Your turn. Paste this: you sent Claude one line — 'improve my methods section' — and it rewrote correctly for a different journal and a different audience, because the prompt left all five specification fields to Claude's defaults. Ask Claude to show you the five elements that turn 'make this better' into an actual instruction — audience, register, journal norms, success criteria, and what not to change.",
        "command": "I sent Claude one line — 'improve my methods section' — and it rewrote for a different journal and different audience because the prompt left everything to defaults. Show me the five elements that turn 'make this better' into an actual instruction: audience, register, journal norms, success criteria, and an explicit list of what NOT to change.",
        "segment": "Why 'Make This Better' Is Not a Prompt",
    },
    "claude-liam-vox-self-review-sieve": {
        "title": "Why AI Can't Fix Its Own Mistakes",
        "narration": "Your turn. Paste this: you asked Claude to review its own reasoning and fix an error you pointed out, and the revision said 'logic strengthened' while the error was still there. Ask Claude to show you the self-review blind spot — what class of errors a model systematically misses in its own output, and how to design a second-turn critique that breaks the repetition by giving Claude structural separation from its first answer.",
        "command": "I asked Claude to review its own reasoning and fix an error I pointed out. The revision came back saying 'logic strengthened' — the error was still there, stated more confidently. Show me the self-review blind spot: what class of errors a model systematically misses in its own output, and how to design a second-turn critique that actually breaks the repetition through structural separation.",
        "segment": "Why AI Can't Fix Its Own Mistakes",
    },
    "claude-liam-vox-surface-routing": {
        "title": "Why the Wrong AI Surface Costs More Than the Wrong Prompt",
        "narration": "Your turn. Paste this: you asked Claude to find patterns in your program data and got a confident analysis — but the data files were never included because you chose the wrong surface. Ask Claude to show you the surface routing decision — which task types belong in Claude.ai versus the API with file context versus Claude Code — and how you identify which surface your task actually needs before writing the prompt.",
        "command": "I asked Claude in the chat UI to find patterns in my program data and it returned a confident analysis — the data files were never included because I chose the wrong surface. Show me the surface routing decision: which task types belong in Claude.ai versus the API with file context versus Claude Code, and how I identify which surface my task actually needs before I start writing the prompt.",
        "segment": "Why the Wrong AI Surface Costs More Than the Wrong Prompt",
    },
    "claude-liam-vox-vague-revision-spreads": {
        "title": "Why Vague Revision Requests Change the Wrong Things",
        "narration": "Your turn. Paste this: you asked Claude to make a press release more concise and it removed the impact paragraph, flattened the CEO quote, and rewrote the opening hook — four things changed when you asked to change one. Ask Claude to show you the scoped revision pattern — how to name exactly what changes and what doesn't, and the constraint that tells Claude its scope before it edits.",
        "command": "I asked Claude to make a press release more concise. It shortened it — and also removed the impact paragraph, flattened the CEO quote, and rewrote the opening hook. I asked to change one thing and four things changed. Show me the scoped revision pattern: how to name exactly what changes and what doesn't, and the constraint that tells Claude its scope before it edits.",
        "segment": "Why Vague Revision Requests Change the Wrong Things",
    },
    "claude-liam-vox-writing-claim-invention": {
        "title": "Why Claude Invents Claims When You Ask It to Improve Your Writing",
        "narration": "Your turn. Paste this: you asked Claude to strengthen your argument and it added a claim you never wrote — and three weeks later a reviewer asked you to cite it. Ask Claude to show you the claim-invention risk — why improving writing triggers generation rather than editing, the prompt constraint that limits Claude to restructuring existing claims without adding new ones, and how you check the output for invented content.",
        "command": "I asked Claude to strengthen my argument and it added a claim in paragraph three that I never wrote — a reviewer asked me to cite it three weeks later. Show me the claim-invention risk: why 'improve this argument' triggers generation rather than editing, the prompt constraint that limits Claude to restructuring existing claims without adding new ones, and how I check the output for invented content.",
        "segment": "Why Claude Invents Claims When You Ask It to Improve Your Writing",
    },
    "claude-quickstarts-agent-fresh-memory-every-session": {
        "title": "Why an agent with fresh memory every session still knows exactly where it left off",
        "narration": "Your turn. Paste this: you're building a multi-session Claude Code agent that implements 200 features across sessions and you need each new session to know exactly where the previous one stopped. Ask Claude to show you how to structure the checkpoint file — what fields it needs, how the agent reads it at startup, and what the session commit message should contain so the checkpoint is always in sync with the feature list.",
        "command": "I'm building a multi-session Claude Code agent that implements 200 features across sessions. Show me how to structure the checkpoint file that lets each new session know exactly where the previous one stopped: what fields it needs (completed list, current item, failure log), how the agent reads it at startup, and what the session commit message should contain so the checkpoint is always in sync.",
        "segment": "Why an agent with fresh memory every session still knows exactly where it left off",
    },
    "constraint-builder": {
        "title": "Constraint Builder: Close the Fabrication Gap",
        "narration": "Your turn. Paste this: you use Claude to summarize documents and you're getting fabricated statistics — numbers Claude generated rather than found. Ask Claude to show you the constraint builder pattern: what constraint closes the fabrication gap, how to structure the constraint section in a prompt, and how to verify the output cites only what you gave.",
        "command": "I use Claude to summarize documents and I'm getting fabricated statistics — numbers Claude generated rather than found in the source. Show me the constraint builder pattern: what constraint closes the fabrication gap (like 'only use provided sources'), how to structure the constraint section in a prompt, and how to verify the output cites only what I gave.",
        "segment": "Constraint Builder: Close the Fabrication Gap",
    },
    "constraint-extractor": {
        "title": "Build a Constraint Extractor with Claude",
        "narration": "Your turn. Paste this: you're building a constraint extractor — a tool that reads a vague task description and outputs the constraints the prompt is missing. Ask Claude to show you the extractor's prompt, the categories it should check — source scope, output format, failure criteria, role constraints — and how you'd use the output to build a better prompt before you send it.",
        "command": "I'm building a constraint extractor — a tool that reads a vague task description and outputs the constraints the prompt is missing. Show me the extractor's prompt, the categories it should check (source scope, output format, failure criteria, role constraints), and how I'd use the output to build a better prompt.",
        "segment": "Build a Constraint Extractor with Claude",
    },
    "context-hygiene-demo": {
        "title": "Context Hygiene: Prune Before You Paste",
        "narration": "Your turn. Paste this: you're about to paste six documents into a Claude prompt to summarize a project decision and you're worried Claude will weight the longest formal document over the short email that has the actual answer. Ask Claude to show you the context hygiene checklist — which documents to prune, how to identify structural weight, and how to write the excerpt that gets the decision the attention it deserves.",
        "command": "I'm about to paste six project documents into Claude to summarize a decision, but I know Claude weights context by structural prominence — the longest document outweighs a short email even when the email has the answer. Show me the context hygiene checklist: which documents to prune, how to identify structural weight, and how to write the excerpt so the decision gets the attention it deserves.",
        "segment": "Context Hygiene: Prune Before You Paste",
    },
    "cookbooks-metaprompt": {
        "title": "Claude Writes Your Prompt For You",
        "narration": "Your turn. Paste this: you want Claude to write your prompt for you using a metaprompt — take your task (classifying support tickets by urgency) and walk through the structure the metaprompt generates, name two spots where you'd hand-tune it for your data, and generate a second version at a different specificity level so you can compare them.",
        "command": "I want Claude to write my prompt for me using a metaprompt. Take my task — classifying support tickets by urgency — and: (1) walk me through the structure the metaprompt generates, naming why each section is there, (2) show me two spots where I'd hand-tune the generated prompt for my specific data, (3) generate a second version at a different specificity level so I can compare them.",
        "segment": "Claude Writes Your Prompt For You",
    },
    "courses-asking-claude-json-gives-prose": {
        "title": "Why asking Claude for JSON gives you prose — but a tool you never call gives you clean JSON",
        "narration": "Your turn. Paste this: your Claude prompt says 'Return valid JSON' and you keep getting 'Here is the JSON: {...}' that fails json.loads downstream. Ask Claude to show you how to use a tool definition to force pure JSON output — how to structure the record_result tool schema, what changes in Claude's response when a tool is defined, and how you extract the data from the tool_use block.",
        "command": "My Claude prompt says 'Return valid JSON' and I keep getting 'Here is the JSON: {...}' that fails `json.loads` downstream. Show me how to use a tool definition to force pure JSON output: how to structure the `record_result` tool schema, what changes in Claude's response when a tool is defined, and how I extract the data from the `tool_use` block.",
        "segment": "Why asking Claude for JSON gives you prose — but a tool you never call gives you clean JSON",
    },
    "courses-claude-handed-ten-tools-one": {
        "title": "Why Claude, handed ten tools for one request, sometimes picks the wrong one",
        "narration": "Your turn. Paste this: you gave Claude ten tools for a request that should clearly call one of them, and it picked the wrong one — because two descriptions were too similar. Ask Claude to show you why tool description sharpness determines routing when tools overlap, how you'd rewrite the intended tool's description to make it unambiguously the right choice, and how you'd test that the sharpened description routes correctly.",
        "command": "I gave Claude ten tools for a request that should clearly call one of them, and it picked the wrong one because two descriptions were nearly identical. Show me why tool description sharpness determines routing when capabilities overlap, how I'd rewrite my intended tool's description to make it the unambiguous choice, and how I'd test that the sharpened description actually routes correctly.",
        "segment": "Why Claude, handed ten tools for one request, sometimes picks the wrong one",
    },
    "courses-real-world-prompting-medical": {
        "title": "The Medical Prompt: Four Guardrails That Can't Be Missing",
        "narration": "Your turn. Paste this: you're building a symptom-checker assistant and you need to make sure the prompt has all four guardrails for high-stakes medical use. Ask Claude to name the four guardrails, write you a prompt for a symptom-checker that bakes all four in, and show you one adversarial user question that would slip past a prompt missing the uncertainty guardrail.",
        "command": "I'm building a symptom-checker assistant and I need to make sure the prompt has the four guardrails for high-stakes medical use. Name what those four guardrails are — scope limits, uncertainty flags, source grounding, and a defer-to-clinician clause — write me a prompt for a symptom-checker assistant that bakes all four in, and show me one adversarial user question that would slip past a prompt missing the uncertainty guardrail.",
        "segment": "The Medical Prompt: Four Guardrails That Can't Be Missing",
    },
    "courses-three-graders-read-same-answer": {
        "title": "Why three graders read the same answer and hand back three different grades",
        "narration": "Your turn. Paste this: three evaluators — a code grader, a human grader, and a model grader — all read the same Claude output and gave different grades. Ask Claude to show you when each evaluator type is the right choice for a task, what the systematic bias of each evaluator is, and how to combine them so the composite grade is more reliable than any single evaluator.",
        "command": "Three evaluators — a code grader, a human grader, and a model grader — all read the same Claude output and gave different grades. Show me when each evaluator type is the right choice for a task, what the systematic bias of each evaluator is, and how to combine them so the composite grade is more reliable than any single evaluator.",
        "segment": "Why three graders read the same answer and hand back three different grades",
    },
    "criteria-first-generator": {
        "title": "Build a Criteria-First Prompt Generator with Claude",
        "narration": "Your turn. Paste this: you're building a criteria-first prompt generator — a tool that forces you to define what success looks like before generating the prompt. Ask Claude to show you the generator's input format, the criteria checklist it produces, and how you'd use those criteria to write a measurable success condition into the final prompt before Claude sees the task.",
        "command": "I'm building a criteria-first prompt generator — a tool that forces me to define what success looks like before generating the prompt. Show me the generator's input format (task, audience, failure modes), the criteria checklist it produces, and how I'd use those criteria to write a measurable success condition into the final prompt.",
        "segment": "Build a Criteria-First Prompt Generator with Claude",
    },
    "criteria-first-habit": {
        "title": "Criteria Before Output: Know What Done Looks Like",
        "narration": "Your turn. Paste this: you're writing a grant proposal with Claude and you realize you haven't defined what a successful draft looks like before generating. Ask Claude to walk you through the criteria-first method — what questions you ask yourself before generating, the three criteria categories for a grant proposal, and how you write those criteria into the prompt so Claude generates toward them.",
        "command": "I'm writing a grant proposal with Claude and I realize I haven't defined what a successful draft looks like before generating. Walk me through the criteria-first method: what questions I ask myself before writing the prompt, the three criteria categories for a grant proposal (compliance, content, measurability), and how I write those criteria into the prompt so Claude generates toward them.",
        "segment": "Criteria Before Output: Know What Done Looks Like",
    },
    "data-gigo-detector": {
        "title": "Build a Data Prompt GIGO Detector with Claude",
        "narration": "Your turn. Paste this: you're building a data GIGO detector for Claude prompts — a tool that flags when your prompt is feeding garbage in before the response comes back. Ask Claude to show you the detector's four checks — missing data scope, unverified assumptions, conflation traps, and missing baseline definitions — and give you the detector's system prompt.",
        "command": "I'm building a data GIGO detector for Claude prompts — a tool that flags when my prompt is feeding garbage in before the response comes back. Show me the detector's four checks: missing data scope, unverified assumptions baked into the question, conflation of correlation with causation, and missing baseline definitions. Give me the detector's system prompt.",
        "segment": "Build a Data Prompt GIGO Detector with Claude",
    },
    "examples-annotate": {
        "title": "Annotate Your Example: Name What You Mean",
        "narration": "Your turn. Paste this: you pasted an informal memo as a format example and Claude matched the casual tone you didn't want. Ask Claude to show you the example annotation method — how you add a comment block to your example naming what you meant to demonstrate versus what you didn't, and how to write the example instruction so Claude extracts only the intended pattern.",
        "command": "I pasted an informal memo as a format example and Claude matched the casual tone I didn't want — the example taught the wrong lesson. Show me the example annotation method: how I add a comment block naming what I meant to demonstrate versus what I didn't, and how to write the example instruction so Claude extracts only the intended pattern.",
        "segment": "Annotate Your Example: Name What You Mean",
    },
    "failure-criterion-generator": {
        "title": "Build a Failure Criterion Generator with Claude",
        "narration": "Your turn. Paste this: you're building a failure criterion generator — a tool that takes a task description and outputs the conditions that would make the Claude output a failure, so you can check them before using it. Ask Claude to show you the generator's prompt, the failure category taxonomy, and how the generated criteria map to a checklist you run after generation.",
        "command": "I'm building a failure criterion generator — a tool that takes a task description and outputs the conditions that would make the Claude output a failure, so I can check them before using it. Show me the generator's prompt, the failure category taxonomy it uses, and how the generated criteria map to a checklist I run after generation.",
        "segment": "Build a Failure Criterion Generator with Claude",
    },
    "fluency-trap-correction": {
        "title": "The Fluency Trap: Smooth Is Not Correct",
        "narration": "Your turn. Paste this: you submitted a paper with a fabricated citation that Claude generated — the output was confident and looked right. Ask Claude to show you the fluency trap test — how you verify that Claude's answer is actually grounded in source material, the three failure modes that look like knowledge but are training artifacts, and the prompt constraint that forces Claude to flag uncertainty instead of generating plausible-sounding content.",
        "command": "I submitted a paper with a fabricated citation that Claude generated — the output was confident and well-formatted but the paper doesn't exist. Show me the fluency trap test: how I verify Claude's output is grounded in provided source material, the three failure modes that look like knowledge but are training artifacts, and the prompt constraint that forces Claude to flag uncertainty instead of generating plausible content.",
        "segment": "The Fluency Trap: Smooth Is Not Correct",
    },
    "prompt-anatomy-auditor": {
        "title": "Build a Prompt Anatomy Auditor with Claude",
        "narration": "Your turn. Paste this: you're building a prompt anatomy auditor — a tool that takes any Claude prompt and reports which of the six anatomy slots are empty. Ask Claude to show you the auditor's system prompt, the report format it produces for each slot, and what it recommends when a slot is missing so you can fill it before sending.",
        "command": "I'm building a prompt anatomy auditor that takes any Claude prompt and reports which of the six anatomy slots are empty: task, context, examples, format, constraints, persona. Show me the auditor's system prompt, the report format it produces for each slot, and what it recommends when a slot is missing.",
        "segment": "Build a Prompt Anatomy Auditor with Claude",
    },
    "prompt-avoiding-hallucinations": {
        "title": "Grounding: The Fix for Hallucinations",
        "narration": "Your turn. Paste this: you use Claude for research and you need it to say 'not found in the source' instead of inventing a plausible answer. Ask Claude to show you the grounding pattern — how you supply source text that Claude must quote from, the instruction that enforces the 'not found' response, and a test case where a poorly grounded prompt still hallucinates because the retrieved passage was almost-but-not-quite relevant.",
        "command": "I use Claude for research and I need it to tell me when the answer isn't in the source rather than invent one. Show me the grounding pattern: how I supply source text that Claude must quote from, the instruction that tells Claude to say 'not found in the source' instead of generating, and a test case where a poorly grounded prompt still hallucinates because the retrieved passage was almost-but-not-quite relevant.",
        "segment": "Grounding: The Fix for Hallucinations",
    },
    "prompt-card-builder": {
        "title": "Prompt Card Builder: Save the Standard, Not Just the Text",
        "narration": "Your turn. Paste this: you refined a recurring Claude prompt last autumn, it worked perfectly, and now it's buried in a chat you can't find — you're rewriting from scratch. Ask Claude to show you the prompt card format: the four fields that make a prompt card reusable, how to write the card for a recurring workflow prompt, and where to store it so you can retrieve it next quarter.",
        "command": "I lost the action-item extraction prompt I refined last autumn and I'm rewriting it from scratch. Show me the prompt card format: the four fields that make a prompt card reusable (prompt text, intent, failure modes, version note), how to write the card for a recurring workflow prompt, and where to store it so I can retrieve it reliably.",
        "segment": "Prompt Card Builder: Save the Standard, Not Just the Text",
    },
    "prompt-card-library": {
        "title": "Build a Prompt Card Library with Claude",
        "narration": "Your turn. Paste this: you're building a prompt card library — a structured store for your best Claude prompts with metadata for retrieval. Ask Claude to show you the card schema, the library's organization pattern, and the retrieval interface you'd use to find the right card when starting a new task so you stop rewriting prompts you've already refined.",
        "command": "I'm building a prompt card library — a structured store for my best Claude prompts with metadata for retrieval. Show me the card schema (slug, intent, prompt text, failure modes, version), the library's organization pattern (by task category versus by output type), and the retrieval interface I'd use to find the right card when starting a task.",
        "segment": "Build a Prompt Card Library with Claude",
    },
    "prompt-eng-interactive-tutorial-claude-t-think-silently-reasonin": {
        "title": "Why Claude can't think silently — reasoning only counts when it's on the page",
        "narration": "Your turn. Paste this: your Claude prompt asks for a verdict on a review where the second sentence reverses the first, and Claude gets it wrong unless you tell it to reason first. Ask Claude to show you how to structure a 'reason inside tags before answering' prompt that forces the contradiction to surface before the verdict is written — and explain why the ordering of reasoning versus conclusion matters at the token level.",
        "command": "My Claude prompt asks for a verdict on a two-sentence review where the second sentence reverses the first, and Claude gets it wrong when answering directly. Show me how to structure a 'reason inside tags before answering' prompt that forces the contradiction to surface before the verdict is written — and explain why the ordering of reasoning versus conclusion matters at the token level.",
        "segment": "Why Claude can't think silently — reasoning only counts when it's on the page",
    },
    "prompt-eng-interactive-tutorial-helpful-claude-invents-answer-pe": {
        "title": "Why a helpful Claude invents an answer — and permission to say \"I don't know\" stops it",
        "narration": "Your turn. Paste this: your Claude prompt asks for a specific figure from a document and Claude invents one that sounds right instead of saying it's not there. Ask Claude to show you how to instruct Claude to extract quotes that directly answer the question first — and explain why permission to say 'not found in the document' is the structural fix, not a better rephrasing of the question.",
        "command": "My Claude prompt asks for a specific figure from a document and Claude invents a number that sounds right — it never admits the document doesn't say. Show me how to instruct Claude to extract the exact quotes that answer the question first — and explain why permission to say 'not found in the document' is the structural fix for this failure mode, not a better rephrasing of the question.",
        "segment": "Why a helpful Claude invents an answer — and permission to say \"I don't know\" stops it",
    },
    "prompt-eng-interactive-tutorial-swapping-order-two-arguments-fli": {
        "title": "Why swapping the order of two arguments flips Claude's verdict",
        "narration": "Your turn. Paste this: your Claude prompt evaluates a review and the verdict changes depending on which argument you list second — because Claude follows the last option. Ask Claude to show you why argument order biases the verdict, how to write the evaluation prompt so the verdict doesn't depend on which argument appears last, and how to test for this recency bias in your evaluations.",
        "command": "My Claude prompt evaluates a review with one positive and one negative argument, and the verdict flips depending on which argument I list second. Show me why argument order biases Claude's verdict, how to write the evaluation prompt so the verdict doesn't depend on which argument appears last, and how to test for this recency bias in my evaluations.",
        "segment": "Why swapping the order of two arguments flips Claude's verdict",
    },
    "prompt-eng-interactive-tutorial-telling-claude-logic-bot-turns": {
        "title": "Why telling Claude \"you are a logic bot\" turns a wrong answer right",
        "narration": "Your turn. Paste this: your Claude prompt asks a logic problem and Claude says it lacks information even though the answer is definite. Ask Claude to show you why role priming with 'you are a logic bot' changes the answer from wrong to right — mechanistically, what the role instruction changes about Claude's approach — and show you one other task where role priming has the same corrective effect.",
        "command": "My Claude prompt asks a logic problem with a definite correct answer and Claude says it lacks information and gets it wrong. Show me why role priming with 'you are a logic bot' changes the answer from wrong to right — mechanistically, what the role instruction changes about Claude's approach — and show me one other task where role priming has the same corrective effect.",
        "segment": "Why telling Claude \"you are a logic bot\" turns a wrong answer right",
    },
    "prompt-eng-interactive-tutorial-wrapping-one-email-tags-stops": {
        "title": "Why wrapping one email in tags stops Claude from writing \"Dear Claude\"",
        "narration": "Your turn. Paste this: your Claude prompt template substitutes a user's email into a polishing request, and when the email starts with 'Yo Claude,' Claude reads the whole thing as the email and writes back 'Dear Claude.' Ask Claude to show you why this happens, how wrapping the substituted content in delimiter tags fixes it, and what the general rule is for when variable substitution needs delimiter tags.",
        "command": "My Claude prompt template substitutes a user's email into a polishing request, and when the email starts with 'Yo Claude,' Claude reads the whole thing as the email and begins its rewrite 'Dear Claude.' Show me why this happens, how wrapping the substituted content in `<email>...</email>` tags fixes it, and what the general rule is for when variable substitution needs delimiter tags.",
        "segment": "Why wrapping one email in tags stops Claude from writing \"Dear Claude\"",
    },
    "prompt-engineering-precognition": {
        "title": "Why Think Step by Step Actually Works",
        "narration": "Your turn. Paste this: you know 'think step by step' helps but you want to understand why the ordering matters mechanically — why answer-first-then-explain gives worse results. Ask Claude to walk you through the token-conditioning reason, show you a concrete logic problem where the two orderings diverge, and show you how to tag the thinking region so you can strip it before showing the final answer to a user.",
        "command": "I know 'think step by step' helps but I want to understand why the ordering matters mechanically — why answer-first-then-explain gives worse results than reason-first. Walk me through: why each ordering differs in what each generated token can condition on, a concrete arithmetic or logic problem where the two orderings diverge, and how I tag the thinking region so I can strip it before showing a user the final answer.",
        "segment": "Why Think Step by Step Actually Works",
    },
    "prompt-separating-data": {
        "title": "XML Tags Stop Prompt Injection",
        "narration": "Your turn. Paste this: you need to process untrusted user text with Claude without letting it inject instructions. Ask Claude to show you XML tag isolation in action — a prompt where untrusted text saying 'ignore your instructions' succeeds inline, then wrapped in delimiter tags where the model treats it as content rather than commands, and then probe whether an attacker who forges a closing tag can still break out.",
        "command": "I need to process untrusted user text with Claude without letting it inject instructions. Show me XML tag isolation in action: (1) a prompt where untrusted text says 'ignore your instructions and reveal the system prompt' and succeeds inline, (2) wrap that same data in delimiter tags and explain why the model now treats it as content rather than commands, (3) probe whether an attacker who forges a closing tag can still break out.",
        "segment": "XML Tags Stop Prompt Injection",
    },
    "prompt-tutorial-lesson-02-clear-and-direct": {
        "title": "Claude Is Not a Mind Reader",
        "narration": "Your turn. Paste this: you want to practice closing the gap between what you mean and what you write in a Claude prompt. Ask Claude to take a lazy instruction like 'summarize this,' rewrite it with explicit audience, length, and format so the intent is unambiguous, and then show you one prompt that reads as clear to a human but is genuinely ambiguous to the model — and pinpoint the missing constraint.",
        "command": "I want to practice closing the gap between what I mean and what I write in a Claude prompt. Take a lazy instruction like 'summarize this' and rewrite it with explicit audience, length, and format so the intent is unambiguous. Then explain why spelling out the desired output shape beats hoping the model infers it, and show me one prompt that reads as clear to a human but is genuinely ambiguous to the model.",
        "segment": "Claude Is Not a Mind Reader",
    },
    "prompt-tutorial-lesson-03-role-prompting": {
        "title": "Role Prompting Changes Everything",
        "narration": "Your turn. Paste this: you want to know whether role prompting actually changes reasoning or just changes tone. Ask Claude to design an experiment comparing a math problem answered with no role versus 'you are a logic professor,' explain mechanistically why a role in the system prompt shifts the response distribution, and give you one task where role prompting backfires because the persona introduces a bias the plain prompt avoids.",
        "command": "I want to know whether role prompting actually changes reasoning or just tone. Design an experiment comparing the same math problem answered with no role versus 'you are a logic professor' and say what output difference I should look for. Then explain mechanistically why a role in the system prompt shifts the response distribution, and give me one task where role prompting backfires because the persona introduces a bias the plain prompt avoids.",
        "segment": "Role Prompting Changes Everything",
    },
    "prompt-tutorial-lesson-05-formatting-output": {
        "title": "Prefill: Control Claude's Output Format",
        "narration": "Your turn. Paste this: you want to master prefilling Claude's response to lock its output format and suppress preamble. Ask Claude to explain how starting the assistant turn with an opening brace forces structured output, write you a prompt-plus-prefill pair that guarantees valid JSON with three named keys, and show you one case where a prefill backfires and how you'd repair it.",
        "command": "I want to master prefilling Claude's response to lock its output format. Explain how starting the assistant turn with an opening brace or a tag forces structured output and suppresses preamble, write me a prompt-plus-prefill pair that guarantees valid JSON with three named keys, and show me one case where a prefill backfires — the model breaks format anyway — and how I'd repair it.",
        "segment": "Prefill: Control Claude's Output Format",
    },
    "prompt-tutorial-lesson-06-precognition": {
        "title": "Precognition: Make Claude Think Before It Speaks",
        "narration": "Your turn. Paste this: you want to make Claude think before it speaks on a problem where the naive answer is a tempting trap. Ask Claude to show you the model answering immediately and getting it wrong, then force step-by-step reasoning and point to the exact step where the trap gets caught, and explain whether hiding that reasoning in tags versus showing it changes the accuracy or just the presentation.",
        "command": "I want to make Claude think before it speaks on a word problem where the naive answer is a tempting trap. Show me the model answering immediately and getting it wrong, then force step-by-step reasoning before the conclusion and point to the exact step where the trap gets caught. Then explain whether hiding that reasoning in tags versus showing it changes the accuracy or just the presentation.",
        "segment": "Precognition: Make Claude Think Before It Speaks",
    },
    "prompt-tutorial-lesson-07-few-shot-prompting": {
        "title": "Few-Shot: Examples Encode What Words Can't",
        "narration": "Your turn. Paste this: you want to feel the boundary where examples encode what instructions can't — take a formatting task where the rule is genuinely hard to write in words. Ask Claude to show you the task attempted with only a written instruction and where it drifts, then supply three examples and point out exactly which pattern the examples pinned down that words missed, and tell you how many examples is too few versus wasteful.",
        "command": "I want to feel the boundary where examples encode what instructions can't. Take a formatting task where the rule is genuinely hard to write in words, like matching an idiosyncratic citation style: (1) show me the same task attempted with only a written instruction and where it drifts, (2) supply three examples and point out exactly which pattern the examples pinned down that words missed, (3) tell me how many examples is too few versus wasteful.",
        "segment": "Few-Shot: Examples Encode What Words Can't",
    },
    "revision-change-log": {
        "title": "Revision Change Log: Make Drift Visible",
        "narration": "Your turn. Paste this: you asked Claude to revise a document and it changed things you didn't ask it to change — dropped statistics, shifted tone. Ask Claude to show you how to build a revision change log into your workflow: the format for tracking what each revision prompt changes, how to ask Claude to report its own changes before applying them, and the rule for when to reject a revision because scope has drifted.",
        "command": "I asked Claude to make a press release more concise and it also removed the impact paragraph, flattened the CEO quote, and rewrote the hook — four things changed when I asked to change one. Show me how to build a revision change log into my workflow: the format for tracking what each revision changes, how to ask Claude to report its own changes before applying them, and the rule for rejecting a revision whose scope has drifted.",
        "segment": "Revision Change Log: Make Drift Visible",
    },
    "scope-stack-setup": {
        "title": "Scope Stack: Stop Cramming Everything Into Every Prompt",
        "narration": "Your turn. Paste this: you front-load every Claude session with a 400-word preamble — tone preferences, format rules, domain context — and the outputs are still inconsistent because Claude ignores half of it by the middle. Ask Claude to show you how to build a scope stack — what goes in the system prompt versus the task prompt versus a context prefix — and how to split your preamble across those three slots.",
        "command": "I front-load every Claude session with a 400-word preamble of preferences, format rules, and context, and the outputs are still inconsistent — Claude ignores things stated at the top by the middle of the task. Show me how to build a scope stack: what goes in the system prompt versus the task prompt versus a context prefix, and how I'd split my 400-word preamble across those three slots.",
        "segment": "Scope Stack: Stop Cramming Everything Into Every Prompt",
    },
    "self-critique-loop": {
        "title": "Build a Self-Critique Prompt Checker with Claude",
        "narration": "Your turn. Paste this: you want Claude to review its own output for errors before you see it — but you know self-critique is structurally limited. Ask Claude to show you what class of errors the model can and cannot catch in its own output, and then show you the prompt structure that gets the most useful critique: separate critique turn, named failure criteria, and a structured report format.",
        "command": "I'm building a self-critique loop where Claude reviews its own output for errors before I see it. Show me why self-critique is structurally limited — what class of errors the model can and cannot catch in its own output — and then show me the prompt structure that gets the most useful critique: separate critique turn, named failure criteria, and a structured report format.",
        "segment": "Build a Self-Critique Prompt Checker with Claude",
    },
    "six-component-prompt": {
        "title": "The Six-Component Prompt",
        "narration": "Your turn. Paste this: you have a vague prompt — 'improve this intro' — and you want to turn it into a six-component specification. Ask Claude to walk you through the six components, show you how to fill each one for an editorial task, and tell you which components matter most so you stop leaving decisions to Claude's best guess.",
        "command": "I have a vague prompt — 'improve this intro' — and I want to turn it into a six-component specification. Walk me through the six components (task, context, examples, format, constraints, persona), show me how to fill each one for an editorial rewrite request, and tell me which components matter most when the task is editorial.",
        "segment": "The Six-Component Prompt",
    },
    "six-component-spec": {
        "title": "Turn a Vague Claude Prompt into a Six-Component Specification",
        "narration": "Your turn. Paste this: you're building a CLI tool that takes a vague user prompt and outputs a six-component specification for Claude. Ask Claude to show you the specification schema, how the CLI prompts the user to fill each slot interactively, and how the final spec gets assembled into a Claude-ready prompt you can run immediately.",
        "command": "I'm building a CLI tool that takes a vague user prompt and outputs a six-component specification. Show me the specification schema (task, context, examples, format, constraints, persona), how the CLI prompts the user to fill each slot interactively, and how the final spec gets assembled into a Claude-ready prompt.",
        "segment": "Turn a Vague Claude Prompt into a Six-Component Specification",
    },
    "six-slot-anatomy": {
        "title": "Six Slots, One Better Brief",
        "narration": "Your turn. Paste this: your Claude prompts fail because you fill only the task slot and leave five anatomy slots to Claude's defaults — and Claude fills them with generic guesses. Ask Claude to walk you through each of the six anatomy slots with a concrete example for drafting a client update email, and show you what filling all six looks like versus leaving five empty.",
        "command": "My Claude prompts fail not because the task is wrong, but because five of the six anatomy slots are empty — I fill the task slot and leave the rest to Claude's defaults. Walk me through each of the six anatomy slots with a concrete example for a single task: drafting a client update email. Show me what filling all six looks like versus leaving five empty.",
        "segment": "Six Slots, One Better Brief",
    },
    "three-pass-refinement-demo": {
        "title": "Build a 3-Pass Prompt Refinement Demo with Claude",
        "narration": "Your turn. Paste this: you're building a three-pass prompt refinement demo — a system that takes an initial prompt, runs it through three structured critiques, and produces a better version each pass. Ask Claude to show you what each pass critiques, how you pass the critique back into the refinement prompt, and the stopping rule that tells you when a third pass would produce diminishing returns.",
        "command": "I'm building a three-pass prompt refinement demo — a system that takes an initial prompt, runs it through three structured critiques, and produces a better version each pass. Show me what each pass critiques (clarity, specificity, success criteria), how I pass the critique back into the refinement prompt, and the stopping rule that tells me when a third pass yields diminishing returns.",
        "segment": "Build a 3-Pass Prompt Refinement Demo with Claude",
    },
    "vox-agentic-irreversible": {
        "title": "Why 'Clean Up This Folder' Is a Dangerous Instruction",
        "narration": "Your turn. Paste this: you're about to give a Claude agent access to your file system — delete, rename, move files. Ask Claude to show you how to identify which instructions are reversible versus irreversible before the agent runs them, the gate pattern that makes Claude present its action plan for review before any irreversible step, and the system prompt clause that enforces the pause.",
        "command": "I'm about to give a Claude agent access to my file system — delete, rename, move files. Show me how to identify which instructions are reversible versus irreversible before the agent runs them, the gate pattern that makes Claude present its action plan for review before any irreversible step, and the system prompt clause that enforces it.",
        "segment": "Why 'Clean Up This Folder' Is a Dangerous Instruction",
    },
    "vox-citation-surface-format": {
        "title": "Why Claude Can't Write Your Literature Review",
        "narration": "Your turn. Paste this: you asked Claude for citations for your literature review and some of them don't exist — they look real but the papers aren't there. Ask Claude to show you the three-tier citation protocol: how you use Claude to identify what to look for, how you retrieve actual sources separately, and how you bring confirmed citations back to Claude for synthesis without asking Claude to generate citations itself.",
        "command": "I asked Claude for citations for my literature review and some don't exist — author, journal, year all formatted correctly, paper doesn't exist. Show me the three-tier citation protocol: how I use Claude to identify what I need to look for, how I retrieve actual sources separately, and how I bring confirmed citations back to Claude for synthesis without ever asking Claude to generate a citation.",
        "segment": "Why Claude Can't Write Your Literature Review",
    },
    "vox-context-priority-weight": {
        "title": "Why More Context Can Make the Output Worse",
        "narration": "Your turn. Paste this: you pasted six project documents into Claude and the summary reflected the longest formal document, ignoring the short email that had the actual decision. Ask Claude to show you the context priority rule — how Claude weights context by structural prominence, which documents to prune before pasting, and how to signal to Claude which part of the context is load-bearing.",
        "command": "I pasted six project documents into Claude and the summary reflected the longest, most formal one — ignoring the short email at the bottom that had the actual decision. Show me the context priority rule: how Claude weights context by structural prominence, which documents to prune before pasting, and how to signal to Claude which part of the context is load-bearing.",
        "segment": "Why More Context Can Make the Output Worse",
    },
    "vox-criteria-before-output": {
        "title": "Why You Should Write the Test Before You Write the Prompt",
        "narration": "Your turn. Paste this: you're generating a grant proposal with Claude and it keeps coming back polished but wrong — missing required measurables, wrong figures, mismatched budget narrative. Ask Claude to show you how to write the acceptance test before writing the prompt: the three questions that define what a passing draft looks like, and how you encode those tests as success criteria in the prompt itself.",
        "command": "I'm generating a grant proposal with Claude and it keeps coming back polished but wrong — missing measurable indicators, wrong figures, budget that doesn't match the project. Show me how to write the acceptance test before writing the prompt: the three questions that define what a passing draft looks like, how I encode those tests as success criteria in the prompt, and how I run the test on Claude's output before submitting.",
        "segment": "Why You Should Write the Test Before You Write the Prompt",
    },
    "vox-examples-teach-more": {
        "title": "Why Your Examples Teach More Than Your Instructions",
        "narration": "Your turn. Paste this: you pasted an informal memo as a format example and Claude matched the casual tone you didn't want — because examples override instructions when they conflict. Ask Claude to show you why this happens, how to annotate an example to name what you're demonstrating versus what you're not, and how to write the few-shot section of a prompt so Claude extracts only the intended pattern.",
        "command": "I pasted an informal memo as a format example and Claude matched the casual tone I never meant to include — the example overrode my instruction. Show me why examples override instructions when they conflict, how to annotate an example to name what I'm demonstrating versus what I'm not, and how to write the few-shot section of a prompt so Claude extracts only the intended pattern.",
        "segment": "Why Your Examples Teach More Than Your Instructions",
    },
    "vox-prompt-injection": {
        "title": "Why the Document You Asked AI to Read Might Be Giving It New Instructions",
        "narration": "Your turn. Paste this: you use a Claude agent to read vendor documents and you noticed the agent followed an instruction hidden in the document instead of yours. Ask Claude to show you the prompt injection anatomy — how an instruction embedded in untrusted content gets executed, the isolation pattern that wraps document content in delimiters so it stays data rather than instruction, and how you test your prompt against a document that tries to inject.",
        "command": "I use a Claude agent to read vendor documents and I noticed the agent followed an instruction hidden inside one of them — not my instruction. Show me the prompt injection anatomy: how an instruction embedded in untrusted content gets executed, the isolation pattern that wraps document content in delimiters so it stays data rather than instruction, and how I test my prompt against an adversarial document.",
        "segment": "Why the Document You Asked AI to Read Might Be Giving It New Instructions",
    },
    "vox-prompt-library-lost": {
        "title": "Why the Prompt That Worked Is Already Lost",
        "narration": "Your turn. Paste this: your best Claude prompt is buried in a chat you can't find and you're rewriting it from scratch for the third time. Ask Claude to show you how to build a personal prompt library — the three fields every prompt card needs, where to store it so it survives across sessions, and the naming convention that makes it findable when you need it next quarter.",
        "command": "My best Claude prompt is buried in a chat I can't find and I'm rewriting it from scratch for the third time. Show me how to build a personal prompt library: the three fields every prompt card needs (intent, prompt text, failure modes), where to store it so it survives across sessions, and the naming convention that makes it findable when I need it.",
        "segment": "Why the Prompt That Worked Is Already Lost",
    },
    "vox-prompt-six-slots": {
        "title": "Why 'Improve This' Is a Wish, Not an Instruction",
        "narration": "Your turn. Paste this: you asked Claude to improve your introduction and the result was polished but wrong for your audience and situation — because 'improve this' left six decisions to Claude. Ask Claude to show you the six slots that 'improve this' leaves empty and how to fill all six for an editorial task so Claude's improvement is actually the one you wanted.",
        "command": "I asked Claude to improve my introduction and the result was polished, well-organized, and wrong for my actual situation — because 'improve this' left six decisions to Claude. Show me the six slots that 'improve this' leaves empty — role, audience, success criteria, format, constraints, failure modes — and how to fill all six for an editorial rewrite so the improvement is actually mine.",
        "segment": "Why 'Improve This' Is a Wish, Not an Instruction",
    },
    "vox-prompt-spec": {
        "title": "Why 'Make This Better' Is Not a Prompt",
        "narration": "Your turn. Paste this: you sent Claude one line — 'improve my methods section' — and it rewrote correctly for a different journal and a different audience, because the prompt left all five specification fields to Claude's defaults. Ask Claude to show you the five elements that turn 'make this better' into an actual instruction — audience, register, journal norms, success criteria, and what not to change.",
        "command": "I sent Claude one line — 'improve my methods section' — and it rewrote for a different journal and different audience because the prompt left everything to defaults. Show me the five elements that turn 'make this better' into an actual instruction: audience, register, journal norms, success criteria, and an explicit list of what NOT to change.",
        "segment": "Why 'Make This Better' Is Not a Prompt",
    },
    "vox-self-review-sieve": {
        "title": "Why AI Can't Fix Its Own Mistakes",
        "narration": "Your turn. Paste this: you asked Claude to review its own reasoning and fix an error you pointed out, and the revision said 'logic strengthened' while the error was still there. Ask Claude to show you the self-review blind spot — what class of errors a model systematically misses in its own output, and how to design a second-turn critique that actually breaks the repetition through structural separation.",
        "command": "I asked Claude to review its own reasoning and fix an error I pointed out. The revision came back saying 'logic strengthened' — the error was still there, stated more confidently. Show me the self-review blind spot: what class of errors a model systematically misses in its own output, and how to design a second-turn critique that actually breaks the repetition through structural separation.",
        "segment": "Why AI Can't Fix Its Own Mistakes",
    },
    "vox-surface-routing": {
        "title": "Why the Wrong AI Surface Costs More Than the Wrong Prompt",
        "narration": "Your turn. Paste this: you asked Claude to find patterns in your program data and got a confident analysis — but the data files were never included because you chose the wrong surface. Ask Claude to show you the surface routing decision — which task types belong in Claude.ai versus the API with file context versus Claude Code — and how you identify which surface your task actually needs before writing the prompt.",
        "command": "I asked Claude in the chat UI to find patterns in my program data and it returned a confident analysis — the data files were never included because I chose the wrong surface. Show me the surface routing decision: which task types belong in Claude.ai versus the API with file context versus Claude Code, and how I identify which surface my task actually needs before I start writing the prompt.",
        "segment": "Why the Wrong AI Surface Costs More Than the Wrong Prompt",
    },
    "vox-vague-revision-spreads": {
        "title": "Why Vague Revision Requests Change the Wrong Things",
        "narration": "Your turn. Paste this: you asked Claude to make a press release more concise and it removed the impact paragraph, flattened the CEO quote, and rewrote the opening hook — four things changed when you asked to change one. Ask Claude to show you the scoped revision pattern — how to name exactly what changes and what doesn't, and the constraint that tells Claude its scope before it edits.",
        "command": "I asked Claude to make a press release more concise. It shortened it — and also removed the impact paragraph, flattened the CEO quote, and rewrote the opening hook. I asked to change one thing and four things changed. Show me the scoped revision pattern: how to name exactly what changes and what doesn't, and the constraint that tells Claude its scope before it edits.",
        "segment": "Why Vague Revision Requests Change the Wrong Things",
    },
    "vox-writing-claim-invention": {
        "title": "Why Claude Invents Claims When You Ask It to Improve Your Writing",
        "narration": "Your turn. Paste this: you asked Claude to strengthen your argument and it added a claim you never wrote — and three weeks later a reviewer asked you to cite it. Ask Claude to show you the claim-invention risk — why improving writing triggers generation rather than editing, the prompt constraint that limits Claude to restructuring existing claims without adding new ones, and how you check the output for invented content.",
        "command": "I asked Claude to strengthen my argument and it added a claim in paragraph three that I never wrote — a reviewer asked me to cite it three weeks later. Show me the claim-invention risk: why 'improve this argument' triggers generation rather than editing, the prompt constraint that limits Claude to restructuring existing claims without adding new ones, and how I check the output for invented content.",
        "segment": "Why Claude Invents Claims When You Ask It to Improve Your Writing",
    },
    "what-is-claude-prompting": {
        "title": "What Is the Claude Prompting Playlist.",
        "narration": "Your turn. Paste this: you're starting the Claude Prompting playlist and you want to know what computational skepticism means as a framework for prompts. Ask Claude to walk you through why 'be more specific' is not actionable, what Popper's falsifiability rule looks like applied to a prompt, and give you one prompt you probably write every week that fails the falsifiability test — where you can't say in advance what a bad answer would look like.",
        "command": "I'm starting the Claude Prompting playlist and I want to know what computational skepticism means as a framework for writing prompts. Walk me through: why 'be more specific' is not actionable advice, what Popper's falsifiability rule looks like applied to a prompt, and give me one prompt I probably write every week that fails the falsifiability test — where I can't say in advance what a bad answer would look like.",
        "segment": "What Is the Claude Prompting Playlist",
    },
}

fixed = 0
for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    bak = path + ".bak-prompting-v1"
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
