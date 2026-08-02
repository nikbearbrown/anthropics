# PLAN.md — claude-liam-arima-integrated (deep-explainer)

**Source:** A third-party ARIMA tutorial transcript (supplied by Bear; ~9 min
spoken walkthrough of the ARIMA model — trend → differencing → model →
recovery). Treated as PEDAGOGICAL SOURCE, not a script to read. The math is
standard and independently verified (see FACTCHECK.md).
**Channel:** claude-liam (Liam in for Bear, Kokoro `am_onyx`, free).
**Register:** Teardown. **Aspect:** 16:9.

**Thesis (one line):** AR, MA, ARMA all need a stationary series — but real
series trend. The "I" in ARIMA is the fix: difference the series until the
trend is gone, model the differences, then integrate back to forecast.

**Estimated landing:** ~4:45–5:15 from ~560 planned body words + bookends at
~2.9 w/s plus holds. In-band for the genre; duration is an output.

---

## TWO FLAGS FOR YOU (decide at the plan gate)

1. **Concrete example — swapped.** The source teaches with a boat-anchor
   salesman. That's another creator's signature example, so I drafted an
   ORIGINAL concrete series — **monthly e-bike sales at a shop (thousands),
   clean upward linear trend**. Same pedagogy (concrete-before-abstract,
   linear trend → constant differences), no lifted example. Say the word and
   I'll revert to anchors, or pick a different product.
2. **Owning book.** Bound to `computational-finance/` (ARIMA forecasting fits
   there). Equally at home in `math-statistics/` or a dedicated time-series
   book — tell me and I'll move the folder.

---

## Act map

| Act | Beats | Claim |
|---|---|---|
| B00 cold open | 1 | Ask answered: "I know AR, MA, ARMA — what's the I in ARIMA?" |
| ACT I — The Trend Problem | 6 | Real series trend; ARMA needs stationarity; a shifting mean breaks it |
| ACT II — The I Is for Integrated | 6 | Difference the series (Z_t = a_t − a_{t−1}); linear trend → constant differences; the differenced series is stationary |
| ACT III — ARIMA(p, d, q) | 4 | Three orders; d = differencing; the ARIMA(1,1,1) equation, AR/I/MA colour-mapped |
| ACT IV — Integrating Back | 4 | Recover a_t from the differences by a cumulative sum → forecast |
| Closing block | 3 | VERDICT recap → YOUR TURN (read in full) → TITLE re-read |

## Lane histogram (20 body beats)

```
VOX      ████        4/20  20%   (target 20–25% ✓)
MANIM    ██████      6/20  30%   (target 25–40% ✓)
REMOTION ██████      6/20  30%   (target 30–45% ✓)
CARD     ████        4/20  20%   (act cards)
```
No lane runs >2 consecutive except vox run R1 (2 beats, in Act I). Runs never
cross an act boundary. Equation tangents at B10, B15, B18. ✓ lint clean.

---

## Beat list (narration drafts; body beats ~22–34 words)

### B00 — cold open (exempt; ClaudeComposerAsk)
> Bonjour — this is Liam, in for Bear. You already know AR, MA, ARMA — the
> autoregressive moving-average model. So what's that extra I doing in
> ARIMA? Let's take it apart.

Typed ask: "Hey Claude — I know the ARMA model for time series. What does the
I in ARIMA add, and when do I actually need it? Teach me the whole thing."
Output lines: "One extra letter, one big idea: difference the trend away." /
"Act One: why plain ARMA breaks."

