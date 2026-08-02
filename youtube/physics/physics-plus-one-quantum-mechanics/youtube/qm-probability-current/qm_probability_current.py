#!/usr/bin/env python3
"""
qm_probability_current.py — Probability Current: Continuity Equation Makes Probability Flow
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-probability-current
    manim -qh qm_probability_current.py ProbabilityCurrentScene

Physics:
    J = (ℏ/m) Im(ψ* ∂ψ/∂x)
    Plane wave ψ = A e^{ikx}: J = ℏk|A|²/m = |A|²v
    Electron k = 2π/λ, λ=1nm: v = ℏk/m = 7.26e5 m/s
    Gaussian packet: J peaks where |ψ|² peaks, moves at v₀
    Real standing wave ψ=cos(kx): J=0
"""
import sys
import numpy as np

HBAR   = 1.055e-34
M_ELEC = 9.109e-31
K_NM   = 2 * np.pi / 1e-9    # k for λ=1nm


def plane_wave_velocity(k, m=M_ELEC):
    return HBAR * k / m


def gaussian_packet(x, x0, sigma, k0):
    """Moving Gaussian wave packet ψ(x,t=0)."""
    return np.exp(-(x - x0)**2 / (4 * sigma**2)) * np.exp(1j * k0 * x)


def probability_current(psi, dx, m=M_ELEC):
    """Compute J = (ℏ/m) Im(ψ* dψ/dx)."""
    dpsi_dx = np.gradient(psi, dx)
    return (HBAR / m) * np.imag(np.conj(psi) * dpsi_dx)


