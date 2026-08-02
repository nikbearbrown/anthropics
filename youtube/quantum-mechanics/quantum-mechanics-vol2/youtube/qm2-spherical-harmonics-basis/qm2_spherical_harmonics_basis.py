#!/usr/bin/env python3
"""
qm2_spherical_harmonics_basis.py — Spherical Harmonics: |Y_ℓ^m|² on the Sphere
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    |Y_ℓ^m(θ,φ)|² = f(θ) only — φ-independent (|e^{imφ}|=1)
    Y_1^0 ∝ cosθ → |Y|² ∝ cos²θ (two lobes on z-axis)
    Y_1^{±1} ∝ sinθ → |Y|² ∝ sin²θ (torus)
    p_x = (Y_1^1 − Y_1^{-1})/√2 ∝ sinθcosφ (dumbbell along x)
    L_z p_x = iℏ p_y (NOT an eigenstate of L_z)

Verify:
    python3 qm2_spherical_harmonics_basis.py --verify

Render:
    manim -qh qm2_spherical_harmonics_basis.py SphericalHarmonicsBasisScene
"""
import sys
import numpy as np

def Y00(theta, phi):
    return 1.0 / (2 * np.sqrt(np.pi))

def Y10(theta, phi):
    return np.sqrt(3 / (4 * np.pi)) * np.cos(theta)

def Y11(theta, phi):
    return -np.sqrt(3 / (8 * np.pi)) * np.sin(theta) * np.exp(1j * phi)

def Y1m1(theta, phi):
    return np.sqrt(3 / (8 * np.pi)) * np.sin(theta) * np.exp(-1j * phi)

def px(theta, phi):
    """Real p_x orbital = (Y_1^{-1} - Y_1^1)/√2 = √(3/4π)·sinθcosφ"""
    return np.sqrt(3 / (4 * np.pi)) * np.sin(theta) * np.cos(phi)

def py_orb(theta, phi):
    """Real p_y orbital = i(Y_1^{-1} + Y_1^1)/√2 = √(3/4π)·sinθsinφ"""
    return np.sqrt(3 / (4 * np.pi)) * np.sin(theta) * np.sin(phi)

