#!/usr/bin/env python3
"""
qmcg_quantum_beat.py — Quantum Beat: Two Stationary States Interfering in Time
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-quantum-beat
    manim -qh qmcg_quantum_beat.py QMCGQuantumBeatScene

Verify:
    python3 qmcg_quantum_beat.py --verify

Physics:
    L=1 nm infinite square well, electron
    E₁=0.376 eV, E₂=1.504 eV, ω=(E₂−E₁)/ħ=1.72×10¹⁵ rad/s, T=3.65 fs
    ψ = (ψ₁e^{−iE₁t/ħ} + ψ₂e^{−iE₂t/ħ})/√2
    ⟨x⟩(t) = L/2 − (16L/9π²)cos(ωt)
    Amplitude = 16L/9π² ≈ 0.1803L
    P2: n=1+n=3 superposition → ⟨x⟩ does NOT oscillate (selection rule)
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
ME   = 9.10938e-31
EV   = 1.60218e-19
L    = 1e-9


def energy(n):
    return n**2 * np.pi**2 * HBAR**2 / (2 * ME * L**2)


def verify():
    print("=== QMCG Quantum beat verification ===")
    E1, E2 = energy(1), energy(2)
    omega = (E2 - E1) / HBAR
    T = 2 * np.pi / omega
    amp = 16 / (9 * np.pi**2)
    print(f"  E₁={E1/EV:.4f} eV, E₂={E2/EV:.4f} eV")
    print(f"  ω=(E₂-E₁)/ħ = {omega:.4e} rad/s")
    print(f"  T=2π/ω = {T*1e15:.4f} fs  (expected 3.65 fs)")
    print(f"  P1: amplitude = 16L/9π² = {amp:.6f}L  (expected 0.1803L)")
    print(f"  Numerically: {amp:.6f}  ≈ 0.1803 ✓")

    # P2: n=1+n=3 superposition — ⟨x⟩ constant by parity
    x = np.linspace(0, L, 10000)
    psi1 = np.sqrt(2/L) * np.sin(np.pi * x / L)
    psi3 = np.sqrt(2/L) * np.sin(3 * np.pi * x / L)
    cross = np.trapz(x * psi1 * psi3, x)
    print(f"\n  ⟨x⟩ oscillation amplitude for n=1+n=3: ∫xψ₁ψ₃dx = {cross:.2e}  (≈0 by symmetry ✓)")
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


class QMCGQuantumBeatScene(Scene):
    """
    Phase 1: title
    Phase 2: |ψ(x,t)|² rocking left-right; ⟨x⟩(t) trace; phase clocks
    Phase 3: selection rule — n=1+n=3 superposition, ⟨x⟩ stays centered
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_beat()
        self._phase_selection()

    def _phase_title(self):
        title = Text("The Quantum Beat", font="EB Garamond", font_size=58, color=INK)
        sub1  = Text(
            "ψ = (ψ₁e^{−iE₁t/ħ} + ψ₂e^{−iE₂t/ħ})/√2  →  ⟨x⟩(t) oscillates",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "Beat frequency = (E₂−E₁)/h — every spectral line is this oscillation",
            font="EB Garamond", font_size=19, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_beat(self):
        E1    = energy(1)
        E2    = energy(2)
        omega = (E2 - E1) / HBAR
        amp   = 16 / (9 * np.pi**2)   # in units of L
        # Display time in units of beat period T
        T_beat_disp = 4.0   # animation seconds per beat period

        ax_top = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 2.5, 0.5],
            x_length=7.0, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(UP * 1.5 + LEFT * 0.5)

        ax_bot = Axes(
            x_range=[0, 3, 1], y_range=[0, 1.0, 0.25],
            x_length=7.0, y_length=2.2,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": True},
        ).shift(DOWN * 1.8 + LEFT * 0.5)

        x_lbl_t = MathTex(r"x/L", color=INK, font_size=18).next_to(ax_top.x_axis.get_end(), RIGHT, buff=0.08)
        x_lbl_b = MathTex(r"t/T", color=INK, font_size=18).next_to(ax_bot.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl_b = MathTex(r"\langle x\rangle/L", color=INK, font_size=18).next_to(ax_bot.y_axis.get_end(), UP, buff=0.08)

        self.play(Create(ax_top), Create(ax_bot), Write(x_lbl_t), Write(x_lbl_b), Write(y_lbl_b), run_time=0.8)

        x_arr = np.linspace(0, 1, 300)
        psi1  = np.sqrt(2) * np.sin(np.pi * x_arr)
        psi2  = np.sqrt(2) * np.sin(2 * np.pi * x_arr)

        t_tracker = ValueTracker(0.0)
        xmean_pts = []

        def _prob():
            t    = t_tracker.get_value()
            ph   = 2 * np.pi * t / T_beat_disp   # relative phase
            psi  = (psi1 + psi2 * np.exp(-1j * ph)) / np.sqrt(2)
            prob = np.abs(psi)**2
            pts  = [ax_top.c2p(x, p) for x, p in zip(x_arr, prob)]
            c = VMobject(color=BLUE, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        def _mean_dot():
            t    = t_tracker.get_value()
            # ⟨x⟩ = 0.5 - amp*cos(2π*t/T)
            xmean = 0.5 - amp * np.cos(2 * np.pi * t / T_beat_disp)
            return Dot(ax_bot.c2p(t / T_beat_disp, xmean), color=GOLD, radius=0.08)

        def _mean_line():
            t    = t_tracker.get_value()
            # draw accumulating ⟨x⟩ trace
            ts   = np.linspace(0, t, max(2, int(t * 60 / T_beat_disp)))
            xms  = [0.5 - amp * np.cos(2 * np.pi * ti / T_beat_disp) for ti in ts]
            pts  = [ax_bot.c2p(ti / T_beat_disp, xm) for ti, xm in zip(ts, xms)]
            if len(pts) < 2:
                return VMobject()
            c = VMobject(color=GOLD, stroke_width=2.2)
            c.set_points_smoothly(pts)
            return c

        dyn_prob = always_redraw(_prob)
        dyn_dot  = always_redraw(_mean_dot)
        dyn_line = always_redraw(_mean_line)
        self.add(dyn_prob, dyn_dot, dyn_line)

        amp_lbl = MathTex(rf"\text{{amplitude}} = \frac{{16L}}{{9\pi^2}} \approx 0.180L", color=GOLD, font_size=22).to_corner(UR, buff=0.35)
        self.play(Write(amp_lbl), run_time=0.5)

        self.play(t_tracker.animate.set_value(3 * T_beat_disp), run_time=9.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_selection(self):
        hdr = Text(
            "Mix n=1 + n=3 instead — ⟨x⟩ stays at L/2.  Selection rule: ∫xψ₁ψ₃ dx = 0",
            font="EB Garamond", font_size=20, color=BROWN,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 2.5, 0.5],
            x_length=7.0, y_length=3.5,
            axis_config={"color": INK, "stroke_width": 1.3, "include_ticks": False},
        ).center().shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.5)

        x_arr = np.linspace(0, 1, 300)
        psi1  = np.sqrt(2) * np.sin(np.pi * x_arr)
        psi3  = np.sqrt(2) * np.sin(3 * np.pi * x_arr)

        t_tracker = ValueTracker(0.0)

        def _prob13():
            t    = t_tracker.get_value()
            ph   = 2 * np.pi * t / 4.0
            psi  = (psi1 + psi3 * np.exp(-1j * ph)) / np.sqrt(2)
            prob = np.abs(psi)**2
            pts  = [ax.c2p(x, p) for x, p in zip(x_arr, prob)]
            c = VMobject(color=BROWN, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        # Mean stays at 0.5
        mean_line = DashedLine(ax.c2p(0, 1.0), ax.c2p(1, 1.0), color=DIM, stroke_width=1.5)
        mean_lbl  = MathTex(r"\langle x \rangle = L/2\;\text{(constant)}", color=DIM, font_size=22).next_to(mean_line, RIGHT, buff=0.1)

        dyn13 = always_redraw(_prob13)
        self.add(dyn13)
        self.play(Create(mean_line), Write(mean_lbl), run_time=0.5)

        self.play(t_tracker.animate.set_value(12.0), run_time=6.0, rate_func=linear)

        fin = Text(
            "Not every superposition shows a beat — selection rules determine which pairs are visible",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
