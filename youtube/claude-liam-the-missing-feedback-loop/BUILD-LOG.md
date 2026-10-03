# BUILD-LOG — claude-liam-the-missing-feedback-loop

## 2026-08-30 — authored (deep-explainer, claude-liam channel)

**Source:** Bear's research brief on Anthropic's Model Hardware Standard
(pasted 2026-08-30) + live fact-check against the primary Anthropic post.
See SOURCES.md / FACTCHECK.md. The brief itself mixes verified and
unverifiable material; the film only carries claims traced to the primary.

**Thesis:** AI took off in code because of the feedback loop; MHS is the bet
that the loop can be built for atoms. Give the mechanism its due
(driver/manifest, integration collapse, the QuEra result is strong), then
keep the three distinctions the headlines blur: (1) Claude wrote the operator
— it is not the operator; (2) the verifier is task-specific and MHS does not
standardize it; (3) programmatic ≠ physical understanding (the bubbles). All
numbers company-reported, and the film says so on screen.

### Act map (29 beats, est. ~7:05 pre-audio)
- **B00** cold open (ClaudeComposerAsk, ask answered): 58% vs 99.3%.
- **ACT I — THE LOOP** (B01–B05): why code fell first; the loop as machinery;
  the same loop priced through atoms; economics kept AI on the screen; the
  MHS bet.
- **ACT II — A DRIVER, NOT A BRAIN** (B06–B11): manifest/driver anatomy
  (Onda code beat); discovery is the novelty (N×M → N+M); integration
  numbers; safety floor below the model + who writes the manifest; what MHS
  does NOT standardize.
- **ACT III — THE LASER** (B12–B19): the lock problem; the 58% baseline; the
  overnight four-role loop; THE REVEAL (deterministic decision tree, no AI in
  production); 700 blind trials; the quieter PID result; three claims
  separated (meta-programmer, not machine operator).
- **ACT IV — THE VERIFIER ISN'T FREE** (B20–B25): compiler = universal free
  verifier vs bolt-on sensors; taxonomy by price of checking; the bubbles;
  "programmatic rather than physical"; weigh the preview as a preview.
- **BVDT** verdict (5 artifact lines) → **BHTF** Your Turn (verifier-hunting
  prompt, read in full) → **BOUT** title outro.

### Lane histogram (25 body beats)
| Lane | Count | Share | Band |
|---|---|---|---|
| VOX | 5 (B04 B09 B13 B18 B23) | 20% | ✓ target 20–25% |
| MANIM | 9 (B02 B03 B08 B10 B14 B15 B17 B21 B25) | 36% | ✓ 25–40% |
| REMOTION | 7 (B05 B07 B11 B16 B19 B22 B24) | 28% | ~ (band 30–45%, 1 under) |
| CARD | 4 (B01 B06 B12 B20 — ClaudeSegmentCard) | 16% | remainder |

No vox runs (all five vox beats are singles — no handoff blocks needed). No
3-in-a-row same-lane. All five vox stills are Tier 1 except B13 (Tier 2,
real quantum-optics table preferred); every vox beat carries a GRAPHIC/own
fallback in `shot.vox.shopping.fallback`.

### Laws applied at authoring
- Stage layout law: every Manim beat = subject operating LEFT, ledger/numbers
  updating RIGHT, causally synced (B02 loop↔counter, B08 topology↔N+M, B14
  chain↔58% bar, B15 loop↔attempts, B17 grid↔695 count, B25 scale↔checklist).
- Visual rhyme: B15 reuses B02's cycle geometry (the loop, with photons).
- B17 human-latency bar uses an explicit axis break — never fake linearity.
- Strip-the-datable: no dates in narration, no partner-name roll-call
  (Genentech named only in the description; narration says "one pharma lab"),
  regulatory threads cut.
- Unverified-source caution: FACTCHECK.md marks CHECKED vs COMPANY-REPORTED
  per claim; the film grades its own sources on screen (B25).

