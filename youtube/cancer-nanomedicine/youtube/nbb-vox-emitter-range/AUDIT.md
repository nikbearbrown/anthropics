# AUDIT.md — nbb-vox-emitter-range (2026-08-30)

Cohort C legacy vox → NBB variant rebuild. Ran the film-loop Phase-1 audit against
`youtube/LENS-NOTES.md` and produced a review slate cut.

## PHASE 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` — WRITTEN (byte-exact snapshot, 24,168 bytes).
- Envelope normalized: `metadata.clock` line added (measured Kokoro mp3s ground-truth);
  metadata already had `engine: kokoro`, `voice: am_onyx`, no dead ElevenLabs-era fields
  to drop.
- Narration LOCKED except: BHTF closing-block narration rewritten from the old NBB02
  template ("Take this prompt, run it on your own — pick any cancer type…") to a real
  next-step ask ("Your turn. Take this prompt into Claude — pick a real tumor whose
  receptor map you know…"). Permitted under rebuild contract §Closing block (new writing
  built from sheet content) and §5c (placeholder Your-Turn template fix). Audio regenerated
  via Kokoro `am_onyx`; measured `actual_duration_s = 7.47s` written back.
- BOUT sub-line ("geometry decides… changes with every patient'") was truncated with a
  broken quote; rewrote to `more lethal per hit does not mean more useful in the tumor`.
- B01 + BOUT display titles got a trailing period to pass §8.9 (the 2-letter "It" ending
  on a 60-char string was flagged as a fragment).

