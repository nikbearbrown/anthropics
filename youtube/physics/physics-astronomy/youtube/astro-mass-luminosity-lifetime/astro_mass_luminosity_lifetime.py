#!/usr/bin/env python3
"""
astro_mass_luminosity_lifetime.py — Mass-Luminosity and Lifetime: Why Massive Stars Die Young
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-mass-luminosity-lifetime
    manim -qh astro_mass_luminosity_lifetime.py MassLuminosityLifetimeScene

Verify:
    python3 astro_mass_luminosity_lifetime.py

Physics:
    L ∝ M^3.5 (main-sequence mass-luminosity)
    t_MS = t_Sun × (M/M_Sun)^{-2.5}  (t_Sun = 10 Gyr)
    Concrete: 10 M_Sun → L=3162 L_Sun, t=32 Myr
"""
import sys
import numpy as np

T_SUN_GYR = 10.0  # Gyr


def luminosity(M: float) -> float:
    """L/L_Sun = M^3.5."""
    return M**3.5


def lifetime_gyr(M: float) -> float:
    """t_MS in Gyr."""
    return T_SUN_GYR * M**(-2.5)


def verify():
    print("=== Mass-luminosity-lifetime verification ===")
    ms = [0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
    for M in ms:
        L = luminosity(M)
        t = lifetime_gyr(M)
        print(f"  M={M:5.1f} M_Sun: L={L:8.1f} L_Sun, t={t:8.2f} Gyr")

    # P1: 2 M_Sun L check
    L2 = luminosity(2.0)
    print(f"\nP1: L(2 M_Sun) = 2^3.5 = {L2:.2f} L_Sun  (card says 11.3)")

    # P2: t_MS(10 M_Sun)
    t10 = lifetime_gyr(10.0)
    print(f"P2: t(10 M_Sun) = {t10*1e3:.1f} Myr  (card says 32 Myr)")
    print("=== PASSED ===" if abs(L2 - 11.31) < 0.1 else "=== CHECK ===")


if __name__ == "__main__":
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


class MassLuminosityLifetimeScene(Scene):
    """
    Log-log plot: L vs M (slope 3.5) and t_MS vs M (slope -2.5).
    Data points for 0.5 to 30 M_Sun. Annotation for 10 M_Sun.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dual_plot()
        self._phase_payoff()

    def _phase_title(self):
        title = Text("Mass-Luminosity and Stellar Lifetime", font="EB Garamond",
                     font_size=52, color=INK)
        sub1 = Text(
            "A 10 M_Sun star has 10× the fuel and burns it 3000× faster.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"L \propto M^{3.5} \quad t_{\rm MS} \propto M^{-2.5}",
                       color=BLUE, font_size=30)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_dual_plot(self):
        M_arr = np.logspace(-0.3, 1.5, 200)  # 0.5 to ~32 M_Sun
        L_arr = luminosity(M_arr)
        t_arr = lifetime_gyr(M_arr)

        # Left: log L vs log M
        ax_L = Axes(
            x_range=[-0.35, 1.55, 0.5],
            y_range=[-1.0, 5.5, 1.0],
            x_length=5.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(LEFT * 3.3 + DOWN * 0.1)
        lbl_xL = MathTex(r"\log_{10}(M/M_\odot)", color=INK, font_size=17
                          ).next_to(ax_L.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_yL = MathTex(r"\log_{10}(L/L_\odot)", color=INK, font_size=17
                          ).next_to(ax_L.y_axis.get_end(), UP, buff=0.1)
        hdr_L  = Text("L vs M  (slope 3.5)", font="EB Garamond", font_size=18, color=DIM
                      ).next_to(ax_L, UP, buff=0.1)

        # Right: log t vs log M
        ax_t = Axes(
            x_range=[-0.35, 1.55, 0.5],
            y_range=[-3.5, 1.5, 1.0],
            x_length=5.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(RIGHT * 3.3 + DOWN * 0.1)
        lbl_xt = MathTex(r"\log_{10}(M/M_\odot)", color=INK, font_size=17
                          ).next_to(ax_t.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_yt = MathTex(r"\log_{10}(t_{\rm MS}/\mathrm{Gyr})", color=INK, font_size=17
                          ).next_to(ax_t.y_axis.get_end(), UP, buff=0.1)
        hdr_t  = Text("t_MS vs M  (slope -2.5)", font="EB Garamond", font_size=18, color=DIM
                      ).next_to(ax_t, UP, buff=0.1)

        self.play(Create(ax_L), Create(ax_t),
                  Write(lbl_xL), Write(lbl_yL), Write(hdr_L),
                  Write(lbl_xt), Write(lbl_yt), Write(hdr_t), run_time=1.8)

        # L line
        c_L = VMobject(color=BLUE, stroke_width=3.5)
        c_L.set_points_smoothly([ax_L.c2p(np.log10(M), np.log10(L))
                                  for M, L in zip(M_arr, L_arr)])
        # t line
        c_t = VMobject(color=BROWN, stroke_width=3.5)
        c_t.set_points_smoothly([ax_t.c2p(np.log10(M), np.log10(t))
                                   for M, t in zip(M_arr, t_arr)])

        self.play(Create(c_L), Create(c_t), run_time=1.5)

        # Data points
        data_Ms = [0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
        for M in data_Ms:
            dL = Dot(ax_L.c2p(np.log10(M), np.log10(luminosity(M))), radius=0.1, color=GOLD)
            dt = Dot(ax_t.c2p(np.log10(M), np.log10(lifetime_gyr(M))), radius=0.1, color=GOLD)
            self.play(FadeIn(dL), FadeIn(dt), run_time=0.4)

        # Highlight M=10 with connecting dashed vertical
        M10 = 10.0
        dL10 = Dot(ax_L.c2p(np.log10(M10), np.log10(luminosity(M10))), radius=0.13, color=GOLD)
        dt10 = Dot(ax_t.c2p(np.log10(M10), np.log10(lifetime_gyr(M10))), radius=0.13, color=GOLD)
        ann_L = Text("L=3162 L_Sun", font="EB Garamond", font_size=16, color=GOLD
                     ).next_to(dL10, UR, buff=0.05)
        ann_t = Text("t=32 Myr", font="EB Garamond", font_size=16, color=GOLD
                     ).next_to(dt10, DR, buff=0.05)
        self.play(FadeIn(dL10), FadeIn(dt10), Write(ann_L), Write(ann_t), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_payoff(self):
        eq = MathTex(
            r"10\,M_\odot:\;L = 3162\,L_\odot,\;t = 32\,\mathrm{Myr}",
            color=INK, font_size=28,
        ).center().shift(UP * 1.0)
        note = Text(
            "The Milky Way has completed 250 such lifetimes since it formed.",
            font="EB Garamond", font_size=21, color=DIM,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "Massive stars are profligate — they manufacture heavy elements and die fast.",
            font="EB Garamond", font_size=20, color=BLUE,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
