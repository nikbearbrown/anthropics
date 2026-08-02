#!/usr/bin/env python3
"""Patch claude-skills reels: author YOURTURN narrations; fix 4 placeholder commands."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

# slug -> { beat_id, narration, command (only if placeholder needs replacing) }
PATCHES = {
    # ── 16 claude-liam-* reels: command already authored; add narration only ──
    "claude-liam-brand-guidelines": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I have a deck I want to make look like it came from Anthropic — apply the brand-guidelines skill, start with the color system, and tell me what you're changing and why before writing any code. Notice whether it explains the palette logic or just applies it.",
    },
    "claude-liam-canvas-design": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I have a concept for a meditation-retreat-in-the-mountains poster — use the canvas-design skill, show me the design philosophy and the conceptual soul of the piece before writing any code. Watch for whether it commits to a visual decision or hedges.",
    },
    "claude-liam-claude-api": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I want to call the Claude API from Python using extended thinking — check the claude-api skill for the current thinking parameter shape, the exact model ID, and any drift from your training prior, then show me a working example. The skill check is the point — it surfaces drift.",
    },
    "claude-liam-doc-coauthoring": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I need to write a decision doc on whether to migrate our auth service to OAuth 2.0 — walk me through the doc-coauthoring workflow. Notice whether it drafts the doc or structures your thinking first.",
    },
    "claude-liam-docx": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I want a one-page technical memo as a Word document — US Letter, header, heading styles, a two-column table, footer with page numbers — use the docx skill. Check whether the output opens in Word without style warnings.",
    },
    "claude-liam-example-skill": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: build a model-invoked skill for database query optimization in my plugin. Pay attention to how it structures the SKILL.md — what it commits to and what it leaves open for your schema.",
    },
    "claude-liam-frontend-design": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: design a landing page for a handmade ceramic studio — strong visual identity, distinctive typography, considered palette, one element I won't have seen elsewhere — use the frontend-design skill. Push back if it lands on something generic.",
    },
    "claude-liam-internal-comms": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: write a 3P update for the Product Design team — progress on onboarding redesign, plans for user testing, blocked on design system approvals — use the internal-comms skill. Check whether the Problems section is honest or softened.",
    },
    "claude-liam-pdf": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: I have a scanned invoice as a PDF called invoice.pdf — extract all text, pull out any tables, save tables to Excel — use the PDF skill. Try it with a real invoice and check whether the table cells line up correctly.",
    },
    "claude-liam-pptx": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: five-slide investor pitch for a carbon-capture hardware startup — bold design, topic-specific palette, dark-light sandwich, one visual motif — use the PPTX skill. The motif test: open the deck and check whether slides 1, 3, and 5 feel like the same film.",
    },
    "claude-liam-skill-creator": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: create a skill that summarizes meeting transcripts into structured action items — start from scratch, define the skill, write the SKILL.md, run the eval loop. The interesting moment is the eval: what does it actually test?",
    },
    "claude-liam-skill-development": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: create a skill for my plugin called pdf-editor that handles rotating PDFs and converting pages to images. Check whether it writes the phase gates clearly enough that you could hand this SKILL.md to someone else.",
    },
    "claude-liam-slack-gif-creator": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: make me a pulsing fire emoji GIF for Slack — smooth loop, energetic, under three seconds — use the Slack GIF Creator skill. Test the loop: play it ten times and check whether the seam is invisible.",
    },
    "claude-liam-web-artifacts-builder": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: build a note-taking app with tags, search, and a markdown editor as a shareable claude.ai artifact — use the Web Artifacts Builder. Try the search after adding three notes — does it filter in real time?",
    },
    "claude-liam-webapp-testing": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: test my local React app on port 3000 — verify clicking Submit on the login form shows a success message — use the Web Application Testing skill. The tell is whether it writes assertions or just clicks and reads the DOM.",
    },
    "claude-liam-xlsx": {
        "beat_ids": ["BHTF"],
        "narration": "Your turn. Paste this: build a three-year SaaS revenue model — growth rate and gross margin assumptions, revenue, COGS, and gross profit projections — deliver as .xlsx. Open the file and check whether the formulas reference the assumption cells or hard-code the numbers.",
    },
    "what-is-claude-skills": {
        "beat_ids": ["B06", "YOURTURN"],
        "narration": "Your turn. Paste this: read this SKILL.md as a skeptic — what will it do that I wouldn't expect from the name, what does it assume about my setup, and where would it do a bad job? Apply it to any SKILL.md in this playlist.",
    },
    # ── 4 skills-* reels: command is placeholder — replace command AND add narration ──
    "skills-50-round-agent-survives-past": {
        "beat_ids": ["YOURTURN"],
        "narration": "Your turn. Paste this: I'm building a coding agent that runs for many rounds of tool calls. Walk me through the three options when context fills up — checkpoint, summarize, or restart — and what each one costs in terms of task continuity. Ask Claude to recommend one for a stateful file-editing agent.",
        "command": "I'm building a coding agent that runs for many rounds of tool calls. Walk me through the three options when context fills up — checkpoint, summarize, or restart — and what each one costs in terms of task continuity. Then recommend one for a stateful file-editing agent.",
        "segment": "Why a 50-round agent survives past its own memory limit",
        "running": "paste your agent loop code…",
    },
    "skills-claude-spends-5000-thinking-tokens": {
        "beat_ids": ["YOURTURN"],
        "narration": "Your turn. Paste this: I'm using extended thinking and Claude spends more tokens on simple questions than hard ones. Explain how budget_tokens actually works — ceiling, target, or hint — and show me how to set it for a pipeline that mixes trivial lookups with multi-step reasoning.",
        "command": "I'm using extended thinking and Claude spends more thinking tokens on simple questions than hard ones. Explain how `budget_tokens` actually works — is it a ceiling, a target, or a hint — and show me how to calibrate it for a pipeline that mixes trivial lookups with multi-step reasoning.",
        "segment": "Why Claude spends 5000 thinking tokens on \"2+2\" and 100 on a hard proof",
        "running": "paste your thinking config…",
    },
    "skills-claude-write-right-spreadsheet-formula": {
        "beat_ids": ["YOURTURN"],
        "narration": "Your turn. Paste this: Claude wrote the correct formula in my spreadsheet but the cell shows the wrong number. Explain why — what the xlsx format stores versus what a recalculation engine computes — and show me the tool-call sequence that forces the correct value to appear.",
        "command": "Claude wrote the correct formula in my spreadsheet but the cell shows the wrong number. Explain why — what the xlsx format stores versus what a recalculation engine computes — and show me the tool-call sequence that forces the correct value to appear after writing.",
        "segment": "Why Claude can write the right spreadsheet formula and the file still shows the wrong number",
        "running": "paste your xlsx-writing code…",
    },
    "skills-number-s-color-financial-model": {
        "beat_ids": ["YOURTURN"],
        "narration": "Your turn. Paste this: I'm reading a financial model with blue, black, green, and red cells. Give me the convention — what each color signals about whether it's an input, formula, cross-tab link, or external reference — and tell me which ones I can safely edit without breaking the model.",
        "command": "I'm reading a financial model with blue, black, green, and red cells. Give me the convention — what each color signals about whether it's an input, formula, cross-tab link, or external reference — and tell me which ones I can safely edit without breaking the model.",
        "segment": "Why a number's color in a financial model tells you whether you're allowed to touch it",
        "running": "paste your financial model structure…",
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
        if beat.get("beat_id") in patch["beat_ids"]:
            beat["narration_text"] = patch["narration"]
            # get or build shot.remotion.props
            shot = beat.setdefault("shot", {})
            if "remotion" in beat and "remotion" not in shot:
                shot["remotion"] = beat.pop("remotion")
            shot.setdefault("type", "REMOTION")
            remotion = shot.setdefault("remotion", {})
            remotion.setdefault("pattern", "ClaudeComposerAsk")
            props = remotion.setdefault("props", {})
            props["greeting"] = "Your turn."
            props.setdefault("topic", "CLAUDE SKILLS · @NikBearBrown")
            props.setdefault("folderLabel", "@NikBearBrown")
            props.setdefault("modelLabel", "Claude Sonnet")
            # override command only for the 4 placeholder reels
            if "command" in patch:
                props["command"] = patch["command"]
            if "segment" in patch:
                props["segment"] = patch["segment"]
            if "running" in patch:
                props["runningText"] = patch["running"]
            fixed = True
            break
    if fixed:
        with open(path, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        fixed_count += 1
        print(f"FIXED: {slug}")
    else:
        print(f"WARN (beat not found): {slug}")

print(f"\nDone. {fixed_count}/21 fixed.")
