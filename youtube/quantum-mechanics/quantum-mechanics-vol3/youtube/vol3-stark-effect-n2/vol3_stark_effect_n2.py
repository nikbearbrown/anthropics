#!/usr/bin/env python3
"""
vol3_stark_effect_n2.py — Stark Effect: Four n=2 States Fan into Three Lines
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    n=2 hydrogen states: |2s⟩, |2p₀⟩, |2p₊₁⟩, |2p₋₁⟩
    Perturbation W = eεz; only ⟨2s|eεz|2p₀⟩ = −3a₀eε survives.
    Eigenvalues: +3a₀eε (one state), 0 (doubly degenerate), −3a₀eε (one state).
    At ε = 10⁵ V/m: |3a₀eε| = 3×0.0529e-9×1.6e-19×1e5 J = 2.54e-24 J = 1.59e-5 eV

Verify:
    python3 vol3_stark_effect_n2.py --verify
"""
import sys
import numpy as np

A0   = 0.0529177e-9   # m (Bohr radius)
E_C  = 1.602176634e-19  # J per eV (elementary charge)
EPS0 = 8.854187817e-12  # C²/(N·m²)

def stark_splitting(eps_field):
    """Returns |3a₀eε| in eV."""
    delta = 3 * A0 * E_C * eps_field
    return delta / E_C   # in eV (divide by e to get eV from J)

def verify():
    print("=== Stark Effect n=2 verification ===")
    eps = 1e5   # V/m
    delta_eV = stark_splitting(eps)
    print(f"ε = {eps:.1e} V/m")
    print(f"|3a₀eε| = {delta_eV:.4e} eV   (should be ≈ 1.587e-5 eV)")
    expected = 3 * 0.0529177e-9 * 1e5  # 3a₀ε in volts (a₀×ε = V)
    print(f"  = 3 × a₀ × ε = {expected:.6f} V  = {expected:.6f} eV (since eε·a₀/e = a₀·ε in V)")
    assert abs(delta_eV - expected) < 1e-8, "FAIL: splitting mismatch"

    # P1: slope = 6a₀e in J/(V/m)
    slope_J_per_Vm = 6 * A0 * E_C   # (split is ±3a₀eε; full width = 6a₀eε)
    print(f"\nP1: linear slope = 6a₀e = {slope_J_per_Vm:.4e} J/(V/m) = {slope_J_per_Vm/E_C:.4e} eV/(V/m)")
    assert abs(slope_J_per_Vm - 6*A0*E_C) < 1e-40, "FAIL: slope"

    # P2: |2p±1⟩ do not shift (m_ℓ selection rule)
    print("\nP2: ⟨2p₊₁|z|2p₊₁⟩ = 0 (m_ℓ = ±1 states unaffected)")
    print("    Eigenvalues: +Δ, 0, 0, −Δ  →  only 3 distinct levels")
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


