#!/usr/bin/env python3
"""
vol4_syndrome_bit_flip.py — Surface Code Syndrome: Bit-Flip Error Detected Without Reading the Qubit
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics:
    3-qubit bit-flip code: |ψ̄⟩ = α|000⟩ + β|111⟩
    Stabilizers: M₁ = Z₁Z₂, M₂ = Z₂Z₃
    Syndromes:
        No error: (+1, +1)
        X₁ error: (-1, +1)
        X₂ error: (-1, -1)
        X₃ error: (+1, -1)

Verify:
    python3 vol4_syndrome_bit_flip.py --verify
"""
import sys
import numpy as np

# Pauli matrices
I2 = np.eye(2)
X  = np.array([[0,1],[1,0]])
Z  = np.array([[1,0],[0,-1]])

def kron3(A, B, C):
    return np.kron(np.kron(A, B), C)

M1 = kron3(Z, Z, I2)   # Z₁Z₂
M2 = kron3(I2, Z, Z)   # Z₂Z₃

def apply_error(state_vec, qubit):
    """Apply X error on given qubit (1,2,3)."""
    if qubit == 1:
        err = kron3(X, I2, I2)
    elif qubit == 2:
        err = kron3(I2, X, I2)
    elif qubit == 3:
        err = kron3(I2, I2, X)
    else:
        err = np.eye(8)
    return err @ state_vec

def syndrome(state_vec):
    """Returns (s1, s2) in {+1, -1}."""
    ev1 = state_vec.conj() @ M1 @ state_vec
    ev2 = state_vec.conj() @ M2 @ state_vec
    return int(round(ev1.real)), int(round(ev2.real))

def verify():
    print("=== Bit-Flip Syndrome verification ===")
    # Logical |+⟩ state: (α=β=1/√2) → (|000⟩+|111⟩)/√2
    alpha, beta = 1/np.sqrt(2), 1/np.sqrt(2)
    # Basis: |000⟩=e0, |001⟩=e1, ..., |111⟩=e7
    psi_bar = np.zeros(8, dtype=complex)
    psi_bar[0] = alpha   # |000⟩
    psi_bar[7] = beta    # |111⟩

    syndromes = {}
    print(f"{'Error':>10}  {'Syndrome':>12}")
    for q in [0, 1, 2, 3]:
        psi_err = apply_error(psi_bar, q) if q > 0 else psi_bar.copy()
        s = syndrome(psi_err)
        label = f"X_{q}" if q > 0 else "None"
        syndromes[q] = s
        print(f"  {label:>8}  {str(s):>12}")

    # P1: X₂ syndrome = (−1, −1) for both α|010⟩ and β|101⟩ terms
    expected = {0: (1,1), 1: (-1,1), 2: (-1,-1), 3: (1,-1)}
    for q, s in syndromes.items():
        assert s == expected[q], f"FAIL: X_{q} syndrome {s} ≠ {expected[q]}"

    print("\nAll syndromes match expected values ✓")

    # P2: Syndrome commutes with logical Z̄ = Z₁Z₂Z₃
    Z_bar = kron3(Z, Z, Z)
    comm1 = M1 @ Z_bar - Z_bar @ M1
    comm2 = M2 @ Z_bar - Z_bar @ M2
    print(f"\nP2: [M₁, Z̄] = {np.max(np.abs(comm1)):.4f}  (should be 0)")
    print(f"    [M₂, Z̄] = {np.max(np.abs(comm2)):.4f}  (should be 0)")
    assert np.allclose(comm1, 0), "FAIL: M1 doesn't commute with Z_bar"
    assert np.allclose(comm2, 0), "FAIL: M2 doesn't commute with Z_bar"
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
RED    = "#E05252"

SYNDROME_TABLE = {
    "No error": ("+1", "+1", BLUE),
    "X₁ error": ("−1", "+1", RED),
    "X₂ error": ("−1", "−1", BROWN),
    "X₃ error": ("+1", "−1", GOLD),
}


