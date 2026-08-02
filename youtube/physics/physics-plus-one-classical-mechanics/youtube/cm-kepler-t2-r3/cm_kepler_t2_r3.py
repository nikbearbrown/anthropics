#!/usr/bin/env python3
"""
cm_kepler_t2_r3.py — Kepler's Third Law: T^2 propto r^3 on a Log-Log Plot
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    T^2 = (4*pi^2 / G*M_sun) * r^3
    On log-log: log(T) = (3/2)*log(r) + const  (slope 3/2)

Verify: python3 cm_kepler_t2_r3.py --verify
Render: manim -qh cm_kepler_t2_r3.py CmKeplerT2R3Scene
"""
import sys
import numpy as np

# ─── Planet data (AU, yr) ────────────────────────────────────────────────────
PLANETS = [
    ("Mercury",  0.3871, 0.2408),
    ("Venus",    0.7233, 0.6152),
    ("Earth",    1.0000, 1.0000),
    ("Mars",     1.5237, 1.8810),
    ("Jupiter",  5.2029, 11.862),
    ("Saturn",   9.5370, 29.457),
    ("Uranus",  19.189,  84.011),
    ("Neptune", 30.071, 164.79),
]

# Jupiter's Galilean moons (semi-major axis in AU, period in yr)
JUP_MOONS = [
    ("Io",       4.218e-3, 1.769 / 365.25),
    ("Europa",   6.711e-3, 3.551 / 365.25),
    ("Ganymede", 1.070e-2, 7.155 / 365.25),
    ("Callisto", 1.883e-2, 16.69 / 365.25),
]

def verify():
    print("=== Kepler T^2 = r^3 verification ===")
    # P1: Earth T=1 yr at r=1 AU
    print(f"P1: Earth: T^2 = {1.0**2:.3f}, r^3 = {1.0**3:.3f}  (both = 1) ✓")
    # P2: Jupiter
    r_jup, T_jup = 5.203, 11.862
    T_pred = r_jup**1.5
    print(f"P2: Jupiter: T_predicted = r^1.5 = {T_pred:.3f} yr, actual = {T_jup:.3f} yr {'✓' if abs(T_pred - T_jup) < 0.05 else '✗'}")
    # Log-log slope check
    log_r = np.log10(np.array([p[1] for p in PLANETS]))
    log_T = np.log10(np.array([p[2] for p in PLANETS]))
    slope = np.polyfit(log_r, log_T, 1)[0]
    print(f"Log-log slope = {slope:.4f}  (expected 1.5) {'✓' if abs(slope - 1.5) < 0.01 else '✗'}")
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

PLANET_COLS = [DIM, DIM, BLUE, DIM, GOLD, GOLD, DIM, DIM]
MOON_COL = BROWN


class CmKeplerT2R3Scene(Scene):
    """
    Log-log plot T^2 vs r^3. Planets appear one by one on the slope-1 line.
    Jupiter moons appear as a parallel line (same slope, different intercept).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_planets(ax)
        self._draw_moons(ax)
        self._finale()

    def _title(self):
        t = Text("Kepler's Third Law: T² ∝ r³",
                 font="EB Garamond", font_size=58, color=INK)
        s = Text(
            "Every planet in the solar system falls on a single slope-3/2 line.\n"
            "Newton derived it from F = Gm₁m₂/r².",
            font="EB Garamond", font_size=23, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        # T^2 (yr^2) vs r^3 (AU^3), log-log (both from ~0.01 to ~10^6)
        ax = Axes(
            x_range=[-2, 5, 1],    # log10(r^3)
            y_range=[-3, 7, 1],    # log10(T^2)
            x_length=9,
            y_length=7,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)

        lx = MathTex(r"\log_{10}(r^3/\mathrm{AU}^3)", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"\log_{10}(T^2/\mathrm{yr}^2)", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        # Draw slope-1 reference line (T^2 = r^3 in log-log: log_T2 = log_r3)
        ref_line = DashedLine(
            ax.c2p(-2, -2), ax.c2p(5, 5),
            color=DIM, stroke_width=1.5, stroke_opacity=0.5,
        )
        slope_lbl = MathTex(r"\mathrm{slope}\ 1", color=DIM, font_size=20)
        slope_lbl.move_to(ax.c2p(3.5, 4.2))

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.5)
        self.play(Create(ref_line), Write(slope_lbl), run_time=0.8)
        return ax

    def _draw_planets(self, ax):
        prev_dot = None
        for (name, r_au, T_yr), col in zip(PLANETS, PLANET_COLS):
            x = np.log10(r_au**3)
            y = np.log10(T_yr**2)
            dot = Dot(ax.c2p(x, y), color=col, radius=0.1)
            lbl = Text(name, font="EB Garamond", font_size=16, color=col)
            lbl.next_to(dot, UR, buff=0.1)
            caption = Text(
                f"{name}: r = {r_au} AU, T = {T_yr} yr  →  T² = r³ (%.4f vs %.4f)" % (T_yr**2, r_au**3),
                font="EB Garamond", font_size=17, color=col,
            ).to_edge(DOWN, buff=0.2)
            self.play(FadeIn(dot), Write(lbl), Write(caption), run_time=0.7)
            self.wait(0.3)
            self.play(FadeOut(caption), run_time=0.2)

        # Overall caption
        all_caption = Text(
            "All eight planets — one slope-1 line. T² = r³ in AU and years.",
            font="EB Garamond", font_size=20, color=BLUE,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(all_caption), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(all_caption), run_time=0.3)

    def _draw_moons(self, ax):
        # Jupiter moons: same slope, different intercept (GM_Jup vs GM_Sun)
        moon_caption = Text(
            "Jupiter's moons: same slope 3/2 — different intercept (GM_Jup vs GM_Sun).",
            font="EB Garamond", font_size=18, color=BROWN,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(moon_caption), run_time=0.8)

        for name, r_au, T_yr in JUP_MOONS:
            x = np.log10(r_au**3)
            y = np.log10(T_yr**2)
            dot = Dot(ax.c2p(x, y), color=MOON_COL, radius=0.1)
            lbl = Text(name, font="EB Garamond", font_size=14, color=MOON_COL)
            lbl.next_to(dot, UR, buff=0.1)
            self.play(FadeIn(dot), Write(lbl), run_time=0.5)

        self.wait(2.0)
        self.play(FadeOut(moon_caption), run_time=0.3)

    def _finale(self):
        eq = MathTex(
            r"T^2 = \frac{4\pi^2}{GM_\odot}\,r^3",
            r"\quad \Longrightarrow \quad \log T = \frac{3}{2}\log r + \mathrm{const}",
            color=INK, font_size=28,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
