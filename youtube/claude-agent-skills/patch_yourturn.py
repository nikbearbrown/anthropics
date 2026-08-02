#!/usr/bin/env python3
"""Patch 16 agent-skills reels: replace YOURTURN placeholders with real prompts."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

PATCHES = {
    "agent-sdk-workshop-adding-one-capability-time-changes": {
        "narration": "Your turn. Paste this: I'm adding tools to a Claude agent one capability at a time. Show me how to structure the tool definitions so each stage is testable in isolation — and tell me what the first tool should be for an agent whose job is competitive briefing.",
        "command": "I'm adding tools to a Claude agent one capability at a time. Show me how to structure the tool definitions so each stage is testable in isolation — and tell me what the first tool should be for an agent whose job is competitive briefing.",
        "segment": "Why adding one capability at a time changes what the same agent produces",
    },
    "agent-sdk-workshop-agent-s-memory-guardrail-one": {
        "narration": "Your turn. Paste this: my agent has a save_memory tool but I'm worried the model skips it when under pressure. Show me how to implement a UserPromptSubmit hook that silently checks memory without the model seeing it — and explain why the hook is more reliable than the tool for critical state.",
        "command": "My agent has a `save_memory` tool but I'm worried the model skips it when under pressure. Show me how to implement a `UserPromptSubmit` hook that silently checks memory without the model seeing it — and explain why the hook is more reliable than the tool for critical state.",
        "segment": "Why an agent's memory guardrail is one the model can't see",
    },
    "agent-sdk-workshop-parallelism-prompt-problem-code-problem": {
        "narration": "Your turn. Paste this: I have five companies to brief. Show me two versions of the same system prompt — one that produces sequential research and one that spawns parallel researchers — with no code changes, just different instruction phrasing. Then explain the minimal orchestration the SDK needs to actually run them in parallel.",
        "command": "I have five companies to brief. Show me two versions of the same system prompt — one that produces sequential research and one that spawns parallel researchers — with no code changes, just different instruction phrasing. Then explain the minimal orchestration the SDK needs to actually run them in parallel.",
        "segment": "Why parallelism is a prompt problem, not a code problem",
    },
    "anthropic-tools-channel-returns-tool-results-also": {
        "narration": "Your turn. Paste this: my agent called a tool with a missing required parameter and the tool returned None. Show me how to write a tool wrapper that catches None returns before they enter the tool_outputs message, and what I should send back to the model so it retries with the correct parameter.",
        "command": "My agent called a tool with a missing required parameter and the tool returned `None`. Show me how to write a tool wrapper that catches `None` returns before they enter the `tool_outputs` message, and what I should send back to the model so it retries with the correct parameter.",
        "segment": "Why the channel that returns tool results also carries the mistakes",
    },
    "claude-agent-sdk-demos-interleaved-parallel-tool-logs-still": {
        "narration": "Your turn. Paste this: I have a lead agent spawning three parallel researchers and a data analyst, and their tool calls are interleaved in the log. Show me the minimal metadata I need to attach to each call — and the log parsing logic — to trace every tool result back to the agent that requested it.",
        "command": "I have a lead agent spawning three parallel researchers and a data analyst, and their tool calls are interleaved in the log. Show me the minimal metadata I need to attach to each call — and the log parsing logic — to trace every tool result back to the agent that requested it.",
        "segment": "Why interleaved parallel tool logs can still be traced to the right agent",
    },
    "claude-agent-sdk-typescript-sending-full-list-beats-sending": {
        "narration": "Your turn. Paste this: I'm syncing task state to an agent with delta updates — only sending what changed. Show me a concrete counter-example where one dropped event causes permanent state drift, and then show me the full-list version that makes dropped events safe. I want to understand the trade-off in token cost versus correctness.",
        "command": "I'm syncing task state to an agent with delta updates — only sending what changed. Show me a concrete counter-example where one dropped event causes permanent state drift, and then show me the full-list version that makes dropped events safe. I want to understand the trade-off in token cost versus correctness.",
        "segment": "Why sending the full list beats sending only what changed",
    },
    "claude-cookbooks-cheap-worker-crew-reads-9": {
        "narration": "Your turn. Paste this: I need to summarize nine research papers and I want to use a hybrid crew — one frontier model to coordinate and cheaper models to read. Show me the task allocation logic: how many papers per worker, which model ID for each tier, and how the coordinator synthesizes the summaries without re-reading the papers.",
        "command": "I need to summarize nine research papers and I want to use a hybrid crew — one frontier model to coordinate and cheaper models to read. Show me the task allocation logic: how many papers per worker, which model ID for each tier, and how the coordinator synthesizes the summaries without re-reading the papers.",
        "segment": "Why a cheap-worker crew reads 9 papers for a third less — at identical quality",
    },
    "claude-for-legal-one-context-flag-flips-every": {
        "narration": "Your turn. Paste this: I'm building a legal review assistant. Show me how a single context flag — vendor-side versus customer-side — should flip the indemnification, liability cap, and IP license positions to their mirror image. Give me the system prompt structure and the two flag values.",
        "command": "I'm building a legal review assistant. Show me how a single context flag — vendor-side versus customer-side — should flip the indemnification, liability cap, and IP license positions to their mirror image. Give me the system prompt structure and the two flag values.",
        "segment": "Why one context flag flips every legal position to its mirror image",
    },
    "claude-quickstarts-waiting-each-result-before-next": {
        "narration": "Your turn. Paste this: I'm automating browser interactions and I'm waiting for each action result before issuing the next click. Show me which actions are safe to batch in one turn versus which require waiting on the result, and give me the decision rule I should apply at each step in the sequence.",
        "command": "I'm automating browser interactions and I'm waiting for each action result before issuing the next click. Show me which actions are safe to batch in one turn versus which require waiting on the result, and give me the decision rule I should apply at each step in the sequence.",
        "segment": "Why waiting for each result before the next click wastes time the agent knew it didn't need",
    },
    "cwc-long-running-agents-agent-will-mark-feature-done": {
        "narration": "Your turn. Paste this: my agent marks features done by running the tests and writing a result file — but it sometimes marks done without proof. Show me how to write a PreToolUse hook that intercepts the file write, checks whether the test results actually exist and are green, and blocks the write if they don't.",
        "command": "My agent marks features done by running the tests and writing a result file — but it sometimes marks done without proof. Show me how to write a `PreToolUse` hook that intercepts the file write, checks whether the test results actually exist and are green, and blocks the write if they don't.",
        "segment": "Why an agent will mark a feature 'done' without proof — and how a hook makes proof structural",
    },
    "cwc-workshops-cutting-402-line-agent-prompt": {
        "narration": "Your turn. Paste this: I have a 402-line agent prompt and the agent is slow and makes more mistakes than it should. Show me the splitting strategy — what moves to on-demand skills versus stays in the core prompt, and how I write a switch-case router that selects the right skill without reading all 402 lines every turn.",
        "command": "I have a 402-line agent prompt and the agent is slow and makes more mistakes than it should. Show me the splitting strategy — what moves to on-demand skills versus stays in the core prompt, and how I write a switch-case router that selects the right skill without reading all 402 lines every turn.",
        "segment": "Why cutting a 402-line agent prompt in half — while keeping every fact — makes it faster and better",
    },
    "financial-services-untrusted-document-s-hidden-instructions": {
        "narration": "Your turn. Paste this: I'm building a financial reconciler that processes counterparty statements that may contain prompt injection payloads. Show me the defense-in-depth architecture — which layer catches the payload, how I isolate document processing from write tools, and what the trust boundary looks like in the system prompt.",
        "command": "I'm building a financial reconciler that processes counterparty statements that may contain prompt injection payloads. Show me the defense-in-depth architecture — which layer catches the payload, how I isolate document processing from write tools, and what the trust boundary looks like in the system prompt.",
        "segment": "Why an untrusted document's hidden instructions never reach the write tool",
    },
    "healthcare-no-family-history-pe-needs": {
        "narration": "Your turn. Paste this: I'm extracting family history from clinical notes and getting null for everything. Show me the three axes I need to track — who reported it, what time period it covers, and what explicitly negated it — and give me the data model that distinguishes a confirmed negative from a missing field.",
        "command": "I'm extracting family history from clinical notes and getting `null` for everything. Show me the three axes I need to track — who reported it, what time period it covers, and what explicitly negated it — and give me the data model that distinguishes a confirmed negative from a missing field.",
        "segment": "Why 'no family history of PE' needs three axes to mean anything",
    },
    "healthcare-prior-auth-ai-structurally-cannot": {
        "narration": "Your turn. Paste this: I'm designing a prior authorization AI and I need to make sure it structurally cannot issue a denial — only approve or pend. Show me the output schema that enforces this constraint, and explain how the human review queue for pended cases should be structured so reviewers get the right context to resolve ambiguity.",
        "command": "I'm designing a prior authorization AI and I need to make sure it structurally cannot issue a denial — only approve or pend. Show me the output schema that enforces this constraint, and explain how the human review queue for pended cases should be structured so reviewers get the right context to resolve ambiguity.",
        "segment": "Why the prior-auth AI that structurally cannot say 'no' is the correct design",
    },
    "healthcare-swapping-fast-model-made-whole": {
        "narration": "Your turn. Paste this: I replaced my frontier model with a faster cheaper one and my pipeline got slower — because rescue rate went up. Show me how to design a benchmark that measures true throughput including rescues, not just per-call latency, and how to use that benchmark to find the right model for my actual workload.",
        "command": "I replaced my frontier model with a faster cheaper one and my pipeline got slower — because rescue rate went up. Show me how to design a benchmark that measures true throughput including rescues, not just per-call latency, and how to use that benchmark to find the right model for my actual workload.",
        "segment": "Why swapping in the 'fast' model made the whole pipeline slower",
    },
    "launch-your-agent-autonomous-agent-freeze-mid-run": {
        "narration": "Your turn. Paste this: I want my autonomous agent to pause mid-run and wait for a human to approve a destructive action — like merging a PR — before continuing. Show me how to implement the approval gate using a custom tool and a session-state flag so the agent resumes exactly where it left off after the human responds.",
        "command": "I want my autonomous agent to pause mid-run and wait for a human to approve a destructive action — like merging a PR — before continuing. Show me how to implement the approval gate using a custom tool and a session-state flag so the agent resumes exactly where it left off after the human responds.",
        "segment": "Why an autonomous agent can freeze mid-run and wait for a human indefinitely",
    },
}

fixed_count = 0
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
        bid = beat.get("beat_id", beat.get("id", ""))
        if bid == "YOURTURN":
            beat["narration_text"] = patch["narration"]
            shot = beat.setdefault("shot", {})
            if "remotion" in beat and "remotion" not in shot:
                shot["remotion"] = beat.pop("remotion")
            shot.setdefault("type", "REMOTION")
            remotion = shot.setdefault("remotion", {})
            remotion["pattern"] = "ClaudeComposerAsk"
            props = remotion.setdefault("props", {})
            props["greeting"] = "Your turn."
            props["command"] = patch["command"]
            props["segment"] = patch["segment"]
            props.setdefault("topic", "CLAUDE AGENT SKILLS · @NikBearBrown")
            props.setdefault("folderLabel", "@NikBearBrown")
            props.setdefault("modelLabel", "Claude Sonnet")
            props.setdefault("runningText", "paste your agent code or prompt…")
            fixed = True
            break
    if fixed:
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed_count += 1
        print(f"FIXED: {slug}")
    else:
        print(f"WARN (YOURTURN beat not found): {slug}")

print(f"\nDone. {fixed_count}/{len(PATCHES)} fixed.")
