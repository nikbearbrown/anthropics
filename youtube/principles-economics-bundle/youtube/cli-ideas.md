# Principles of Economics Bundle — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Build the Demand-Supply Model with Claude: Four-Step Analysis Animated"
- Source: principles-economics-bundle/chapters/03-demand-and-supply.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The demand-supply model predicts the direction AND magnitude of price changes from any market shock — in four steps. Claude codes the model, shocks it, and animates the curve shifts so the mechanism is visible, not just stated.
- The artifact: An animated PQ diagram showing supply and demand curves for a gasoline market. Step 1: equilibrium at P₀, Q₀. Step 2: a crude oil price increase shifts supply left. Step 3: the new supply curve appears. Step 4: new equilibrium at higher P, lower Q is highlighted. A panel shows the numerical shift in equilibrium computed from linear supply and demand equations. A second scenario: demand shifts right (income increases) — same four-step treatment.
- Prompt seed: `claude "Write Python that models a demand-supply market. Demand: Q_d = 200 - 5*P. Supply: Q_s = 3*P - 40. Compute equilibrium (Q_d=Q_s): P*=30, Q*=50. Then simulate a supply shock: Q_s_new = 3*P - 70 (supply shifts left by 30 units at every price). Find new equilibrium. Plot both demand curves and both supply curves, mark old and new equilibrium. Print equilibrium P and Q before and after the shock. Also compute consumer surplus = 0.5*(P_max - P*)*Q*."`
- Read / check: Code: verify initial equilibrium P=30, Q=50 from Q_d=Q_s; verify after supply shift new P>30 and Q<50 (correct direction); verify consumer surplus formula as triangle area. Output: the four curves should be color-coded; the equilibrium shift should be clearly visible with labeled coordinates.
- Human supplies: Nothing — fully synthetic (linear supply and demand equations are illustrative parameters).
- Output medium: Manim — animate: first the equilibrium point, then animate the supply curve shifting left, then animate the new equilibrium point appearing; label the price and quantity changes.
- The change: Add a simultaneous demand increase (income rises, luxury good) and show how the combined shock produces ambiguous quantity effects (P definitely rises, Q direction depends on magnitudes) — demonstrating why you need both curves to predict both variables.
- Teardown angle: The four-step method forces you to identify which curve shifts and why before computing anything. Students who skip step 2 (is it demand or supply?) get the wrong answer every time. The animation makes each step a distinct visual act.
- Exclusions: Non-linear supply/demand curves; markets with externalities; general equilibrium (multiple markets).
- Score: 9/10

## Candidate 02 — "Compute Price Elasticity with Claude: Revenue Impact Visualized"
- Source: principles-economics-bundle/chapters/05-elasticity.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Netflix raised prices 60% in 2011 and lost fewer subscribers than predicted. The explanation is price elasticity: when demand is inelastic, revenue rises after a price hike. Claude computes elasticity for five goods and shows the revenue-elasticity relationship on one plot.
- The artifact: A two-panel figure. Left: demand curves for 5 goods (insulin, Netflix 2011, gasoline, restaurant meals, luxury handbags) with different slopes — steep = inelastic, flat = elastic. Right: a bar chart of "total revenue after 10% price increase" for each good — inelastic goods show revenue increase, elastic goods show revenue decrease. Elasticity values labeled on each bar.
- Prompt seed: `claude "Write Python that computes price elasticity of demand for 5 goods and shows the revenue effect of a 10% price increase. Goods and elasticities: insulin (e=0.1), Netflix-2011 (e=0.4), gasoline (e=0.5), restaurant-meals (e=1.5), luxury-handbags (e=2.2). For each: (1) compute new quantity after 10% price increase using e = -(dQ/Q)/(dP/P), (2) compute old and new total revenue (TR=P*Q), (3) classify: elastic/inelastic. Plot demand curves (normalize P0=100, Q0=100) and a bar chart of delta_TR."`
- Read / check: Code: verify for insulin: new Q = 100 × (1-0.1×0.1) = 99, new TR = 110 × 99 = 10890 > 10000 (revenue up); verify for luxury handbags: new Q = 100 × (1-2.2×0.1) = 78, new TR = 110 × 78 = 8580 < 10000 (revenue down). Output: all 5 goods should be correctly classified as elastic or inelastic; the bar chart sign (positive/negative) should match the classification.
- Human supplies: Nothing — fully synthetic (elasticity estimates are standard textbook values; human may wish to verify with a peer-reviewed source for authenticity).
- Output medium: Manim — animate the five demand curves appearing with different slopes labeled; then animate the revenue bar chart with bars growing positive (inelastic) or negative (elastic).
- The change: Show the "unit elastic" special case (elasticity = 1, Netflix 2012 after competitors arrived) where revenue is unchanged by a price hike — and explain why this is the revenue-maximizing price point.
- Teardown angle: Elasticity is a number that summarizes how much "exit power" buyers have. Low elasticity = captive customers = pricing power. High elasticity = competitive market = price-taker. Every pricing decision a business makes is implicitly an elasticity bet.
- Exclusions: Income elasticity derivation; cross-price elasticity; supply elasticity tax incidence full derivation.
- Score: 9/10

