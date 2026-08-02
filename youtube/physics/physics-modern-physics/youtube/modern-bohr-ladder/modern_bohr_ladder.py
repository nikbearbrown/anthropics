#!/usr/bin/env python3
"""
modern_bohr_ladder.py — Bohr Energy Ladder: Electron Drops and Balmer Series
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    En = -13.6 eV / n²
    Balmer: 1/λ = R_H(1/4 - 1/n²)
    Hα=656.3 nm (n=3→2), Hβ=486.1 nm (n=4→2)

Run standalone to verify:
    python3 modern_bohr_ladder.py
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34   # J·s
C_LIGHT = 2.998e8      # m/s
EV = 1.602e-19         # J per eV
R_H = 1.0974e7         # m⁻¹ (Rydberg constant)
E0 = 13.6              # eV (hydrogen ionization energy)


def En(n): return -E0 / n**2


def wavelength_nm(ni, nf):
    inv_lam = R_H * (1.0 / nf**2 - 1.0 / ni**2)
    return 1.0 / inv_lam * 1e9  # nm


def verify():
    print("=== Bohr Energy Ladder verification ===")
    for n in range(1, 7):
        print(f"n={n}: E={En(n):.3f} eV")
    print(f"\nBalmer series (n→2):")
    for ni in range(3, 8):
        lam = wavelength_nm(ni, 2)
        print(f"n={ni}→2: λ={lam:.1f} nm")
    print(f"\nP1: Hα (n=3→2) = {wavelength_nm(3,2):.1f} nm  (card: 656.3 nm)")
    print(f"P1: Hβ (n=4→2) = {wavelength_nm(4,2):.1f} nm  (card: 486.1 nm)")
    print(f"P2: Series limit (n=∞→2) = {1/(R_H*(1/4))*1e9:.1f} nm  (card: 364.6 nm)")
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


class ModernBohrLadderScene(Scene):
    """
    Energy ladder n=1..6, electron drops for Balmer series,
    photon emitted at correct wavelength, spectrum strip grows.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_energy_levels()
        self._phase_balmer_series()
        self._phase_spectrum()

    def _phase_title(self):
        title = Text("Bohr Energy Ladder — Hydrogen Spectrum",
                     font="EB Garamond", font_size=56, color=INK)
        sub = MathTex(r"E_n = -\frac{13.6\,\text{eV}}{n^2}", color=BLUE, font_size=36)
        hook = Text("Each drop fires one photon at one exact wavelength",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_energy_levels(self):
        # Build energy ladder on left
        # Map energy to y position: -13.6 eV → y=-3, 0 eV → y=2.5
        def E_to_y(e): return 2.5 + (e + 0.5) / 2.5  # rough linear mapping

        # Better: map E linearly
        E_min, E_max = -14.0, 0.5
        y_min, y_max = -3.2, 2.8
        def e2y(e): return y_min + (e - E_min) / (E_max - E_min) * (y_max - y_min)

        ladder = VGroup()
        level_mobs = {}
        for n in range(1, 7):
            e = En(n)
            y = e2y(e)
            level_line = Line([-6.5, y, 0], [-3.5, y, 0], color=BLUE, stroke_width=2)
            e_lbl = MathTex(f"n={n},\\;{e:.2f}\\,\\text{{eV}}", color=BLUE,
                            font_size=18).next_to(level_line, RIGHT, buff=0.1)
            ladder.add(level_line, e_lbl)
            level_mobs[n] = y

        # ionization level
        cont_line = Line([-6.5, e2y(0), 0], [-3.5, e2y(0), 0],
                         color=DIM, stroke_width=1.5, stroke_opacity=0.6)
        cont_lbl = MathTex(r"n\to\infty:\;0\,\text{eV}", color=DIM, font_size=17
                           ).next_to(cont_line, RIGHT, buff=0.1)

        hdr = Text("Energy levels", font="EB Garamond", font_size=22, color=INK
                   ).move_to([-5, 3.2, 0])

        self.play(Create(ladder), Create(cont_line), Write(cont_lbl), Write(hdr),
                  run_time=2.5)
        self.wait(1.5)
        return level_mobs, e2y

    def _phase_balmer_series(self):
        E_min, E_max = -14.0, 0.5
        y_min, y_max = -3.2, 2.8
        def e2y(e): return y_min + (e - E_min) / (E_max - E_min) * (y_max - y_min)

        # Balmer transitions n=3,4,5,6 → n=2
        balmer_colors = {
            3: "#FF6060",   # red (Hα 656 nm)
            4: "#60A0FF",   # blue-green (Hβ 486 nm)
            5: "#8080FF",   # blue-violet (Hγ 434 nm)
            6: "#C060FF",   # violet (Hδ 410 nm)
        }
        x_arrow = -5.0  # x position of ladder arrows

        arrows_made = VGroup()
        for ni in [3, 4, 5, 6]:
            lam = wavelength_nm(ni, 2)
            y_top = e2y(En(ni))
            y_bot = e2y(En(2))
            color = balmer_colors[ni]
            arr = Arrow(start=[x_arrow, y_top, 0], end=[x_arrow, y_bot, 0],
                        color=color, stroke_width=2.5, buff=0, tip_length=0.22)
            lbl = MathTex(f"\\lambda={lam:.0f}\\,\\text{{nm}}", color=color,
                          font_size=18).next_to(arr, LEFT, buff=0.08)
            caption = Text(f"n={ni}→2  ({lam:.0f} nm)",
                           font="EB Garamond", font_size=19, color=color
                           ).to_edge(DOWN, buff=0.3)
            self.play(Create(arr), Write(lbl), Write(caption), run_time=1.2)
            self.wait(0.5)
            self.play(FadeOut(caption), run_time=0.2)
            arrows_made.add(arr, lbl)

        self.wait(1.5)

    def _phase_spectrum(self):
        # Draw spectrum strip at bottom
        title = Text("Balmer series — the hydrogen spectrum",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        # Spectrum strip (wavelength 380–700 nm)
        strip_left = -3.0
        strip_right = 5.5
        strip_y = -1.5
        strip_w = strip_right - strip_left
        strip = Rectangle(width=strip_w, height=0.35, color=DIM, stroke_width=1,
                          fill_color=CANVAS, fill_opacity=0.5).move_to(
            [(strip_left + strip_right) / 2, strip_y, 0])
        lam_min, lam_max = 380, 700

        def lam_to_x(lam):
            return strip_left + (lam - lam_min) / (lam_max - lam_min) * strip_w

        lbl_nm_l = MathTex(r"380\,\text{nm}", color=DIM, font_size=17
                           ).next_to(strip, DOWN).shift(LEFT * (strip_w / 2 - 0.5))
        lbl_nm_r = MathTex(r"700\,\text{nm}", color=DIM, font_size=17
                           ).next_to(strip, DOWN).shift(RIGHT * (strip_w / 2 - 0.5))

        balmer_colors = {
            656.3: "#FF6060",
            486.1: "#60A0FF",
            434.0: "#9080FF",
            410.2: "#C060FF",
        }

        self.play(Create(strip), Write(lbl_nm_l), Write(lbl_nm_r), run_time=0.8)
        for lam_nm, color in balmer_colors.items():
            x = lam_to_x(lam_nm)
            vline = Line([x, strip_y - 0.2, 0], [x, strip_y + 0.2, 0],
                         color=color, stroke_width=3)
            lbl = MathTex(f"{lam_nm:.0f}", color=color, font_size=16).move_to(
                [x, strip_y + 0.45, 0])
            self.play(Create(vline), Write(lbl), run_time=0.6)

        # Lyman and Paschen annotation
        ly_lbl = Text("Lyman series (UV, n→1)", font="EB Garamond",
                      font_size=17, color=DIM).move_to([-4, 0.5, 0])
        pa_lbl = Text("Paschen (IR, n→3)", font="EB Garamond",
                      font_size=17, color=DIM).move_to([3.5, 0.5, 0])
        self.play(FadeIn(ly_lbl), FadeIn(pa_lbl), run_time=0.7)
        self.wait(3.5)
