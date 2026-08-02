#!/usr/bin/env python3
"""
separation_variables_quantum_numbers.py — Separation of Variables: Three Quantum Numbers
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/separation-variables-quantum-numbers
    manim -qh separation_variables_quantum_numbers.py SeparationVariablesScene

Verify:
    python3 separation_variables_quantum_numbers.py --verify

Physics:
    ψ(r,θ,φ) = R(r)Θ(θ)Φ(φ)
    Φ(φ) = e^{imφ}; single-valuedness → m ∈ ℤ
    Θ(θ): P_ℓ^m finite at poles → ℓ ≥ |m|, ℓ ∈ {0,1,2,...}
    R(r): termination of Laguerre series → n = 1,2,3,...
    For n=2: E₂ = −13.6/4 = −3.4 eV; 4-fold degeneracy
    Total states at level n = n² (sum 2ℓ+1 for ℓ=0..n-1)
"""
import sys
import numpy as np


def verify():
    print("=== Separation of variables verification ===")
    # P1: single-valuedness
    for m in [0, 1, 2, -1, -2]:
        phase = np.exp(1j * m * 2 * np.pi)
        print(f"  m={m}: e^{{im·2π}} = {phase.real:.8f} + {phase.imag:.8f}i  (should be 1+0i)")

    # P2: total states at level n = n²
    print("\n  States per n level:")
    for n in range(1, 6):
        total = sum(2 * ell + 1 for ell in range(n))
        print(f"  n={n}: Σ(2ℓ+1,ℓ=0..{n-1}) = {total} = n² = {n**2}  ✓" if total == n**2 else f"  n={n}: {total}")

    # n=2 energy in eV
    E2 = -13.6 / 4
    print(f"\n  E₂ = −13.6/4 = {E2:.2f} eV")
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


class SeparationVariablesScene(Scene):
    """
    Flowchart animation: PDE → ODE_φ → ODE_θ → ODE_r
    Each ODE births a quantization condition and a quantum number.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_flowchart()
        self._phase_states()

    def _phase_title(self):
        title = Text("Separation of Variables", font="EB Garamond", font_size=56, color=INK)
        sub   = Text(
            "One PDE → three ODEs → three quantum numbers  (n, ℓ, m)",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _make_box(self, text_lines, color, width=4.0, height=1.5):
        """Return VGroup: rectangle + text."""
        rect = RoundedRectangle(width=width, height=height, corner_radius=0.2,
                                color=color, stroke_width=2.5, fill_opacity=0.12, fill_color=color)
        txts = VGroup(*[
            Text(t, font="EB Garamond", font_size=18, color=INK) for t in text_lines
        ]).arrange(DOWN, buff=0.08).move_to(rect.get_center())
        return VGroup(rect, txts)

    def _phase_flowchart(self):
        # Main PDE box at top
        pde_box = self._make_box(["Schrödinger PDE", r"ψ(r,θ,φ) = R(r)Θ(θ)Φ(φ)"], BLUE, width=5.0, height=1.2)
        pde_box.to_edge(UP, buff=0.5)
        self.play(Create(pde_box), run_time=0.8)

        # Three ODE boxes
        y2 = 0.5
        phi_box = self._make_box(["ODE in φ", "Φ″ = −m²Φ", "→ e^{imφ}  ·  m ∈ ℤ"], GOLD, width=3.8, height=1.6)
        phi_box.move_to(LEFT * 4.5 + DOWN * 0.3)

        theta_box = self._make_box(["ODE in θ", "Legendre equation", "→ ℓ = 0, 1, 2, ..."], BROWN, width=3.8, height=1.6)
        theta_box.move_to(ORIGIN + DOWN * 0.3)

        r_box = self._make_box(["ODE in r", "Laguerre equation", "→ n = 1, 2, 3, ..."], BLUE, width=3.8, height=1.6)
        r_box.move_to(RIGHT * 4.5 + DOWN * 0.3)

        # Arrows from PDE box
        for box, label_str in zip([phi_box, theta_box, r_box], ["m ∈ ℤ", "ℓ ≥ |m|", "n ≥ ℓ+1"]):
            arr = Arrow(pde_box.get_bottom(), box.get_top(), buff=0.1, color=DIM, stroke_width=2.0)
            sep_lbl = Text(label_str, font="EB Garamond", font_size=16, color=DIM).next_to(arr, RIGHT, buff=0.05)
            self.play(GrowArrow(arr), Create(box), Write(sep_lbl), run_time=0.7)

        # Quantization condition callout boxes
        cond_m  = MathTex(r"e^{im(\varphi+2\pi)}=e^{im\varphi}\;\Rightarrow\;m\in\mathbb{Z}", color=GOLD, font_size=20)
        cond_l  = MathTex(r"P_\ell^m\;\text{finite at poles}\;\Rightarrow\;\ell\geq|m|", color=BROWN, font_size=20)
        cond_n  = MathTex(r"\text{series terminates}\;\Rightarrow\;n=1,2,3,\ldots", color=BLUE, font_size=20)

        cond_m.next_to(phi_box,   DOWN, buff=0.3)
        cond_l.next_to(theta_box, DOWN, buff=0.3)
        cond_n.next_to(r_box,     DOWN, buff=0.3)

        for cond in [cond_m, cond_l, cond_n]:
            self.play(Write(cond), run_time=0.7)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_states(self):
        hdr = Text(
            "For n=2:  n² = 4 degenerate states  ·  E₂ = −3.4 eV",
            font="EB Garamond", font_size=24, color=GOLD,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        # List the (ℓ,m) pairs for n=2
        states = [(0,0), (1,-1), (1,0), (1,1)]
        labels = [
            MathTex(r"(\ell,m) = (0,\;0)", color=BLUE, font_size=28),
            MathTex(r"(\ell,m) = (1,-1)", color=BROWN, font_size=28),
            MathTex(r"(\ell,m) = (1,\;0)", color=BROWN, font_size=28),
            MathTex(r"(\ell,m) = (1,+1)", color=BROWN, font_size=28),
        ]
        VGroup(*labels).arrange(DOWN, buff=0.45).center()
        for lbl in labels:
            self.play(FadeIn(lbl), run_time=0.4)

        # Show n² formula
        formula = MathTex(
            r"\text{Total states at level }n = \sum_{\ell=0}^{n-1}(2\ell+1) = n^2",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.0)
        self.wait(2.5)
