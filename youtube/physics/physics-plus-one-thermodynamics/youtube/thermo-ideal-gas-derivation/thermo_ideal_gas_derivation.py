#!/usr/bin/env python3
"""
thermo_ideal_gas_derivation.py — Ideal Gas from First Principles: Bouncing Molecule → PV = NkT
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-thermodynamics book.

Render:
    cd physics-plus-one-thermodynamics/youtube/thermo-ideal-gas-derivation
    manim -qh thermo_ideal_gas_derivation.py IdealGasDerivationScene

Physics:
    Single molecule in box length L, mass m, velocity component v_x.
    F = mv_x^2 / L → P = NkT/V (equipartition: (1/2)m<v^2> = (3/2)kT)
    At STP: V/N = kT/P = 3.72e-26 m^3/molecule = 22.4 L/mol  ✓
    N2 v_rms = sqrt(3kT/m) = 511 m/s  ✓
"""
import sys
import numpy as np

# ─── Physics constants ────────────────────────────────────────────────────────
K_B   = 1.381e-23    # J/K
M_N2  = 4.65e-26     # kg  N2 molecule
N_A   = 6.022e23     # /mol


def molar_volume_stp():
    """V/mol at STP (T=273 K, P=101325 Pa), should be ~22.4 L/mol."""
    T_STP = 273.0
    P_STP = 101325.0
    return N_A * K_B * T_STP / P_STP * 1e3  # L/mol


def v_rms(m, T):
    return np.sqrt(3.0 * K_B * T / m)


if __name__ == "__main__":
    print("=== Ideal Gas Derivation Verification ===")
    vm = molar_volume_stp()
    print(f"Molar volume at STP = {vm:.2f} L/mol  (expect 22.4)")
    assert abs(vm - 22.4) < 0.1, f"Molar volume FAIL: {vm}"
    vr = v_rms(M_N2, 293.0)
    print(f"N2 v_rms at 293 K = {vr:.0f} m/s  (expect 511)")
    assert abs(vr - 511) < 5, f"v_rms FAIL: {vr}"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class IdealGasDerivationScene(Scene):
    """Animate: one molecule bounces → force → pressure → PV = NkT."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_one_molecule()
        self._phase_derivation()
        self._phase_verify()

    def _phase_title(self):
        title = Text("Ideal Gas Law Derived", font="EB Garamond",
                     font_size=56, color=INK)
        sub = Text("One molecule bouncing in a box → PV = NkT",
                   font="EB Garamond", font_size=24, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_one_molecule(self):
        # Draw a 1D box and animate molecule bouncing
        box_w = 5.0
        LEFT_WALL  = LEFT  * (box_w / 2)
        RIGHT_WALL = RIGHT * (box_w / 2)
        box_top    = UP * 1.2
        box_bot    = DOWN * 1.2

        walls = VGroup(
            Line(LEFT_WALL + box_bot, LEFT_WALL  + box_top, color=INK, stroke_width=4),
            Line(RIGHT_WALL + box_bot, RIGHT_WALL + box_top, color=INK, stroke_width=4),
            Line(LEFT_WALL + box_bot, RIGHT_WALL + box_bot, color=INK, stroke_width=2),
            Line(LEFT_WALL + box_top, RIGHT_WALL + box_top, color=INK, stroke_width=2),
        )
        lbl_L = MathTex(r"L", color=DIM, font_size=28).next_to(
            (LEFT_WALL + RIGHT_WALL) / 2 + box_bot, DOWN, buff=0.1)

        molecule = Dot(color=BLUE, radius=0.18).move_to(LEFT_WALL * 0.8)

        hdr = Text("Single molecule, mass m, velocity v_x",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(hdr), Create(walls), Write(lbl_L), FadeIn(molecule), run_time=1.2)

        # Animate three bounces
        for _ in range(3):
            self.play(molecule.animate.move_to(RIGHT_WALL * 0.82), run_time=0.55)
            impulse = MathTex(r"2mv_x", color=GOLD, font_size=22).next_to(
                RIGHT_WALL, RIGHT, buff=0.08)
            self.play(FadeIn(impulse), run_time=0.25)
            self.wait(0.15)
            self.play(FadeOut(impulse), run_time=0.15)
            self.play(molecule.animate.move_to(LEFT_WALL * 0.82), run_time=0.55)

        step1 = MathTex(
            r"F_{\rm wall}=\frac{mv_x^2}{L}",
            color=BLUE, font_size=30).to_edge(DOWN, buff=0.35)
        self.play(Write(step1), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(hdr, walls, lbl_L, molecule, step1), run_time=0.5)

    def _phase_derivation(self):
        steps = [
            MathTex(r"F = \frac{mv_x^2}{L}", color=BLUE, font_size=34),
            MathTex(r"P = \frac{F}{A}=\frac{mv_x^2}{V}", color=GOLD, font_size=34),
            MathTex(r"PV = Nm\langle v_x^2\rangle = \frac{Nm\langle v^2\rangle}{3}",
                    color=GOLD, font_size=34),
            MathTex(r"\tfrac{1}{2}m\langle v^2\rangle=\tfrac{3}{2}k_BT",
                    color=DIM, font_size=34),
            MathTex(r"PV = Nk_BT", color=INK, font_size=48),
        ]
        VGroup(*steps).arrange(DOWN, buff=0.42).center()
        for step in steps:
            self.play(Write(step), run_time=0.9)
            self.wait(0.5)
        self.wait(1.5)
        self.play(FadeOut(*steps), run_time=0.5)

    def _phase_verify(self):
        hdr = Text("Verify: N₂ at T = 293 K, STP", font="EB Garamond",
                   font_size=26, color=INK).to_edge(UP, buff=0.25)

        vm = molar_volume_stp()
        vr = v_rms(M_N2, 293.0)

        p1 = MathTex(
            r"\frac{V}{N} = \frac{k_BT}{P} \Rightarrow 22.4\,\mathrm{L/mol}",
            color=BLUE, font_size=30)
        p2 = MathTex(
            r"v_{\rm rms} = \sqrt{3k_BT/m} = 511\,\mathrm{m/s}",
            color=GOLD, font_size=30)
        p3 = MathTex(
            r"P_{\rm stellar\,core}\approx 2.3\times10^{16}\,\mathrm{Pa}"
            r"\quad\text{(same law, }T=1.5\times10^7\,\mathrm{K)}",
            color=BROWN, font_size=24)

        VGroup(p1, p2, p3).arrange(DOWN, buff=0.5).center()
        self.play(Write(hdr), run_time=0.5)
        self.play(Write(p1), run_time=1.0)
        self.wait(0.5)
        self.play(Write(p2), run_time=1.0)
        self.wait(0.5)
        self.play(Write(p3), run_time=1.0)
        self.wait(2.5)
        final = Text("One molecule. One law. Eleven orders of magnitude.",
                     font="EB Garamond", font_size=28, color=INK).to_edge(DOWN, buff=0.3)
        self.play(Write(final), run_time=1.2)
        self.wait(2.0)
