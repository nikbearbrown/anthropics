# Economics — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build an Elasticity Calculator and Revenue Predictor with Claude Code

- Source: economics/chapters/05-elasticity.md
- Lane: BUILD (Claude Code)
- Hook: Netflix raised prices 60% and revenue went up. Most people's intuition says that's wrong. One number — the price elasticity of demand — predicts it before you open the news.
- The artifact: A Python elasticity calculator and revenue simulator. Inputs: current price, current quantity demanded, elasticity estimate (with a slider for range), proposed price change percent. Outputs: (1) new quantity demanded via arc elasticity formula, (2) new total revenue, (3) an animated demand curve showing the original and new price-quantity points, with the revenue rectangle and the "lost quantity" triangle both labeled, (4) a revenue-vs-price-change curve that sweeps the price change from -50% to +100% and shows where revenue peaks (the unitary elasticity point). Demo: replicate the Netflix 2011 case (60% price hike, estimated elasticity ~0.3) and show revenue increase.
- Prompt seed: `claude "Build a Python elasticity calculator and revenue simulator. Inputs: P0 (original price), Q0 (original quantity), elasticity (absolute value, with low/high range), delta_P_pct (proposed price change %). Outputs: new quantity via midpoint elasticity formula, new total revenue, direction of revenue change. Plot: (1) animated demand curve with revenue rectangle before/after, (2) revenue vs delta_P_pct curve sweeping -50% to +100%, marking the unitary-elasticity revenue peak. Demo: Netflix 2011 (P0=$9.99, delta_P=+60%, elasticity=0.3). Show revenue increases despite quantity drop."`
- Read / check: Verify the midpoint formula is implemented correctly (not the simple formula). Confirm that at elasticity=1 the revenue-vs-price curve peaks. Check that the Netflix demo shows a revenue increase with a quantity decrease. Verify the animated demand curve shows the rightward revenue rectangle shrinking but the price rectangle growing more.
- Human supplies: Nothing — fully synthetic. The Netflix parameters come directly from the chapter. No real data sources needed.
- Output medium: Manim (animated demand curve with rectangle, then revenue-vs-price sweep curve building left to right with peak labeled)
- The change: Swap in an elastic good (elasticity=1.8, representing a streaming service in a competitive market with many substitutes in 2024) and watch the revenue curve invert — price hike now loses revenue. Shows how the same company in a different competitive environment faces a completely different pricing constraint.
- Teardown angle: Elasticity is not a property of a good — it's a property of a market situation. The same company's elasticity changed as competitors arrived. The Netflix story is a case study in how time changes the math.
- Exclusions: Income elasticity and cross-price elasticity deep-dives, Giffen goods, tax incidence derivation (save for separate card).
- Score: 9/10

---

## Candidate 02 — Simulate Tax Incidence with Elastic/Inelastic Supply and Demand

