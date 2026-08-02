# MBA Computational Finance — Simulation Ideas

MANIM-lane candidates only. Score ≥ 6 required. All cards are directed, scripted, cinematic animations of known equations.

---

## Candidate 01 — The Diversification Miracle: Portfolio Variance Collapses as Correlation Falls

- Source: `mba-computational-finance/chapters/08-the-diversification-miracle.md`
- Topic: DIVERSIFICATION · PORTFOLIO VARIANCE
- Lane: MANIM (directed animation)
- Hook: Two identical stocks, same expected return, same volatility — combine them and the risk can drop to zero. The formula shows exactly when and why.
- The rule: σ_p² = w_A²σ_A² + w_B²σ_B² + 2w_A·w_B·ρ_{AB}·σ_A·σ_B — the cross-term is controlled entirely by ρ
- Concrete numbers: Both assets: E(R)=10%, σ=30%, equal weights w_A=w_B=0.5; ρ sweeps from +1 → 0 → −1 in continuous animation
- The artifact / what moves: A single number — the portfolio volatility — animates downward from 30% (at ρ=+1) to ~21% (at ρ=0) to 0% (at ρ=−1), while a bracket on-screen shows the two components (variance terms) staying fixed and only the cross-term shrinking. The volatility bar literally collapses to zero at ρ=−1. Expected return stays pinned at 10% throughout — a horizontal line that never moves.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At ρ=0 (independent assets), portfolio σ = 30% × (1/√2) ≈ 21.2% — exactly half the variance of either asset alone; P2: At ρ=−1 with equal weights (w_A=w_B=0.5), σ_p = |w_A·σ_A − w_B·σ_B| = 0% — a riskless portfolio with 10% expected return
- The change: Animate ρ continuously from +1 to −1; show the cross-term (the third bar in a three-bar stacked display) shrinking from +450 to −450 in variance units while the sum (portfolio variance) traces a curve downward
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The "free lunch" of diversification is real and exact — a 30% reduction in volatility from ρ=0 alone, zero cost in expected return. The chapter shows this result, but watching it animate makes visceral what the formula merely states.
- Exclusions: Do not simulate crisis correlation spikes (D3 territory); do not show the n-asset generalization or the covariance matrix; do not plot actual stock returns
- Sim slug: diversification-correlation-sweep
- Score: 10/10

---

## Candidate 02 — Black-Scholes Call Price: The S-Curve from Deep OTM to Deep ITM

- Source: `mba-computational-finance/chapters/07-options-and-derivatives.md`
- Topic: OPTIONS · BLACK-SCHOLES
- Lane: MANIM (directed animation)
- Hook: The call price rises from almost nothing to exactly the stock price — but it traces an S-curve, not a line, and the inflection happens right at-the-money. That kink is where all the interesting trading lives.
- The rule: C = S·N(d₁) − K·e^{−rT}·N(d₂), where d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T), d₂ = d₁ − σ√T
- Concrete numbers: K=$100 (fixed strike), r=4.5%, T=0.5 years, σ=25%; S sweeps from $60 (deep OTM) to $140 (deep ITM)
- The artifact / what moves: A curve draws itself left-to-right as S/K sweeps from 0.6 to 1.4. The curve starts near zero, traces a sigmoid inflection at S=K=$100, and approaches the intrinsic-value line (S−K, the 45° line) at high S. Two reference lines animate simultaneously: the intrinsic value floor max(S−K,0) as a kinked line, and the BS curve above it. The gap between them (time value) peaks at-the-money and shrinks to zero deep ITM and OTM.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At S=K=$100 (at-the-money), C ≈ $5.16 using the Jin example from the chapter (S=185→170 put; scaling to S=K gives the ATM value near σ·S·√(T/2π) ≈ $100 × 0.25 × √(0.5/2π) ≈ $4.99); P2: At S=$140 (deep ITM, S/K=1.4), C ≈ $40.80 (intrinsic value $40, time value ≈ $0.80) — the BS price within $1 of intrinsic value, demonstrating the deep-ITM collapse of time value
- The change: Hold K, r, T, σ fixed; animate S sweeping; then show a second animation where σ shifts from 15% to 35% and the curve "inflates" (time value rises uniformly, sigmoid becomes more pronounced)
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The probability distribution N(d₁) is the expected payoff if exercised; N(d₂) is the risk-neutral probability of exercise. The S-curve drawing is the visual evidence that an option's delta varies — it is not a fixed sensitivity, and that variation (gamma) is concentrated exactly at-the-money.
- Exclusions: Do not simulate implied volatility surfaces (interactive D3); do not show binomial tree convergence; do not show Greeks as separate panels (one animation at a time)
- Sim slug: black-scholes-call-curve-sweep
- Score: 9/10

---

## Candidate 03 — The Efficient Frontier: Parabola Traces as Portfolio Weights Vary

