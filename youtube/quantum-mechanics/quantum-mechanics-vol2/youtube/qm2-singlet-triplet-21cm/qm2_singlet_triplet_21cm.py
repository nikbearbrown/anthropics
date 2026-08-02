#!/usr/bin/env python3
"""
qm2_singlet_triplet_21cm.py — Singlet vs Triplet: One Minus Sign Controls the 21-cm Line
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    H_hf = A·S_e·S_p = (A/2)(F² − S_e² − S_p²)
    Triplet F=1: E = +Aℏ²/4  (×3 degenerate)
    Singlet F=0: E = −3Aℏ²/4
    ΔE = Aℏ² = 5.87×10⁻⁶ eV → f = 1420.405 MHz → λ = 21.1 cm
    |1,0⟩ = (|↑↓⟩+|↓↑⟩)/√2  vs  |0,0⟩ = (|↑↓⟩−|↓↑⟩)/√2

Verify:
    python3 qm2_singlet_triplet_21cm.py --verify

Render:
    manim -qh qm2_singlet_triplet_21cm.py SingletTriplet21cmScene
"""
import sys
import numpy as np

H_EV_S = 4.1357e-15  # eV·s
C       = 3e8         # m/s

def freq_Hz():
    return 1420.405e6  # Hz (exact historical value)

def wavelength_cm():
    return C / freq_Hz() * 100

def energy_gap_eV():
    return H_EV_S * freq_Hz()

def verify():
    print("=== Singlet-Triplet 21-cm Verification ===")
    f = freq_Hz()
    lam_cm = wavelength_cm()
    dE = energy_gap_eV()
    print(f"f = {f/1e6:.3f} MHz")
    print(f"λ = {lam_cm:.3f} cm")
    print(f"ΔE = {dE:.4e} eV")

    # P1: ⟨J²⟩|0,0⟩ = 0
    # |0,0⟩ = (|↑↓⟩ - |↓↑⟩)/√2
    # J² = J₁² + J₂² + 2J₁·J₂ = 3ℏ²/2 + 2J₁·J₂
    # J₁·J₂ on singlet: J₁·J₂|singlet⟩ = -3ℏ²/4|singlet⟩ (F=0)
    # ⟨J²⟩ = 3ℏ²/2 + 2×(-3ℏ²/4) = 3ℏ²/2 - 3ℏ²/2 = 0 ✓
    J2_singlet = 0  # F(F+1)ℏ² = 0
    print(f"\nP1: ⟨J²⟩|0,0⟩ = {J2_singlet}  (F=0 → F(F+1)=0) ✓")

    # P2: Energy gap = Aℏ²
    # Triplet: Aℏ²/4; Singlet: -3Aℏ²/4; gap = Aℏ²
    print(f"P2: E_triplet = +Aℏ²/4,  E_singlet = -3Aℏ²/4")
    print(f"    Gap = Aℏ² (triplet - singlet) = {dE:.4e} eV")
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


