#!/usr/bin/env python3
"""
double_slit_interference_fringe_spacing.py — Double-Slit Interference: Fringe Pattern as d Changes
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/double-slit-interference-fringe-spacing
    manim -qh double_slit_interference_fringe_spacing.py DoubleSlitInterferenceScene

Numpy verification (run standalone):
    python3 double_slit_interference_fringe_spacing.py --verify

Physics (checkable):
    I(y) = I₀ cos²(πdy / λL)  — fringe spacing Δy = λL/d

    P1: d=0.1mm, λ=550nm, L=1m → Δy = 550e-9×1/0.1e-3 = 5.5mm ✓
    P2: λ=633nm vs λ=405nm: ratio Δy_red/Δy_violet = 633/405 ≈ 1.562 ✓
"""
import sys
import numpy as np

LAMBDA = 550e-9   # m
L_M    = 1.0      # m


def fringe_spacing(d_m, lam=LAMBDA, L=L_M):
    return lam * L / d_m


def fringe_intensity(y_arr, d_m, lam=LAMBDA, L=L_M):
    """I(y)/I₀ = cos²(πdy / λL)"""
    return np.cos(np.pi * d_m * y_arr / (lam * L)) ** 2


def verify():
    print("=== Double-slit interference verification ===")
    # P1
    d = 0.1e-3
    dy = fringe_spacing(d)
    print(f"P1: d={d*1e3:.1f}mm, λ={LAMBDA*1e9:.0f}nm, L={L_M}m")
    print(f"    Δy = λL/d = {dy*1e3:.2f} mm  (should be 5.5 mm)")
    # P2
    dy_red = fringe_spacing(d, lam=633e-9)
    dy_vio = fringe_spacing(d, lam=405e-9)
    print(f"P2: Δy_red(633nm)/Δy_violet(405nm) = {dy_red/dy_vio:.3f}  (should be ≈1.562)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class DoubleSlitInterferenceScene(Scene):
    """
    Double-slit interference fringe pattern.
    As slit separation d increases: fringe spacing narrows (more fringes on screen).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_equation()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Double-Slit Interference", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "I(y) = I₀ cos²(πdy/λL)  ·  fringe spacing  Δy = λL/d",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "More separated slits  →  finer fringes  (anti-intuitive)",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_equation(self):
        eq = MathTex(
            r"I(y) = I_0 \cos^2\!\!\left(\frac{\pi d\, y}{\lambda L}\right)",
            r"\quad \Longrightarrow \quad",
            r"\Delta y = \frac{\lambda L}{d}",
            color=INK, font_size=38,
        )
        note = MathTex(
            r"\lambda = 550\,\text{nm},\; L = 1\,\text{m} \;\;\Rightarrow\;\; \Delta y \propto 1/d",
            color=BLUE, font_size=26,
        )
        VGroup(eq, note).arrange(DOWN, buff=0.5).center()
        self.play(Write(eq), run_time=1.4)
        self.play(Write(note), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(eq, note), run_time=0.4)

    def _phase_sweep(self):
        # Plot: x = screen position y (mm), y-axis = I/I₀
        y_range_mm = 20.0  # ±20 mm half-screen
        ax = Axes(
            x_range=[-y_range_mm, y_range_mm, 5],
            y_range=[0, 1.15, 0.25],
            x_length=11.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.15),
            x_axis_config=dict(numbers_to_include=[-15, -10, -5, 0, 5, 10, 15]),
            y_axis_config=dict(numbers_to_include=[0, 0.5, 1.0]),
        ).shift(UP * 0.3)

        lbl_x = MathTex(r"y\;\mathrm{(mm)}", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"I/I_0", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.4)

        slit_d_vals = [0.05e-3, 0.1e-3, 0.2e-3, 0.5e-3, 1.0e-3]
        colors = [INK, BLUE, GOLD, BROWN, DIM]

        y_m = np.linspace(-y_range_mm * 1e-3, y_range_mm * 1e-3, 2000)
        y_mm = y_m * 1e3

        curve = None
        live_lbl = None
        for i, d in enumerate(slit_d_vals):
            intensity = fringe_intensity(y_m, d)
            pts = [ax.c2p(ym, iv) for ym, iv in zip(y_mm, intensity)]
            new_curve = VMobject(color=colors[i], stroke_width=3.0)
            new_curve.set_points_smoothly(pts)

            dy_mm = fringe_spacing(d) * 1e3
            new_lbl = Text(
                f"d = {d*1e3:.2f} mm  ·  Δy = λL/d = {dy_mm:.1f} mm",
                font="EB Garamond", font_size=21, color=colors[i],
            ).to_edge(DOWN, buff=0.25)

            if curve is None:
                self.play(Create(new_curve), Write(new_lbl), run_time=1.8)
            else:
                self.play(
                    Transform(curve, new_curve),
                    FadeOut(live_lbl), Write(new_lbl),
                    run_time=1.6,
                )
            self.wait(0.9)
            curve = new_curve
            live_lbl = new_lbl

        # Payoff
        payoff = MathTex(
            r"\Delta y = \frac{\lambda L}{d} \;\;\; \Longrightarrow \;\;\; d\uparrow \;\; \Rightarrow \;\; \Delta y\downarrow \;\; (\text{fringes compress})",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(live_lbl), Write(payoff), run_time=1.2)
        self.wait(3.0)
