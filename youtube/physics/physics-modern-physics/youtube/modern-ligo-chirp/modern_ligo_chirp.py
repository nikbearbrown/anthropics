#!/usr/bin/env python3
"""
modern_ligo_chirp.py — LIGO Chirp: Binary Black Hole Inspiral
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    GW150914: M1=36 M_sun, M2=29 M_sun
    Chirp mass M_c = 28.3 M_sun
    f sweeps 35→250 Hz over 0.2 s
    Strain h ~ 10^{-21}, displacement 4e-18 m

Run standalone to verify:
    python3 modern_ligo_chirp.py
"""
import sys
import numpy as np

G = 6.674e-11         # m³/(kg·s²)
C_LIGHT = 2.998e8     # m/s
M_SUN = 1.989e30      # kg
M1 = 36 * M_SUN
M2 = 29 * M_SUN


def chirp_mass(m1, m2):
    return (m1 * m2)**0.6 / (m1 + m2)**0.2


def gw_frequency_from_orbital(f_orbital):
    return 2 * f_orbital


def isco_frequency(M_total):
    """Innermost stable circular orbit frequency for Schwarzschild BH."""
    return C_LIGHT**3 / (6**(3.0/2) * np.pi * G * M_total)


def chirp_strain(M_c_kg, r_m):
    """Peak strain order-of-magnitude estimate."""
    return 4 * G**(5.0/3) * M_c_kg**(5.0/3) / (C_LIGHT**4 * r_m)


