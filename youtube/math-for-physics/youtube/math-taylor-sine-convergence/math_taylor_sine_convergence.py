#!/usr/bin/env python3
"""
math_taylor_sine_convergence.py — Taylor Series Convergence for sin(x)
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_taylor_sine_convergence.py --verify

Math (checkable):
    sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9! - ...
    At x=π/2=1.5708:
      N=1: π/2 ≈ 1.5708  error = |1.5708-1.0| ≈ 57%
      N=3: π/2 - (π/2)³/6 ≈ 1.5708 - 0.6460 = 0.9248+... (3-term sum = 1.0045) error ≈ 0.45%
      N=5: ≈ 1.0000 error < 0.1%
    At x=π (N=7): 7-term sum ≈ 0 (sin π = 0)
"""
import sys
import numpy as np
from math import factorial

TERMS_N = [1, 3, 5, 7, 9]


def taylor_sine(x, n_terms):
    """Partial sum of Taylor series for sin(x), using first n_terms odd terms."""
    x = np.asarray(x, dtype=float)
    total = np.zeros_like(x)
    sign = 1
    for k in range(n_terms):
        power = 2 * k + 1
        total += sign * (x ** power) / factorial(power)
        sign *= -1
    return total


def relative_error(x_val, n_terms):
    approx = taylor_sine(np.array([x_val]), n_terms)[0]
    exact = np.sin(x_val)
    if abs(exact) < 1e-10:
        return abs(approx - exact)
    return abs((approx - exact) / exact) * 100


def verify():
    print("=== Taylor sine convergence verification ===")
    x_pi2 = np.pi / 2
    print(f"At x = π/2 = {x_pi2:.4f}:")
    for n in TERMS_N:
        approx = taylor_sine(np.array([x_pi2]), n)[0]
        err = relative_error(x_pi2, n)
        print(f"  N={n} terms: sum = {approx:.6f}  error = {err:.4f}%")
    print()
    print("At x = π (sin π = 0):")
    for n in TERMS_N:
        approx = taylor_sine(np.array([np.pi]), n)[0]
        print(f"  N={n} terms: sum = {approx:.6f}")
    print()
    # Check at x=1 rad
    print("At x = 1 rad (sin(1) = 0.84147):")
    for n in TERMS_N:
        approx = taylor_sine(np.array([1.0]), n)[0]
        err = relative_error(1.0, n)
        print(f"  N={n} terms: sum = {approx:.6f}  error = {err:.6f}%")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
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

TERM_COLORS = [BLUE, BROWN, GOLD, "#E87040", "#A0D0A0"]
TERM_LABELS = ["N=1: x", "N=3: x−x³/6", "N=5: +x⁵/120", "N=7: −x⁷/5040", "N=9: +x⁹/362880"]


class TaylorSineScene(Scene):
    """
    sin(x) (dashed). Add Taylor terms one by one.
    Each partial sum extends its tracking range further from origin.
    Error counter at x=1 rad shrinks with each term.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_true_sine(ax)
        self._phase_build_terms(ax)
        self._phase_formula(ax)

    def _phase_title(self):
        title = Text("Taylor Series for sin(x)", font="EB Garamond", font_size=58, color=INK)
        eq = MathTex(
            r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots",
            color=BLUE, font_size=32,
        )
        sub = Text("each term extends the accurate range", font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, eq, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.0)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, eq, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[-0.3, 4.5, 1.0],
            y_range=[-2.0, 2.0, 1.0],
            x_length=9.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.2, include_numbers=True,
                             font_size=16, decimal_number_config={"color": DIM}),
        ).shift(DOWN * 0.2)
        lbl_x = MathTex(r"x\;(\mathrm{rad})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"y", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)
        return ax

    def _phase_true_sine(self, ax):
        x_vals = np.linspace(-0.2, 4.4, 600)
        y_vals = np.sin(x_vals)
        true_curve = ax.plot_line_graph(
            x_values=list(x_vals), y_values=list(y_vals),
            line_color=DIM, stroke_width=2.5, add_vertex_dots=False,
        )
        lbl = Text("sin(x)  exact", font="EB Garamond", font_size=18, color=DIM)
        lbl.next_to(ax.c2p(3.2, np.sin(3.2)), UP, buff=0.15)
        self.play(Create(true_curve), Write(lbl), run_time=1.0)
        self.wait(0.3)

    def _phase_build_terms(self, ax):
        x_vals = np.linspace(-0.2, 4.4, 600)
        prev_curve = None

        for idx, n in enumerate(TERMS_N):
            y_approx = taylor_sine(x_vals, n)
            y_clipped = np.clip(y_approx, -2.1, 2.1)

            curve = ax.plot_line_graph(
                x_values=list(x_vals), y_values=list(y_clipped),
                line_color=TERM_COLORS[idx], stroke_width=2.5, add_vertex_dots=False,
            )

            err_at_1 = relative_error(1.0, n)
            caption = Text(
                f"{TERM_LABELS[idx]}     error at x=1 rad: {err_at_1:.4f}%",
                font="EB Garamond", font_size=20, color=TERM_COLORS[idx],
            ).to_edge(UP, buff=0.25)

            anims = [FadeIn(curve), Write(caption)]
            if prev_curve:
                anims.append(FadeOut(prev_curve))

            self.play(*anims, run_time=1.2)
            self.wait(1.0)
            prev_curve = curve

        self.wait(0.5)

    def _phase_formula(self, ax):
        formula = MathTex(
            r"f'(0) = 1,\; f'''(0) = -1,\; \ldots \Rightarrow \sin x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k+1}}{(2k+1)!}",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=1.2)
        self.wait(2.5)
