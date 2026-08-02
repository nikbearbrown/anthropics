#!/usr/bin/env python3
"""
qm_hydrogen_radial_probability.py — Hydrogen Radial Probability: r_mp vs <r>
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-hydrogen-radial-probability
    manim -qh qm_hydrogen_radial_probability.py HydrogenRadialProbabilityScene

Verify:
    python3 qm_hydrogen_radial_probability.py

Physics:
    a0 = 0.0529 nm (Bohr radius)
    P(r) = r² |R_nl(r)|² — radial probability density
    1s: P(r) = 4r²/a0³ * e^(-2r/a0)
       r_mp = a0 (from dP/dr=0)
       <r> = 3a0/2 (from integral)
    2s: <r> = 6a0, 2p: <r> = 5a0, 3d: <r> = 7a0
"""
import sys
import numpy as np
from math import factorial

A0 = 0.0529177  # nm
EV = 1.60218e-19


def laguerre(n: int, alpha: float, x: np.ndarray) -> np.ndarray:
    """Associated Laguerre polynomial L_n^alpha(x)."""
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 1.0 + alpha - x
    L0, L1 = np.ones_like(x), 1.0 + alpha - x
    for k in range(1, n):
        L_next = ((2*k + 1 + alpha - x) * L1 - (k + alpha) * L0) / (k + 1)
        L0, L1 = L1, L_next
    return L1


def radial_wf_sq(n: int, l: int, r_arr: np.ndarray) -> np.ndarray:
    """
    R_nl(r)² in units of a0^-3, r in units of a0.
    Hydrogen radial wavefunctions (SI-free; r measured in a0).
    """
    rho = 2.0 * r_arr / n
    nr  = n - l - 1  # number of radial nodes
    # Normalisation constant squared (dimensionless, r in a0)
    norm_sq = (2.0 / n)**3 * factorial(nr) / (2*n * factorial(n+l)**3)
    # Corrected formula: norm² = (2/(n*a0))^3 * (n-l-1)! / (2n*((n+l)!)^3 / ...)
    # Use standard form:
    norm_sq = (2.0 / n)**3 * factorial(n - l - 1) / (2.0 * n * factorial(n + l)**3)
    Laguerre = laguerre(n - l - 1, 2*l + 1, rho)
    R_sq = norm_sq * np.exp(-rho) * rho**(2*l) * Laguerre**2
    return R_sq


def prob_density(n: int, l: int, r_arr: np.ndarray) -> np.ndarray:
    """P(r) = r² R²_nl(r), r in a0."""
    return r_arr**2 * radial_wf_sq(n, l, r_arr)


def mean_r(n: int, l: int) -> float:
    """<r> = a0/2 * [3n² - l(l+1)] in units of a0."""
    return 0.5 * (3.0 * n**2 - l * (l + 1))


def r_mp_1s() -> float:
    """Most probable r for 1s: dP/dr=0 → r_mp = a0 (=1 in a0 units)."""
    return 1.0


