# AUDIT.md — claude-liam-simple-delve/short

Auditor: filmloop pass, 2026-08-31.
Sheet mtime baseline: 2026-08-15T15:05.
Verdict: **BLOCKED — do not build.** Cause: every Manim scene is authored for 16:9
landscape but rendered at 9:16 vertical (1214×2160). Anchor content is cropped
off the horizontal edges on every S-beat, and captions are narration fragments
that clip mid-word. The `short/` directory has no `scenes.py` source; without
it, re-render is not possible from this reel alone. This is a scripting/render
rebuild job, not an audit-and-compile fix.

## Backup

`beat_sheet.pre-rebuild.json` copied byte-exact before any inspection. No sheet
edits made this pass.

## Phase 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `<slug>.mp4` / `<slug>-slate.mp4` at reel root; nothing to purge. |
| 2 | Bookends | PASS w/ note | B00 seedance MARCUS puppet is non-canonical for `palette=claude` but `folderLabel=@NikBearBrown` — the NikBearBrown channel legitimately keeps the Shannon-puppet lab open (skin_warnings in metadata log this). BCRY (WantQuote916) is the carry-out slot in place of BVDT; BVDT absent is legal per amendment. BHTF (ClaudeComposerAsk916) and BOUT (ClaudeTitleOutro916) canonical. |
| 3 | Spark lines | PASS | BCRY.sparkLine="Habit, not mark." (3 words, from own narration). BHTF.greeting="Your turn." ✓. B00 is not a composer beat, so no greeting requirement. |
| 4 | Verdict | PASS | BCRY narration is specific to this reel's argument ("A word that shows up again and again is a habit, not a watermark. The watermark never picks the same favourite twice."). Not placeholder, not template, not boilerplate — states the reel's carry-out from its own nouns. No BVDT beat exists; absence is legal. |
| 5c | Your-Turn placeholder | PASS | BHTF command is a real exercise ("Take three pieces of writing I'm sure a human wrote… count the supposed AI tells… take something I know was AI-written and count again"). No `[ ... ]` brackets, no restate. |
| 5b | Chart text | **BLOCKER** | Every Manim scene uses narration fragments as chart captions AND every layout overflows the 9:16 frame. Frame-checks at t≈2s: S01 "conclusions, one" clips; S03 anchor word "delve" shows only "ve", caption "like fifteen-fold in" clips right; S07 top caption "each word posit…" clips both sides, "goes"→"oes" clipped; S12 both watermark-family columns cut, side labels ghost off the right; S13 anchor payoff "delve"→"ve", caption "have nudged it" clips. This is Check 5b's exact defect (Text(narration[:30]) mid-word truncation) compounded by a 16:9→9:16 layout mismatch. |
| 5 | Card text | PASS | Remotion bookends (WantQuote916 / ClaudeComposerAsk916 / ClaudeTitleOutro916) carry real strings; no FormA/FormB beats. |
| 6 | Punt sweep | PASS | Every beat has a real render (16 manim, 4 media, 1 STILL). Zero unfilled slates, zero DoodleScene, zero STILL src=archive. |
| 7 | Card-only reel | PASS | 16 body beats are Manim scenes — hardly card-only. |
| 8 | Lens audit | PASS | Reel earns at least THREE moves: Popper (S05: "a watermark that always favoured the same words could be stripped with a find-and-replace" — states in advance what would falsify the fixed-favorite reading), Plato/artifact-vs-world (S13: "same word, two different reasons, and from outside they look identical"), Hume (S15/S16 mirror pair: an AI-sounding word doesn't prove the mark; clean prose doesn't disprove it — confidence is a property of the reader's model, not the world). |
| 9 | Brand fields | PASS | `folderLabel=@NikBearBrown` is a channel handle. Per-beat engine/voice matches: B00→seedance/MARCUS (baked audio in mp4), all other beats→kokoro/am_onyx (mp3 present). Persona "Liam (in for Bear)" coherent with am_onyx voice for the S-beats and outro. |
| 10 | Pacing (LOG) | Advisory | Beats outside 2.0–3.4 WPS: S04 (3.53), S11 (4.16, hot), S13 (3.52), BHTF (3.54). No silent retime. |
| 11 | type_check.py | Not re-run | Existing TYPECHECK.md dated 2026-08-15 says PASS but every S-beat is "no video" SKIP — result is misleading. Re-running is moot because the reel is BLOCKED upstream at Check 5b. |

## Root cause

The Manim scenes in `manim/*.mp4` were rendered at 1214×2160 (9:16) from a
`scenes.py` that was authored for 16:9 landscape composition — text sizes,
positions, and captions were laid out for a 1920×1080 stage and never reflowed
for vertical. There is no `scenes.py` in the `short/` folder to re-render
against; the parent reel has one, but adapting it to 9:16 layout is a
scene-rewrite job, not a compile-time fix. The `pantry/<bid>-916.*` slot the
metadata mentions is the intended human-supplied remediation path when
center-cut fails; nothing has been placed there.

## Action to unblock

Not this invocation. Needs a `rebuild` skill pass on the scenes source:
- rewrite every scene in scenes.py (16 of them) for 9:16 layout — resize/
  reposition anchor text ("delve", act labels), split multi-column layouts
  vertically, replace narration-fragment captions with 1–3 word category nouns,
- OR generate `pantry/<bid>-916.*` overrides by hand,
- re-render Manim, re-run this audit.

## No sheet edits

Beat sheet was NOT touched this pass. No compile attempted. Reel remains in the
state it was on 2026-08-15.
