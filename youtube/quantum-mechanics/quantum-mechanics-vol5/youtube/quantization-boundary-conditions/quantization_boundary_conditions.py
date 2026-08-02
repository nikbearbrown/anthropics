#!/usr/bin/env python3
"""
quantization_boundary_conditions.py — Quantization from Boundary Conditions
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/quantization-boundary-conditions
    manim -qh quantization_boundary_conditions.py QuantizationBoundaryScene

Verify:
    python3 quantization_boundary_conditions.py --verify

Physics:
    L=1 nm electron; E_n = n²π²ℏ²/(2mL²)
    E₁ = 0.376 eV,  E₂ = 1.504 eV,  E₃ = 3.384 eV
    Rejected: k = 1.7π/L → ψ(L) ≠ 0
    n-th mode has exactly n−1 interior nodes
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
ME   = 9.10938e-31
EV   = 1.60218e-19
L    = 1e-9


def energy(n):
    return n**2 * np.pi**2 * HBAR**2 / (2 * ME * L**2)


def psi(x_norm, k_norm):
    """ψ(x) = sin(k_norm * π * x_norm) with x_norm ∈ [0,1]."""
    return np.sin(k_norm * np.pi * x_norm)


def verify():
    print("=== Quantization boundary conditions verification ===")
    for n in range(1, 5):
        En  = energy(n)
        print(f"  n={n}: E_{n} = {En/EV:.4f} eV")
    print()
    # Node counting: n-th wavefunction has n-1 interior nodes
    for n in range(1, 5):
        x = np.linspace(0, 1, 10000)
        y = np.sin(n * np.pi * x)
        # count sign changes in interior
        nodes = np.sum(np.diff(np.sign(y[1:-1])) != 0)
        print(f"  n={n}: interior nodes = {nodes}  (expected {n-1})")
    print()
    # Rejected wavefunction: k=1.7π/L
    x_end = psi(1.0, 1.7)
    print(f"  Rejected k=1.7π/L: ψ(L) = sin(1.7π) = {x_end:.6f}  (not zero ✓)")
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
GREEN  = "#4DB84D"
RED    = "#DD4444"


class QuantizationBoundaryScene(Scene):
    """
    Phase 1: title
    Phase 2: k slider sweeps — rejected (red) vs accepted (green) wavefunctions
    Phase 3: energy ladder with accepted n=1,2,3 frozen
    Phase 4: node counting verification
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_slider()
        self._phase_ladder()

    def _phase_title(self):
        title = Text("Quantization from Boundary Conditions", font="EB Garamond", font_size=48, color=INK)
        sub1  = Text(
            "ψ″ = −k²ψ  ·  ψ(0) = ψ(L) = 0  →  k_n = nπ/L",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Only discrete k fit — continuous energy gives discrete spectrum",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_slider(self):
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[-1.3, 1.3, 0.5],
            x_length=7.0, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).shift(LEFT * 0.5)

        x_lbl = MathTex(r"x/L", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\psi", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Vertical wall at x=1
        wall_top = ax.c2p(1.0, 1.3)
        wall_bot = ax.c2p(1.0, -1.3)
        wall = Line(wall_bot, wall_top, color=BROWN, stroke_width=4)

        k_tracker = ValueTracker(0.5)

        def _curve():
            k = k_tracker.get_value()
            x = np.linspace(0, 1, 400)
            y = np.sin(k * np.pi * x)
            end_val = abs(np.sin(k * np.pi))   # ψ(L)
            col = GREEN if end_val < 0.06 else RED
            pts = [ax.c2p(xi, yi) for xi, yi in zip(x, y)]
            c = VMobject(color=col, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        def _k_lbl():
            k = k_tracker.get_value()
            end_val = abs(np.sin(k * np.pi))
            status  = "ACCEPTED ✓" if end_val < 0.06 else "REJECTED ✗"
            col     = GREEN if end_val < 0.06 else RED
            return Text(
                f"k = {k:.2f}π/L   ψ(L) = {np.sin(k*np.pi):.3f}   {status}",
                font="EB Garamond", font_size=20, color=col,
            ).to_edge(DOWN, buff=0.28)

        dyn_curve = always_redraw(_curve)
        dyn_lbl   = always_redraw(_k_lbl)

        self.play(Create(ax), Write(x_lbl), Write(y_lbl), Create(wall), run_time=1.0)
        self.add(dyn_curve, dyn_lbl)

        hdr = Text(
            "Sweep k — only k_n = nπ/L satisfies the right wall",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.6)

        # Animate k from 0.5 to 4.0
        self.play(k_tracker.animate.set_value(4.0), run_time=8.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(ax, x_lbl, y_lbl, wall, dyn_curve, dyn_lbl, hdr), run_time=0.5)

    def _phase_ladder(self):
        # Show first 3 accepted modes stacked as energy ladder
        n_levels = [1, 2, 3]
        colors    = [BLUE, GOLD, BROWN]
        E_vals    = [energy(n) / EV for n in n_levels]
        E_max     = E_vals[-1] * 1.15

        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, E_max, E_max/4],
            x_length=6.5, y_length=4.8,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": False},
        ).shift(LEFT * 1.0)

        y_lbl = MathTex(r"E\;\mathrm{(eV)}", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax), Write(y_lbl), run_time=0.8)

        x_arr = np.linspace(0, 1, 300)
        for n, col, En in zip(n_levels, colors, E_vals):
            y_offset = En
            psi_n    = np.sin(n * np.pi * x_arr)
            scale    = 0.3 * E_max / max(abs(psi_n))

            pts = [ax.c2p(x, y_offset + scale * p) for x, p in zip(x_arr, psi_n)]
            curve = VMobject(color=col, stroke_width=2.5)
            curve.set_points_smoothly(pts)

            level_line = DashedLine(ax.c2p(0, En), ax.c2p(1, En), color=col, stroke_width=1.2)
            lbl = MathTex(f"n={n},\\;E_{n}={En:.3f}\\;\\mathrm{{eV}}", color=col, font_size=20)
            lbl.next_to(ax.c2p(1.0, En), RIGHT, buff=0.15)

            self.play(Create(level_line), Create(curve), Write(lbl), run_time=0.8)

        # Node count
        node_note = Text(
            "n-th wavefunction has n−1 interior nodes  (n=1: 0, n=2: 1, n=3: 2)",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        e_ratio = MathTex(r"E_n = n^2 E_1\quad\Rightarrow\quad E_3/E_1 = 9", color=GOLD, font_size=28).to_edge(DOWN, buff=0.28)
        self.play(Write(node_note), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(node_note), Write(e_ratio), run_time=0.8)
        self.wait(2.5)
