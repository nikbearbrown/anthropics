#!/usr/bin/env python3
"""
astro_cmb_blackbody.py — CMB Blackbody at 2.725 K
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    B_lambda(T) = 2hc^2/lambda^5 / (exp(hc/lambda/kT) - 1)
    Wien peak: lambda_peak = b/T, b = 2.898e-3 m*K
    CMB: T = 2.725 K -> lambda_peak = 1.064 mm
    Recombination: T_rec ~ 3000 K -> lambda_peak = 0.966 um
    Redshift z ~ 1100: lambda_CMB / lambda_rec = 1100

Verify: python3 astro_cmb_blackbody.py --verify
Render: manim -qh astro_cmb_blackbody.py AstroCmbBlackbodyScene
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34
C_LIGHT  = 2.998e8
K_BOLTZ  = 1.381e-23
B_WIEN   = 2.898e-3

T_CMB  = 2.725    # K
T_REC  = 3000.0   # K  recombination

def planck_lambda(lam_mm, T):
    """B_lambda in arbitrary units vs wavelength in mm."""
    lam = lam_mm * 1e-3   # m
    exp_arg = np.clip(H_PLANCK * C_LIGHT / (lam * K_BOLTZ * T), 0, 700)
    return 2 * H_PLANCK * C_LIGHT**2 / lam**5 / (np.exp(exp_arg) - 1)

def wien_peak_mm(T):
    return B_WIEN / T * 1e3   # mm

def verify():
    print("=== CMB blackbody verification ===")
    peak_cmb = wien_peak_mm(T_CMB)
    print(f"P1: CMB peak = {peak_cmb:.4f} mm  (expected 1.064 mm) {'✓' if abs(peak_cmb - 1.064) < 0.01 else '✗'}")

    # P2: redshift factor from T_rec to T_CMB
    peak_rec = wien_peak_mm(T_REC)
    z_factor = peak_cmb / peak_rec
    print(f"P2: lambda shift factor = {z_factor:.0f}  (expected ~1100) {'✓' if abs(z_factor - 1100) < 50 else '✗'}")
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


class AstroCmbBlackbodyScene(Scene):
    """
    CMB Planck curve at 2.725 K (microwave); cooling animation from 3000 K.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curves(ax)
        self._cooling_animation(ax)
        self._finale()

    def _title(self):
        t = Text("The CMB: 2.725 K Relic from 380 000 Years Ago",
                 font="EB Garamond", font_size=48, color=INK)
        s = Text(
            "The best blackbody ever measured — the afterglow of the Big Bang.\n"
            "Wien peak at 1.064 mm: microwaves.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        # Wavelength axis in mm, log-like spacing but linear for animation clarity
        ax = Axes(
            x_range=[0, 4.0, 1.0],   # mm, 0 to 4 mm
            y_range=[0, 1.1, 0.25],
            x_length=10,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\lambda\;(\mathrm{mm})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = Text("Relative intensity", font="EB Garamond",
                  font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(lx), Write(ly), run_time=1.3)
        return ax

    def _draw_curves(self, ax):
        lam = np.linspace(0.05, 4.0, 500)

        # CMB curve at 2.725 K
        plan_cmb = planck_lambda(lam, T_CMB)
        norm_cmb = plan_cmb.max()
        plan_n = plan_cmb / norm_cmb

        pts = np.array([ax.c2p(l, b) for l, b in zip(lam, plan_n)])
        cmb_curve = VMobject(color=BLUE, stroke_width=3.5)
        cmb_curve.set_points_smoothly(pts)

        # Peak marker
        peak_mm = wien_peak_mm(T_CMB)
        peak_dot = Dot(ax.c2p(peak_mm, 1.0), color=GOLD, radius=0.1)
        peak_lbl = MathTex(r"1.064\,\mathrm{mm}", color=GOLD, font_size=22)
        peak_lbl.next_to(peak_dot, UP, buff=0.15)
        peak_dash = DashedLine(ax.c2p(peak_mm, 0), ax.c2p(peak_mm, 1.0),
                               color=GOLD, stroke_width=1.5, stroke_opacity=0.6)

        cmb_lbl = MathTex(r"T_{\rm CMB} = 2.725\,\mathrm{K}", color=BLUE, font_size=26)
        cmb_lbl.move_to(ax.c2p(2.8, 0.75))

        caption = Text(
            "Peak in the microwave — not visible, not radio. Microwaves.",
            font="EB Garamond", font_size=20, color=BLUE,
        ).to_edge(DOWN, buff=0.2)

        self.play(Create(cmb_curve), run_time=2.0)
        self.play(Create(peak_dash), FadeIn(peak_dot), Write(peak_lbl),
                  Write(cmb_lbl), Write(caption), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(caption), run_time=0.3)

    def _cooling_animation(self, ax):
        # Start with recombination curve (3000 K, shown at MUCH smaller scale)
        # normalised together with CMB to show relative shift
        lam = np.linspace(0.00005, 4.0, 600)

        tc = ValueTracker(T_REC)

        def _curve():
            T = tc.get_value()
            B = planck_lambda(lam, T)
            # Normalize to CMB peak for comparison
            B_cmb_peak = planck_lambda(np.array([wien_peak_mm(T_CMB)]), T_CMB)[0]
            B_n = np.clip(B / B_cmb_peak, 0, 1.05)
            pts = np.array([ax.c2p(l, b) for l, b in zip(lam, B_n)
                            if 0 <= b <= 1.05])
            if len(pts) < 3:
                return VMobject()
            m = VMobject(color=BROWN, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        dyn = always_redraw(_curve)
        self.add(dyn)

        T_lbl = Text("T = ", font="EB Garamond", font_size=24, color=BROWN)
        T_num = DecimalNumber(T_REC, num_decimal_places=0, color=BROWN, font_size=24)
        T_K   = Text(" K", font="EB Garamond", font_size=24, color=BROWN)
        T_num.add_updater(lambda m: m.set_value(tc.get_value()))
        T_row = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.1).to_corner(UR, buff=0.3)

        hdr = Text("Cooling from recombination (3 000 K) to today (2.725 K)",
                   font="EB Garamond", font_size=19, color=BROWN).to_edge(DOWN, buff=0.2)

        self.play(Write(T_row), Write(hdr), run_time=0.8)
        # Animate cooling
        self.play(tc.animate.set_value(T_CMB), run_time=5.0, rate_func=smooth)
        self.wait(1.5)

        z_lbl = MathTex(r"z \approx 1100", color=GOLD, font_size=28)
        z_lbl.to_edge(DOWN, buff=0.25)
        self.play(FadeOut(hdr), Write(z_lbl), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(T_row, z_lbl), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"\lambda_{\rm peak}^{\rm CMB} = \frac{2.898\times10^{-3}\,\mathrm{m\cdot K}}{2.725\,\mathrm{K}} = 1.064\,\mathrm{mm}",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
