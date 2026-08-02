# BUILD-PROMPT.md — claude-liam-different-kind-of-wrong

Paste-ready Claude Code prompt. Run from `books/` on the Mac, typically under
`claude --dangerously-skip-permissions` (seatbelt-safe: git-tracked, regenerable
outputs, GATE P still needs a human signature before any paid spend). This reel
is **claude-liam** — Kokoro `am_onyx`, free — so GATE P is a narration-review
sign-off, not an ElevenLabs spend, unless you deliberately swap to Bear's voice.

---

```
Build the deep-explainer reel at validating-output-from-ai-systems/youtube/claude-liam-different-kind-of-wrong/.

It is authored through the PLAN gate: beat_sheet.json, PLAN.md, FACTCHECK.md,
SOURCES.md, and BUILD-LOG.md already exist in that folder. Channel is claude-liam
(Liam in for Bear, Kokoro am_onyx, free). Register Teardown. 16:9. Never publish —
stop at the master in the reel folder.

Work the gates in order, and STOP at each human gate:

1. GATE F — FACTCHECK re-verify (live). Open FACTCHECK.md and independently verify
   every row marked "re-verify at Gate F": Goodhart's Law (1975 attribution/wording),
   McNemar's test + the NIST reference and small-sample exact-binomial caveat, the
   LLM-as-judge position/verbosity/authority-bias literature, and the four named
   works — CheckList, Dynabench, HELM, PoLL. For each: confirm it exists and says
   what B03/B13/B21/B31 claim; if a claim doesn't hold, cut or soften it and log the
   change. Confirm the EXCLUDED items stay excluded — the invented "Exponential
   Impact Score" formula and the synthetic worked-example numbers (p ≈ 0.39, the
   40-case walkthrough) must NOT appear on screen as if real. Update FACTCHECK.md
   with verdicts + sources. Then STOP and show me the diff.

2. GATE P — narration review. Render an animated slate previz of the narration only
   (no audio spend yet) and show it to me. On my sign-off, generate audio:
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py validating-output-from-ai-systems/youtube/claude-liam-different-kind-of-wrong
   (am_onyx). Measure per-beat durations; those become the master clock. Do NOT
   hand-time anything — if a beat is mistimed, fix the narration and regenerate.
   Captions via the faster-whisper pipeline.

3. Audio lock → Gate D2 SHOPPING.md. Only AFTER durations are locked: run the
   tier-0 library pass for each of the 7 vox stills —
   python3 brutalist-art/runtime/scripts/pantry_search.py "<terms>" for B03 (Goodhart
   portrait — Tier 3, archival first, rights escalate to Bear), B07/B08 (specimen /
   card-catalog tray, run R0), B19 (panel of judges), B28/B29/B30 (archival regression
   log / ledger / version history, run R1 — one wide high-res plate that survives a
   2.0x zoom). LOOK at candidates; copy real matches into pantry/ pre-checked. Write
   SHOPPING.md from the LOCKED durations, tier-tagged, one entry per still still
   missing. Then STOP and show me SHOPPING.md.

4. Gate D1 — slate previz (full length). Compile the whole reel with vox beats as
   slates, Manim + Remotion beats rendered for real, audio real:
   ./brutalist-art/art run validating-output-from-ai-systems/youtube/claude-liam-different-kind-of-wrong --review
   This is a PREVIZ, not a cut — the pantry is the bottleneck. Show it to me for
   pacing and let me source the stills.

5. Pantry fill → review cut. As I drop stills into pantry/, intake + treat + rename
   them (the `pantry` command word), set shot.focus toward each sentence's subject,
   and fill the provenance sidecars (B03 needs a .source.txt with the photograph's
   rights; any AI-generated real-person image needs the disclosure sidecar). Rerun —
   only changed slots recompile. Honor the vox-run handoff blocks: R0 (B07→B08) and
   R1 (B28→B29→B30) render as one continuous camera move each; every other lane change
   is a hard cut. Never chain continuity across an act boundary.

6. VISUAL QC LAW pass. After each compile, sample frames (ffmpeg fps=2 plus each beat
   at ~15/50/85% of its span), actually READ the PNGs, and audit the 9-point rubric —
   edge bleed, title-safe margins, container overflow, collision, offscreen anchors,
   legibility, brand-bug placement (NBB corner bug every beat; full-size on the outro),
   aspect, and CANVAS FILL (type and content sized to fill the safe area; one terracotta
   moment per beat; segment titles Title Case). Log defects + fixes in _qc/REPORT.md;
   fix root causes in scene source and re-render until zero BLOCKER / zero MAJOR.

7. Master: ./brutalist-art/art final validating-output-from-ai-systems/youtube/claude-liam-different-kind-of-wrong
   Clean cut, no review label, into the reel folder. Update BUILD-LOG.md with gate
   signatures. Do NOT publish — public is a manual Studio flip I do myself.

House laws that bind every beat: COLD OPEN LAW (B00 = ClaudeComposerAsk, ask lands
answered), ILLUSTRATE LAW (the Claude UI appears only at B00, the verdict, the your-turn,
the outro — every inner beat illustrates its concept), SHOW-DON'T-TELL (the animation
enacts the sentence, reveals land on the spoken word), SPARK-LINE LAW (inner spark beats
carry a ≤4-word serif line), REBUILD LAW (no screenshots — everything native animated),
HANDOFF LAW (B34 prompt is read aloud in full and discussed), OUTRO LAW (B35 restates the
title), IN-FOR-BEAR LAW (Liam says it in B00 and signs off in B35). Datable-strip: no model
versions, no vendor tool lists, no "as of" claims. Ship BUILD-PROMPT.md in the folder.
```

---

**If you'd rather run it stepwise by hand (same order):**

1. `./brutalist-art/art todo validating-output-from-ai-systems/youtube/claude-liam-different-kind-of-wrong` — beat ledger
2. FACTCHECK re-verify (Gate F) → narration slate → GATE P sign-off
3. `generate_audio_kokoro.py … claude-liam-different-kind-of-wrong` → lock durations
4. tier-0 `pantry_search.py` pass → write SHOPPING.md (Gate D2)
5. `./brutalist-art/art run … --review` → Gate D1 previz
6. pantry fill → rerun → VISUAL QC → `./brutalist-art/art final …`
