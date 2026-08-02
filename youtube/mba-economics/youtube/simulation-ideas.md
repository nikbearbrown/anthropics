# MBA Economics — Simulation Ideas

*Generated 2026-07-26 · MANIM lane only · Score ≥ 6 · D3 cards excluded*

---

## Candidate 01 — Elasticity Varying Along a Linear Demand Curve

- Source: `mba-economics/chapters/05-elasticity.md`
- Topic: Price elasticity of demand
- Lane: MANIM (directed animation)
- Hook: A single straight demand curve is elastic at the top, inelastic at the bottom, and unitary-elastic exactly in the middle — but students always treat elasticity as a fixed property of the curve.
- The rule: ε = (ΔQ/Q)/(ΔP/P) = (P/Q) × (1/slope); for a linear demand curve Q = a − bP, elasticity at any point = −P/(a/b − P), which sweeps from −∞ at P_max to 0 at Q_max.
- Concrete numbers: Demand curve Q = 100 − 2P (a = 100, b = 2); P ranges from 0 to 50; slope = −2 throughout; elasticity at P = 40 is −4.0 (elastic); at P = 25 is −1.0 (unitary); at P = 10 is −0.25 (inelastic).
- The artifact / what moves: A dot travels down the demand curve from (Q=0, P=50) to (Q=100, P=0) as P decreases; simultaneously a second panel draws the elasticity value as a live number and a color-coded bar (red = elastic, green = inelastic, yellow = unitary) that transitions through all three zones; total revenue rectangle redraws on each frame so the viewer watches revenue rise, peak at the unitary point, then fall.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At exactly P = 25 (the midpoint of the price axis), the elasticity equals −1.0 and total revenue is maximized at $1,250. P2: At P = 40, elasticity = −4.0; a 1% price increase reduces quantity by 4% and total revenue falls.
- The change: Shift the demand intercept from a = 100 to a = 200 (more potential buyers) and watch the unitary-elasticity point relocate to P = 50; the revenue peak moves right.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: There is no such thing as an "elastic good" or "inelastic good" — only elastic or inelastic regions. Every business chooses which region of its own demand curve to price into.
- Exclusions: Cross-price elasticity, income elasticity, supply elasticity — this animation is demand only.
- Sim slug: elasticity-along-linear-demand
- Score: 8/10

---

## Candidate 02 — Monopoly Deadweight Loss: MR = MC Animation

- Source: `mba-economics/chapters/09-monopoly.md`
- Topic: Monopoly pricing and deadweight loss
- Lane: MANIM (directed animation)
- Hook: The deadweight loss triangle is described in every economics course but almost never shown forming in real time — which obscures that it is value that was never created, not value that was taken.
- The rule: Profit-maximizing quantity at MR = MC; for linear demand P = a − bQ, MR = a − 2bQ; competitive quantity where P = MC, monopoly quantity where MR = MC; deadweight loss = ½ × (Q_c − Q_m) × (P_m − P_c).
- Concrete numbers: Demand P = 100 − Q; MC = 20 (constant); MR = 100 − 2Q; MR = MC → Q_m = 40, P_m = 60; competitive Q_c = 80, P_c = 20; monopoly profit = (60 − 20) × 40 = $1,600; DWL = ½ × (80 − 40) × (60 − 20) = $800.
- The artifact / what moves: Demand curve and MC line draw first; then the MR curve draws (same intercept, twice the slope); a vertical marker sweeps right from Q = 0, stops at Q_m = 40 when it intersects MR = MC; the monopoly price reads up to the demand curve; a profit rectangle fills in green; then the DWL triangle to the right of Q_m fills in red, with the label "value destroyed — no one captures this"; finally the competitive equilibrium point appears at Q_c = 80, P_c = 20 and a connecting arc shows what the market would look like.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Monopoly profit rectangle area = $1,600; DWL triangle area = $800 — the DWL is exactly half the profit for this linear/constant-MC case. P2: If MC rises from 20 to 40, Q_m falls to 30, P_m rises to 70, and DWL shrinks to ½ × (60 − 30) × (70 − 40) = $450 — higher MC reduces both output and the waste triangle.
- The change: Add a lump-sum tax equal to the DWL ($800) on the monopolist — show that it does not change Q_m or P_m (lump-sum has no effect on the margin), so DWL persists; contrast with a per-unit tax that does shift MR and worsens DWL further.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The profit rectangle is a transfer — it irritates but can in principle be redistributed; the red triangle is a permanent erasure that no policy can redistribute because those transactions never happened.
- Exclusions: Price discrimination, natural monopoly regulation, multi-period dynamic stories.
- Sim slug: monopoly-deadweight-loss-forming
- Score: 9/10

---

## Candidate 03 — Compound Growth and the Solow Doubling-Time J-Curve

