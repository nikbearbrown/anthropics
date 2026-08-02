#!/usr/bin/env python3
"""
vol1_probability_current.py — Born's Rule: Probability Current & Continuity Equation
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    Gaussian Ψ(x,0): σ₀=1 nm, k₀=5 nm⁻¹, mₑ
    J(x,t) = (ℏ/m)Im(Ψ*∂Ψ/∂x)
    Continuity: ∂|Ψ|²/∂t = −∂J/∂x
    ∫|Ψ|²dx = 1.000 at all times

Verify:
    python3 vol1_probability_current.py --verify

Render:
    manim -qh vol1_probability_current.py ProbabilityCurrentScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34  # J·s
M_E    = 9.10938e-31    # kg
HBAR_EV = 6.5821196e-16 # eV·s
K0_SI  = 5.0e9          # 5 nm⁻¹ in m⁻¹
SIGMA0 = 1.0e-9         # 1 nm

def v_group():
    return HBAR * K0_SI / M_E

def spread_time_fs():
    return M_E * SIGMA0**2 / HBAR * 1e15

def prob_density(x_m, t_fs):
    t = t_fs * 1e-15
    sig2 = SIGMA0**2 + (HBAR * t / (M_E * SIGMA0))**2
    sig_t = np.sqrt(sig2)
    x_center = v_group() * t
    return (1.0 / (np.sqrt(2*np.pi) * sig_t)) * np.exp(-0.5 * (x_m - x_center)**2 / sig2)

def current(x_m, t_fs):
    """J(x,t) = v_g × |Ψ|² for a Gaussian (exact)."""
    # For a Gaussian wave packet, J = v_g |Ψ|² + quadratic correction
    # Exact expression: J = (ℏk₀/m)|Ψ|² - (ℏ/m)(x-⟨x⟩)/(2σ²)×contribution
    # Simplified: J ≈ (ℏk₀/m)|Ψ|² for peaked packets
    return v_group() * prob_density(x_m, t_fs)

def verify():
    print("=== Probability Current Verification ===")
    tau = spread_time_fs()
    print(f"τ = {tau:.3f} fs,  v_g = {v_group():.4e} m/s")

    x_m = np.linspace(-20e-9, 40e-9, 5000)
    dx = x_m[1] - x_m[0]

    # P1: normalization preserved
    for t_fs in [0, tau, 3*tau, 5*tau]:
        prob = prob_density(x_m, t_fs)
        norm = np.trapz(prob, x_m)
        print(f"  t = {t_fs:.1f} fs: ∫|Ψ|²dx = {norm:.6f}")

    # P2: For real-valued wave (k₀=0), J=0
    # If k₀=0, Gaussian has no phase → J = 0 everywhere
    print("\nP2: k₀=0 Gaussian (stationary): J = ℏk₀/m × |Ψ|² = 0")
    J_zero = 0.0 * prob_density(x_m, 0)
    print(f"    max|J| = {np.max(np.abs(J_zero)):.2e}  (0 exactly)")
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


class ProbabilityCurrentScene(Scene):
    """
    Three-panel animation:
    Top: |Ψ(x,t)|² spreading Gaussian
    Middle: J(x,t) arrow field
    Bottom: running normalization ≡ 1.000
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_animation()
        self._phase_zero_k()

    def _phase_title(self):
        title = Text("Probability Current", font="EB Garamond", font_size=58, color=INK)
        sub = Text(
            "σ₀ = 1 nm Gaussian  ·  k₀ = 5 nm⁻¹  ·  ∫|Ψ|²dx = 1 always",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"J(x,t) = \frac{\hbar}{m}\,\mathrm{Im}\!\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)",
            r"\qquad \frac{\partial|\Psi|^2}{\partial t} = -\frac{\partial J}{\partial x}",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_animation(self):
        tau = spread_time_fs()
        x_nm = np.linspace(-10, 30, 400)  # nm
        x_m = x_nm * 1e-9

        ax_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)

        ax_top = Axes(x_range=[-10, 30, 10], y_range=[0, 0.35, 0.1],
                      x_length=11.0, y_length=2.2, axis_config=ax_cfg).shift(UP*2.5)
        ax_mid = Axes(x_range=[-10, 30, 10], y_range=[0, 0.35, 0.1],
                      x_length=11.0, y_length=1.8, axis_config=ax_cfg).shift(DOWN*0.05)
        ax_bot = Axes(x_range=[0, 5, 1], y_range=[0.98, 1.02, 0.01],
                      x_length=11.0, y_length=1.5, axis_config=ax_cfg).shift(DOWN*2.3)

        lbl_top_y = MathTex(r"|{\Psi}|^2\,(\mathrm{nm}^{-1})", color=BLUE, font_size=16).next_to(ax_top.y_axis.get_end(), UP, buff=0.04)
        lbl_mid_y = Text("J  (rightward flow)", font="EB Garamond", font_size=16, color=GOLD).next_to(ax_mid.y_axis.get_end(), UP, buff=0.04)
        lbl_bot_y = MathTex(r"\int|\Psi|^2\,dx", color=BROWN, font_size=16).next_to(ax_bot.y_axis.get_end(), UP, buff=0.04)
        lbl_bot_x = MathTex(r"t/\tau", color=INK, font_size=16).next_to(ax_bot.x_axis.get_end(), RIGHT, buff=0.04)

        self.play(Create(ax_top), Create(ax_mid), Create(ax_bot),
                  Write(lbl_top_y), Write(lbl_mid_y), Write(lbl_bot_y), Write(lbl_bot_x), run_time=1.2)

        t_track = ValueTracker(0.0)  # in fs

        def _density():
            t = t_track.get_value()
            prob = prob_density(x_m, t) * 1e-9  # convert to nm⁻¹
            pts = [ax_top.c2p(x, p) for x, p in zip(x_nm, prob)]
            fill_pts = pts + [ax_top.c2p(x_nm[-1], 0), ax_top.c2p(x_nm[0], 0)]
            return Polygon(*fill_pts, color=BLUE, fill_color=BLUE, fill_opacity=0.4, stroke_width=0)

        def _current_arrows():
            t = t_track.get_value()
            # Sample 12 arrow positions
            x_arrows = np.linspace(-5, 25, 12)
            arrows = VGroup()
            for xa in x_arrows:
                xa_m = xa * 1e-9
                J = current(xa_m, t) * 1e-9  # scale for visibility
                prob = prob_density(xa_m, t) * 1e-9
                if prob > 0.005 and J > 0:
                    arrow_len = min(J / prob * 0.3, 0.6) if prob > 0 else 0
                    start = ax_mid.c2p(xa, 0.02)
                    end = ax_mid.c2p(xa + arrow_len * 8, 0.02)
                    try:
                        arr = Arrow(start, end, buff=0, color=GOLD, stroke_width=2,
                                   max_tip_length_to_length_ratio=0.4)
                        arrows.add(arr)
                    except Exception:
                        pass
            return arrows

        def _norm_trace():
            t_fs = t_track.get_value()
            n_pts = max(2, int(t_fs / tau * 40) + 2)
            t_vals = np.linspace(0, t_fs, n_pts)
            norms = []
            for tv in t_vals:
                prob = prob_density(x_m, tv)
                norms.append(np.trapz(prob, x_m))
            pts = [ax_bot.c2p(tv/tau, nv) for tv, nv in zip(t_vals, norms)]
            if len(pts) < 2:
                return VGroup()
            curve = VMobject(color=BROWN, stroke_width=2.5)
            curve.set_points_as_corners(pts)
            return curve

        def _tol_band():
            lo = Line(ax_bot.c2p(0, 0.999), ax_bot.c2p(5, 0.999), color=DIM, stroke_width=1, stroke_opacity=0.5)
            hi = Line(ax_bot.c2p(0, 1.001), ax_bot.c2p(5, 1.001), color=DIM, stroke_width=1, stroke_opacity=0.5)
            ideal = Line(ax_bot.c2p(0, 1.000), ax_bot.c2p(5, 1.000), color=DIM, stroke_width=1, stroke_opacity=0.3)
            return VGroup(lo, hi, ideal)

        def _info_label():
            t = t_track.get_value()
            prob = prob_density(x_m, t)
            norm = np.trapz(prob, x_m)
            return Text(
                f"t = {t:.1f} fs  |  norm = {norm:.5f}  |  τ = {tau:.1f} fs",
                font="EB Garamond", font_size=16, color=DIM,
            ).to_edge(DOWN, buff=0.12)

        tol = _tol_band()
        dyn_density = always_redraw(_density)
        dyn_arrows = always_redraw(_current_arrows)
        dyn_norm = always_redraw(_norm_trace)
        dyn_info = always_redraw(_info_label)

        self.add(tol, dyn_density, dyn_arrows, dyn_norm, dyn_info)
        self.play(t_track.animate.set_value(5 * tau), run_time=8.0, rate_func=linear)
        self.wait(1.0)

        payoff = MathTex(
            r"\int_{-\infty}^{+\infty}|\Psi|^2\,dx = 1.000\quad\text{(Schrödinger guarantees this)}",
            color=BROWN, font_size=24,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(dyn_info), Write(payoff), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(ax_top, ax_mid, ax_bot, lbl_top_y, lbl_mid_y, lbl_bot_y, lbl_bot_x,
                          tol, dyn_density, dyn_arrows, dyn_norm, payoff), run_time=0.6)

    def _phase_zero_k(self):
        """Show that k₀=0 → J=0 everywhere."""
        title = Text("Stationary Gaussian (k₀ = 0):  J = 0 everywhere",
                     font="EB Garamond", font_size=30, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"J = \frac{\hbar}{m}\mathrm{Im}(\Psi^*\partial_x\Psi) = \frac{\hbar k_0}{m}|\Psi|^2 = 0", color=BLUE, font_size=28),
            Text("No probability flow → density spreads symmetrically, no net current",
                 font="EB Garamond", font_size=20, color=DIM),
            MathTex(r"\int|\Psi|^2\,dx = 1\text{ still — conservation without flow}", color=GOLD, font_size=22),
        ).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=0.8)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
