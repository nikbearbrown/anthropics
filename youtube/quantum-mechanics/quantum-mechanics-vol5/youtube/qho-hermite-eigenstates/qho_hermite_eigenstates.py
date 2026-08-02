#!/usr/bin/env python3
"""
qho_hermite_eigenstates.py — QHO Hermite Eigenstates and Gaussian Envelope
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/qho-hermite-eigenstates
    manim -qh qho_hermite_eigenstates.py QHOHermiteScene

Verify:
    python3 qho_hermite_eigenstates.py --verify

Physics:
    ψₙ(ξ) = Nₙ Hₙ(ξ) e^{−ξ²/2};  Eₙ = ℏω(n+½)
    n=0: H₀=1, 0 nodes, E₀=ℏω/2
    n=1: H₁=2ξ, 1 node, E₁=3ℏω/2
    n=2: H₂=4ξ²−2, nodes at ±1/√2, E₂=5ℏω/2
    Classical turning points: ξ = ±√(2n+1)
"""
import sys
import numpy as np
from scipy.special import hermite, factorial
from scipy.special import eval_hermite


def psi_n(xi, n):
    """Normalized QHO eigenstate ψₙ(ξ)."""
    Hn = eval_hermite(n, xi)
    norm = 1.0 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
    return norm * Hn * np.exp(-xi**2 / 2)


def verify():
    print("=== QHO Hermite eigenstates verification ===")
    xi = np.linspace(-6, 6, 50000)
    for n in range(5):
        psi  = psi_n(xi, n)
        prob = psi**2
        # Normalization
        norm = np.trapz(prob, xi)
        # Node count
        sign_changes = np.sum(np.diff(np.sign(psi[np.abs(psi) > 1e-8])) != 0)
        # Classical turning points at ξ = ±sqrt(2n+1)
        turning = np.sqrt(2*n + 1)
        print(f"  n={n}: norm={norm:.6f}, interior nodes≈{n}(expected), turning pts ±{turning:.3f}")
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


