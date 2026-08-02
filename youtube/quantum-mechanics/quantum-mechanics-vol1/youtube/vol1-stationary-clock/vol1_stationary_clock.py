#!/usr/bin/env python3
"""
vol1_stationary_clock.py — Stationary State: Re and Im Oscillate, |Ψ|² Doesn't
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    Infinite well n=1, L=1 nm: E₁=0.377 eV, T₁=h/E₁ ≈ 11 fs
    n=2: E₂=1.508 eV, T₂ ≈ 2.75 fs
    Re(Ψ) = ψ_n cos(Eₙt/ℏ)
    Im(Ψ) = −ψ_n sin(Eₙt/ℏ)
    |Ψ|² = |ψ_n|² (time-independent!)

Verify:
    python3 vol1_stationary_clock.py --verify

Render:
    manim -qh vol1_stationary_clock.py StationaryClockScene
"""
import sys
import numpy as np

HBAR  = 6.5821196e-16   # eV·s
M_E   = 9.10938e-31     # kg
EV    = 1.60218e-19     # J
L_NM  = 1.0e-9         # 1 nm well width

def energy_eV(n, L=L_NM):
    return (n**2 * np.pi**2 * (1.0545718e-34)**2) / (2 * M_E * L**2) / EV

E1 = energy_eV(1)  # ≈ 0.377 eV
E2 = energy_eV(2)  # ≈ 1.508 eV

T1_fs = 2 * np.pi * HBAR / E1 * 1e15  # fs
T2_fs = 2 * np.pi * HBAR / E2 * 1e15  # fs

def psi_n(n, x, L=L_NM):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def Re_Psi(n, x, t_fs, L=L_NM):
    En = energy_eV(n, L)
    omega = En / HBAR * 1e-15  # rad/fs
    return psi_n(n, x, L) * np.cos(omega * t_fs)

def Im_Psi(n, x, t_fs, L=L_NM):
    En = energy_eV(n, L)
    omega = En / HBAR * 1e-15  # rad/fs
    return -psi_n(n, x, L) * np.sin(omega * t_fs)

def prob_density(n, x, t_fs=0, L=L_NM):
    """Always |ψ_n(x)|²  — time-independent."""
    return psi_n(n, x, L)**2

def verify():
    print("=== Stationary State Clock Verification ===")
    print(f"E₁ = {E1:.4f} eV,  T₁ = {T1_fs:.3f} fs")
    print(f"E₂ = {E2:.4f} eV,  T₂ = {T2_fs:.3f} fs")

    x = np.linspace(0, L_NM, 5000)
    # P1: |Ψ|² at T/4 = |Ψ|² at t=0
    prob0 = prob_density(1, x)
    probT4 = Re_Psi(1, x, T1_fs/4)**2 + Im_Psi(1, x, T1_fs/4)**2
    max_diff = np.max(np.abs(prob0 - probT4))
    print(f"\nP1: max |ρ(t=T/4) - ρ(t=0)| = {max_diff:.2e}  (should be ~0)")

    # P2: Re(Ψ) at t=T/4 = Im(Ψ) at t=0 (up to sign)
    re_T4 = Re_Psi(1, x, T1_fs/4)
    im_0 = Im_Psi(1, x, 0)  # = 0 at t=0
    re_0 = Re_Psi(1, x, 0)
    im_T4 = Im_Psi(1, x, T1_fs/4)
    # At t=0: Re = ψ_n, Im = 0
    # At t=T/4: Re = ψ_n·cos(π/2) = 0, Im = -ψ_n·sin(π/2) = -ψ_n
    print(f"P2: Re(Ψ) at t=T/4 max = {np.max(np.abs(re_T4)):.2e}  (should be ≈0)")
    print(f"    Im(Ψ) at t=T/4: max|Im(Ψ) + ψ_1| = {np.max(np.abs(im_T4 + psi_n(1, x))):.2e}  (should be ≈0)")
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
ORANGE_COL = "#FF8C42"


