#!/usr/bin/env python3
"""
vol3_hydrogen_fine_structure.py — Fine Structure of Hydrogen n=2: Three Scales, Three Mechanisms
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    Bohr:  E₂ = −3.4 eV
    Fine structure (j-dependent only):
        E_fs = −(E_n²/2mc²)·[4n/(j+½) − 3]
        For n=2, j=½:   E_fs = −5.66×10⁻⁵ eV
        For n=2, j=3/2: E_fs = −1.13×10⁻⁵ eV
        Splitting ΔE_fs = 4.53×10⁻⁵ eV
    Lamb shift:  ΔE_Lamb ≈ 4×10⁻⁶ eV  (2s₁/₂ above 2p₁/₂)

Verify:
    python3 vol3_hydrogen_fine_structure.py --verify
"""
import sys
import numpy as np

ALPHA  = 7.2973525693e-3   # fine structure constant
M_E_C2 = 0.51099895e6      # eV (electron rest energy)
E2_BOHR = -3.4             # eV

def E_fine_structure(n, j):
    """Fine-structure correction in eV for hydrogen state (n, j)."""
    E_n = -13.6 / n**2  # eV
    return -(E_n**2 / (2 * M_E_C2)) * (4*n/(j + 0.5) - 3)

def verify():
    print("=== Hydrogen Fine Structure verification ===")
    print(f"E₂ (Bohr) = {E2_BOHR} eV")
    print()

    # n=2 states
    for j, label in [(0.5, "j=1/2 (2s₁/₂, 2p₁/₂)"), (1.5, "j=3/2 (2p₃/₂)")]:
        Efs = E_fine_structure(2, j)
        print(f"  E_fs(n=2, {label}) = {Efs:.4e} eV")

    Efs_half = E_fine_structure(2, 0.5)
    Efs_3half = E_fine_structure(2, 1.5)
    splitting = abs(Efs_half - Efs_3half)
    print(f"\nFine-structure splitting ΔE_fs = {splitting:.4e} eV  (should be ≈ 4.53×10⁻⁵ eV)")
    assert abs(splitting - 4.53e-5) < 0.1e-5, f"FAIL: splitting {splitting:.4e}"

    # P1: 2s₁/₂ and 2p₁/₂ degenerate under fine structure (same j=1/2)
    print(f"\nP1: E_fs(2s₁/₂) = E_fs(2p₁/₂) = {Efs_half:.4e} eV  (both j=1/2, exact degeneracy)")

    # P2: Lamb shift ratio
    lamb = 4e-6  # eV
    ratio = splitting / lamb
    print(f"\nP2: Lamb shift ≈ {lamb:.1e} eV  ≈ 1/{ratio:.0f} × fine-structure splitting")
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