- Source: economics/chapters/05-elasticity.md
- Lane: BUILD (Claude Code)
- Hook: A payroll tax is split 50/50 between employer and employee by law. In the long run, workers pay 80% of it. The legal split and the economic split are different things, and the difference is computable from two elasticity numbers.
- The artifact: A Python tax incidence simulator. Inputs: demand elasticity (Ed), supply elasticity (Es), tax amount per unit. Outputs: (1) buyer's share of tax burden = Es/(Ed+Es), seller's share = Ed/(Ed+Es), (2) animated supply-and-demand diagram showing the pre-tax equilibrium, then the tax wedge inserted, then the new buyer price and seller price labeled, (3) a sensitivity surface: a heatmap showing buyer burden fraction across a grid of Ed (0.1 to 3.0) and Es (0.1 to 3.0). Demo cases: cigarettes (Ed=0.4, Es=1.5 — buyer bears most), beachfront real estate (Ed=2.0, Es=0.1 — seller bears most), labor market (Ed=1.2, Es=0.5 — worker bears ~70%).
- Prompt seed: `claude "Build a Python tax incidence simulator. Inputs: Ed (demand elasticity), Es (supply elasticity), tax T per unit. Formulas: buyer_share = Es/(Ed+Es), seller_share = Ed/(Ed+Es). Plot: (1) animated S&D diagram with pre-tax equilibrium, then tax wedge T, new Pb and Ps labeled, tax rectangle shaded with buyer/seller split, (2) heatmap: buyer_burden_fraction over Ed=[0.1..3.0] × Es=[0.1..3.0] grid. Run 3 demo cases: cigarettes (Ed=0.4, Es=1.5), beachfront (Ed=2.0, Es=0.1), labor (Ed=1.2, Es=0.5). Print buyer/seller split for each."`
- Read / check: Verify the buyer-share formula Es/(Ed+Es) is correct. Confirm the labor market case gives approximately 70% worker burden. Check the heatmap is symmetric (swapping Ed and Es flips buyer/seller shares). Verify the animated diagram shows the tax wedge correctly as the vertical gap between the two prices.
- Human supplies: Nothing — fully synthetic. All elasticity inputs and the formula come from the chapter.
- Output medium: Manim (animated S&D diagram with tax wedge appearing, then heatmap building cell by cell, three demo cases labeled)
- The change: Add a "long-run" slider that increases both Ed and Es (as buyers and sellers have more time to adjust) and watch the incidence fractions shift — demonstrating the chapter's core claim that elasticity grows with time and incidence changes accordingly.
- Teardown angle: The tax burden falls on whichever side is less elastic — whichever side can't leave. The legal incidence is irrelevant. This is why payroll taxes fall on workers even when they're nominally split: workers have fewer exit options than capital.
- Exclusions: Deadweight loss from taxation, Ramsey optimal taxation theory, specific tax policy recommendations.
- Score: 9/10

---

## Candidate 03 — Build a Monopoly Deadweight Loss Calculator with Claude Code

- Source: economics/chapters/09-monopoly.md
- Lane: BUILD (Claude Code)
- Hook: The Boston Tea Party started with a monopoly grant. The economic cost of monopoly isn't abstract — it's a triangle you can compute, and it turns out the transfer to the monopolist is much larger than the deadweight loss.
- The artifact: A Python monopoly welfare calculator. Inputs: linear demand function (price-intercept, slope), constant marginal cost. Outputs: (1) competitive equilibrium (P=MC, Q_comp), (2) monopoly equilibrium (MR=MC, Q_mono, P_mono), (3) consumer surplus under competition, (4) consumer surplus under monopoly, (5) monopoly profit, (6) deadweight loss triangle area, (7) an animated diagram building the demand curve, MR curve, MC line, then revealing competitive equilibrium, then monopoly equilibrium, with the DWL triangle shaded and the profit rectangle shaded in different colors, labeled with dollar amounts.
- Prompt seed: `claude "Build a Python monopoly welfare calculator. Inputs: demand intercept a, demand slope b (so P = a - b*Q), marginal cost MC (constant). Compute: Q_comp = (a-MC)/b, P_comp = MC; MR = a - 2b*Q → Q_mono = (a-MC)/(2b), P_mono = a - b*Q_mono; consumer surplus under competition and monopoly, monopoly profit = (P_mono-MC)*Q_mono, DWL = 0.5*(P_mono-MC)*(Q_comp-Q_mono). Plot animated diagram: demand curve, MR curve, MC line, competitive equilibrium labeled, then monopoly equilibrium labeled, profit rectangle shaded, DWL triangle shaded. Print all values."`
- Read / check: Verify Q_comp = (a-MC)/b and Q_mono = (a-MC)/(2b). Confirm DWL = 0.5*(P_mono-MC)*(Q_comp-Q_mono) (triangle area formula). Check that profit > DWL for typical parameters (the transfer exceeds the efficiency loss). Verify MR curve has twice the slope of demand.
- Human supplies: Nothing — fully synthetic. Linear demand with constant MC is a textbook construction.
- Output medium: Manim (animated diagram: demand curve draws left to right, MR curve appears, MC line horizontal, then competitive point appears, then monopoly point appears, DWL triangle fills in red, profit rectangle fills in blue)
- The change: Add natural monopoly mode: give the firm decreasing average cost (ATC curve) so that MC < ATC at Q_mono — demonstrate the regulatory dilemma where forcing P=MC produces losses, and show the P=ATC "rate-of-return regulation" compromise.
- Teardown angle: The monopoly profit (the transfer) is much larger than the deadweight loss (the efficiency loss). This is why monopoly is a distributional problem as much as an efficiency problem — and why antitrust is political even when the economics are clear.
- Exclusions: Price discrimination strategies, oligopoly Nash equilibrium, antitrust case specifics.
- Score: 8/10

