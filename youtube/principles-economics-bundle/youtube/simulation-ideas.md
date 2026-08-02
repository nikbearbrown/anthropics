# Principles of Economics Bundle — Simulation Ideas

*Generated 2026-07-26 · MANIM lane only · Score ≥ 6 · D3 cards excluded*

---

*Note: This bundle shares most quantitative content with `mba-economics`. The cards below cover areas where the bundle's treatment either adds unique framing or where the larger student audience warrants a more foundational animation entry-point. Shared candidates (monopoly DWL, elasticity along a demand curve, compound growth, indifference curve tangency) are documented in `mba-economics/youtube/simulation-ideas.md` and not repeated here to avoid duplication.*

---

## Candidate 01 — The Long-Run Competitive Equilibrium: Entry Erodes Profit

- Source: `principles-economics-bundle/chapters/08-perfect-competition.md`
- Topic: Perfect competition; long-run zero profit
- Lane: MANIM (directed animation)
- Hook: Zero economic profit sounds like failure, but it is what every well-functioning competitive market converges to — and watching the profit rectangle shrink to nothing as firms enter is the most counterintuitive result in introductory economics.
- The rule: Short-run: profit = (P − ATC) × Q at the P = MC point; entry shifts supply right → P falls → ATC at Q* falls toward P; long-run: P = min(ATC) = MC simultaneously; entry stops when economic profit = 0.
- Concrete numbers: Initial market price P₀ = $80; firm ATC minimum = $50 at Q* = 100 units; initial profit = ($80 − $50) × 100 = $3,000 per firm; 50 firms; market supply Q_S = 5,000. Entry over five periods: +10 firms per period; after 5 periods 100 firms; new equilibrium P₁ = $65; profit = ($65 − $50) × 100 = $1,500 per firm; convergence continues to P* = $50 (zero profit).
- The artifact / what moves: Two-panel animation — left panel: market supply-and-demand diagram; right panel: individual firm cost-curve diagram. As a "period" counter ticks from 1 to 10, the market supply curve shifts right in steps; the equilibrium price line falls and is simultaneously drawn on the right panel; the profit rectangle between P and ATC shrinks visually in real time; at P = $50 = min(ATC), the rectangle collapses to zero, the firm's output dot sits exactly at the bottom of the U-shaped ATC curve, and a label appears: "Productive efficiency + Allocative efficiency achieved."
- Output medium: Manim (mp4)
- Two testable predictions: P1: The long-run equilibrium price equals the minimum of the ATC curve (= $50); at this price MC also equals $50, so P = MC = min(ATC) simultaneously — both efficiency conditions hold at the same output level. P2: The total industry output at long-run equilibrium = Q* × N_final; if each firm produces 100 units and 100 firms are in the market, Q_industry = 10,000 — double the initial quantity, at a price 37.5% lower.
- The change: Raise input costs (shift ATC up by $10) after the equilibrium is reached — the profit rectangle reappears as negative (a loss); firms begin to exit; supply shifts left; price rises; losses shrink; the new zero-profit equilibrium settles at min(ATC_new) = $60.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The zero-profit theorem is not pessimism. It is the mechanism that makes competitive markets direct resources efficiently. Once you see it, every industry with sustained positive profits is a neon sign saying "something is blocking entry here."
- Exclusions: Monopolistic competition (different structure), supply-and-demand *shifts* from non-entry sources.
- Sim slug: competitive-equilibrium-entry-erodes-profit
- Score: 8/10

---

## Candidate 02 — Short-Run Cost Curves: MC Crosses ATC at Its Minimum

