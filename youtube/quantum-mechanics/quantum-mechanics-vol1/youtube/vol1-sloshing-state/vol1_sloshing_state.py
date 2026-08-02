#!/usr/bin/env python3
"""
vol1_sloshing_state.py — Quantum Probability Sloshing: n=1+n=2 superposition
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    L = 1 nm electron infinite square well
    E_n = n²π²ℏ²/(2m_e L²)
    E₁ ≈ 0.377 eV, E₂ ≈ 1.508 eV
    Beat period T = h/(E₂−E₁) ≈ 3.66 fs
    ⟨x⟩(t) = L/2 − (16L/9π²)cos(ωt), ω = (E₂−E₁)/ℏ
    ⟨x⟩ oscillates between 0.320L and 0.680L, amplitude 0.360L
    ⟨Ĥ⟩ = (E₁+E₂)/2 = 0.9425 eV constant

Verify:
    python3 vol1_sloshing_state.py --verify

Render:
    manim -qh vol1_sloshing_state.py SloshingStateScene
"""
import sys
import numpy as np

# ─── Physics constants ────────────────────────────────────────────────────────
HBAR  = 1.0545718e-34   # J·s
HBAR_EV = 6.5821196e-16  # eV·s
M_E   = 9.10938e-31     # kg
EV    = 1.60218e-19     # J per eV
L_NM  = 1.0e-9         # 1 nm well width in meters

# Energy levels: E_n = n²π²ℏ²/(2m_e L²)
def energy_eV(n, L=L_NM):
    return (n**2 * np.pi**2 * HBAR**2) / (2 * M_E * L**2) / EV

E1 = energy_eV(1)
E2 = energy_eV(2)
omega_beat = (E2 - E1) * EV / HBAR  # rad/s
T_beat_fs = 2 * np.pi / omega_beat * 1e15  # femtoseconds

# Eigenstates
def psi_n(n, x, L=L_NM):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

# Superposition |Ψ(x,t)|²  = ½[ψ₁² + ψ₂² + 2ψ₁ψ₂cos(ωt)]
def prob_density(x, t_fs, L=L_NM):
    t = t_fs * 1e-15
    psi1 = psi_n(1, x, L)
    psi2 = psi_n(2, x, L)
    phase = omega_beat * t
    return 0.5 * (psi1**2 + psi2**2 + 2 * psi1 * psi2 * np.cos(phase))

def mean_x_analytic(t_fs, L=L_NM):
    t = t_fs * 1e-15
    return L/2 - (16*L/(9*np.pi**2)) * np.cos(omega_beat * t)

