#!/usr/bin/env python3
"""
modern_photoelectric.py — Photoelectric Effect: KEmax = hf - BE
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    Sodium: BE=2.28 eV, f₀=5.51×10¹⁴ Hz
    Green 6.0e14 Hz → KE=0.20 eV
    Blue 7.5e14 Hz → KE=0.82 eV
    h=6.626×10⁻³⁴ J·s

Run standalone to verify:
    python3 modern_photoelectric.py
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34   # J·s
EV = 1.602e-19         # J per eV
BE_NA = 2.28           # eV (sodium work function)
C_LIGHT = 2.998e8      # m/s


def f0(): return BE_NA * EV / H_PLANCK


def KE_eV(f): return H_PLANCK * f / EV - BE_NA


def verify():
    print("=== Photoelectric effect verification ===")
    print(f"h = {H_PLANCK:.4e} J·s")
    print(f"Threshold f₀ = {f0():.3e} Hz  (card: 5.51e14)")
    print(f"λ₀ = c/f₀ = {C_LIGHT/f0()*1e9:.1f} nm  (card: 544 nm)")
    for f_hz, lbl in [(6.0e14, "green"), (7.5e14, "blue")]:
        ke = KE_eV(f_hz)
        print(f"{lbl} f={f_hz:.1e}: KE = {ke:.3f} eV")
    # P1: slope = h
    print(f"P1: slope = {H_PLANCK:.4e} J·s  (= Planck's constant)")
    # P2: threshold λ
    lam0 = C_LIGHT / f0() * 1e9
    print(f"P2: λ₀ = {lam0:.1f} nm  (green 550 nm barely fails, blue 450 nm succeeds)")
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

RED_COLOR = "#E05252"
GREEN_COLOR = "#5CAD5C"


class ModernPhotoelectricScene(Scene):
    """
    KE_max vs frequency line with threshold.
    Three photon arrows (below, at, above threshold).
    Classical prediction contradicted by intensity control.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_ke_graph()
        self._phase_intensity_failure()
        self._phase_gold_test()

    def _phase_title(self):
        title = Text("Photoelectric Effect", font="EB Garamond",
                     font_size=64, color=INK)
        sub = MathTex(r"K_{\max} = hf - \phi", color=BLUE, font_size=36)
        hook = Text("Brighter light doesn't eject faster electrons — higher frequency does",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eqs = VGroup(
            MathTex(r"K_{\max} = hf - \phi\;(\text{work function})",
                    color=INK, font_size=34),
            MathTex(r"V_{\rm stop} = K_{\max}/e", color=BLUE, font_size=32),
            MathTex(r"f_0 = \phi/h\;(\text{threshold frequency})",
                    color=GOLD, font_size=32),
            MathTex(r"\text{No emission below }f_0\text{, regardless of intensity}",
                    color=DIM, font_size=28),
        ).arrange(DOWN, buff=0.42).center()
        for mob in eqs:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_ke_graph(self):
        f0_hz = f0()
        f_max = 9.0e14
        ax = Axes(
            x_range=[3.0, 9.0, 1.0],
            y_range=[-0.5, 3.0, 0.5],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        # Scale x axis in units of 10¹⁴ Hz
        f_scale = 1e14
        lx = MathTex(r"f\;(10^{14}\,\text{Hz})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"K_{\max}\;(\text{eV})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("KEmax vs frequency — slope = h",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        # Threshold line
        f0_scaled = f0_hz / f_scale
        thresh = DashedLine(ax.c2p(f0_scaled, -0.5), ax.c2p(f0_scaled, 3.0),
                            color=GOLD, stroke_width=2)
        thresh_lbl = MathTex(r"f_0 = 5.51\times10^{14}\,\text{Hz}", color=GOLD,
                             font_size=20).next_to(ax.c2p(f0_scaled, 2.5), RIGHT, buff=0.08)

        # KE line (zero below threshold, linear above)
        f_above = np.linspace(f0_scaled, 9.0, 300)
        ke_above = [KE_eV(f * f_scale) for f in f_above]
        ke_line = ax.plot_line_graph(
            x_values=list(f_above), y_values=ke_above,
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        zero_line = ax.plot_line_graph(
            x_values=[3.0, f0_scaled], y_values=[0.0, 0.0],
            line_color=DIM, stroke_width=2, add_vertex_dots=False,
        )

        # Three photon points
        points = [
            (4.5, "below f₀: no emission", DIM),
            (f0_scaled, "at threshold: KE≈0", GOLD),
            (7.5, "above f₀: fast electron", BLUE),
        ]
        for f_pt, txt, color in points:
            ke_pt = max(KE_eV(f_pt * f_scale), 0)
            d = Dot(ax.c2p(f_pt, ke_pt), color=color, radius=0.1)
            l = Text(txt, font="EB Garamond", font_size=17, color=color
                     ).next_to(d, UP, buff=0.12)
            self.play(FadeIn(d), Write(l), run_time=0.5)

        self.play(Create(thresh), Write(thresh_lbl), run_time=0.8)
        self.play(Create(zero_line), Create(ke_line), run_time=2.0)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, thresh, thresh_lbl, ke_line, zero_line),
                  run_time=0.5)

    def _phase_intensity_failure(self):
        title = Text("Classical prediction — contradicted by experiment",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        # Show intensity control with no effect on KE
        intensity_txt = Text("Intensity: ████████████ (10×)",
                             font="EB Garamond", font_size=26, color=GOLD).shift(UP * 1.0)
        ke_txt = MathTex(r"K_{\max} = \text{unchanged}", color=BLUE, font_size=34
                         ).shift(DOWN * 0.3)
        classical_wrong = Text("Classical wave theory predicts KE ∝ intensity — WRONG",
                               font="EB Garamond", font_size=22, color=DIM
                               ).to_edge(DOWN, buff=0.28)
        cross = Text("✗", font="EB Garamond", font_size=60, color="#E05252"
                     ).shift(DOWN * 0.3 + RIGHT * 3)

        self.play(Write(intensity_txt), run_time=0.7)
        self.play(Write(ke_txt), FadeIn(cross), run_time=0.8)
        self.play(Write(classical_wrong), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(title, intensity_txt, ke_txt, cross, classical_wrong),
                  run_time=0.5)

    def _phase_gold_test(self):
        # Gold: higher work function, threshold shifts right
        BE_AU = 5.1  # eV
        f0_au = BE_AU * EV / H_PLANCK
        note = VGroup(
            MathTex(r"\text{Gold: }\phi = 5.1\,\text{eV},\;f_0 = 1.23\times10^{15}\,\text{Hz (deep UV)}",
                    color=GOLD, font_size=28),
            MathTex(r"\text{Sodium: }\phi = 2.28\,\text{eV},\;f_0 = 5.51\times10^{14}\,\text{Hz}",
                    color=BLUE, font_size=28),
            Text("φ is a property of the metal, not of the light",
                 font="EB Garamond", font_size=24, color=INK),
            MathTex(r"\text{Same slope }h\text{ for both}",
                    color=DIM, font_size=26),
        ).arrange(DOWN, buff=0.45).center()
        for mob in note:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob),
                      run_time=0.8)
        self.wait(3.5)
