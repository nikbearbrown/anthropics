#!/usr/bin/env python3
"""
vol3_breit_wigner_resonance.py — Breit-Wigner Resonance: Phase Shift Through π/2
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    σ₀(E) = (4π/k²) sin²δ₀(E)
    Near resonance: tan δ₀ = (Γ/2)/(E_R − E)
    Breit-Wigner: σ₀(E) = (4π/k_R²)·(Γ/2)²/[(E−E_R)²+(Γ/2)²]

Parameters:
    E_R = 1.00 eV, Γ = 0.20 eV, m = m_e
    k_R = √(2m_e E_R)/ℏ ≈ 5.13 nm⁻¹
    σ_peak = 4π/k_R² ≈ 0.476 nm²
    σ_classical = πa² with a=0.1 nm → 0.031 nm²

Verify:
    python3 vol3_breit_wigner_resonance.py --verify
"""
import sys
import numpy as np

HBAR = 1.054571817e-34  # J·s
M_E  = 9.10938e-31      # kg
EV   = 1.602176634e-19  # J

E_R  = 1.00  # eV
GAMMA = 0.20  # eV
A_CLASS = 0.1e-9   # m (geometric radius for classical comparison)

def k_at_E(E_eV):
    """k in nm⁻¹"""
    return np.sqrt(2 * M_E * E_eV * EV) / HBAR * 1e-9

def phase_shift(E_eV):
    """δ₀ in radians, mod π taken to [0, π]"""
    return np.arctan((GAMMA/2) / (E_R - E_eV + 1e-15)) % np.pi

def sigma_bw(E_eV):
    """Breit-Wigner cross-section in nm²"""
    k = k_at_E(E_eV)
    lorentz = (GAMMA/2)**2 / ((E_eV - E_R)**2 + (GAMMA/2)**2)
    return (4*np.pi / k**2) * lorentz

def sigma_classical():
    """πa² in nm²"""
    return np.pi * (A_CLASS * 1e9)**2   # convert m to nm

def verify():
    print("=== Breit-Wigner Resonance verification ===")
    k_R = k_at_E(E_R)
    sigma_peak = 4 * np.pi / k_R**2
    sigma_cl   = sigma_classical()
    print(f"E_R = {E_R} eV,  Γ = {GAMMA} eV")
    print(f"k_R = {k_R:.4f} nm⁻¹  (should be ≈ 5.13 nm⁻¹)")
    print(f"σ_peak = 4π/k_R² = {sigma_peak:.4f} nm²  (should be ≈ 0.476 nm²)")
    print(f"σ_classical = πa² = {sigma_cl:.4f} nm²  (a={A_CLASS*1e9:.1f} nm)")
    factor = sigma_peak / sigma_cl
    print(f"Enhancement factor = {factor:.1f}×  (should be ≈ 15)")

    assert abs(k_R - 5.13) < 0.05, f"FAIL: k_R = {k_R:.3f} should be ≈ 5.13"
    assert abs(sigma_peak - 0.476) < 0.01, f"FAIL: σ_peak = {sigma_peak:.4f}"

    # P1: peak at E_R when δ₀ = π/2
    delta_at_resonance = phase_shift(E_R + 1e-6)   # just above (arctan → π/2)
    print(f"\nP1: δ₀(E_R) = {delta_at_resonance:.4f} rad  (should be ≈ π/2 = {np.pi/2:.4f})")
    sigma_at_res = sigma_bw(E_R)
    print(f"    σ₀(E_R) = {sigma_at_res:.4f} nm²  (should be σ_peak = {sigma_peak:.4f} nm²)")
    assert abs(sigma_at_res - sigma_peak) < 0.001, "FAIL: peak cross-section"

    # P2: FWHM = Γ
    E_half = E_R + GAMMA/2
    sigma_half = sigma_bw(E_half)
    print(f"\nP2: σ at E_R + Γ/2 = {E_half:.2f} eV:  {sigma_half:.4f} nm²")
    print(f"    σ_peak/2 = {sigma_peak/2:.4f} nm²  (full BW uses k_R; var-k shifts slightly)")
    print(f"    Ratio = {sigma_half/(sigma_peak/2):.4f}  (should be ≈ 0.9 to 1.1)")
    # The half-max at variable k(E) deviates slightly from exact Γ/2 definition
    assert abs(sigma_half - sigma_peak/2) < 0.04, "FAIL: FWHM too far from half-max"
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED    = "#E05252"


