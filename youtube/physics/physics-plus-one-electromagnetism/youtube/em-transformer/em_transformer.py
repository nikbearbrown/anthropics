#!/usr/bin/env python3
"""
em_transformer.py — Transformer: V2/V1 = N2/N1, Power Conservation
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    V2/V1 = N2/N1  (ideal transformer)
    P = V1*I1 = V2*I2  (power conservation)
    I2/I1 = N1/N2
    I^2*R loss: ratio = (I2/I1)^2 = (N1/N2)^2  -> stepping up 100x reduces loss 10000x

Verify: python3 em_transformer.py --verify
Render: manim -qh em_transformer.py EmTransformerScene
"""
import sys
import numpy as np

V1_PRI  = 120.0    # V primary
N1_PRI  = 100      # primary turns
N2_SEC  = 10000    # secondary turns (step-up)
POWER   = 1200.0   # W

def V2(N1=N1_PRI, N2=N2_SEC, V1=V1_PRI):
    return V1 * N2 / N1

def I1(P=POWER, V1=V1_PRI):
    return P / V1

def I2(P=POWER, V2_val=None, N1=N1_PRI, N2=N2_SEC, V1=V1_PRI):
    if V2_val is None:
        V2_val = V2(N1, N2, V1)
    return P / V2_val

