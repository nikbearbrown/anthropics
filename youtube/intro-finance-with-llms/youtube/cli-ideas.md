# Introduction to Finance: with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Capital Stack Waterfall with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-securities.md (§3.2)
- Lane: BUILD (Claude Code)
- Hook: Common stockholders "own" the company — until liquidation day, when they discover they own the residual of a waterfall that paid everyone else first. Build the waterfall and watch what's left.
- The artifact: An animated Manim waterfall chart showing liquidation proceeds flowing from secured creditors down through common shareholders, with the remaining amount after each tier labeled. The viewer sees in real time how much equity gets in a specific scenario (e.g., $80M proceeds vs $95M total claims).
- Prompt seed: `claude "Write Python (Manim) code to animate a capital stack liquidation waterfall. Tiers (in order): secured $40M, senior unsecured $30M, subordinated $15M, preferred $10M, common (residual). Liquidation raises $80M. Animate cash flowing down each tier, each tier's bar filling to its claim or to whatever remains. Color: tiers made whole = green, tiers partially paid = yellow, tiers paid zero = red."`
- Read / check: Verify the arithmetic (40+30+10=80, so subordinated gets 10/15, preferred gets 0, common gets 0); verify each bar's filled portion matches the math; verify the color coding is applied correctly at each tier.
- Human supplies: Nothing — fully synthetic. The dollar amounts are illustrative; the structure and the lesson (common gets zero in this scenario) are the point. Changing the liquidation amount to $110M for the "change" beat is also synthetic.
- Output medium: Manim (waterfall animation with cash flowing downward, tiers coloring as they fill)
- The change: Raise liquidation proceeds to $110M and re-run — show how the common stockholders suddenly go from zero to $15M, illustrating the unlimited upside of residual claims.
- Teardown angle: The waterfall makes the "residual claim" concept visceral. Common equity is not ownership of assets — it is a bet that enough value survives the queue.
- Exclusions: No bankruptcy law detail, no specific case study, no international insolvency comparison.
- Score: 9/10

---

## Candidate 02 — Value Preferred Stock Under Three Scenarios with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-securities.md (§3.4)
- Lane: BUILD (Claude Code)
- Hook: The perpetuity formula for preferred stock looks simple: P = D/r. But a 1-point change in required return moves the price by 20%. Build the sensitivity surface and see why "simple" is dangerous.
- The artifact: A 2D sensitivity plot: x-axis = required return (3% to 12%), y-axis = preferred price, for a $6 annual dividend. Three horizontal lines mark the par value ($100), the call price ($105), and zero. The region above the call price is shaded "issuer calls it" — showing where the formula overestimates value. Rendered as Manim animated line with shaded regions.
- Prompt seed: `claude "Write Python code to plot preferred stock price P = D/r for D=$6, with required return r sweeping from 0.03 to 0.12 in steps of 0.001. Plot P vs r. Add horizontal lines at P=100 (par), P=105 (call price), and P=0. Shade the region where P > 105 in red labeled 'issuer calls; formula overestimates'. Return matplotlib code."`
- Read / check: Verify P = 6/0.06 = $100 appears correctly on the plot at r=6%; verify the shaded region starts at the correct r value where 6/r > 105 (r < ~5.7%); verify axes are labeled and the formula is stated in the title.
- Human supplies: Nothing — fully synthetic. The $6 dividend and $105 call price are illustrative. No real security data needed.
- Output medium: Manim (line draws from right to left as r decreases; shaded "callable" region fades in; horizontal reference lines appear as landmarks)
- The change: Add a second curve for a callable preferred where price is capped at 105 (min(D/r, 105)) and overlay it on the original — show how the cap flattens the curve.
- Teardown angle: The formula's simplicity hides a structural assumption (perpetual, non-callable) that breaks in the most interesting cases. Every model has a domain of validity smaller than its domain of use.
- Exclusions: No duration calculation, no bond comparison, no credit risk. One security, one formula, one sensitivity surface.
- Score: 9/10

---

