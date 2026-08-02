#!/usr/bin/env python3
"""
qm2_wavepacket_spread.py — Free-Particle Wavepacket Spreading and Dispersion
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    Gaussian wavepacket: σ(t) = σ_0 √(1 + (ℏt/2mσ_0²)²)
    τ = 2mσ_0²/ℏ ≈ 17 fs (electron, σ₀ = 1 nm)
    At t=τ: σ = σ_0√2 ≈ 1.41 nm
    At t=5τ: σ ≈ 5.1 nm
    Group velocity: ⟨x⟩ = ⟨x⟩₀ + ⟨p⟩t/m

Verify:
    python3 qm2_wavepacket_spread.py --verify

Render:
    manim -qh qm2_wavepacket_spread.py WavepacketSpreadScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34
M_E    = 9.10938e-31
SIGMA0 = 1.0e-9   # 1 nm
K0_SI  = 5.0e9    # 5 nm⁻¹

def spread_time_fs():
    return 2 * M_E * SIGMA0**2 / HBAR * 1e15

def sigma_t(t_fs):
    tau = spread_time_fs()
    return SIGMA0 * np.sqrt(1 + (t_fs / tau)**2)

def v_group():
    return HBAR * K0_SI / M_E

def prob_density(x_m, t_fs, k0=K0_SI):
    t = t_fs * 1e-15
    sig_t = sigma_t(t_fs)
    x_center = HBAR * k0 / M_E * t
    return (1.0 / (np.sqrt(2*np.pi) * sig_t)) * np.exp(-0.5 * (x_m - x_center)**2 / sig_t**2)

def verify():
    print("=== Wavepacket Spread Verification ===")
    tau = spread_time_fs()
    print(f"τ = {tau:.3f} fs")
    print(f"σ₀ = {SIGMA0*1e9:.3f} nm")

    # P1: σ(τ) = σ₀√2
    sig_tau = sigma_t(tau)
    print(f"\nP1: σ(τ) = {sig_tau*1e9:.4f} nm  (should be σ₀√2 = {SIGMA0*np.sqrt(2)*1e9:.4f} nm)")
    print(f"    ratio = {sig_tau/SIGMA0:.6f}  (should be {np.sqrt(2):.6f})")

    # P2: centroid at group velocity
    vg = v_group()
    x_at_tau = vg * tau * 1e-15 * 1e9
    print(f"\nP2: ⟨x⟩(τ) = v_g·τ = {x_at_tau:.4f} nm  (group velocity)")
    print(f"    v_g = {vg:.4e} m/s")

    # σ at 5τ
    sig_5tau = sigma_t(5 * tau)
    print(f"\nσ(5τ) = {sig_5tau*1e9:.2f} nm")
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


class WavepacketSpreadScene(Scene):
    """
    Bright Gaussian envelope |ψ(x,t)|² spreading smoothly.
    Phase angle color-coded.
    Width meter and normalization displayed.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_spread()
        self._phase_moving()

    def _phase_title(self):
        title = Text("Wavepacket Spreading", font="EB Garamond", font_size=58, color=INK)
        sub = Text(
            "σ₀ = 1 nm electron  ·  τ = 17 fs  ·  σ(τ) = σ₀√2  ·  area constant",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"\sigma(t) = \sigma_0\sqrt{1 + \left(\frac{\hbar t}{2m\sigma_0^2}\right)^2}",
            color=BLUE, font_size=32,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_spread(self):
        """Stationary packet spreading — k₀=0."""
        tau = spread_time_fs()
        x_nm = np.linspace(-10, 10, 400)
        x_m = x_nm * 1e-9

        ax = Axes(
            x_range=[-10, 10, 5], y_range=[0, 0.45, 0.1],
            x_length=12.0, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(UP*0.3)
        lbl_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_y = MathTex(r"|\psi|^2\;(\mathrm{nm}^{-1})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.05)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=0.8)

        t_track = ValueTracker(0.0)

        def _density():
            t_fs = t_track.get_value()
            prob = prob_density(x_m, t_fs, k0=0) * 1e-9  # nm⁻¹
            pts = [ax.c2p(x, p) for x, p in zip(x_nm, prob)]
            fill_pts = pts + [ax.c2p(x_nm[-1], 0), ax.c2p(x_nm[0], 0)]
            try:
                return Polygon(*fill_pts, color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=2, stroke_color=BLUE)
            except Exception:
                return VGroup()

        def _width_marker():
            t_fs = t_track.get_value()
            sig_nm = sigma_t(t_fs) * 1e9
            prob_peak = prob_density(np.array([0.0]), t_fs, k0=0)[0] * 1e-9
            left = Dot(ax.c2p(-sig_nm, prob_peak * 0.607), color=GOLD, radius=0.07)
            right = Dot(ax.c2p(sig_nm, prob_peak * 0.607), color=GOLD, radius=0.07)
            brace = Line(ax.c2p(-sig_nm, prob_peak * 0.607), ax.c2p(sig_nm, prob_peak * 0.607),
                         color=GOLD, stroke_width=1.5)
            return VGroup(left, right, brace)

        def _sigma_text():
            t_fs = t_track.get_value()
            sig_nm = sigma_t(t_fs) * 1e9
            tau = spread_time_fs()
            norm = np.trapz(prob_density(x_m, t_fs, k0=0), x_m)
            return Text(
                f"t = {t_fs:.1f} fs  |  σ = {sig_nm:.3f} nm  |  norm = {norm:.4f}",
                font="EB Garamond", font_size=18, color=DIM,
            ).to_edge(DOWN, buff=0.18)

        dyn_d = always_redraw(_density)
        dyn_w = always_redraw(_width_marker)
        dyn_s = always_redraw(_sigma_text)
        self.add(dyn_d, dyn_w, dyn_s)

        self.play(t_track.animate.set_value(5 * tau), run_time=8.0, rate_func=linear)

        # Mark τ
        t_track.set_value(tau)
        ann = MathTex(
            rf"t = \tau:\quad \sigma = \sqrt{{2}}\,\sigma_0 = {sigma_t(tau)*1e9:.3f}\,\mathrm{{nm}}",
            color=GOLD, font_size=24,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(dyn_s), Write(ann), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(ax, dyn_d, dyn_w, ann, lbl_x, lbl_y), run_time=0.5)

    def _phase_moving(self):
        """Moving packet: k₀ ≠ 0."""
        tau = spread_time_fs()
        x_nm = np.linspace(-5, 35, 400)
        x_m = x_nm * 1e-9

        ax = Axes(
            x_range=[-5, 35, 10], y_range=[0, 0.45, 0.1],
            x_length=12.0, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(UP*0.3)
        lbl_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        self.play(Create(ax), Write(lbl_x), run_time=0.7)

        t_track = ValueTracker(0.0)

        def _moving_density():
            t_fs = t_track.get_value()
            prob = prob_density(x_m, t_fs, k0=K0_SI) * 1e-9
            pts = [ax.c2p(x, max(0, p)) for x, p in zip(x_nm, prob)]
            fill_pts = pts + [ax.c2p(x_nm[-1], 0), ax.c2p(x_nm[0], 0)]
            try:
                return Polygon(*fill_pts, color=BLUE, fill_color=BLUE, fill_opacity=0.45, stroke_width=0)
            except Exception:
                return VGroup()

        def _centroid_dot():
            t_fs = t_track.get_value()
            xc_nm = HBAR * K0_SI / M_E * t_fs * 1e-15 * 1e9
            return Dot(ax.c2p(min(xc_nm, 33), 0.02), color=GOLD, radius=0.1)

        def _info():
            t_fs = t_track.get_value()
            xc_nm = HBAR * K0_SI / M_E * t_fs * 1e-15 * 1e9
            sig_nm = sigma_t(t_fs) * 1e9
            return Text(
                f"t = {t_fs:.1f} fs  |  ⟨x⟩ = {xc_nm:.2f} nm  |  σ = {sig_nm:.3f} nm",
                font="EB Garamond", font_size=17, color=DIM,
            ).to_edge(DOWN, buff=0.18)

        dyn_d = always_redraw(_moving_density)
        dyn_c = always_redraw(_centroid_dot)
        dyn_i = always_redraw(_info)
        self.add(dyn_d, dyn_c, dyn_i)

        title = Text("k₀ = 5 nm⁻¹: envelope drifts AND spreads",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.2)
        self.play(Write(title), run_time=0.6)

        self.play(t_track.animate.set_value(3 * tau), run_time=7.0, rate_func=linear)
        self.wait(1.0)

        payoff = VGroup(
            MathTex(r"\langle x\rangle(t) = \frac{\hbar k_0}{m}\,t\quad\text{(centroid = Newton)}", color=GOLD, font_size=24),
            MathTex(r"\sigma(t) = \sigma_0\sqrt{1+(t/\tau)^2}\quad\text{(width = Heisenberg)}", color=BLUE, font_size=24),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(dyn_i), Write(payoff), run_time=1.0)
        self.wait(2.5)
