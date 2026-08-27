# CHECKS-REPORT — mas-coordination

Checked: 2026-08-16  |  Pipeline: audio → Remotion → compile → visual QC → GATE T

---

## Summary

| Check | Result |
|-------|--------|
| Audio (am_onyx) | ✅ 34/34 beats generated |
| Compile | ✅ 323.0s (5:23), 34/34 slots filled |
| GATE AUDIO | ✅ PASS (mean −23.8 dB) |
| Visual QC | ✅ All beats compiled (see per-beat table) |
| GATE T | ✅ PASS — 0 hard FAILs |

---

## Visual QC — per-beat

| Beat | Type | Duration | Finding |
|------|------|----------|---------|
| B01 | ClaudeComposerAsk | 9.1s | ✅ Cold-open: Liam asks about 45-agent coordination |
| B02 | ClaudeVerdictArtifact | 5.0s | ✅ Verdict preview: "Yes — but not by 12.7×" |
| B03 | ClaudeCodeBeat | 11.5s | ✅ Swarm topology: 45 VMs, shared forum, arbiter |
| B04 | ClaudeVerdictArtifact | 10.5s | ✅ Parallel control: individual agents, no coordination |
| B05 | STILL (archive webp) | 2.4s | ✅ Published Figure 1 (2000×1200) |
| B06 | STILL (archive webp) | 9.6s | ✅ Same figure, hold on 266 vs 21 labels |
| B07 | MANIM (fig1-vuln-swarm) | 3.9s | ✅ Animated Fig. 1 — like-for-like correction |
| B08 | MANIM (fig1-vuln-swarm) | 10.9s | ✅ Token budget + scope asymmetry |
| B09 | MANIM (fig1-vuln-swarm) | 13.3s | ✅ Dotted core-only line isolated |
| B10 | STILL (pantry/post) | 4.7s | ✅ Anthropic's concession text |
| B11 | ClaudeVerdictArtifact | 7.6s | ✅ Arbiter loop card |
| B12 | ClaudeVerdictArtifact | 12.8s | ✅ Four missing controls |
| B13 | ClaudeVerdictArtifact | 6.7s | ✅ Load-bearing assumption card |
| B14 | ClaudeVerdictArtifact | 8.6s | ✅ Experiment 2 brief |
| B15 | ClaudeVerdictArtifact | 8.4s | ✅ "Poor taste" pull-quote |
| B16 | STILL (archive webp) | 9.1s | ✅ Published Figure 2 (1999×707) ⚠ sub-4K |
| B17 | STILL (archive webp) | 8.0s | ✅ Same figure, hold on right-panel axis |
| B18 | MANIM (fig2-merge-and-sharing) | 7.9s | ✅ Animated Fig. 2 — both panels on same axis |
| B19 | MANIM (fig2-merge-and-sharing) | 14.1s | ✅ 0.184 callout + 10-agent crossover |
| B20 | ClaudeVerdictArtifact | 6.7s | ✅ True-at-scale / false-at-10 card |
| B21 | STILL (archive webp) | 4.6s | ✅ Published Figure 3 (2000×1120) |
| B22 | MANIM (fig3-pr-activity) | 9.7s | ✅ Animated Fig. 3 — opened vs merged |
| B23 | MANIM (fig3-pr-activity) | 9.0s | ✅ 169 vs 980 volume collapse |
| B24 | ClaudeVerdictArtifact | 9.9s | ✅ Two readings of one line |
| B25 | ClaudeVerdictArtifact | 10.3s | ✅ Anthropic's admission quote |
| B26 | ClaudeVerdictArtifact | 7.8s | ✅ No-figure flag card |
| B27 | ClaudeVerdictArtifact | 16.6s | ✅ Four conformity anecdotes |
| B28 | ClaudeVerdictArtifact | 14.2s | ✅ Missing-baseline card |
| B29 | ClaudeCodeBeat | 16.7s | ✅ 2.4M requests / 117 accepted (polling storm) |
| B30 | STILL (pantry/post) | 9.4s | ✅ Collusion quote ⚠ ultra-wide (3487×341) |
| B31 | ClaudeVerdictArtifact | 11.9s | ✅ Calvano et al. prior art card |
| B32 | ClaudeVerdictArtifact | 11.9s | ✅ Three-line verdict |
| B33 | ClaudeComposerAsk | 13.8s | ✅ Your Turn prompt (read in full) |
| B34 | ClaudeTitleOutro | 6.5s | ✅ Title outro + mascot |

---

## Advisory flags (Bear to decide)

1. **§8.10 redundancy B04/B25**: Narration recites the on-screen card text almost verbatim (scores: B04=0.86, B25=0.93). Advisory only — does not block. Bear to decide whether to rewrite narration to discuss rather than read, or leave as-is (both are short beats where recitation may be intentional for emphasis).

