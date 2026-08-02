#!/usr/bin/env python3
"""Fix claude-plugins: YOURTURN content only."""
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
                    topic="CLAUDE PLUGINS · @NikBearBrown"):
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
        "runningText": "paste your plugin manifest, integration spec, or connector setup here…",
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
    "claude-code-plugin-seven-surfaces": {
        "narration": "Your turn. Paste this: you want to understand the seven surfaces in the Claude manifest — the places where a plugin's metadata appears and influences behavior. Ask Claude to walk you through all seven surfaces, what each one controls, and what happens when the manifest metadata doesn't match what the plugin actually does.",
        "command": "I want to understand the seven surfaces in the Claude plugin manifest — the places where a plugin's metadata appears and influences Claude's behavior. Walk me through all seven surfaces: what does each one control, how does Claude use it, and what happens when the manifest metadata doesn't match what the plugin actually does at runtime?",
        "segment": "Seven Surfaces, One Manifest",
    },
    "claude-plugins-community-copyright-restrictions-mean-three-compl": {
        "narration": "Your turn. Paste this: you want to understand why the phrase 'copyright restrictions' in a plugin policy can mean three completely different things depending on context. Ask Claude to explain the three distinct meanings — what each one permits or prohibits — and how to write plugin policy language that is actually unambiguous.",
        "command": "I want to understand why 'copyright restrictions' in a plugin policy can mean three completely different things depending on context. Explain the three distinct meanings — what each one permits or prohibits for the user and the plugin — and how to write plugin policy language that is actually unambiguous rather than leaving users to guess which interpretation applies.",
        "segment": "Why 'copyright restrictions' can mean three completely different things",
    },
    "claude-plugins-community-image-model-s-burned-captions": {
        "narration": "Your turn. Paste this: you want to understand why an image model's burned-in captions hallucinate but an ASR endpoint's don't — even though both are producing text from visual or audio input. Ask Claude to explain the architectural difference that causes this divergence, and what it implies for choosing between image OCR and ASR when you need accurate text extraction.",
        "command": "I want to understand why an image model's burned-in captions hallucinate but an ASR endpoint's don't — even though both produce text from sensory input. Explain the architectural difference that causes this divergence: why does the image model hallucinate caption text while the ASR endpoint transcribes accurately? And what does this imply for choosing between image OCR and ASR when I need accurate text extraction from a video or slide?",
        "segment": "Why an image model's burned-in captions hallucinate but an ASR endpoint's don't",
    },
    "claude-plugins-official-enabling-sms-breaks-access-control": {
        "narration": "Your turn. Paste this: you want to understand why enabling SMS in a Claude plugin breaks access control even when your phone number is on the allowlist. Ask Claude to explain the access control failure — what assumption the allowlist makes that SMS bypasses — and how to design the integration so the allowlist actually holds.",
        "command": "I want to understand why enabling SMS in a Claude plugin breaks access control even when my phone number is on the allowlist. Explain the access control failure: what assumption does the allowlist make that SMS bypasses — and how do I design the integration so the allowlist constraint actually holds when SMS is enabled?",
        "segment": "Why enabling SMS breaks access control even when your number is allowlisted",
    },
    "claude-plugins-official-live-bot-hands-pairing-codes": {
        "narration": "Your turn. Paste this: you want to understand why a live bot hands pairing codes to strangers and then suddenly stops — what the failure mode is and what caused the fix. Ask Claude to explain the pairing code leak pattern: what made the bot issue codes to unintended recipients, what check stopped it, and how to audit your own bot for similar session boundary failures.",
        "command": "I want to understand why a live bot hands pairing codes to strangers and then suddenly stops — what the failure mode is and what caused the fix. Explain the pairing code leak pattern: what made the bot issue codes to unintended recipients, what specific check or state boundary stopped the leak, and how do I audit my own bot integration for similar session boundary failures?",
        "segment": "Why a live bot hands pairing codes to strangers, then suddenly stops",
    },
    "claude-plugins-official-same-assistant-code-runs-discord": {
        "narration": "Your turn. Paste this: you want to understand why the same assistant code can run on Discord, Telegram, and iMessage unchanged — what the abstraction is that makes this possible. Ask Claude to explain the platform abstraction layer: what it normalizes across the three platforms, what it cannot normalize, and what you must handle per-platform even with a shared codebase.",
        "command": "I want to understand why the same assistant code can run on Discord, Telegram, and iMessage without changes — what abstraction makes this possible. Explain the platform abstraction layer: what does it normalize across the three platforms so the assistant code doesn't need to know which one it's on, what does it cannot normalize so the assistant still needs to handle, and what must I handle per-platform even with a shared codebase?",
        "segment": "Why the same assistant code runs on Discord, Telegram, and iMessage unchanged",
    },
    "knowledge-work-plugins-responding-webhook-after-processing-silen": {
        "narration": "Your turn. Paste this: you want to understand why responding to a webhook after processing it silently doubles every event — what the sequencing error is and how to fix it. Ask Claude to explain the double-processing pattern: what the correct webhook acknowledgment sequence is, what causes the duplication when response is delayed, and how to make the fix idempotent so even duplicate deliveries don't cause double processing.",
        "command": "I want to understand why responding to a webhook after processing it silently doubles every event — what is the sequencing error and how do I fix it? Explain the double-processing pattern: what is the correct webhook acknowledgment sequence (respond first, then process), what causes duplication when the response is delayed until after processing, and how do I make my handler idempotent so even duplicate deliveries don't cause double processing?",
        "segment": "Why responding to a webhook after processing it silently doubles every event",
    },
}

fixed = 0
for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    bak = path + ".bak-plugins-v1"
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