### Plan-gate note
Built autonomously to the Gate D1 slate previz per Bear's request
("ai deep explainer Liam persona" + research prompt) and this session's
standing pattern: build to slate cut, STOP, Bear reviews. GATE P: Kokoro
(free); narration review happens at the previz watch.

## 2026-08-31 — built to Gate D1 slate previz (STOP for Bear)

Audio: 29 Kokoro am_onyx beats, measured, aligned (words.json). Total 6:47.
Visuals: 9 Manim scenes (scenes.py, layout law + check_overlaps incl. labels)
+ 15 Remotion beats (schema-matched props). 5 vox slots render as slates
pending pantry stills (SHOPPING.md, all tier-0 misses — library/Smithsonian
hold only period instruments).

**Cut:** `claude-liam-the-missing-feedback-loop-slate.mp4` (406.9 s, 48 kHz
AAC verified, tail audible to the last beat). Final cut correctly refused
while slates remain.

**Gates:** F, L, BANNED-CARD, SWEEP, G, V, T, SHARPNESS, BOOKEND all PASS.
MASTER/AUDIO pend the clean cut (post-pantry).

Defects found by reading frames and fixed at root cause this pass:
- Pango space-collapse recurred (compilererror/silentfault/4engineers) →
  _t doubles every space; _mono does NOT (Menlo never collapses; doubling
  tripped GATE T kerning with real double-wide gaps).
- 57% truncation bug (int → round) on B14's bar; 695/700 mash (Integer
  arranged at 0-width) on B17; B25 balance rework (shift-tilt, no chip skew);
  B10 label-on-band collisions; B08/B14/B21 off-frame layouts.
- GATE V title-safe (±6.4u): six scenes pulled inside; GATE T: EB Garamond
  old-style digits/% and mono tilde read under the 20px floor → mono digits,
  no ~ or % glyphs in small ledgers; ClaudeCodeBeat title must be a filename
  (mhs_driver.py).
- Exemptions added with justification (house precedent): ClaudeC2FullStatement
  → SPARSE_OK (final_frame_check.py); B02/B08/B15 → BBOX_OVERLAP_EXEMPT and
  B03 → KERNING_EXEMPT (type_check.py) — bordered label-in-card and same-band
  compound-run false positives, frames verified by eye.

NEXT: Bear watches the previz; drops stills into pantry/ per SHOPPING.md
(fallbacks authored for all five); then pantry intake → recompile → final →
stage via post. NEVER publish from here.

## 2026-08-31 — HUMAN FEEDBACK (Bear): pantry filled, full 4K master

Bear generated the five vox assets as VIDEO (not the stills the shopping list
asked for) and delivered them in `books/PANTRY/`, beat-id prefixed, each with a
base and an upscaled `_ddv3` variant. Instruction: rename, move to the reel's
pantry, update, make a 4K 16:9.

**Selection.** Took the `_ddv3` upscales. B04/B09/B13/B23 came back true
3840x2160; B18's first upscale was 3328x1856, and Bear regenerated it mid-pass
— the replacement (`_2_4_ddv3`) is true 4K and is the one used. The 3328 file
is superseded and unused.

**Prep before intake (pantry law — assets arrive restored).** Each clip is
5.21 s but the beats run 12.9-17.0 s. A straight slow-to-fit would have run
2.5x-3.3x; B18 at 3.3x trips compile's extreme-slow-mo warning (~7 fps
effective, visibly choppy). Fix: scale+pad to exactly 3840x2160 16:9, then
ping-pong (forward + reverse) to 10.42 s. Compile now slows only 1.2-1.6x,
which reads smoothly, and the reverse leg is invisible on ambient equipment
motion. Prepped files -> `pantry/<BID>.mp4`.

**Sheet.** The five beats moved STILL -> VIDEO, source archive -> `ai` (they
are generated, and `ai` is what triggers the house laundering: hue s=0.25,
contrast 1.12 — seats the footage on the cream stage). Stale `motion`/`focus`
keys dropped. `beat_sheet.pre-pantry.json` holds the pre-edit sheet.
Provenance sidecars written per asset with generator, original filename,
subject, tier, and the prep applied.

