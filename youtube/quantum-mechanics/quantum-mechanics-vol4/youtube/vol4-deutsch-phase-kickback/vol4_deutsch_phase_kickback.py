#!/usr/bin/env python3
"""
vol4_deutsch_phase_kickback.py — Deutsch Algorithm: Phase Kickback Cancellation Animated
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics:
    Two-qubit circuit: q₀ (query), q₁ (ancilla in |−⟩)
    H⊗H → U_f → H on q₀ → measure q₀
    Phase kickback: U_f|x⟩|−⟩ = (−1)^f(x)|x⟩|−⟩
    Constant f: phases equal → q₀ = |0⟩ after final H
    Balanced f: phases opposite → q₀ = |1⟩ after final H

Verify:
    python3 vol4_deutsch_phase_kickback.py --verify
"""
import sys
import numpy as np

def verify():
    print("=== Deutsch Algorithm verification ===")
    H = np.array([[1,1],[1,-1]]) / np.sqrt(2)
    I2 = np.eye(2)

    # Initial state |0⟩|1⟩ → after H⊗H → |+⟩|−⟩
    psi_in = np.array([0,1,0,0], dtype=complex)   # |01⟩
    HH = np.kron(H, H)
    psi_after_HH = HH @ psi_in
    # Should be |+⟩|−⟩ = (|0⟩+|1⟩)/√2 ⊗ (|0⟩-|1⟩)/√2
    expected_HH = np.array([1, -1, 1, -1]) / 2.0
    assert np.allclose(psi_after_HH, expected_HH), f"FAIL after H⊗H: {psi_after_HH}"
    print("P0: After H⊗H: state = (|0⟩+|1⟩)/√2 ⊗ (|0⟩-|1⟩)/√2  ✓")

    # Oracle for constant f(x)=0: U_f = I (no phase flip)
    U_const = np.eye(4)
    # Oracle for balanced f(x)=x: U_f flips sign on |1x⟩ component
    # Phase kickback: U_f|x⟩|−⟩ = (-1)^f(x)|x⟩|−⟩
    # Effective action on q₀: |x⟩ → (-1)^f(x)|x⟩
    # For f(x)=x: |0⟩→|0⟩, |1⟩→-|1⟩
    U_bal = np.diag([1, -1, 1, -1])  # flip sign when x=1 (rows 1,3 which are |1⟩|0⟩ and |1⟩|1⟩...
    # More carefully: basis |00⟩,|01⟩,|10⟩,|11⟩
    # Phase kickback for f(x)=x on q₀ (x=q₀), ancilla on q₁:
    # U_f|0⟩|−⟩ = (-1)^0|0⟩|−⟩ = |0⟩|−⟩   (no change to |00⟩,|01⟩)
    # U_f|1⟩|−⟩ = (-1)^1|1⟩|−⟩ = -|1⟩|−⟩  (flip sign of |10⟩,|11⟩)
    U_bal = np.diag([1,1,-1,-1])

    # P1: Constant oracle → q₀ measures 0 with certainty
    psi_const = U_const @ psi_after_HH
    # Apply H on q₀ only
    H_q0 = np.kron(H, I2)
    psi_final_const = H_q0 @ psi_const
    prob_0_const = abs(psi_final_const[0])**2 + abs(psi_final_const[1])**2  # q₀=|0⟩ subspace
    print(f"\nP1: Constant f → P(q₀=0) = {prob_0_const:.6f}  (should be 1.0)")
    assert abs(prob_0_const - 1.0) < 1e-10, f"FAIL: P(q₀=0) = {prob_0_const}"

    # P2: Balanced oracle → q₀ measures 1 with certainty
    psi_bal = U_bal @ psi_after_HH
    psi_final_bal = H_q0 @ psi_bal
    prob_1_bal = abs(psi_final_bal[2])**2 + abs(psi_final_bal[3])**2  # q₀=|1⟩ subspace
    print(f"P2: Balanced f → P(q₀=1) = {prob_1_bal:.6f}  (should be 1.0)")
    assert abs(prob_1_bal - 1.0) < 1e-10, f"FAIL: P(q₀=1) = {prob_1_bal}"

    print("\nSingle query distinguishes constant from balanced  ✓")
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


