#!/usr/bin/env python3
"""
vol3_form_factor_diffraction.py — Nuclear Form Factor: Diffraction Reveals the Proton's Size
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    dσ/dΩ = (dσ/dΩ)_Rutherford × |F(q)|²
    F(q) = 3[sin(qR) − qR·cos(qR)]/(qR)³   (uniform sphere)
    First zero at qR = 4.493 (first zero of 3j₁(qR)/qR)

Gold nucleus (Au-197):
    R = 1.2 × 197^(1/3) fm ≈ 7.0 fm
    E_e = 250 MeV → k ≈ 1.27 fm⁻¹
    First zero: qR = 4.493 → q = 0.642 fm⁻¹ → θ_zero ≈ 29.3°

Verify:
    python3 vol3_form_factor_diffraction.py --verify
"""
import sys
import numpy as np

R_AU = 7.0      # fm  (gold nuclear radius)
K_E  = 1.27     # fm⁻¹  (electron wavenumber at 250 MeV)

def form_factor(q_R):
    """F(qR) = 3[sin(qR) − qR·cos(qR)]/(qR)³ for uniform sphere."""
    x = np.asarray(q_R, dtype=float)
    # Avoid singularity at x=0
    result = np.ones_like(x)
    mask = np.abs(x) > 1e-6
    xm = x[mask]
    result[mask] = 3 * (np.sin(xm) - xm * np.cos(xm)) / xm**3
    return result

def rutherford(theta_deg, k):
    """Rutherford (point-nucleus) dσ/dΩ in fm²/sr (up to a constant we set=1 at θ=1°)"""
    th = np.radians(theta_deg)
    return 1.0 / np.sin(th/2)**4

def dsigma(theta_deg, k, R):
    """dσ/dΩ = Rutherford × |F(q)|²"""
    th = np.radians(theta_deg)
    q  = 2 * k * np.sin(th / 2)
    F  = form_factor(q * R)
    return rutherford(theta_deg, k) * F**2

def verify():
    print("=== Nuclear Form Factor verification ===")
    print(f"R_Au = {R_AU:.1f} fm,  k_e = {K_E:.3f} fm⁻¹")

    # Find first zero analytically: qR = 4.493
    qR_zero = 4.493
    q_zero  = qR_zero / R_AU
    sin_half = q_zero / (2 * K_E)
    theta_zero_rad = 2 * np.arcsin(sin_half)
    theta_zero_deg = np.degrees(theta_zero_rad)
    print(f"\nP1: First zero at qR = {qR_zero:.3f}")
    print(f"    q_zero = {q_zero:.4f} fm⁻¹")
    print(f"    sin(θ/2) = {sin_half:.4f}")
    print(f"    θ_zero = {theta_zero_deg:.2f}°  (should be ≈ 29.3°)")
    assert abs(theta_zero_deg - 29.3) < 1.0, f"FAIL: θ_zero = {theta_zero_deg:.2f}°"

    # P2: ratio of first to second zero angle
    qR_second = 7.725   # second zero of j₁(qR)/qR
    ratio_qR  = qR_zero / qR_second
    print(f"\nP2: qR_first/qR_second = {qR_zero}/{qR_second} = {ratio_qR:.4f}")
    print(f"    (should be ≈ 0.582)")
    assert abs(ratio_qR - 0.582) < 0.002, "FAIL: zero ratio"

    # Verify F(qR_zero) ≈ 0
    F_at_zero = form_factor(np.array([qR_zero]))[0]
    print(f"\n|F(qR=4.493)| = {abs(F_at_zero):.6f}  (should be ≈ 0)")
    assert abs(F_at_zero) < 0.001, f"FAIL: F not zero at first zero: {F_at_zero}"
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


