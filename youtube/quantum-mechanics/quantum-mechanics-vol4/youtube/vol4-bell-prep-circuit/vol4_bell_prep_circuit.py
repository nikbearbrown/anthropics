#!/usr/bin/env python3
"""
vol4_bell_prep_circuit.py — Bell State Preparation: H + CNOT, Step by Step
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics:
    |00⟩ → (H⊗I) → |+0⟩ = (|0⟩+|1⟩)/√2 ⊗ |0⟩
           → CNOT  → |Φ+⟩ = (|00⟩+|11⟩)/√2
    After H:  det(C) = 0 (separable), r_A = (1,0,0), r_B = (0,0,1)
    After CNOT: det(C) = 1/√2, r_A = r_B = (0,0,0) (maximally mixed)

All four initial states → four Bell states:
    |00⟩ → |Φ+⟩,  |01⟩ → |Ψ+⟩,  |10⟩ → |Φ-⟩,  |11⟩ → |Ψ-⟩

Verify:
    python3 vol4_bell_prep_circuit.py --verify
"""
import sys
import numpy as np

def verify():
    print("=== Bell Prep Circuit verification ===")
    H = np.array([[1,1],[1,-1]]) / np.sqrt(2)
    I = np.eye(2)
    # CNOT: |00⟩→|00⟩, |01⟩→|01⟩, |10⟩→|11⟩, |11⟩→|10⟩
    CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    HI = np.kron(H, I)

    # P1: After H⊗I on |00⟩
    psi_00 = np.array([1,0,0,0], dtype=complex)
    psi_after_H = HI @ psi_00
    # State should be |+0⟩ = (|00⟩+|10⟩)/√2
    expected_H = np.array([1,0,1,0])/np.sqrt(2)
    assert np.allclose(psi_after_H, expected_H), f"FAIL after H: {psi_after_H}"

    # Reduced density matrix of qubit A after H
    rho_2q = np.outer(psi_after_H, psi_after_H.conj())
    rho_A  = np.trace(rho_2q.reshape(2,2,2,2), axis1=1, axis2=3)
    det_C_after_H = np.linalg.det(rho_2q.reshape(4,4))
    print(f"P1: After H⊗I, ρ_A = {rho_A}")
    print(f"    Bloch vector r_A = ({2*rho_A[0,1].real:.4f}, {2*rho_A[0,1].imag:.4f}, {(rho_A[0,0]-rho_A[1,1]).real:.4f})")
    # r_A should be (1,0,0) - check from H|0⟩ = |+⟩
    rho_Ap = np.array([[0.5, 0.5],[0.5, 0.5]])
    assert np.allclose(rho_A, rho_Ap), f"FAIL: ρ_A after H = {rho_A}"

    # P2: After CNOT
    psi_bell = CNOT @ psi_after_H
    expected_bell = np.array([1,0,0,1])/np.sqrt(2)
    assert np.allclose(psi_bell, expected_bell), f"FAIL after CNOT: {psi_bell}"
    rho_bell = np.outer(psi_bell, psi_bell.conj())
    rho_A_bell = np.trace(rho_bell.reshape(2,2,2,2), axis1=1, axis2=3)
    print(f"\nP2: After CNOT, ρ_A = {rho_A_bell}")
    print(f"    Should be I/2 = [[0.5,0],[0,0.5]]")
    purity_A = np.trace(rho_A_bell @ rho_A_bell).real
    print(f"    Purity Tr(ρ_A²) = {purity_A:.6f}  (should be 0.5)")
    assert np.allclose(rho_A_bell, np.eye(2)/2), f"FAIL: ρ_A after CNOT = {rho_A_bell}"
    assert abs(purity_A - 0.5) < 1e-10, "FAIL: purity"

    print("\nAll four Bell states:")
    states_in = [np.array([1,0,0,0]),np.array([0,1,0,0]),
                 np.array([0,0,1,0]),np.array([0,0,0,1])]
    labels = ["|00⟩","|01⟩","|10⟩","|11⟩"]
    bell_labels = ["|Φ+⟩","|Ψ+⟩","|Φ-⟩","|Ψ-⟩"]
    for psi0, label, bell in zip(states_in, labels, bell_labels):
        psi_f = CNOT @ (HI @ psi0.astype(complex))
        print(f"  {label} → {psi_f}  ≈ {bell}")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class BellPrepCircuitScene(Scene):
    """
    Two-wire circuit: H gate on qubit A, then CNOT.
    Bloch spheres shown above each wire; they collapse inward after CNOT.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._circuit_animation()
        self._payoff()

    def _title(self):
        t = Text("Bell State Preparation: H + CNOT", font="EB Garamond",
                 font_size=52, color=INK)
        s = Text(
            "One gate creates superposition; the next creates entanglement.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _make_bloch(self, center, r_vec, color, radius=0.9):
        """Draw Bloch sphere projection + Bloch vector arrow."""
        cx, cy = center
        sphere = Circle(radius=radius, color=DIM, stroke_width=1.2,
                        fill_opacity=0).move_to([cx, cy, 0])
        equator = Ellipse(width=radius*2, height=radius*0.6, color=DIM,
                          stroke_width=0.8, stroke_opacity=0.5).move_to([cx, cy, 0])
        # Bloch vector
        rx, ry_bloch, rz = r_vec
        # Project: x_screen = cx + r*(rx + 0.3*ry), y_screen = cy + r*rz
        ex = cx + radius * (rx + 0.3 * ry_bloch)
        ey = cy + radius * rz
        if rx**2 + ry_bloch**2 + rz**2 < 0.01:
            # Maximally mixed — dot at center
            vec = Dot([cx, cy, 0], radius=0.08, color=color)
        else:
            vec = Arrow([cx, cy, 0], [ex, ey, 0], color=color,
                        stroke_width=2.5, tip_length=0.18, buff=0)
        return VGroup(sphere, equator, vec)

    def _circuit_animation(self):
        Y_A =  0.8   # qubit A wire
        Y_B = -0.8   # qubit B wire
        X0  = -5.5
        X_H = -2.8
        X_CNOT = -0.5
        X_END  =  4.5

        # Wires
        w_a = Line([X0, Y_A, 0], [X_END, Y_A, 0], color=BLUE, stroke_width=2)
        w_b = Line([X0, Y_B, 0], [X_END, Y_B, 0], color=BROWN, stroke_width=2)
        lbl_a = MathTex(r"|0\rangle_A", color=BLUE, font_size=22
                        ).next_to([X0, Y_A, 0], LEFT, buff=0.1)
        lbl_b = MathTex(r"|0\rangle_B", color=BROWN, font_size=22
                        ).next_to([X0, Y_B, 0], LEFT, buff=0.1)

        self.play(Create(w_a), Create(w_b), Write(lbl_a), Write(lbl_b), run_time=0.9)

        # ─── Initial Bloch spheres ────────────────────────────────────────
        bloch_A_init = self._make_bloch((X0+0.8, Y_A+1.6), (0, 0, 1), BLUE)
        bloch_B_init = self._make_bloch((X0+0.8, Y_B-1.6), (0, 0, 1), BROWN)
        north_lbl_A = MathTex(r"|0\rangle", color=BLUE, font_size=16
                              ).next_to(bloch_A_init, UP, buff=0.05)
        north_lbl_B = MathTex(r"|0\rangle", color=BROWN, font_size=16
                              ).next_to(bloch_B_init, DOWN, buff=0.05)
        self.play(Create(bloch_A_init), Create(bloch_B_init),
                  Write(north_lbl_A), Write(north_lbl_B), run_time=0.8)

        # ─── H gate on A ─────────────────────────────────────────────────
        h_box = Square(side_length=0.65, color=BLUE, fill_color=CANVAS,
                       fill_opacity=1, stroke_width=2.5).move_to([X_H, Y_A, 0])
        h_lbl = MathTex(r"H", color=BLUE, font_size=24).move_to(h_box)
        step1 = Text("H gate: |0⟩ → |+⟩ = (|0⟩+|1⟩)/√2  [superposition, still separable]",
                     font="EB Garamond", font_size=17, color=BLUE).to_edge(DOWN, buff=0.28)

        self.play(FadeIn(h_box, h_lbl), Write(step1), run_time=0.8)

        # Update Bloch A to equator (r=(1,0,0))
        bloch_A_plus = self._make_bloch((X_H, Y_A+1.6), (1, 0, 0), BLUE)
        plus_lbl = MathTex(r"|+\rangle", color=BLUE, font_size=16
                           ).next_to(bloch_A_plus, UP, buff=0.05)
        det_lbl = MathTex(r"\det(C)=0\;\text{(separable)}", color=DIM, font_size=18
                          ).to_edge(UP, buff=0.35)

        self.play(Transform(bloch_A_init, bloch_A_plus),
                  FadeOut(north_lbl_A), Write(plus_lbl),
                  Write(det_lbl), run_time=1.0)
        self.wait(0.8)

        # ─── CNOT gate ───────────────────────────────────────────────────
        cnot_c = Dot([X_CNOT, Y_A, 0], radius=0.12, color=GOLD)
        cnot_t = Circle(radius=0.28, color=GOLD, stroke_width=2.5
                        ).move_to([X_CNOT, Y_B, 0])
        cnot_cross = VGroup(
            Line([X_CNOT-0.28, Y_B, 0], [X_CNOT+0.28, Y_B, 0], color=GOLD, stroke_width=2),
            Line([X_CNOT, Y_B-0.28, 0], [X_CNOT, Y_B+0.28, 0], color=GOLD, stroke_width=2),
        )
        cnot_vert = Line([X_CNOT, Y_A, 0], [X_CNOT, Y_B, 0],
                         color=GOLD, stroke_width=1.5)

        step2 = Text("CNOT: correlates A and B → both Bloch vectors collapse to origin",
                     font="EB Garamond", font_size=17, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(step1), FadeIn(step2), run_time=0.3)
        self.play(FadeIn(cnot_c, cnot_t, cnot_cross, cnot_vert), run_time=0.6)

        # Both Bloch spheres collapse to center (maximally mixed)
        bloch_A_mixed = self._make_bloch((X_CNOT, Y_A+1.6), (0, 0, 0), BLUE)
        bloch_B_mixed = self._make_bloch((X_CNOT, Y_B-1.6), (0, 0, 0), BROWN)
        mixed_lbl_A = MathTex(r"I/2", color=BLUE, font_size=16
                              ).next_to(bloch_A_mixed, UP, buff=0.05)
        mixed_lbl_B = MathTex(r"I/2", color=BROWN, font_size=16
                              ).next_to(bloch_B_mixed, DOWN, buff=0.05)
        det_lbl2 = MathTex(r"\det(C)=1/\sqrt{2}\;\text{(entangled)}", color=GOLD, font_size=18
                           ).to_edge(UP, buff=0.35)

        self.play(
            Transform(bloch_A_init, bloch_A_mixed),
            Transform(bloch_B_init, bloch_B_mixed),
            FadeOut(plus_lbl, north_lbl_B, det_lbl),
            Write(mixed_lbl_A), Write(mixed_lbl_B),
            Write(det_lbl2),
            run_time=1.5,
        )

        # Bell state output label
        out_lbl = MathTex(r"|\Phi^+\rangle = \tfrac{|00\rangle+|11\rangle}{\sqrt{2}}",
                          color=GOLD, font_size=24).next_to([X_END, 0, 0], RIGHT, buff=0.1)
        self.play(Write(out_lbl), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(step2), run_time=0.3)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"|00\rangle \xrightarrow{H\otimes I} |+0\rangle \xrightarrow{\rm CNOT} |\Phi^+\rangle",
                    color=INK, font_size=28),
            MathTex(r"\text{After CNOT: }\rho_A = \rho_B = I/2\;\text{(purity }= 0.5\text{)}",
                    color=GOLD, font_size=24),
            MathTex(r"\text{H creates superposition; CNOT creates entanglement}",
                    color=BLUE, font_size=24),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
