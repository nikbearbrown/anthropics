#!/usr/bin/env python3
"""
taylor_convergence_small_angle.py — Taylor Convergence and the Small-Angle Approximation
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/taylor-convergence-small-angle
    manim -qh taylor_convergence_small_angle.py TaylorConvergenceScene

Verify:
    python3 taylor_convergence_small_angle.py --verify

Physics:
    sin(x) = x − x³/6 + x⁵/120 − ...
    At x=0.262 rad (15°): N=1 error ≈ 1.2%
    At x=0.524 rad (30°): N=1 error ≈ 2.4%
    Cubic N=3: sin(30°) ≈ 0.500 to 0.02%
    At x=π/2: N=1 gives π/2 ≈ 1.571 vs 1.0 → 57% error
"""
import sys
import numpy as np
from math import factorial


def sin_taylor(x, N):
    """Taylor sum of sin(x) to order 2N-1."""
    total = 0.0
    for k in range(N):
        total += ((-1)**k) * x**(2*k+1) / factorial(2*k+1)
    return total


def verify():
    print("=== Taylor convergence verification ===")
    # P1: at x=π/2, N=1 gives 57% error
    x = np.pi / 2
    approx = sin_taylor(x, 1)
    exact  = np.sin(x)
    err    = abs(approx - exact) / abs(exact) * 100
    print(f"  x=π/2: N=1 approx={approx:.6f}, exact={exact:.6f}, error={err:.1f}%")

    # P2: cubic N=3 at 30°
    x30 = 30 * np.pi / 180
    approx3 = sin_taylor(x30, 2)  # N=2 terms: x − x³/6
    exact30  = np.sin(x30)
    err30    = abs(approx3 - exact30) / abs(exact30) * 100
    print(f"  x=30°: N=3(cubic) approx={approx3:.6f}, exact={exact30:.6f}, error={err30:.4f}%")

    print("\n  Small-angle 1% threshold:")
    for x_deg in [5, 10, 14, 15, 20, 30]:
        x = x_deg * np.pi / 180
        err_lin = abs(x - np.sin(x)) / np.sin(x) * 100
        print(f"    {x_deg}°: linear error = {err_lin:.3f}%")
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


