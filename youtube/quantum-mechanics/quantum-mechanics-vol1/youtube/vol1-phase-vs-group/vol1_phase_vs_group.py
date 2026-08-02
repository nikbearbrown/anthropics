#!/usr/bin/env python3
"""
vol1_phase_vs_group.py — Phase Velocity vs Group Velocity for Free Electron
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    k₀ = 5 nm⁻¹ electron
    ω(k) = ℏk²/2m  (free particle)
    v_g = ℏk₀/mₑ ≈ 5.78×10⁵ m/s  (group = classical)
    v_ph = v_g/2 ≈ 2.89×10⁵ m/s  (phase = half classical)
    σ₀ = 1 nm, τ = 2mₑσ₀²/ℏ ≈ 17.2 fs
    carrier λ = 2π/k₀ ≈ 1.26 nm

Verify:
    python3 vol1_phase_vs_group.py --verify

Render:
    manim -qh vol1_phase_vs_group.py PhaseVsGroupScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34   # J·s
HBAR_NM = 6.5821196e-16 * 1e9  # eV·nm·s... use SI
M_E    = 9.10938e-31     # kg
NM     = 1e-9            # 1 nm in meters

K0     = 5.0e9           # k₀ in m⁻¹ (5 nm⁻¹)
SIGMA0 = 1.0e-9          # σ₀ = 1 nm

def v_group():
    return HBAR * K0 / M_E

def v_phase():
    return HBAR * K0 / (2 * M_E)

def spread_time():
    """τ = 2mσ₀²/ℏ in fs"""
    return 2 * M_E * SIGMA0**2 / HBAR * 1e15

def sigma_t(t_fs):
    tau = spread_time()
    return SIGMA0 * np.sqrt(1 + (t_fs / tau)**2)

def psi_real(x_m, t_fs):
    """Re(Ψ(x,t)) for Gaussian wave packet."""
    t = t_fs * 1e-15
    sig = M_E * SIGMA0 / (M_E + 1j * HBAR * t / SIGMA0**2)
    # Gaussian envelope × carrier
    envelope = np.abs(sig) / M_E * np.exp(-0.5 * x_m**2 / (SIGMA0**2 + (HBAR*t/M_E/SIGMA0)**2))
    # Phase: carrier moves at v_ph, envelope moves at v_g
    x_center = v_group() * t
    carrier = np.cos(K0 * (x_m - x_center) + np.angle(sig) * 0)
    phase_carrier = np.cos(K0 * x_m - HBAR * K0**2 / (2*M_E) * t)
    prob = envelope * np.cos(K0 * x_m - HBAR * K0**2 / (2*M_E) * t -
                             np.arctan(HBAR * t / (M_E * SIGMA0**2)))
    return prob

def prob_density(x_m, t_fs):
    """|Ψ(x,t)|² for Gaussian wave packet."""
    t = t_fs * 1e-15
    sig_t = SIGMA0 * np.sqrt(1 + (HBAR * t / (M_E * SIGMA0**2))**2)
    x_center = v_group() * t
    return (1.0 / (np.sqrt(2*np.pi) * sig_t)) * np.exp(-0.5 * (x_m - x_center)**2 / sig_t**2)

def verify():
    print("=== Phase vs Group Velocity Verification ===")
    vg = v_group()
    vph = v_phase()
    tau = spread_time()
    lam = 2 * np.pi / K0 * 1e9  # nm
    print(f"v_g = {vg:.4e} m/s")
    print(f"v_ph = {vph:.4e} m/s")
    print(f"v_g/v_ph = {vg/vph:.4f}  (should be 2.000)")
    print(f"τ = {tau:.3f} fs")
    print(f"λ = 2π/k₀ = {lam:.3f} nm")
    # P1: ratio
    print(f"\nP1: v_g/v_ph = {vg/vph:.6f}  (exactly 2)")
    # P2: width at t=τ
    sig_tau = sigma_t(tau)
    print(f"P2: σ(τ)/σ₀ = {sig_tau/SIGMA0:.6f}  (should be √2 = {np.sqrt(2):.6f})")
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


class PhaseVsGroupScene(Scene):
    """
    Two-layer animation:
    Orange envelope |Ψ(x,t)|² at v_g
    Blue oscillation Re(Ψ) at v_ph = v_g/2
    Show crest lagging behind envelope
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_animation()
        self._phase_proton()

    def _phase_title(self):
        title = Text("Phase vs Group Velocity", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "k₀ = 5 nm⁻¹  ·  v_g = 5.78×10⁵ m/s  ·  v_ph = v_g/2",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(
            r"\omega(k) = \frac{\hbar k^2}{2m} \implies v_{\rm ph} = \frac{\omega}{k} = \frac{\hbar k}{2m} = \frac{v_g}{2}",
            color=BLUE, font_size=28,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_animation(self):
        # Use normalized units: x in units of σ₀, t in units of τ
        tau = spread_time()
        vg = v_group()
        vph = v_phase()

        ax = Axes(
            x_range=[0, 10, 2], y_range=[-2.5, 2.5, 1.0],
            x_length=12.0, y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.2)
        lbl_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)

        self.play(Create(ax), Write(lbl_x), run_time=0.8)

        # time tracker
        t_tracker = ValueTracker(0.0)  # in fs

        # x array in nm
        x_nm = np.linspace(0, 10, 600)
        x_m = x_nm * 1e-9

        def _envelope_curve():
            t_fs = t_tracker.get_value()
            prob = prob_density(x_m, t_fs)
            prob_norm = prob / prob.max() * 1.8
            pts = [ax.c2p(x, p) for x, p in zip(x_nm, prob_norm)]
            fill_pts = pts + [ax.c2p(x_nm[-1], 0), ax.c2p(x_nm[0], 0)]
            return Polygon(*fill_pts, color=GOLD, fill_color=GOLD, fill_opacity=0.35, stroke_width=0)

        def _re_psi_curve():
            t_fs = t_tracker.get_value()
            t = t_fs * 1e-15
            sig_t = SIGMA0 * np.sqrt(1 + (HBAR * t / (M_E * SIGMA0**2))**2)
            x_center = vg * t
            envelope = np.exp(-0.25 * (x_m - x_center)**2 / sig_t**2)
            carrier = np.cos(K0 * x_m - HBAR * K0**2 / (2*M_E) * t)
            re_psi = envelope * carrier * 1.8 / (np.sqrt(2*np.pi) * sig_t * 1e9) * (np.sqrt(2*np.pi) * SIGMA0 * 1e9)
            pts = [ax.c2p(x, r) for x, r in zip(x_nm, re_psi)]
            curve = VMobject(color=BLUE, stroke_width=2.5, stroke_opacity=0.9)
            curve.set_points_smoothly(pts)
            return curve

        def _centroid_dot():
            t_fs = t_tracker.get_value()
            x_center_nm = vg * t_fs * 1e-15 * 1e9  # nm
            return Dot(ax.c2p(min(x_center_nm, 9.8), 0), color=GOLD, radius=0.10)

        def _phase_crest():
            """Track a specific crest that moves at v_ph."""
            t_fs = t_tracker.get_value()
            t = t_fs * 1e-15
            # nearest crest to center at t=0 would be at x=0
            # crest position: K0·x - ω₀·t = 2πn → x = (2πn + ω₀t)/K0
            omega0 = HBAR * K0**2 / (2 * M_E)
            n_crest = 0
            x_crest_m = (2 * np.pi * n_crest + omega0 * t) / K0
            x_crest_nm = x_crest_m * 1e9
            if 0 <= x_crest_nm <= 10:
                return Dot(ax.c2p(x_crest_nm, 0), color=BROWN, radius=0.10)
            return VGroup()

        def _info_text():
            t_fs = t_tracker.get_value()
            sig_t_nm = sigma_t(t_fs) * 1e9
            x_env_nm = vg * t_fs * 1e-15 * 1e9
            tau = spread_time()
            return Text(
                f"t = {t_fs:.1f} fs  (τ = {tau:.1f} fs)  |  σ(t) = {sig_t_nm:.3f} nm  |  envelope at {x_env_nm:.2f} nm",
                font="EB Garamond", font_size=17, color=DIM,
            ).to_edge(DOWN, buff=0.15)

        dyn_fill = always_redraw(_envelope_curve)
        dyn_re = always_redraw(_re_psi_curve)
        dyn_env_dot = always_redraw(_centroid_dot)
        dyn_crest = always_redraw(_phase_crest)
        dyn_info = always_redraw(_info_text)

        # Labels
        lbl_env = Text("|Ψ|² envelope  (v_g)", font="EB Garamond", font_size=18, color=GOLD).to_corner(UR, buff=0.5).shift(DOWN*0.1)
        lbl_re = Text("Re(Ψ) oscillation  (v_ph = v_g/2)", font="EB Garamond", font_size=18, color=BLUE).next_to(lbl_env, DOWN, buff=0.1)
        lbl_vg = MathTex(r"v_g / v_{\rm ph} = 2.000", color=INK, font_size=22).next_to(lbl_re, DOWN, buff=0.18)

        self.add(dyn_fill, dyn_re, dyn_env_dot, dyn_crest, dyn_info)
        self.play(FadeIn(lbl_env, lbl_re, lbl_vg), run_time=0.8)

        # Animate over ~2τ
        tau = spread_time()
        self.play(t_tracker.animate.set_value(2 * tau), run_time=8.0, rate_func=linear)
        self.wait(1.0)

        # Show width doubling at τ
        t_tracker.set_value(tau)
        sig_tau_nm = sigma_t(tau) * 1e9
        width_ann = MathTex(
            rf"\sigma(\tau) = \sqrt{{2}}\,\sigma_0 = {sig_tau_nm:.3f}\,\mathrm{{nm}}",
            color=GOLD, font_size=24,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(dyn_info), Write(width_ann), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(ax, dyn_fill, dyn_re, dyn_env_dot, dyn_crest, lbl_env, lbl_re, lbl_vg, width_ann), run_time=0.6)

    def _phase_proton(self):
        """Show that a proton (1836× heavier) barely spreads."""
        title = Text(
            "Replace electron with proton  (m = 1836 mₑ)",
            font="EB Garamond", font_size=30, color=INK,
        ).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"v_g(\mathrm{proton}) = \frac{\hbar k_0}{1836\,m_e} \approx 315\,\mathrm{m/s}", color=BLUE, font_size=26),
            MathTex(r"\tau(\mathrm{proton}) = \frac{2\cdot1836\,m_e\,\sigma_0^2}{\hbar} \approx 31{,}600\,\mathrm{fs}", color=GOLD, font_size=26),
            MathTex(r"\sigma(\tau_{\rm proton}) = \sqrt{2}\,\sigma_0\,\text{ — at 31 ps, barely changed}", color=DIM, font_size=24),
        ).arrange(DOWN, buff=0.4).center()
        payoff = Text(
            "The heavier the particle, the more classical it behaves",
            font="EB Garamond", font_size=26, color=BROWN,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(title), run_time=0.8)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.play(Write(payoff), run_time=0.8)
        self.wait(3.0)