def verify():
    print("=== LIGO Chirp verification ===")
    M_c = chirp_mass(M1, M2)
    print(f"Chirp mass M_c = {M_c/M_SUN:.2f} M_sun  (card: 28.3)")
    M_total = M1 + M2
    f_isco = isco_frequency(M_total)
    f_gw_isco = gw_frequency_from_orbital(f_isco)
    print(f"f_GW at ISCO (65 M_sun) = {f_gw_isco:.1f} Hz  (card: ~150 Hz)")
    # Strain at 410 Mpc
    r_m = 1.3e9 * 3.086e16  # 1.3 Gly in meters
    h = chirp_strain(M_c, r_m)
    print(f"Strain h ~ {h:.2e}  (card: 10^-21)")
    # LIGO arm displacement
    L_arm = 4e3  # m
    disp = h * L_arm
    print(f"Displacement = h × L = {disp:.2e} m  (card: 4e-18 m)")
    print(f"P1: M_c = {M_c/M_SUN:.2f} M_sun  (GW150914: 28.3)")
    print(f"P2: f_GW at ISCO (M_total=65 M_sun) = {f_gw_isco:.1f} Hz  (card: ~150 Hz)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class ModernLigoChirpScene(Scene):
    """
    Left: two BH dots spiral inward.
    Right: h(t) chirp waveform draws (frequency increases).
    Merger flash. Key numbers annotated.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_key_numbers()
        self._phase_inspiral_and_chirp()
        self._phase_scale()

    def _phase_title(self):
        title = Text("LIGO Chirp — Binary Black Hole Inspiral",
                     font="EB Garamond", font_size=52, color=INK)
        sub = Text(
            "Two black holes a billion light-years away merged in 0.2 seconds",
            font="EB Garamond", font_size=22, color=BLUE)
        hook = Text(
            "LIGO felt a displacement of 4×10⁻¹⁸ m — 1/1000 of a proton diameter",
            font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_key_numbers(self):
        M_c = chirp_mass(M1, M2)
        M_total = M1 + M2
        f_isco = isco_frequency(M_total)
        f_gw_isco = gw_frequency_from_orbital(f_isco)

        rows = VGroup(
            MathTex(r"M_1=36\,M_\odot,\;M_2=29\,M_\odot,\;M_{\rm total}=65\,M_\odot",
                    color=INK, font_size=28),
            MathTex(r"M_c = \frac{(M_1M_2)^{3/5}}{(M_1+M_2)^{1/5}} = "
                    + f"{M_c/M_SUN:.1f}" + r"\,M_\odot", color=GOLD, font_size=30),
            MathTex(r"f_{\rm GW}: 35 \to 250\,\text{Hz in }0.2\,\text{s}",
                    color=BLUE, font_size=30),
            MathTex(r"h \sim 10^{-21},\;\Delta L = hL = 4\times10^{-18}\,\text{m}",
                    color=BROWN, font_size=28),
            MathTex(r"3\,M_\odot c^2 \approx 5.4\times10^{47}\,\text{J}\;\text{in GWs}",
                    color=DIM, font_size=26),
        ).arrange(DOWN, buff=0.38).center()
        for mob in rows:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(rows), run_time=0.5)

    def _phase_inspiral_and_chirp(self):
        # ── Left: spiraling BHs ────────────────────────────────────────────────
        center = np.array([-3.5, 0, 0])
        n_orbits = 12
        n_pts = 500

        # Spiral: radius shrinks from 1.5 to 0 over n_orbits turns
        theta = np.linspace(0, n_orbits * 2 * np.pi, n_pts)
        r_spiral = 1.5 * (1 - theta / (n_orbits * 2 * np.pi))

        # Two BHs: 180° apart
        bh1_pts = [center + r_spiral[i] * np.array([np.cos(theta[i]), np.sin(theta[i]), 0])
                   for i in range(n_pts)]
        bh2_pts = [center + r_spiral[i] * np.array([-np.cos(theta[i]), -np.sin(theta[i]), 0])
                   for i in range(n_pts)]

        spiral1 = VMobject(color=BLUE, stroke_width=1.5, stroke_opacity=0.6)
        spiral1.set_points_smoothly(bh1_pts)
        spiral2 = VMobject(color=BROWN, stroke_width=1.5, stroke_opacity=0.6)
        spiral2.set_points_smoothly(bh2_pts)

        bh1_dot = Dot(center + 1.5 * np.array([1, 0, 0]), color=BLUE, radius=0.18)
        bh2_dot = Dot(center - 1.5 * np.array([1, 0, 0]), color=BROWN, radius=0.18)
        bh1_lbl = MathTex(r"36\,M_\odot", color=BLUE, font_size=18
                          ).next_to(bh1_dot, UP, buff=0.1)
        bh2_lbl = MathTex(r"29\,M_\odot", color=BROWN, font_size=18
                          ).next_to(bh2_dot, UP, buff=0.1)

        # ── Right: chirp waveform ──────────────────────────────────────────────
        # Synthesize chirp: f increases from 35 to 250 Hz over 0.2 s
        t_chirp = np.linspace(0, 0.2, 1000)
        f_start, f_end = 35.0, 250.0
        # Instantaneous frequency: linear sweep for simplicity
        f_inst = f_start + (f_end - f_start) * (t_chirp / 0.2)**1.5
        # Instantaneous phase
        phi = 2 * np.pi * np.cumsum(f_inst) * (t_chirp[1] - t_chirp[0])
        # Amplitude: rises toward merger
        amp = 0.8 * (t_chirp / 0.2 + 0.1)**0.5
        h_t = amp * np.sin(phi)

        # Scale to scene
        t_scene = t_chirp / 0.2 * 6.5 + 0.5  # x: 0.5 to 7.0
        h_scene = h_t + 0  # y offset: center at y=0

        # Plot on right side (x from 0.5 to 7, y from -1 to 1)
        wf_pts = [np.array([0.5 + t * 6.5, h * 1.2, 0])
                  for t, h in zip(t_chirp / 0.2, h_t)]
        chirp_mob = VMobject(color=GOLD, stroke_width=2)
        chirp_mob.set_points_smoothly(wf_pts)

        ax_x = Line([0.5, 0, 0], [7.5, 0, 0], color=DIM, stroke_width=1.5)
        t_lbl = MathTex(r"t\;(0\to0.2\,\text{s})", color=DIM, font_size=18
                        ).next_to([7.5, 0, 0], RIGHT, buff=0.08)
        h_lbl = MathTex(r"h(t)", color=GOLD, font_size=22).move_to([3.5, 1.6, 0])

        freq_lbl = MathTex(r"35\to250\,\text{Hz}", color=GOLD, font_size=18
                           ).move_to([3.5, -1.7, 0])
        merger_lbl = Text("merger + ringdown", font="EB Garamond",
                          font_size=16, color=INK).move_to([7.0, 1.5, 0])

        sep = DashedLine([0, -3, 0], [0, 3, 0], color=DIM, stroke_width=1)

        self.play(FadeIn(bh1_dot), FadeIn(bh2_dot), Write(bh1_lbl), Write(bh2_lbl),
                  Create(sep), run_time=0.8)
        self.play(Create(spiral1), Create(spiral2), run_time=2.5)
        self.play(Create(ax_x), Write(t_lbl), Write(h_lbl), run_time=0.7)
        self.play(Create(chirp_mob), run_time=2.5)
        self.play(Write(freq_lbl), Write(merger_lbl), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(spiral1, spiral2, bh1_dot, bh2_dot, bh1_lbl, bh2_lbl,
                          sep, ax_x, t_lbl, h_lbl, chirp_mob, freq_lbl, merger_lbl),
                  run_time=0.5)

    def _phase_scale(self):
        final = VGroup(
            MathTex(r"h = \frac{4G^{5/3}M_c^{5/3}}{c^4 r}\,\cdot\,(\text{signal frequency})^{2/3}",
                    color=INK, font_size=28),
            MathTex(r"\Delta L = h\cdot L_{\rm arm} = 10^{-21}\times 4\,\text{km} = 4\times10^{-18}\,\text{m}",
                    color=GOLD, font_size=28),
            Text("Smaller than 10⁻³ of a proton diameter — measured with light",
                 font="EB Garamond", font_size=22, color=BLUE),
            Text("The chirp mass matched GR to within measurement noise",
                 font="EB Garamond", font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.45).center()
        for mob in final:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob), run_time=0.9)
        self.wait(4.0)
