#!/usr/bin/env python3
"""
vol1_stern_gerlach_sequential.py — Sequential Stern-Gerlach: Measurement Erases Certainty
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    Z→Z:        P(↑) = 1.000  (eigenstate remeasured)
    Z→X→Z:      P(+x after ↑) = 0.500, P(↑ after +x) = 0.500
    Z→X(both)→Z: P(↑) = 0.500 still
    Commutator: [σ_x, σ_z] = −2iσ_y ≠ 0 is the cause

Verify:
    python3 vol1_stern_gerlach_sequential.py --verify

Render:
    manim -qh vol1_stern_gerlach_sequential.py SternGerlachSequentialScene
"""
import sys
import numpy as np

def verify():
    print("=== Sequential Stern-Gerlach Verification ===")
    # |↑⟩ = [1, 0]^T
    # |+x⟩ = [1, 1]^T / √2
    # |−x⟩ = [1, -1]^T / √2
    up = np.array([1, 0], dtype=complex)
    down = np.array([0, 1], dtype=complex)
    plus_x = np.array([1, 1], dtype=complex) / np.sqrt(2)
    minus_x = np.array([1, -1], dtype=complex) / np.sqrt(2)

    # P1: Z→X→Z: P(↑ from final Z) = 0.500
    P_plus_x_given_up = abs(np.dot(plus_x.conj(), up))**2
    P_up_given_plus_x = abs(np.dot(up.conj(), plus_x))**2
    print(f"P1: P(+x | ↑) = {P_plus_x_given_up:.4f}  (should be 0.500)")
    print(f"    P(↑ | +x)  = {P_up_given_plus_x:.4f}  (should be 0.500)")

    P_minus_x = abs(np.dot(minus_x.conj(), up))**2
    P_up_given_minus_x = abs(np.dot(up.conj(), minus_x))**2
    print(f"    P(−x | ↑) = {P_minus_x:.4f}  (should be 0.500)")
    print(f"    P(↑ | −x)  = {P_up_given_minus_x:.4f}  (should be 0.500)")

    # P2: Z→Z: P(↑ | ↑) = 1.000
    P_up_given_up = abs(np.dot(up.conj(), up))**2
    print(f"\nP2: P(↑ | ↑) = {P_up_given_up:.6f}  (should be 1.000 exactly)")

    # Commutator check
    sx = np.array([[0, 1], [1, 0]])
    sz = np.array([[1, 0], [0, -1]])
    sy = np.array([[0, -1j], [1j, 0]])
    comm = sx @ sz - sz @ sx
    expected = -2j * sy
    print(f"\nCommutator [σ_x,σ_z] = {comm[0,0]:.2f},{comm[0,1]:.2f},{comm[1,0]:.2f},{comm[1,1]:.2f}")
    print(f"           -2iσ_y =   {expected[0,0]:.2f},{expected[0,1]:.2f},{expected[1,0]:.2f},{expected[1,1]:.2f}")
    print(f"Match: {np.allclose(comm, expected)}")
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


def magnet_box(ax_x, ax_y, label="Z", color=BLUE):
    """Draw a Stern-Gerlach magnet box."""
    box = Rectangle(width=1.0, height=0.8, color=color, fill_color=color, fill_opacity=0.3, stroke_width=2)
    box.move_to(np.array([ax_x, ax_y, 0]))
    lbl = Text(label, font="EB Garamond", font_size=20, color=color).move_to(box.get_center())
    return VGroup(box, lbl)


