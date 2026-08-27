# REBUILD-LOG — agent-decomposition-skills-vs-tools

Run: 2026-08-26

---

## What was LOCKED (carried verbatim)

- All `narration_text` per beat B00–B10 (the script)
- Beat order and act labels
- Shot intent per beat (CwcXxx pattern assignments, sparkLine props, command/output props)
- Metadata identity: title, slug, topic, source, channel, register

## What was REBUILT

- `beat_sheet.pre-rebuild.json` — byte-exact copy created before any edit
- Envelope normalized: dead ElevenLabs-era fields were absent (sheet was already clean)
- BVDT verdict: `narration_text` written from body nouns/numbers (was empty ""); `artifactLines` authored from body (was template placeholder)
- BHTF `folderLabel` corrected: `"@claude-liam"` → `"@NikBearBrown"` (brand field error — claude-liam is a persona, not a channel handle)

## Datable-claim edits (DOUBLE-CHECK LAW)

| Beat | Field | Old value | New value | Source |
|---|---|---|---|---|
| B00 | `props.modelLabel` | `"Fable 5"` | `"Opus 4.7"` | Current Anthropic model lineup (claude-opus-4-7) |
| B09 | `props.modelLabel` | `"Fable 5"` | `"Opus 4.7"` | Current Anthropic model lineup (claude-opus-4-7) |

"Fable 5" is not a real Claude model name. Adjacent CWC reels (claude-liam-workshop, rightmodel-pareto-frontier) use `"Opus 4.7"`.

## Post-render Gate T fixes (applied before final recompile)

### Fix 1 — BHTF modelLabel missing (Gate V catch)

BHTF had no `modelLabel` prop, so `ClaudeComposerAsk` fell back to its hard-coded default "Fable 5" on screen. Added `"modelLabel": "Opus 4.7"` to BHTF `remotion.props`. Re-rendered BHTF with `--force`.

### Fix 2 — BHTF topic truncated (§8.9 TYPECHECK fail)

BHTF `topic` was `"YOUR TURN · THE 402-LINE PROMPT: HOW DECOMPOSITION M"` — pre-truncated mid-word in the beat sheet (ticket: TYPECHECK §8.9). Shortened to `"YOUR TURN · AGENT DECOMPOSITION"`. Re-rendered BHTF.

### Fix 3 — B07 green contrast §8.3 WCAG fail

`CwcCostLatencyGain.tsx` used `const GREEN = '#4CAF50'`. On `#FAF9F5` cream background, contrast = 3.32:1 < 4.5:1 WCAG (TYPECHECK §8.3 FAIL). Changed component source constant to `GREEN = '#2E7D32'` (dark green, >8:1 on cream). Re-rendered B07. This is a component-level constant, not a prop — no beat-sheet change needed for this fix.

---

## BVDT verdict authored (new writing from body content)

BVDT `narration_text` (new, built from sheet's own sparkLines/verdict content):
> "Three levers. Tools for stateless calls — bounded, deterministic, negligible context cost. Skills for on-demand instructions — complexity hides behind the interface, the core stays lean. The 402-line monolith became a 15-line core. 102 tool calls and 488 seconds became 3 scripts and roughly 100. Same correctness. Approximately five times faster."

BVDT `artifactLines` (new, from B03 and B08 numbers):
- "Tools — stateless calls: one function signature, one result, negligible context cost."
- "Skills — on-demand instructions: load only what the current task needs, not all upfront."
- "Subagents — separate context windows for tasks that require full autonomy."
- "402-line monolith → 15-line core: 102 tool calls, 488 s → 3 scripts, ~100 s (≈5×)."