**Master:** `claude-liam-the-missing-feedback-loop.mp4` — 3840x2160, 24 fps,
AAC 48 kHz, 406.96 s (6:47). ALL GATES PASS: F, L, BANNED-CARD, SWEEP, G, V,
T, SHARPNESS, BOOKEND, AUDIO, MASTER, LOUDNESS, RECEIPTS.

**Gate fix (upstream, justified).** GATE V raised 4 COSMETIC `low-contrast`
flags on the footage beats. The check measures ink-vs-background separation
for DESIGNED TYPOGRAPHY; footage carries none, so it reads the scene's own
tonal range and calls a pale lab bench "hard to read". Added the existing
synthetic `FullBleedFootage` pattern (already exempt from edge-bleed and
underfill for declared shot.type VIDEO/STILL) to `LOW_CONTRAST_OK_PATTERNS`
in `runtime/qc/final_frame_check.py`. Frames verified by eye first — B04 and
B18 both read cleanly.

OPEN: `claude-liam-the-missing-feedback-loop-slate.mp4` (the previz, 255 MB)
still sits beside the master and is now superseded — left in place for Bear
to delete. NOT staged to TOPOST and NOT published.

## 2026-08-31 — PUBLISHED (Bear approved) → https://youtu.be/CHMrIPYM9IM

Uploaded to @NikBearBrown as **unlisted** (house rule: public is a manual
Studio flip — the human decides). English CC track uploaded. Added to all four
playlists per Bear: Claude & Agentic AI · Computational Skepticism · Behind the
Model · Claude Research.

**post's 4K audit earned its keep.** All nine Manim beats were rendered at
1080p and were being stretched into the "4K" composite — a 4K master in name
only. Root cause: this reel's `manim/scenes.py` hardcoded
`config.pixel_height = 1080`, which SILENTLY OVERRODE manim's `-qk` flag, so
asking for 4K produced 1080 and said nothing. Fixed by making the render size
the render target (`ART_MANIM_H`/`ART_MANIM_W`, default 1080); all nine
re-rendered at true 2160p. **This pattern is copied across other reels'
scenes.py — any reel with the same pinned config has been shipping upscaled
Manim in its "4K" masters.** Worth a sweep.

At 2160 the GATE T type floor rises 20px → 41px, which surfaced two real
defects the 1080 pass could not see: B08's device labels measured 40px (1px
under) and, once enlarged, overflowed title-safe — both fixed (labels 16→18,
row clamped). B25 hit the bordered-chip-encloses-its-label false positive
already exempted for B02/B08/B15; added with the same justification.

**Description generator fixed (systemic).** `stage_publish.py` emitted, on
EVERY reel: (a) the unconditional line "fact-checked against the source
chapter…" — naming a chapter even for reels that have none, the exact bookloop
violation Bear has been flagging all day; and (b) a stale tag default of
`#physics #quantum #sciencehistory`, which this MHS/robotics film would have
shipped with. Both corrected at source; this reel now carries a real blurb,
real tags, and timestamped chapters from measured offsets.

**Publisher crash (post-upload).** `publish_playlist.py` uploaded successfully,
then raised FileNotFoundError writing its ledger to
`brutalist-art/youtube/credentials/nikbearbrown/` — a directory that did not
exist (real creds live in `books/youtube/credentials/`). The crash landed
BEFORE caption upload and playlist insertion, so both were completed manually
and verified via the API. Ledger directory created so the next publish does not
crash. NOTE: the ledger is empty of this upload — `staged.json` is the record
(status=uploaded, video_id=CHMrIPYM9IM).

OPEN: Topaz 8K variant not produced (Topaz IS installed; skipped to unblock
publishing — `staged.json.topaz.ran=false` with that reason). The superseded
`-slate.mp4` previz is still in the reel folder.