---

## Candidate 04 — Build an AD-AS Shock Simulator with Claude Code

- Source: economics/chapters/24-the-aggregate-demand-aggregate-supply-model.md
- Lane: BUILD (Claude Code)
- Hook: In 2006 the U.S. built 1.6 million homes. In 2009 it built 550,000. One sector's collapse moved every macroeconomic variable in the country. The AD-AS model predicts which way they all moved — and the size of the fiscal stimulus needed to get back.
- The artifact: A Python AD-AS shock simulator. The model: linear AD curve (P decreasing in GDP), SRAS curve (three zones — horizontal Keynesian, upward-sloping intermediate, vertical neoclassical), LRAS as a vertical line at potential GDP. Inputs: shock type (AD left/right, AS left/right, supply shock vs demand shock), shock magnitude, fiscal multiplier. Outputs: (1) pre-shock equilibrium (P*, GDP*), (2) short-run post-shock equilibrium, (3) long-run adjustment path (if LRAS constraint), (4) animated diagram showing all three curves, the shock arrow, and both equilibria labeled, (5) a summary table: ΔP, ΔGDP, which "zone" the economy is in, whether fiscal or monetary policy is effective in that zone.
- Prompt seed: `claude "Build a Python AD-AS shock simulator. Model: AD as P = AD_intercept - slope_AD*GDP; SRAS with three zones: horizontal (Keynesian, P=P_floor for GDP < 0.85*GDP_potential), upward-sloping (0.85 to 1.0*GDP_potential), vertical (neoclassical, GDP=GDP_potential). LRAS vertical at GDP_potential. Inputs: shock type (AD_shift or AS_shift), shock magnitude. Compute short-run and long-run equilibria. Plot animated diagram with curves, shock arrow, both equilibria labeled, zone boundaries. Print: ΔP, ΔGDP, zone, policy effectiveness. Demo: 2008 recession (AD left shift by 15%) and 2020 COVID supply shock (SRAS left shift by 10%)."`
- Read / check: Verify the 2008 AD-left-shift scenario shows GDP falling and P falling (Keynesian zone). Confirm the LRAS constraint correctly prevents GDP from staying below potential in the long run. Check the policy-effectiveness output correctly identifies that fiscal policy is effective in the Keynesian zone and ineffective in the neoclassical zone.
- Human supplies: Nothing — fully synthetic. The model is a stylized three-zone SRAS construction, not calibrated to real data.
- Output medium: Manim (three curves drawing, equilibrium points appearing, shock arrow animating left/right, new equilibrium revealing, zone labels appearing)
- The change: Add a simultaneous adverse supply shock + fiscal stimulus (the stagflation scenario) and show why AD-right doesn't restore both price stability and full employment when AS has shifted left — the policy can fix output or fix prices but not both.
- Teardown angle: The zone the economy is in determines which policy tools work. Fiscal stimulus in the Keynesian zone raises GDP with little inflation. The same stimulus in the neoclassical zone raises prices with little real GDP gain. Reading the zone is the prerequisite to choosing the tool.
- Exclusions: Full Keynesian multiplier derivation, IS-LM model, exchange rate feedbacks, specific country case studies.
- Score: 8/10