class HydrogenFineStructureScene(Scene):
    """
    Three-stage zoom: Bohr → fine structure → Lamb shift.
    Energy axis rescales by factor ~10 at each stage.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._stage1_bohr()
        self._stage2_fine_structure()
        self._stage3_lamb_shift()
        self._payoff()

    def _title(self):
        t = Text("Hydrogen n=2: Three Scales", font="EB Garamond",
                 font_size=56, color=INK)
        s = Text(
            "Bohr → fine structure → Lamb shift  —  each a factor of ~10 smaller",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _make_level_row(self, states, x_start, x_end, y_coords, colors, labels):
        """Draw horizontal energy levels with labels."""
        objs = []
        for (state, y, col, lbl_str) in zip(states, y_coords, colors, labels):
            line = Line(x_start, x_end, color=col, stroke_width=2.5).set_y(y)
            lbl  = MathTex(lbl_str, color=col, font_size=18).next_to(line, RIGHT, buff=0.1)
            objs.extend([line, lbl])
        return objs

    def _stage1_bohr(self):
        hdr = Text("Stage 1 — Bohr model: 8 degenerate states at E₂ = −3.4 eV",
                   font="EB Garamond", font_size=20, color=BLUE).to_edge(UP, buff=0.3)
        self.play(Write(hdr), run_time=0.7)

        y0 = 0.0
        lines = []
        state_labels = [r"2s_{1/2}", r"2p_{1/2}", r"2p_{3/2}^{(m=+3/2)}",
                        r"2p_{3/2}^{(m=+1/2)}", r"2p_{3/2}^{(m=-1/2)}", r"2p_{3/2}^{(m=-3/2)}",
                        r"2p_{1/2}^{(m=-1/2)}", r"2s_{1/2}^{(m=-1/2)}"]
        for i in range(8):
            x = -3.5 + i * 0.6
            line = Line([x, y0, 0], [x+0.5, y0, 0], color=DIM, stroke_width=2.5)
            lines.append(line)
        energy_lbl = MathTex(r"E_2 = -3.4\;\mathrm{eV}", color=DIM, font_size=22
                             ).shift(LEFT*4 + DOWN*0.4)
        brace_lbl  = Text("8 degenerate states", font="EB Garamond",
                          font_size=18, color=DIM).shift(DOWN * 0.7)

        self.play(*[Create(l) for l in lines], Write(energy_lbl), run_time=1.2)
        self.play(Write(brace_lbl), run_time=0.5)
        self.wait(1.0)
        self.play(*[FadeOut(o) for o in lines + [energy_lbl, brace_lbl, hdr]], run_time=0.5)

    def _stage2_fine_structure(self):
        hdr = Text("Stage 2 — Fine structure: 2p₃/₂ rises; 2s₁/₂ and 2p₁/₂ stay degenerate",
                   font="EB Garamond", font_size=18, color=BLUE).to_edge(UP, buff=0.3)
        self.play(Write(hdr), run_time=0.7)

        # Two levels after fine structure
        # j=3/2: higher energy (less negative correction)
        Efs_half  = E_fine_structure(2, 0.5)   # ≈ -5.66e-5 eV
        Efs_3half = E_fine_structure(2, 1.5)   # ≈ -1.13e-5 eV
        splitting = Efs_3half - Efs_half       # > 0

        # Scale to canvas: map splitting to 1.5 units
        scale = 1.5 / splitting
        y_half  = 0.0
        y_3half = splitting * scale

        lvl_half = Line([-2.5, y_half, 0], [0.5, y_half, 0],
                        color=BLUE, stroke_width=3)
        lvl_3half = Line([-2.5, y_3half, 0], [0.5, y_3half, 0],
                         color=GOLD, stroke_width=3)

        lbl_half  = MathTex(r"2s_{1/2},\;2p_{1/2}\;\;(j=1/2)",
                            color=BLUE, font_size=20).next_to(lvl_half, RIGHT, buff=0.1)
        lbl_3half = MathTex(r"2p_{3/2}\;\;(j=3/2)",
                            color=GOLD, font_size=20).next_to(lvl_3half, RIGHT, buff=0.1)

        delta_lbl = MathTex(
            r"\Delta E_{\rm fs} = 4.53\times10^{-5}\;\mathrm{eV}",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.3)

        arrow = DoubleArrow(
            [0.6, y_half, 0], [0.6, y_3half, 0],
            color=INK, stroke_width=1.5, tip_length=0.15, buff=0,
        )

        self.play(Create(lvl_half), Create(lvl_3half), run_time=1.0)
        self.play(Write(lbl_half), Write(lbl_3half), run_time=0.7)
        self.play(Create(arrow), Write(delta_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(*[FadeOut(o) for o in
                    [lvl_half, lvl_3half, lbl_half, lbl_3half, delta_lbl, arrow, hdr]],
                  run_time=0.5)

    def _stage3_lamb_shift(self):
        hdr = Text("Stage 3 — Lamb shift: 2s₁/₂ lifts above 2p₁/₂ by 4×10⁻⁶ eV (QED)",
                   font="EB Garamond", font_size=18, color=GOLD).to_edge(UP, buff=0.3)
        self.play(Write(hdr), run_time=0.7)

        y_2p = 0.0
        y_2s = 1.8    # zoomed in — represents 4e-6 eV

        lvl_2p = Line([-2.5, y_2p, 0], [0.5, y_2p, 0], color=BLUE, stroke_width=3)
        lvl_2s = Line([-2.5, y_2s, 0], [0.5, y_2s, 0], color=GOLD, stroke_width=3)

        lbl_2p = MathTex(r"2p_{1/2}", color=BLUE, font_size=22
                         ).next_to(lvl_2p, RIGHT, buff=0.1)
        lbl_2s = MathTex(r"2s_{1/2}", color=GOLD, font_size=22
                         ).next_to(lvl_2s, RIGHT, buff=0.1)

        lamb_lbl = MathTex(
            r"\Delta E_{\rm Lamb} \approx 4\times10^{-6}\;\mathrm{eV}\;\approx 1057\;\mathrm{MHz}",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.3)

        arrow = DoubleArrow(
            [0.6, y_2p, 0], [0.6, y_2s, 0],
            color=INK, stroke_width=1.5, tip_length=0.15, buff=0,
        )
        note = Text("QED required — this cannot come from Dirac alone",
                    font="EB Garamond", font_size=18, color=BROWN).shift(DOWN * 1.5)

        self.play(Create(lvl_2p), Create(lvl_2s), run_time=0.8)
        self.play(Write(lbl_2p), Write(lbl_2s), run_time=0.6)
        self.play(Create(arrow), Write(lamb_lbl), run_time=0.8)
        self.play(Write(note), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(lvl_2p, lvl_2s, lbl_2p, lbl_2s, lamb_lbl,
                          arrow, note, hdr), run_time=0.5)

    def _payoff(self):
        hierarchy = VGroup(
            MathTex(r"3.4\;\mathrm{eV}", color=BLUE, font_size=26),
            MathTex(r"\xrightarrow{\;\text{fine structure}\;} 4.5\times10^{-5}\;\mathrm{eV}",
                    color=GOLD, font_size=26),
            MathTex(r"\xrightarrow{\;\text{Lamb shift}\;} 4\times10^{-6}\;\mathrm{eV}\;\text{(QED)}",
                    color=BROWN, font_size=26),
        ).arrange(DOWN, buff=0.4).center()

        for eq in hierarchy:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