- Source: `mba-economics/chapters/20-economic-growth.md`
- Topic: Compound economic growth; rule of 70
- Lane: MANIM (directed animation)
- Hook: The J-curve of compound growth is described verbally in every macro course, but the moment when a 2%-per-year economy and a 7%-per-year economy diverge by a factor of 10 is almost never shown happening in real time against a common baseline.
- The rule: Y(t) = Y₀ × e^(g×t); doubling time ≈ ln(2)/g ≈ 70/g (rule of 70); after n doublings, Y = 2ⁿ × Y₀.
- Concrete numbers: Y₀ = $1,000 for all economies; g₁ = 0.02 (U.S. frontier), g₂ = 0.05 (catch-up), g₃ = 0.09 (China 1980s peak); at t = 35 years: Y₁ = $2,000 (doubled once), Y₂ = $5,755, Y₃ = $21,644; at t = 70 years: Y₁ = $4,000, Y₂ = $33,115, Y₃ = $469,008.
- The artifact / what moves: Three exponential curves draw simultaneously on a log-scale vertical axis (so straight lines on log scale); a time cursor sweeps from t = 0 to t = 100; at each doubling-time milestone, the curve flashes and the cumulative multiplier appears as a live number; the gap between the slowest and fastest curve widens visibly, with a bracket and ratio label animating in real time; a second sub-panel shows the derivative (annual increment) so the viewer sees absolute gains are also accelerating.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At t = 35 years (one U.S. doubling), the 9%-growth economy has multiplied by ≈21.6× — 10.8× more than the 2% economy. P2: Doubling time for g = 7% is ln(2)/0.07 ≈ 9.9 years; by year 40 the 7% economy has doubled four times (factor 16×) while the 2% economy doubled once (factor 2×).
- The change: Drop g₃ from 9% to 5% at t = 40 (simulating China's post-2015 growth slowdown) — the curve's slope flattens and converges toward g₂; show the divergence gap stopping to widen.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The Solow model is not optimistic — it says capital deepening produces diminishing returns, so the only path to sustained frontier growth is technological progress (TFP), and TFP is the one thing we can't engineer on demand.
- Exclusions: Convergence scatter plots (D3 territory), cross-country institutional comparisons, specific historical timelines.
- Sim slug: compound-growth-j-curve-solow
- Score: 7/10

---

## Candidate 04 — Indifference Curve and Budget Line Tangency

- Source: `mba-economics/chapters/06-consumer-choices.md`
- Topic: Utility maximization; equimarginal rule
- Lane: MANIM (directed animation)
- Hook: The tangency between a budget line and an indifference curve looks static in every textbook, but the reason it's the optimum only becomes clear when you watch the consumer try every other point and see that each other point either wastes budget or lands on a lower utility curve.
- The rule: Maximize U = x^α × y^(1-α) subject to P_x × x + P_y × y = I; at the optimum, MRS = P_x/P_y, which gives x* = αI/P_x, y* = (1−α)I/P_y (Cobb-Douglas interior solution).
- Concrete numbers: α = 0.4, P_x = $2, P_y = $5, I = $100; x* = 0.4 × 100 / 2 = 20, y* = 0.6 × 100 / 5 = 12; U* = 20^0.4 × 12^0.6 ≈ 15.0; budget exhausted: 2×20 + 5×12 = $100. ✓
- The artifact / what moves: A budget line draws first; then three indifference curves appear — one below the optimal (feasible but not maximized), the optimal tangency curve, and one above (infeasible — outside the budget); an "optimizer dot" starts at the left endpoint of the budget line and slides along it; a utility meter in the corner counts up, peaks at the tangency point, then falls as the dot continues; the tangency is highlighted with the slope-equality label MRS = P_x/P_y.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At x = 20, y = 12 the budget is exactly exhausted and the MRS = (α/(1−α)) × (y/x) = (0.4/0.6) × (12/20) = 0.4 = P_x/P_y. P2: If P_x doubles to $4, the new optimum is x* = 0.4×100/4 = 10, y* = 0.6×100/5 = 12; x falls by 50% (own-price elasticity = −1 for Cobb-Douglas), y unchanged (cross-price effect zero for Cobb-Douglas).
- The change: Animate a 50% income increase (I from $100 to $150) — the budget line shifts out parallel, the tangency moves to x* = 30, y* = 18; both goods consume proportionally more because income elasticity = 1 for Cobb-Douglas.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The equimarginal rule is just a tangency condition — it says you've hit the highest feasible indifference curve. Every deviation from the tangency point is money left on the table.
- Exclusions: Corner solutions (when α = 0 or 1), income vs. substitution effect decomposition (separate animation), behavioral departures.
- Sim slug: indifference-curve-budget-tangency
- Score: 7/10

---

## Candidate 05 — Cobb-Douglas Isoquant Map: MPK and MPL as Partial Derivatives

- Source: `mba-economics/chapters/07-production-costs-and-industry-structure.md`
- Topic: Production function; marginal products; isoquants
- Lane: MANIM (directed animation)
- Hook: Diminishing marginal product is described as intuitive but counterintuitive in practice — a farm can hire 100 workers and still get less total output per additional worker than it got from the 5th. The Cobb-Douglas surface makes this viscerally visible.
- The rule: Q = A × K^α × L^(1-α); MPL = ∂Q/∂L = (1−α) × A × K^α × L^(−α); MPK = ∂Q/∂K = α × A × K^(1−α) × L^(1−α); isoquant: K = (Q̄/(A × L^(1-α)))^(1/α).
- Concrete numbers: A = 1, α = 0.3 (capital share), (1−α) = 0.7 (labor share); fix K = 10; MPL at L=1: 0.7×10^0.3×1^(−0.3) ≈ 1.40; at L=10: 0.7×10^0.3×10^(−0.3) = 0.70; at L=100: 0.7×10^0.3×100^(−0.3) ≈ 0.35 — MPL halves each time L increases 10-fold.
- The artifact / what moves: A 3D production surface draws (K on x-axis, L on y-axis, Q on z-axis); then the view rotates to show a 2D isoquant map; a sequence of isoquant curves (Q = 2, 4, 8, 16) appear one by one — each spaced farther apart on the L-axis than the K-axis, reflecting the higher labor share; a tangent line at a moving point on one isoquant draws and its slope animates as MRTS = MPL/MPK; the slope flattens as you move right along the isoquant (more L, less K), visually showing diminishing MRTS.
- Output medium: Manim (mp4)
- Two testable predictions: P1: MRTS at (K=10, L=5) = MPL/MPK = (0.7/0.3) × (K/L) = (7/3) × (10/5) = 4.67; isoquant is steep there. P2: On the Q=4 isoquant, doubling both K and L produces Q = 8 (exactly 2×) — confirming constant returns to scale for Cobb-Douglas with α+(1-α)=1.
- The change: Increase α from 0.3 to 0.6 (more capital-intensive production) — the isoquants rotate; the MRTS at any given K/L ratio changes by the formula (α/(1-α)) × (K/L), so the same point now has a steeper isoquant slope.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: The α and (1−α) parameters are not arbitrary — they equal the capital and labor income shares in a competitive economy. Cobb-Douglas is not just a math convenience; it's calibrated to decades of national accounts data.
- Exclusions: Cost minimization over isocost lines (separate animation), specific industry calibrations.
- Sim slug: cobb-douglas-isoquant-marginal-products
- Score: 7/10

---

## Candidate 06 — Tax Incidence: The Relative-Elasticity Rule

- Source: `mba-economics/chapters/05-elasticity.md`
- Topic: Tax incidence; burden distribution by elasticity
- Lane: MANIM (directed animation)
- Hook: The payroll tax is split 50/50 by law between employers and employees — but economists estimate workers bear roughly 80% of the burden. The elasticity ratio explains the gap, and it's counterintuitive every time.
- The rule: Consumer's share of tax = ε_S / (ε_S − ε_D); producer's share = −ε_D / (ε_S − ε_D); where ε_D < 0 and ε_S > 0.
- Concrete numbers: Labor market; ε_S (labor supply) = 0.1, ε_D (labor demand) = −0.4; worker's burden share = 0.4 / (0.1 + 0.4) = 0.8 (80%); employer's share = 0.1 / (0.1 + 0.4) = 0.2 (20%). Cigarettes: ε_D = −0.3, ε_S = 1.0; consumer's share = 1.0 / (1.0 + 0.3) = 0.77 (77%); producer's share = 23%.
- The artifact / what moves: A supply-and-demand diagram draws; a $1 tax wedge is inserted (shifting the supply curve up by $1); two arrows appear — consumer price rises by 80¢, producer net price falls by 20¢; the split labels animate in; then a slider changes ε_D from −0.1 (very inelastic) to −2.0 (very elastic) while the wedge stays fixed; the consumer-share label counts from 91% down to 33% as demand becomes more elastic; the supply and demand slopes visually steepen and flatten accordingly.
- Output medium: Manim (mp4)
- Two testable predictions: P1: When ε_D = ε_S (equal elasticities), consumer and producer each bear exactly 50% — verified: 0.4/(0.4+0.4) = 0.5. P2: As ε_D → 0 (perfectly inelastic demand), consumer's share → 100%; confirmed by formula: ε_S/(ε_S − 0) = 1.
- The change: Switch the legal incidence from seller to buyer (tax imposed on buyer instead of seller) — show the diagram re-drawn with the demand curve shifting down instead of supply shifting up; the economic incidence (wedge split) is identical; the labels confirm the theorem.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic.
- Teardown angle: Who writes the check to the government is a legal question. Who ends up poorer is an elasticity question. The two answers are almost never the same.
- Exclusions: Specific goods with real-world elasticity estimates (those are for D3 tooltips), multi-market general equilibrium.
- Sim slug: tax-incidence-elasticity-wedge
- Score: 8/10