## Candidate 03 — Decode the Buffett-Goldman Deal with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-securities.md (§3.5)
- Lane: BUILD (Claude Code)
- Hook: Buffett put $5B into Goldman in 2008 and made ~$5-6B over five years. The math is easy; the structure that made it work is the lesson. Build the cash flow model and show what each piece contributed.
- The artifact: A stacked bar chart (Manim) showing Buffett's total return decomposed into: preferred dividends ($500M/year × ~2.5 years), redemption premium ($550M), and warrant gain (~$2B+). Each bar segment animates in with its label and dollar amount.
- Prompt seed: `claude "Write Python code to build a stacked bar chart decomposing Berkshire's Goldman Sachs investment return. Three components: (1) preferred dividends: $500M/year for 2.5 years = $1.25B, (2) redemption premium: $5.64B - $5B = $640M, (3) warrant gain: ~$2B (illustrative). Stack these in a single horizontal bar. Label each segment with name and amount. Total = ~$3.9B illustrative. Return matplotlib code."`
- Read / check: Verify the three segments sum to ~$3.9B and the bar represents that correctly; verify each segment is labeled; verify the illustrative nature of the warrant gain is noted in the title or caption.
- Human supplies: The exact warrant gain figures are contested/approximate. The video should label the warrant segment "~$2B (illustrative)" and note the actual figure varies by source. A screen-recording of the Goldman press releases being read would add authenticity but is not required.
- Output medium: Manim (stacked bar builds left to right, each segment sliding in with label and amount; total appears at the right edge)
- The change: Add a counterfactual bar: "if Buffett had bought common stock at $125/share in Sept 2008" — show the common stock value at Goldman's 2013 price (~$160) for the same $5B investment. Compare the two bars side by side.
- Teardown angle: The preferred + warrants structure wasn't cleverness — it was the only structure that satisfied both parties' constraints simultaneously. Preferred solved Goldman's capital problem; warrants solved Buffett's upside problem. Neither instrument alone would have worked.
- Exclusions: No Goldman's full financial history, no 2008 crisis timeline, no Basel capital rules detail.
- Score: 8/10

---

## Candidate 04 — Compute Dual-Class Voting Power vs. Economic Exposure with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-securities.md (§3.3)
- Lane: BUILD (Claude Code)
- Hook: Mark Zuckerberg owns ~13% of Meta's economic value and controls ~61% of its votes. Build the math for any dual-class company and see how the multiplier works.
- The artifact: A Python calculator that takes (Class A shares, Class A votes, Class B shares, Class B votes, founder B-share percentage) and outputs a 2-panel chart: left panel = economic exposure pie (founder vs. public), right panel = voting power pie (founder vs. public). Rendered as Manim with two pies animating in side by side, labeled with percentages.
- Prompt seed: `claude "Write Python code for a dual-class voting power calculator. Inputs: class_a_shares=800M, class_a_votes_per_share=1, class_b_shares=200M, class_b_votes_per_share=10, founder_b_fraction=1.0. Compute: founder economic % = class_b_shares / total_shares; founder voting % = (founder_b_fraction * class_b_shares * class_b_votes_per_share) / total_votes. Plot two pie charts side by side: economic split and voting split. Return matplotlib code."`
- Read / check: Verify founder economic = 200/(800+200) = 20%; verify founder voting = (200×10)/(800×1+200×10) = 2000/2800 = 71.4%; verify both pies sum to 100% and the gap is visually obvious.
- Human supplies: Nothing — fully synthetic. The 800M/200M split is hypothetical. The video can note that Meta's actual numbers differ but follow the same structure.
- Output medium: Manim (two pies animate in; a bracket between them highlights the gap between 20% economic and 71% votes with a label "control leverage")
- The change: Sweep the Class B vote multiplier from 2× to 20× and animate how founder voting power grows. Show the point at which a 20% economic stake gives majority control.
- Teardown angle: The vote multiplier is not financial engineering — it is a governance philosophy baked into the capital structure. The question is not whether it is legal; it is whether the founder whose conviction you are buying is actually worth the control premium.
- Exclusions: No SEC dual-class debate, no index-inclusion controversy, no corporate governance theory beyond the one required concept.
- Score: 8/10

---

