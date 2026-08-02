#!/usr/bin/env python3
"""
vol4_superdense_coding.py — Superdense Coding: One Qubit, Four Messages
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics:
    Pre-shared |Φ+⟩ = (|00⟩+|11⟩)/√2
    Alice encodes 2 bits by applying I/X/Z/iY to her qubit:
        00 → I|Φ+⟩ = |Φ+⟩
        01 → X|Φ+⟩ = |Ψ+⟩
        10 → Z|Φ+⟩ = |Φ-⟩
        11 → iY|Φ+⟩ = |Ψ-⟩
    Bob decodes: CNOT → H → measure in computational basis

Verify:
    python3 vol4_superdense_coding.py --verify
"""
import sys
import numpy as np

I2 = np.eye(2)
X  = np.array([[0,1],[1,0]], dtype=complex)
Z  = np.array([[1,0],[0,-1]], dtype=complex)
Y  = np.array([[0,-1j],[1j,0]], dtype=complex)
H  = np.array([[1,1],[1,-1]], dtype=complex)/np.sqrt(2)

CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)

def encode(message_bits, phi_plus):
    """Alice applies gate to her qubit (qubit A = qubit 0 of the 2-qubit state)."""
    gates = {(0,0): I2, (0,1): X, (1,0): Z, (1,1): 1j*Y}
    gate = gates[message_bits]
    # Alice operates on qubit A (first qubit)
    op = np.kron(gate, I2)
    return op @ phi_plus

def decode(state_vec):
    """Bob applies CNOT then H on qubit A."""
    H_A = np.kron(H, I2)
    return H_A @ (CNOT @ state_vec)

def verify():
    print("=== Superdense Coding verification ===")
    phi_plus = np.array([1,0,0,1], dtype=complex) / np.sqrt(2)
    messages = [(0,0), (0,1), (1,0), (1,1)]
    bell_names = ["|Φ+⟩", "|Ψ+⟩", "|Φ-⟩", "|Ψ-⟩"]

    print(f"{'Msg':>6}  {'Bell state after encode':>22}  {'Bob measures':>15}")
    for msg, bell_name in zip(messages, bell_names):
        encoded = encode(msg, phi_plus)
        decoded = decode(encoded.copy())
        # Find which basis state has amplitude ≈ ±1
        idx = np.argmax(np.abs(decoded))
        measured_bits = (idx >> 1, idx & 1)
        print(f"  {''.join(map(str,msg))!r:>6}  {bell_name:>22}  {measured_bits} ✓")
        assert measured_bits == msg, f"FAIL: decoded {measured_bits} ≠ {msg}"

    # P1: All four Bell states are orthogonal
    encoded_states = [encode(msg, phi_plus) for msg in messages]
    for i in range(4):
        for j in range(4):
            inner = np.dot(encoded_states[i].conj(), encoded_states[j]).real
            if i == j:
                assert abs(inner - 1.0) < 1e-10, f"FAIL: norm {inner}"
            else:
                assert abs(inner) < 1e-10, f"FAIL: orthogonality {i},{j}: {inner}"
    print("\nP1: All four Bell states are orthogonal  ✓")

    # P2: Before receiving Alice's qubit, Bob's state = I/2
    # ρ_B = Tr_A(|Φ+⟩⟨Φ+|) = I/2 — before encoding
    rho_phi = np.outer(phi_plus, phi_plus.conj())
    rho_B = np.trace(rho_phi.reshape(2,2,2,2), axis1=0, axis2=2)
    print(f"\nP2: ρ_B before Alice's qubit arrives = {rho_B}")
    print(f"    (should be I/2 = [[0.5,0],[0,0.5]])")
    assert np.allclose(rho_B, np.eye(2)/2), f"FAIL: ρ_B = {rho_B}"
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

MESSAGES = [(0,0), (0,1), (1,0), (1,1)]
GATES    = ["I", "X", "Z", "iY"]
BELLS    = [r"|\Phi^+\rangle", r"|\Psi^+\rangle", r"|\Phi^-\rangle", r"|\Psi^-\rangle"]
COLORS   = [BLUE, GOLD, BROWN, INK]