## Candidate 03 — "Model Firm Costs with Claude: Build the Seven Short-Run Cost Curves"
- Source: principles-economics-bundle/chapters/07-production-costs-and-industry-structure.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Every firm's supply decision comes down to one question: is price above marginal cost? But marginal cost depends on the production function — and a 40-line script builds all seven cost curves from a production function, making the supply curve's source visible.
- The artifact: A 2×2 panel figure. Panel 1: production function Q(L) with diminishing marginal product. Panel 2: total cost (TC), total fixed cost (TFC), total variable cost (TVC) vs. Q. Panel 3: marginal cost (MC), average total cost (ATC), average variable cost (AVC), average fixed cost (AFC) vs. Q. Panel 4: highlights that MC intersects ATC at its minimum — the "efficient scale" point.
- Prompt seed: `claude "Write Python that builds all 7 short-run cost curves from a production function. Production: Q = 10*L^0.7 (diminishing marginal product). Labor cost w=100/unit, fixed cost TFC=500. For L from 0.1 to 20, compute: Q, TVC=w*L, TC=TFC+TVC, MC=dTC/dQ (numerical differentiation), ATC=TC/Q, AVC=TVC/Q, AFC=TFC/Q. Plot 4-panel figure. Verify MC intersects ATC at ATC minimum. Print the efficient scale (minimum ATC point)."`
- Read / check: Code: verify diminishing marginal product (dQ/dL decreasing as L increases); verify AFC is hyperbolic (always falling); verify MC crosses ATC at ATC's minimum (use numpy to find the index). Output: the four panels should be clearly labeled; the MC-ATC intersection should be annotated.
- Human supplies: Nothing — fully synthetic (Cobb-Douglas production function with standard parameters).
- Output medium: Manim — animate each cost curve appearing in sequence, building from the production function; highlight the MC-ATC intersection as it appears.
- The change: Change the production function exponent from 0.7 (diminishing returns) to 1.2 (increasing returns) and show how the cost curves change shape — especially that MC now falls as Q increases, producing a natural monopoly cost structure.
- Teardown angle: The MC-ATC intersection rule is the key: ATC is falling when MC < ATC, rising when MC > ATC. This is just mathematics (when a marginal value is below the average, the average falls) — but it explains why firms produce at different scales.
- Exclusions: Long-run average cost curve; economies of scale measurement; multiproduct cost functions.
- Score: 9/10

