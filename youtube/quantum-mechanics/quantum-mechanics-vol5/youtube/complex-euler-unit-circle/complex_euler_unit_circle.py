#!/usr/bin/env python3
"""
complex_euler_unit_circle.py — Euler's Formula: e^{iθ} Traces the Unit Circle
SILENT — math-explainer candidate, quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/complex-euler-unit-circle
    manim -qh complex_euler_unit_circle.py ComplexEulerUnitCircleScene

Verify:
    python3 complex_euler_unit_circle.py --verify

Physics:
    e^{iθ} = Σ_{n=0}^{N} (iθ)^n / n!
    At θ = π/2: partial sums converge to (0, 1)
    At θ = π:   partial sums converge to (−1, 0)   [Euler's identity]
    |e^{iθ}| = 1 for all real θ
"""
import sys
import numpy as np
from math import factorial

# ─── Verification (numpy only) ───────────────────────────────────────────────

def euler_partial_sum(theta: float, N: int) -> complex:
    """Taylor partial sum of e^{iθ} to order N."""
    result = 0j
    for n in range(N + 1):
        result += (1j * theta) ** n / factorial(n)
    return result


def verify():
    print("=== Euler unit circle verification ===")
    # P1: at θ=π, partial sums converge to -1
    for N in [1, 5, 10, 20, 50]:
        z = euler_partial_sum(np.pi, N)
        print(f"  N={N:2d}: e^{{iπ}} ≈ {z.real:.6f} + {z.imag:.6f}i  |z|={abs(z):.6f}")
    exact = np.exp(1j * np.pi)
    print(f"  exact: {exact.real:.6f} + {exact.imag:.6f}i")
    print()
    # P2: |e^{iθ}| = 1 for a sweep of θ
    thetas = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi, 3*np.pi/2]
    for th in thetas:
        z = np.exp(1j * th)
        print(f"  θ={th/np.pi:.3f}π: |e^{{iθ}}| = {abs(z):.10f}  (should be 1.0)")
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


