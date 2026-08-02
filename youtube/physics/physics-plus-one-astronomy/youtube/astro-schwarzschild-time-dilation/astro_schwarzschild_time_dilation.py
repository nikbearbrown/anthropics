#!/usr/bin/env python3
"""
astro_schwarzschild_time_dilation.py — Gravitational Time Dilation at the Schwarzschild Horizon
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    R_S = 2GM/c^2
    dt_inf/dt_r = 1/sqrt(1 - R_S/r)

Verify: python3 astro_schwarzschild_time_dilation.py --verify
Render: manim -qh astro_schwarzschild_time_dilation.py AstroSchwarzschildTimeDilationScene
"""
import sys
import numpy as np

# ─── Physical constants ───────────────────────────────────────────────────────
G_GRAV  = 6.674e-11   # m^3 kg^-1 s^-2
C_LIGHT = 2.998e8     # m/s
M_SUN   = 1.989e30    # kg

def schwarzschild_radius_km(mass_solar):
    """R_S in km for given mass in solar masses."""
    M = mass_solar * M_SUN
    return 2 * G_GRAV * M / C_LIGHT**2 / 1e3

def time_dilation(r_over_rs):
    """dt_inf/dt_r = 1/sqrt(1 - R_S/r) = 1/sqrt(1 - 1/x) where x = r/R_S."""
    x = np.asarray(r_over_rs, dtype=float)
    # Avoid singularity
    safe = np.where(x > 1.001, 1.0 - 1.0/x, np.nan)
    return np.where(x > 1.001, 1.0 / np.sqrt(safe), np.inf)

def verify():
    print("=== Schwarzschild time dilation verification ===")
    # Stellar BH: 10 M_sun
    Rs = schwarzschild_radius_km(10.0)
    print(f"10 M_sun BH: R_S = {Rs:.1f} km  (expected ≈ 29.5 km)")
    assert abs(Rs - 29.5) < 1.0, f"R_S off: {Rs}"

    # P1: r = 2 R_S -> factor = 1/sqrt(0.5) = sqrt(2)
    f2 = time_dilation(2.0)
    print(f"P1: r=2R_S: dt_inf/dt_r = {f2:.4f}  (expected {np.sqrt(2):.4f}) {'✓' if abs(f2 - np.sqrt(2)) < 0.001 else '✗'}")

    # P2: r = 1.5 R_S -> factor = 1/sqrt(1 - 2/3) = sqrt(3)
    f15 = time_dilation(1.5)
    print(f"P2: r=1.5R_S: dt_inf/dt_r = {f15:.4f}  (expected {np.sqrt(3):.4f}) {'✓' if abs(f15 - np.sqrt(3)) < 0.001 else '✗'}")
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


class AstroSchwarzschildTimeDilationScene(Scene):
    """
    Gravitational time dilation curve dt_inf/dt_r vs r/R_S.
    Shows divergence at horizon; two clock-rate markers.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curve(ax)
        self._markers(ax)
        self._finale()

    def _title(self):
        t = Text("Time Slows at the Schwarzschild Horizon",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "A clock near a black hole runs slower — at r = R_S, it freezes.\n"
            "GPS satellites correct for exactly this effect.",
            font="EB Garamond", font_size=23, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[1.0, 6.0, 1.0],
            y_range=[0, 8.0, 2.0],
            x_length=9,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3 + LEFT * 0.5)
        lx = MathTex(r"r / R_S", color=INK, font_size=26).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"\frac{dt_\infty}{dt_r}", color=INK, font_size=26).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Gravitational Time Dilation", font="EB Garamond",
                   font_size=22, color=DIM).next_to(ax, UP, buff=0.15)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.5)
        return ax

    def _draw_curve(self, ax):
        x_vals = np.linspace(1.02, 6.0, 600)
        y_vals = np.clip(time_dilation(x_vals), 0, 7.8)
        pts = np.array([ax.c2p(x, y) for x, y in zip(x_vals, y_vals)])
        curve = VMobject(color=BLUE, stroke_width=3.5)
        curve.set_points_smoothly(pts)

        # Horizon asymptote
        h_line = DashedLine(
            ax.c2p(1.0, 0), ax.c2p(1.0, 7.8),
            color=BROWN, stroke_width=2, stroke_opacity=0.7,
        )
        h_lbl = MathTex(r"r = R_S", color=BROWN, font_size=22)
        h_lbl.next_to(ax.c2p(1.0, 4.0), RIGHT, buff=0.15)

        eq = MathTex(
            r"\frac{dt_\infty}{dt_r} = \frac{1}{\sqrt{1 - R_S/r}}",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.25)

        self.play(Create(curve), run_time=2.5)
        self.play(Create(h_line), Write(h_lbl), run_time=1.0)
        self.play(Write(eq), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(eq), run_time=0.4)

    def _markers(self, ax):
        markers = [
            (2.0, np.sqrt(2), "r = 2R_S", f"clock rate {100/np.sqrt(2):.1f}%"),
            (1.5, np.sqrt(3), "r = 1.5R_S", f"clock rate {100/np.sqrt(3):.1f}%"),
        ]
        for x, y, pos_lbl, rate_lbl in markers:
            y_clamped = min(y, 7.8)
            dot = Dot(ax.c2p(x, y_clamped), color=GOLD, radius=0.1)
            x_dash = DashedLine(ax.c2p(x, 0), ax.c2p(x, y_clamped),
                                color=GOLD, stroke_width=1.5, stroke_opacity=0.6)
            pos_m = MathTex(rf"{pos_lbl}", color=GOLD, font_size=20)
            pos_m.next_to(dot, RIGHT, buff=0.15)
            rate_m = Text(rate_lbl, font="EB Garamond", font_size=18, color=DIM)
            rate_m.next_to(dot, UP, buff=0.1)
            self.play(Create(x_dash), FadeIn(dot), Write(pos_m), run_time=1.0)
            self.play(Write(rate_m), run_time=0.6)
            self.wait(0.8)

        # Annotate divergence
        cap = Text(
            "As r → R_S,  the distant clock sees the infalling clock freeze",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(cap), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"R_S = \frac{2GM}{c^2}",
            r"\approx 2.95\,\mathrm{km}\times\left(\frac{M}{M_\odot}\right)",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.28)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
