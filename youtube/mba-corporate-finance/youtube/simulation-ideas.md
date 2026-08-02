# MBA Corporate Finance — Simulation Ideas

MANIM-lane candidates only. Score ≥ 6 required. All cards are directed, scripted, cinematic animations of known equations.

Note: `corporate-finance-with-ai/` covers essentially the same content (same protagonist, same firm Halverson). Cards below reflect the most thorough treatment across both books; they are written once here and noted as applying to both.

---

## Candidate 01 — MM Proposition II: Cost of Equity Rises Linearly as Leverage Increases

- Source: `mba-corporate-finance/chapters/07-capital-structure-theory-the-modigliani-miller-world.md` (also applies to `corporate-finance-with-ai/chapters/07-capital-structure-theory-the-modigliani-miller-world.md`)
- Topic: CAPITAL STRUCTURE · MODIGLIANI-MILLER
- Lane: MANIM (directed animation)
- Hook: Add cheap debt, and the equity gets more expensive by exactly the same amount. The WACC never moves. This is the theorem that says capital structure is irrelevant — and watching the two costs offset in real time is the proof.
- The rule: R_E = R_U + (D/E) × (R_U − R_D); WACC = (E/V)·R_E + (D/V)·R_D·(1−T); in the no-tax MM world WACC = R_U (constant)
- Concrete numbers: R_U = 9% (unlevered equity cost), R_D = 5% (cost of debt, held constant); D/E sweeps from 0 to 3.0 (0% to 75% debt); tax rate T=0 (pure MM world first, then T=24% in second pass)
- The artifact / what moves: Three curves animate simultaneously as D/E sweeps left to right. (1) R_E rises linearly per the formula — the rising line. (2) R_D stays flat at 5% — a horizontal line. (3) WACC stays flat at R_U=9% — another horizontal line. The animation shows R_E rising and the equity weight falling in exact lockstep so the WACC never budges. Then in a second beat, T=24% is introduced: R_E still rises, but the after-tax R_D falls slightly, and the WACC line gently slopes downward — the tax shield is visible as the gap between the two WACC lines (with and without taxes).
- Output medium: Manim (mp4)
- Two testable predictions: P1: At D/E=1.0 (50% debt), R_E = 9% + 1.0×(9%−5%) = 13%. WACC = 0.5×13% + 0.5×5%×(1−0) = 6.5% + 2.5% = 9% — exactly R_U, confirming MM invariance; P2: At D/E=2.0 (67% debt), R_E = 9% + 2.0×4% = 17%. WACC still = (1/3)×17% + (2/3)×5% = 5.67% + 3.33% = 9% — still R_U. Every leverage ratio produces the same WACC.
- The change: After the no-tax animation, replay with T=24%: WACC falls from 9% to approximately 8.1% at D/E=1 (the tax shield creates a wedge). The gap between the two WACC curves is T×R_D×(D/V) — the value of the interest tax shield, labeled on-screen.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic
- Teardown angle: The theorem is counterintuitive because cheap debt "should" lower the average cost. MM shows it doesn't — the rising equity cost is the exact mechanical offset. What changes the WACC is not the mix but the taxes: only when T>0 does the tax shield break the MM invariance.
- Exclusions: Do not animate bankruptcy costs or distress thresholds (D3 territory for the tradeoff-theory curve); do not show actual firm capital structures; keep to the two-cost framework (no preferred equity, no hybrid instruments)
- Sim slug: mm-prop-ii-wacc-invariance
- Score: 7/10