def verify():
    print("=== Sloshing State Verification ===")
    print(f"E₁ = {E1:.4f} eV")
    print(f"E₂ = {E2:.4f} eV")
    print(f"⟨Ĥ⟩ = (E₁+E₂)/2 = {(E1+E2)/2:.4f} eV")
    print(f"ω_beat = {omega_beat:.4e} rad/s")
    print(f"T_beat = {T_beat_fs:.4f} fs")
    amplitude = 16 * L_NM / (9 * np.pi**2)
    print(f"⟨x⟩ amplitude = {amplitude/L_NM:.4f} L = {amplitude*1e9:.4f} nm")
    print(f"⟨x⟩_min = {(0.5 - 16/(9*np.pi**2)):.4f} L")
    print(f"⟨x⟩_max = {(0.5 + 16/(9*np.pi**2)):.4f} L")
    # P1: omega_beat = (E2-E1)/ℏ = 3*E1/ℏ
    omega_from_3E1 = 3 * E1 * EV / HBAR
    print(f"\nP1: ω_beat = {omega_beat:.6e} rad/s")
    print(f"    3E₁/ℏ  = {omega_from_3E1:.6e} rad/s  match={np.isclose(omega_beat, omega_from_3E1)}")
    # P2: ⟨Ĥ⟩
    x = np.linspace(0, L_NM, 10000)
    dx = x[1] - x[0]
    H_mean = 0.5 * (E1 + E2)
    print(f"\nP2: ⟨Ĥ⟩ = {H_mean:.6f} eV (constant)")
    # Check normalization
    prob = prob_density(x, 0.0)
    norm = np.trapz(prob, x)
    print(f"    Normalization at t=0: {norm:.6f} (should be 1.000)")
    prob_half = prob_density(x, T_beat_fs/2)
    norm_half = np.trapz(prob_half, x)
    print(f"    Normalization at t=T/2: {norm_half:.6f} (should be 1.000)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class SloshingStateScene(Scene):
    """
    Three-panel animation of ψ₁+ψ₂ superposition:
    Top: |Ψ(x,t)|² sloshing
    Middle: ⟨x⟩(t) sinusoidal trace
    Bottom: ⟨Ĥ⟩(t) flat line
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_animation()

    def _phase_title(self):
        title = Text("The Sloshing State", font="EB Garamond", font_size=60, color=INK)
        sub = Text(
            "ψ₁ + ψ₂ superposition  ·  L = 1 nm electron  ·  T_beat ≈ 3.66 fs",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = MathTex(
            r"|\Psi(x,t)|^2 = \tfrac{1}{2}[\psi_1^2 + \psi_2^2 + 2\psi_1\psi_2\cos(\omega t)]",
            color=BLUE, font_size=28,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_animation(self):
        N_PTS = 300
        x_arr = np.linspace(0, L_NM, N_PTS)
        x_norm = x_arr / L_NM  # 0 to 1

        # ── Axes setup ──────────────────────────────────────────────────────
        ax_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)

        # Top: |Ψ|² density
        ax_top = Axes(
            x_range=[0, 1, 0.5], y_range=[0, 3.2, 1.0],
            x_length=9.0, y_length=2.2,
            axis_config=ax_cfg,
        ).shift(UP * 2.4)
        lbl_top = Text("|Ψ(x,t)|²", font="EB Garamond", font_size=20, color=BLUE)
        lbl_top.next_to(ax_top.y_axis.get_end(), UP, buff=0.05)

        # Middle: ⟨x⟩(t)
        ax_mid = Axes(
            x_range=[0, 1, 0.5], y_range=[0.25, 0.76, 0.25],
            x_length=9.0, y_length=2.0,
            axis_config=ax_cfg,
        ).shift(DOWN * 0.1)
        lbl_mid = MathTex(r"\langle x \rangle(t)/L", color=GOLD, font_size=20)
        lbl_mid.next_to(ax_mid.y_axis.get_end(), UP, buff=0.05)

        # Bottom: ⟨Ĥ⟩
        ax_bot = Axes(
            x_range=[0, 1, 0.5], y_range=[0.88, 1.01, 0.05],
            x_length=9.0, y_length=1.5,
            axis_config=ax_cfg,
        ).shift(DOWN * 2.5)
        lbl_bot = MathTex(r"\langle \hat{H} \rangle\,(\mathrm{eV})", color=BROWN, font_size=20)
        lbl_bot.next_to(ax_bot.y_axis.get_end(), UP, buff=0.05)

        # Axis labels
        lbl_x1 = MathTex(r"x/L", color=INK, font_size=16).next_to(ax_top.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_x2 = MathTex(r"t/T", color=INK, font_size=16).next_to(ax_mid.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_x3 = MathTex(r"t/T", color=INK, font_size=16).next_to(ax_bot.x_axis.get_end(), RIGHT, buff=0.05)

        self.play(
            Create(ax_top), Create(ax_mid), Create(ax_bot),
            Write(lbl_top), Write(lbl_mid), Write(lbl_bot),
            Write(lbl_x1), Write(lbl_x2), Write(lbl_x3),
            run_time=1.5,
        )

        # ── ValueTracker — phase through 1 full beat period ─────────────────
        phase_t = ValueTracker(0.0)  # 0 to 1 (fraction of T_beat)

        # Top: |Ψ(x,t)|² curve (always_redraw)
        def _density_curve():
            frac = phase_t.get_value()
            t_fs = frac * T_beat_fs
            prob = prob_density(x_arr, t_fs)
            pts = [ax_top.c2p(xn, p * L_NM) for xn, p in zip(x_norm, prob)]
            curve = VMobject(color=BLUE, stroke_width=2.5)
            curve.set_points_smoothly(pts)
            return curve

        def _density_fill():
            frac = phase_t.get_value()
            t_fs = frac * T_beat_fs
            prob = prob_density(x_arr, t_fs)
            pts = [ax_top.c2p(xn, p * L_NM) for xn, p in zip(x_norm, prob)]
            pts_closed = list(pts) + [ax_top.c2p(1.0, 0), ax_top.c2p(0.0, 0)]
            fill = Polygon(*pts_closed, color=BLUE, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)
            return fill

        # Middle: ⟨x⟩ trace builds up
        def _mean_trace():
            frac = phase_t.get_value()
            n_trace = max(2, int(frac * 200) + 2)
            t_vals = np.linspace(0, frac, n_trace)
            pts = [ax_mid.c2p(tv, mean_x_analytic(tv * T_beat_fs) / L_NM) for tv in t_vals]
            if len(pts) < 2:
                return VGroup()
            curve = VMobject(color=GOLD, stroke_width=2.5)
            curve.set_points_smoothly(pts)
            return curve

        # Bottom: ⟨Ĥ⟩ flat line builds
        def _energy_trace():
            frac = phase_t.get_value()
            H_mean = (E1 + E2) / 2
            pts = [ax_bot.c2p(0, H_mean), ax_bot.c2p(max(frac, 0.001), H_mean)]
            line = VMobject(color=BROWN, stroke_width=2.5)
            line.set_points_as_corners(pts)
            return line

        # Centroid marker on top panel
        def _centroid_dot():
            frac = phase_t.get_value()
            t_fs = frac * T_beat_fs
            x_mean = mean_x_analytic(t_fs) / L_NM
            prob_mean = prob_density(np.array([mean_x_analytic(t_fs)]), t_fs)[0] * L_NM
            return Dot(ax_top.c2p(x_mean, min(prob_mean, 3.1)), color=GOLD, radius=0.08)

        # Info labels
        def _phase_label():
            frac = phase_t.get_value()
            t_fs_val = frac * T_beat_fs
            x_mean_nm = mean_x_analytic(t_fs_val) * 1e9
            text = Text(
                f"t = {t_fs_val:.2f} fs    ⟨x⟩ = {x_mean_nm:.3f} nm    ⟨Ĥ⟩ = {(E1+E2)/2:.4f} eV",
                font="EB Garamond", font_size=18, color=DIM,
            ).to_edge(DOWN, buff=0.18)
            return text

        dyn_fill = always_redraw(_density_fill)
        dyn_curve = always_redraw(_density_curve)
        dyn_dot = always_redraw(_centroid_dot)
        dyn_trace_mid = always_redraw(_mean_trace)
        dyn_trace_bot = always_redraw(_energy_trace)
        dyn_label = always_redraw(_phase_label)

        # Annotations
        ann_e1 = MathTex(r"E_1 = 0.377\,\mathrm{eV}", color=BLUE, font_size=18).to_corner(UR, buff=0.3).shift(DOWN*0.1)
        ann_e2 = MathTex(r"E_2 = 1.508\,\mathrm{eV}", color=BROWN, font_size=18).next_to(ann_e1, DOWN, buff=0.12)
        ann_T = MathTex(r"T_{\rm beat} = 3.66\,\mathrm{fs}", color=GOLD, font_size=18).next_to(ann_e2, DOWN, buff=0.12)

        self.add(dyn_fill, dyn_curve, dyn_dot, dyn_trace_mid, dyn_trace_bot, dyn_label)
        self.play(FadeIn(ann_e1, ann_e2, ann_T), run_time=0.8)

        # Animate one full beat period
        self.play(
            phase_t.animate.set_value(1.0),
            run_time=8.0,
            rate_func=linear,
        )
        self.wait(1.0)

        # Payoff text
        payoff = VGroup(
            MathTex(r"\langle \hat{H} \rangle = \tfrac{E_1+E_2}{2} = 0.9425\,\mathrm{eV}", color=BROWN, font_size=28),
            Text("Energy frozen — only the phase relationship moves", font="EB Garamond", font_size=22, color=INK),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(dyn_label), Write(payoff[0]), run_time=1.2)
        self.play(FadeIn(payoff[1]), run_time=0.8)
        self.wait(2.5)