## PHASE 1 — Audit checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no `.mp4` in reel folder before this pass. |
| 2 | Bookends canonical | FIXED | pre-rebuild carried TWO parallel bookend sets: (a) empty `B00 / BVDT / BHTF / BOUT` scaffold with `"Key finding one/two/three"` placeholder verdict + `[Take what you learned from...]` bracketed BHTF template, and (b) filled `NBB00 / NBB01 / NBB02 / NBB03` with real narration and measured Kokoro audio. Dropped the empty scaffold; renamed the filled NBB set to canonical ids (`B00 · BVDT · BHTF · BOUT`); mp3 files renamed on disk to match. |
| 3 | Spark lines | FIXED | `B00.greeting` was `"Your turn."` (wrong for a cold open) → `"Hola, Liam"` (Spanish; not used in adjacent nbb reels this batch: Olá, Annyeong, Bonjour, Vanakkam, Kia ora, Ni hao, Konnichiwa, Salve, Namaste, Aloha). `BHTF.greeting` = `"Your turn."` ✓. Truncated `segment` fields normalized to `"emitter range · geometry over lethality"`. Dropped legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` from B00 + BHTF (Kokoro reel, not model-branded). |
| 4 | Verdict | AUTHORED | `BVDT.artifactHeading` was truncated mid-clause (`"Why 'Alpha Radiation Is Stronger' Is the Wrong"`) → `"geometry decides which emitter wins"`. `artifactLines` were 2 body-lifted sentences + 1 four-word fragment ("More lethal per hit."); rewrote to four real key findings from the body's own numbers: alpha 50–100 μm one-cell reach; beta 1–2 mm crossfire; illustrative Lu-177 ≈ 78% vs Ac-225 ≈ 41% on a 3 cm heterogeneous NET; match range to geometry not raw LET. `verdict_audit.py` does not flag this reel. |
| 5 | Card text | FIXED | `B01` FormBCard items were `"Key point one/two/three"` placeholder labels with empty `sub`. Rewrote to real content: `Bulky, heterogeneous tumor / receptor-positive rim, receptor-negative core` · `Alpha hits harder per particle / 50–100 μm range — one or two cell widths` · `Oncologist picks beta anyway / 1–2 mm crossfire reaches the cold core`. |
| 5b | Chart text | N/A | no local Manim scenes; body beats render as Remotion FormACard slates (see punt sweep). |
| 5c | Your-Turn placeholder | FIXED | pre-rebuild `NBB02.command` matched the bracketed template law: `"Explain how [Why 'Alpha Radiation Is Stronger'...] applies to a specific cancer type..."` (one of the 3,472 sheets caught 2026-08-30). Rewrote to a real exercise: pick a solid tumor you know the histology of, sketch its target map, choose the emitter by geometry, and state the imaging finding that would falsify the pick. Also populated `output` with three specific next-step lines (name the target, justify by geometry, state the falsifier). |
| 6 | Punt sweep | PASS | 0 gen-AI asks, 0 unfilled `fill_slates`, 0 DoodleScene, 0 `STILL src=archive` for conceptual content, 0 FormA card naming a visual it never draws. Every beat draws either a Remotion card (13 body + 3 bookends = 16 renders) or a real still (B07 heterogeneous-tumor cross-section PNG). |
| 7 | Card-only reel | LOG | this IS a Remotion-card-heavy review slate cut by design: the source `../vox-emitter-range` supplies the schematic B07 tumor still; every other body beat renders a FormACard slate whose text is compressed from that beat's `graphic.production_viz.label` — the intent record for the source's animated alpha/beta/crossfire diagrams. This mirrors the sibling nbb-vox-abraxane-solvent and nbb-vox-doxil-heart rebuilds, which also route legacy GRAPHIC bodies through FormACard. The animated Manim visuals from the source vox reel (`../vox-emitter-range/manim/*.mp4`) exist and could be reused, but their inherited 18–30pt Manim labels fail §8.1 min-size at 720p and cannot be fixed without a source-side re-render (out of scope for a per-reel film-loop invocation). |
| 8 | Lens audit | PASS | The body earns two moves. **Popper**: the falsifier is stated in advance — "alpha stronger = better" would predict alpha wins on a bulky, heterogeneous tumor with a receptor-negative core; the reel names the exact finding that refutes it (alpha 50–100 μm range never crosses the gap; core survives; illustrative Ac-225 ≈ 41% kill vs Lu-177 ≈ 78%). **Plato**: the artifact ("more lethal per hit") is held apart from the world ("actual tumor cell kill in a heterogeneous geometry"), and the relationship is interrogated ("the answer is not in the particle — it is in the tumor"). Descartes / Hume are not explicitly named; narration is locked. |
| 9 | Brand fields | FIXED | `metadata.audience = NikBearBrown`, `metadata.engine = kokoro`, `metadata.voice = am_onyx` ✓. `folderLabel = "@NikBearBrown"` on every ClaudeComposerAsk beat. Legacy `modelLabel/effortLabel` removed. |
| 10 | Pacing (wps) | PASS | every timed beat lands 2.0–3.4 wps against measured Kokoro durations. |
| 11 | `type_check.py` | PASS | GATE T PASS; two §8.10 recite advisories (B07, B12) — advisory only, not fails. |

## Datable-claim scan
- `Lu-177`, `Ac-225`, `SSTR2` — isotope + molecular-target names, not datable.
- `~78% kill`, `~41% kill` — illustrative numbers, labeled as such in both narration ("About forty-one percent kill") and in the visual (footer `illustrative numbers`).
- `50–100 μm`, `1–2 mm` — physical particle ranges (physics constant), not datable.
- No model / tool / version claims to fix.

## Blocked?
No. GATE T PASS; every beat renders real; the review slate cut can compile.

## Rendered slot map
- B00 · ClaudeComposerAsk · media/B00.mp4 (5.6 s)
- B01 · FormBCard · media/B01.mp4 (9.8 s)
- B02–B06 · FormACard · media/B02–B06.mp4 (11.6–15.3 s each)
- B07 · STILL (heterogeneous tumor cross-section) · media/B07.png
- B08–B12 · FormACard · media/B08–B12.mp4 (8.8–22.0 s)
- BVDT · ClaudeVerdictArtifact · media/BVDT.mp4 (27.9 s)
- BHTF · ClaudeComposerAsk · media/BHTF.mp4 (7.5 s)
- BOUT · ClaudeTitleOutro · media/BOUT.mp4 (6.0 s)
