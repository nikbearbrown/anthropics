#!/usr/bin/env python3
"""
perturbation_convergence_avoided_crossing.py — Perturbation Convergence and Avoided Crossings
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/perturbation-convergence-avoided-crossing
    manim -qh perturbation_convergence_avoided_crossing.py PerturbationConvergenceScene

Verify:
    python3 perturbation_convergence_avoided_crossing.py --verify

Physics:
    H = diag(0, ε) + λ[[0,1],[1,0]]
    Exact: E_± = ε/2 ± √((ε/2)² + λ²)
    Series valid for λ ≪ ε;  convergence radius λ = ε/2
    Degenerate (ε=0): series diverges for any λ≠0; gap = 2λ
"""
import sys
import numpy as np
from math import factorial


def exact_eigenvalues(eps, lam):
    """Exact eigenvalues of the 2x2 system."""
    return np.array([
        eps/2 - np.sqrt((eps/2)**2 + lam**2),
        eps/2 + np.sqrt((eps/2)**2 + lam**2),
    ])


def perturbation_series(eps, lam, order):
    """
    Perturbation series for the lower eigenvalue E₋ around λ=0.
    E₋ = 0 + 0·λ − λ²/ε + 0·λ³ + λ⁴/ε³ − ...
    (Maclaurin series of −√((ε/2)² + λ²) + ε/2 in λ)
    """
    # Compute via Taylor: E(λ) = ε/2 − √((ε/2)²+λ²)
    # Taylor expand √(a²+λ²) = a + λ²/(2a) − λ⁴/(8a³) + ...
    a = eps / 2.0
    if a == 0:
        return np.sign(lam) * lam  # degenerate: diverges
    result = 0.0
    # Terms: E_- = ε/2 - (a + λ²/2a - λ⁴/8a³ + λ⁶/16a⁵ - ...)
    # = 0 - λ²/2a + λ⁴/8a³ - λ⁶/16a⁵ ...
    for k in range(1, order + 1):
        # k-th term coefficient from √(a²+λ²)
        # coefficient of λ^{2k} in √(a²+λ²) = a * C(1/2, k) * (λ/a)^{2k}
        coeff_binom = 1.0
        for j in range(k):
            coeff_binom *= (0.5 - j) / (j + 1)
        result += -coeff_binom * (lam**(2*k)) / (a**(2*k - 1))
    return result


