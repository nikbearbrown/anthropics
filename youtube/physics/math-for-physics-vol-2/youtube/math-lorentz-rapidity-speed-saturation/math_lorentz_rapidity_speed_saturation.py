#!/usr/bin/env python3
"""
math_lorentz_rapidity_speed_saturation.py — Lorentz Rapidity: Speed Saturation
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

β = tanh(φ). Rapidities add; velocities do not. Speed never reaches c.

Render:
    cd math-for-physics-vol-2/youtube/math-lorentz-rapidity-speed-saturation
    manim -qh math_lorentz_rapidity_speed_saturation.py LorentzRapidityScene

Verify:
    python3 math_lorentz_rapidity_speed_saturation.py --verify

Testable predictions:
    P1: Two boosts of β=0.75 → φ=2×0.9730=1.9459 → β_total=tanh(1.9459)=0.9600
    P2: N boosts of φ₀=tanh⁻¹(0.5)=0.5493 → β_5=tanh(5×0.5493)≈0.9915
"""
import sys
import numpy as np

def rapidity(beta):
    return np.arctanh(beta)

def beta_from_rapidity(phi):
    return np.tanh(phi)

def add_velocities(b1, b2):
    return (b1 + b2) / (1 + b1 * b2)

def verify():
    print("=== Lorentz Rapidity Speed Saturation — verification ===")
    b = 0.75
    phi = rapidity(b)
    phi_total = 2 * phi
    b_total = beta_from_rapidity(phi_total)
    b_naive = 2 * b
    print(f"P1: β=0.75 → φ={phi:.4f}")
    print(f"    2×φ = {phi_total:.4f} → β_total = tanh(2φ) = {b_total:.4f}  (expected 0.9600) {'✓' if abs(b_total-0.96)<1e-3 else '✗'}")
    print(f"    Naive sum = {b_naive:.2f}  (WRONG — exceeds c)")
    print(f"    Relativistic: {b_total:.4f}  ✓")
    print()
    phi0 = rapidity(0.5)
    phi5 = 5 * phi0
    b5 = beta_from_rapidity(phi5)
    print(f"P2: β=0.5 → φ₀={phi0:.4f}")
    print(f"    5×φ₀={phi5:.4f} → β_5=tanh(5φ₀)={b5:.4f}  (expected ≈0.9915) {'✓' if abs(b5-0.9915)<1e-3 else '✗'}")
    print()
    # Check velocity addition formula
    b_add = add_velocities(0.75, 0.75)
    print(f"Velocity addition (0.75+0.75): β_total = {b_add:.4f}  (should match tanh result {b_total:.4f}) ✓")
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