class BreitWignerResonanceScene(Scene):
    """
    Two synchronized panels:
    Top: σ₀(E)/σ_classical Lorentzian  (cursor sweeps left→right)
    Bottom: δ₀(E) phase shift (0 → π/2 → π)
    Unitarity maximum labeled at E=E_R.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._dual_panel()
        self._payoff()

    def _title(self):
        t = Text("Breit-Wigner Resonance", font="EB Garamond",
                 font_size=58, color=INK)
        s = Text(
            "Phase shift through π/2  →  cross-section rockets to 4π/k²",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _dual_panel(self):
        E_min, E_max = 0.4, 1.8
        E_vals = np.linspace(E_min, E_max, 600)

        k_R     = k_at_E(E_R)
        sig_peak = 4 * np.pi / k_R**2
        sig_cl   = sigma_classical()
        ratio_max = sig_peak / sig_cl   # ≈ 15

        # ─── Top axis: σ/σ_classical ─────────────────────────────────────
        ax_top = Axes(
            x_range=[E_min, E_max, 0.2],
            y_range=[0, ratio_max * 1.15, 5],
            x_length=9.0,
            y_length=3.2,
            axis_config=dict(color=INK, stroke_width=1.3,
                             include_ticks=True, tip_length=0.15),
        ).shift(UP * 1.5)

        xl_top = MathTex(r"E\;(\mathrm{eV})", color=INK, font_size=20
                         ).next_to(ax_top.x_axis.get_end(), RIGHT, buff=0.08)
        yl_top = MathTex(r"\sigma_0/\sigma_{\rm cl}", color=INK, font_size=20
                         ).next_to(ax_top.y_axis.get_end(), UP, buff=0.05)

        # Unitarity ceiling line
        sigma_top = np.array([sigma_bw(E)/sig_cl for E in E_vals])
        top_pts   = [ax_top.c2p(E, s) for E, s in zip(E_vals, sigma_top)]
        top_curve = VMobject(color=BLUE, stroke_width=3.5)
        top_curve.set_points_smoothly(top_pts)

        unit_line = DashedLine(ax_top.c2p(E_min, ratio_max),
                               ax_top.c2p(E_max, ratio_max),
                               color=GOLD, stroke_width=1.5, dash_length=0.1)
        unit_lbl  = MathTex(r"4\pi/k_R^2", color=GOLD, font_size=17
                            ).next_to(ax_top.c2p(E_max, ratio_max), RIGHT, buff=0.05)

        classic_line = DashedLine(ax_top.c2p(E_min, 1),
                                  ax_top.c2p(E_max, 1),
                                  color=BROWN, stroke_width=1.2, dash_length=0.1)
        cl_lbl = MathTex(r"\sigma_{\rm cl}", color=BROWN, font_size=17
                         ).next_to(ax_top.c2p(E_max, 1), RIGHT, buff=0.05)

        # ─── Bottom axis: δ₀(E) ──────────────────────────────────────────
        ax_bot = Axes(
            x_range=[E_min, E_max, 0.2],
            y_range=[0, np.pi * 1.05, np.pi/2],
            x_length=9.0,
            y_length=2.5,
            axis_config=dict(color=INK, stroke_width=1.3,
                             include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 1.8)

        xl_bot = MathTex(r"E\;(\mathrm{eV})", color=INK, font_size=20
                         ).next_to(ax_bot.x_axis.get_end(), RIGHT, buff=0.08)
        yl_bot = MathTex(r"\delta_0\;(\mathrm{rad})", color=INK, font_size=20
                         ).next_to(ax_bot.y_axis.get_end(), UP, buff=0.05)

        delta_vals = np.array([phase_shift(E) for E in E_vals])
        bot_pts    = [ax_bot.c2p(E, d) for E, d in zip(E_vals, delta_vals)]
        bot_curve  = VMobject(color=BROWN, stroke_width=3.5)
        bot_curve.set_points_smoothly(bot_pts)

        # π/2 reference
        pi2_line = DashedLine(ax_bot.c2p(E_min, np.pi/2),
                              ax_bot.c2p(E_max, np.pi/2),
                              color=GOLD, stroke_width=1.2, dash_length=0.1)
        pi2_lbl  = MathTex(r"\pi/2", color=GOLD, font_size=17
                           ).next_to(ax_bot.c2p(E_max, np.pi/2), RIGHT, buff=0.05)

        self.play(
            Create(ax_top), Create(ax_bot),
            Write(xl_top), Write(yl_top), Write(xl_bot), Write(yl_bot),
            run_time=1.2,
        )
        self.play(
            Create(unit_line), Write(unit_lbl),
            Create(classic_line), Write(cl_lbl),
            Create(pi2_line), Write(pi2_lbl),
            run_time=0.8,
        )

        # Draw curves as cursor sweeps
        self.play(Create(top_curve), Create(bot_curve), run_time=3.0)
        self.wait(0.5)

        # Vertical cursor at E_R
        vl_top = DashedLine(ax_top.c2p(E_R, 0), ax_top.c2p(E_R, ratio_max),
                            color=GOLD, stroke_width=1.5)
        vl_bot = DashedLine(ax_bot.c2p(E_R, 0), ax_bot.c2p(E_R, np.pi),
                            color=GOLD, stroke_width=1.5)
        ann = Text("UNITARITY MAXIMUM\nδ₀ = π/2", font="EB Garamond",
                   font_size=17, color=GOLD).next_to(
                       ax_top.c2p(E_R, ratio_max * 0.5), LEFT, buff=0.12)

        self.play(Create(vl_top), Create(vl_bot), Write(ann), run_time=0.9)

        params = MathTex(
            r"E_R = 1.00\;\mathrm{eV},\;\Gamma = 0.20\;\mathrm{eV},\;"
            r"\sigma_{\rm peak} = 0.476\;\mathrm{nm}^2\;\approx 15\sigma_{\rm cl}",
            color=INK, font_size=19,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(params), run_time=0.8)
        self.wait(2.5)

    def _payoff(self):
        eqs = VGroup(
            MathTex(
                r"\sigma_0(E) = \frac{4\pi}{k_R^2}\cdot"
                r"\frac{(\Gamma/2)^2}{(E-E_R)^2+(\Gamma/2)^2}",
                color=INK, font_size=28,
            ),
            MathTex(
                r"\text{FWHM} = \Gamma = 0.20\;\mathrm{eV}\;"
                r"\Rightarrow\;\tau = \hbar/\Gamma \approx 3.3\;\mathrm{fs}",
                color=BLUE, font_size=24,
            ),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