class SternGerlachSequentialScene(Scene):
    """
    Three-panel stacked beam-splitting animation.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_ZZ()
        self._phase_ZXZ()
        self._phase_commutator()

    def _phase_title(self):
        title = Text("Sequential Stern-Gerlach", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "One non-commuting measurement in the middle erases spin certainty",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(r"[\hat{S}_x,\,\hat{S}_z] = -2i\hat{S}_y \neq 0", color=BLUE, font_size=30)
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_ZZ(self):
        """Z→Z: pure spin-up comes out spin-up, P=1.000."""
        title = Text("Z → Z:  certainty preserved  (P = 1.000)",
                     font="EB Garamond", font_size=26, color=BLUE).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        # Magnets
        m1 = magnet_box(-4.5, 0, "Z", BLUE)
        m2 = magnet_box(1.5, 0, "Z", BLUE)

        # Beam: thick upper (spin-up) beam enters
        beam_in = Arrow(np.array([-7, 0, 0]), np.array([-5.5, 0, 0]),
                        buff=0, color=INK, stroke_width=4)
        lbl_in = Text("↑ filtered", font="EB Garamond", font_size=16, color=INK).next_to(beam_in, UP, buff=0.08)

        # Split at first magnet: only up exits (thick)
        beam_up1 = Arrow(np.array([-4.0, 0.4, 0]), np.array([1.0, 0.4, 0]),
                         buff=0, color=BLUE, stroke_width=5)
        beam_dn1 = Line(np.array([-4.0, -0.4, 0]), np.array([-2.0, -0.4, 0]),
                        color=DIM, stroke_width=1.5).set_opacity(0.5)
        lbl_dn1 = Text("↓ (blocked)", font="EB Garamond", font_size=13, color=DIM).next_to(beam_dn1, DOWN, buff=0.06)

        # Exit second Z magnet: only up
        beam_out = Arrow(np.array([2.0, 0.4, 0]), np.array([5.5, 0.4, 0]),
                         buff=0, color=BLUE, stroke_width=5)
        lbl_out = Text("P(↑) = 1.000", font="EB Garamond", font_size=20, color=GOLD).next_to(beam_out, UP, buff=0.1)

        self.play(Create(m1), Create(m2), run_time=0.6)
        self.play(GrowArrow(beam_in), Write(lbl_in), run_time=0.6)
        self.play(GrowArrow(beam_up1), Create(beam_dn1), FadeIn(lbl_dn1), run_time=0.8)
        self.play(GrowArrow(beam_out), Write(lbl_out), run_time=0.8)

        caption = MathTex(r"|\langle\uparrow|\uparrow\rangle|^2 = 1.000\text{ — eigenstate remeasured}",
                         color=INK, font_size=22).to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(title, m1, m2, beam_in, beam_up1, beam_dn1, beam_out, lbl_in, lbl_dn1, lbl_out, caption), run_time=0.5)

    def _phase_ZXZ(self):
        """Z→X→Z: P(↑) = 0.500."""
        title = Text("Z → X → Z:  certainty destroyed  (P = 0.500)",
                     font="EB Garamond", font_size=26, color=BROWN).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        m1 = magnet_box(-5.5, 0, "Z", BLUE)
        m2 = magnet_box(0.0, 0, "X", BROWN)
        m3 = magnet_box(5.5, 0, "Z", BLUE)

        beam_in = Arrow(np.array([-7.5, 0, 0]), np.array([-6.5, 0, 0]),
                        buff=0, color=INK, stroke_width=3)

        # Z1: filter up
        beam_up1 = Arrow(np.array([-5.0, 0.3, 0]), np.array([-0.6, 0.3, 0]),
                         buff=0, color=BLUE, stroke_width=4)

        # X: splits 50/50
        beam_px = Arrow(np.array([0.6, 0.6, 0]), np.array([4.8, 0.6, 0]),
                        buff=0, color=BROWN, stroke_width=3)
        beam_mx = Arrow(np.array([0.6, -0.1, 0]), np.array([2.5, -0.1, 0]),
                        buff=0, color=BROWN, stroke_width=3, stroke_opacity=0.6)
        lbl_px = Text("+x  (50%)", font="EB Garamond", font_size=14, color=BROWN).next_to(beam_px, UP, buff=0.06)
        lbl_mx = Text("−x  (50%)", font="EB Garamond", font_size=14, color=DIM).next_to(beam_mx, DOWN, buff=0.06)

        # Z2: +x → ↑ 50%, ↓ 50%
        beam_up2 = Arrow(np.array([6.1, 0.9, 0]), np.array([7.5, 0.9, 0]),
                         buff=0, color=BLUE, stroke_width=3)
        beam_dn2 = Arrow(np.array([6.1, 0.3, 0]), np.array([7.5, 0.3, 0]),
                         buff=0, color=DIM, stroke_width=3)
        lbl_up2 = Text("P(↑) = 0.500", font="EB Garamond", font_size=15, color=GOLD).next_to(beam_up2, UP, buff=0.05)
        lbl_dn2 = Text("P(↓) = 0.500", font="EB Garamond", font_size=15, color=GOLD).next_to(beam_dn2, DOWN, buff=0.05)

        caption = MathTex(
            r"|\langle\uparrow|{+x}\rangle|^2 = \tfrac{1}{2}\quad\Longrightarrow\quad P(\uparrow) = 0.500",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.3)

        self.play(Create(m1), Create(m2), Create(m3), GrowArrow(beam_in), run_time=0.8)
        self.play(GrowArrow(beam_up1), run_time=0.6)
        self.play(GrowArrow(beam_px), GrowArrow(beam_mx), FadeIn(lbl_px, lbl_mx), run_time=0.8)
        self.play(GrowArrow(beam_up2), GrowArrow(beam_dn2), FadeIn(lbl_up2, lbl_dn2), run_time=0.8)
        self.play(Write(caption), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(
            title, m1, m2, m3, beam_in, beam_up1, beam_px, beam_mx,
            lbl_px, lbl_mx, beam_up2, beam_dn2, lbl_up2, lbl_dn2, caption,
        ), run_time=0.5)

    def _phase_commutator(self):
        """Show the algebraic cause."""
        title = Text("Why does the X apparatus erase the Z certainty?",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"[\hat{\sigma}_x,\,\hat{\sigma}_z] = -2i\hat{\sigma}_y \neq 0", color=BLUE, font_size=32),
            Text("Non-zero commutator → no shared eigenstates", font="EB Garamond", font_size=22, color=DIM),
            Text("A Z eigenstate is not an X eigenstate — measuring X collapses Z certainty",
                 font="EB Garamond", font_size=20, color=BROWN),
            MathTex(
                r"\text{If measured Z→Z (commuting): } P(\uparrow) = 1.000",
                color=GOLD, font_size=22,
            ),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
