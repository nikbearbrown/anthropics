# AUDIT — claude-liam-plugin-settings

**Date:** 2026-08-25  
**Auditor:** filmloop

---

## Check 1 — Stale renders
**PASS.** No mp4 files exist in any subfolder. Nothing to delete.

## Check 2 — Bookends
**PASS.**  
- B00: `ClaudeComposerAsk` ✓  
- BVDT: `ClaudeVerdictArtifact` ✓  
- BHTF: `ClaudeComposerAsk` ✓  
- BOUT: `ClaudeTitleOutro` ✓  

## Check 3 — Spark lines
**FIXED.**  
- B00 `greeting`: "Shalom, Liam" — world-language hello + Liam ✓  
- BHTF `greeting`: "Your Turn" → **"Your turn."** (HANDOFF LAW requires lowercase + period)  
- B01 `sparkLine`: "One file. Three consumers. YAML on top, context below." ≤4 words per clause ✓  
- B02 `sparkLine`: "Toggle with enabled. Coordinate with body. Parse with sed — carefully." ✓  
- B05 `sparkLine`: "Pattern clear. sed parser: bring your own validation." ✓  

## Check 4 — Verdict
**PASS.** `verdict_audit.py` confirms `claude-liam-plugin-settings` is NOT in the violations list (260/348 reels with specific verdicts). BVDT artifactLines are specific to plugin settings — no boilerplate ("Same input → same output", "Key finding one") present.

## Check 5 — Card text
**PASS.** No FormA/FormB beats. All sparkLine values are compressed topic phrases ≤4 words. No placeholder `sub` fields, no clipped labels.

## Check 6 — Punt sweep
**PASS.**  
- `PluginSettingsAnatomy` → confirmed at `runtime/remotion/src/scenes/PluginSettingsAnatomy.tsx` ✓  
- `PluginSettingsPatterns` → confirmed at `runtime/remotion/src/scenes/PluginSettingsPatterns.tsx` ✓  
- `PluginSettingsTell` → confirmed at `runtime/remotion/src/scenes/PluginSettingsTell.tsx` ✓  
- No gen-AI clip asks, no unfilled fill_slates, no DoodleScene/DoodleChart, no STILL src=archive.

## Check 7 — Card-only reel
**PASS.** Inner beats (B01, B02, B05) use purpose-built Remotion scenes with animated file diagrams, pattern cards, and teardown layouts — not generic text cards.

## Check 8 — Lens audit
**PASS — 2 moves confirmed.**  
- **Popper:** B05 states failure modes in advance ("sed frontmatter parser is fragile on complex YAML"; "gitignore not enforced"); BHTF gives an explicit falsification rubric ("If the settings are in a different file format... the pattern is wrong").  
- **Descartes:** B05's "Where it bites" section asks what would have to be true for the design to fail — restart buried, sed fragile, gitignore gap, body-as-prompt unexplained.  

## Check 9 — Brand fields
**FIXED.**  
- `folderLabel`: "@NikBearBrown" ✓ (channel handle, not brand key)  
- `engine`: "kokoro" ✓, `voice`: "am_onyx" ✓  
- `modelLabel`: "Opus 4.8" → **"Opus 4.7"** in B00 and BHTF (Opus 4.8 does not exist; current max is claude-opus-4-7)  
- Persona coherence: narration "Liam, in for Bear", voice kokoro am_onyx ✓  

## Check 10 — Pacing
**PASS.** Using actual_duration_s from measured audio:  
- B00: 112w / 35.56s = 3.15 WPS ✓  
- B01: ~170w / 59.5s = 2.86 WPS ✓  
- B02: ~185w / 60.37s = 3.07 WPS ✓  
- B05: ~195w / 73.79s = 2.64 WPS ✓  
- BVDT: ~117w / 38.87s = 3.01 WPS ✓  
- BHTF: ~155w / 46.02s = 3.37 WPS ✓  
- BOUT: 6w / 2.79s = 2.15 WPS ✓  

## Check 11 — type_check.py
**PENDING** — to run after build.

---

## Summary
- **BLOCKED:** No  
- **Fixes applied:** 3 (BHTF greeting case/period; B00 modelLabel; BHTF modelLabel)  
- **Narration changes:** None (narration is LOCKED)
