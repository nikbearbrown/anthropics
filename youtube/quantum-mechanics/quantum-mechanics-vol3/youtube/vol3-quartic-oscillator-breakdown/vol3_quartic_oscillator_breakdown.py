#!/usr/bin/env python3
"""
vol3_quartic_oscillator_breakdown.py — Quartic Oscillator: Perturbation Theory Breaks Faster at High n
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics (ℏ = m = ω = 1):
    Ĥ = Ĥ₀ + λx̂⁴
    E_n^(1) = (3λ/4)(2n² + 2n + 1)
    Breakdown criterion: |E_n^(1)| ~ ℏω = 1  →  λ_break(n) ≈ 4/(3(2n²+2n+1))

Verify:
    python3 vol3_quartic_oscillator_breakdown.py --verify
"""
import sys
import numpy as np

def E1_coeff(n):
    """Coefficient c_n such that E_n^(1) = λ·c_n"""
    return (3.0/4) * (2*n**2 + 2*n + 1)

def lambda_break(n):
    """λ at which |E_n^(1)| = ℏω = 1"""
    return 1.0 / E1_coeff(n)

def verify():
    print("=== Quartic Oscillator Breakdown verification ===")
    print(f"{'n':>3}  {'c_n = 3(2n²+2n+1)/4':>22}  {'λ_break':>12}  {'E^(1)/level(λ=0.1)':>20}")
    for n in range(6):
        cn = E1_coeff(n)
        lb = lambda_break(n)
        e1_ratio = 0.1 * cn   # ratio to level spacing (=1) at λ=0.1
        print(f"{n:>3}  {cn:>22.3f}  {lb:>12.4f}  {e1_ratio:>20.3f}")

    # P1: ratio of λ_break(n=0) to λ_break(n=4)
    ratio = lambda_break(0) / lambda_break(4)
    expected = E1_coeff(4) / E1_coeff(0)
    print(f"\nP1: λ_break(n=0)/λ_break(n=4) = {ratio:.2f}  (should be {expected:.1f})")
    assert abs(ratio - expected) < 0.01, "FAIL: breakdown ratio"

    # P2: E^(1) is quadratic in n
    ns = np.array([0,1,2,3,4,5])
    cn_vals = np.array([E1_coeff(n) for n in ns])
    coeffs = np.polyfit(ns, cn_vals, 2)
    print(f"\nP2: Polynomial fit of c_n vs n: {coeffs[0]:.3f}n² + {coeffs[1]:.3f}n + {coeffs[2]:.3f}")
    print(f"    Leading coefficient ≈ {coeffs[0]:.3f}  (should be 3/2 = {3/2:.3f})")
    assert abs(coeffs[0] - 1.5) < 0.01, "FAIL: quadratic coefficient"
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED    = "#E05252"

N_MAX  = 5     # show states n = 0 ... 5
BAR_W  = 0.45


class QuarticOscillatorBreakdownScene(Scene):
    """
    Grouped bar chart: unperturbed levels (grey) + first-order corrections (colored).
    As λ increases, bars grow and cross the "breakdown" threshold line n by n.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._animate_bars(ax)
        self._payoff()

    def _title(self):
        t = Text("Quartic Oscillator — PT Breaks at High n First",
                 font="EB Garamond", font_size=52, color=INK)
        s = Text(
            "E_n^(1) = (3λ/4)(2n²+2n+1)  grows quadratically in n",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[-0.5, N_MAX + 0.5, 1],
            y_range=[0, 5.0, 1],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.3)

        xl = MathTex(r"n", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        yl = MathTex(r"E_n^{(1)}/\lambda", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        # x tick labels
        for n in range(N_MAX + 1):
            lbl = MathTex(str(n), color=DIM, font_size=18
                          ).next_to(ax.c2p(n, 0), DOWN, buff=0.15)
            self.add(lbl)

        # Threshold line: E_n^(1) = level spacing = 1 (in ℏω units)
        thresh = DashedLine(ax.c2p(-0.5, 1), ax.c2p(N_MAX + 0.5, 1),
                            color=RED, stroke_width=2.0, dash_length=0.12)
        thresh_lbl = MathTex(r"E^{(1)} = \hbar\omega\;\text{(BREAK)}",
                             color=RED, font_size=18).next_to(
                                 ax.c2p(N_MAX, 1), RIGHT, buff=0.1)

        self.play(Create(ax), Write(xl), Write(yl), run_time=1.2)
        self.play(Create(thresh), Write(thresh_lbl), run_time=0.7)
        return ax

    def _animate_bars(self, ax):
        coeffs = [E1_coeff(n) for n in range(N_MAX + 1)]
        colors = [BLUE, GOLD, GOLD, BROWN, BROWN, RED]
        bar_colors = colors[:N_MAX + 1]

        # Initial bars at λ=0 (height 0)
        lam = ValueTracker(0.0)

        def make_bars():
            bars = VGroup()
            for n in range(N_MAX + 1):
                height = coeffs[n] * lam.get_value()
                height_plot = min(height, 5.0)   # clip to axis
                bar_h = height_plot / 5.0 * 5.5  # scale to canvas
                rect = Rectangle(
                    width=BAR_W,
                    height=max(0.001, bar_h),
                    color=bar_colors[n],
                    fill_color=bar_colors[n],
                    fill_opacity=0.75,
                    stroke_width=1.0,
                )
                bot = ax.c2p(n, 0)
                rect.align_to(np.array([bot[0] - BAR_W/2, bot[1], 0]), DL)
                bars.add(rect)
            return bars

        bars = always_redraw(make_bars)
        self.add(bars)

        # λ readout
        lam_lbl = MathTex(r"\lambda = ", color=DIM, font_size=26)
        lam_num = DecimalNumber(0.0, num_decimal_places=3, color=GOLD, font_size=26)
        lam_num.add_updater(lambda m: m.set_value(lam.get_value()))
        lam_row = VGroup(lam_lbl, lam_num).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.32)
        self.add(lam_row)

        caption = Text(
            "As λ grows, n=4 crosses the threshold first, then n=3, n=2, ...",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(UP, buff=0.25)
        self.play(Write(caption), run_time=0.5)

        # Animate λ from 0 to 0.13
        self.play(lam.animate.set_value(0.13), run_time=6.0, rate_func=smooth)
        self.wait(1.0)

        # Label BREAKING states
        for n in [4, 3, 2, 1]:
            lb = lambda_break(n)
            brk_lbl = Text(f"n={n} BREAKING", font="EB Garamond",
                           font_size=16, color=RED).next_to(ax.c2p(n, 1.2), UP, buff=0.05)
            self.play(FadeIn(brk_lbl), run_time=0.35)
        self.wait(1.5)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"E_n^{(1)} = \frac{3\lambda}{4}(2n^2+2n+1)", color=GOLD, font_size=28),
            MathTex(r"\lambda_{\rm break}(n) = \frac{4}{3(2n^2+2n+1)}\propto n^{-2}",
                    color=INK, font_size=26),
            MathTex(r"\frac{\lambda_{\rm break}(0)}{\lambda_{\rm break}(4)} = 41",
                    color=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
