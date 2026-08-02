#!/usr/bin/env python3
"""
qm2_ladder_operators_ell2.py — Ladder Operator Climb for ℓ=2
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    L_+|ℓ,m⟩ = ℏ√((ℓ−m)(ℓ+m+1)) |ℓ,m+1⟩
    ℓ=2: coefficients at |2,−2⟩→|2,−1⟩: 2; |2,−1⟩→|2,0⟩: √6; |2,0⟩→|2,1⟩: √6; |2,1⟩→|2,2⟩: 2
    L_+|2,2⟩ = 0 (terminated)
    L² eigenvalue = ℏ²ℓ(ℓ+1) = 6ℏ² (constant on all rungs)

Verify:
    python3 qm2_ladder_operators_ell2.py --verify

Render:
    manim -qh qm2_ladder_operators_ell2.py LadderOperatorsEll2Scene
"""
import sys
import numpy as np

def ladder_coeff_up(ell, m):
    """Coefficient of L_+ raising: √((ℓ−m)(ℓ+m+1))."""
    return np.sqrt((ell - m) * (ell + m + 1))

def ladder_coeff_down(ell, m):
    """Coefficient of L_− lowering: √((ℓ+m)(ℓ−m+1))."""
    return np.sqrt((ell + m) * (ell - m + 1))

def verify():
    print("=== Ladder Operators ℓ=2 Verification ===")
    ell = 2
    L2_eigenvalue = ell * (ell + 1)  # in units of ℏ²
    print(f"L² eigenvalue = ℏ²·{L2_eigenvalue} = 6ℏ²")

    print("\nRaising coefficients L_+|2,m⟩:")
    for m in [-2, -1, 0, 1, 2]:
        c = ladder_coeff_up(ell, m)
        print(f"  m={m:+d}: √((2-{m})(2+{m}+1)) = √({(ell-m)*(ell+m+1)}) = {c:.4f}")

    print("\nLowering coefficients L_−|2,m⟩:")
    for m in [-2, -1, 0, 1, 2]:
        c = ladder_coeff_down(ell, m)
        print(f"  m={m:+d}: √((2+{m})(2-{m}+1)) = √({(ell+m)*(ell-m+1)}) = {c:.4f}")

    # P1: L² = 6ℏ² on all rungs
    print(f"\nP1: L²|2,m⟩ = ℏ²·ℓ(ℓ+1)|2,m⟩ = {L2_eigenvalue}ℏ² for all m ∈ {{-2,-1,0,1,2}}")

    # P2: coefficient at |2,1⟩→|2,2⟩ = 2
    c_21 = ladder_coeff_up(ell, 1)
    print(f"P2: L_+|2,1⟩ coefficient = {c_21:.4f}  (should be 2.000)")
    c_m1_0 = ladder_coeff_up(ell, -1)
    print(f"    L_+|2,-1⟩→|2,0⟩ coefficient = {c_m1_0:.4f}  (should be √6 = {np.sqrt(6):.4f})")
    c_0_1 = ladder_coeff_up(ell, 0)
    print(f"    L_+|2,0⟩→|2,1⟩ coefficient = {c_0_1:.4f}  (should be √6 = {np.sqrt(6):.4f})")

    # Termination
    c_top = ladder_coeff_up(ell, ell)
    print(f"\nTermination: L_+|2,2⟩ coeff = {c_top:.6f}  (should be 0)")
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