---

## Candidate 05 — Research the CPI Measurement Bias with Claude

- Source: economics/chapters/22-inflation.md
- Lane: RESEARCH (Claude assistant)
- Hook: CPI overstates true inflation by a percentage point or two per year. Over 40 years of Social Security COLAs, that's a multi-trillion dollar cumulative overpayment. The bias has a name (substitution bias), a method for correcting it (chained CPI), and a political reason why the correction was slow to adopt.
- The artifact: A sourced 4-section research brief: (1) the three CPI biases named and quantified (substitution ~0.5pp, quality ~0.4pp, new-goods ~0.1pp) with citations to Boskin Commission report and BLS methodology docs, (2) the chained CPI and PCE as corrections — how they differ from standard CPI and by how much, (3) the policy stakes — Social Security COLA, income tax bracket indexing, TIPS — with estimated cumulative dollar impact of each, (4) a comparison table: CPI vs. chained CPI vs. PCE vs. GDP deflator on three dimensions (update frequency, coverage, typical divergence from CPI). Formatted as a scannable document with labeled sections.
- Prompt seed: `claude "Research CPI measurement bias. Produce a 4-section sourced brief: (1) three CPI biases (substitution, quality-improvement, new-goods) — definition, magnitude estimate, citation to primary source. (2) chained CPI and PCE as corrections — how calculated, how they differ from standard CPI in practice (verify current BLS figures). (3) policy stakes — Social Security COLA, tax bracket indexing, TIPS — estimated cumulative dollar impact if CPI overstates by 0.5pp/yr vs 1pp/yr over 10 years. (4) comparison table: CPI vs chained CPI vs PCE vs GDP deflator — update frequency, coverage, typical divergence. Verify all claims against BLS.gov and CBO sources."`
- Read / check: Verify that substitution bias, quality-improvement bias, and new-goods bias are all named with correct definitions. Confirm the PCE typically reads 0.3pp below CPI (chapter's figure). Check that Social Security COLA is correctly identified as CPI-indexed. Verify the comparison table's update frequencies are correct (BLS updates CPI monthly, PCE monthly).
- Human supplies: Verify specific dollar estimates against current CBO budget projections (these shift with policy). The bias magnitude estimates (0.5–1pp range) should be checked against the current Boskin Commission literature and any BLS methodology updates since 2020.
- Output medium: slate (formatted research brief as a structured document displayed on screen, key figures highlighted in callout boxes, comparison table as a visual grid)
- The change: Add a 2021–2024 inflation episode analysis: was the CPI's overstated-inflation-bias larger or smaller during a high-inflation period? (Answer: substitution bias is larger when relative price changes are larger — a testable prediction.)
- Teardown angle: The CPI bias is not a conspiracy — it's a known methodological limitation with a known correction (chained CPI) that was slow to adopt because the correction reduces Social Security payments. The measurement problem and the political economy problem are the same problem.
- Exclusions: Hedonic regression methodology in detail, producer price index, core vs. headline CPI distinction, international CPI comparison.
- Score: 8/10

---

## Candidate 06 — Model the Hyperinflation Mechanism with Claude Code

- Source: economics/chapters/22-inflation.md
- Lane: BUILD (Claude Code)
- Hook: Zimbabwe's 2008 hyperinflation: prices doubled daily. Hungary 1945: doubled every 15 hours. The mechanism is the same in every case — fiscal deficit → monetary financing → expectations updating → acceleration. It's a dynamic system you can simulate in 30 lines.
- The artifact: A Python hyperinflation dynamics simulator. The model: money supply grows at rate g (the "monetization rate"); price level adjusts via Fisher-like expectation updating (adaptive expectations); fiscal deficit is partially monetized at rate mu. Run for 36 months. Outputs: (1) animated time series showing money supply growth, inflation rate, and inflation expectations converging upward, (2) a phase diagram showing inflation vs. inflation expectations with the unstable equilibrium marked, (3) a policy intervention: at month 18, set fiscal deficit to zero and watch inflation expectations un-anchor slowly (the "cold turkey" vs. "gradual disinflation" comparison). Demo: calibrate to approximate 1970s U.S. episode (g=0.10) and Zimbabwe episode (g=0.50).
- Prompt seed: `claude "Simulate hyperinflation dynamics. Model: M(t) = M(t-1)*(1+g), P(t) = P(t-1)*(1 + alpha*(M(t)-M(t-1))/M(t-1) + beta*(E_pi(t-1))), E_pi(t) = lambda*pi(t) + (1-lambda)*E_pi(t-1). Parameters: g (monetization rate), alpha (price sensitivity), beta (expectations weight), lambda (expectations updating speed). Run 36 months. Plot animated time series: M_growth, actual pi, E_pi. Plot phase diagram: pi vs E_pi with 45-degree line. At month 18 set g=0. Demo: g=0.10 (moderate inflation) and g=0.50 (hyperinflation path). Show divergence."`
- Read / check: Verify the model shows price-level acceleration (not just constant inflation) at high g values. Confirm the cold-turkey intervention at month 18 stabilizes the model eventually but with a lag (inertia from adaptive expectations). Check the phase diagram shows the unstable equilibrium above the 45-degree line.
- Human supplies: Nothing — fully synthetic. The calibration parameters are stylized (not empirically estimated); note this in the video.
- Output medium: Manim (animated time series with three lines growing, phase diagram building, cold-turkey intervention marked with a vertical dashed line, stabilization path after)
- The change: Set lambda (expectations updating speed) to 0.9 (fast updating) vs. 0.1 (slow) and show how a more rational-expectations economy breaks into hyperinflation faster but also stabilizes faster when g=0 — demonstrating the credibility mechanism.
- Teardown angle: Hyperinflation is a fiscal phenomenon that becomes a monetary phenomenon through expectations. The solution requires both fiscal discipline AND credible monetary commitment — either alone is insufficient, which is why historically it required institutional change, not just policy adjustment.
- Exclusions: Full quantity theory of money derivation, Sargent's rational expectations disinflation papers, specific Venezuela/Argentina political economy.
- Score: 8/10

---

## Candidate 07 — Research the Minimum Wage Debate Evidence with Claude

- Source: economics/chapters/14-labor-markets-and-income.md
- Lane: RESEARCH (Claude assistant)
- Hook: The textbook says minimum wage causes unemployment. Card and Krueger's 1994 New Jersey study said it didn't. Both can be right — and the question of which is right in your context depends on monopsony power, which most introductory treatments skip.
- The artifact: A sourced 4-section research brief: (1) the canonical competitive model prediction (minimum wage above equilibrium → unemployment, labor demand elasticity matters), (2) the Card-Krueger New Jersey/Pennsylvania natural experiment — methodology, findings, and the Neumark-Wascher reanalysis controversy, (3) the monopsony model — when does employer market power change the minimum wage prediction? (Seattle Minimum Wage Study results), (4) current consensus: a sourced summary of what the 2024 literature says minimum wage effects are for low-wage workers, distinguishing effects by size of increase and local labor market conditions. All claims linked to verifiable primary sources.
- Prompt seed: `claude "Research the minimum wage employment effects debate. Produce a 4-section sourced brief: (1) competitive model prediction — formula for unemployment as function of labor demand elasticity and wage increase. (2) Card-Krueger 1994 — methodology (difference-in-differences NJ vs PA), findings, Neumark-Wascher reanalysis critique, current reading of the evidence. (3) monopsony model — when employer market power changes the prediction, Seattle Minimum Wage Study (U Washington) findings. (4) current 2024 consensus — what does the meta-analytic evidence say? Distinguish effect by size of wage increase. Verify all claims against peer-reviewed sources."`
- Read / check: Verify the Card-Krueger study used NJ and PA fast-food employment as the DID. Confirm the Seattle study finding (mixed results — some workers harmed by hours reduction). Check that the monopsony model is correctly described as predicting minimum wage can increase employment when there's employer market power. Verify the current consensus is not presented as settled (the literature is genuinely divided).
- Human supplies: Verify that cited paper conclusions have not been superseded by more recent meta-analyses (economics literature moves; flagging uncertain results is critical). Primary sources should be linked for human verification.
- Output medium: slate (structured research brief with claim-by-claim source tags, Card-Krueger DID design shown as a simple 2×2 table, monopsony wage-setting diagram as a visual)
- The change: Narrow the research question to: "What does the evidence say for Seattle specifically in 2015–2018?" and show how the same national framework produces a more granular local answer — demonstrating that the "right" minimum wage answer is always conditional on local labor market structure.
- Teardown angle: The debate is not about whether both models are valid — they are. The debate is about which model applies in which labor market. Employer market power (monopsony) is the key conditional: in competitive labor markets, minimum wage reduces employment; in monopsonistic labor markets, it may not.
- Exclusions: Living wage vs. minimum wage distinction, international comparison of minimum wage levels, automation effects of minimum wage.
- Score: 8/10

---

## Candidate 08 — Simulate Perfect Competition Long-Run Equilibrium with Claude Code

- Source: economics/chapters/08-perfect-competition.md
- Lane: BUILD (Claude Code)
- Hook: A wheat farmer makes $5.82 × 50,000 bushels. Her neighbor sees the profit and plants wheat too. And the next neighbor. And the one after that. Within three years, the price is back at zero economic profit — not by design, but by the mathematics of free entry.
- The artifact: A Python perfect-competition industry simulator. Model: industry with N firms each with quadratic cost function (TC = aQ² + bQ + c), identical across firms. Market demand curve (P = D_intercept - D_slope*Q_total). Simulate: (1) initial equilibrium with N=10 firms, compute P*, profit per firm, (2) entry when profit > 0 or exit when profit < 0 — add/remove one firm per period, (3) run 20 periods to long-run equilibrium (zero economic profit), (4) animate: price level per period, number of firms per period, profit per firm per period — all three on a three-panel chart. Show that zero-profit equilibrium is at minimum ATC.
- Prompt seed: `claude "Simulate perfect competition long-run equilibrium with entry/exit. N firms, each TC(Q) = a*Q^2 + b*Q + c. Market demand P = D - d*Q_total where Q_total = N*q_firm. Each firm's optimal q: where P = MC = 2a*q + b. Profit per firm = (P - ATC)*q. Each period: if profit > 0 add one firm; if profit < 0 remove one. Run 20 periods. Plot animated 3-panel: (1) market price vs period, (2) number of firms vs period, (3) profit per firm vs period. Mark long-run equilibrium when profit ≈ 0 and P = min(ATC)."`
- Read / check: Verify the long-run equilibrium price equals minimum ATC. Confirm the firm exits correctly when average total cost > price. Check that the entry/exit dynamics converge (oscillation is possible — show dampening). Verify market price decreases as firms enter.
- Human supplies: Nothing — fully synthetic. Cost function parameters are chosen to produce plausible dynamics. Mention that the model is stylized (single homogeneous good, no transportation costs, etc.).
- Output medium: Manim (three-panel animated chart with all three lines building simultaneously per period, long-run equilibrium marked with a horizontal dashed line on the price and profit panels)
- The change: Give one firm a cost advantage (lower fixed cost) and show that in long-run equilibrium, that firm makes positive economic profit while all other firms make zero — demonstrating that competitive markets equalize profit to zero only for identical firms; cost advantages persist.
- Teardown angle: The case for competitive markets is not laissez-faire — it's the case for competition, which sometimes requires institutional intervention to preserve. The long-run zero-profit result is a theorem about what markets do when entry is free; maintaining free entry is the institutional work.
- Exclusions: Factor market adjustments, comparative statics from demand shifts, industry-specific capital adjustment costs.
- Score: 7/10