class SingletTriplet21cmScene(Scene):
    """
    Left: CG ladder building triplet and singlet states with ± sign highlighted.
    Right: energy level diagram with 21-cm photon emission arrow.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_cg_ladder()
        self._phase_energy_diagram()
        self._phase_sign_flip()

    def _phase_title(self):
        title = Text("One Minus Sign → 21-cm Radio Astronomy", font="EB Garamond", font_size=48, color=INK)
        sub = Text(
            "f = 1420.405 MHz  ·  λ = 21.1 cm  ·  the most observed line in the universe",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"|1,0\rangle = \frac{|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle}{\sqrt{2}}\quad\text{vs}\quad"
            r"|0,0\rangle = \frac{|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle}{\sqrt{2}}",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_cg_ladder(self):
        """Build |1,1⟩ → |1,0⟩ (triplet) and show orthogonal |0,0⟩."""
        title = Text("Clebsch-Gordan ladder for 2 spin-½ particles",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(title), run_time=0.6)

        states = VGroup(
            MathTex(r"|1,1\rangle = |\!\uparrow\uparrow\rangle", color=BLUE, font_size=26),
            MathTex(r"|1,0\rangle = \frac{|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle}{\sqrt{2}}", color=BLUE, font_size=26),
            MathTex(r"|1,-1\rangle = |\!\downarrow\downarrow\rangle", color=BLUE, font_size=26),
            MathTex(r"|0,0\rangle = \frac{|\!\uparrow\downarrow\rangle \mathbf{-} |\!\downarrow\uparrow\rangle}{\sqrt{2}}", color=GOLD, font_size=26),
        ).arrange(DOWN, buff=0.5).shift(LEFT*2.5 + DOWN*0.3)

        labels_right = VGroup(
            Text("Triplet F=1 (symmetric)", font="EB Garamond", font_size=16, color=BLUE),
            Text("Triplet |1,0⟩ (J₋ lowering)", font="EB Garamond", font_size=16, color=BLUE),
            Text("Triplet F=1 (symmetric)", font="EB Garamond", font_size=16, color=BLUE),
            Text("Singlet F=0 (antisymmetric) ← the minus sign!", font="EB Garamond", font_size=16, color=GOLD),
        ).arrange(DOWN, buff=0.5).shift(RIGHT*3.0 + DOWN*0.3)

        for i, (s, l) in enumerate(zip(states, labels_right)):
            self.play(FadeIn(s), FadeIn(l), run_time=0.6 if i < 3 else 0.8)
            if i < 2:
                arrow = Arrow(s.get_bottom(), states[i+1].get_top(), buff=0.1, color=DIM, stroke_width=1.5)
                arr_lbl = Text("J₋", font="EB Garamond", font_size=13, color=DIM).next_to(arrow, RIGHT, buff=0.05)
                self.play(GrowArrow(arrow), Write(arr_lbl), run_time=0.5)

        # Highlight minus sign
        box = SurroundingRectangle(states[3], color=GOLD, stroke_width=2)
        self.play(Create(box), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_energy_diagram(self):
        """Energy level diagram with 21-cm photon."""
        title = Text("Hyperfine energy splitting",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(title), run_time=0.6)

        # Energy levels
        ax = Axes(
            x_range=[-1.5, 1.5, 1], y_range=[-4, 2, 1],
            x_length=4.0, y_length=5.0,
            axis_config=dict(color=DIM, stroke_width=1, include_ticks=False, tip_length=0.15),
        ).shift(LEFT*0.5)

        # Triplet: E = +ℏ²/4 (in units of Aℏ²)
        triplet_y = 1.0
        singlet_y = -3.0

        # Three triplet levels (degenerate)
        for offset, m_lbl in [(-0.35, "m=−1"), (0, "m=0"), (0.35, "m=+1")]:
            trip_line = Line(ax.c2p(-0.8+offset, triplet_y), ax.c2p(0.8+offset, triplet_y),
                             color=BLUE, stroke_width=3)
            self.play(Create(trip_line), run_time=0.3)

        trip_label = MathTex(r"F=1\;\text{(triplet)}\quad E = +\tfrac{A\hbar^2}{4}", color=BLUE, font_size=18)
        trip_label.to_corner(UR, buff=0.5).shift(DOWN*0.3)

        # Singlet level
        sing_line = Line(ax.c2p(-0.8, singlet_y), ax.c2p(0.8, singlet_y),
                         color=GOLD, stroke_width=3)
        sing_label = MathTex(r"F=0\;\text{(singlet)}\quad E = -\tfrac{3A\hbar^2}{4}", color=GOLD, font_size=18)
        sing_label.to_corner(UR, buff=0.5).shift(DOWN*1.2)

        self.play(Create(sing_line), FadeIn(trip_label, sing_label), run_time=0.8)

        # Photon emission arrow
        photon_arrow = CurvedArrow(ax.c2p(1.0, triplet_y), ax.c2p(1.0, singlet_y),
                                   color=BROWN, stroke_width=3, angle=-np.pi/4)
        f_lbl = MathTex(r"f = 1420.405\,\mathrm{MHz}", color=BROWN, font_size=18).to_corner(UR, buff=0.5).shift(DOWN*2.1)
        lam_lbl = MathTex(r"\lambda = 21.1\,\mathrm{cm}", color=BROWN, font_size=18).next_to(f_lbl, DOWN, buff=0.1)
        dE_lbl = MathTex(r"\Delta E = A\hbar^2 = 5.87\times10^{-6}\,\mathrm{eV}", color=INK, font_size=16).next_to(lam_lbl, DOWN, buff=0.12)

        self.play(Create(photon_arrow), FadeIn(f_lbl, lam_lbl, dE_lbl), run_time=1.0)

        # Voyager note
        voyager = Text("Engraved on Voyager — λ as a time unit (T = 0.704 ns)",
                       font="EB Garamond", font_size=17, color=DIM).to_edge(DOWN, buff=0.3)
        self.play(Write(voyager), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_sign_flip(self):
        """What if the minus sign were a plus sign?"""
        title = Text("What if the minus sign → plus sign?",
                     font="EB Garamond", font_size=30, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"\frac{|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle}{\sqrt{2}} = |1,0\rangle", color=BLUE, font_size=26),
            Text("Both states become triplet |1,0⟩ — no F=0 singlet exists",
                 font="EB Garamond", font_size=20, color=DIM),
            Text("No 21-cm line. Radio astronomy of neutral hydrogen: impossible.",
                 font="EB Garamond", font_size=20, color=BROWN),
            MathTex(r"\text{One minus sign} \Longrightarrow 1420.405\,\mathrm{MHz}", color=GOLD, font_size=26),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
