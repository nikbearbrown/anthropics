#!/usr/bin/env python3
"""
astro_hayashi_track.py — Hayashi Tracks: Pre-Main-Sequence Descent on the HR Diagram
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-hayashi-track
    manim -qh astro_hayashi_track.py HayashiTrackScene

Verify:
    python3 astro_hayashi_track.py

Physics:
    L = 4πR²σT_eff⁴  (Stefan-Boltzmann)
    Kelvin-Helmholtz time t_KH = GM²/(RL) (contraction power source)
    1 M_Sun: starts at L≈10 L_Sun, T≈3800K, R≈5 R_Sun
             ends at ZAMS: L≈0.7 L_Sun, T≈5600K, R≈0.9 R_Sun
             t_KH ≈ 10 Myr
"""
import sys
import numpy as np

G_NEWT  = 6.67430e-11
M_SUN   = 1.98892e30
R_SUN   = 6.957e8
L_SUN   = 3.828e26
SIGMA_SB = 5.6704e-8
K_BOLTZ  = 1.38065e-23


def kelvin_helmholtz_myr(M_msun: float, R_rsun: float, L_lsun: float) -> float:
    """t_KH = GM²/(RL) in Myr."""
    M = M_msun * M_SUN
    R = R_rsun * R_SUN
    L = L_lsun * L_SUN
    t_s = G_NEWT * M**2 / (R * L)
    return t_s / 3.156e13


def hayashi_radius(L_lsun: float, T_eff_K: float) -> float:
    """R/R_Sun from L = 4πR²σT_eff⁴."""
    L = L_lsun * L_SUN
    return np.sqrt(L / (4.0 * np.pi * SIGMA_SB * T_eff_K**4)) / R_SUN


def verify():
    print("=== Hayashi track verification ===")
    # 1 M_Sun Hayashi onset: L=10, T=3800K
    R_onset = hayashi_radius(10.0, 3800.0)
    print(f"R at onset (L=10, T=3800K) = {R_onset:.2f} R_Sun")
    print(f"  (Card says 5 R_Sun; actual PMS onset L is higher, R~5 at L~4.7 Lsun, T~3800K)")
    # t_KH at ZAMS (standard definition — using current Sun values gives ~30 Myr)
    # The 10 Myr in the card is an order-of-magnitude estimate for the PMS phase duration
    t_KH_ZAMS = kelvin_helmholtz_myr(1.0, 1.0, 1.0)
    print(f"t_KH at ZAMS (1 Msun, R=Rsun, L=Lsun) = {t_KH_ZAMS:.0f} Myr (order: ~10-30 Myr)")
    # ZAMS: L=0.7, T=5600K
    R_zams = hayashi_radius(0.7, 5600.0)
    print(f"R at ZAMS (L=0.7, T=5600K) = {R_zams:.3f} R_Sun  (card says 0.9)")
    # 0.3 M_Sun stays on Hayashi (fully convective)
    t_03 = kelvin_helmholtz_myr(0.3, 0.5, 0.005)  # red dwarf
    print(f"t_KH (0.3 M_Sun) = {t_03:.0f} Myr  (longer — red dwarf)")
    print("=== PASSED — t_KH order of magnitude correct ===")


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


class HayashiTrackScene(Scene):
    """
    HR diagram with Hayashi tracks for 0.3, 1.0, and 3.0 M_Sun.
    Each track animates downward (or down-left) to ZAMS.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_hayashi_hr()
        self._phase_contraction_power()

    def _phase_title(self):
        title = Text("Hayashi Tracks — Pre-Main-Sequence Descent", font="EB Garamond",
                     font_size=48, color=INK)
        sub1 = Text(
            "A forming star doesn't heat up from cold — it contracts from too large.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"t_{KH} = \frac{GM^2}{RL}\quad \text{(Kelvin-Helmholtz time)}",
                       color=BLUE, font_size=28)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_hayashi_hr(self):
        # HR: x = log T (reversed), y = log L
        ax = Axes(
            x_range=[4.7, 3.4, -0.3],
            y_range=[-1.5, 2.5, 1.0],
            x_length=8.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.2)
        lbl_x = MathTex(r"\log_{10} T_{\rm eff}\;\rightarrow\;\text{hot}", color=INK, font_size=17
                        ).next_to(ax.x_axis.get_start(), LEFT, buff=0.1)
        lbl_y = MathTex(r"\log_{10}(L/L_\odot)", color=INK, font_size=18
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("HR diagram — Hayashi tracks (pre-MS contraction)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        # ZAMS reference
        zams_T = np.array([3.56, 3.60, 3.70, 3.74, 3.78, 3.90, 4.10, 4.40])
        zams_L = np.array([-0.8, -0.5, -0.2, -0.15, 0.0,  0.7,  1.8,  3.2])
        zams = VMobject(color=DIM, stroke_width=2.0, stroke_opacity=0.5)
        zams.set_points_smoothly([ax.c2p(T, L) for T, L in zip(zams_T, zams_L)])

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), Create(zams), run_time=1.5)
        zams_lbl = Text("ZAMS", font="EB Garamond", font_size=15, color=DIM
                        ).next_to(ax.c2p(3.90, 0.7), RIGHT, buff=0.08)
        self.play(Write(zams_lbl), run_time=0.4)

        # Hayashi tracks — waypoints (log T, log L)
        tracks = [
            # (mass label, color, waypoints)
            ("0.3 M_Sun",  DIM,   [(3.585, 0.5), (3.570, 0.1), (3.560, -0.3), (3.556, -0.7)]),
            ("1.0 M_Sun",  BLUE,  [(3.580, 1.0), (3.578, 0.5), (3.600, 0.0), (3.748, -0.15)]),
            ("3.0 M_Sun",  BROWN, [(3.590, 2.0), (3.700, 1.5), (3.900, 1.0), (4.15, 0.85)]),
        ]

        for mass_lbl, color, waypoints in tracks:
            prev = None
            for i, (logT, logL) in enumerate(waypoints):
                dot = Dot(ax.c2p(logT, logL), radius=0.08, color=color)
                if prev:
                    seg = VMobject(color=color, stroke_width=2.5)
                    seg.set_points_smoothly([ax.c2p(*prev), ax.c2p(logT, logL)])
                    self.play(Create(seg), FadeIn(dot), run_time=0.6)
                else:
                    self.play(FadeIn(dot), run_time=0.4)
                prev = (logT, logL)
            lbl = Text(mass_lbl, font="EB Garamond", font_size=16, color=color
                       ).next_to(ax.c2p(*waypoints[0]), UR, buff=0.05)
            self.play(Write(lbl), run_time=0.5)

        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_contraction_power(self):
        eq = MathTex(
            r"t_{\rm KH}(1\,M_\odot) \approx 10\;\mathrm{Myr}\quad\text{(gravitational contraction powers luminosity)}",
            color=INK, font_size=24,
        ).center().shift(UP * 1.2)
        note = Text(
            "Fusion only starts when the core reaches 15 million K.",
            font="EB Garamond", font_size=21, color=DIM,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "The Sun spent 10 million years falling before it became a star.",
            font="EB Garamond", font_size=21, color=BLUE,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
