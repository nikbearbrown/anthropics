# BUILD-LOG — claude-basics--computer-use-best-practices (nbb-rebrand)

**Skill:** nbb-rebrand · **Channel:** claude-liam (@NikBearBrown) · **Built:** 2026-08-29

## Source

`anthropics/youtube/hai-simple/claude-basics--computer-use-best-practices/` —
verified read-only source master SHA-256 `8642773b30e21c49f9ecd985945bb5352fabbfb5fb5ecdaa3d03cc4a0dd51398`
matches SUBJECT.json at both PHASE 0 and PHASE 5 (re-checked after build —
unchanged). See `SOURCE-MEDIA-LOCK.md` for the full asset ledger.

## What was built

- **BASK** (new) — `ClaudeComposerAsk` / `ClaudeComposerAsk916`. Liam asks the
  video's real question ("What actually changes when you take a computer-use
  agent from a working demo to production?"), drawn from the source's own
  QUESTION.md/CARRY-OUT.md.
- **B00** (new, replaces source B00) — `BrutalistHesitantWriter` /
  `BrutalistHesitantWriter916`. Same misconception (longer→leaner), same
  palette as the source's own B00 (carried forward, not re-branded — palette
  isn't the chip).
- **B01–B04, BCRY** — reused verbatim (same beat_id, narration_text,
  audio_file, actual_duration_s, media). Byte-identity verified against
  source before and after the build.
- **BHTF** — narration/audio/duration reused verbatim; video re-rendered
  fresh because its `folderLabel` prop carried the old `@HumanitariansAI`
  chip → changed to `@NikBearBrown` (THE CHIP law: only the chip-bearing
  beat's video is touched, never its audio).
- **BMASCOT** (new) — `ClaudeMascotScene`, `wave` animation, silent, label
  "Leaner. Logged." (compressed from BCRY's own sparkLine).
- **BOUT** (new, replaces source BOUT/OutroCTA) — `NikBearBrownOutro` /
  `NikBearBrownOutro916`, default brand/tagline/url, handle `@NikBearBrown`.

Both aspect ratios shipped: `claude-basics--computer-use-best-practices.mp4`
(3840×2160, 125.0s) and `claude-basics--computer-use-best-practices-916.mp4`
(1216×2160, 125.0s). Both pass GATE AUDIO (mean_volume −24.1 dB, well above
the −40 dB floor).

## Gates

- **beat_lint.py RULE 7 (branding):** clean on both sheets — `folderLabel`
  correctly `@NikBearBrown` for channel `claude-liam`.
- **Pixel chip check:** OCR (tesseract) across all 250 sampled frames (2fps)
  of BOTH masters — zero hits for "Humanitarian" anywhere. Manual frame reads
  of BASK/BHTF/BOUT in both aspects confirm the `@NikBearBrown` chip renders
  correctly and no frame anywhere still carries the old handle.
- **content_check / frame_check / lane_check (compile.py hard gates):** PASS
  on both sheets.
- **GATE T (type_check.py):** 9/10 beats PASS. **BMASCOT FAILS §8.1 min-size**
  — the checker reports "no text blobs detected." Root-caused: BMASCOT's
  label renders as white text on a terracotta bottom strip inside an
  otherwise cream-background (light-polarity) frame; the checker's global
  per-frame polarity detection (border-strip sampling) classifies the whole
  frame as light-polarity and its ink-vs-cream text mask does not recognize
  light-on-mid-tone-terracotta as text, so it finds zero qualifying blobs.
  Manually verified by extracting frames directly from `media/BMASCOT.mp4`:
  the label ("Leaner. Logged.") is large (110px display font), bold,
  high-contrast, and clearly legible — this is a checker false-negative
  specific to `ClaudeMascotScene`'s bottom-strip layout, not a real
  legibility defect. `ClaudeMascotScene` is not yet in `type_check.py`'s
  existing false-positive exemption lists (`HAND_DRAWN_PATTERNS`,
  `DIEGETIC_PALETTE_PATTERNS`) that cover the same category of issue for
  other components. Per the house rule ("fix content, never the validator"),
  I did not touch `type_check.py` or the shared `ClaudeMascotScene.tsx`
  component (out of scope for a single-reel build, and would affect every
  other reel using that component); I shortened the label to fit one line
  as a content-side attempt, which did not change the outcome, confirming the
  polarity-detection root cause rather than a wrapping artifact. Logging this
  as an accepted, verified-by-eye exception rather than silently claiming
  GATE T fully green.

## Vertical (9:16) cut — known, accepted limitation

Per the skill's own instruction, body beats (B01–B04, BCRY, BHTF) are NOT
re-rendered for the 9:16 sheet — they reuse the same 16:9-native media, and
compile.py's own aspect-driven scale+crop conforms them into the vertical
canvas. Visual inspection of the 9:16 master confirms this crop is a genuine
**center-crop that clips both edges** of these beats' text/diagrams (e.g.
B01's loop diagram loses its outer boxes' edges, BCRY's quote text is clipped
left/right, BHTF's composer card text is clipped left/right). This is the
documented, pre-authorized trade-off of reusing 16:9 body media in a 9:16
companion cut ("you do not re-render or duplicate body media for the
vertical cut") — not a build defect, but also not cosmetically clean. Noting
it plainly rather than claiming a flawless vertical cut. BMASCOT (reused
as-is, no 916 variant) and the new bookends (BASK/B00/BOUT, which DO have
proper 916-native renders) show no clipping.

## Tooling gotcha hit during this build (for future nbb-rebrand runs)

`compile.py`'s `purge_stale_renders()` deletes ANY root-level `*.mp4` older
than the just-compiled sheet's mtime, regardless of which sheet it belongs
to — it has no concept of a reel carrying two persistent masters (16:9 +
916) side by side. Compiling the 916 sheet after the 16:9 sheet silently
deleted the finished 16:9 master. Worked around by backing up the 916
master, recompiling 16:9 last (so its unchanged-content sheet mtime stays
older than the 916 master file), then restoring the 916 master via a plain
file copy (no further compile.py/remotion_scenes.py calls after, to avoid
re-triggering the purge). Both masters verified present and correct at the
end of the build. A future run of this skill should expect the same
gotcha — compile whichever sheet's master must NOT get deleted LAST, or
back up before the second compile.

## Delivery

Committed and pushed to `anthropics` (commit `8f201e22`, rebased onto
`ff259ffc` from a concurrent worker, pushed as `550a2253`). Staged to the
local Drive outbox via `deliver.py --push`
(`~/Documents/books/DELIVERY-nbb/claude-basics--computer-use-best-practices/`:
4K master, 9:16 master, description).

**Post-push mtime note:** `git pull --rebase` (needed to resolve a push
rejection from a concurrent worker's commit) re-checks-out the files in my
own commit during replay, which bumped `beat_sheet.json`/`beat_sheet.916.json`/
`TYPECHECK.md`'s mtimes to the rebase time — momentarily making them appear
newer than the already-compiled masters. Verified via `git diff` that content
is byte-identical to what was compiled (no real edit occurred), then `touch`ed
the three master mp4s to restore the true build ordering (masters newer than
sheets). Documenting this in case a future nbb-rebrand run hits the same
rebase-mtime artifact and needs to know it's not a real staleness signal.
