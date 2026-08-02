# Principles of Finance with LLMs — Simulation Ideas

MANIM-lane candidates only. Score ≥ 6 required. All cards are directed, scripted, cinematic animations of known equations.

---

## Candidate 01 — Bond Price vs. Yield: Convexity Drawing as Rate Sweeps

- Source: `principles-finance-with-llms/chapters/10-bonds-and-bond-valuation.md`
- Topic: BONDS · PRICE-YIELD RELATIONSHIP · CONVEXITY
- Lane: MANIM (directed animation)
- Hook: When rates rise, bond prices fall — but not in a straight line. The price curve bends toward you (convexity), meaning bonds fall slower at high yields than they rise at low yields. Watching that curve draw itself is the moment you stop thinking bonds are "safe."
- The rule: P = C × [1 − (1+y)^{−n}] / y + F / (1+y)^n; price computed as y sweeps from 1% to 12% for a fixed-coupon, fixed-maturity bond
- Concrete numbers: 3M-style bond: F=$1,000, coupon=2.25% annual, n=20 years; y sweeps from 1% to 12%. Reference points: at y=2.25% price=par=$1,000; at y=1.24% price≈$1,051 (the chapter's opening example); at y=5% price≈$774; at y=8% price≈$601
- The artifact / what moves: A curve draws itself left-to-right as yield sweeps from 1% to 12%. The curve starts steeply descending from the left (high price at low rates) and flattens progressively toward the right — the convexity visible as the curve bends away from a straight line. A straight-line "duration approximation" (tangent line at y=2.25%) draws simultaneously; the gap between the line and the curve widens at high and low yields, showing where the linear approximation fails. A vertical marker drops at y=2.25% labeling P=par. Then a second marker at y=5% shows P≈$774 with a dotted line to the actual curve vs. the linear approximation.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At y=2.25% (coupon rate = YTM), P = $1,000 exactly (par bond) — this follows from the formula analytically; P2: A 1 percentage-point rise from y=2.25% to y=3.25% produces a larger absolute price drop than a 1 percentage-point rise from y=5.25% to y=6.25% — convexity means price sensitivity declines as yields rise. At y=2.25%→3.25%: ΔP ≈ −$144; at y=5.25%→6.25%: ΔP ≈ −$93 (for 20-year 2.25% coupon bond)
- The change: After the 20-year bond curve, animate a 5-year bond curve on the same axes — it is flatter (less interest-rate sensitive), demonstrating that duration (maturity) controls the steepness of the price-yield curve
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The chapter opens with the 3M bond trading at $1,051 when rates fell — the premium is not a gift, it is the exact mathematical consequence of convexity. Most investors who "bought a safe bond" don't know they own a curve, not a line.
- Exclusions: Do not add duration/modified-duration computation panels (keep focus on price-yield curve); do not simulate credit risk or yield spread dynamics; do not show the yield curve (separate concept)
- Sim slug: bond-price-yield-convexity-curve
- Score: 10/10

---

## Candidate 02 — Compounding Hockey Stick: FV = PV(1+r)^n as Time and Rate Sweep

- Source: `principles-finance-with-llms/chapters/07-time-value-of-money-i-single-payment-value.md`
- Topic: TIME VALUE OF MONEY · COMPOUND INTEREST
- Lane: MANIM (directed animation)
- Hook: At 4%, $1,000 grows 7x in 50 years. At 8%, the same $1,000 grows 47x. Double the rate, six times the final value. The exponential is not intuitive — watching the curve grow makes it visceral.
- The rule: FV = PV × (1+r)^n; PV=$1,000; n sweeps from 0 to 50 years; animated for r=4%, 8%, and 12% simultaneously
- Concrete numbers: At r=4%: FV(50)=$1,000×(1.04)^{50}=$7,107; At r=8%: FV(50)=$46,902; At r=12%: FV(50)=$289,002. Rule of 72: 4%→doubles at 18y; 8%→doubles at 9y; 12%→doubles at 6y
- The artifact / what moves: Three curves grow simultaneously from the same point (n=0, FV=$1,000) as n sweeps from 0 to 50. The 4% curve rises slowly and curves upward late. The 8% curve diverges visibly after year 20. The 12% curve rockets away, leaving the others far below by year 50. Doubling markers animate on each curve (vertical tick at each doubling point), showing the 4% curve doubling 2.8 times in 50 years versus the 12% curve doubling 8.3 times. A horizontal "simple interest" reference line (FV = 1000 + 1000×r×n) draws alongside each curve to show how fast the compound-over-simple gap opens.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r=8%, n=18 years, FV ≈ $3,996 — the Rule of 72 says doubling at 9 years, so two doublings in 18 years gives FV ≈ 4×$1,000=$4,000; P2: At r=4% vs r=8% at n=50 years, the ratio FV(8%)/FV(4%) = (1.08/1.04)^{50} ≈ (1.0385)^{50} ≈ 6.60 — the 8% curve is more than 6× the 4% curve at the 50-year mark, even though the rate is only 2× higher
- The change: After the three-curve animation, freeze at n=50 and animate r sweeping continuously from 1% to 15% as a single curve, showing how FV(50) grows from $1,638 (at r=1%) to $1,083,657 (at r=15%) — the nonlinearity of the rate sensitivity
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The chapter's Friend A / Friend B example (invest $45,000 total, end up with $887,000 vs $175,000 invested → $861,000) is this animation's final beat: starting 8 years earlier means 8 more years of the curve's steep end. Time in the market beats timing the market because of where on the exponential curve the dollars sit.
- Exclusions: Do not simulate inflation adjustments (Fisher equation) in the same animation; do not show annuities or multiple payment streams; one investment, one formula, multiple rates
- Sim slug: compounding-hockey-stick-fv-sweep
- Score: 9/10

---

## Candidate 03 — Gordon Growth Model Singularity: PV Explodes as g Approaches r

- Source: `principles-finance-with-llms/chapters/08-time-value-of-money-ii-equal-multiple-payments.md` (also in `mba-computational-finance/chapters/03-equity-and-fixed-income.md` and `mba-computational-finance/chapters/05-time-value-of-money-and-discounted-cash-flows.md`)
- Topic: VALUATION · GORDON GROWTH MODEL · PERPETUITY
- Lane: MANIM (directed animation)
- Hook: The Gordon Growth Model has a singularity baked in. As g approaches r, the stock price approaches infinity. In 2024, some analysts applied g near r to NVDA. The formula was trying to tell them something — watching the explosion shows what.
- The rule: PV = C / (r − g); growing perpetuity. C=$4 (first payment), r=8% (required return, fixed); g sweeps from 0% to 7.9%, approaching but never reaching 8%
- Concrete numbers: At g=0%: PV = $4/0.08 = $50; at g=4%: PV = $4/0.04 = $100; at g=6%: PV = $4/0.02 = $200; at g=7%: PV = $4/0.01 = $400; at g=7.5%: PV = $4/0.005 = $800; at g=7.9%: PV = $4/0.001 = $4,000; as g→r=8%, PV→∞
- The artifact / what moves: A curve draws left-to-right as g sweeps from 0% to 7.99%. The y-axis (PV) starts at $50 and the curve rises slowly, then faster, then near-vertically as g approaches 8%. The vertical asymptote at g=r is labeled with a dashed line. The formula (r−g) in the denominator is displayed on-screen and the denominator value updates as g sweeps, showing it shrinking toward zero. A second panel shows the same g sweep applied to two different values of r (8% and 10%), producing two curves with different singularity points — proving the explosion depends on where r is set, not just g.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At g=r/2=4% (half the discount rate), PV exactly doubles the no-growth value: PV=C/r=50, PV(g=r/2)=C/(r−r/2)=C/(r/2)=2×C/r=100 — confirmed by the formula; P2: The ratio PV(g=7%)/PV(g=4%) = (r−g_1)/(r−g_2) = (8%−4%)/(8%−7%) = 4%/1% = 4× — a 3 percentage-point increase in g causes a 4× increase in valuation, even though g only moved from 4% to 7%
- The change: After the single-asset animation, show what happens when r also increases (interest rates rise): both the level shifts down and the singularity moves to the right (to the new r). This shows how rising rates compress valuations doubly — directly (higher denominator) and by shrinking the safe g range
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The formula is not broken — it is right. An infinite valuation is the formula screaming that the assumption "g continues forever at near-r rates" is economically impossible. No company can grow faster than the economy forever. The animation makes the danger of optimistic g assumptions quantitative, not merely verbal.
- Exclusions: Do not simulate actual company valuations with this formula; do not extend to multi-stage DDM; do not show the derivation of the geometric series (known result)
- Sim slug: gordon-growth-singularity-sweep
- Score: 10/10

---

## Candidate 04 — Bond Duration as a Weighted Seesaw: Cash Flow Arms Balance at the Fulcrum

- Source: `principles-finance-with-llms/chapters/10-bonds-and-bond-valuation.md` ("Dig Deeper — Duration as a sensitivity measure" section)
- Topic: BONDS · MACAULAY DURATION · INTEREST RATE RISK
- Lane: MANIM (directed animation)
- Hook: Duration is not a calendar concept — it is a weighted average of when you get paid. A 30-year bond has a duration shorter than 30 years, because the coupons arrive early. Watching a seesaw balance at the fulcrum shows exactly why longer maturity bonds are more rate-sensitive.
- The rule: Macaulay Duration = Σ [t × PV(CF_t)] / Price = Σ [t × C/(1+y)^t + n×F/(1+y)^n] / Price — each cash flow weighted by its discounted present value, summed and divided by price
- Concrete numbers: 10-year bond, 5% annual coupon, F=$1,000, y=5% (par bond, P=$1,000). Ten coupon arms of $47.62 each (PV of $50/(1.05)^t for t=1..10) plus principal arm of $613.91 at t=10. Macaulay duration = 7.72 years. Compare: zero-coupon bond (duration = 10 years exactly). Compare: 5-year same coupon (duration ≈ 4.33 years).
- The artifact / what moves: A horizontal time axis draws from t=0 to t=10. Vertical bars rise at each period — ten short bars (coupons, smaller PV) and one tall bar at t=10 (principal, larger PV). Each bar is labeled with its PV contribution. A seesaw/balance beam materializes under the bars. As the animation plays, the fulcrum slides right from t=0 toward t=7.72, and the balance beam tilts until it is level at t=7.72 — Macaulay duration. The formula is shown numerically updating as each bar is added to the weighted sum. Then: a zero-coupon bond version shows only one bar (at t=10) and the fulcrum sits at t=10 exactly — maximum sensitivity.
- Output medium: Manim (mp4)
- Two testable predictions: P1: A 5% coupon 10-year bond at par (y=5%) has Macaulay duration exactly 7.72 years (verifiable analytically using the closed-form duration formula: D = (1+y)/y − [n×(c−y)+y+1]/[c×((1+y)^n−1)+y] for coupon rate c=y gives D = (1+y)/y × [1 − 1/(1+y)^n] ≈ 7.72); P2: The same bond's Modified Duration = Macaulay Duration / (1+y) = 7.72/1.05 ≈ 7.35 — meaning a 1% rise in yields produces a price fall of approximately 7.35%. At P=$1,000, that is a $73.50 price drop. Verified: at y=6%, P = 50×[1−(1.06)^{-10}]/0.06 + 1000/(1.06)^{10} ≈ $926, a $74 drop
- The change: After the 10-year coupon bond, animate a 30-year coupon bond — the bars extend far to the right but the coupons' early PV contributions pull the fulcrum forward to about 14–15 years, showing that even a 30-year bond has a duration much shorter than 30 years
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The chapter tells the reader that long bonds are rate-sensitive. The seesaw shows WHY — the fulcrum is where most of the PV sits, and for coupon bonds it is always less than maturity. A zero-coupon bond (fulcrum at maturity=maximum sensitivity) is the extreme case that makes the concept exact.
- Exclusions: Do not animate convexity (second-order Taylor term) in the same scene; do not show modified duration formula derivation; keep to the Macaulay duration geometric interpretation
- Sim slug: bond-duration-weighted-seesaw
- Score: 8/10