class SyndromeBitFlipScene(Scene):
    """
    3 data qubits + 2 ancilla shown as nodes.
    X error strikes a random qubit; syndrome extraction fires;
    syndrome table lights up the matching row.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._code_diagram()
        self._syndrome_table()
        self._payoff()

    def _title(self):
        t = Text("Bit-Flip Code Syndrome", font="EB Garamond",
                 font_size=56, color=INK)
        s = Text(
            "Learn which qubit flipped without reading the logical state",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _code_diagram(self):
        # Three data qubits in a row
        DATA_Y  = 1.5
        ANCS_Y  = -0.5
        DATA_XS = [-3.5, 0, 3.5]
        ANC_XS  = [-1.75, 1.75]

        data_dots = []
        data_lbls = []
        for i, x in enumerate(DATA_XS):
            d = Circle(radius=0.4, color=BLUE, stroke_width=2.5,
                       fill_color=CANVAS, fill_opacity=1).move_to([x, DATA_Y, 0])
            l = MathTex(f"q_{i+1}", color=BLUE, font_size=20).move_to(d)
            data_dots.append(d)
            data_lbls.append(l)

        anc_dots = []
        anc_lbls = []
        for i, x in enumerate(ANC_XS):
            a = Circle(radius=0.35, color=GOLD, stroke_width=2.0,
                       fill_color=CANVAS, fill_opacity=1).move_to([x, ANCS_Y, 0])
            l = MathTex(f"a_{i+1}", color=GOLD, font_size=18).move_to(a)
            anc_dots.append(a)
            anc_lbls.append(l)

        # Connections: a₁ couples q₁,q₂; a₂ couples q₂,q₃
        lines = []
        for (qidx, aidx) in [(0,0),(1,0),(1,1),(2,1)]:
            lines.append(Line(
                [DATA_XS[qidx], DATA_Y, 0],
                [ANC_XS[aidx], ANCS_Y, 0],
                color=DIM, stroke_width=1.2,
            ))

        lbl_code = MathTex(r"|\bar{\psi}\rangle = \alpha|000\rangle + \beta|111\rangle",
                           color=INK, font_size=22).to_edge(UP, buff=0.35)

        self.play(Write(lbl_code), run_time=0.6)
        self.play(*[Create(l) for l in lines], run_time=0.6)
        self.play(*[FadeIn(d) for d in data_dots + anc_dots],
                  *[Write(l) for l in data_lbls + anc_lbls], run_time=0.8)
        self.wait(0.5)

        # ─── Animate an error on q₂ ──────────────────────────────────────
        error_lbl = Text("X₂ error strikes q₂!", font="EB Garamond",
                         font_size=21, color=RED).to_edge(DOWN, buff=0.3)
        lightning = Text("⚡", font_size=38).move_to([DATA_XS[1], DATA_Y + 0.6, 0])
        self.play(Write(error_lbl), FadeIn(lightning), run_time=0.7)
        self.play(data_dots[1].animate.set_stroke(RED).set_fill(RED, opacity=0.3), run_time=0.5)
        self.wait(0.5)

        # Syndrome extraction — ancilla flash
        synd_lbl = MathTex(r"M_1 = Z_1 Z_2:\;-1\quad M_2 = Z_2 Z_3:\;-1",
                           color=GOLD, font_size=20).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(error_lbl), Write(synd_lbl), run_time=0.7)
        self.play(
            *[a.animate.set_stroke(GOLD).set_fill(GOLD, opacity=0.3) for a in anc_dots],
            run_time=0.7,
        )
        self.wait(1.0)

        # Correction applied
        cor_lbl = Text("Syndrome (−1,−1) → X₂ identified → apply X₂ → restored",
                       font="EB Garamond", font_size=18, color=BLUE).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(synd_lbl), Write(cor_lbl), run_time=0.7)
        self.play(data_dots[1].animate.set_stroke(BLUE).set_fill(CANVAS, opacity=1), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(lbl_code, cor_lbl, lightning,
                          *data_dots, *data_lbls, *anc_dots, *anc_lbls, *lines), run_time=0.5)

    def _syndrome_table(self):
        hdr = Text("Complete syndrome table", font="EB Garamond",
                   font_size=22, color=DIM).to_edge(UP, buff=0.3)
        self.play(Write(hdr), run_time=0.5)

        rows = [
            ("No error", r"+1", r"+1", BLUE),
            (r"X_1 \text{ error}", r"-1", r"+1", RED),
            (r"X_2 \text{ error}", r"-1", r"-1", BROWN),
            (r"X_3 \text{ error}", r"+1", r"-1", GOLD),
        ]

        header = MathTex(r"\text{Error} \quad M_1 \quad M_2",
                         color=DIM, font_size=22).shift(UP * 1.8)
        self.play(Write(header), run_time=0.5)

        for i, (err, s1, s2, col) in enumerate(rows):
            y = 0.9 - i * 0.8
            row = MathTex(
                err + r" \quad " + s1 + r" \quad " + s2,
                color=col, font_size=22,
            ).shift([0, y, 0])
            self.play(Write(row), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(hdr, header), run_time=0.3)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"\text{Syndrome tells error location, not logical state}",
                    color=INK, font_size=24),
            MathTex(r"[M_1, \bar{Z}] = [M_2, \bar{Z}] = 0\;\text{(commute with logical ops)}",
                    color=GOLD, font_size=22),
            MathTex(r"\text{QEC: extract only error info, preserve }\alpha,\beta",
                    color=BLUE, font_size=24),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