## Candidate 04 — "Compute Gini Coefficient with Claude: Lorenz Curve from Income Data"
- Source: principles-economics-bundle/chapters/15-poverty-and-economic-inequality.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The Gini coefficient is a single number between 0 and 1 that summarizes income inequality for an entire country. Claude computes it from first principles — the Lorenz curve and the area formula — then compares it across countries.
- The artifact: A Lorenz curve plot showing cumulative income share vs. cumulative population share for three countries (US Gini≈0.40, Sweden Gini≈0.27, Brazil Gini≈0.53). The 45° "perfect equality" line is shown as a benchmark. The Gini coefficient is computed as twice the area between the Lorenz curve and the 45° line. A bar chart compares the three Gini values.
- Prompt seed: `claude "Write Python that computes the Gini coefficient and Lorenz curve for three countries using quintile income share data. US quintiles (% of income): [3, 9, 15, 23, 50]. Sweden: [9, 14, 18, 23, 36]. Brazil: [2, 5, 10, 19, 64]. For each: compute cumulative population shares [20,40,60,80,100] and cumulative income shares. Compute Gini = 1 - 2*(area under Lorenz curve) using the trapezoidal rule. Plot all three Lorenz curves + 45-degree line. Print Gini values."`
- Read / check: Code: verify US Lorenz curve passes through approximately (60%, 27%) for the bottom 3 quintiles' income; verify Gini formula: Gini = 1 - sum(L_i+1 + L_i)*(P_i+1-P_i) using trapezoid rule; verify US Gini ≈ 0.38–0.42. Output: all three Lorenz curves should be visibly different; Brazil's should be furthest from the 45° line.
- Human supplies: Quintile income share data from World Bank or OECD — the human should verify the current year's data rather than using textbook approximations. The quintile data provided in the prompt is illustrative; real data is preferred.
- Output medium: Manim — animate the three Lorenz curves being drawn simultaneously; animate the area between each curve and the 45° line being shaded; reveal the Gini values as numbers growing from 0.
- The change: Compute Gini for pre-tax vs. post-tax income in the US (pre-tax Gini≈0.52, post-tax≈0.40 after transfers) — showing the redistributive effect of the tax and transfer system.
- Teardown angle: The Gini coefficient hides a lot — two countries with the same Gini can have very different income distributions at the top and bottom. The Lorenz curve shows the full shape; the Gini is a convenient scalar summary that loses information.
- Exclusions: Atkinson index; wealth inequality vs. income inequality; measurement methodology (survey vs. tax records).
- Score: 8/10

## Candidate 05 — "Model Economic Growth with Claude: Compound Rates and the Rule of 70"
- Source: principles-economics-bundle/chapters/20-economic-growth.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A 2% annual growth rate doubles GDP in 35 years. A 4% rate doubles it in 18 years. The compounding difference between rich and poor countries is almost entirely explained by persistent 1–2% growth rate differences. Claude plots the divergence.
- The artifact: A log-scale GDP per capita chart from year 0 to 50, showing 6 growth trajectories: 1%, 2%, 3%, 5%, 7%, 10% annual growth — all starting at $5,000. The doubling times are annotated on each line (Rule of 70: 70/r ≈ doubling years). A second panel shows the ratio of 7%-to-2% GDP after 50 years: more than 10× gap from just a 5 percentage point growth rate difference.
- Prompt seed: `claude "Write Python that plots GDP growth trajectories for 6 annual growth rates (1%, 2%, 3%, 5%, 7%, 10%) over 50 years. Initial GDP=5000. GDP(t) = 5000 * (1+r)^t. Plot all 6 on a log-scale y-axis. Annotate each line with the Rule of 70 doubling time (70/r years). Plot a second panel showing the ratio GDP(7%)/GDP(2%) vs year — compute the gap at year 50. Print all doubling times."`
- Read / check: Code: verify Rule of 70 approximation: doubling time at 2% ≈ 35 years; verify exact doubling: (1.02)^35 ≈ 2.0; verify ratio at year 50: (1.07/1.02)^50 ≈ 11.5×. Output: on the log scale, all trajectories should be straight lines (confirming exponential growth); the 10% line should be dramatically above the 1% line.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate all 6 trajectories being drawn simultaneously from left to right; annotate each doubling event with a small marker; reveal the ratio panel after all trajectories are drawn.
- The change: Overlay the actual GDP per capita growth of South Korea (1960-2010, ~7%/yr), US (1960-2010, ~2%/yr), and sub-Saharan Africa (1960-2010, ~1%/yr) on the trajectory chart — showing the model fits historical data.
- Teardown angle: The difference between a country that grows at 2% vs. 4% is invisible in a single year but constitutes a factor-of-4 difference in living standards after 70 years. Compounding is the most underestimated force in economics.
- Exclusions: Growth accounting decomposition; total factor productivity measurement; endogenous growth theory.
- Score: 8/10

