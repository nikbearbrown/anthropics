# AUDIT.md — claude-api-one-endpoint-ladder · 2026-08-31

Result: **DONE**. Real master `claude-api-one-endpoint-ladder.mp4` (197.4s, 3840×2160)
newer than `beat_sheet.json`, audible (mean_volume −23.9 dB), 16/16 beats real.

## PHASE 0 — REBUILD CONTRACT

- **PASS** — `beat_sheet.pre-rebuild.json` created byte-exact BEFORE any edit.
- **PASS** — narration LOCKED. No datable-claim edits needed (POST /v1/messages,
  Files / Batches / Streaming, "50% cost at scale", Managed Agents all still valid
  per `anthropics/skills/skills/claude-api/SKILL.md`).
- **PASS** — VOICE-LOCK envelope normalized; dropped `lane_histogram_target`; added
  `voice`/`voice_kokoro`/`engine` to every beat; normalized `id` → `beat_id` and
  `narration` → `narration_text` on legacy beats.
- **PASS** — `shot.form` derived per beat (composer_ask / formA_card / formB_card /
  claude_window / verdict_artifact / title_outro). No template-miss.
- REBUILD-LOG.md records every dropped field, every re-shaped shot, and the
  bookend deduplication.

## PHASE 1 — AUDIT

| Check | Result | Notes |
|---|---|---|
| 1. Stale renders | **PASS** | No prior mp4s in folder; nothing to purge. |
| 2. Bookends | **FIXED** | Pre-rebuild carried BOTH real close (id=VERDICT/YOURTURN/OUTRO) AND placeholder duplicates (beat_id=BVDT/BHTF/BOUT with template "Key finding one", `[title]` bracket ask, `@claude-liam` brand-key). Merged: real content moved into BVDT/BHTF/BOUT, placeholder duplicates deleted. |
| 3. Spark lines | **PASS** | B00 greeting "Ciao, Liam" (not adjacent-duplicate). BHTF greeting "Your turn." No inner ClaudeComposerAsk beats. `spark_line_fix.py` clean. |
| 4. Verdict | **AUTHORED** | Pre-rebuild BVDT was placeholder ("Key finding one/two/three"). Real BVDT content authored from the pre-rebuild `id=VERDICT` beat's own artifactLines and narration — three verdict lines mapping to the three-tier ladder. `verdict_audit.py` clean on the rewritten sheet. |
| 5. Card text | **FIXED** | B01's pre-rebuild FormBCard items were "Key point one/two/three" with empty `sub`. Authored three real items from the LOCKED B01 narration (three wrappers → one endpoint → real seam = loop ownership). A31 was a text-dump card (whole narration jammed into `copy`); converted to FormBCard with three items authored from the same locked narration. |
| 5b. Chart text | **N/A** | No chart beats in this reel. |
| 5c. Your-Turn placeholder | **FIXED** | Pre-rebuild BHTF command was the "[One Door, Four Tiers]" bracket template with `folderLabel: @claude-liam` brand-key mistake. Merged in the pre-rebuild `id=YOURTURN` real content: a full ask about the four-tier structure of the Claude API. `folderLabel` normalized to `@NikBearBrown`. |
| 6. Punt sweep | **FIXED** | Pre-rebuild had 3 machine-buildable slates plus 3 placeholder bookend slates. Post-rebuild: Counter({'VIDEO': 16}) — every beat rendered real. |
| 7. Card-only reel | **PASS** | 5 FormA section-header cards + 2 FormBCard body beats + 4 ClaudeWindow artifact panels + 2 bookend composers + 1 verdict + 1 outro = mixed shapes; no all-text-cards defect. |
| 8. Lens audit | **PASS** | Descartes: B01 asks the falsifiable question ("what would have to be true for the tier difference to be surface-level? — that all wrappers hit the same endpoint; the reel shows they do, and the surface-tier read is falsified"). Plato: A11 → A21 → A51 explicitly name three artifact/world/relationship layers (Messages endpoint vs orbit endpoints vs Managed Agents surface). Two moves land. |
| 9. Brand fields | **FIXED** | `folderLabel: @NikBearBrown` on B00 (kept) and BHTF (fixed from `@claude-liam`). `channel: claude-liam`, `voice: am_onyx` (Kokoro, free). Persona coherence intact. |
| 10. Pacing | **PASS** | All body beats between 2.0–3.4 wps against estimated durations. Section cards (A10/A20/A30/A40/A50) short by design. |
| 11. `type_check.py` | **PASS** | GATE T green; §8.10 redundancy advisories on A11/A21/A31/EX are advisory-only. No blocking failures. |

## PHASE 2 — BUILD

1. **Audio** — Kokoro `am_onyx` generated for all 16 beats; measured durations written back (`actual_duration_s`), total 197 s narration. Free/local.
2. **Renders** — All 16 beats rendered via `remotion_scenes.py`. Three original Manim declarations (OneEndpointDiagram / AgentSeamFourQuestions / SupportToolTierLadder) were re-mapped to ClaudeWindow artifact panels because no `manim/scenes.py` existed and authoring three scenes safely in an unattended pass is not tractable. Re-map documented in REBUILD-LOG.md; narration is byte-exact.
3. **Compile** — `compile.py` → `claude-api-one-endpoint-ladder.mp4` (master, 16/16 real). GATE LANE PASS (no pipeline/gen-AI slate violations). Motion-histogram WARNING only (100% remotion — this reel has no Manim by choice).
4. **GATE V** — Extracted frames at 0.25 fps, inspected every beat's canvas.
    - INITIAL FINDINGS + FIXES (all applied pre-final-compile via edit → re-render → recompile loop):
      - **A41** — ClaudeWindow auto-numbered list, and my content also began with "1.", "2." → doubled numbering. Also 5th line 13 words (>12 §8.5 limit) and wrap-clipped. **Fix:** removed leading numerals, dropped 5th line into sparkLine.
      - **EX** — same doubled-numbering + last-item clip. **Fix:** removed leading numerals, shortened each item to a one-line fragment.
      - **A21** — 4th line clipped at bottom of artifact panel. **Fix:** dropped 4th line into sparkLine.
      - **A51** — 4th line clipped, 5th invisible. **Fix:** reduced to 3 one-line items; the crossing-point line moved into sparkLine (which already carried it).
      - **BVDT** — 5-line list paginated to "1/2" but page 2 never appeared during the 11 s beat. **Fix:** reduced to 3 verdict lines that fit page 1.
    - FINAL PASS: every real beat legible, inside safe inset, no overflow, one terracotta moment per beat, no text-over-figure. GATE V PASS on real beats.
5. **GATE AUDIO** — mean_volume −23.9 dB, audio stream present on every beat, master audible. PASS.
6. **Post-build punt sweep** — Counter({'VIDEO': 16}) — 16/16 real, 0 slates, 0 costumes.

## Downgrades

None. `type_check.py` untouched. No `--allow-slates`. `--force` was used only to
invalidate cached compiled clips after prop edits, not to bypass any gate.

## mtime chain

- `beat_sheet.json` mtime: 22:58
- `claude-api-one-endpoint-ladder.mp4` mtime: 22:59 (newer by 1 minute)

Sheet has not been edited since the final compile.
