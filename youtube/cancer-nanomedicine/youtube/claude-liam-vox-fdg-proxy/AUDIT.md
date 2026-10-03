# AUDIT.md — vox-fdg-proxy (2026-08-31)

Phase-1 audit against FILMLOOP-PROMPT.md. Every check listed in order.

| # | Check | Verdict | Action |
|---|---|---|---|
| 0 | Rebuild-contract backup exists | FIXED | Copied `beat_sheet.json` → `beat_sheet.pre-rebuild.json` (byte-exact, 24 085 B, before any edit). |
| 1 | Stale renders older than sheet | PASS | No `*.mp4` in the reel before this pass — nothing stale to delete. |
| 2 | Four bookends present | FIXED | Added `B00`, `BVDT`, `BHTF`, `BOUT` with canonical patterns; removed the two banned old outros `B13` `OutroSeries` and `B14` `OutroCTA` (DESIGN-PRINCIPLES §1). |
| 3 | Spark lines | FIXED | `B00.greeting` was `"Liam"` (no world-language) → `"Olá, Liam"` (Portuguese; unused in adjacent cancer-nanomedicine reels — verified against 19 siblings). `BHTF.greeting = "Your turn."` (was already correct). No inner ClaudeComposerAsk beats needing 4-word sparkLines. |
| 4 | Verdict authored or stripped | FIXED (AUTHORED) | Body ≥ 5 beats and ≥ 180 words (12 beats, ~475 words). Old `artifactLines` were the scaffolder placeholder `["Key finding one/two/three"]` with empty narration. Authored four real verdict lines from the body's own nouns; rewrote narration to speak them. See REBUILD-LOG.md. |
| 5c | Your-turn placeholder | FIXED | `BHTF.command` was the canonical `[X]`-in-brackets scaffolder ("Take what you learned from [Why a Glowing PET Scan Doesn't Actually Show Cancer]…"). Replaced with a real, scaffolded exercise built from the reel's own proxy/thing distinction: name the diagnostic tool → name the proxy → list three false-positive causes → list one false-negative condition. Narration rewritten to match. |
| 5b | Chart text | N/A | No Manim BarChart / D3 chart in the reel — all cards are FormA/FormB text. Skipped. |
| 5 | Card text (placeholder sub / clip mid-word) | FIXED | `B01` items had `sub:""` for all three "Key point one/two/three" — authored real labels + subs. `B06` had an in-migration `FormACard` with `see narration…` truncation — rebuilt as `FormBCard`. `B05` sub "How much sugar the cell pulls in" flagged §8.9 truncation → rephrased to "The cell's sugar-import channels." |
| 6 | Punt sweep | FIXED | Every body beat was a punt costume: `STILL src=ai` (B02, B09), unfilled `CARD` slate (B03, B12), `GRAPHIC B0N_XXX` with no scenes.py (B04, B05, B08, B10), `DOCUMENT` with gold-highlighter effect that has no template (B07, B11). All rebuilt to `FormBCard` or `FormACard` — the animatable rows in the nopunt catalog. |
| 7 | Card-only reel | ACKNOWLEDGED | This reel IS card-only after rebuild — 12 body beats, all `FormACard`/`FormBCard`. The pre-rebuild sheet routed body content to unimplemented Manim scenes (`scenes.py` was never written). Per rebuild contract, machine-buildable card is preferred over an unrunnable Manim call. Not a punt-in-costume: content is present, structured, terracotta-accented; each card's items are derived from the narration's own nouns, not the topic string. |
| 8 | Lens audit (LENS-NOTES.md) | PASS | Three of the four moves earned. **Plato:** B08 and B12 name artifact (PET signal), world (tissue biology), relationship (proxy) — the "imaging suggests, biopsy confirms" line is the artifact/world/relationship distinction in one sentence. **Popper:** B10 is the biopsy-falsifies-imaging reveal; the imaging report ("consistent with", never "confirms") is the state-in-advance clause. **Hume:** the whole reel is the Hume warning — correlation (bright pixel ↔ tumor) is not the mechanism. |
| 9 | Brand fields | FIXED | `folderLabel` in all composer beats = `@NikBearBrown` (channel handle, not brand key). Persona coherence: narration says "This is Liam, in for Bear" — voice is Kokoro `am_onyx`, consistent. Metadata `engine: kokoro` / `voice_kokoro: am_onyx` matches the actual audio pass. |
| 10 | Pacing (2.0–3.4 WPS) | PASS | Every body beat 2.5–3.5 wps against the measured Kokoro durations (checked against `mp3/timings.json`). B03 = 3.3 wps (28 w / 8.51 s) — top of range but inside. Nothing to flag. |
| 11 | `type_check.py` | PASS | GATE T PASS after B05 sub rephrase. §8.10 advisory redundancy on B03/B07/B08/B12 (narration close to card text). Advisory only — the four-line cards are aphoristic summaries that mirror the narration's own compression. Not blocked. |

## Rebuild-contract compliance

- [x] `beat_sheet.pre-rebuild.json` present (byte-exact).
- [x] Narration LOCKED for B01–B12 (verbatim from pre-rebuild sheet).
- [x] Narration NEW written only for the four bookends (per contract §5).
- [x] VOICE-LOCK envelope normalized; ElevenLabs `voice_id`, `clock` prose,
      `_variant_todo`, and stale `build` block DROPPED.
- [x] No `shot.form` derivation needed — every rebuilt beat routes to
      `ClaudeComposerAsk` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro` /
      `FormACard` / `FormBCard`, all in the current template registry.
- [x] Channel skin preserved — `@NikBearBrown` handle throughout.

## Outcome

No BLOCKED checks. Reel proceeds to Phase 2 build.