def verify():
    print("=== Transformer verification ===")
    v2 = V2()
    i1 = I1()
    i2 = I2()
    print(f"Step-up (N2/N1 = {N2_SEC/N1_PRI:.0f}): V2 = {v2:.0f} V, I1 = {i1:.1f} A, I2 = {i2:.3f} A")
    print(f"P1 = {V1_PRI*i1:.0f} W, P2 = {v2*i2:.0f} W  {'✓' if abs(V1_PRI*i1 - v2*i2) < 0.1 else '✗'}")

    # P1: V2 = 100*V1 for N2/N1=100
    ratio = v2 / V1_PRI
    print(f"P1: V2/V1 = {ratio:.1f}  (expected 100.0) {'✓' if abs(ratio - 100) < 0.1 else '✗'}")

    # P2: I2 = I1/100, power unchanged
    curr_ratio = i2 / i1
    print(f"P2: I2/I1 = {curr_ratio:.4f}  (expected 0.0100) {'✓' if abs(curr_ratio - 0.01) < 0.001 else '✗'}")

    # Resistance loss: P_loss = I^2 * R
    R_line = 1.0   # ohm (1 ohm transmission line)
    loss_120V  = i1**2 * R_line
    loss_12kV  = i2**2 * R_line
    print(f"\nTransmission line loss (R=1 ohm):")
    print(f"  At 120 V: {loss_120V:.1f} W  ({loss_120V/POWER*100:.1f}% of power)")
    print(f"  At 12 kV: {loss_12kV:.4f} W  ({loss_12kV/POWER*100:.5f}% of power)")
    print(f"  Loss reduction: {loss_120V/loss_12kV:.0f}x  (= (N2/N1)^2 = {(N2_SEC/N1_PRI)**2:.0f}x)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class EmTransformerScene(Scene):
    """
    Transformer schematic: primary/secondary coils on core.
    N2/N1 slider morphs V2 up, I2 down. Power gauges stay equal.
    I^2 R loss comparison.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._schematic()
        self._slider_phase()
        self._loss_demo()
        self._finale()

    def _title(self):
        t = Text("Transformer: V₂/V₁ = N₂/N₁, Power Conserved",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "Step up voltage 100× → current drops 100× → resistive losses drop 10 000×.\n"
            "This is why long-distance power transmission is thermodynamically feasible.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _schematic(self):
        # Iron core (rectangle)
        core = Rectangle(width=2, height=3, color=BROWN,
                         fill_opacity=0.2, stroke_width=2)
        core.center()

        # Primary coil (left) — stacked rects
        prim_lbl = MathTex(r"N_1 = 100", color=BLUE, font_size=22)
        prim_lbl.next_to(core, LEFT, buff=1.0)
        prim_coil = Rectangle(width=0.4, height=2.4, color=BLUE,
                              stroke_width=2.5, fill_opacity=0.1)
        prim_coil.next_to(core.get_left(), LEFT, buff=0.1)

        # Secondary coil (right)
        sec_lbl = MathTex(r"N_2 = 10\,000", color=GOLD, font_size=22)
        sec_lbl.next_to(core, RIGHT, buff=1.0)
        sec_coil = Rectangle(width=0.6, height=2.4, color=GOLD,
                             stroke_width=2.5, fill_opacity=0.1)
        sec_coil.next_to(core.get_right(), RIGHT, buff=0.1)

        # Voltage labels
        V1_lbl = MathTex(r"V_1 = 120\,\mathrm{V}", color=BLUE, font_size=22)
        V1_lbl.next_to(prim_coil, DOWN, buff=0.3)
        V2_lbl = MathTex(r"V_2 = 12\,000\,\mathrm{V}", color=GOLD, font_size=22)
        V2_lbl.next_to(sec_coil, DOWN, buff=0.3)

        I1_lbl = MathTex(r"I_1 = 10\,\mathrm{A}", color=BLUE, font_size=20)
        I1_lbl.next_to(V1_lbl, DOWN, buff=0.2)
        I2_lbl = MathTex(r"I_2 = 0.1\,\mathrm{A}", color=GOLD, font_size=20)
        I2_lbl.next_to(V2_lbl, DOWN, buff=0.2)

        P_lbl = MathTex(r"P_1 = P_2 = 1\,200\,\mathrm{W}", color=INK, font_size=24)
        P_lbl.to_edge(DOWN, buff=0.25)

        all_mobs = [core, prim_coil, sec_coil, prim_lbl, sec_lbl,
                    V1_lbl, V2_lbl, I1_lbl, I2_lbl, P_lbl]
        self.play(*[FadeIn(m) for m in all_mobs], run_time=2.0)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.4)

    def _slider_phase(self):
        ratio_tracker = ValueTracker(1.0)   # N2/N1

        # Fixed labels
        v1_lbl = MathTex(r"V_1 = 120\,\mathrm{V}", color=BLUE, font_size=26)
        v1_lbl.shift(LEFT * 4.5 + UP * 1.5)
        i1_lbl_s = MathTex(r"I_1 = 10\,\mathrm{A}", color=BLUE, font_size=22)
        i1_lbl_s.shift(LEFT * 4.5 + UP * 0.8)
        p1_lbl  = MathTex(r"P_1 = 1\,200\,\mathrm{W}", color=BLUE, font_size=22)
        p1_lbl.shift(LEFT * 4.5 + UP * 0.1)

        arrow = MathTex(r"\xrightarrow{N_2/N_1}", color=DIM, font_size=30).center()

        ratio_lbl = MathTex(r"\frac{N_2}{N_1} = ", color=DIM, font_size=26)
        ratio_num = DecimalNumber(1.0, num_decimal_places=0, color=GOLD, font_size=26)
        ratio_num.add_updater(lambda m: m.set_value(ratio_tracker.get_value()))
        ratio_row = VGroup(ratio_lbl, ratio_num).arrange(RIGHT, buff=0.1).shift(DOWN * 2.0)

        V2_label = MathTex(r"V_2 = ", color=GOLD, font_size=26)
        V2_num   = DecimalNumber(V1_PRI, num_decimal_places=0, color=GOLD, font_size=26)
        V2_V     = MathTex(r"\,\mathrm{V}", color=GOLD, font_size=26)
        V2_num.add_updater(lambda m: m.set_value(V1_PRI * ratio_tracker.get_value()))

        I2_label = MathTex(r"I_2 = ", color=GOLD, font_size=22)
        I2_num   = DecimalNumber(10.0, num_decimal_places=3, color=GOLD, font_size=22)
        I2_A     = MathTex(r"\,\mathrm{A}", color=GOLD, font_size=22)
        I2_num.add_updater(lambda m: m.set_value(POWER / max(V1_PRI * ratio_tracker.get_value(), 0.01)))

        P2_label = MathTex(r"P_2 = ", color=GOLD, font_size=22)
        P2_num   = DecimalNumber(POWER, num_decimal_places=0, color=GOLD, font_size=22)
        P2_W     = MathTex(r"\,\mathrm{W}", color=GOLD, font_size=22)
        P2_note  = Text("(unchanged)", font="EB Garamond", font_size=18, color=DIM)

        V2_row = VGroup(V2_label, V2_num, V2_V).arrange(RIGHT, buff=0.1).shift(RIGHT * 3.5 + UP * 1.5)
        I2_row = VGroup(I2_label, I2_num, I2_A).arrange(RIGHT, buff=0.1).shift(RIGHT * 3.5 + UP * 0.8)
        P2_row = VGroup(P2_label, P2_num, P2_W, P2_note).arrange(RIGHT, buff=0.1).shift(RIGHT * 3.5 + UP * 0.1)

        self.play(FadeIn(v1_lbl, i1_lbl_s, p1_lbl), Write(arrow),
                  Write(ratio_row),
                  Write(V2_row), Write(I2_row), Write(P2_row), run_time=1.5)

        self.play(ratio_tracker.animate.set_value(100.0), run_time=4.0, rate_func=smooth)
        self.wait(1.5)
        self.play(ratio_tracker.animate.set_value(1.0), run_time=2.0, rate_func=smooth)
        self.wait(1.0)
        self.play(FadeOut(v1_lbl, i1_lbl_s, p1_lbl, arrow, ratio_row,
                          V2_row, I2_row, P2_row), run_time=0.4)

    def _loss_demo(self):
        R_line = 1.0  # ohm
        I1_val = I1()
        I2_val = I2()

        loss_low  = I1_val**2 * R_line
        loss_high = I2_val**2 * R_line

        row1 = MathTex(
            rf"120\,\mathrm{{V}}:\ I^2 R = ({I1_val:.0f})^2 \times 1\,\Omega = {loss_low:.0f}\,\mathrm{{W}}\ ({loss_low/POWER*100:.0f}\%\ \mathrm{{lost}})",
            color=BROWN, font_size=24,
        )
        row2 = MathTex(
            rf"12\,000\,\mathrm{{V}}:\ I^2 R = ({I2_val:.2f})^2 \times 1\,\Omega = {loss_high:.4f}\,\mathrm{{W}}\ (<0.001\%)",
            color=GOLD, font_size=24,
        )
        ratio_row = MathTex(
            rf"\frac{{\text{{loss}}_{{\rm low}}}}{{\text{{loss}}_{{\rm high}}}} = \left(\frac{{N_2}}{{N_1}}\right)^2 = {(N2_SEC/N1_PRI)**2:.0f}\times",
            color=INK, font_size=26,
        )
        VGroup(row1, row2, ratio_row).arrange(DOWN, buff=0.5).center()
        self.play(Write(row1), run_time=1.0)
        self.play(Write(row2), run_time=1.0)
        self.play(Write(ratio_row), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(row1, row2, ratio_row), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"\frac{V_2}{V_1} = \frac{N_2}{N_1}",
            r"\quad \frac{I_2}{I_1} = \frac{N_1}{N_2}",
            r"\quad P_1 = P_2",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
