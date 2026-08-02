#!/usr/bin/env python3
"""
astro_planck_blackbody.py — Planck Curve vs Rayleigh-Jeans: UV Catastrophe
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    B_lambda(T) = 2hc^2 / lambda^5 / (exp(hc/lambda/kT) - 1)
    Rayleigh-Jeans: B_RJ = 2ckT / lambda^4
    Wien peak: lambda_peak = b/T, b = 2.898e-3 m*K

Verify: python3 astro_planck_blackbody.py --verify
Render: manim -qh astro_planck_blackbody.py AstroPlanckBlackbodyScene
"""
import sys
import numpy as np

# ─── Physical constants ───────────────────────────────────────────────────────
H_PLANCK = 6.626e-34    # J s
C_LIGHT  = 2.998e8      # m/s
K_BOLTZ  = 1.381e-23    # J/K
B_WIEN   = 2.898e-3     # m K  (Wien displacement constant)

TEMPS = [3000.0, 5778.0, 10000.0]   # K: M-dwarf, Sun, A-star
TEMP_NAMES = ["M dwarf  3 000 K", "Sun  5 778 K", "A star  10 000 K"]

def planck_lambda(lam_nm, T):
    """Spectral radiance B_lambda [W/m^2/sr/m] at wavelength lam_nm (nm)."""
    lam = lam_nm * 1e-9
    exponent = H_PLANCK * C_LIGHT / (lam * K_BOLTZ * T)
    # Clip to avoid overflow
    exponent = np.clip(exponent, 0, 700)
    return 2 * H_PLANCK * C_LIGHT**2 / lam**5 / (np.exp(exponent) - 1)

def rayleigh_jeans(lam_nm, T):
    """Classical Rayleigh-Jeans B_RJ [same units] — diverges at short lambda."""
    lam = lam_nm * 1e-9
    return 2 * C_LIGHT * K_BOLTZ * T / lam**4

def wien_peak_nm(T):
    """Peak wavelength in nm from Wien's displacement law."""
    return B_WIEN / T * 1e9

def verify():
    print("=== Planck/RJ verification ===")
    for T, name in zip(TEMPS, TEMP_NAMES):
        peak = wien_peak_nm(T)
        print(f"{name}: Wien peak = {peak:.1f} nm")
    # P1: Sun peak ~502 nm
    sun_peak = wien_peak_nm(5778.0)
    assert abs(sun_peak - 502) < 5, f"Sun peak off: {sun_peak}"
    print(f"\nP1: Sun peak = {sun_peak:.1f} nm  (expected ~502 nm) ✓")
    # P2: RJ exceeds Planck by >50x at 200 nm, T=5778 K
    lam_test = 200.0
    ratio = rayleigh_jeans(lam_test, 5778.0) / planck_lambda(lam_test, 5778.0)
    print(f"P2: RJ/Planck at 200 nm, 5778 K = {ratio:.1f}x  (expected >50) {'✓' if ratio > 50 else '✗'}")
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

COLORS_T = [DIM, BLUE, GOLD]   # M-dwarf, Sun, A-star

LAM_MIN =  100.0   # nm
LAM_MAX = 2500.0   # nm
N_PTS   = 400


