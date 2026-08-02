# CAJAL figure candidates — mba-math (previz track)

Mechanism figures mined from chapter content. Blank unannotated vector — no baked text. Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

Zero-candidate chapters (quantitative computational — route to graphs skill): 01 (percentages/ratios — bar charts), 02 (algebra — break-even line charts), 03 (financial statement math — tables), 04 (TVM — timeline tables), 05 (DCF/NPV/IRR — value curves), 06 (CAPM/WACC — scatter plots, SML → graphs), 07 (probability — tables), 08 (statistics — histograms, sampling distributions → graphs), 09 (regression — scatter plots → graphs), 10 (portfolio math — efficient frontier curves → graphs), 11 (calculus — marginal cost/revenue curves → graphs), 14 (quantitative finance — option payoff diagrams, Monte Carlo → graphs).

---

## 1. decision-tree-rollback  — settle-vs-trial litigation decision tree with rollback EMV  (MC · process flowchart · Important)
*Source: chapter 13 — "Decision Analysis: Trees, Expected Utility, and Bayes"*

**PASTE:** Draw a blank two-stage decision tree on a white background: a root square decision node on the left splits into two branches. The upper branch leads directly to a terminal circle (the "settle" outcome). The lower branch leads to a chance circle (diamond-shaped node), which then splits into two branches — upper (favorable outcome, probability 0.6) leading to a terminal circle, and lower (unfavorable outcome, probability 0.4) leading to a terminal circle. A small annotation box sits at the chance node showing the rolled-back EMV. No labels, no text, flat fills, uniform strokes.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] litigation decision tree: root decision square (settle or go to trial); settle branch (upper) → terminal node at fixed cost ($400K); trial branch (lower) → chance circle → 60% probability: win at $0 cost / 40% probability: lose at $1.2M cost. EMV of trial = 0.6×0 + 0.4×$1.2M = $480K > $400K settle, so settle is optimal. Rollback rule: take expectation at chance circles, take best option at decision squares.
- [O] root square at left; upper branch straight to terminal circle; lower branch to chance circle (diamond); chance circle branches to two terminal circles with probability weights noted by tick marks; rolled-back EMV annotation box at chance node; left-to-right tree structure.
- [P] flat vector, Okabe-Ito: decision square Blue #0072B2, chance diamond Orange #E69F00, favorable terminal Bluish Green #009E73, unfavorable terminal Vermillion #D55E00, settle terminal Sky Blue #56B4E9, rollback box neutral gray. No baked text.
- [E] exclude: risk aversion / expected utility theory, EVPI formula, Bayes updating, real-options extension.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. bayes-natural-frequency-tree  — 1000-firm fraud audit cascading into flagged/not outcomes  (MC · process flowchart · Important)
*Source: chapter 13 — "Decision Analysis: Trees, Expected Utility, and Bayes"*

**PASTE:** Draw a blank natural-frequency tree on a white background: a single wide rectangle at the top (1000 firms) splits downward into two rectangles — a small rectangle on the left (10 fraudulent firms) and a wide rectangle on the right (990 clean firms). Each of those two rectangles then splits downward again: the fraudulent rectangle splits into "correctly flagged" (small circle) and "missed" (small circle); the clean rectangle splits into "wrongly flagged" (small circle) and "correctly passed" (large circle). Total six nodes. No labels, no text, flat fills, uniform strokes. Node sizes are proportional to counts.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] Bayes natural frequency structure: 1000 firms total; 10 fraudulent (1%), 990 clean (99%). Fraudulent: 9 correctly flagged (90% sensitivity), 1 missed. Clean: 50 wrongly flagged (5% false positive rate), 940 correctly passed. Total flagged = 9 + 50 = 59. Post-test probability of fraud given flag = 9/59 ≈ 15% — not the intuitive 90%. Base-rate neglect: the small fraudulent pool means most flagged firms are false positives. This is the same as the prosecutor's fallacy: confusing P(flag|fraud) with P(fraud|flag).
- [O] root rectangle (1000) at top; splits into two child rectangles (10 fraudulent small, 990 clean large); each child splits into two terminal circles proportional in size to their counts; node sizes reflect relative frequencies.
- [P] flat vector, Okabe-Ito: root rectangle Blue #0072B2, fraudulent sub-tree Vermillion #D55E00, clean sub-tree Bluish Green #009E73, flagged terminal circles Orange #E69F00, unflagged terminal circles neutral gray; proportional sizing. No baked text.
- [E] exclude: Bayes formula notation, posterior vs. prior formal notation, quality-inspection example (separate application), audit firm names.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. prisoner-dilemma-payoff-matrix  — 2×2 payoff matrix with Nash equilibrium and jointly-optimal cell distinguished  (MC · comparison panels · Important)
*Source: chapter 12 — "Matrices, Linear Programming, and Game Theory"*

**PASTE:** Draw a blank 2×2 payoff matrix on a white background: four equal cells arranged in a two-by-two grid separated by thin lines. Each cell contains two small rectangles in opposite corners representing the two players' payoffs. One cell (bottom-right, the Nash equilibrium) has a heavier border. One cell (top-left, the jointly best but unstable outcome) has a dashed border. A horizontal axis band above the grid and a vertical axis band to the left indicate strategy dimensions. No labels, no text, flat fills, uniform strokes.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] two firms (A and B) each choose High or Low price/output: (High,High) = (50,50) jointly optimal, unstable (dashed border — each firm wants to defect to the 80 corner); (High,Low) = (10,80) A loses, B gains; (Low,High) = (80,10) A gains, B loses; (Low,Low) = (20,20) Nash equilibrium (heavy border — dominant strategy for both, stable despite mutual preference for High,High). Nash result: individually rational dominant-strategy play lands both players in the worse collective outcome — the prisoner's dilemma structure.
- [O] 2×2 grid; rows = Firm A's strategy (High/Low); columns = Firm B's strategy (High/Low); Nash equilibrium cell (Low,Low) heavy border; jointly-optimal cell (High,High) dashed border; payoff circles in opposing corners of each cell.
- [P] flat vector, Okabe-Ito: Firm A payoff circles Blue #0072B2, Firm B payoff circles Bluish Green #009E73, Nash equilibrium cell border Vermillion #D55E00 (heavy), jointly-optimal cell border Sky Blue #56B4E9 (dashed), grid lines neutral gray. No baked text.
- [E] exclude: mixed-strategy equilibria, cartel legal analysis, OPEC case, Coke-Pepsi advertising example.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE decision-tree-rollback — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE bayes-natural-frequency-tree — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE prisoner-dilemma-payoff-matrix — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.

**Chapter recommendation:** **decision-tree-rollback** — the sole video candidate; a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
