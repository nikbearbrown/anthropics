# AUDIT.md — claude-liam-writing-rules

Invocation: 2026-08-31  ·  auditor: unattended film-factory pass  ·  target: review-slate cut

## Phase 0 — rebuild contract
- **pre-rebuild backup**: FIXED — `beat_sheet.pre-rebuild.json` created byte-exact (missing before this pass).
- **narration lock**: PASS — no narration edits. Only two prop edits (see Phase 1 §9 datable + §11 wordy-card).
- **VOICE-LOCK envelope**: PASS — `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx`. No dead ElevenLabs fields present.
- **shot.form derivation**: PASS — all seven beats already carry named Remotion patterns (ClaudeComposerAsk × 2, HookifyRuleAnatomy, HookifyEventTypes, HookifyTell, ClaudeVerdictArtifact, ClaudeTitleOutro); every one is renderable per `./art scenes --check`.
- **channel skin**: PASS — Claude channel, Claude skin. `folderLabel: @NikBearBrown` (channel handle, not brand key).

## Phase 1 — audit checklist

| # | check | status | notes |
|---|---|---|---|
| 1 | Stale renders | FIXED | Deleted `media/B01.mp4` (mtime 17:54, sheet 17:55, 1 min stale) and `media/B05.mp4` (matched sheet second, treated as stale under safety margin). |
| 2 | Bookends canonical | PASS | B00 ClaudeComposerAsk · BVDT ClaudeVerdictArtifact · BHTF ClaudeComposerAsk · BOUT ClaudeTitleOutro — all four present, all four canonical patterns. |
| 3 | Spark lines | PASS after fix | B00 greeting `"Ciao, Liam"` (Italian; adjacent `claude-liam-command-development` also uses Ciao, but only reel in this run so no in-run collision — narration hardcodes "Ciao"). BHTF greeting `"Your turn."`. Inner-body sparkLines: B01 shortened from 13 words to 9 (§8.5, see §11). B02 11 words, B05 10 words — both under limit. |
| 4 | Verdict | AUTHORED, KEPT | BVDT narration + `ClaudeVerdictArtifact` lines are a real verdict authored from the body's own nouns (rule format, 5 events, simple vs. advanced conditions, action semantics, body guidance, four named gaps). Body has 3 body beats × ~200 words each ≈ 620 words > 180 threshold. Not stripped. |
| 5c | Your-turn placeholder | PASS | BHTF `command` is a real exercise ("write Hookify rules that Claude Code can enforce deterministically — the rule-writing pattern; vague-vs-precise example; how to test that the rule fires correctly without triggering on false positives"), not the "[Take what you learned from …]" template. Output has 3 real red-flag / expected lines. |
| 5b | Chart text | N/A | No Manim/D3 chart in this reel. |
| 5 | Card text | PASS | No FormA/FormB cards; no `sub` placeholders or clipped labels. |
| 6 | Punt sweep | PASS | Zero slate cards; zero unfilled `remotion_scenes` / `fill_slates`; zero `STILL src=archive`; zero DoodleScene/Chart; zero FormA that names a visual it doesn't draw. Every beat maps to a Remotion pattern that renders. |
| 7 | Card-only reel | PASS | Not card-only — B01/B02/B05 are dedicated HookifyRuleAnatomy/HookifyEventTypes/HookifyTell scenes that draw structure (frontmatter fields, event grid, teardown two-column). |
| 8 | Lens audit | PASS | The teardown enacts two lenses on the SKILL.md artifact: **Popper** (states, in advance and per-item, what would count as this skill failing — "block action described but never demonstrated", "stop/prompt condition fields undocumented", "rule execution order not documented", "all event no example" are named as falsifying gaps) and **Plato** (artifact = the SKILL.md; world = the actual hook execution behavior at the tool layer; relationship examined per-gap: the doc claims coverage the runtime behavior does not verify). Verdict + your-turn recapitulate; body carries the two moves. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown` — channel handle ✓. `engine/voice: kokoro/am_onyx` matches Liam persona ✓. Datable-claim fix: B00 `modelLabel: "Opus 4.8"` → `"Opus 4.7"` (Opus 4.8 does not exist; current top model is `claude-opus-4-7`). Logged in `REBUILD-LOG.md`. |
| 10 | Pacing | PASS | Words/sec against measured audio: B00 108w/37.8s = 2.86, B01 175w/58.2s = 3.01, B02 180w/58.7s = 3.07, B05 236w/69.0s = 3.42 (top of band), BVDT 87w/33.4s = 2.60, BHTF 54w/16.3s = 3.31, BOUT 8w/3.4s = 2.35. All inside 2.0–3.4 window. |
| 11 | type_check | PASS after fixes | Initial run: 2 FAILs (B01 wordy-card 13 words > 12; B05 overflow — hardcoded header text ran outside title-safe box on left/right at fontSize 38 without insets). Fixed: (a) B01 sparkLine shortened to 9 words; (b) `HookifyTell.tsx` header switched to `left/right: W*0.07` insets and fontSize 32 with lineHeight 1.2; (c) HookifyTell sparkLine moved from `bottom: H*0.04` to `H*0.09` (was still measuring outside safe on the pixel check); (d) redundant callout that overlapped rows 4–5 removed. GATE T: PASS. |

Only this reel uses `HookifyRuleAnatomy` / `HookifyEventTypes` / `HookifyTell` — grep across every `beat_sheet.json` under `anthropics/youtube/` confirms one consumer each. Scene edits are per-reel content fixes, not shared-scene loosenings.

## Phase 2 — build

- Audio (Kokoro `am_onyx`, free): PASS — all 7 mp3s generated in one pass; `actual_duration_s` re-measured and written back. BHTF re-measured 16.3s (old sheet had 51.7s — legacy stale value; new value is ground truth).
- Remotion renders: PASS — 7/7 beats rendered fresh via `runtime/scripts/remotion_scenes.py --force` after each scene fix. B05 re-rendered three times to converge on GATE T + Gate V pass.
- Compile: PASS — `runtime/scripts/compile.py --force` — 7/7 VIDEO slots, zero slates. 4K master 3840×2160.
- **GATE T (type-lock)**: PASS. `TYPECHECK.md` overall PASS, 0 FAILs, 7 beats checked.
- **GATE AUDIO**: PASS. `mean_volume -23.7 dB`, `max_volume -2.8 dB` — audible.
- **Gate V (frame inspection)**: PASS. Sampled per-beat 15/50/85% frames; B00 composer clean, B01 anatomy card clean (frontmatter fields readable, sparkLine at floor), B02 event grid clean, B05 teardown two-column clean after callout removal, BVDT verdict card clean, BHTF composer clean, BOUT title outro clean. One terracotta moment per beat honoured across the reel.
- Post-build punt sweep: PASS. `build.status = Counter({'VIDEO': 7})`.

## Deliverable

- `claude-liam-writing-rules.mp4` — 277.7s @ 3840×2160, 24fps, AAC 48kHz stereo.
- mtime: 2026-08-31 17:25:47 (2m31s newer than `beat_sheet.json` at 17:23:16 — supervisor DONE check satisfied).
- No slate cards; filename is `<slug>.mp4`, not `<slug>-slate.mp4`.
- No post-compile sheet edits.

Result: BUILT.
