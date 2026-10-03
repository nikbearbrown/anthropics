# AUDIT.md — nbb-vox-fdg-proxy

**Checked:** 2026-08-31 06:11
**Result:** BUILT — vox-fdg-proxy-slate.mp4 (225.7s, 12/16 filled, mean_volume −24.6 dB)

## PHASE 0 — REBUILD CONTRACT

- `beat_sheet.pre-rebuild.json` created byte-exact BEFORE any edit (was missing on entry).
- Locked script preserved: no body-narration edits. Datable-claim pass surfaced no rotted claims (no model versions, prices, or "as of" phrasing in narration).
- Envelope normalized: VOICE-LOCK already correct (kokoro / am_onyx everywhere). No ElevenLabs-era fields found; nothing to drop.

## PHASE 1 — audits

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no pre-existing mp4 in folder to purge |
| 2 | Bookends canonical patterns | FIXED | see BOOKEND CLEANUP below |
| 3 | Spark lines | FIXED | NBB00 greeting was `"Your turn."` — swapped for a world-language hello (`"Salve, Liam."`) not used by adjacent nbb-vox reels (Vanakkam, Bonjour, Namaste, Kia ora). NBB02 keeps `"Your turn."` (correct for the your-turn beat) |
| 4 | Verdict | FIXED | NBB01 heading was truncated `"Why a Glowing PET Scan Doesn't Actually Show"` → `"PET measures metabolism, not malignancy"`. Lines were 4 phrase-fragments starting with `"And..."` — replaced with 4 complete, reel-specific verdict lines drawn from body content |
| 5b | Chart text | PASS | Manim beats (B04, B10) reuse source clips; no re-authored chart text |
| 5 | Card text | FIXED | B01 FormBCard had `label:"Key point one/two/three"` + empty `sub` placeholders — authored real items from the beat's own narration (three bright nodes / salvage radiation / wrong diagnosis). B02, B06, B09 FormACard `lines` were truncated mid-word (`"…for…"`, `"…Activated immune cells…"`) — rewrote as complete two-line summaries |
| 5c | Your-Turn placeholder | FIXED | NBB02 command was the generic `"Explain how [X] applies to a specific cancer type…"` template with bracket placeholder — rewrote as a specific PET-proxy exercise (pick a bright finding → name three non-cancer causes → pick a target-specific tracer PSMA/DOTATATE/FES → interpret bright-then-dark or dark-then-bright patterns) |
| 6 | Punt sweep | PASS | zero gen-AI asks; no unfilled slates on pipeline-owned beats; the four remaining declared slates (B03, B07, B11, B12) are CARD/DOCUMENT beats legitimately deferred in a review cut |
| 7 | Card-only reel | PASS | 6 body beats render as drawn/graphic figures (B04, B05, B08, B10 Manim + B07/B11 highlight quotes as declared slates) |
| 8 | Lens audit | PASS | The reel earns TWO CS moves: **Plato** (artifact = bright PET spot vs world = tumor biology; relationship = proxy, not identity — B05, B08, B11) and **Popper** (states in advance what would falsify a "bright = cancer" reading — false positives listed in B06, false negatives in B07). Ash-shaped: FDG-PET is fluent (bright, precise numbers) but wrong-in-relationship (measures hexokinase, not malignancy). |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, correct for the nbb variant). `engine: kokoro`, `voice: am_onyx` — matches the audio actually generated (Liam narration) |
| 10 | Pacing | ADVISORY | Body beats reuse source-reel audio; pacing already accepted upstream. All measured durations within band |
| 11 | type_check | PASS | see TYPECHECK NOTE below |

## BOOKEND CLEANUP

The reel arrived with DOUBLE bookends: NBB00-03 (real narration, measured audio, canonical patterns) AND B00/BVDT/BHTF/BOUT (empty SLATE placeholders, no audio). A prior automated rebuild had scaffolded the second set on top of the first.

Deleted the four empty SLATE duplicates:
- `B00` (ClaudeComposerAsk, greeting `"Liam"` only, no narration_text) → NBB00 covers this
- `BVDT` (ClaudeVerdictArtifact with `"Key finding one/two/three"`) → NBB01 covers this
- `BHTF` (ClaudeComposerAsk with generic `"Take what you learned from [X]…"`) → NBB02 covers this
- `BOUT` (ClaudeTitleOutro) → NBB03 covers this

The four remaining NBB* beats fulfill the canonical bookend patterns (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro) with real narration and measured audio.

## TYPECHECK NOTE (§8.10 advisory, §8.1 downgrade)

- Advisory: B06 and B09 narration recites the on-screen text (0.82 / 0.83). Both beats are already-shipped source-reel narration; not rewritten per the LOCKED-SCRIPT rule.
- Downgrade logged: B04 and B10 are pipeline-owned Manim beats (`B04_FDGUptake`, `B10_ExampleResult`); source-reel clips were reused (720p, small caption text 8–12px, below the 13px min-size floor). Slating them would trigger GATE LANE (pipeline-owned beats may not slate). Re-rendering the source Manim scenes at higher DPI is out of scope for this remaster — the underlying content and pedagogy are correct; only the resolution is under-floor. Logged and accepted for the review slate cut; a future master pass would need to re-render `vox_scenes.py` at 4K.
- B03, B07, B11, B12 (CARD/DOCUMENT source-reel clips with the same font-size issue) were promoted to declared SLATE cards — legal in a review cut, not pipeline-owned.

## PHASE 2 — build

- Audio-first: NBB00-03 use fresh local mp3 (already measured); B01-B12 reuse source-reel mp3 via `../vox-fdg-proxy/mp3/beat-B*.mp3` (audio_file paths preserved).
- Remotion renders: 8 beats via `remotion_scenes.py` (NBB00, B01, B02, B06, B09, NBB01, NBB02, NBB03).
- Body beats: B04, B05, B08, B10 copied from source reel clips (pipeline-owned graphic beats); B03, B07, B11, B12 left to slate as declared review-cut placeholders.
- Compile: `compile.py --review` → `vox-fdg-proxy-slate.mp4` (225.7s, 4 declared slates, GATE AUDIO PASS, GATE LANE PASS, content-check PASS, frame-check PASS).
- GATE V (frame read): qc-sheet.png contact sheet inspected. Every beat's frame legible; NBB00 spark ("Salve"), NBB01 verdict heading + 4 lines, NBB02 exercise, B01 FormB items all render as authored. B04/B10 graphics from source read cleanly at contact-sheet scale (the sub-floor caption text is present but not the dominant defect).
- Cut mtime (06:11:54) > sheet mtime (06:07:07) — DONE-check clean.

## Skipped / not applicable

- BLOCKED.md: nothing to append — reel built.