class TaylorConvergenceScene(Scene):
    """
    Phase 1: title
    Phase 2: sin(x) in blue; add polynomial terms one by one; shaded 1% band
    Phase 3: error plot — linear vs cubic at various angles
    Phase 4: 57% failure at x=π/2
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_polynomial_buildup()
        self._phase_error_plot()

    def _phase_title(self):
        title = Text("Taylor Convergence", font="EB Garamond", font_size=60, color=INK)
        sub1  = Text(
            "sin(x) = x − x³/6 + x⁵/120 − …  with quantifiable error bounds",
            font="EB Garamond", font_size=23, color=BLUE,
        )
        sub2  = Text(
            "Small-angle approx (sin x ≈ x) valid to 1% for |x| < 0.244 rad",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_polynomial_buildup(self):
        ax = Axes(
            x_range=[0, np.pi, np.pi/4],
            y_range=[-0.1, 1.2, 0.25],
            x_length=9.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).shift(UP * 0.2)

        x_lbl = MathTex(r"x\;\mathrm{(rad)}", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(x_lbl), run_time=0.8)

        # Exact sin(x)
        sin_curve = ax.plot(np.sin, x_range=[0, np.pi], color=BLUE, stroke_width=3.0)
        sin_lbl   = MathTex(r"\sin(x)", color=BLUE, font_size=24).next_to(ax.c2p(2.3, 0.75), UP, buff=0.1)
        self.play(Create(sin_curve), Write(sin_lbl), run_time=1.0)

        # Taylor terms N=1,2,3,4
        poly_colors = [GOLD, BROWN, "#88CC44", "#CC88AA"]
        n_labels    = ["N=1: x", "N=3: x−x³/6", "N=5: x−x³/6+x⁵/120", "N=7"]

        prev_curves = []
        for i, (N, col, lbl_str) in enumerate(zip([1, 2, 3, 4], poly_colors, n_labels)):
            def _poly(x, N=N):
                return float(sin_taylor(x, N))
            try:
                curve = ax.plot(lambda x, N=N: sin_taylor(x, N), x_range=[0.01, np.pi - 0.01],
                                color=col, stroke_width=2.5, stroke_opacity=0.85)
            except Exception:
                continue
            lbl = Text(lbl_str, font="EB Garamond", font_size=18, color=col).to_corner(UR, buff=0.35).shift(DOWN * (0.5 * i))
            self.play(Create(curve), Write(lbl), run_time=0.8)
            prev_curves.append((curve, lbl))

        # 1% error band
        x_threshold = 0.244   # rad
        band_pts_lo = [ax.c2p(x, np.sin(x) * 0.99) for x in np.linspace(0, x_threshold, 50)]
        band_pts_hi = [ax.c2p(x, np.sin(x) * 1.01) for x in np.linspace(0, x_threshold, 50)]
        band = Polygon(*(band_pts_lo + band_pts_hi[::-1]),
                       color=GOLD, fill_color=GOLD, fill_opacity=0.15, stroke_width=0)
        threshold_line = DashedLine(ax.c2p(x_threshold, 0), ax.c2p(x_threshold, 1.1), color=GOLD, stroke_width=1.5)
        thresh_lbl = MathTex(r"0.244\,\mathrm{rad} \approx 14°", color=GOLD, font_size=20).next_to(
            ax.c2p(x_threshold, 1.05), UR, buff=0.1)
        self.play(FadeIn(band), Create(threshold_line), Write(thresh_lbl), run_time=0.8)

        note = Text("Shaded band: linear approximation within 1%",
                    font="EB Garamond", font_size=19, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.6)
        self.wait(2.0)
        self.play(*[FadeOut(c, l) for c, l in prev_curves],
                  FadeOut(ax, sin_curve, sin_lbl, band, threshold_line, thresh_lbl, note, x_lbl), run_time=0.5)

    def _phase_error_plot(self):
        ax = Axes(
            x_range=[0, 50, 10], y_range=[0, 60, 10],
            x_length=8.5, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).shift(UP * 0.3)
        x_lbl = MathTex(r"\theta\;(°)", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\%\;\mathrm{error}", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        degs = np.linspace(1, 50, 300)
        rads = degs * np.pi / 180

        err_lin = np.abs(rads - np.sin(rads)) / np.sin(rads) * 100
        err_cub = np.abs((rads - rads**3/6) - np.sin(rads)) / np.sin(rads) * 100

        pts_lin = [ax.c2p(d, min(e, 59.9)) for d, e in zip(degs, err_lin)]
        pts_cub = [ax.c2p(d, min(e, 59.9)) for d, e in zip(degs, err_cub)]

        c_lin = VMobject(color=GOLD, stroke_width=2.8)
        c_lin.set_points_smoothly(pts_lin)
        c_cub = VMobject(color=BLUE, stroke_width=2.8)
        c_cub.set_points_smoothly(pts_cub)

        lbl_lin = Text("N=1 (linear)", font="EB Garamond", font_size=20, color=GOLD).to_corner(UR, buff=0.35)
        lbl_cub = Text("N=3 (cubic)", font="EB Garamond", font_size=20, color=BLUE).to_corner(UR, buff=0.35).shift(DOWN*0.4)

        self.play(Create(c_lin), Write(lbl_lin), run_time=1.0)
        self.play(Create(c_cub), Write(lbl_cub), run_time=1.0)

        # 1% horizontal line
        line_1pct = DashedLine(ax.c2p(0, 1), ax.c2p(50, 1), color=DIM, stroke_width=1.5)
        lbl_1pct  = MathTex(r"1\%", color=DIM, font_size=18).next_to(ax.c2p(0, 1), LEFT, buff=0.1)
        self.play(Create(line_1pct), Write(lbl_1pct), run_time=0.6)

        fin = MathTex(
            r"\sin(30°)\approx 0.524 - \frac{0.524^3}{6} = 0.500\quad(\text{error } 0.02\%)",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=1.0)
        self.wait(2.5)