## Candidate 06 — "Simulate the Money Multiplier with Claude: How Banks Create Money"
- Source: principles-economics-bundle/chapters/27-money-and-banking.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: When the central bank creates $5,000 in new reserves, the banking system multiplies it into $100,000 in deposits — through a chain of lending and depositing. Claude traces all 10+ rounds of the multiplier, computing how much money each bank creates.
- The artifact: A bar chart showing the deposit expansion process: Round 1: Bank A receives $5,000, keeps $250 reserves (5%), lends $4,750. Round 2: Bank B receives $4,750, keeps $237.50, lends $4,512.50. ... Round 10+: the bars shrink geometrically. Total deposits created = $5,000 × (1/0.05) = $100,000. A running total panel shows deposits accumulating.
- Prompt seed: `claude "Write Python that simulates the money multiplier process. Initial reserves injected = 5000. Reserve requirement = 5%. Simulate 20 rounds: each bank keeps 5% of received deposit as reserves, lends the rest. Compute cumulative deposits created at each round. Plot the deposit amount per round as a bar chart (geometric decline). Add a horizontal line at the theoretical limit M = initial / reserve_ratio = 100000. Print when the cumulative total reaches 95% of the theoretical limit."`
- Read / check: Code: verify Round 1 lending = $4,750; verify Round 2 lending = $4,512.50; verify total after 20 rounds ≈ 99.4% of $100,000; verify theoretical multiplier = 1/0.05 = 20×. Output: the bars should show a clear geometric decline; the cumulative total should asymptote to $100,000.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the bars appearing one by one across a banking chain (Bank A → Bank B → Bank C...) with a running total counter; the theoretical limit line appears when the total reaches 50% of maximum.
- The change: Reduce reserve requirement to 2% (current US near-zero reserve requirement) and show the multiplier increases to 50× — then explain why actual money multiplication in the post-2008 era is much lower (excess reserves, cash holdings).
- Teardown angle: The money multiplier is the theoretical maximum — it assumes no excess reserves and no cash held outside banks. The real-world multiplier has collapsed since 2008 because banks hold vast excess reserves. The model reveals what banks actually do, not just what they theoretically could.
- Exclusions: Federal Reserve balance sheet mechanics; quantitative easing; cryptocurrency and money supply.
- Score: 8/10

## Candidate 07 — "Build an AD-AS Model with Claude: Simulate a Demand Shock"
- Source: principles-economics-bundle/chapters/24-the-aggregate-demand-aggregate-supply-model.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The AD-AS model predicts whether a stimulus causes inflation, growth, or both — depending on which "zone" of the aggregate supply curve the economy is in. Claude builds all three zones and shocks the model.
- The artifact: A Price Level vs. Real GDP diagram with three SRAS zones: horizontal (high unemployment, Keynesian zone), upward-sloping (intermediate), vertical (LRAS/potential output). A demand stimulus shifts AD right. In the Keynesian zone, output rises, prices flat. In the intermediate zone, both rise. At LRAS, only prices rise (pure inflation). Three side-by-side panels show the same AD shift in each zone.
- Prompt seed: `claude "Write Python that draws an AD-AS model with three SRAS zones. Zone 1 (Keynesian): P=100 for Q from 0 to 800. Zone 2 (Intermediate): P = 100 + 0.05*(Q-800) for Q from 800 to 1200. Zone 3 (Classical): Q=1200 vertical LRAS. AD curve: P = 200 - 0.1*Q. Compute equilibrium. Then shift AD right by 10%: new P_AD = 220 - 0.1*Q. Show new equilibrium for each zone. Plot in 3 subplots. Print change in P and Q for each zone."`
- Read / check: Code: verify Keynesian zone equilibrium: P=100, Q=1000 before shift; verify after AD shift in Keynesian zone: Q increases (stimulus works), P unchanged; verify at LRAS: Q unchanged (Q=1200), P increases only (pure inflation). Output: all three subplots should show the same AD shift with visibly different equilibrium outcomes.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the AD shift in all three panels simultaneously, with the new equilibrium point appearing and delta-P and delta-Q labels appearing for each zone.
- The change: Simulate a negative supply shock (SRAS shifts left — an oil price spike) in the intermediate zone and show stagflation: P rises AND Q falls — the worst of both worlds.
- Teardown angle: The three-zone model is a simplification that captures one crucial policy insight: a demand stimulus at full employment is inflationary, not stimulative. The 2021-2022 US inflation episode is the textbook intermediate-to-classical zone transition.
- Exclusions: Endogenous wage adjustment and LRAS dynamics; specific monetary policy rules; Phillips curve connection.
- Score: 8/10