## Candidate 05 — Build the Three-Model Valuation Disagreement Display with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-valuation.md (§4.5)
- Hook: Three valuation methods — DDM, DCF, multiples — produce three different prices for the same stock. The disagreement is the most useful output. Build all three for one company and read the gap.
- Lane: BUILD (Claude Code)
- The artifact: A three-bar chart (Manim) showing DDM-implied price, DCF-implied price, and relative-valuation-implied price for a single hypothetical company, with the current market price overlaid as a horizontal dashed line. The gap between each bar and the market price is labeled as the "implied mispricing under each theory."
- Prompt seed: `claude "Write Python code to plot three equity valuations for a hypothetical company. DDM (Gordon Growth): D1=2, r=0.09, g=0.06 → P=D1/(r-g). DCF: fcf=[240,288,345,397,437], wacc=0.09, terminal_g=0.03, net_debt=400, shares=100 (use perpetuity terminal value). Relative: median_pe=20, eps=3.50 → P=median_pe*eps. Market price = 500. Plot three bars plus a horizontal line at 500. Label each bar with its implied price and the gap to 500. Return matplotlib code."`
- Read / check: Verify DDM = 2/(0.09-0.06) = $66.67; verify DCF runs the perpetuity-growth terminal value and gives ~$57.70; verify relative = 20×3.50 = $70; verify market line at $500 is labeled; verify gap labels are correct.
- Human supplies: Nothing — fully synthetic. The numbers are deliberately illustrative to make the DDM/relative undervalue and the market price far higher, forcing the viewer to read the gap as a theory question.
- Output medium: Manim (three bars animate up; market price line slides in; gap brackets appear with labels)
- The change: Change the DDM growth rate from 6% to 7% and show how sensitive the DDM bar is — it jumps from $67 to $100. Reframe: small assumption changes, large price moves.
- Teardown angle: The three bars don't average to the right answer. They are three different theories of what determines value. The disagreement names which assumption the market and the analyst do not share.
- Exclusions: No full DCF walkthrough (covered in Candidate 06), no CAPM derivation, no options pricing.
- Score: 9/10

---

## Candidate 06 — Simulate DCF Terminal Value Dominance with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-valuation.md (§4.3)
- Hook: In a 5-year DCF, the terminal value typically represents 60–85% of enterprise value. That means you're not really valuing the forecast — you're valuing one assumption. Build the model and watch where the weight falls.
- Lane: BUILD (Claude Code)
- The artifact: A stacked bar chart showing DCF enterprise value decomposed into: PV of explicit forecast years 1–5 vs. PV of terminal value, with the terminal value percentage labeled. A second chart shows how the terminal value share changes as terminal growth rate varies from 1% to 5%. Rendered as Manim with the bar appearing first, then the sensitivity curve animating.
- Prompt seed: `claude "Write Python code to compute a DCF. fcf_forecast=[240,288,345,397,437], wacc=0.09, terminal_growth=0.03, net_debt=400, shares=100. Compute (a) PV of explicit period, (b) PV of terminal value, (c) EV = (a)+(b), (d) terminal_pct = (b)/EV. Plot a stacked bar: explicit PV in blue, terminal PV in orange. Add terminal_pct as a text label. Then sweep terminal_growth from 0.01 to 0.05, plot terminal_pct vs terminal_growth as a line chart. Return matplotlib code."`
- Read / check: Verify terminal value PV ≈ $4,876M and explicit period PV ≈ $1,294M (total ~$6,170M); verify terminal_pct ≈ 79%; verify the sweep chart shows terminal_pct rising as g increases; verify EV and equity per share are computed correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (stacked bar appears, percentage label pops in; then sweep chart animates from left to right as g increases)
- The change: Change terminal_growth to 0.08 (near WACC) and show the terminal value explode toward infinity — then add the error-check that raises ValueError when g >= wacc.
- Teardown angle: When terminal value exceeds 85% of EV, the DCF is not valuing a business — it is valuing an assumption about what the business looks like in perpetuity. That assumption deserves more scrutiny than the forecast it dwarfs.
- Exclusions: No WACC derivation, no beta calculation, no multi-stage DCF. One model, one decomposition, one sensitivity.
- Score: 9/10

---