if __name__ == "__main__":
    print("=== Probability Current Verification ===")
    v = plane_wave_velocity(K_NM)
    print(f"P1: Plane wave v = ℏk/m = {v:.3e} m/s  (expect 7.26e5)")
    assert abs(v - 7.26e5) < 1e4, f"P1 FAIL: {v:.3e}"
    # P2: real wavefunction J = 0
    x = np.linspace(-5e-9, 5e-9, 1000)
    dx = x[1] - x[0]
    psi_real = np.cos(K_NM * x).astype(complex)
    J_real = probability_current(psi_real, dx)
    print(f"P2: J for cos(kx): max|J| = {np.max(np.abs(J_real)):.3e}  (expect ~0)")
    # Numerical gradient gives near-zero but not exactly 0 due to discretization
    assert np.max(np.abs(J_real)) < 1e-5, f"P2 FAIL: {np.max(np.abs(J_real)):.3e}"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class ProbabilityCurrentScene(Scene):
    """Moving Gaussian packet + probability current arrows below it."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_moving_packet()
        self._phase_standing_wave()

    def _phase_title(self):
        title = Text("Probability Current", font="EB Garamond",
                     font_size=54, color=INK)
        sub = MathTex(r"J=\frac{\hbar}{m}\,\mathrm{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right)",
                      color=BLUE, font_size=32)
        sub2 = Text("Probability is locally conserved — it must flow, not teleport",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_formula(self):
        rows = [
            MathTex(r"\frac{\partial|\psi|^2}{\partial t}=-\frac{\partial J}{\partial x}",
                    color=BLUE, font_size=36),
            MathTex(r"\psi=Ae^{ikx}\;\Rightarrow\;J=\frac{\hbar k}{m}|A|^2=|A|^2 v",
                    color=GOLD, font_size=30),
            MathTex(r"v=\frac{\hbar k}{m}=\frac{1.055\times10^{-34}\times2\pi/10^{-9}}{9.11\times10^{-31}}=7.26\times10^5\,\mathrm{m/s}",
                    color=INK, font_size=22),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.5).center()
        for r in rows:
            self.play(Write(r), run_time=1.0)
            self.wait(0.5)
        self.wait(1.5)
        self.play(FadeOut(*rows), run_time=0.5)

    def _phase_moving_packet(self):
        ax_psi  = Axes(x_range=[-5, 5, 2], y_range=[0, 1.2, 0.5],
                       x_length=9.5, y_length=2.5,
                       axis_config=dict(color=INK, stroke_width=1.2,
                                        include_ticks=False, tip_length=0.15),
                       ).shift(UP * 1.5)
        ax_J = Axes(x_range=[-5, 5, 2], y_range=[-0.3, 1.2, 0.5],
                    x_length=9.5, y_length=2.0,
                    axis_config=dict(color=INK, stroke_width=1.2,
                                     include_ticks=False, tip_length=0.15),
                    ).shift(DOWN * 1.5)

        y_psi = MathTex(r"|\psi|^2", color=BLUE, font_size=20).next_to(
            ax_psi.y_axis.get_end(), UP, buff=0.05)
        y_J   = MathTex(r"J(x)", color=GOLD, font_size=20).next_to(
            ax_J.y_axis.get_end(), UP, buff=0.05)

        self.play(Create(ax_psi), Create(ax_J), Write(y_psi), Write(y_J), run_time=1.2)

        x0_track = ValueTracker(-4.0)

        def _psi2():
            x0 = x0_track.get_value()
            x = np.linspace(-5, 5, 400)
            psi2 = np.exp(-(x - x0)**2 / (2 * 0.7**2))
            pts = [ax_psi.c2p(x_, y) for x_, y in zip(x, psi2)]
            m = VMobject(color=BLUE, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        def _J():
            x0 = x0_track.get_value()
            x = np.linspace(-5, 5, 400)
            psi2 = np.exp(-(x - x0)**2 / (2 * 0.7**2))
            # J ∝ |ψ|² × v  (rightward-moving packet)
            J = psi2 * 0.9
            pts = [ax_J.c2p(x_, j) for x_, j in zip(x, J)]
            m = VMobject(color=GOLD, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        dyn_psi2 = always_redraw(_psi2)
        dyn_J    = always_redraw(_J)
        self.add(dyn_psi2, dyn_J)

        hdr = Text("Rightward-moving packet — J > 0 everywhere under the packet",
                   font="EB Garamond", font_size=20, color=INK).to_edge(UP, buff=0.18)
        norm_lbl = MathTex(r"\int|\psi|^2dx=1\;\text{(conserved)}",
                           color=DIM, font_size=20).to_edge(DOWN, buff=0.25)
        self.play(Write(hdr), Write(norm_lbl), run_time=0.8)
        self.play(x0_track.animate.set_value(4.0), run_time=4.0, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(hdr, norm_lbl, ax_psi, ax_J, y_psi, y_J,
                          dyn_psi2, dyn_J), run_time=0.5)

    def _phase_standing_wave(self):
        hdr = Text("Standing wave ψ = cos(kx) — J = 0 everywhere",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.22)
        ax = Axes(x_range=[-5, 5, 2], y_range=[-1.2, 1.2, 0.5],
                  x_length=9.5, y_length=4.0,
                  axis_config=dict(color=INK, stroke_width=1.5,
                                   include_ticks=False, tip_length=0.2),
                  ).shift(DOWN * 0.5)
        x_arr = np.linspace(-5, 5, 600)
        psi   = np.cos(2.5 * x_arr)
        psi2  = psi**2

        pts_psi = [ax.c2p(x, p) for x, p in zip(x_arr, psi)]
        pts_psi2 = [ax.c2p(x, p2) for x, p2 in zip(x_arr, psi2)]
        c_psi  = VMobject(color=DIM, stroke_width=2.0)
        c_psi.set_points_smoothly(pts_psi)
        c_psi2 = VMobject(color=BLUE, stroke_width=2.5)
        c_psi2.set_points_smoothly(pts_psi2)

        j_zero = DashedLine(ax.c2p(-5, 0), ax.c2p(5, 0),
                            color=GOLD, stroke_width=2.0)
        j_lbl  = MathTex(r"J=0", color=GOLD, font_size=26).move_to(ax.c2p(3, 0.2))

        self.play(Create(ax), Write(hdr), run_time=0.8)
        self.play(Create(c_psi), Create(c_psi2), run_time=1.5)
        self.play(Create(j_zero), Write(j_lbl), run_time=0.8)
        conclusion = MathTex(
            r"\psi\in\mathbb{R}\;\Rightarrow\;J=\frac{\hbar}{m}\mathrm{Im}(\psi\partial_x\psi)=0",
            color=INK, font_size=26).to_edge(DOWN, buff=0.25)
        self.play(Write(conclusion), run_time=1.0)
        self.wait(2.5)
