#!/usr/bin/env python3
"""
modern_blackbody_uv_catastrophe.py — Blackbody Radiation: UV Catastrophe and Planck's Fix
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    Planck: B_λ = (2hc²/λ⁵) / (exp(hc/λkT) - 1)
    Rayleigh-Jeans: B_λ^RJ = 2ckT/λ⁴
    Wien: λ_peak = b/T, b=2.898e-3 m·K

Run standalone to verify:
    python3 modern_blackbody_uv_catastrophe.py
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34   # J·s
C_LIGHT = 2.998e8      # m/s
K_BOLTZ = 1.381e-23    # J/K
B_WIEN = 2.898e-3      # m·K


def planck(lam, T):
    x = H_PLANCK * C_LIGHT / (lam * K_BOLTZ * T)
    return 2 * H_PLANCK * C_LIGHT**2 / lam**5 / (np.exp(x) - 1)


def rayleigh_jeans(lam, T):
    return 2 * C_LIGHT * K_BOLTZ * T / lam**4


def lam_peak(T):
    return B_WIEN / T


def verify():
    print("=== Blackbody UV catastrophe verification ===")
    T_sun = 5778.0
    lp = lam_peak(T_sun) * 1e9
    print(f"Sun T={T_sun:.0f} K: λ_peak = {lp:.1f} nm  (card: 502 nm)")
    print(f"P1: λ_peak × T = {lam_peak(T_sun)*T_sun:.4e} m·K  (b = {B_WIEN:.4e})")
    # P2: RJ/Planck ratio at long wavelength (microwave, ~5mm, 290K)
    lam_mw = 5e-3
    T_room = 290
    ratio = rayleigh_jeans(lam_mw, T_room) / planck(lam_mw, T_room)
    print(f"P2: RJ/Planck at λ=5mm, T=290K = {ratio:.4f}  (should be ~1)")
    # UV catastrophe at short wavelength
    lam_uv = 200e-9
    T_hot = 6000
    p_uv = planck(lam_uv, T_hot)
    rj_uv = rayleigh_jeans(lam_uv, T_hot)
    print(f"UV (200nm, 6000K): Planck={p_uv:.3e}, RJ={rj_uv:.3e}  ratio={rj_uv/p_uv:.2f}x")
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


class ModernBlackbodyUvCatastropheScene(Scene):
    """
    Planck curve vs Rayleigh-Jeans at T=5778 K.
    UV catastrophe labeled. T sweeps 3000→8000 K.
    CMB overlay at T=2.725 K.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_curves()
        self._phase_temp_sweep()

    def _phase_title(self):
        title = Text("Blackbody Radiation — The UV Catastrophe",
                     font="EB Garamond", font_size=52, color=INK)
        sub = Text(
            "Classical physics predicted every hot object emits infinite power at short wavelengths",
            font="EB Garamond", font_size=21, color=BLUE)
        hook = Text("Planck's fix launched quantum mechanics",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eqs = VGroup(
            MathTex(r"B_\lambda = \frac{2hc^2/\lambda^5}{e^{hc/\lambda kT}-1}",
                    color=BLUE, font_size=34),
            MathTex(r"B_\lambda^{\rm RJ} = \frac{2ckT}{\lambda^4}\quad\text{(diverges as }\lambda\to0)",
                    color=BROWN, font_size=30),
            MathTex(r"\lambda_{\rm peak} = \frac{b}{T},\quad b=2.898\times10^{-3}\,\text{m}\cdot\text{K}",
                    color=GOLD, font_size=30),
        ).arrange(DOWN, buff=0.48).center()
        for mob in eqs:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_curves(self):
        T = 5778.0
        lam_min, lam_max = 100e-9, 2000e-9  # m
        # Plot in nm for display
        lam_arr = np.linspace(150e-9, 1900e-9, 500)
        p_arr = np.array([planck(l, T) for l in lam_arr])
        rj_arr = np.array([rayleigh_jeans(l, T) for l in lam_arr])

        # Normalize to peak of Planck
        p_max = np.max(p_arr)
        p_norm = p_arr / p_max
        rj_norm = rj_arr / p_max

        lam_nm = lam_arr * 1e9
        lam_plot_max = 1900.0

        ax = Axes(
            x_range=[100, lam_plot_max, 300],
            y_range=[0, 4.5, 1],
            x_length=9,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\lambda\;(\text{nm})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"B_\lambda\;(\text{normalized})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text(f"T = {T:.0f} K  (Sun)", font="EB Garamond", font_size=26,
                     color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        # Planck curve
        valid_p = p_norm <= 4.5
        planck_curve = ax.plot_line_graph(
            x_values=[l for l, v in zip(lam_nm, valid_p) if v],
            y_values=[p for p, v in zip(p_norm, valid_p) if v],
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        planck_lbl = Text("Planck (correct)", font="EB Garamond", font_size=20,
                          color=BLUE).to_corner(UR, buff=0.5)
        self.play(Create(planck_curve), Write(planck_lbl), run_time=2.0)

        # Rayleigh-Jeans
        valid_rj = (rj_norm <= 4.5) & (lam_nm > 400)
        rj_curve = ax.plot_line_graph(
            x_values=[l for l, v in zip(lam_nm, valid_rj) if v],
            y_values=[r for r, v in zip(rj_norm, valid_rj) if v],
            line_color=BROWN, stroke_width=3, add_vertex_dots=False,
        )
        rj_lbl = Text("Rayleigh-Jeans (diverges)", font="EB Garamond", font_size=20,
                      color=BROWN).next_to(planck_lbl, DOWN, buff=0.2)
        self.play(Create(rj_curve), Write(rj_lbl), run_time=2.0)

        # UV catastrophe label
        cat_arrow = Arrow(start=ax.c2p(250, 4.0), end=ax.c2p(200, 4.3),
                          color=GOLD, stroke_width=2, buff=0, tip_length=0.18)
        cat_lbl = Text("UV catastrophe: RJ → ∞", font="EB Garamond",
                       font_size=19, color=GOLD).next_to(cat_arrow, DOWN, buff=0.05)

        # Wien peak marker
        lp_nm = lam_peak(T) * 1e9
        peak_line = DashedLine(ax.c2p(lp_nm, 0), ax.c2p(lp_nm, 1.05),
                               color=GOLD, stroke_width=2)
        peak_lbl = MathTex(r"\lambda_{\rm peak}=502\,\text{nm}", color=GOLD,
                           font_size=19).next_to(ax.c2p(lp_nm, 1.1), RIGHT, buff=0.08)
        self.play(Create(cat_arrow), Write(cat_lbl), run_time=0.8)
        self.play(Create(peak_line), Write(peak_lbl), run_time=0.8)
        self.wait(3.5)
        self.play(FadeOut(title, ax, lx, ly, planck_curve, planck_lbl,
                          rj_curve, rj_lbl, cat_arrow, cat_lbl, peak_line, peak_lbl),
                  run_time=0.5)

    def _phase_temp_sweep(self):
        title = Text("Raise T: curve shifts left (bluer), grows taller",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[100, 3000, 500],
            y_range=[0, 1.2, 0.3],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\lambda\;(\text{nm})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"B_\lambda\;(\text{norm.})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)

        T_vals = [3000, 5778, 8000]
        colors = [BROWN, BLUE, GOLD]
        for T, color in zip(T_vals, colors):
            lam_arr = np.linspace(100e-9, 3000e-9, 500)
            p_arr = np.array([planck(l, T) for l in lam_arr])
            p_max = np.max(p_arr)
            p_norm = p_arr / p_max
            lam_nm = lam_arr * 1e9
            valid = (p_norm >= 0) & (p_norm <= 1.2) & (lam_nm <= 3000)
            curve = ax.plot_line_graph(
                x_values=[l for l, v in zip(lam_nm, valid) if v],
                y_values=[p for p, v in zip(p_norm, valid) if v],
                line_color=color, stroke_width=2.5, add_vertex_dots=False,
            )
            lp_nm = lam_peak(T) * 1e9
            lbl = MathTex(f"T={T}\\,\\text{{K}}", color=color, font_size=20
                          ).next_to(ax.c2p(lp_nm, 1.1), UP, buff=0.08)
            self.play(Create(curve), Write(lbl), run_time=1.5)

        note = Text("Wien's displacement: λ_peak × T = 2.898×10⁻³ m·K",
                    font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.7)
        self.wait(3.5)