## Candidate 07 — Build the Gordon Growth Sensitivity Surface with Claude Code
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-valuation.md (§4.2)
- Hook: The Gordon Growth Model says P = D1/(r-g). When r and g are close, a 1-point change in either moves the price by 30–50%. Build the 2D sensitivity surface and see the cliff.
- Lane: BUILD (Claude Code)
- The artifact: A 3D surface plot (matplotlib) with r on one axis (5%–12%), g on another (2%–8%), and P = D1/(r-g) on the vertical axis, for D1=$2. The surface includes a shaded "undefined" region where g >= r. Rendered as a Manim-animated rotation of the 3D surface, then a 2D slice at a specific r.
- Prompt seed: `claude "Write Python code to plot a 3D surface: P = D1/(r-g) for D1=2, r sweeping 0.05 to 0.12, g sweeping 0.02 to 0.08. Mask (set to NaN) all points where g >= r. Use matplotlib mpl_toolkits.mplot3d. Color the surface by P value (viridis). Label axes r, g, P. Title: 'Gordon Growth Sensitivity Surface'. Return code."`
- Read / check: Verify the NaN masking correctly excludes g>=r regions; verify P at r=0.08, g=0.05 equals 2/0.03 = $66.67; verify the color scale shows the explosion toward infinity near the constraint boundary.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (3D surface rotates to show the cliff near g=r; then camera pulls back to show a 2D slice at r=9% as a line chart)
- The change: Add a second surface for D1=$4 (a different stock) on the same axes — show how the sensitivity structure is identical, just scaled up. Both stocks have the same danger zone near g=r.
- Teardown angle: The surface makes visible what the formula hides in plain sight: the model is hypersensitive near its own constraint. The region where Gordon Growth is most commonly misused is exactly where the math is most fragile.
- Exclusions: No dividend growth history, no sector comparison, no analyst report critique.
- Score: 8/10

---

## Candidate 08 — Research the Coca-Cola "Moat" Thesis: Was Buffett Right and Why?
- Source: intro-finance-with-llms/chapters/2026-04-21-equity-valuation.md (§4.1 + §4.5)
- Lane: RESEARCH (Claude assistant)
- Hook: In 1988, Buffett bought Coke at 15× earnings when Wall Street called it overpriced. His thesis was a "durable economic moat" — a higher long-run growth rate g. Research what actually happened to Coke's growth rate from 1988 to 2010 and whether the data vindicated the thesis.
- The artifact: A sourced 3-decade earnings-growth summary: EPS growth by decade (1988–1998, 1998–2008, 2008–2018), with commentary on whether each decade supported or challenged the moat thesis, plus one counterargument Buffett's critics could have made using available 1988 data. Rendered as a Manim animated timeline with data points and annotations.
- Prompt seed: `claude "Research Coca-Cola's EPS growth by decade: 1988-1998, 1998-2008, 2008-2018. Provide approximate CAGR for each decade (cite sources or note they are approximations). Then: using only data available in 1988, what was the strongest argument a skeptic could have made against Buffett's 'durable moat' thesis? Cite at least one real 1988-era concern about Coca-Cola."`
- Read / check: Verify the EPS CAGRs are approximately consistent with known Coca-Cola financials (1988–1998 was strong; 1998–2008 weaker due to the 1999 earnings reset); verify the 1988 skeptic argument is historically plausible (e.g., New Coke failure, market saturation concerns).
- Human supplies: Actual Coca-Cola annual report data for 1988–2018 would make the EPS chart authentic. Without it, the chart must be labeled "approximate / illustrative" and sourced to Claude's training knowledge. A real data pull from SEC EDGAR would be authentic.
- Output medium: Manim (timeline with decade bars animating in, EPS CAGR labels appearing, annotation bubbles for key events)
- The change: Build the Gordon Growth price that a 1988 analyst using consensus g would have estimated, vs. Buffett's implied g, and show the price difference — making the disagreement numerical.
- Teardown angle: The data vindicated Buffett's thesis for ~15 years, then partially challenged it. The lesson is not "Buffett was right" — it is "his theory was specific enough to be falsified, and it survived the first test."
- Exclusions: No full Berkshire portfolio analysis, no diet Coke/New Coke history, no 1990s emerging-markets expansion detail.
- Score: 8/10