class ComplexEulerUnitCircleScene(Scene):
    """
    Euler's formula: e^{iθ} sweeps the unit circle.
    Phases:
      1. Title card
      2. Complex plane + unit circle
      3. Taylor partial sums build toward e^{iπ/2} = i  (each term an arrow)
      4. Full sweep θ: 0 → 2π tracing the circle
      5. Decaying spiral e^{(−γ+iω)t} morph
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax, circle = self._phase_axes()
        self._phase_partial_sums(ax)
        self._phase_full_sweep(ax, circle)
        self._phase_decay_morph(ax)

    # ── Phase 1: Title ────────────────────────────────────────────────────────

    def _phase_title(self):
        title = Text("Euler's Formula", font="EB Garamond", font_size=64, color=INK)
        sub1  = Text(
            "e^{iθ} = cos θ + i sin θ  —  algebra forces a perfect circle",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Taylor series: even terms → real axis  ·  odd terms → imaginary axis",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    # ── Phase 2: Axes + unit circle ───────────────────────────────────────────

    def _phase_axes(self):
        ax = ComplexPlane(
            x_range=[-1.8, 1.8, 0.5],
            y_range=[-1.8, 1.8, 0.5],
            x_length=6.5,
            y_length=6.5,
            background_line_style={"stroke_color": DIM, "stroke_width": 0.6},
            axis_config={"color": INK, "stroke_width": 1.5},
        ).shift(LEFT * 0.5)

        lbl_re = Text("Re", font="EB Garamond", font_size=40, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_im = Text("Im", font="EB Garamond", font_size=40, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        circle = Circle(radius=ax.get_x_unit_size(), color=DIM, stroke_width=1.5).move_to(ax.get_origin())

        self.play(Create(ax), Write(lbl_re), Write(lbl_im), run_time=1.5)
        self.play(Create(circle), run_time=1.0)
        self.add(circle)
        return ax, circle

    # ── Phase 3: Taylor partial sums toward θ = π/2 ───────────────────────────

    def _phase_partial_sums(self, ax):
        theta = np.pi / 2
        caption = Text(
            "Target: e^{iπ/2} = i = (0, 1)  —  adding one Taylor term at a time",
            font="EB Garamond", font_size=36, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(caption), run_time=0.8)

        origin = ax.get_origin()
        unit   = ax.get_x_unit_size()
        prev   = np.array([0.0, 0.0])   # real, imag running sum
        arrows = []
        for n in range(8):
            term_c = (1j * theta) ** n / factorial(n)
            term   = np.array([term_c.real, term_c.imag])
            new_pt = prev + term
            # Arrow from prev to new_pt in screen coords
            p0 = origin + np.array([prev[0] * unit, prev[1] * unit, 0])
            p1 = origin + np.array([new_pt[0] * unit, new_pt[1] * unit, 0])
            color = BLUE if n % 2 == 0 else BROWN
            arr = Arrow(p0, p1, buff=0, color=color, stroke_width=2.5, max_tip_length_to_length_ratio=0.25)
            lbl_n = MathTex(f"n={n}", color=color, font_size=18).next_to(p1, RIGHT if new_pt[0] >= 0 else LEFT, buff=0.08)
            self.play(Create(arr), FadeIn(lbl_n), run_time=0.6)
            arrows.append((arr, lbl_n))
            prev = new_pt.copy()

        # Dot at the final point
        final_pt = origin + np.array([prev[0] * unit, prev[1] * unit, 0])
        dot = Dot(final_pt, color=GOLD, radius=0.1)
        exact_lbl = MathTex(r"e^{i\pi/2} = i", color=GOLD, font_size=26).next_to(dot, UR, buff=0.15)
        self.play(FadeIn(dot), Write(exact_lbl), run_time=0.8)
        self.wait(1.5)
        # Clean up partial sum arrows
        self.play(*[FadeOut(a) for a, l in arrows], *[FadeOut(l) for a, l in arrows],
                  FadeOut(dot, exact_lbl, caption), run_time=0.6)

    # ── Phase 4: Full sweep θ: 0 → 2π ────────────────────────────────────────

    def _phase_full_sweep(self, ax, circle):
        origin = ax.get_origin()
        unit   = ax.get_x_unit_size()
        tracker = ValueTracker(0.0)

        def _dot():
            th = tracker.get_value()
            z  = np.exp(1j * th)
            pt = origin + np.array([z.real * unit, z.imag * unit, 0])
            return Dot(pt, color=GOLD, radius=0.09)

        def _line():
            th = tracker.get_value()
            z  = np.exp(1j * th)
            pt = origin + np.array([z.real * unit, z.imag * unit, 0])
            return Line(origin, pt, color=BLUE, stroke_width=2.5)

        def _theta_lbl():
            th = tracker.get_value()
            return MathTex(
                rf"\theta = {th/np.pi:.2f}\pi",
                color=INK, font_size=40,
            ).to_corner(UR, buff=0.35)

        dyn_dot  = always_redraw(_dot)
        dyn_line = always_redraw(_line)
        dyn_lbl  = always_redraw(_theta_lbl)

        hdr = Text(
            "Sweep θ from 0 to 2π — the locus is exactly the unit circle",
            font="EB Garamond", font_size=36, color=INK,
        ).to_edge(DOWN, buff=0.22)

        self.add(dyn_dot, dyn_line, dyn_lbl)
        self.play(Write(hdr), run_time=0.6)
        self.play(tracker.animate.set_value(2 * np.pi), run_time=5.0, rate_func=linear)
        self.wait(1.0)

        # Euler's identity callout
        euler_eq = MathTex(r"e^{i\pi} + 1 = 0", color=GOLD, font_size=42).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(hdr), Write(euler_eq), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(euler_eq, dyn_dot, dyn_line, dyn_lbl), run_time=0.5)

    # ── Phase 5: Decaying spiral ──────────────────────────────────────────────

    def _phase_decay_morph(self, ax):
        origin = ax.get_origin()
        unit   = ax.get_x_unit_size()
        gamma  = 0.25   # decay rate
        omega  = 2.5    # angular frequency

        T_max = 3 * np.pi   # animate for a few turns
        N_pts = 600
        ts    = np.linspace(0, T_max, N_pts)
        zs    = np.exp((-gamma + 1j * omega) * ts)

        pts = [origin + np.array([z.real * unit, z.imag * unit, 0]) for z in zs]
        spiral = VMobject(color=BROWN, stroke_width=2.5, stroke_opacity=0.85)
        spiral.set_points_smoothly(pts)

        hdr = Text(
            "Replace θ → −γt + iωt :  decaying oscillator spiral e^{(−γ + iω)t}",
            font="EB Garamond", font_size=19, color=BROWN,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(hdr), run_time=0.7)
        self.play(Create(spiral), run_time=3.5, rate_func=linear)
        self.wait(2.0)
        fin = Text(
            "Unit circle  →  inward spiral:  one formula, two physical regimes",
            font="EB Garamond", font_size=36, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(hdr), Write(fin), run_time=0.8)
        self.wait(2.5)
