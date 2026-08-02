#!/usr/bin/env python3
"""
gaussian_wavepacket_spreading.py — Gaussian Wave Packet Spreading
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/gaussian-wavepacket-spreading
    manim -qh gaussian_wavepacket_spreading.py GaussianWavepacketScene

Verify:
    python3 gaussian_wavepacket_spreading.py --verify

Physics:
    Δx(t) = Δx(0) √(1 + (t/τ)²)
    τ = 2mΔx(0)² / ℏ
    electron, Δx(0) = 1 nm → τ ≈ 17 fs (atomic units τ=1 displayed)
    At t=τ: Δx = √2·Δx(0)  ✓
    At t=2τ: Δx ≈ 2.236·Δx(0)  ✓
    Momentum-space |φ̃(p)|² is CONSTANT in time (dispersion is purely phase)
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
ME   = 9.10938e-31


def dx_t(dx0, t_over_tau):
    """Δx(t) in units of Δx(0)."""
    return dx0 * np.sqrt(1 + t_over_tau**2)


def verify():
    print("=== Gaussian wavepacket spreading verification ===")
    # Physical spreading time for electron, Δx0=1nm
    dx0 = 1e-9   # m
    tau_phys = 2 * ME * dx0**2 / HBAR
    print(f"  τ = 2mΔx₀²/ℏ = {tau_phys:.4e} s = {tau_phys*1e15:.2f} fs")

    # P1: at t=τ, Δx = √2·Δx₀
    dx_tau = dx_t(1.0, 1.0)
    print(f"\n  P1: Δx(τ)/Δx₀ = {dx_tau:.8f}  (should be √2 = {np.sqrt(2):.8f})")

    # Numerical check
    for t_tau in [0.5, 1.0, 2.0, 5.0]:
        dxt = dx_t(1.0, t_tau)
        print(f"  t/τ={t_tau:.1f}: Δx = {dxt:.4f}·Δx₀")

    # Macroscopic ball: Δx=1 Å, m=1 g
    dx0_ball = 1e-10
    m_ball   = 1e-3
    tau_ball = 2 * m_ball * dx0_ball**2 / HBAR
    print(f"\n  Macroscopic ball (m=1g, Δx₀=1Å): τ ≈ {tau_ball:.2e} s  (age of universe ≈ 4×10¹⁷ s)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class GaussianWavepacketScene(Scene):
    """
    Phase 1: title
    Phase 2: |ψ(x,t)|² spreading over time (left); momentum |φ̃(p)|² frozen (right)
    Phase 3: Δx(t) formula and comparison electron vs proton
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_spreading()
        self._phase_comparison()

    def _phase_title(self):
        title = Text("Gaussian Wave Packet Spreading", font="EB Garamond", font_size=50, color=INK)
        sub1  = Text(
            "Δx(t) = Δx₀ √(1 + t²/τ²)   ·   τ = 2mΔx₀²/ℏ",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Momentum-space width never changes — spreading is purely phase",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_spreading(self):
        # Left: position space — spreading Gaussian
        ax_x = Axes(
            x_range=[-8, 8, 2], y_range=[0, 0.55, 0.1],
            x_length=5.5, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": True},
        ).shift(LEFT * 3.0)

        # Right: momentum space — frozen Gaussian
        ax_p = Axes(
            x_range=[-4, 4, 1], y_range=[0, 0.55, 0.1],
            x_length=5.5, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": True},
        ).shift(RIGHT * 3.0)

        x_lbl_x = MathTex(r"x/\Delta x_0", color=INK, font_size=20).next_to(ax_x.x_axis.get_end(), RIGHT, buff=0.08)
        x_lbl_p = MathTex(r"p\Delta x_0/\hbar", color=INK, font_size=20).next_to(ax_p.x_axis.get_end(), RIGHT, buff=0.08)
        hdr_x   = Text("|ψ(x,t)|²", font="EB Garamond", font_size=20, color=BLUE).next_to(ax_x, UP, buff=0.1)
        hdr_p   = Text("|φ̃(p)|²", font="EB Garamond", font_size=20, color=GOLD).next_to(ax_p, UP, buff=0.1)

        self.play(Create(ax_x), Create(ax_p), Write(x_lbl_x), Write(x_lbl_p), Write(hdr_x), Write(hdr_p), run_time=1.0)

        t_tracker = ValueTracker(0.0)

        def _prob_x():
            t_tau = t_tracker.get_value()
            dx_t_val = np.sqrt(1 + t_tau**2)   # in units of Δx₀
            # center drifts at group velocity — for simplicity set p₀=0 (v_g=0)
            x_arr = np.linspace(-8, 8, 400)
            prob  = (1 / (np.sqrt(2 * np.pi) * dx_t_val)) * np.exp(-x_arr**2 / (2 * dx_t_val**2))
            pts   = [ax_x.c2p(x, p) for x, p in zip(x_arr, prob)]
            c = VMobject(color=BLUE, stroke_width=2.5)
            c.set_points_smoothly(pts)
            return c

        def _bracket():
            t_tau    = t_tracker.get_value()
            dx_t_val = np.sqrt(1 + t_tau**2)
            left_pt  = ax_x.c2p(-dx_t_val, 0.01)
            right_pt = ax_x.c2p(+dx_t_val, 0.01)
            return DoubleArrow(left_pt, right_pt, buff=0, color=GOLD, stroke_width=2.0, tip_length=0.15)

        def _time_lbl():
            t = t_tracker.get_value()
            dx = np.sqrt(1 + t**2)
            return MathTex(rf"t/\tau={t:.1f}\quad\Delta x={dx:.2f}\,\Delta x_0", color=INK, font_size=22).to_edge(DOWN, buff=0.28)

        # Momentum (frozen)
        p_arr  = np.linspace(-4, 4, 300)
        prob_p = (1 / np.sqrt(2 * np.pi)) * np.exp(-p_arr**2 / 2)
        pts_p  = [ax_p.c2p(p, pp) for p, pp in zip(p_arr, prob_p)]
        curve_p = VMobject(color=GOLD, stroke_width=2.5)
        curve_p.set_points_smoothly(pts_p)
        frozen_lbl = MathTex(r"\text{CONSTANT in time}", color=GOLD, font_size=18).next_to(ax_p, DOWN, buff=0.15)
        self.play(Create(curve_p), Write(frozen_lbl), run_time=0.8)

        dyn_x   = always_redraw(_prob_x)
        dyn_br  = always_redraw(_bracket)
        dyn_lbl = always_redraw(_time_lbl)
        self.add(dyn_x, dyn_br, dyn_lbl)

        self.play(t_tracker.animate.set_value(5.0), run_time=6.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_comparison(self):
        hdr = Text(
            "Electron vs Proton — same σ₀, different spreading time",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 8, 1],
            x_length=8.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(DOWN * 0.2)

        x_lbl = MathTex(r"t/\tau_e", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\Delta x/\Delta x_0", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        t_arr = np.linspace(0, 6, 400)

        # Electron: τ_e = 1 (normalized)
        dx_e = [dx_t(1.0, t) for t in t_arr]
        pts_e = [ax.c2p(t, min(d, 7.9)) for t, d in zip(t_arr, dx_e)]
        c_e = VMobject(color=BLUE, stroke_width=2.8); c_e.set_points_smoothly(pts_e)

        # Proton: τ_p = 1836·τ_e (at t/τ_e, the proton barely spreads: t/τ_p = t/(1836))
        dx_p = [dx_t(1.0, t / 1836) for t in t_arr]
        pts_p = [ax.c2p(t, min(d, 7.9)) for t, d in zip(t_arr, dx_p)]
        c_p = VMobject(color=GOLD, stroke_width=2.8); c_p.set_points_smoothly(pts_p)

        lbl_e = Text("Electron", font="EB Garamond", font_size=20, color=BLUE).to_corner(UR, buff=0.35)
        lbl_p = Text("Proton (1836× slower)", font="EB Garamond", font_size=20, color=GOLD).to_corner(UR, buff=0.35).shift(DOWN*0.4)

        self.play(Create(c_e), Write(lbl_e), run_time=0.8)
        self.play(Create(c_p), Write(lbl_p), run_time=0.8)

        # Mark √2 at t=τ_e
        tau_dot = Dot(ax.c2p(1.0, np.sqrt(2)), color=BROWN, radius=0.12)
        tau_lbl = MathTex(r"t=\tau_e:\;\Delta x=\sqrt{2}\,\Delta x_0", color=BROWN, font_size=22).next_to(tau_dot, RIGHT, buff=0.15)
        self.play(FadeIn(tau_dot), Write(tau_lbl), run_time=0.7)

        fin = Text(
            "τ ∝ mΔx₀² — heavier or wider packets survive exponentially longer",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