class SuperdenseCodingScene(Scene):
    """
    Alice applies Pauli gate → steers Bell pair → sends one qubit → Bob decodes 2 bits.
    Cycles through all four messages.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._protocol_diagram()
        self._payoff()

    def _title(self):
        t = Text("Superdense Coding", font="EB Garamond",
                 font_size=60, color=INK)
        s = Text(
            "One qubit, four messages — entanglement doubles the classical capacity",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _protocol_diagram(self):
        # Shared Bell pair line
        shared_lbl = MathTex(r"\text{Pre-shared: }|\Phi^+\rangle_{AB}",
                             color=DIM, font_size=22).to_edge(UP, buff=0.4)
        self.play(Write(shared_lbl), run_time=0.7)

        # Static diagram: Alice side, quantum channel, Bob side
        alice_box = Rectangle(width=2.8, height=2.0, color=BLUE, stroke_width=2,
                              fill_color=CANVAS, fill_opacity=1).shift(LEFT*3.5 + UP*0.5)
        alice_lbl = Text("Alice", font="EB Garamond",
                         font_size=22, color=BLUE).next_to(alice_box, UP, buff=0.08)
        alice_gate = MathTex(r"\text{Apply gate}\;G", color=BLUE, font_size=20).move_to(alice_box)

        bob_box = Rectangle(width=2.8, height=2.0, color=BROWN, stroke_width=2,
                            fill_color=CANVAS, fill_opacity=1).shift(RIGHT*3.5 + UP*0.5)
        bob_lbl = Text("Bob", font="EB Garamond",
                       font_size=22, color=BROWN).next_to(bob_box, UP, buff=0.08)
        bob_gate = MathTex(r"\text{CNOT}\to H\to\text{measure}", color=BROWN, font_size=18
                           ).move_to(bob_box)

        channel = Arrow(alice_box.get_right(), bob_box.get_left(),
                        color=GOLD, stroke_width=2.5, tip_length=0.2, buff=0.1)
        ch_lbl  = Text("send 1 qubit", font="EB Garamond",
                       font_size=16, color=GOLD).next_to(channel, UP, buff=0.08)

        self.play(
            FadeIn(alice_box, alice_lbl, alice_gate),
            FadeIn(bob_box, bob_lbl, bob_gate),
            Create(channel), Write(ch_lbl),
            run_time=1.0,
        )
        self.wait(0.5)

        # Cycle through 4 messages
        for i, (msg, gate, bell, col) in enumerate(zip(MESSAGES, GATES, BELLS, COLORS)):
            msg_str = ''.join(map(str, msg))
            msg_lbl = MathTex(
                r"\text{Message: }" + msg_str + r"\quad G=" + gate,
                color=col, font_size=22,
            ).to_edge(DOWN, buff=0.8)
            bell_lbl = MathTex(
                r"\text{Encodes to: }" + bell,
                color=col, font_size=22,
            ).to_edge(DOWN, buff=0.35)
            result_lbl = MathTex(
                r"\text{Bob reads: }" + msg_str,
                color=col, font_size=22,
            ).to_corner(DR, buff=0.35)

            self.play(Write(msg_lbl), run_time=0.5)
            self.play(Write(bell_lbl), run_time=0.5)
            self.play(Write(result_lbl), run_time=0.5)
            self.wait(0.8)
            self.play(FadeOut(msg_lbl, bell_lbl, result_lbl), run_time=0.3)

        self.play(FadeOut(alice_box, alice_lbl, alice_gate,
                          bob_box, bob_lbl, bob_gate,
                          channel, ch_lbl, shared_lbl), run_time=0.5)

    def _payoff(self):
        table = MathTex(
            r"\begin{array}{c|c|c}"
            r"\text{Bits} & G & \text{Bell state} \\ \hline"
            r"00 & I & |\Phi^+\rangle \\"
            r"01 & X & |\Psi^+\rangle \\"
            r"10 & Z & |\Phi^-\rangle \\"
            r"11 & iY & |\Psi^-\rangle"
            r"\end{array}",
            color=INK, font_size=24,
        ).shift(LEFT * 2.5)

        cap = VGroup(
            MathTex(r"\text{1 qubit} + \text{1 ebit} = \text{2 classical bits}",
                    color=GOLD, font_size=26),
            MathTex(r"\rho_B = I/2\;\text{before Alice's qubit} \Rightarrow 0\;\text{information leaks}",
                    color=BLUE, font_size=22),
        ).arrange(DOWN, buff=0.3).shift(RIGHT * 2.5)

        self.play(Write(table), run_time=1.5)
        self.play(Write(cap[0]), run_time=0.8)
        self.play(Write(cap[1]), run_time=0.8)
        self.wait(3.0)
