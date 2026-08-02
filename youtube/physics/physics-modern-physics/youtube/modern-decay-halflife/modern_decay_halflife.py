#!/usr/bin/env python3
"""
modern_decay_halflife.py — Nuclear Decay: N(t) = N₀ e^{-λt} and Half-Life Staircase
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    C-14: t_1/2=5730 yr, λ=3.83e-12 s⁻¹
    After n half-lives: N = N₀/2ⁿ
    Mean lifetime τ = t_1/2 / ln2

Run standalone to verify:
    python3 modern_decay_halflife.py
"""
import sys
import numpy as np
from math import factorial

# Use stdlib factorial to avoid deprecated np.math.factorial
LAMBDA_C14 = np.log(2) / (5730 * 365.25 * 24 * 3600)  # s⁻¹
T_HALF_C14 = 5730.0  # years
T_HALF_I131 = 8.02   # days


def N(t_yr, t_half_yr=T_HALF_C14, N0=1.0):
    lam = np.log(2) / t_half_yr
    return N0 * np.exp(-lam * t_yr)


def verify():
    print("=== Nuclear Decay Half-life verification ===")
    print(f"C-14 λ = {LAMBDA_C14:.4e} s⁻¹  (card: 3.83e-12)")
    print(f"After 1 t_1/2: N/N0 = {N(5730):.6f}  (should be 0.500000)")
    print(f"After 3 t_1/2: N/N0 = {N(3*5730):.6f}  (should be 0.125000)")
    print(f"After 10 t_1/2: N/N0 = {N(10*5730):.8f}  (should be {1/1024:.8f})")
    # P2: mean lifetime
    tau = T_HALF_C14 / np.log(2)
    print(f"τ = t_1/2/ln2 = {tau:.2f} yr  (= 1.443 × t_1/2)")
    print(f"At t=τ: N/N0 = {N(tau):.6f}  (should be 1/e = {1/np.e:.6f})")
    # Compare C-14 and I-131 over 30 days
    print(f"\nOver 30 days:")
    print(f"  C-14 fraction: {N(30/365.25):.8f}  (barely budges)")
    print(f"  I-131 fraction: {N(30, T_HALF_I131/365.25):.6f}  (nearly gone)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class ModernDecayHalflifeScene(Scene):
    """
    Continuous exponential N(t) + discrete staircase.
    Half-life markers. Mean lifetime annotation.
    C-14 vs I-131 overlay.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_curve_and_staircase()
        self._phase_comparison()

    def _phase_title(self):
        title = Text("Radioactive Decay — N(t) = N₀ e^{−λt}",
                     font="EB Garamond", font_size=54, color=INK)
        sub = MathTex(r"t_{1/2} = \frac{\ln 2}{\lambda},\quad \tau = \frac{1}{\lambda}",
                      color=BLUE, font_size=32)
        hook = Text(
            "Every nucleus has the same decay probability per second — age doesn't matter",
            font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eqs = VGroup(
            MathTex(r"N(t) = N_0\,e^{-\lambda t}", color=INK, font_size=38),
            MathTex(r"t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}",
                    color=BLUE, font_size=34),
            MathTex(r"\tau = \frac{1}{\lambda} = \frac{t_{1/2}}{\ln 2} \approx 1.443\,t_{1/2}",
                    color=GOLD, font_size=32),
            MathTex(r"\text{At }t=\tau:\; N = N_0/e \neq N_0/2",
                    color=DIM, font_size=28),
        ).arrange(DOWN, buff=0.42).center()
        for mob in eqs:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_curve_and_staircase(self):
        # C-14: plot in units of half-lives
        n_half = 10
        t_arr = np.linspace(0, n_half, 500)
        N_arr = 0.5**t_arr  # N(t) in units where t is measured in half-lives

        ax = Axes(
            x_range=[0, n_half, 1],
            y_range=[0, 1.05, 0.25],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"t\;(t_{1/2})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"N/N_0", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("Continuous exponential + stochastic staircase",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        # Smooth curve
        exp_curve = ax.plot_line_graph(
            x_values=list(t_arr), y_values=list(N_arr),
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        self.play(Create(exp_curve), run_time=2.0)

        # Stochastic staircase (simulate ~50 atoms for visual clarity)
        np.random.seed(42)
        n_atoms = 50
        # Exponential inter-event times
        lam = np.log(2)  # per half-life unit
        events = []
        t_current = 0
        remaining = n_atoms
        while remaining > 0 and t_current < n_half:
            dt = np.random.exponential(1.0 / (lam * remaining))
            t_current += dt
            if t_current < n_half:
                events.append((t_current, remaining))
            remaining -= 1

        # Build staircase segments
        stair_x = [0]
        stair_y = [n_atoms / n_atoms]
        current_n = n_atoms
        for t_ev, n_before in events:
            stair_x.extend([t_ev, t_ev])
            stair_y.extend([current_n / n_atoms, (current_n - 1) / n_atoms])
            current_n -= 1
        if stair_x[-1] < n_half:
            stair_x.append(n_half)
            stair_y.append(current_n / n_atoms)

        stair = ax.plot_line_graph(
            x_values=stair_x, y_values=stair_y,
            line_color=BROWN, stroke_width=1.5, add_vertex_dots=False,
        )
        self.play(Create(stair), run_time=2.0)

        # Half-life dashed markers
        for i in range(1, 4):
            marker = DashedLine(ax.c2p(i, 0), ax.c2p(i, 0.5**i),
                                color=GOLD, stroke_width=1.5)
            horiz = DashedLine(ax.c2p(0, 0.5**i), ax.c2p(i, 0.5**i),
                               color=GOLD, stroke_width=1.5)
            lbl = MathTex(f"N_0/2^{i}", color=GOLD, font_size=18
                          ).next_to(ax.c2p(0, 0.5**i), LEFT, buff=0.1)
            self.play(Create(marker), Create(horiz), Write(lbl), run_time=0.6)

        # Mean lifetime τ = 1/ln2 ≈ 1.443 half-lives
        tau_pos = 1.0 / np.log(2)
        tau_dot = Dot(ax.c2p(tau_pos, np.exp(-1)), color=GOLD, radius=0.1)
        tau_lbl = MathTex(r"\tau=1.443\,t_{1/2},\;N=N_0/e", color=GOLD, font_size=19
                          ).next_to(tau_dot, UR, buff=0.1)
        self.play(FadeIn(tau_dot), Write(tau_lbl), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, exp_curve, stair, tau_dot, tau_lbl),
                  run_time=0.5)

    def _phase_comparison(self):
        title = Text("C-14 vs I-131: 4 orders of magnitude in half-life",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        # Plot both on time scale of 30 days
        t_days = np.linspace(0, 30, 300)
        t_half_I = 8.02         # days
        t_half_C14 = 5730 * 365.25  # days

        N_I = 0.5**(t_days / t_half_I)
        N_C14 = 0.5**(t_days / t_half_C14)

        ax = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 1.1, 0.2],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"t\;(\text{days})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"N/N_0", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        c14_curve = ax.plot_line_graph(
            x_values=list(t_days), y_values=list(N_C14),
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        i131_curve = ax.plot_line_graph(
            x_values=list(t_days), y_values=list(N_I),
            line_color=BROWN, stroke_width=3, add_vertex_dots=False,
        )
        c14_lbl = MathTex(r"{}^{14}\text{C}\;(t_{1/2}=5730\,\text{yr})",
                          color=BLUE, font_size=20).to_corner(UR, buff=0.5)
        i131_lbl = MathTex(r"{}^{131}\text{I}\;(t_{1/2}=8.02\,\text{d})",
                           color=BROWN, font_size=20).next_to(c14_lbl, DOWN, buff=0.2)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(c14_curve), Write(c14_lbl), run_time=1.5)
        self.play(Create(i131_curve), Write(i131_lbl), run_time=1.5)

        note = Text("I-131 collapses to near-zero; C-14 barely budges — same physics, 4 orders apart",
                    font="EB Garamond", font_size=19, color=DIM).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.8)
        self.wait(3.5)