class AstroPlanckBlackbodyScene(Scene):
    """
    Two curves per temperature: Planck (solid) vs Rayleigh-Jeans (dashed).
    Temperature slider morphs curves; Wien peak marker rides along.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_three_stars(ax)
        self._slider_phase(ax)

    # ── Title ────────────────────────────────────────────────────────────────

    def _title(self):
        t = Text("The Planck Curve Kills the UV Catastrophe",
                 font="EB Garamond", font_size=52, color=INK)
        s = Text(
            "Classical physics predicts infinite brightness at short wavelengths.\n"
            "Planck's fix was the first quantum.",
            font="EB Garamond", font_size=24, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.4).center()
        self.play(Write(t), run_time=1.4)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    # ── Axes ─────────────────────────────────────────────────────────────────

    def _axes(self):
        ax = Axes(
            x_range=[0, 2600, 500],
            y_range=[0, 1.05, 0.25],
            x_length=11,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.4)
        lx = MathTex(r"\lambda\;(\mathrm{nm})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = Text("Relative intensity", font="EB Garamond",
                  font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        # Wavelength band labels
        bands = [
            (100, 400, "UV", DIM),
            (400, 700, "Visible", BLUE),
            (700, 2600, "IR", BROWN),
        ]
        for x1, x2, label, col in bands:
            mid = (x1 + x2) / 2
            lbl = Text(label, font="EB Garamond", font_size=16, color=col)
            lbl.move_to(ax.c2p(mid, -0.07))
        self.play(Create(ax), Write(lx), Write(ly), run_time=1.5)
        return ax

    # ── Draw three stellar temperatures ──────────────────────────────────────

    def _draw_three_stars(self, ax):
        lam = np.linspace(LAM_MIN, LAM_MAX, N_PTS)

        for T, name, col in zip(TEMPS, TEMP_NAMES, COLORS_T):
            # Normalise to peak of this Planck curve
            plan = planck_lambda(lam, T)
            norm = plan.max()
            plan_n = plan / norm
            rj_n   = np.clip(rayleigh_jeans(lam, T) / norm, 0, 2.0)

            peak_nm = wien_peak_nm(T)

            # Planck curve (solid)
            plan_pts = [ax.c2p(l, b) for l, b in zip(lam, plan_n)]
            plan_mob = VMobject(color=col, stroke_width=3)
            plan_mob.set_points_smoothly(np.array(plan_pts))

            # RJ curve (dashed appearance via lower opacity)
            rj_pts = [ax.c2p(l, b) for l, b in zip(lam, rj_n) if b <= 1.02]
            if len(rj_pts) > 2:
                rj_mob = VMobject(color=col, stroke_width=2, stroke_opacity=0.5)
                rj_mob.set_points_smoothly(np.array(rj_pts))
            else:
                rj_mob = VMobject()

            # Peak marker
            peak_y = 1.0
            peak_dot = Dot(ax.c2p(peak_nm, peak_y), color=col, radius=0.08)
            peak_lbl = MathTex(rf"{peak_nm:.0f}\,\mathrm{{nm}}", color=col, font_size=20)
            peak_lbl.next_to(peak_dot, UP, buff=0.1)

            star_lbl = Text(name, font="EB Garamond", font_size=19, color=col)
            star_lbl.move_to(ax.c2p(1800, 0.85 if T == 3000 else (0.7 if T == 5778 else 0.55)))

            caption = Text(
                f"Wien peak at {peak_nm:.0f} nm  —  {'near-IR' if T == 3000 else ('green' if T == 5778 else 'UV')}",
                font="EB Garamond", font_size=20, color=col,
            ).to_edge(DOWN, buff=0.18)

            self.play(Create(plan_mob), run_time=1.8)
            if len(rj_pts) > 2:
                self.play(Create(rj_mob), run_time=1.0)
            self.play(FadeIn(peak_dot), Write(peak_lbl), Write(star_lbl),
                      Write(caption), run_time=1.0)
            self.wait(1.2)
            self.play(FadeOut(caption), run_time=0.3)

        # RJ divergence caption
        div_lbl = Text(
            "Rayleigh-Jeans (dashed) diverges to ∞ at short wavelengths  —  the UV catastrophe.",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.18)
        self.play(Write(div_lbl), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(div_lbl), run_time=0.4)

    # ── Slider: T sweep 3000 → 10000 K ───────────────────────────────────────

    def _slider_phase(self, ax):
        tc = ValueTracker(3000.0)
        lam = np.linspace(LAM_MIN, LAM_MAX, N_PTS)

        def _plan_curve():
            T = tc.get_value()
            plan = planck_lambda(lam, T)
            norm = plan.max()
            plan_n = plan / norm
            pts = np.array([ax.c2p(l, b) for l, b in zip(lam, plan_n)])
            m = VMobject(color=GOLD, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        def _peak_dot():
            T = tc.get_value()
            peak = wien_peak_nm(T)
            return Dot(ax.c2p(peak, 1.0), color=GOLD, radius=0.1)

        dyn_plan = always_redraw(_plan_curve)
        dyn_dot  = always_redraw(_peak_dot)
        self.add(dyn_plan, dyn_dot)

        T_lbl = Text("T = ", font="EB Garamond", font_size=28, color=INK)
        T_num = DecimalNumber(3000, num_decimal_places=0, color=GOLD, font_size=28)
        T_K   = Text(" K", font="EB Garamond", font_size=28, color=INK)
        T_num.add_updater(lambda m: m.set_value(tc.get_value()))
        T_row = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.1).to_edge(UP, buff=0.25)

        peak_lbl = Text("Wien peak: ", font="EB Garamond", font_size=24, color=DIM)
        peak_num = DecimalNumber(wien_peak_nm(3000), num_decimal_places=0,
                                 color=GOLD, font_size=24)
        peak_nm_lbl = Text(" nm", font="EB Garamond", font_size=24, color=DIM)
        peak_num.add_updater(lambda m: m.set_value(wien_peak_nm(tc.get_value())))
        peak_row = VGroup(peak_lbl, peak_num, peak_nm_lbl).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.25)

        self.play(Write(T_row), Write(peak_row), run_time=0.8)
        self.play(tc.animate.set_value(10000.0), run_time=5.0, rate_func=smooth)
        self.wait(1.5)

        finale = MathTex(
            r"\lambda_{\rm peak} = \frac{b}{T},\quad b = 2.898\times10^{-3}\,\mathrm{m\cdot K}",
            color=INK, font_size=32,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(T_row, peak_row), Write(finale), run_time=1.5)
        self.wait(2.5)
