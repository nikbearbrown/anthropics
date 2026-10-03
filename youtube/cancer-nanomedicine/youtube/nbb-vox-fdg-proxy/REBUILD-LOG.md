# REBUILD-LOG.md — nbb-vox-fdg-proxy

Date: 2026-08-31
Contract: `skills/make/rebuild/SKILL.md` — old sheet is a LOCKED SCRIPT + SHOT LIST; machinery rebuilt.

## Provenance

- `beat_sheet.pre-rebuild.json` — byte-exact copy of the entry-state sheet (made 2026-08-31 05:57 BEFORE any edit)
- `beat_sheet.nbb.json` — earlier (2026-07-16) intermediate; kept for archaeology, not authoritative

## LOCKED (unchanged)

- All 12 body beats (B01–B12) narration_text — from the source vox-fdg-proxy reel; audio measured; not touched
- NBB00 / NBB01 / NBB02 / NBB03 narration_text — measured local audio (kokoro am_onyx); not touched
- All beat order and act labels
- Metadata identity: slug (`vox-fdg-proxy`), title, topic, register, source pointer

## REBUILT (this pass)

### Envelope

- VOICE-LOCK already correct on entry (kokoro / am_onyx). No dead ElevenLabs fields present. Nothing to drop.
- `shot.form` derivation not applied — this reel's shots already carry current `pattern`/`props` shapes.

### Bookends — DUPLICATE REMOVAL

The entry-state sheet carried DOUBLE bookends: `NBB00-03` (real narration + measured audio, the legacy nbb variant) AND `B00 / BVDT / BHTF / BOUT` (empty SLATE placeholders scaffolded by a later automated rebuild pass).

**Removed 4 beats** (empty duplicates; the NBB* beats already fulfill the canonical patterns):

| beat_id | pattern | reason for removal |
|---|---|---|
| `B00` | ClaudeComposerAsk | empty (`greeting:"Liam"` only, no narration, SLATE); NBB00 is the real cold open |
| `BVDT` | ClaudeVerdictArtifact | placeholder lines `"Key finding one/two/three"`, SLATE; NBB01 is the real verdict |
| `BHTF` | ClaudeComposerAsk | generic template command with bracket placeholder, SLATE; NBB02 is the real your-turn |
| `BOUT` | ClaudeTitleOutro | duplicate of NBB03, SLATE |

Beat count 20 → 16. No narration deleted (the removed beats carried none).

### Datable-claims pass over narration

Read every beat's narration_text against the DOUBLE-CHECK LAW checklist. **No changes:** the body of this reel makes no version, price, or "as of" claim that has rotted since 2026-07 — the science (FDG mechanism, Warburg effect, false-positive/-negative examples, "consistent with" clinical language) is not datable.

### Prop authoring (visual props, narration unchanged)

Locked-script rule permits editing visual props; audio is not affected by these edits.

| beat | field | old (verbatim) | new |
|---|---|---|---|
| NBB00 | props.greeting | `"Your turn."` | `"Salve, Liam."` (world-language hello; adjacent nbb-vox reels use Vanakkam/Bonjour/Namaste/Kia ora — Salve unused) |
| NBB00 | props.runningText | `"explaining the mechanism…"` | `"reasoning with the proxy…"` (pulled from beat's own narration `"I want to reason with the proxy instead of against it"`) |
| NBB01 | props.artifactHeading | `"Why a Glowing PET Scan Doesn't Actually Show"` (mid-word truncation) | `"PET measures metabolism, not malignancy"` (from beat B12 recap line) |
| NBB01 | props.artifactLines | `["And glucose metabolism is not unique to cancer.","False negatives are equally real.","Every imaging signal is a proxy.","FDG-PET doesn't show cancer."]` (2 phrase-fragments starting with `"And..."`, 2 generic) | `["FDG lights up hexokinase activity — not tumors.","Infection, healing wounds, and brown fat glow too.","Well-differentiated thyroid cancer barely glows.","Imaging suggests. Biopsy confirms."]` (each specific to THIS reel's body content) |
| NBB02 | props.command | `"Explain how [Why a Glowing PET Scan Doesn't Actually Show Cancer] applies to a specific cancer type or clinical case you're studying. What proteins are involved, what goes wrong at the molecular level, and what is the therapeutic or diagnostic significance?"` (generic template with bracket placeholder) | `"Pick a bright FDG-PET finding from a case you're studying. Name three non-cancer causes that could raise glucose metabolism at that anatomic site. Then pick one target-specific tracer (PSMA, DOTATATE, FES) that would resolve it, and say what a bright-then-dark or dark-then-bright pattern across the two scans would tell you."` (concrete exercise from THIS reel's mechanism) |
| B01 | props.items | 3 items with `label:"Key point one/two/three"` and empty `sub` | 3 items authored from B01 narration (Three bright nodes / Team plans salvage radiation / The diagnosis is wrong, with matching `sub`) |
| B02 | props.lines | `["FDG-PET is the standard tool for staging cancer and checking for…"]` (truncated mid-word) | `["FDG-PET stages cancer and checks for recurrence.","Bright spots = tracer accumulated. Clinicians act daily."]` |
| B06 | props.lines | `["And glucose metabolism is not unique to cancer. Activated immune cells…"]` (truncated) | `["Glucose metabolism is not unique to cancer.","Immune cells, healing wounds, brown fat — all glow."]` |
| B09 | props.lines | `["Here's an illustrative case. A 58-year-old patient — breast cancer surgery…"]` (truncated) | `["58yo, breast cancer surgery three months prior.","FDG-PET flags three bright chest nodes."]` |

Narration edits: **NONE.** All the above are visual props (on-screen text). The audio track is untouched.

### Audio

Existing measured mp3s reused wholesale:
- NBB00-03: local `mp3/beat-NBB*.mp3` (fresh Kokoro am_onyx, measured Jul 2026)
- B01-B12: source `../vox-fdg-proxy/mp3/beat-B*.mp3`

No regeneration triggered (no narration edits).

### Renders (this pass)

- Remotion: 8 beats rendered by `remotion_scenes.py` (NBB00, B01, B02, B06, B09, NBB01, NBB02, NBB03) — pulls current props from the sheet, writes `media/<beat>.mp4`
- Source-clip reuse: B04, B05, B08, B10 copied from `../vox-fdg-proxy/clips/` (pipeline-owned Manim beats — GATE LANE requires video, not slate)
- Declared slates: B03, B07, B11, B12 (CARD/DOCUMENT beats — legitimate in a review cut)

### Gates

- FACTCHECK.md — pre-existing, no new datable claims to check.
- TYPECHECK.md — GATE T PASS after purging the six typecheck-failing source clips from media/ (see AUDIT.md TYPECHECK NOTE for the B04/B10 downgrade rationale).
- Compile: `compile.py --review` → `vox-fdg-proxy-slate.mp4` (225.7s, 12/16 filled, mean_volume −24.6 dB, GATE AUDIO PASS, GATE LANE PASS, content-check PASS, frame-check PASS).

## Not published

Rebuild is a machinery refresh + review-cut delivery. This reel is not staged and not posted.