## Candidate 08 — "Research Free Trade Winners and Losers with Claude: Stolper-Samuelson in Practice"
- Source: principles-economics-bundle/chapters/33-international-trade.md (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: Comparative advantage proves trade makes both countries richer in aggregate. But Stolper-Samuelson theorem predicts who within each country wins and loses — and the losers are often politically powerful enough to stop the gains.
- The artifact: A structured 3-case analysis document: (1) US-China trade 2001-2015: winners (US consumers, Chinese export workers, US capital owners), losers (US manufacturing Rust Belt — cite Autor-Dorn-Hanson 2013 study with specific job-loss numbers); (2) NAFTA 1994-2019: winners (Mexican export maquiladoras, US consumers, US capital), losers (US auto workers, Mexican subsistence farmers — cite specific studies); (3) Vietnam joining WTO 2007: winners and losers by factor intensity. Each case has a one-paragraph policy implication.
- Prompt seed: `claude "Research distributional effects of international trade using Stolper-Samuelson theory. For each of three trade liberalizations — US-China trade 2001-2015, NAFTA 1994-2019, Vietnam WTO accession 2007 — identify: (1) the factor-abundant/scarce factors in each country, (2) which groups win (abundant factor) and lose (scarce factor), (3) cite one specific economic study with numbers (job losses, wage changes, consumer savings). Produce a structured 3-case analysis with policy implications for trade adjustment."`
- Read / check: Research prompts: verify the model cites Autor, Dorn, and Hanson (2013) American Economic Review paper with specific "China shock" job-loss numbers (~2 million manufacturing jobs); verify NAFTA employment effects from at least one academic study; verify Stolper-Samuelson theorem stated correctly (factor abundant in each country gains from trade). Synthesis: each case should have winners AND losers, not just aggregate gains.
- Human supplies: Nothing — RESEARCH lane. Human should verify citation accuracy against original papers if publishing.
- Output medium: Manim — animate a "who wins / who loses" split bar chart for each trade agreement, with bars growing to show magnitude of effect and geographic annotation.
- The change: Research whether trade adjustment assistance programs (TAA) have compensated the losers at the scale the Stolper-Samuelson analysis suggests they should be funded — and whether the political economy of trade adjustment explains why TAA is underfunded.
- Teardown angle: Comparative advantage is true and incomplete. It proves aggregate gains but predicts concentrated losses — in the same industries, in the same ZIP codes, to the same workers. The gap between macro-efficiency and micro-distribution is where trade politics lives.
- Exclusions: Full Heckscher-Ohlin model derivation; currency manipulation; intra-industry trade dynamics.
- Score: 8/10

## Candidate 09 — "Compute Consumer Surplus with Claude: Who Benefits Most from Price Drops?"
- Source: principles-economics-bundle/chapters/03-demand-and-supply.md
- Lane: BUILD (Claude Code)
- Hook: Consumer surplus is the gap between what people would have paid and what they actually paid — and it's a triangle on the demand curve. When prices fall (due to technology, competition, or trade), consumer surplus expands — and Claude calculates exactly who captures the gain.
- The artifact: A supply-demand diagram for a market (e.g., smartphones) before and after a cost reduction shifts supply right. The initial consumer surplus (upper triangle) and the additional consumer surplus from the price drop (lower trapezoid) are shaded separately and labeled with dollar values. A calculation shows: ΔCS = Q₀ × ΔP + ½ × ΔQ × ΔP (the trapezoid formula).
- Prompt seed: `claude "Write Python that computes consumer surplus before and after a supply shift. Demand: P = 500 - 0.5*Q. Initial supply: P = 50 + 0.5*Q. Compute initial equilibrium and consumer surplus CS1 = 0.5*(P_max - P1)*Q1. After supply shift: new supply P = 20 + 0.5*Q. Compute new equilibrium and CS2. Compute delta_CS = CS2 - CS1. Plot the demand curve, both supply curves, shade the original CS and the gain in CS. Print all values."`
- Read / check: Code: verify initial equilibrium: P₁=275, Q₁=450; verify CS₁ = 0.5×(500-275)×450 = $50,625; verify new equilibrium after supply shift; verify ΔCS > 0 (consumers benefit from supply increase). Output: the two shaded regions should be clearly distinct colors; dollar values labeled on each.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — animate the supply shift, then animate the CS regions being shaded with dollar amounts appearing; animate the "gain" trapezoid filling in after the shift.
- The change: Add a price floor set above the equilibrium (minimum wage analogy) and show how it creates deadweight loss — reducing total surplus by the triangle of unrealized trades.
- Teardown angle: Consumer surplus is invisible to the firm — customers capture the value silently. The real puzzle is why competitive markets produce so much surplus that no one captures, and how monopoly changes the split.
- Exclusions: Producer surplus derivation; deadweight loss from taxation; total surplus maximization proof.
- Score: 7/10

## Candidate 10 — "Research Behavioral Economics with Claude: When Humans Aren't Rational"
- Source: principles-economics-bundle/chapters/06-consumer-choices.md (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: Standard microeconomics assumes rational utility maximizers. Behavioral economics documents the systematic ways real humans deviate — and the deviations are predictable enough to exploit and to design around.
- The artifact: A sourced research brief: "Top 5 Behavioral Economics Findings That Survive Replication." Five biases with one real-world application each: (1) Loss aversion (Kahneman-Tversky 1979 — people weight losses 2× more than gains) → retirement saving defaults; (2) Present bias (hyperbolic discounting) → gym membership overpurchase; (3) Anchoring (Ariely 2008) → price decoy effects; (4) Endowment effect (Thaler) → WTP/WTA gap; (5) Choice overload (Iyengar-Lepper 2000 — jam study) → default-setting policy. Each finding cited with the key study and magnitude estimate.
- Prompt seed: `claude "Research the 5 most replicated findings in behavioral economics, each with a specific study citation, the estimated effect size, and one real-world policy or business application. Focus on: (1) loss aversion (Kahneman-Tversky), (2) present bias/hyperbolic discounting, (3) anchoring effects (Ariely or Tversky-Kahneman), (4) endowment effect (Thaler), (5) choice overload (Iyengar-Lepper). For each: state the finding, cite the study, give the approximate effect size, and name one policy implication. Produce a structured 5-row table."`
- Read / check: Research prompts: verify Kahneman-Tversky 1979 Prospect Theory cited; verify Thaler and Sunstein "Nudge" cited for policy applications; verify at least one finding's replication status noted (some behavioral economics findings have failed to replicate in recent years — the brief should acknowledge this). Synthesis: the brief should distinguish "well-replicated" from "mixed replication" findings.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate a 5-row table building with each bias; for each, show a simple diagram of the bias (e.g., the kinked loss-aversion value function for loss aversion).
- The change: Research which behavioral economics findings have failed to replicate in the "replication crisis" (2010-2020) — and what this means for behavioral nudge policy design.
- Teardown angle: Behavioral economics doesn't replace rational choice theory — it identifies the predictable failures. The policy value is in designing choice environments (defaults, frames, anchor points) that make it easier for people to choose what they actually want.
- Exclusions: Full prospect theory formalism; neuroeconomics; specific nudge policy evaluations.
- Score: 7/10