### ACT I — The Trend Problem
- **B01 CARD** — "Act I — The Trend Problem"
- **B02 VOX — run R1, beat 1** (still: time-series-are-everywhere — ticker tape / chart wall): "Time series are everywhere — prices, temperatures, sales. The game is always the same: use the past to forecast the next step."
- **B03 VOX — run R1, beat 2** (pull to the concrete series: a shop's e-bike sales ledger): "Say you sell e-bikes, and you track units per month. You want next month's number — so you plot what you've got."
- **B04 MANIM** (time-series plot, clear upward trend): "And there it is: a steady climb, month over month. Useful — but that climb is exactly what stops you from using ARMA."
- **B05 REMOTION** (stationarity checklist: constant mean · constant variance · no seasonality): "ARMA needs a STATIONARY series: constant mean, constant variance, no seasonality. Check the list — this one fails on the very first item."
- **B06 MANIM** (highlight the drifting mean line): "The mean isn't constant — it drifts upward with the trend. Feed that to ARMA and the model chases a moving target. We need to kill the trend."

### ACT II — The I Is for Integrated
- **B07 CARD** — "Act II — The I Is for Integrated"
- **B08 VOX** (still: George Box & Gwilym Jenkins — verified portrait/context): "In nineteen-seventy, statisticians George Box and Gwilym Jenkins gave us the fix, and the name for it: the I in ARIMA stands for Integrated."
- **B09 REMOTION** (acronym unpack: AR · I · MA; "Integrated ≠ integrals"): "And before you brace for calculus — this integrated has nothing to do with integrals. It means one plain operation: differencing."
- **B10 MANIM equation** (define Z_t = a_t − a_{t−1}): "Build a new series. Z at time t is just this month minus last month — the CHANGE. You stop modelling the level, and start modelling the step."
- **B11 REMOTION C3** (linear step-up: constant rise → constant difference): "Why does that help? A straight-line trend climbs by the same amount every step. Subtract consecutive points, and that constant is all that's left."
- **B12 MANIM** (the Z_t plot, hovering flat around a constant mean): "So plot the differences, and the trend is gone. Z hovers around a constant mean — constant variance, no seasonality. Stationary. Now ARMA is fair game."

### ACT III — ARIMA(p, d, q)
- **B13 CARD** — "Act III — ARIMA(p, d, q)"
- **B14 REMOTION** (three-parameter card: p = AR order · d = differencing · q = MA order): "ARMA had two knobs, p and q. ARIMA has three: p, d, q. The new one, d, is how many times you differenced — here, once."
- **B15 MANIM equation** (ARIMA(1,1,1): Z_t = φ₁Z_{t−1} + θ₁ε_{t−1} + ε_t, AR/I/MA colour-mapped): "The simplest case, ARIMA one-one-one: model the DIFFERENCE Z with one AR term, one MA term. The I is hiding in plain sight — Z is already a difference."
- **B16 REMOTION** (higher-order differencing: d=2, second difference W_t): "Still trending after one pass? Difference again — that's d equals two. But keep d as low as it takes; simpler models generalize better."

### ACT IV — Integrating Back
- **B17 CARD** — "Act IV — Integrating Back"
- **B18 MANIM equation** (recovery: a_k = a_L + Σ Z, telescoping/cumulative sum): "But you wanted e-bikes sold, not differences. So integrate back: start from your last real value and add up the predicted steps. A cumulative sum."
- **B19 REMOTION C3** (differencing ↔ integrating, the two arrows): "THAT'S why it's 'integrated' — undoing the differencing is a running sum, the discrete cousin of an integral. Difference to model; integrate to forecast."
- **B20 VOX** (still: forecasting / business-decision payoff): "And now you have next month's number — the forecast you couldn't get from the raw, trending series. One extra letter, whole new reach."

### Closing block (your-turn standard, exempt)
- **B21 VERDICT** (ClaudeVerdictArtifact): recap — trend breaks ARMA · difference to reach stationarity (the I) · ARIMA(p,d,q), d = differencing order · integrate back to forecast · keep d as small as it takes.
- **B22 YOUR TURN** (ClaudeComposerAsk, greeting "Your turn.", read in full): "Take a trending series you care about. Difference it once and plot it — is it stationary yet? If not, difference again. Tell me the smallest d that flattens it, and why over-differencing would cost you."
- **B23 TITLE outro** (ClaudeTitleOutro): title re-read.

---

## Vox runs (handoff blocks authored at beat-sheet time)

- **R1** (B02→B03, Act I): one camera move — wide on the "time series
  everywhere" plate (s1.0) → push in to the concrete e-bike ledger detail
  (x0.5 y0.55 s1.6). Pantry: one wide plate, or `-bg/-mid` layers.

## Vox shopping preview (SHOPPING.md proper comes ONLY after audio lock)

4 vox slots:
- **B02, B03** (run R1) — Tier 1: "time series everywhere" (ticker/chart wall)
  + the concrete e-bike sales ledger. AI-generate or stock.
- **B08** — **Tier 3: George Box & Gwilym Jenkins** — real named people →
  archival photograph, the PHOTOGRAPH's rights govern; rights check escalates
  to you every time. AI-portrait fallback is labelled per the disclosure
  sidecar. (If sourcing is a hassle, this beat can fall back to a Remotion
  type card — say so and I'll re-lane it, nudging VOX to ~16%.)
- **B20** — Tier 1: forecasting / business-decision payoff still.

All treated per the vox laundering function (desat ~80%, Claude cream stage,
grain, terracotta the one accent).

## Gate state

- [ ] **PLAN GATE — Bear approves the act map + lane mix + the two flags above**
- then: beat_sheet.json (vox_run/handoff + Manim scene names + Remotion props +
  equation specs) → FACTCHECK re-confirm → GATE P narration → Kokoro audio →
  SHOPPING.md → Gate D1 slate previz on the Mac (compile now floors to 4K).