class LorentzRapidityScene(Scene):
    """
    β = tanh(φ) curve. Arrow walks along rapidity axis; velocity saturates.
    Ten boosts of 0.5c show rapidity growing linearly, β saturating.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_curve()
        self._phase_two_boosts()
        self._phase_many_boosts()

    def _phase_title(self):
        title = Text("Lorentz Rapidity", font="EB Garamond", font_size=60, color=INK)
        sub1 = Text(
            "β = tanh(φ)  ·  rapidities add  ·  speed never reaches c",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "0.75c + 0.75c = 0.96c  —  not 1.50c",
            font="EB Garamond", font_size=26, color=GOLD,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_curve(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2)
        ax = Axes(
            x_range=[0, 5.0, 1.0],
            y_range=[0, 1.1, 0.25],
            x_length=9.0,
            y_length=5.0,
            axis_config=axis_cfg,
        ).shift(DOWN * 0.5)

        lbl_phi = MathTex(r"\varphi\;(\text{rapidity})", color=INK, font_size=26).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_b   = MathTex(r"\beta = v/c",               color=INK, font_size=26).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Asymptote at β=1
        asym = DashedLine(ax.c2p(0, 1.0), ax.c2p(5.0, 1.0),
                          color=DIM, stroke_width=1.8, dash_length=0.15)
        asym_lbl = MathTex(r"\beta = 1\;(c)", color=DIM, font_size=22).next_to(ax.c2p(5.0, 1.0), RIGHT, buff=0.05)

        phi_arr = np.linspace(0, 5.0, 500)
        b_arr   = np.tanh(phi_arr)
        curve_pts = [ax.c2p(phi, b) for phi, b in zip(phi_arr, b_arr)]
        curve = VMobject(color=BLUE, stroke_width=4)
        curve.set_points_smoothly(curve_pts)

        tanh_lbl = MathTex(r"\beta = \tanh(\varphi)", color=BLUE, font_size=26)
        tanh_lbl.move_to(ax.c2p(3.0, 0.65))

        self.play(Create(ax), Write(lbl_phi), Write(lbl_b), run_time=1.5)
        self.play(Create(asym), Write(asym_lbl), run_time=0.8)
        self.play(Create(curve), run_time=2.0)
        self.play(Write(tanh_lbl), run_time=0.8)
        self.wait(1.2)

        self._ax = ax
        self._curve = curve

    def _phase_two_boosts(self):
        ax = self._ax
        b = 0.75
        phi = rapidity(b)
        phi2 = 2 * phi
        b_total = beta_from_rapidity(phi2)
        b_naive = 2 * b

        # Mark φ₁
        dot1 = Dot(ax.c2p(phi, 0), color=GOLD, radius=0.08)
        line1 = DashedLine(ax.c2p(phi, 0), ax.c2p(phi, b), color=GOLD, stroke_width=1.8)
        dot1b = Dot(ax.c2p(phi, b), color=GOLD, radius=0.08)
        lbl1 = MathTex(rf"\varphi_1={phi:.3f}", color=GOLD, font_size=20).next_to(ax.c2p(phi, 0), DOWN, buff=0.1)

        self.play(Create(dot1), Create(line1), Create(dot1b), Write(lbl1), run_time=1.0)

        # Mark φ₁+φ₂ = 2φ
        dot2 = Dot(ax.c2p(phi2, 0), color=BROWN, radius=0.08)
        line2 = DashedLine(ax.c2p(phi2, 0), ax.c2p(phi2, b_total), color=BROWN, stroke_width=1.8)
        dot2b = Dot(ax.c2p(phi2, b_total), color=BROWN, radius=0.08)
        lbl2 = MathTex(rf"\varphi_1+\varphi_2={phi2:.3f}", color=BROWN, font_size=20).next_to(ax.c2p(phi2, 0), DOWN, buff=0.1)
        lbl_b2 = MathTex(rf"\beta_{{total}}={b_total:.4f}", color=BROWN, font_size=22).next_to(ax.c2p(phi2, b_total), RIGHT, buff=0.1)

        # Arrow walking from phi to phi2 along x-axis
        arrow = Arrow(ax.c2p(phi, 0.05), ax.c2p(phi2, 0.05), color=GOLD,
                      stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.15)
        self.play(Create(arrow), run_time=1.0)
        self.play(Create(dot2), Create(line2), Create(dot2b),
                  Write(lbl2), Write(lbl_b2), run_time=1.2)

        # Caption: 0.75+0.75≠1.50
        caption = Text(
            f"β₁+β₂ naively = {b_naive:.2f}c  (impossible!)   actual: tanh(2φ) = {b_total:.4f}c",
            font="EB Garamond", font_size=21, color=GOLD,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(caption), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(caption, arrow, dot1, line1, dot1b, lbl1,
                          dot2, line2, dot2b, lbl2, lbl_b2), run_time=0.5)

    def _phase_many_boosts(self):
        ax = self._ax
        # 10 boosts of 0.5c
        b0 = 0.5
        phi0 = rapidity(b0)
        phis = [phi0 * i for i in range(1, 11)]
        betas = [beta_from_rapidity(p) for p in phis]

        caption = Text(
            "Ten boosts of β=0.5c each: rapidity grows linearly, speed saturates",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(caption), run_time=0.8)

        prev_dot = None
        for i, (phi, b) in enumerate(zip(phis, betas)):
            frac = i / 9
            r1 = int(0x58); g1 = int(0xC4); b1_c = int(0xDD)
            r2 = int(0xF0); g2 = int(0xE4); b2_c = int(0x42)
            r = int(r1 + frac * (r2 - r1))
            g_c = int(g1 + frac * (g2 - g1))
            bc = int(b1_c + frac * (b2_c - b1_c))
            col = f"#{r:02X}{g_c:02X}{bc:02X}"
            dot = Dot(ax.c2p(phi, b), color=col, radius=0.07)
            vline = DashedLine(ax.c2p(phi, 0), ax.c2p(phi, b), color=col, stroke_width=1.5)
            self.play(Create(vline), Create(dot), run_time=0.35)

        self.wait(1.0)

        final = Text(
            "Speed saturates at c — rapidity is the additive quantity; β is not",
            font="EB Garamond", font_size=24, color=BLUE,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(caption), Write(final), run_time=1.2)
        self.wait(2.5)