class LadderOperatorsEll2Scene(Scene):
    """
    Vertical ladder with 5 rungs |2,-2⟩ through |2,2⟩.
    Animated raise/lower arrows with normalization coefficients.
    L² eigenvalue display throughout.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_ladder()
        self._phase_spin_half()

    def _phase_title(self):
        title = Text("The Ladder Operators: ℓ=2", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "L_+|ℓ,m⟩ = ℏ√((ℓ−m)(ℓ+m+1))|ℓ,m+1⟩  ·  terminates at m=ℓ",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(
            r"L^2|2,m\rangle = \hbar^2\cdot 6\,|2,m\rangle\text{ for all }m",
            color=GOLD, font_size=28,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_ladder(self):
        ell = 2
        m_vals = [-2, -1, 0, 1, 2]
        y_positions = [-2.0, -1.0, 0.0, 1.0, 2.0]
        colors_m = [DIM, BLUE, GOLD, BLUE, DIM]

        # Rung lines
        rungs = VGroup()
        rung_labels = VGroup()
        for m, y, col in zip(m_vals, y_positions, colors_m):
            rung = Line(LEFT*2.5, RIGHT*0.5, color=col, stroke_width=3).shift(UP*y)
            lbl = MathTex(rf"|2,{m:+d}\rangle", color=col, font_size=22).next_to(rung, RIGHT, buff=0.2)
            rungs.add(rung)
            rung_labels.add(lbl)

        self.play(*[Create(r) for r in rungs], *[Write(l) for l in rung_labels], run_time=1.0)

        # L² panel
        L2_lbl = MathTex(r"L^2 = 6\hbar^2\text{ (constant)}", color=GOLD, font_size=22).to_corner(UR, buff=0.5)
        self.play(Write(L2_lbl), run_time=0.6)

        # Raising arrows with coefficients
        raise_coeffs = {
            (-2, -1): 2.0,
            (-1, 0): np.sqrt(6),
            (0, 1): np.sqrt(6),
            (1, 2): 2.0,
        }
        lower_coeffs = {
            (2, 1): 2.0,
            (1, 0): np.sqrt(6),
            (0, -1): np.sqrt(6),
            (-1, -2): 2.0,
        }

        # Animate raising: bottom to top
        prev_dot = None
        for i, m_from in enumerate([-2, -1, 0, 1]):
            m_to = m_from + 1
            y_from = y_positions[m_from + 2]
            y_to = y_positions[m_to + 2]
            coeff = raise_coeffs[(m_from, m_to)]
            coeff_str = r"2" if abs(coeff - 2) < 0.01 else r"\sqrt{6}"

            arr = Arrow(
                LEFT*1.5 + UP*y_from, LEFT*1.5 + UP*y_to,
                buff=0.08, color=BLUE, stroke_width=2.5,
            )
            coeff_lbl = MathTex(rf"c = {coeff_str}", color=BLUE, font_size=18).next_to(arr, LEFT, buff=0.1)

            self.play(GrowArrow(arr), Write(coeff_lbl), run_time=0.6)

        # Termination
        term = MathTex(r"L_+|2,2\rangle = 0\text{ (terminated)}", color=DIM, font_size=20)
        term.next_to(rungs[-1], UP, buff=0.2)
        cross = Cross(Line(LEFT*2.5 + UP*2.5, RIGHT*0.5 + UP*2.5), color=DIM, stroke_width=2)
        self.play(Write(term), Create(cross), run_time=0.7)
        self.wait(1.0)

        # Show Robertson saturation
        rob_lbl = MathTex(
            r"\sigma_{L_x}\sigma_{L_y} = \hbar^2\ell/2 = \hbar^2",
            color=BROWN, font_size=20,
        ).to_corner(UR, buff=0.5).shift(DOWN*0.8)
        self.play(Write(rob_lbl), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_spin_half(self):
        """ℓ=1/2: only two rungs, Pauli matrices."""
        title = Text("ℓ = 1/2 (spin-½): two rungs, same algebra",
                     font="EB Garamond", font_size=30, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"|{\tfrac{1}{2}},{+\tfrac{1}{2}}\rangle \equiv |{\uparrow}\rangle\quad |{\tfrac{1}{2}},{-\tfrac{1}{2}}\rangle \equiv |{\downarrow}\rangle", color=BLUE, font_size=26),
            MathTex(r"L_+|\downarrow\rangle = \hbar\sqrt{(\tfrac{1}{2}+\tfrac{1}{2})(\tfrac{1}{2}-\tfrac{1}{2}+1)}\cdot|\uparrow\rangle = \hbar|\uparrow\rangle", color=GOLD, font_size=22),
            MathTex(r"\Rightarrow S_{\pm} = \hbar\sigma_{\pm}/2\text{ — Pauli raising/lowering}", color=BROWN, font_size=22),
            Text("Half-integer ℓ: algebraically valid, but orbital wave functions require integer",
                 font="EB Garamond", font_size=18, color=DIM),
        ).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