- Source: `mba-computational-finance/chapters/09-portfolio-construction.md`
- Topic: PORTFOLIO THEORY · EFFICIENT FRONTIER
- Lane: MANIM (directed animation)
- Hook: Two assets combine into every possible portfolio — and the set of those portfolios isn't a cloud; it traces a precise parabola in return-risk space, with a leftmost tip that defines the minimum-variance portfolio.
- The rule: E(R_p) = w·E(R_A) + (1−w)·E(R_B); σ_p² = w²σ_A² + (1−w)²σ_B² + 2w(1−w)ρσ_Aσ_B; trace over w ∈ [0,1]
- Concrete numbers: Asset A: E(R)=11%, σ=16% (like VTI); Asset B: E(R)=3%, σ=6% (like BND); ρ=−0.10 (equity-bond calm-period correlation). Risk-free rate r_f=4.5% for Capital Market Line
- The artifact / what moves: A dot moves along a curved path in (σ, E[R]) space as w_A sweeps from 0 (100% bonds) to 1 (100% stocks). The path curves leftward — bulging toward lower volatility than the straight-line mix — forming the parabola. The minimum-variance portfolio is labeled as the leftmost point (around w_A≈20%). Then a Capital Market Line extends from (0, r_f=4.5%) tangent to the frontier, marking the tangency (max-Sharpe) portfolio. The path is drawn continuously, point by point.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The minimum-variance portfolio weight is w_A = (σ_B² − ρσ_Aσ_B) / (σ_A² + σ_B² − 2ρσ_Aσ_B) ≈ (36 − (−0.1)(16)(6)) / (256 + 36 − 2(−0.1)(16)(6)) ≈ (36 + 9.6) / (292 + 19.2) ≈ 45.6/311.2 ≈ 14.6%, giving σ_MVP ≈ 5.4% (lower than either asset alone); P2: With ρ=+1 (perfect correlation) the frontier degenerates to a straight line — no bulge, no diversification benefit — confirming the formula's prediction that the cross-term at ρ=+1 factors to a perfect square
- The change: After tracing the frontier at ρ=−0.1, re-animate with ρ=+0.6 (equity-equity correlation) and show the parabola "tighten" — less leftward bulge, minimum-variance portfolio shifts right, proving more correlation = less diversification benefit
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The minimum-variance portfolio is mathematically exact — there is a specific weight at which further diversifying does not reduce risk. That point is the argument against concentration, made geometric. The Capital Market Line shows that once a risk-free asset exists, the tangency portfolio dominates every other risky portfolio for a rational investor.
- Exclusions: Do not extend to n-asset frontier (requires matrix optimization — D3 territory for interactivity); do not show actual ETF return data; do not add more than one correlation value per animation segment
- Sim slug: efficient-frontier-parabola-trace
- Score: 9/10

---

## Candidate 04 — CAPM Security Market Line: Expected Return Drawing as Beta Climbs

- Source: `mba-computational-finance/chapters/11-asset-pricing-models.md`
- Topic: ASSET PRICING · CAPM · SECURITY MARKET LINE
- Lane: MANIM (directed animation)
- Hook: CAPM says every asset's required return is just one equation — and every fairly priced asset should sit on the same line. NVDA didn't. Its alpha was 64 percentage points. You can see exactly where that is.
- The rule: E(R_i) = R_f + β_i · (E(R_m) − R_f); the Security Market Line is this equation plotted across all β
- Concrete numbers: R_f=4.5%, ERP=6%; SML drawn for β from 0 to 2.5; NVDA: β=1.65 (36-month estimate), actual return ≈78%, CAPM-predicted ≈14.4%, alpha ≈64 pp; market portfolio: β=1, E(R)=10.5%
- The artifact / what moves: The SML line draws itself from left to right as β sweeps 0→2.5 — starting from the risk-free point (0, 4.5%) and rising at slope=ERP=6%. As the line draws, labeled dots appear: T-bills at β=0; market portfolio at β=1, E(R)=10.5%; hypothetical average stock at β=1.5; finally NVDA's dot appears at (β=1.65, E(R)=14.4%) on the SML, then an arrow shoots upward to (β=1.65, E(R)=78%) — the actual return — labeled "alpha = +64pp". The gap is animated.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The SML slope equals the equity risk premium exactly — a β=2.0 stock requires E(R)=4.5% + 2.0×6%=16.5%, and a β=0.5 stock requires 4.5%+3%=7.5%; P2: If the SML holds, all assets plot on the line. An asset above the SML (positive alpha) is underpriced — its expected return exceeds its risk-justified level. NVDA at +64pp alpha sits 10.7× above the SML-predicted return, a visible displacement on any reasonable y-axis scale.
- The change: Show the SML under two ERP assumptions (4.5% and 6.5%) — the line pivots, changing its slope while anchored at the risk-free rate intercept, demonstrating how ERP uncertainty translates directly into CAPM required-return uncertainty
- Human supplies (Claude can't): Nothing — fully synthetic/analytic (NVDA's approximate figures are stated in the chapter)
- Teardown angle: The alpha gap is the entire question of whether NVDA was exceptional or lucky. CAPM draws the baseline that makes the question precise — without the SML, "exceptional" and "lucky" are indistinguishable. The animation makes the gap geometric rather than arithmetic.
- Exclusions: Do not animate beta regression scatter plots (D3 territory); do not show Fama-French factors as additional panels; do not plot historical data points
- Sim slug: capm-security-market-line-draw
- Score: 9/10