class StationaryClockScene(Scene):
    """
    Three-row animation for n=1 state:
    Row 1: Re(Ψ) oscillates  (orange)
    Row 2: Im(Ψ) oscillates 90° behind  (blue)
    Row 3: |Ψ|² sits completely still  (gold filled)
    + Phase phasor inset
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_three_rows(n=1)
        self._phase_compare_n2()

    def _phase_title(self):
        title = Text("The Stationary-State Clock", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "Ψ_n spins in the complex plane — yet |Ψ_n|² never moves",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(
            r"\Psi_n(x,t) = \psi_n(x)\,e^{-iE_n t/\hbar}",
            r"\quad \Longrightarrow \quad |\Psi_n|^2 = |\psi_n|^2",
            color=BLUE, font_size=28,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_three_rows(self, n=1):
        x_arr = np.linspace(0, L_NM, 300)
        x_norm = x_arr / L_NM
        En = energy_eV(n)
        Tn = 2 * np.pi * HBAR / En * 1e15
        omega_n = En / HBAR * 1e-15  # rad/fs

        ax_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)
        # Three rows
        ax_re = Axes(x_range=[0,1,.5], y_range=[-2, 2, 1], x_length=9.0, y_length=2.0,
                     axis_config=ax_cfg).shift(UP*2.5)
        ax_im = Axes(x_range=[0,1,.5], y_range=[-2, 2, 1], x_length=9.0, y_length=2.0,
                     axis_config=ax_cfg).shift(UP*0.3)
        ax_pr = Axes(x_range=[0,1,.5], y_range=[0, 2.5, 1], x_length=9.0, y_length=2.0,
                     axis_config=ax_cfg).shift(DOWN*2.0)

        lbl_re = Text("Re(Ψ)", font="EB Garamond", font_size=18, color=ORANGE_COL).next_to(ax_re.y_axis.get_end(), UP, buff=0.05)
        lbl_im = Text("Im(Ψ)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_im.y_axis.get_end(), UP, buff=0.05)
        lbl_pr = Text("|Ψ|²  (frozen)", font="EB Garamond", font_size=18, color=GOLD).next_to(ax_pr.y_axis.get_end(), UP, buff=0.05)

        self.play(Create(ax_re), Create(ax_im), Create(ax_pr),
                  Write(lbl_re), Write(lbl_im), Write(lbl_pr), run_time=1.2)

        # Time tracker (in fs)
        t_track = ValueTracker(0.0)

        scale = 1.8 / np.sqrt(2.0 / L_NM)  # normalize to visible amplitude

        def _re_curve():
            t = t_track.get_value()
            y = Re_Psi(n, x_arr, t) * scale * L_NM
            pts = [ax_re.c2p(x, yv) for x, yv in zip(x_norm, y)]
            c = VMobject(color=ORANGE_COL, stroke_width=2.5)
            c.set_points_smoothly(pts)
            return c

        def _im_curve():
            t = t_track.get_value()
            y = Im_Psi(n, x_arr, t) * scale * L_NM
            pts = [ax_im.c2p(x, yv) for x, yv in zip(x_norm, y)]
            c = VMobject(color=BLUE, stroke_width=2.5, stroke_opacity=0.85)
            c.set_points_smoothly(pts)
            return c

        def _prob_fill():
            # always the same!
            y = psi_n(n, x_arr)**2 * scale**2 * L_NM**2 * 0.6
            pts_top = [ax_pr.c2p(x, yv) for x, yv in zip(x_norm, y)]
            pts_bot = [ax_pr.c2p(x, 0) for x in x_norm]
            fill = Polygon(*(pts_top + list(reversed(pts_bot))),
                           color=GOLD, fill_color=GOLD, fill_opacity=0.35, stroke_width=0)
            return fill

        def _phasor():
            """Small phasor circle inset."""
            t = t_track.get_value()
            angle = -omega_n * t  # rotating clockwise
            center = ax_re.c2p(0.88, 1.5)
            radius = 0.3
            end = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            circle = Circle(radius=radius, color=DIM, stroke_width=1.0).move_to(center)
            arrow = Arrow(center, end, buff=0, color=ORANGE_COL, stroke_width=2)
            return VGroup(circle, arrow)

        def _time_label():
            t = t_track.get_value()
            return Text(
                f"t = {t:.2f} fs   (T₁ = {Tn:.2f} fs)",
                font="EB Garamond", font_size=17, color=DIM,
            ).to_edge(DOWN, buff=0.18)

        dyn_re = always_redraw(_re_curve)
        dyn_im = always_redraw(_im_curve)
        dyn_pr = always_redraw(_prob_fill)
        dyn_ph = always_redraw(_phasor)
        dyn_t = always_redraw(_time_label)

        self.add(dyn_re, dyn_im, dyn_pr, dyn_ph, dyn_t)

        # Animate 2 full periods
        self.play(t_track.animate.set_value(2 * Tn), run_time=8.0, rate_func=linear)
        self.wait(1.0)

        # Payoff annotation
        payoff = MathTex(
            r"|\Psi_n|^2 = |\psi_n(x)|^2 \quad \text{(time-independent)}",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(dyn_t), Write(payoff), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(ax_re, ax_im, ax_pr, lbl_re, lbl_im, lbl_pr,
                          dyn_re, dyn_im, dyn_pr, dyn_ph, payoff), run_time=0.6)

    def _phase_compare_n2(self):
        """Switch to superposition — show |Ψ|² now moves."""
        title = Text(
            "Switch to ψ₁ + ψ₂ superposition — |Ψ|² wakes up",
            font="EB Garamond", font_size=28, color=INK,
        ).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"\Psi(x,t) = \tfrac{1}{\sqrt{2}}(\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar})", color=BLUE, font_size=26),
            MathTex(r"|\Psi|^2 = \tfrac{1}{2}[\psi_1^2 + \psi_2^2 + 2\psi_1\psi_2\cos(\omega_{21}t)]", color=GOLD, font_size=26),
            Text("⟨Ĥ⟩ frozen, but probability sloshes — see Candidate 01",
                 font="EB Garamond", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.8)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
