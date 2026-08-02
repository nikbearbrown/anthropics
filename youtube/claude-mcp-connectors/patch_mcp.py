#!/usr/bin/env python3
"""Fix claude-mcp-connectors: voice_id + OUTRO props + YOURTURN placeholders."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def get_beat_id(b):
    return b.get("beat_id", b.get("id", ""))

def fix_voice(meta):
    meta.pop("voice_id", None)
    if not meta.get("engine"): meta["engine"] = "kokoro"
    meta["voice"] = "am_onyx"
    if not meta.get("voice_kokoro"): meta["voice_kokoro"] = "am_onyx"

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

def ensure_outro(beats, title, slug):
    for i, b in enumerate(beats):
        bid = get_beat_id(b)
        act = b.get("act", "")
        scene = b.get("scene", "")
        shot = b.get("shot", {})
        rem = shot.get("remotion", {}) if isinstance(shot, dict) else {}
        pat = rem.get("pattern", "") if isinstance(rem, dict) else ""
        top_rem = b.get("remotion", {})
        pat_top = (top_rem or {}).get("pattern", "") if isinstance(top_rem, dict) else ""
        if ("Outro" in pat or "Outro" in pat_top or "Outro" in scene
                or bid in ("OUTRO", "BOUT") or act == "OUTRO" or "outro" in bid.lower()):
            shot = b.setdefault("shot", {})
            shot["type"] = "REMOTION"
            shot["source"] = "own"
            shot.pop("motion", None)
            remotion = shot.setdefault("remotion", {})
            remotion["pattern"] = "ClaudeTitleOutro"
            props = remotion.setdefault("props", {})
            props["title"] = title
            props["handle"] = "@NikBearBrown"
            props["mascotSeed"] = slug
            props.pop("subline", None)
            props.pop("brand", None)
            props.pop("tagline", None)
            props.pop("url", None)
            if "remotion" in b:
                b.pop("remotion", None)
            return True
    beats.append({
        "beat_id": "OUTRO",
        "act": "OUTRO",
        "narration_text": "Nik Bear Brown. MCP.",
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {"title": title, "handle": "@NikBearBrown", "mascotSeed": slug},
            },
        },
    })
    return True

def is_placeholder(text):
    if not text: return True
    t = text.strip()
    return t in ("", "Your turn.", "[seed]") or "[Your turn" in t

def ensure_yourturn(beats, narration, command, segment,
                    topic="CLAUDE MCP CONNECTORS · @NikBearBrown"):
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
        if ("Outro" in pat or "Outro" in pat_top or bid in ("OUTRO", "BOUT")
                or act == "OUTRO" or "outro" in bid.lower()):
            outro_idx = i

    yt_props = {
        "greeting": "Your turn.",
        "command": command,
        "segment": segment,
        "topic": topic,
        "folderLabel": "@NikBearBrown",
        "modelLabel": "Claude Sonnet",
        "runningText": "paste your MCP server URL, tool list, or server code here…",
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
    "evaluate-mcp-server": {
        "title": "Evaluate an MCP Server Before Connecting It with Claude",
        "narration": "Your turn. Paste this: you found an MCP server and you want to evaluate it before connecting it to Claude. Ask Claude for the evaluation checklist — what permissions to audit, what tool names signal over-reach, and what a safe MCP server looks like versus a risky one.",
        "command": "I found an MCP server and I want to evaluate it before connecting it to Claude. Give me the evaluation checklist: what permissions should I audit, what tool names or scopes signal over-reach, and what does a safe MCP server look like versus a risky one?",
        "segment": "Evaluate an MCP Server Before Connecting It with Claude",
    },
    "mcp-resource-vs-tool": {
        "title": "MCP Resource vs. Tool: The Distinction That Matters",
        "narration": "Your turn. Paste this: you're designing an MCP server and you're not sure whether to expose something as a resource or a tool. Ask Claude to explain the resource-versus-tool distinction — what each one is for, when the wrong choice causes problems, and give you a decision rule.",
        "command": "I'm designing an MCP server and I'm not sure whether to expose something as a resource or a tool. Explain the resource-versus-tool distinction: what is each one for, when does the wrong choice cause problems for Claude's ability to use the server, and give me a decision rule for choosing.",
        "segment": "MCP Resource vs. Tool: The Distinction That Matters",
    },
    "vox-mcp-blast-radius": {
        "title": "Why a Connected MCP Server Changes the Risk Profile of Every Task",
        "narration": "Your turn. Paste this: you connected an MCP server to Claude and you want to understand how it changed the risk profile of your session. Ask Claude to explain the blast radius — what actions the connected server makes possible that weren't possible before — and how to scope the server's permissions to match only what you actually need.",
        "command": "I connected an MCP server to Claude and I want to understand how it changed the risk profile of my session. Explain the blast radius: what actions does the connected server make possible that weren't possible before — and how do I scope the server's permissions to match only what I actually need it to do?",
        "segment": "Why a Connected MCP Server Changes the Risk Profile of Every Task",
    },
    "github-mcp-server-giving-model-tools-makes-choose": {
        "title": "Why giving a model more tools makes it choose worse",
        "narration": "Your turn. Paste this: you added more tools to your MCP server hoping Claude would use them better, but it's making worse choices. Ask Claude to explain the tool-count paradox — why adding tools degrades selection accuracy — and what the design pattern is for keeping Claude's tool selection sharp.",
        "command": "I added more tools to my MCP server expecting Claude to use them better, but it's making worse choices. Explain the tool-count paradox: why does adding more tools degrade Claude's selection accuracy — and what is the design pattern for keeping Claude's tool selection sharp as I scale the number of available tools?",
        "segment": "Why giving a model more tools makes it choose worse",
    },
    "github-mcp-server-one-generic-cli-drive-api": {
        "title": "Why one generic CLI can drive an API it has never seen",
        "narration": "Your turn. Paste this: you want to understand how a generic MCP CLI tool can call an API it was never explicitly trained on. Ask Claude to explain the schema-driven reasoning — how Claude reads an API schema at runtime and calls endpoints it has never seen before — and what the MCP tool definition needs to include to make this work.",
        "command": "I want to understand how a generic MCP CLI tool can call an API it was never explicitly trained on. Explain the schema-driven reasoning: how does Claude read an API schema at runtime and call endpoints it has never seen before — and what does the MCP tool definition need to include for Claude to drive a novel API correctly?",
        "segment": "Why one generic CLI can drive an API it has never seen",
    },
}

fixed = 0
for base_slug, patch in PATCHES.items():
    for slug in [base_slug, f"claude-liam-{base_slug}"]:
        path = os.path.join(BASE, slug, "beat_sheet.json")
        if not os.path.exists(path):
            continue
        bak = path + ".bak-mcp-v1"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        with open(path) as f:
            d = json.load(f)
        meta = d.get("metadata", {})
        fix_voice(meta)
        beats = d.get("beats", d.get("scenes", []))
        strip_all_sublines(beats)
        ensure_outro(beats, patch["title"], slug)
        ensure_yourturn(beats, patch["narration"], patch["command"], patch["segment"])
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed += 1
        print(f"FIXED: {slug}")

print(f"\nDone. {fixed} files fixed.")
