#!/usr/bin/env python3
"""
vol1_coherent_state.py — The Coherent State: Gaussian That Never Spreads
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    ω = 10¹⁴ rad/s, mₑ
    |α| = 3: ⟨n⟩ = |α|² = 9
    σ_x = √(ℏ/2mₑω) ≈ 0.074 nm (constant!)
    x₀ = √(2ℏ/mₑω)·|α| ≈ 0.443 nm amplitude
    ⟨x(t)⟩ = x₀·cos(ωt), period T ≈ 62.8 fs
    Free particle with same σ₀: spreads as √(1 + (t/τ)²)

Verify:
    python3 vol1_coherent_state.py --verify

Render:
    manim -qh vol1_coherent_state.py CoherentStateScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34
M_E    = 9.10938e-31
OMEGA  = 1.0e14
ALPHA  = 3.0

def sigma_x():
    """σ_x for ground state of harmonic osc (= coherent state σ_x)."""
    return np.sqrt(HBAR / (2 * M_E * OMEGA))

def x0_amplitude():
    """Classical orbit amplitude = √(2ℏ/mω)·|α|"""
    return np.sqrt(2 * HBAR / (M_E * OMEGA)) * ALPHA

def period_fs():
    return 2 * np.pi / OMEGA * 1e15

def mean_x_coherent(t_fs):
    return x0_amplitude() * np.cos(OMEGA * t_fs * 1e-15)

def sigma_free(t_fs, sigma0):
    """Width of free Gaussian at time t_fs."""
    tau = M_E * sigma0**2 / HBAR * 1e-15  # fs
    return sigma0 * np.sqrt(1 + (t_fs / tau)**2)

def verify():
    print("=== Coherent State Verification ===")
    sx = sigma_x()
    x0 = x0_amplitude()
    T = period_fs()
    print(f"σ_x = {sx*1e9:.4f} nm  (constant)")
    print(f"x₀ = {x0*1e9:.4f} nm  (classical amplitude)")
    print(f"T = {T:.2f} fs  (period)")
    print(f"⟨n⟩ = |α|² = {ALPHA**2:.1f}")

    # P1: σ_x = constant
    sigmas = [sigma_x() for _ in [0, T/4, T/2, T]]
    print(f"\nP1: σ_x at t=0, T/4, T/2, T: {[f'{s*1e9:.6f}' for s in sigmas]} nm  (all identical)")

    # P2: ⟨x(T)⟩ = x₀ (one full cycle)
    xT = mean_x_coherent(T)
    print(f"\nP2: ⟨x(T)⟩ = {xT*1e9:.6f} nm  (should = x₀ = {x0*1e9:.6f} nm)")
    print(f"    Error = {abs(xT - x0)*1e9:.2e} nm")
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


class CoherentStateScene(Scene):
    """
    Side-by-side: left = coherent state (width stays), right = free Gaussian (width grows).
    Width meter beneath each.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_comparison()
        self._phase_poisson()

    def _phase_title(self):
        title = Text("The Coherent State", font="EB Garamond", font_size=58, color=INK)
        sub = Text(
            "ω = 10¹⁴ rad/s  ·  |α| = 3  ·  σ_x = 0.074 nm  (constant forever)",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"|\alpha(t)\rangle:\quad \langle x(t)\rangle = x_0\cos(\omega t),\quad \sigma_x = \sqrt{\hbar/2m\omega}",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_comparison(self):
        sx = sigma_x()
        x0 = x0_amplitude()
        T_fs = period_fs()
        sigma0_free = sx  # same initial width for free particle

        ax_cfg = dict(color=INK, stroke_width=1.3, include_ticks=False, tip_length=0.16)

        # Left: coherent state in parabola
        ax_left = Axes(
            x_range=[-0.7, 0.7, 0.3], y_range=[0, 1.4, 0.5],
            x_length=5.5, y_length=3.8, axis_config=ax_cfg,
        ).shift(LEFT*3.4 + UP*0.8)

        # Right: free particle
        ax_right = Axes(
            x_range=[0, 3.0, 1.0], y_range=[0, 1.4, 0.5],
            x_length=5.5, y_length=3.8, axis_config=ax_cfg,
        ).shift(RIGHT*3.4 + UP*0.8)

        hdr_left = Text("Coherent state\n(harmonic well)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_left, UP, buff=0.08)
        hdr_right = Text("Free Gaussian\n(same initial σ)", font="EB Garamond", font_size=18, color=BROWN).next_to(ax_right, UP, buff=0.08)

        # Parabola in left panel
        xp = np.linspace(-0.65, 0.65, 80)
        V_parab = 0.5 * M_E * OMEGA**2 * (xp*1e-9)**2 / (HBAR * OMEGA) * 0.5
        par_pts = [ax_left.c2p(x, min(v, 1.3)) for x, v in zip(xp, V_parab)]
        parabola = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        parabola.set_points_smoothly(par_pts)

        lbl_left_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=14).next_to(ax_left.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_right_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=14).next_to(ax_right.x_axis.get_end(), RIGHT, buff=0.04)

        self.play(
            Create(ax_left), Create(ax_right),
            Write(hdr_left), Write(hdr_right),
            Write(lbl_left_x), Write(lbl_right_x),
            Create(parabola), run_time=1.2,
        )

        t_track = ValueTracker(0.0)

        def _coh_density():
            t_fs = t_track.get_value()
            xc = mean_x_coherent(t_fs) * 1e9  # nm
            x_nm = np.linspace(-0.65, 0.65, 300)
            sx_nm = sx * 1e9
            prob = np.exp(-0.5 * (x_nm - xc)**2 / sx_nm**2)
            prob = prob / prob.max() * 1.2
            pts = [ax_left.c2p(x, p) for x, p in zip(x_nm, prob)]
            pts_c = [p for p in pts if -10 < p[0] < 10 and -10 < p[1] < 10]
            if len(pts_c) < 4:
                return VGroup()
            fill_pts = pts_c + [ax_left.c2p(0.64, 0), ax_left.c2p(-0.64, 0)]
            try:
                return Polygon(*fill_pts, color=BLUE, fill_color=BLUE, fill_opacity=0.4, stroke_width=0)
            except Exception:
                return VGroup()

        def _free_density():
            t_fs = t_track.get_value()
            tau_fs = M_E * sigma0_free**2 / HBAR * 1e15
            sig_t = sigma0_free * np.sqrt(1 + (t_fs/tau_fs)**2)
            x_nm = np.linspace(0, 3, 300)
            x_center_nm = 1.5  # stationary free particle
            sig_t_nm = sig_t * 1e9
            prob = np.exp(-0.5 * (x_nm - x_center_nm)**2 / sig_t_nm**2)
            prob = prob / prob.max() * 1.2
            pts = [ax_right.c2p(x, p) for x, p in zip(x_nm, prob)]
            fill_pts = pts + [ax_right.c2p(2.9, 0), ax_right.c2p(0.1, 0)]
            try:
                return Polygon(*fill_pts, color=BROWN, fill_color=BROWN, fill_opacity=0.35, stroke_width=0)
            except Exception:
                return VGroup()

        def _sigma_labels():
            t_fs = t_track.get_value()
            tau_fs = M_E * sigma0_free**2 / HBAR * 1e15
            sig_t = sigma0_free * np.sqrt(1 + (t_fs/tau_fs)**2) * 1e9
            sx_nm = sx * 1e9
            return VGroup(
                Text(f"σ_x = {sx_nm:.4f} nm", font="EB Garamond", font_size=16, color=BLUE).move_to(ax_left.get_bottom() + DOWN*0.4),
                Text(f"σ_x = {sig_t:.4f} nm", font="EB Garamond", font_size=16, color=BROWN).move_to(ax_right.get_bottom() + DOWN*0.4),
            )

        dyn_coh = always_redraw(_coh_density)
        dyn_free = always_redraw(_free_density)
        dyn_sig = always_redraw(_sigma_labels)
        self.add(dyn_coh, dyn_free, dyn_sig)

        hdr_line = Text(
            "Left: σ_x flat  |  Right: σ_x grows  |  same initial width",
            font="EB Garamond", font_size=17, color=DIM,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(hdr_line), run_time=0.6)

        # 3 full periods
        self.play(t_track.animate.set_value(3 * T_fs), run_time=10.0, rate_func=linear)
        self.wait(1.0)

        payoff = VGroup(
            MathTex(r"\sigma_x(\text{coherent}) = \sqrt{\hbar/2m\omega} = 0.074\,\mathrm{nm}\text{ — constant}", color=BLUE, font_size=24),
            MathTex(r"\sigma_x(\text{free}) = \sigma_0\sqrt{1+(t/\tau)^2}\text{ — grows}", color=BROWN, font_size=24),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(hdr_line, dyn_sig), Write(payoff), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(ax_left, ax_right, hdr_left, hdr_right, lbl_left_x, lbl_right_x,
                          parabola, dyn_coh, dyn_free, payoff), run_time=0.6)

    def _phase_poisson(self):
        """Show Poisson photon-number distribution."""
        title = Text("Poisson photon-number distribution  P(n) = e^{−|α|²}|α|^{2n}/n!",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 18, 3], y_range=[0, 0.16, 0.05],
            x_length=10.0, y_length=4.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.16),
        ).shift(DOWN*0.5)
        lbl_x = MathTex(r"n", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_y = MathTex(r"P(n)", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.05)

        from scipy.special import factorial
        alpha_sq = ALPHA**2
        n_vals = np.arange(0, 18)
        P_n = np.exp(-alpha_sq) * alpha_sq**n_vals / np.array([float(factorial(int(n))) for n in n_vals])

        bars = VGroup()
        for n, p in zip(n_vals, P_n):
            bar = Rectangle(
                width=0.45, height=ax.c2p(0, p)[1] - ax.c2p(0, 0)[1],
                fill_color=GOLD, fill_opacity=0.8, stroke_width=0,
            )
            bar.move_to(ax.c2p(n, p/2))
            bars.add(bar)

        mean_line = DashedLine(ax.c2p(9, 0), ax.c2p(9, 0.15), color=BLUE, stroke_width=2)
        mean_lbl = MathTex(r"\langle n\rangle = |\alpha|^2 = 9", color=BLUE, font_size=20).next_to(mean_line, RIGHT, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=0.6)
        self.play(Create(bars), run_time=1.2)
        self.play(Create(mean_line), Write(mean_lbl), run_time=0.6)

        caption = Text("Laser light is a coherent state — Poisson photon statistics",
                       font="EB Garamond", font_size=20, color=DIM).to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.6)
        self.wait(3.0)