def verify():
    print("=== Hydrogen radial probability verification ===")
    r_arr = np.linspace(0.001, 25, 100000)
    dr    = r_arr[1] - r_arr[0]

    P1s = prob_density(1, 0, r_arr)
    norm = np.trapz(P1s, r_arr)
    print(f"∫P_1s dr = {norm:.6f}  (should be 1.0)")

    r_mp_num = r_arr[P1s.argmax()]
    print(f"r_mp (1s) = {r_mp_num:.4f} a0  (should be 1.0 a0 = 0.0529 nm)")

    r_mean_num = np.trapz(r_arr * P1s, r_arr)
    r_mean_ana = mean_r(1, 0)
    print(f"<r> (1s) numerical = {r_mean_num:.4f} a0  (analytical = {r_mean_ana:.4f} a0 = 1.5)")
    print(f"  = {r_mean_ana * A0 * 1e3:.4f} pm  (card says 0.0794 nm = 79.4 pm)")

    r_mean_2p = mean_r(2, 1)
    print(f"<r> (2p) = {r_mean_2p:.1f} a0  (card says 5a0)")
    ratio_2p_1s = r_mean_2p / r_mean_ana
    print(f"<r>(2p)/<r>(1s) = {ratio_2p_1s:.1f}  (should be 5)")
    print("=== PASSED ===" if abs(norm - 1.0) < 0.01 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED_C  = "#FF6B6B"


class HydrogenRadialProbabilityScene(Scene):
    """
    Radial probability P(r) for hydrogen 1s, 2s, 2p, 3d.
    Shows r_mp vs <r>, node structure, and n-scaling.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_1s_buildup()
        self._phase_excited_states()
        self._phase_jensen()

    def _phase_title(self):
        title = Text("Hydrogen Radial Probability", font="EB Garamond",
                     font_size=56, color=INK)
        sub1 = Text(
            "Most probable distance ≠ average distance — the distribution is skewed.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"P(r) = r^2 |R_{nl}|^2 \quad r_{\rm mp} = a_0 \quad \langle r\rangle = \tfrac{3}{2}a_0",
                       color=BLUE, font_size=26)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_1s_buildup(self):
        r_max = 8.0
        r_arr = np.linspace(0.0, r_max, 500)
        ax = Axes(
            x_range=[0, r_max, 2],
            y_range=[0, 0.60, 0.2],
            x_length=9.0,
            y_length=4.2,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"r / a_0", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"P(r)", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("1s radial probability density — step by step",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.3)

        # Step 1: |ψ|² ∝ e^{-2r} (monotone decreasing)
        psi2 = np.exp(-2.0 * r_arr) / np.pi   # unnormalised density
        c_psi2 = VMobject(color=DIM, stroke_width=2.5)
        c_psi2.set_points_smoothly([ax.c2p(r, y * 3.0) for r, y in zip(r_arr, psi2)])
        lbl1 = MathTex(r"|R_{10}|^2 \propto e^{-2r/a_0}", color=DIM, font_size=22
                       ).to_edge(DOWN, buff=0.28)
        self.play(Create(c_psi2), Write(lbl1), run_time=1.2)
        self.wait(0.6)

        # Step 2: r² factor
        r2_arr = r_arr**2 / 4.0   # display
        c_r2 = VMobject(color=BROWN, stroke_width=2.5)
        c_r2.set_points_smoothly([ax.c2p(r, y) for r, y in zip(r_arr, r2_arr)])
        lbl2 = MathTex(r"r^2\ \text{(volume factor — grows outward)}",
                       color=BROWN, font_size=22).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(lbl1), Create(c_r2), Write(lbl2), run_time=1.0)
        self.wait(0.6)

        # Step 3: Product P(r)
        P_1s = prob_density(1, 0, np.where(r_arr < 0.0001, 0.0001, r_arr))
        c_P = VMobject(color=BLUE, stroke_width=3.5)
        c_P.set_points_smoothly([ax.c2p(r, y) for r, y in zip(r_arr, P_1s)])
        lbl3 = MathTex(r"P(r) = r^2 |R_{10}|^2 \quad \text{peak at } r_{mp} = a_0",
                       color=BLUE, font_size=22).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(lbl2), Create(c_P), Write(lbl3), run_time=1.2)

        # Markers
        r_mp_val = 1.0
        r_mean_val = mean_r(1, 0)
        mk_mp = DashedLine(ax.c2p(r_mp_val, 0), ax.c2p(r_mp_val, P_1s.max()),
                           color=GOLD, dash_length=0.08, stroke_width=2.0)
        mk_mean = DashedLine(ax.c2p(r_mean_val, 0), ax.c2p(r_mean_val, P_1s.max() * 0.75),
                             color=RED_C, dash_length=0.08, stroke_width=2.0)
        lbl_mp   = MathTex(r"r_{mp} = a_0", color=GOLD, font_size=20).next_to(ax.c2p(r_mp_val, P_1s.max()), UP, buff=0.05)
        lbl_mean = MathTex(r"\langle r\rangle = \frac{3}{2}a_0", color=RED_C, font_size=20).next_to(
            ax.c2p(r_mean_val, P_1s.max() * 0.75), UR, buff=0.05)
        self.play(Create(mk_mp), Create(mk_mean), Write(lbl_mp), Write(lbl_mean), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_psi2, c_r2, c_P, lbl3,
                          mk_mp, mk_mean, lbl_mp, lbl_mean), run_time=0.5)

    def _phase_excited_states(self):
        r_arr = np.linspace(0.001, 25, 600)
        states = [(1, 0, BLUE), (2, 0, GOLD), (2, 1, BROWN), (3, 2, DIM)]
        ax = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 0.35, 0.1],
            x_length=9.0,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.6)
        lbl_x = MathTex(r"r / a_0", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"P(r)", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Radial probability for n=1,2,3 states",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)

        legend_items = []
        for n, l, color in states:
            P = prob_density(n, l, r_arr)
            c = VMobject(color=color, stroke_width=2.8)
            c.set_points_smoothly([ax.c2p(r, y) for r, y in zip(r_arr, P)])
            r_mean_val = mean_r(n, l)
            lbl_s = Text(f"n={n},ℓ={l}  ⟨r⟩={r_mean_val:.0f}a₀",
                         font="EB Garamond", font_size=18, color=color)
            legend_items.append(lbl_s)
            self.play(Create(c), run_time=0.9)

        leg = VGroup(*legend_items).arrange(DOWN, buff=0.18, aligned_edge=LEFT).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(leg), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, leg, *self.mobjects), run_time=0.5)

    def _phase_jensen(self):
        eq = MathTex(
            r"\langle 1/r\rangle \neq 1/\langle r\rangle",
            r"\quad\Rightarrow\quad E = -\frac{e^2}{2a_0}\,\langle 1/r\rangle",
            color=INK, font_size=32,
        ).center().shift(UP * 0.5)
        note = Text(
            "Jensen's inequality: the average energy comes from ⟨1/r⟩, not 1/⟨r⟩.",
            font="EB Garamond", font_size=21, color=DIM,
        ).next_to(eq, DOWN, buff=0.45)
        self.play(Write(eq), run_time=1.2)
        self.play(FadeIn(note), run_time=0.9)
        self.wait(3.0)