class FormFactorDiffractionScene(Scene):
    """
    Angular distribution dσ/dΩ(θ):
    Two curves: Rutherford (dashed orange) and form-factor-modified (solid blue).
    At θ_zero the blue curve touches zero; a ruler extracts R.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curves(ax)
        self._inset_sphere()
        self._payoff()

    def _title(self):
        t = Text("Nuclear Form Factor & Diffraction", font="EB Garamond",
                 font_size=52, color=INK)
        s = Text(
            "Zeros in dσ/dΩ reveal the nuclear radius  —  diffraction as a ruler",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0, 90, 15],
            y_range=[-4, 14, 3],   # log10 scale
            x_length=7.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=True, tip_length=0.18),
        ).shift(LEFT * 0.8 + DOWN * 0.1)

        xl = MathTex(r"\theta\;(°)", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        yl = MathTex(r"\log_{10}(d\sigma/d\Omega)", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        self.play(Create(ax), Write(xl), Write(yl), run_time=1.2)
        return ax

    def _draw_curves(self, ax):
        theta_vals = np.linspace(1, 89, 600)

        # Normalize so that at θ=3° both curves equal the same value
        norm_theta = 3.0
        ruth_norm = rutherford(norm_theta, K_E)
        ff_norm   = dsigma(norm_theta, K_E, R_AU)
        # Use log10, clip for display
        log_ruth = np.log10(np.array([rutherford(t, K_E)/ruth_norm for t in theta_vals]))
        log_ff   = np.log10(np.maximum(
            [dsigma(t, K_E, R_AU)/ff_norm for t in theta_vals], 1e-10))
        log_ruth = np.clip(log_ruth, -4, 14)
        log_ff   = np.clip(log_ff, -4, 14)

        ruth_pts = [ax.c2p(t, v) for t, v in zip(theta_vals, log_ruth)]
        ff_pts   = [ax.c2p(t, v) for t, v in zip(theta_vals, log_ff)]

        ruth_curve = DashedVMobject(
            VMobject(color=BROWN, stroke_width=2.5).set_points_smoothly(ruth_pts),
            num_dashes=80,
        )
        ff_curve = VMobject(color=BLUE, stroke_width=3.5)
        ff_curve.set_points_smoothly(ff_pts)

        lbl_ruth = Text("Rutherford (point nucleus)", font="EB Garamond",
                        font_size=17, color=BROWN).to_corner(UR, buff=0.35).shift(DOWN*0.5)
        lbl_ff   = Text("Form-factor modified", font="EB Garamond",
                        font_size=17, color=BLUE).next_to(lbl_ruth, DOWN, buff=0.15)

        self.play(Create(ruth_curve), Create(ff_curve), run_time=2.5)
        self.play(Write(lbl_ruth), Write(lbl_ff), run_time=0.7)

        # Annotate first zero
        # θ_zero ≈ 29.3°  — find log10 floor for arrow
        theta_z = 29.3
        # Arrow from above to the dip
        arr_start = ax.c2p(theta_z, 2)
        arr_end   = ax.c2p(theta_z, -3.5)
        arrow = Arrow(arr_start, arr_end, color=GOLD, buff=0.05,
                      stroke_width=2.5, tip_length=0.18)
        ann = MathTex(
            r"\theta_{\rm zero} = 29.3°",
            color=GOLD, font_size=19,
        ).next_to(arr_start, UL, buff=0.08)
        zero_note = MathTex(r"qR = 4.493 \Rightarrow R = 7.0\;\mathrm{fm}",
                            color=GOLD, font_size=18).to_edge(DOWN, buff=0.25)

        self.play(GrowArrow(arrow), Write(ann), run_time=0.9)
        self.play(Write(zero_note), run_time=0.7)
        self.wait(2.0)

    def _inset_sphere(self):
        # Small inset showing uniform sphere with radius annotation
        circle = Circle(radius=0.8, color=BLUE, stroke_width=2.5,
                        fill_color=BLUE, fill_opacity=0.2).to_corner(DR, buff=0.5)
        r_lbl  = MathTex(r"R = 7.0\;\mathrm{fm}", color=INK, font_size=16
                         ).next_to(circle, DOWN, buff=0.1)
        r_arrow = DoubleArrow(
            circle.get_left(), circle.get_right(),
            color=GOLD, stroke_width=1.5, tip_length=0.12, buff=0,
        )
        self.play(Create(circle), Write(r_lbl), Create(r_arrow), run_time=0.8)
        self.wait(1.5)

    def _payoff(self):
        eqs = VGroup(
            MathTex(
                r"\frac{d\sigma}{d\Omega} = \left(\frac{d\sigma}{d\Omega}\right)_{\rm Ruth}"
                r"\times |F(q)|^2",
                color=INK, font_size=26,
            ),
            MathTex(
                r"F(q) = \frac{3[\sin(qR)-qR\cos(qR)]}{(qR)^3}",
                color=BLUE, font_size=24,
            ),
            MathTex(
                r"\text{First zero: }qR = 4.493\;"
                r"\Rightarrow\;R = \frac{4.493}{2k\sin(\theta_{\rm zero}/2)}",
                color=GOLD, font_size=22,
            ),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