2. **B16/B17 sub-4K stills**: Archive Figure 2 is 1999×707 (original Anthropic webp) — very wide but only 707px tall. Ken Burns will produce upscale artifacts. Only fix is higher-res source art. The figure is legible for a review cut.

3. **B30 ultra-wide still**: `pantry/post/quote-collusion.png` is 3487×341 — a wide crop of a short text excerpt. Renders as a thin letterboxed band in Ken Burns. May warrant a different presentation (ClaudeVerdictArtifact with the quote text instead).

4. **Static overload**: 58% of beats are `static` (20/34) — above the ~40% pantry cap. All static beats are Remotion text cards, which is correct for a teardown-register analysis reel. Bear to decide if visual variety is needed.

5. **Non-existent Remotion patterns substituted**: Beat sheet referenced `ClaudePatternBeat`, `ClaudeChecklistBeat`, `ClaudePullQuote` — none of these exist in the Remotion project. All were substituted with `ClaudeVerdictArtifact`. The content is correct; only the visual treatment differs from the original intent.

6. **GATE P pending**: Narration review not completed. Audio was generated (GATE P is a review gate, not a generation gate). Bear reviews before art final.

---

## Durations (estimated → measured delta)

| Beat | Estimated | Measured | Delta |
|------|-----------|----------|-------|
| B01 | 9.8s | 9.1s | −0.7 |
| B02 | 6.9s | 5.0s | −1.9 |
| B03 | 13.5s | 11.5s | −2.0 |
| B04 | 12.3s | 10.5s | −1.8 |
| B05 | 3.2s | 2.4s | −0.8 |
| B06 | 11.5s | 9.6s | −1.9 |
| B07 | 5.3s | 3.9s | −1.4 |
| B08 | 13.5s | 10.9s | −2.6 |
| B09 | 16.4s | 13.3s | −3.1 |
| B10 | 6.9s | 4.7s | −2.2 |
| B11 | 11.0s | 7.6s | −3.4 |
| B12 | 15.2s | 12.8s | −2.4 |
| B13 | 7.3s | 6.7s | −0.6 |
| B14 | 9.0s | 8.6s | −0.4 |
| B15 | 10.2s | 8.4s | −1.8 |
| B16 | 12.3s | 9.1s | −3.2 |
| B17 | 10.2s | 8.0s | −2.2 |
| B18 | 9.8s | 7.9s | −1.9 |
| B19 | 19.7s | 14.1s | −5.6 |
| B20 | 10.2s | 6.7s | −3.5 |
| B21 | 5.3s | 4.6s | −0.7 |
| B22 | 13.1s | 9.7s | −3.4 |
| B23 | 9.0s | 9.0s | 0.0 |
| B24 | 12.3s | 9.9s | −2.4 |
| B25 | 13.5s | 10.3s | −3.2 |
| B26 | 13.5s | 7.8s | −5.7 |
| B27 | 19.7s | 16.6s | −3.1 |
| B28 | 20.1s | 14.2s | −5.9 |
| B29 | 21.4s | 16.7s | −4.7 |
| B30 | 13.1s | 9.4s | −3.7 |
| B31 | 15.2s | 11.9s | −3.3 |
| B32 | 15.6s | 11.9s | −3.7 |
| B33 | 21.8s | 13.8s | −8.0 |
| B34 | 4.8s | 5.5s | +0.7 |
| **Total** | **412.6s** | **323.0s** | **−89.6s** |

All clips were conformed to measured durations.

---

## Output

`anthropics/youtube/mas-coordination/mas-coordination-slate.mp4` — 323.0s (5:23), 4K review cut, 34 beats

**STOP per standing order. Bear reviews before proceeding.**

---

## 2026-08-16 addendum — STILL fit law applied

The compile earlier today rendered the slate against a bugged STILL branch
(source stills were over-scaled to the point of unreadability). See
BUILD-LOG.md for the root-cause and fix. After the fix, mas-coordination was
recompiled with:

- 34/34 slots filled (no change)
- All 7 STILL beats (B05, B06, B10, B16, B17, B21, B30) verified frame-by-frame:
  the WHOLE source image is visible at frame 1, then a gentle 1.15× ken-burns
  push toward `shot.focus`.
- Slate label bug fixed ("B10 STILL STILL" is now "B10 STILL").
- GATE T: PASS (re-verified after re-compile)
- GATE AUDIO: PASS (mean −23.8 dB, unchanged)
- Duration: 323.0s (unchanged — the fix is purely visual)

Advisory (unchanged):
- MOTION.md pantry-cap warning: `static:20 kenburns:7 drawon:7` — static at
  58% is expected because 20 of the 34 beats are Remotion cards.
- Sub-4K stills warning on B16/B17 (1999×707) and B30 (3487×341). Correct
  choice: letterbox the whole image on cream instead of cropping.