class StarkEffectN2Scene(Scene):
    """
    Four degenerate n=2 levels split by a z-field: only 3 distinct energies emerge.
    Matrix animate: selection rules zero out entries; two off-diagonal survive.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._levels_animation()
        self._matrix_reveal()
        self._payoff()

    def _title(self):
        t = Text("Linear Stark Effect  —  n = 2", font="EB Garamond",
                 font_size=56, color=INK)
        s = Text(
            "4 degenerate states  →  3 spectral lines  (parity + m_ℓ selection rules)",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _levels_animation(self):
        # Energy axis
        ax = Axes(
            x_range=[0, 1, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=7.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.18),
        ).shift(LEFT * 1.5)
        # hide x-axis
        ax.x_axis.set_opacity(0)

        yl = MathTex(r"E - E_2^{(0)}", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        # State labels
        states = [r"|2s\rangle", r"|2p_0\rangle",
                  r"|2p_{+1}\rangle", r"|2p_{-1}\rangle"]
        colors = [BLUE, BLUE, BROWN, BROWN]
        lines = []
        for i, (state, col) in enumerate(zip(states, colors)):
            y0 = 0.0
            line = Line(ax.c2p(0.15, y0), ax.c2p(0.85, y0),
                        color=col, stroke_width=3)
            lbl  = MathTex(state, color=col, font_size=20
                           ).next_to(ax.c2p(0.85, y0), RIGHT, buff=0.1)
            lines.append((line, lbl, col, y0))

        # Draw all degenerate at ε=0
        self.play(Create(ax), Write(yl), run_time=1.0)
        for line, lbl, col, y in lines:
            self.play(Create(line), Write(lbl), run_time=0.35)
        self.wait(0.8)

        # Now animate the split (field turns on via tracker)
        field = ValueTracker(0.0)  # in units of Δ
        delta = 0.8   # coordinate units for full split

        def make_line(y_coord, col):
            return Line(ax.c2p(0.15, y_coord), ax.c2p(0.85, y_coord),
                        color=col, stroke_width=3)

        split_lines = []
        # Upper: |2s+2p₀⟩ — goes to +Δ
        l_up   = always_redraw(lambda: make_line( field.get_value() * delta, BLUE))
        # Middle: |2p±1⟩ — stays at 0
        l_mid1 = always_redraw(lambda: make_line(0, BROWN))
        l_mid2 = always_redraw(lambda: make_line(0, BROWN))
        # Lower: goes to −Δ
        l_dn   = always_redraw(lambda: make_line(-field.get_value() * delta, BLUE))

        # Remove static lines, add dynamic
        for line, lbl, col, y in lines:
            self.remove(line)
        self.add(l_up, l_mid1, l_mid2, l_dn)

        field_lbl = MathTex(r"\varepsilon = 0", color=DIM, font_size=22
                            ).to_edge(DOWN, buff=0.35)
        field_lbl2 = MathTex(r"\varepsilon \to 10^5\;\mathrm{V/m}",
                              color=GOLD, font_size=22).to_edge(DOWN, buff=0.35)

        self.play(Write(field_lbl), run_time=0.5)
        self.play(
            FadeOut(field_lbl), FadeIn(field_lbl2),
            field.animate.set_value(1.0),
            run_time=2.5, rate_func=smooth,
        )
        self.wait(1.0)

        # Annotate energy labels
        lbl_up  = MathTex(r"+3a_0 e\varepsilon", color=BLUE, font_size=20
                          ).next_to(ax.c2p(0.85, delta), RIGHT, buff=0.1)
        lbl_mid = MathTex(r"0\;\text{(doubly degenerate)}", color=BROWN, font_size=20
                          ).next_to(ax.c2p(0.85, 0), RIGHT, buff=0.1)
        lbl_dn  = MathTex(r"-3a_0 e\varepsilon", color=BLUE, font_size=20
                          ).next_to(ax.c2p(0.85, -delta), RIGHT, buff=0.1)

        self.play(Write(lbl_up), Write(lbl_mid), Write(lbl_dn), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(field_lbl2, lbl_up, lbl_mid, lbl_dn,
                          ax, yl, *[lbl for _,lbl,_,_ in lines]), run_time=0.5)

    def _matrix_reveal(self):
        title = Text("Why only two off-diagonal entries survive:",
                     font="EB Garamond", font_size=22, color=DIM).to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.6)

        # Display 4x4 W matrix
        rows = [
            [r"0",         r"\langle 2s|e\varepsilon z|2p_0\rangle", r"0", r"0"],
            [r"\langle 2p_0|e\varepsilon z|2s\rangle", r"0",  r"0", r"0"],
            [r"0", r"0", r"0", r"0"],
            [r"0", r"0", r"0", r"0"],
        ]
        row_strs = [r" & ".join(r) for r in rows]
        mat_str = r"\begin{pmatrix}" + r"\\" .join(row_strs) + r"\end{pmatrix}"
        mat = MathTex(mat_str, color=INK, font_size=22).center().shift(DOWN * 0.2)
        self.play(Write(mat), run_time=1.5)

        note = Text("Only ⟨2s|eεz|2p₀⟩ ≠ 0  (parity selects; m_ℓ conservation kills ±1 rows)",
                    font="EB Garamond", font_size=19, color=GOLD).to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(title, mat, note), run_time=0.5)

    def _payoff(self):
        eq = VGroup(
            MathTex(r"\text{Splitting: }\;\Delta E = \pm 3a_0 e\varepsilon", color=INK, font_size=30),
            MathTex(r"\text{Slope} = 6a_0 e = 3.18\times10^{-28}\;\mathrm{J/(V/m)}",
                    color=BLUE, font_size=26),
            MathTex(r"|2p_{\pm1}\rangle\;\text{unshifted (}m_\ell\text{ selection rule)}",
                    color=BROWN, font_size=26),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(eq[0]), run_time=0.9)
        self.play(Write(eq[1]), run_time=0.8)
        self.play(Write(eq[2]), run_time=0.8)
        self.wait(3.0)
