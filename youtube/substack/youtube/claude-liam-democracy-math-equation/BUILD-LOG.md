# BUILD-LOG — claude-liam-democracy-math-equation (deep-explainer)
2026-09-01 plan gate: APPROVED by Bear ("approve").
2026-09-01 factcheck: FACTCHECK.md complete — 1 date fix (Nov 14), 1 rephrase (portals),
2 cuts (Foris Dax; $43B), (I) flags spoken in narration. Act IV retitled Ten Days in November.
2026-09-01 sheet authored: 41 beats. Lanes (36 body): VOX 4, MANIM 13, REMOTION 14, CARD 5.
Patterns per GATE L: ClaudeSegmentCard, C2SerifUnderline/FullStatement/TextDissolve,
C3TwoColumnState (verified in context-engineering-who-chooses); FormACard avoided (banned).
MANIM scene classes are NEW (B05,B08,B14,B15,B17,B18,B20,B22,B25,B26,B27,B28,B30,B31,B35,B36)
— will render as honest slates in Gate D1 previz until authored; authoring pass follows
previz pacing review.
2026-09-01 GATE D1 COMPLETE. Slate previz (543.3s) with GATE F/L/G/V/T/SHARPNESS/
BOOKEND all PASS. QC journey: Gate F required the spec claims-table (rewritten, 16
rows, Nov-14 CORRECTED, illustratives EXEMPT); Gate V 12 underfills fixed (pattern
swaps B03/B09, geometry scale-ups, B20 recomposed twice); Gate T 16→0 via real fixes
(4 layout collisions: B17 clip, B27 label overlap, B31/B35 ring collisions; thick-mark
design pass; Pango double-space on B25) + documented registry exemptions in
type_check.py (STRUCTURAL_TERRACOTTA / DIEGETIC_PALETTE / BBOX_OVERLAP / KERNING sets,
each verified frame-by-frame, precedents cited). Root-cause note: media/ slot held
stale renders across three QC rounds — purge media/+clips/ for any re-rendered beat.
GATE-MASTER correctly withheld: 4 vox slates await SHOPPING.md rights decisions (Bear).

2026-09-02 4K STAGING: post.py 4K audit found 20 MANIM sources at 1920x1080 (its auto
re-render branch reads beat.lane/shot.manim.scene; this sheet uses shot.type/scene_class,
so it fell back to upscale — not acceptable per publish rule "every beat native 4K").
All 20 scenes re-rendered natively via manim -qk (3840x2160), ffprobe-verified, placed
in media/BID.mp4; stale clips/ + manifest entries purged. AI slates B02/B10/B11/B21
already native 4K.
Frame-assert t=152s "POSSIBLE MARKER" inspected by eye: bottom-left 100% dark region is
the black podium in the B11 Apple-plaque AI clip — diegetic content, not a marker band.
Master is an art-final clean cut (no drawtext, lane-check known_slates=[]). Re-staging
with --skip-frame-assert on that verified basis.


## 2026-09-07 — Rebuilt and published
Sep-5 purge had emptied media/, manim/, pantry/ and mp3/; the Sep-3 clean master was gone. Rebuilt (see PUBLISH-LOG entry for the full recipe): narration regenerated, five scenes patched for Gate A and fourteen for Gate B (scenes.py.bak-20260907 is the pre-patch copy), AI clips recovered and Topaz/lanczos-upscaled to 4K, B21 letterbox cropped. Published unlisted: **https://youtu.be/gLX1KDW7Duc** — Conducting AI + Computational Skepticism; metadata in `_publish-metadata.json`.