- Source: `principles-economics-bundle/chapters/07-production-costs-and-industry-structure.md`
- Topic: Cost curves; marginal cost; average total cost
- Lane: MANIM (directed animation)
- Hook: "Marginal pulls average" is stated in every economics textbook, but most students cannot explain *why* the MC curve must cross ATC exactly at ATC's minimum — a fact with a clean, visualizable proof.
- The rule: ATC = TC/Q; MC = dTC/dQ; d(ATC)/dQ = (MC − ATC)/Q; so d(ATC)/dQ = 0 when MC = ATC. The crossing must be at the minimum.
- Concrete numbers: TC = Q³ − 12Q² + 60Q + 100 (fixed cost = 100); ATC = Q² − 12Q + 60 + 100/Q; MC = 3Q² − 24Q + 60; ATC minimized at dATC/dQ = 2Q − 12 − 100/Q² = 0 → approximately Q = 6.3; MC(6.3) ≈ 3(6.3)² − 24(6.3) + 60 ≈ 27.7; ATC(6.3) ≈ 27.7. ✓ (Both equal at the crossing.)
- The artifact / what moves: TC curve draws on the top panel; on the bottom panel, ATC and MC curves draw simultaneously; a tracking dot moves along the ATC curve from left to right; a live slope indicator shows "ATC is falling — MC < ATC" to the left of the minimum, then "ATC is rising — MC > ATC" to the right; at the crossover Q ≈ 6.3, the dot highlights in gold and the label "MC = ATC = min(ATC)" appears; simultaneously the fixed-cost hyperbola AFC draws and is labeled "keeps falling forever."
- Output medium: Manim (mp4)
- Two testable predictions: P1: At Q = 5 (left of minimum), MC = 3(25) − 24(5) + 60 = 75 − 120 + 60 = 15; ATC = 25 − 60 + 60 + 20 = 45. MC < ATC ✓, ATC is falling. P2: At Q = 8 (right of minimum), MC = 3(64) − 24(8) + 60 = 192 − 192 + 60 = 60; ATC = 64 − 96 + 60 + 12.5 = 40.5. MC > ATC ✓, ATC is rising.
- The change: Double the fixed cost (FC from 100 to 200) — show that the MC curve does not move (MC = dTC/dQ, fixed costs drop out), but ATC shifts up everywhere and its minimum moves slightly to the right; the crossing still occurs at the ATC minimum, but the minimum is now higher.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The MC-crosses-ATC-at-minimum rule is not a coincidence — it's a consequence of the derivative condition. A firm that doesn't understand this will misread its own cost data and make wrong output decisions at scale.
- Exclusions: Long-run average cost curves (require capital variation), economies of scale comparisons across industries.
- Sim slug: mc-crosses-atc-at-minimum
- Score: 7/10

---

## Candidate 03 — Intertemporal Budget Constraint and the Interest Rate Pivot

- Source: `principles-economics-bundle/chapters/06-consumer-choices.md`
- Topic: Intertemporal choice; saving; interest rate effects
- Lane: MANIM (directed animation)
- Hook: The textbook says "higher interest rates increase saving" — but the animation shows the income and substitution effects pulling in *opposite* directions, making the prediction ambiguous for consumers who start as net lenders vs. net borrowers.
- The rule: Budget constraint: C_future = (1 + r)(I_present − C_present) + I_future; slope = −(1 + r); optimal tangency at the indifference-curve MRS = (1 + r); for Cobb-Douglas intertemporal utility U = C_present^α × C_future^(1−α), C*_present = α(I_present + I_future/(1+r)).
- Concrete numbers: I_present = $100, I_future = $105, α = 0.5; at r = 0.05: endowment point (100, 105); budget constraint passes through (100, 105) with slope −1.05; optimal C*_present = 0.5 × (100 + 105/1.05) = 0.5 × 200 = $100 → no saving (exactly consuming endowment); at r = 0.10: C*_present = 0.5 × (100 + 105/1.10) = 0.5 × 195.45 = $97.73 → saving $2.27 (saver is helped by higher rate).
- The artifact / what moves: An (x = C_present, y = C_future) diagram draws; the endowment point plots as a dot; the budget line draws through the endowment with slope −(1+r); an indifference curve is tangent at the optimum; a slider changes r from 0% to 20% in steps; the budget line *pivots around the endowment point* as r changes (the endowment is always feasible regardless of r); the tangency point moves; a label tracks "saving = I_present − C*_present" and turns positive (yellow) when the consumer saves and negative (red) when they borrow.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 0%, slope = −1; C*_present = 0.5×(100 + 105) = $102.5 → consumer borrows $2.50 against future income; endowment point is to the left of optimum. P2: At r = 10%, C*_present = $97.73 as computed — consumer saves $2.27; the higher return makes deferring consumption worthwhile.
- The change: Make α = 0.3 (patient consumer who values future consumption more) — at r = 5%, C*_present = 0.3×200 = $60; saving = $40; the tangency point sits far to the left of the endowment, and the budget-line pivot barely moves it.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The standard "higher rates → more saving" claim is only correct for consumers who start as savers. Net borrowers face an income effect that runs the other way. The ambiguity is not a model failure — it's the model telling the truth about heterogeneous households.
- Exclusions: Multi-period retirement planning, behavioral hyperbolic discounting (different animation), general equilibrium interest-rate determination.
- Sim slug: intertemporal-budget-interest-rate-pivot
- Score: 7/10
