#!/usr/bin/env python3
"""Patch 9 scaffold reels: replace YOURTURN placeholder with topic-specific content."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

PATCHES = {
    "anthropic-sdk-php-server-hands-back-encrypted-context": {
        "narration": "Your turn. Paste this into a Claude session: you're building a multi-turn PHP app with the Anthropic SDK. Show me how to detect a compaction block in the response, and write the code that threads the encrypted_content blob — not the human-readable summary — back into the next messages array. Explain what breaks if you send the summary text instead.",
        "command": "You're building a multi-turn PHP app with the Anthropic SDK. Show me how to detect a compaction block in the response, and write the code that threads the `encrypted_content` blob — not the human-readable summary — back into the next `messages` array. What breaks if you send the summary text instead?",
        "running": "paste your current multi-turn implementation…",
        "segment": "Why the server hands back an encrypted context you're only going to echo",
    },
    "anthropic-sdk-typescript-partial-json-valid-object-before": {
        "narration": "Your turn. Paste this: I'm streaming a tool call with the Anthropic TypeScript SDK and I see partial JSON arriving via the inputJson event. Walk me through why each chunk's jsonSnapshot is already a valid JS object before the closing brace arrives, and show me how to read a field from it safely mid-stream without waiting for the tool_use_delta done event.",
        "command": "I'm streaming a tool call with the Anthropic TypeScript SDK and I see partial JSON arriving via the `inputJson` event. Walk me through why each chunk's `jsonSnapshot` is already a valid JS object before the closing brace arrives, and show me how to read a field from it safely mid-stream without waiting for the `tool_use_delta` done event.",
        "running": "paste your streaming tool-call handler…",
        "segment": "Why partial JSON can be a valid object before the closing brace arrives",
    },
    "claude-constitution-one-narrow-safety-rule-make": {
        "narration": "Your turn. Paste this: I want to audit a safety rule in my Claude deployment. The rule is: always recommend a licensed professional when a user mentions mental health. Walk me through the second-order effects — what self-concept does this rule teach the model about itself, and how might that self-concept leak into unrelated conversations that never mention mental health?",
        "command": "I want to audit a safety rule in my Claude deployment. The rule is: always recommend a licensed professional when a user mentions mental health. Walk me through the second-order effects — what self-concept does this rule teach the model about itself, and how might that self-concept leak into unrelated conversations that never mention mental health?",
        "running": "paste your current system prompt or safety rule…",
        "segment": "How one narrow safety rule can make an AI less safe everywhere else",
    },
    "claude-cookbooks-splitting-chunk-from-document-makes": {
        "narration": "Your turn. Here's the prompt: I have a research paper being split into chunks for RAG. A chunk says 'This treatment reduced mortality by 12%' with no disease name in context. Show me how to prepend a context header to each chunk before embedding, what fields should be in that header, and how I'd verify the fix is actually preventing false matches on unrelated queries.",
        "command": "I have a research paper being split into chunks for RAG. A chunk says 'This treatment reduced mortality by 12%' with no disease name in context. Show me how to prepend a context header to each chunk before embedding, what fields should be in that header, and how I'd verify the fix is actually preventing false matches on unrelated queries.",
        "running": "paste your chunking function…",
        "segment": "Why splitting a chunk from its document makes it retrieve for the wrong question",
    },
    "claude-quickstarts-50-turn-agent-pays-same": {
        "narration": "Your turn. Paste this: I'm building a 50-turn computer-use agent that revisits the same 5 desktop states repeatedly. Show me exactly where to place cache_control on the screenshot messages so each unique state is only billed once, and write the code that detects a repeated state and routes to the cached version instead of sending the raw image again.",
        "command": "I'm building a 50-turn computer-use agent that revisits the same 5 desktop states repeatedly. Show me exactly where to place `cache_control` on the screenshot messages so each unique state is only billed once, and write the code that detects a repeated state and routes to the cached version instead of sending the raw image again.",
        "running": "paste your agent loop code…",
        "segment": "Why a 50-turn agent pays for the same screenshot 35 times unless it caches the pixels",
    },
    "claude-quickstarts-claude-s-click-lands-wrong": {
        "narration": "Your turn. Here's the prompt: my computer-use app sends Claude a 1456×819 view of a 1920×1080 screen. Claude returns click coordinates in the view's coordinate space. Show me the two-line scaling formula I need to apply before passing those coordinates to the OS input driver, and explain what happens if I skip it on a Retina display with a device pixel ratio of 2.",
        "command": "My computer-use app sends Claude a 1456×819 view of a 1920×1080 screen. Claude returns click coordinates in the view's coordinate space. Show me the two-line scaling formula I need to apply before passing those coordinates to the OS input driver, and explain what happens if I skip it on a Retina display with a device pixel ratio of 2.",
        "running": "paste your coordinate-handling code…",
        "segment": "Why Claude's click lands in the wrong spot — and the one ratio that fixes it",
    },
    "claudeforfoundationmodels-same-api-key-shipped-prototype": {
        "narration": "Your turn. Paste this: I'm shipping a Claude-powered iOS app and my API key is currently baked into the binary. Walk me through the backend relay architecture I need — what the iOS client sends, how the relay injects the real key server-side, and what the minimum viable server looks like so I can pass App Store review without exposing the key.",
        "command": "I'm shipping a Claude-powered iOS app and my API key is currently baked into the binary. Walk me through the backend relay architecture I need — what the iOS client sends, how the relay injects the real key server-side, and what the minimum viable server looks like so I can pass App Store review without exposing the key.",
        "running": "paste your current auth setup…",
        "segment": "Why the same API key that shipped your prototype becomes a critical bug in production",
    },
    "claudeforfoundationmodels-web-search-never-runs-code": {
        "narration": "Your turn. Here's the prompt: in the Anthropic Swift SDK I have both .webSearch declared in serverTools and a local Swift function declared in tools. Walk me through what happens at the network level for each — how many round-trips, who executes the tool, and where the result enters the conversation — so I can reason about latency budgets in my app.",
        "command": "In the Anthropic Swift SDK I have both `.webSearch` declared in `serverTools` and a local Swift function declared in `tools`. Walk me through what happens at the network level for each — how many round-trips, who executes the tool, and where the result enters the conversation — so I can reason about latency budgets in my app.",
        "running": "paste your tool declarations…",
        "segment": "Why web search never runs your code but your own tool always does — with identical syntax",
    },
    "evals-model-says-i-have-no": {
        "narration": "Your turn. Paste this: I'm building an eval for preference elicitation and I suspect my current method — reading the generated string — is missing the real signal. Show me how to read the log probabilities at the completion position for each option token instead, and write the code that converts those raw logits into a probability distribution I can compare across model versions.",
        "command": "I'm building an eval for preference elicitation and I suspect my current method — reading the generated string — is missing the real signal. Show me how to read the log probabilities at the completion position for each option token instead, and write the code that converts those raw logits into a probability distribution I can compare across model versions.",
        "running": "paste your current eval harness…",
        "segment": "The model says 'I have no preferences' while assigning 74% to survival",
    },
}

for slug, patch in PATCHES.items():
    path = os.path.join(BASE, slug, "beat_sheet.json")
    bak = path + ".bak-yourturn-v1"
    if not os.path.exists(path):
        print(f"SKIP (not found): {slug}")
        continue
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    with open(path) as f:
        d = json.load(f)
    beats = d.get("beats", d.get("scenes", []))
    fixed = False
    for beat in beats:
        if beat.get("beat_id") == "YOURTURN":
            beat["narration_text"] = patch["narration"]
            shot = beat.setdefault("shot", {})
            remotion = shot.setdefault("remotion", beat.pop("remotion", {}))
            shot["type"] = "REMOTION"
            props = remotion.setdefault("props", {})
            remotion["pattern"] = "ClaudeComposerAsk"
            props["greeting"] = "Your turn."
            props["command"] = patch["command"]
            props["runningText"] = patch["running"]
            props["segment"] = patch["segment"]
            props["topic"] = "CLAUDE BASICS · @NikBearBrown"
            props["folderLabel"] = "@NikBearBrown"
            props["modelLabel"] = "Claude Sonnet"
            fixed = True
            break
    if fixed:
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"FIXED: {slug}")
    else:
        print(f"WARN (no YOURTURN beat found): {slug}")

print("Done.")
