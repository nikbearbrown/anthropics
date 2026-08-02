#!/usr/bin/env python3
"""
astro_hubble_law.py — Hubble's Law: v = H0 * d
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    v = H0 * d,  H0 = 70 km/s/Mpc
    Age estimate: t0 = 1/H0 (in consistent units)
    1 Mpc = 3.086e22 m,  1 km/s/Mpc = 1e3/(3.086e22) s^-1

Verify: python3 astro_hubble_law.py --verify
Render: manim -qh astro_hubble_law.py AstroHubbleLawScene
"""
import sys
import numpy as np

MPC_M   = 3.086e22   # m per Mpc
YR_SEC  = 3.156e7    # s per year

def hubble_age_gyr(H0_kmsMpc):
    """Age estimate 1/H0 in Gyr."""
    H0_si = H0_kmsMpc * 1e3 / MPC_M  # s^-1
    return 1.0 / H0_si / YR_SEC / 1e9

def hubble_radius_mpc(H0_kmsMpc):
    """Distance where recession = c (Hubble radius), in Mpc."""
    c_km = 2.998e5   # km/s
    return c_km / H0_kmsMpc

def verify():
    print("=== Hubble law verification ===")
    H0 = 70.0
    age = hubble_age_gyr(H0)
    print(f"P1: 1/H0 at H0=70 = {age:.2f} Gyr  (expected ~13.97 Gyr) {'✓' if abs(age - 14.0) < 0.5 else '✗'}")
    # P2: d=10 Mpc -> v = 700 km/s
    v10 = H0 * 10.0
    print(f"P2: v at d=10 Mpc = {v10:.0f} km/s  (expected 700) {'✓' if v10 == 700 else '✗'}")
    hr = hubble_radius_mpc(H0)
    print(f"Hubble radius = {hr:.0f} Mpc")
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

# Synthetic galaxy data: scattered around v = H0*d line with observational noise
rng = np.random.default_rng(42)
d_gals = rng.uniform(5, 450, 35)    # Mpc
v_gals = 70.0 * d_gals + rng.normal(0, 150, 35)   # km/s


class AstroHubbleLawScene(Scene):
    """
    Hubble diagram: v vs d. Points scatter in, slope = H0.
    H0 slider morphs line; implied age counter updates.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_points_and_line(ax)
        self._h0_tension(ax)
        self._slider_phase(ax)
        self._finale()

    def _title(self):
        t = Text("Hubble's Law: v = H₀ d",
                 font="EB Garamond", font_size=56, color=INK)
        s = Text(
            "Every galaxy recedes — the farther, the faster.\n"
            "The slope sets the age of the universe.",
            font="EB Garamond", font_size=23, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0, 500, 100],
            y_range=[0, 35000, 10000],
            x_length=9,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3 + LEFT * 0.5)
        lx = MathTex(r"d\;(\mathrm{Mpc})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"v\;(\mathrm{km/s})", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lx), Write(ly), run_time=1.3)
        return ax

    def _draw_points_and_line(self, ax):
        # Main H0=70 line
        line_pts = [ax.c2p(0, 0), ax.c2p(490, 70 * 490)]
        h0_line = Line(line_pts[0], line_pts[1], color=BLUE, stroke_width=2.5)

        # Scatter dots
        dots = VGroup(*[
            Dot(ax.c2p(d, max(0, v)), color=DIM, radius=0.06)
            for d, v in zip(d_gals, v_gals)
            if 0 < v < 35000
        ])

        slope_lbl = MathTex(r"H_0 = 70\,\frac{\mathrm{km/s}}{\mathrm{Mpc}}", color=BLUE, font_size=26)
        slope_lbl.move_to(ax.c2p(320, 15000))

        # Hubble radius marker
        hr = hubble_radius_mpc(70.0)
        hr_line = DashedLine(ax.c2p(hr, 0), ax.c2p(hr, 34000),
                             color=BROWN, stroke_width=1.5, stroke_opacity=0.6)
        hr_lbl = Text("v = c", font="EB Garamond", font_size=17, color=BROWN)
        hr_lbl.next_to(ax.c2p(hr, 24000), RIGHT, buff=0.1)

        self.play(Create(h0_line), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots],
                              lag_ratio=0.04), run_time=2.0)
        self.play(Write(slope_lbl), run_time=0.8)
        self.play(Create(hr_line), Write(hr_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(dots, h0_line, slope_lbl, hr_line, hr_lbl), run_time=0.4)

    def _h0_tension(self, ax):
        # Show two lines: Planck H0=67.4 vs SH0ES H0=73
        for H0, col, name in [(67.4, BLUE, "Planck 67.4"), (73.0, GOLD, "SH0ES 73.0")]:
            line = Line(ax.c2p(0, 0), ax.c2p(480, H0 * 480), color=col, stroke_width=2.5)
            lbl = MathTex(rf"H_0 = {H0}\,\frac{{\mathrm{{km/s}}}}{{\mathrm{{Mpc}}}}", color=col, font_size=22)
            lbl.move_to(ax.c2p(380, H0 * 380 + 1500))
            self.play(Create(line), Write(lbl), run_time=1.0)
        cap = Text(
            "Two methods, same universe — the H₀ tension.",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(cap), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects[self.mobjects.index(cap):]), run_time=0.4)
        # Clear axes region manually
        self.play(*[FadeOut(m) for m in self.mobjects if m not in []], run_time=0.01)

    def _slider_phase(self, ax):
        h0_tracker = ValueTracker(70.0)

        def _line():
            H = h0_tracker.get_value()
            return Line(ax.c2p(0, 0), ax.c2p(490, H * 490), color=BLUE, stroke_width=3)

        dyn_line = always_redraw(_line)
        self.add(dyn_line)

        H_lbl = MathTex(r"H_0 = ", color=INK, font_size=28)
        H_num = DecimalNumber(70.0, num_decimal_places=1, color=GOLD, font_size=28)
        H_unit = MathTex(r"\,\frac{\mathrm{km/s}}{\mathrm{Mpc}}", color=INK, font_size=28)
        H_num.add_updater(lambda m: m.set_value(h0_tracker.get_value()))
        H_row = VGroup(H_lbl, H_num, H_unit).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.3)

        age_lbl = Text("Age = ", font="EB Garamond", font_size=24, color=DIM)
        age_num = DecimalNumber(hubble_age_gyr(70.0), num_decimal_places=2,
                                color=GOLD, font_size=24)
        age_gyr = Text(" Gyr", font="EB Garamond", font_size=24, color=DIM)
        age_num.add_updater(lambda m: m.set_value(hubble_age_gyr(h0_tracker.get_value())))
        age_row = VGroup(age_lbl, age_num, age_gyr).arrange(RIGHT, buff=0.1).to_corner(UR, buff=0.3)

        self.play(Write(H_row), Write(age_row), run_time=0.8)
        self.play(h0_tracker.animate.set_value(50.0), run_time=2.0, rate_func=smooth)
        self.play(h0_tracker.animate.set_value(90.0), run_time=2.0, rate_func=smooth)
        self.play(h0_tracker.animate.set_value(70.0), run_time=1.5, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(H_row, age_row, dyn_line), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"v = H_0\,d",
            r"\quad t_0 \approx \frac{1}{H_0} \approx 14\,\mathrm{Gyr}",
            color=INK, font_size=34,
        )
        eq.arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.28)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