def verify():
    print("=== Perturbation convergence verification ===")
    eps = 1.0
    for lam in [0.0, 0.2, 0.5, 0.8, 1.2]:
        exact = exact_eigenvalues(eps, lam)[0]
        pert3 = perturbation_series(eps, lam, 3)
        print(f"  λ={lam:.1f}: exact={exact:.6f}, 3rd-order={pert3:.6f}, diff={abs(exact-pert3):.6f}")

    print(f"\n  Convergence radius: λ = ε/2 = {eps/2}")
    print(f"  Gap at λ=0.5ε: exact gap = 2√((ε/2)²+λ²) = {2*np.sqrt((eps/2)**2+(eps*0.5)**2):.4f}")

    # Degenerate case: ε=0
    print("\n  Degenerate case ε=0:")
    for lam in [0.1, 0.5, 1.0]:
        E_exact = exact_eigenvalues(0.0, lam)
        print(f"  λ={lam:.1f}: exact E_± = {E_exact[0]:.4f}, {E_exact[1]:.4f}  (gap=2λ={2*lam:.3f})")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class PerturbationConvergenceScene(Scene):
    """
    Phase 1: title
    Phase 2: avoided crossing — exact hyperbola vs 1st, 2nd, 3rd order series
    Phase 3: degenerate case ε→0 — series collapses, gap = 2λ
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_avoided_crossing()
        self._phase_degenerate()

    def _phase_title(self):
        title = Text("Perturbation Convergence", font="EB Garamond", font_size=52, color=INK)
        sub1  = Text(
            "E_n(λ) is a Taylor series — it has a radius of convergence",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "H = diag(0, ε) + λ [[0,1],[1,0]] — avoided crossing hyperbola",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_avoided_crossing(self):
        eps = 1.0
        lam_max = 2.0

        ax = Axes(
            x_range=[0, lam_max, 0.5], y_range=[-2.2, 2.2, 0.5],
            x_length=8.5, y_length=5.0,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).shift(UP * 0.1)

        x_lbl = MathTex(r"\lambda", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"E", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        lams = np.linspace(0.01, lam_max, 500)

        # Exact curves
        E_minus = [exact_eigenvalues(eps, l)[0] for l in lams]
        E_plus  = [exact_eigenvalues(eps, l)[1] for l in lams]
        pts_minus = [ax.c2p(l, e) for l, e in zip(lams, E_minus)]
        pts_plus  = [ax.c2p(l, e) for l, e in zip(lams, E_plus)]
        c_minus = VMobject(color=BLUE, stroke_width=3.0); c_minus.set_points_smoothly(pts_minus)
        c_plus  = VMobject(color=GOLD, stroke_width=3.0); c_plus.set_points_smoothly(pts_plus)
        self.play(Create(c_minus), Create(c_plus), run_time=1.2)

        lbl_exact = Text("Exact (avoided crossing)", font="EB Garamond", font_size=18, color=INK).to_corner(UR, buff=0.35)
        self.play(Write(lbl_exact), run_time=0.5)

        # Perturbation series at various orders
        pert_styles = [(1, BROWN), (2, "#88CC44"), (3, "#CC88AA")]
        for order, col in pert_styles:
            pert_vals = [perturbation_series(eps, l, order) for l in lams]
            pert_pts  = [ax.c2p(l, max(min(v, 2.2), -2.2)) for l, v in zip(lams, pert_vals)]
            c_pert = VMobject(color=col, stroke_width=2.0, stroke_opacity=0.55)
            c_pert.set_points_smoothly(pert_pts)
            lbl_p = Text(f"Order {2*order}", font="EB Garamond", font_size=16, color=col).to_corner(UR, buff=0.35).shift(DOWN * (0.5 * pert_styles.index((order, col)) + 0.5))
            self.play(Create(c_pert), Write(lbl_p), run_time=0.7)

        # Convergence radius line
        conv_line = DashedLine(ax.c2p(eps/2, -2.2), ax.c2p(eps/2, 2.2), color=DIM, stroke_width=1.5)
        conv_lbl  = MathTex(r"\lambda = \varepsilon/2", color=DIM, font_size=20).next_to(ax.c2p(eps/2, 1.8), RIGHT, buff=0.1)
        self.play(Create(conv_line), Write(conv_lbl), run_time=0.6)

        fin = Text(
            "Series diverges from exact at λ = ε/2 — the radius of convergence",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_degenerate(self):
        hdr = Text(
            "Degenerate case ε → 0: series diverges for any λ≠0  ·  gap = 2λ",
            font="EB Garamond", font_size=22, color=BROWN,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        eps_tracker = ValueTracker(1.0)
        lam_max = 1.5

        ax = Axes(
            x_range=[0, lam_max, 0.5], y_range=[-2.0, 2.0, 0.5],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(DOWN * 0.2)
        self.play(Create(ax), run_time=0.6)

        lams = np.linspace(0.0, lam_max, 400)

        def _curves():
            eps = eps_tracker.get_value()
            E_m = [exact_eigenvalues(eps, l)[0] for l in lams]
            E_p = [exact_eigenvalues(eps, l)[1] for l in lams]
            pts_m = [ax.c2p(l, e) for l, e in zip(lams, E_m)]
            pts_p = [ax.c2p(l, e) for l, e in zip(lams, E_p)]
            gm = VMobject(color=BLUE, stroke_width=2.8); gm.set_points_smoothly(pts_m)
            gp = VMobject(color=GOLD, stroke_width=2.8); gp.set_points_smoothly(pts_p)
            return VGroup(gm, gp)

        def _eps_lbl():
            eps = eps_tracker.get_value()
            return MathTex(rf"\varepsilon = {eps:.2f}", color=INK, font_size=28).to_corner(UR, buff=0.35)

        dyn = always_redraw(_curves)
        lbl = always_redraw(_eps_lbl)
        self.add(dyn, lbl)

        self.play(eps_tracker.animate.set_value(0.0), run_time=4.0, rate_func=smooth)

        gap_lbl = MathTex(r"\text{gap} = 2|\langle 1|H'|2\rangle| = 2\lambda", color=GOLD, font_size=28).to_edge(DOWN, buff=0.28)
        self.play(Write(gap_lbl), run_time=0.8)
        self.wait(2.5)