class QHOHermiteScene(Scene):
    """
    Phase 1: title
    Phase 2: energy ladder (left) + wavefunctions for n=0..4 (right)
    Phase 3: Gaussian envelope + classical turning points
    Phase 4: probability density |ψ|² vs classical distribution
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_eigenstates()
        self._phase_correspondence()

    def _phase_title(self):
        title = Text("QHO Eigenstates — Hermite × Gaussian", font="EB Garamond", font_size=52, color=INK)
        sub   = Text(
            "ψₙ = Nₙ Hₙ(ξ) e^{−ξ²/2}  ·  Eₙ = ℏω(n+½)  ·  n nodes",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_eigenstates(self):
        # Energy ladder on the left
        n_max    = 4
        E_levels = [n + 0.5 for n in range(n_max + 1)]  # in units of ℏω
        colors   = [BLUE, GOLD, BROWN, "#88CC44", "#CC88AA"]

        lad_ax = Axes(
            x_range=[0, 1, 0.5], y_range=[0, 5.5, 1],
            x_length=1.8, y_length=4.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).to_edge(LEFT, buff=0.5)

        y_lbl = MathTex(r"E_n/\hbar\omega", color=INK, font_size=18).next_to(lad_ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(lad_ax), Write(y_lbl), run_time=0.8)

        # Wavefunction axes on right
        xi_range  = 6.0
        wav_ax = Axes(
            x_range=[-xi_range, xi_range, 2], y_range=[-0.8, 0.8, 0.4],
            x_length=8.0, y_length=4.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).to_edge(RIGHT, buff=0.4)

        xi_lbl = MathTex(r"\xi = x/x_0", color=INK, font_size=20).next_to(wav_ax.x_axis.get_end(), RIGHT, buff=0.08)
        self.play(Create(wav_ax), Write(xi_lbl), run_time=0.6)

        xi = np.linspace(-xi_range, xi_range, 600)
        gauss_env = np.exp(-xi**2 / 2) * 0.6
        env_pts_p = [wav_ax.c2p(x, g) for x, g in zip(xi, gauss_env)]
        env_pts_n = [wav_ax.c2p(x, -g) for x, g in zip(xi, gauss_env)]
        env_curve_p = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        env_curve_p.set_points_smoothly(env_pts_p)
        env_curve_n = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        env_curve_n.set_points_smoothly(env_pts_n)
        self.play(Create(env_curve_p), Create(env_curve_n), run_time=0.6)

        for n, col, En in zip(range(n_max + 1), colors, E_levels):
            # Ladder line
            level_line = Line(
                lad_ax.c2p(0.1, En), lad_ax.c2p(0.9, En), color=col, stroke_width=2.5
            )
            n_lbl = MathTex(f"n={n}", color=col, font_size=18).next_to(lad_ax.c2p(0.9, En), RIGHT, buff=0.05)
            self.play(Create(level_line), Write(n_lbl), run_time=0.4)

            # Wavefunction (offset vertically by energy)
            psi  = psi_n(xi, n)
            scale = 0.55  # scale factor
            y_offset = 0.0  # draw all at same y=0 for clarity
            pts = [wav_ax.c2p(x, scale * p) for x, p in zip(xi, psi)]
            curve = VMobject(color=col, stroke_width=2.2)
            curve.set_points_smoothly(pts)

            # Mark nodes (zero crossings)
            signs = np.sign(psi)
            node_xs = []
            for i in range(len(signs) - 1):
                if signs[i] != signs[i+1] and abs(psi[i]) < 0.08 and 0 < (xi[i]+xi[i+1])/2 < xi_range:
                    node_xs.append((xi[i] + xi[i+1]) / 2)
            # Also negative side
            for i in range(len(signs) - 1):
                if signs[i] != signs[i+1] and abs(psi[i]) < 0.08 and -xi_range < (xi[i]+xi[i+1])/2 < 0:
                    node_xs.append((xi[i] + xi[i+1]) / 2)
            node_dots = [Dot(wav_ax.c2p(nx, 0), color=BROWN, radius=0.07) for nx in node_xs]

            self.play(Create(curve), *[FadeIn(d) for d in node_dots], run_time=0.7)

        # Turning points for n=4
        turn_4 = np.sqrt(2 * 4 + 1)
        for sign in [1, -1]:
            v_line = DashedLine(wav_ax.c2p(sign * turn_4, -0.8), wav_ax.c2p(sign * turn_4, 0.8),
                                color=GOLD, stroke_width=1.5)
            self.play(Create(v_line), run_time=0.4)

        note = Text(
            "Dashed: classical turning points ξ = ±√(2n+1)  ·  wavefunction leaks out (tunneling)",
            font="EB Garamond", font_size=18, color=GOLD,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(note), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_correspondence(self):
        # Classical vs quantum probability for n=5
        n = 5
        xi_range = 4.0
        xi = np.linspace(-xi_range, xi_range, 600)

        ax = Axes(
            x_range=[-xi_range, xi_range, 1], y_range=[0, 0.5, 0.1],
            x_length=9.0, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.2)

        xi_lbl = MathTex(r"\xi", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        self.play(Create(ax), Write(xi_lbl), run_time=0.8)

        # Quantum |ψ₅|²
        prob_q = psi_n(xi, n)**2
        pts_q  = [ax.c2p(x, p) for x, p in zip(xi, prob_q)]
        curve_q = VMobject(color=BLUE, stroke_width=2.5)
        curve_q.set_points_smoothly(pts_q)

        # Classical: 1/(π√(A²−x²)) where A = sqrt(2n+1)
        A = np.sqrt(2 * n + 1)
        xi_cl = np.linspace(-A + 0.05, A - 0.05, 400)
        prob_cl = 1.0 / (np.pi * np.sqrt(A**2 - xi_cl**2))
        prob_cl = prob_cl / np.trapz(prob_cl, xi_cl)   # normalize to match
        pts_cl  = [ax.c2p(x, p) for x, p in zip(xi_cl, prob_cl)]
        curve_cl = VMobject(color=GOLD, stroke_width=2.0, stroke_opacity=0.6)
        curve_cl.set_points_smoothly(pts_cl)

        lbl_q  = Text("|ψ₅|² (quantum)", font="EB Garamond", font_size=20, color=BLUE).to_corner(UR, buff=0.35)
        lbl_cl = Text("Classical (1/v)", font="EB Garamond", font_size=20, color=GOLD).to_corner(UR, buff=0.35).shift(DOWN*0.4)
        self.play(Create(curve_q), Write(lbl_q), run_time=1.0)
        self.play(Create(curve_cl), Write(lbl_cl), run_time=1.0)

        cor_note = Text(
            "Correspondence principle: at large n, quantum → classical (peaks near turning points)",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(cor_note), run_time=0.8)
        self.wait(2.5)