class DeutschPhaseKickbackScene(Scene):
    """
    Two-wire circuit. Amplitudes shown as signed bars on |0⟩ and |1⟩.
    Oracle step shows phase flipping or not.
    Final H converts relative phase to measurement outcome.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._circuit_constant()
        self._circuit_balanced()
        self._payoff()

    def _title(self):
        t = Text("Deutsch Algorithm", font="EB Garamond",
                 font_size=58, color=INK)
        s = Text(
            "One quantum query — not parallelism, but interference of phases",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _amplitude_bars(self, center, amps, colors, bar_w=0.35, bar_h_scale=1.2):
        """Draw amplitude bar chart at center position."""
        bars = VGroup()
        labels = [MathTex(r"|0\rangle", color=DIM, font_size=16),
                  MathTex(r"|1\rangle", color=DIM, font_size=16)]
        cx, cy = center
        for i, (amp, col, lbl) in enumerate(zip(amps, colors, labels)):
            x = cx + (i - 0.5) * 0.8
            h = abs(amp) * bar_h_scale
            rect = Rectangle(
                width=bar_w, height=max(0.02, h),
                color=col, fill_color=col, fill_opacity=0.7 if amp >= 0 else 0.4,
                stroke_width=1.0,
            )
            rect.align_to(np.array([x - bar_w/2, cy, 0]), DL)
            # Negative amp: draw downward
            if amp < 0:
                rect.align_to(np.array([x - bar_w/2, cy - h, 0]), UL)
            sign = MathTex("+" if amp >= 0 else "-", color=col, font_size=18
                           ).next_to(rect, UP if amp >= 0 else DOWN, buff=0.05)
            lbl.next_to(rect, DOWN if amp >= 0 else UP, buff=0.05)
            bars.add(rect, sign, lbl)
        return bars

    def _draw_one_circuit(self, f_name, amps_after_oracle, outcome_text, outcome_color):
        Y_Q0 =  1.2
        Y_Q1 = -0.6
        X0   = -5.5
        X_H1 = -3.5
        X_OR = -1.5
        X_H2 =  0.5
        X_M  =  2.5
        X_END =  4.2

        # Wires
        w0 = Line([X0, Y_Q0, 0], [X_END, Y_Q0, 0], color=BLUE, stroke_width=1.8)
        w1 = Line([X0, Y_Q1, 0], [X_END, Y_Q1, 0], color=BROWN, stroke_width=1.8)
        l0 = MathTex(r"|0\rangle", color=BLUE, font_size=20).next_to([X0, Y_Q0, 0], LEFT, buff=0.1)
        l1 = MathTex(r"|1\rangle", color=BROWN, font_size=20).next_to([X0, Y_Q1, 0], LEFT, buff=0.1)
        self.play(Create(w0), Create(w1), Write(l0), Write(l1), run_time=0.7)

        # H⊗H
        h0 = Square(0.55, color=BLUE, fill_color=CANVAS, fill_opacity=1, stroke_width=2
                    ).move_to([X_H1, Y_Q0, 0])
        h0l = MathTex(r"H", color=BLUE, font_size=20).move_to(h0)
        h1 = Square(0.55, color=BROWN, fill_color=CANVAS, fill_opacity=1, stroke_width=2
                    ).move_to([X_H1, Y_Q1, 0])
        h1l = MathTex(r"H", color=BROWN, font_size=20).move_to(h1)
        self.play(FadeIn(h0, h0l, h1, h1l), run_time=0.5)

        # Amplitude bars after H⊗H (equal phases)
        bars_H = self._amplitude_bars((X_H1 + 1.0, Y_Q0 + 1.8),
                                      [1/np.sqrt(2), 1/np.sqrt(2)], [BLUE, BLUE])
        self.play(FadeIn(bars_H), run_time=0.5)

        # Oracle box
        oracle = Rectangle(width=1.2, height=abs(Y_Q0 - Y_Q1) + 0.7,
                           color=GOLD, fill_color=CANVAS, fill_opacity=1, stroke_width=2
                           ).move_to([X_OR, (Y_Q0+Y_Q1)/2, 0])
        or_lbl = MathTex(r"U_f", color=GOLD, font_size=22).move_to(oracle)
        fn_lbl = Text(f"f: {f_name}", font="EB Garamond", font_size=15, color=DIM
                      ).next_to(oracle, DOWN, buff=0.08)
        self.play(FadeIn(oracle, or_lbl, fn_lbl), run_time=0.5)

        # Amplitude bars after oracle
        bars_OR = self._amplitude_bars((X_OR + 1.2, Y_Q0 + 1.8),
                                       amps_after_oracle, [BLUE, BLUE])
        self.play(Transform(bars_H, bars_OR), run_time=0.7)

        # Final H on q₀
        h2 = Square(0.55, color=BLUE, fill_color=CANVAS, fill_opacity=1, stroke_width=2
                    ).move_to([X_H2, Y_Q0, 0])
        h2l = MathTex(r"H", color=BLUE, font_size=20).move_to(h2)
        self.play(FadeIn(h2, h2l), run_time=0.5)

        # Final amplitudes after H
        a0, a1 = amps_after_oracle
        final_amps = [(a0+a1)/np.sqrt(2), (a0-a1)/np.sqrt(2)]
        bars_final = self._amplitude_bars((X_H2+1.0, Y_Q0+1.8),
                                          final_amps, [BLUE, BLUE])
        self.play(Transform(bars_H, bars_final), run_time=0.7)

        # Measurement
        m = VGroup(
            Arc(radius=0.25, start_angle=0, angle=np.pi, color=BLUE, stroke_width=2
                ).move_to([X_M, Y_Q0, 0]),
            Arrow([X_M, Y_Q0-0.25, 0], [X_M+0.2, Y_Q0+0.1, 0],
                  color=BLUE, stroke_width=1.5, tip_length=0.12, buff=0),
        )
        self.play(FadeIn(m), run_time=0.5)
        out = Text(outcome_text, font="EB Garamond",
                   font_size=22, color=outcome_color).next_to([X_END, Y_Q0, 0], RIGHT, buff=0.1)
        self.play(Write(out), run_time=0.5)
        self.wait(1.5)

        all_objs = VGroup(w0, w1, l0, l1, h0, h0l, h1, h1l,
                          oracle, or_lbl, fn_lbl, h2, h2l, m, out, bars_H)
        self.play(FadeOut(all_objs), run_time=0.4)

    def _circuit_constant(self):
        hdr = Text("Case 1: Constant f (f(0)=f(1)=0)  →  phases equal  →  q₀ = |0⟩",
                   font="EB Garamond", font_size=18, color=BLUE).to_edge(UP, buff=0.28)
        self.play(Write(hdr), run_time=0.6)
        # After oracle (constant): both amplitudes same sign
        self._draw_one_circuit(
            "constant",
            amps_after_oracle=[1/np.sqrt(2), 1/np.sqrt(2)],
            outcome_text="Measures |0⟩ → CONSTANT",
            outcome_color=BLUE,
        )
        self.play(FadeOut(hdr), run_time=0.4)

    def _circuit_balanced(self):
        hdr = Text("Case 2: Balanced f (f(x)=x)  →  phases opposite  →  q₀ = |1⟩",
                   font="EB Garamond", font_size=18, color=GOLD).to_edge(UP, buff=0.28)
        self.play(Write(hdr), run_time=0.6)
        # After oracle (balanced): amplitudes flip sign
        self._draw_one_circuit(
            "balanced",
            amps_after_oracle=[1/np.sqrt(2), -1/np.sqrt(2)],
            outcome_text="Measures |1⟩ → BALANCED",
            outcome_color=GOLD,
        )
        self.play(FadeOut(hdr), run_time=0.4)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle",
                    color=GOLD, font_size=28, substrings_to_isolate=["kickback"]),
            MathTex(r"\text{Constant: phases equal} \rightarrow |0\rangle",
                    color=BLUE, font_size=26),
            MathTex(r"\text{Balanced: phases opposite} \rightarrow |1\rangle",
                    color=BROWN, font_size=26),
            MathTex(r"\text{One query. Classical needs two.}",
                    color=INK, font_size=26),
        ).arrange(DOWN, buff=0.35).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.8)
        self.wait(3.0)