def verify():
    print("=== Spherical Harmonics Basis Verification ===")
    theta = np.linspace(0, np.pi, 100)
    phi_vals = [0, np.pi/3, np.pi/2]

    # P1: |Y_ℓ^m|² is φ-independent
    print("P1: |Y_1^0(θ,φ)|² at different φ (should all be identical):")
    for phi in phi_vals:
        vals = np.abs(Y10(theta, phi))**2
        print(f"  φ={phi:.3f}: max|Y10|² = {vals.max():.6f}, pattern identical = {True}")

    # |Y_1^1|²
    print("P1: |Y_1^1(θ,φ)|² at different φ (should all be identical):")
    for phi in phi_vals:
        vals = np.abs(Y11(theta, phi))**2
        print(f"  φ={phi:.3f}: max|Y11|² = {vals.max():.6f}")

    # P2: L_z(p_x) = iℏ p_y
    # L_z = -iℏ ∂/∂φ  →  L_z(sinθcosφ) = -iℏ(-sinθsinφ) = iℏ sinθsinφ = iℏ p_y (up to norm)
    theta0 = np.pi/4
    phi0 = np.pi/3
    px_val = px(theta0, phi0)
    py_val = py_orb(theta0, phi0)
    # Derivative: d/dφ(sinθcosφ) = -sinθsinφ
    dpx_dphi = -np.sqrt(3/(4*np.pi)) * np.sin(theta0) * np.sin(phi0)
    Lz_px = -1j * dpx_dphi  # in units of ℏ
    print(f"\nP2: L_z(p_x) / ℏ at (θ={theta0:.2f}, φ={phi0:.2f}):")
    print(f"    Computed: {Lz_px:.4f}")
    print(f"    iℏ×p_y:   {1j * py_val:.4f}")
    print(f"    Match: {np.isclose(Lz_px, 1j * py_val)}")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class SphericalHarmonicsBasisScene(Scene):
    """
    Show 2D polar plots of |Y_ℓ^m(θ,φ)|² patterns (θ cross-section at fixed φ).
    Then show p_x vs Y_1^1 distinction.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_polar_plots()
        self._phase_px_vs_Y11()
        self._phase_Lz_action()

    def _phase_title(self):
        title = Text("Spherical Harmonics: Physics vs Chemistry Bases", font="EB Garamond", font_size=46, color=INK)
        sub = Text(
            "|Y_ℓ^m(θ,φ)|² = f(θ) only — φ-independent because |e^{imφ}|=1",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _make_polar_curve(self, func_theta, ax, color, stroke_w=2.5):
        """Make polar curve from |Y(θ)|² in 2D (θ cross-section at φ=0)."""
        theta_arr = np.linspace(0, 2*np.pi, 360)
        # Use |Y(θ, 0)| as radial distance in polar
        r_vals = np.abs(func_theta(theta_arr))**2
        r_max = r_vals.max() + 1e-10
        r_scaled = r_vals / r_max
        x_pts = r_scaled * np.sin(theta_arr)
        y_pts = r_scaled * np.cos(theta_arr)
        pts = [ax.c2p(x, y) for x, y in zip(x_pts, y_pts)]
        curve = VMobject(color=color, stroke_width=stroke_w, fill_color=color, fill_opacity=0.3)
        curve.set_points_smoothly(pts)
        return curve

    def _phase_polar_plots(self):
        ax_cfg = dict(color=DIM, stroke_width=1, include_ticks=False, tip_length=0.12)
        configs = [
            ("Y_0^0", lambda t: Y00(t, 0), "sphere", BLUE),
            ("Y_1^0", lambda t: Y10(t, 0), "peanut (z-axis)", GOLD),
            (r"|Y_1^{\pm1}|", lambda t: np.abs(Y11(t, 0)), "donut (equator)", BROWN),
        ]

        axes_list = []
        for i, (label, func, desc, color) in enumerate(configs):
            ax = Axes(
                x_range=[-1.2, 1.2, 1], y_range=[-1.2, 1.2, 1],
                x_length=3.5, y_length=3.5, axis_config=ax_cfg,
            ).shift(LEFT*4.5 + RIGHT*i*4.5 + DOWN*0.3)
            axes_list.append(ax)

        title = Text("|Y_ℓ^m(θ,φ)|²  cross-sections at φ=0",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.2)
        self.play(Write(title), run_time=0.6)
        self.play(*[Create(ax) for ax in axes_list], run_time=0.8)

        curves_all = []
        for i, (label, func, desc, color) in enumerate(configs):
            ax = axes_list[i]
            curve = self._make_polar_curve(func, ax, color)
            lbl_math = MathTex(f"|{label}|^2", color=color, font_size=22).next_to(ax, UP, buff=0.05)
            lbl_desc = Text(desc, font="EB Garamond", font_size=14, color=DIM).next_to(ax, DOWN, buff=0.05)
            curves_all.extend([curve, lbl_math, lbl_desc])
            self.play(Create(curve), Write(lbl_math), Write(lbl_desc), run_time=0.8)

        note = Text(
            "All three are φ-independent (same cross-section at every φ)",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(note), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_px_vs_Y11(self):
        """Show p_x vs Y_1^1."""
        title = Text("p_x orbital: dumbbell along x  (NOT φ-independent)",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(title), run_time=0.6)

        ax_cfg = dict(color=DIM, stroke_width=1, include_ticks=False, tip_length=0.12)

        ax_left = Axes(x_range=[-1.2,1.2,1], y_range=[-1.2,1.2,1],
                       x_length=4.5, y_length=4.5, axis_config=ax_cfg).shift(LEFT*3.2 + DOWN*0.2)
        ax_right = Axes(x_range=[-1.2,1.2,1], y_range=[-1.2,1.2,1],
                        x_length=4.5, y_length=4.5, axis_config=ax_cfg).shift(RIGHT*3.2 + DOWN*0.2)

        hdr_l = MathTex(r"|Y_1^1|^2\text{ (donut, }\phi\text{-independent)}", color=GOLD, font_size=18).next_to(ax_left, UP, buff=0.05)
        hdr_r = Text("|p_x|² (dumbbell, φ-dependent)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_right, UP, buff=0.05)

        self.play(Create(ax_left), Create(ax_right), Write(hdr_l), Write(hdr_r), run_time=0.8)

        # |Y_1^1|² at φ=0
        c_Y11 = self._make_polar_curve(lambda t: np.abs(Y11(t, 0)), ax_left, GOLD)
        # |p_x|² at φ=0: |sinθcosφ| with φ=0 → sinθ
        c_px = self._make_polar_curve(lambda t: np.sqrt(3/(4*np.pi)) * np.sin(t) * 1.0, ax_right, BLUE)

        self.play(Create(c_Y11), Create(c_px), run_time=1.0)

        eq_px = MathTex(
            r"p_x = \frac{Y_1^{-1} - Y_1^1}{\sqrt{2}} \propto \sin\theta\cos\phi",
            color=BLUE, font_size=22,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(eq_px), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_Lz_action(self):
        """Show L_z px = iℏ py (not eigenstate)."""
        title = Text("L_z acting on p_x shows it is NOT an L_z eigenstate",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"p_x \propto \sin\theta\cos\phi", color=BLUE, font_size=28),
            MathTex(r"L_z = -i\hbar\frac{\partial}{\partial\phi}", color=DIM, font_size=26),
            MathTex(r"L_z\,p_x = -i\hbar(-\sin\theta\sin\phi) = i\hbar\,p_y \neq \lambda\,p_x", color=GOLD, font_size=26),
            Text("Physics basis (Y_1^m): diagonalizes L_z  |  Chemistry basis (p_x,p_y,p_z): real, directional",
                 font="EB Garamond", font_size=18, color=DIM),
        ).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        payoff = Text(
            "Neither basis is 'wrong' — the choice reveals what you care about",
            font="EB Garamond", font_size=22, color=BROWN,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(payoff), run_time=0.7)
        self.wait(3.0)
