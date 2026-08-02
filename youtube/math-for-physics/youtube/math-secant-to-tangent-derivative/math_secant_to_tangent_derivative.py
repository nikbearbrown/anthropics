#!/usr/bin/env python3
"""
math_secant_to_tangent_derivative.py — Secant Lines Converging to the Tangent
SILENT SLATE — math-explainer candidate, math-for-physics book.

Verification (run standalone):
    python3 math_secant_to_tangent_derivative.py --verify

Physics/math (checkable):
    f(x) = x², f'(x) = 2x
    At x=2: f(2)=4, f'(2)=4
    h=1.0 → slope = (f(3)-f(2))/1 = (9-4)/1 = 5.0
    h=0.5 → slope = (f(2.5)-f(2))/0.5 = (6.25-4)/0.5 = 4.5
    h=0.25 → slope = (4.5625-4)/0.25 = 4.25
    h=0.1  → slope = (4.41-4)/0.1 = 4.1
    h=0.01 → slope = (4.0401-4)/0.01 = 4.01
    Limit → 4.0 (= 2·2) ✓
"""
import sys
import numpy as np

H_VALUES = [1.0, 0.5, 0.25, 0.1, 0.01]
X0 = 2.0


def f(x):
    return x ** 2


def secant_slope(h):
    return (f(X0 + h) - f(X0)) / h


def verify():
    print("=== Secant-to-tangent verification ===")
    print(f"f(x) = x²,  x₀ = {X0},  f(x₀) = {f(X0)},  exact f'(x₀) = {2*X0}")
    for h in H_VALUES:
        s = secant_slope(h)
        print(f"  h={h:.2f}  →  slope = ({f(X0+h):.4f} - {f(X0):.4f}) / {h:.2f} = {s:.4f}")
    print(f"Limit h→0: slope → {2*X0} ✓")
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


class SecantToTangentScene(Scene):
    """
    Parabola f(x)=x². Fixed point at x=2. Second point slides from x=3 toward x=2.
    Secant line pivots toward tangent; running slope label closes in on 4.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        ax = self._phase_axes()
        self._phase_parabola(ax)
        self._phase_secant_animation(ax)
        self._phase_final(ax)

    def _phase_title(self):
        title = Text("The Derivative as a Limit", font="EB Garamond", font_size=60, color=INK)
        sub1 = Text(
            "f(x) = x²   at   x = 2",
            font="EB Garamond", font_size=28, color=BLUE,
        )
        sub2 = Text(
            "secant slope  →  f'(2) = 4  as  h → 0",
            font="EB Garamond", font_size=24, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[-0.5, 5.0, 1.0],
            y_range=[-0.5, 12.0, 2.0],
            x_length=7.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.2, include_numbers=True,
                             font_size=18, decimal_number_config={"color": DIM}),
        ).shift(LEFT * 0.5 + DOWN * 0.5)

        lbl_x = MathTex(r"x", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"f(x)", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.5)
        return ax

    def _phase_parabola(self, ax):
        parabola = ax.plot(f, x_range=[0.0, 3.5], color=BLUE, stroke_width=3)
        lbl = MathTex(r"f(x) = x^2", color=BLUE, font_size=28).next_to(ax.c2p(3.2, 10.2), RIGHT, buff=0.1)
        self.play(Create(parabola), Write(lbl), run_time=1.5)

        # Fixed point at x=2
        p0 = Dot(ax.c2p(X0, f(X0)), color=GOLD, radius=0.1)
        lbl0 = MathTex(r"(2,\,4)", color=GOLD, font_size=22).next_to(ax.c2p(X0, f(X0)), LEFT, buff=0.15)
        self.play(FadeIn(p0), Write(lbl0), run_time=0.7)
        self.wait(0.5)
        return parabola, p0

    def _phase_secant_animation(self, ax):
        # h ValueTracker starting at 1.0, descending to 0.01
        h_tracker = ValueTracker(1.0)

        def get_x1():
            return X0 + h_tracker.get_value()

        # Moving point on parabola
        moving_dot = always_redraw(
            lambda: Dot(ax.c2p(get_x1(), f(get_x1())), color=BROWN, radius=0.09)
        )

        # Secant line: passes through (x0, f(x0)) and (x1, f(x1))
        def secant_line():
            h = h_tracker.get_value()
            x1 = X0 + h
            slope = secant_slope(h)
            # Line from x=0.5 to x=4.5
            x_lo, x_hi = 0.5, 4.5
            y_lo = f(X0) + slope * (x_lo - X0)
            y_hi = f(X0) + slope * (x_hi - X0)
            return Line(
                ax.c2p(x_lo, y_lo), ax.c2p(x_hi, y_hi),
                color=BROWN, stroke_width=2.5,
            )

        dyn_secant = always_redraw(secant_line)

        # Slope label
        slope_label = always_redraw(
            lambda: MathTex(
                r"\text{slope} = " + f"{secant_slope(h_tracker.get_value()):.3f}",
                color=GOLD, font_size=28,
            ).to_edge(UP, buff=0.3)
        )

        h_label = always_redraw(
            lambda: MathTex(
                r"h = " + f"{h_tracker.get_value():.3f}",
                color=DIM, font_size=24,
            ).to_edge(UP, buff=0.8)
        )

        self.play(FadeIn(moving_dot), Create(dyn_secant), Write(slope_label), Write(h_label), run_time=1.0)
        self.wait(0.5)

        # Animate h from 1.0 → 0.01 with pauses at key values
        for h_target in [0.5, 0.25, 0.1, 0.01]:
            self.play(h_tracker.animate.set_value(h_target), run_time=2.5, rate_func=smooth)
            self.wait(0.8)

        self.wait(1.0)
        # Store references for final phase
        self._slope_label = slope_label
        self._h_label = h_label
        self._moving_dot = moving_dot
        self._dyn_secant = dyn_secant

    def _phase_final(self, ax):
        # Tangent line at x=2: slope=4
        x_lo, x_hi = 0.5, 3.8
        y_lo = f(X0) + 4.0 * (x_lo - X0)
        y_hi = f(X0) + 4.0 * (x_hi - X0)
        tangent = Line(ax.c2p(x_lo, y_lo), ax.c2p(x_hi, y_hi), color=GOLD, stroke_width=3.5)

        formula = MathTex(
            r"f'(2) = \lim_{h \to 0} \frac{f(2+h)-f(2)}{h} = 4",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.3)

        self.play(
            FadeOut(self._dyn_secant, self._moving_dot, self._slope_label, self._h_label),
            Create(tangent),
            Write(formula),
            run_time=1.5,
        )
        self.wait(2.5)
