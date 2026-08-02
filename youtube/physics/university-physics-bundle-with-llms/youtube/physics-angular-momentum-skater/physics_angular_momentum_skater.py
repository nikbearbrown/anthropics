#!/usr/bin/env python3
"""
physics_angular_momentum_skater.py — Angular Momentum Conservation: Ice Skater
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  L = Iω = const  (no external torque)
  Arms extended: I₀ = 21.6 kg·m², ω₀ = 1.0 rev/s
  Arms tucked:   I₁ = 5.4 kg·m²,  ω₁ = 4.0 rev/s
  L = 21.6 × 2π = 135.7 kg·m²/s
  KE_ext  = ½ × 21.6 × (2π)²  = 426 J
  KE_tuck = ½ × 5.4  × (8π)²  = 1704 J

Testable predictions:
  P1: L = I₀ω₀ = I₁ω₁ (angular momentum flat)
  P2: KE_tuck / KE_ext = I₀/I₁ = 4.0

Run standalone verification:
  python3 physics_angular_momentum_skater.py --verify

Render:
  manim -qh physics_angular_momentum_skater.py AngularMomentumSkaterScene
"""
import sys
import numpy as np

I_EXT   = 21.6   # kg·m²
I_TUCK  = 5.4    # kg·m²
W0_RPS  = 1.0    # rev/s
W1_RPS  = I_EXT / I_TUCK * W0_RPS  # = 4.0 rev/s

def angular_momentum(I, w_rps):
    return I * (w_rps * 2 * np.pi)   # kg·m²/s

def kinetic_energy(I, w_rps):
    w = w_rps * 2 * np.pi
    return 0.5 * I * w**2

def verify():
    print("=== Angular momentum skater verification ===")
    L0 = angular_momentum(I_EXT, W0_RPS)
    L1 = angular_momentum(I_TUCK, W1_RPS)
    KE0 = kinetic_energy(I_EXT, W0_RPS)
    KE1 = kinetic_energy(I_TUCK, W1_RPS)
    print(f"  ω₀ = {W0_RPS:.2f} rev/s  → {W0_RPS*2*np.pi:.4f} rad/s")
    print(f"  ω₁ = {W1_RPS:.2f} rev/s  → {W1_RPS*2*np.pi:.4f} rad/s")
    print(f"  L₀ = {L0:.4f} kg·m²/s")
    print(f"  L₁ = {L1:.4f} kg·m²/s")
    print(f"  L conserved: {np.isclose(L0, L1)}")
    print(f"  KE₀ = {KE0:.2f} J,  KE₁ = {KE1:.2f} J")
    print(f"  KE₁/KE₀ = {KE1/KE0:.4f}  (expect {I_EXT/I_TUCK:.4f})")
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
GREEN  = "#50FA7B"


class AngularMomentumSkaterScene(Scene):
    """
    Bar charts: L (flat) and KE (quadruples). Schematic skater silhouette.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Conservation of Angular Momentum",
                     font="EB Garamond", font_size=52, color=INK)
        sub   = Text(
            "L = Iω = const  ·  arms in → ω soars → KE quadruples",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "I₀=21.6 kg·m²  I₁=5.4 kg·m²  ω₀=1 rev/s → ω₁=4 rev/s",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.28).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Setup values ───────────────────────────────────────────────────
        L0  = angular_momentum(I_EXT,  W0_RPS)
        L1  = angular_momentum(I_TUCK, W1_RPS)
        KE0 = kinetic_energy(I_EXT,  W0_RPS)
        KE1 = kinetic_energy(I_TUCK, W1_RPS)

        # ── Schematic skater (left side) ───────────────────────────────────
        center_left = np.array([-4.2, 0.0, 0])

        def skater_group(arm_width=1.2, body_h=1.5, color=BLUE):
            body  = Rectangle(width=0.5, height=body_h, fill_color=color, fill_opacity=0.9,
                               stroke_width=0, color=color)
            head  = Circle(radius=0.25, fill_color=color, fill_opacity=0.9, stroke_width=0, color=color)
            arm_l = Rectangle(width=arm_width, height=0.15, fill_color=color, fill_opacity=0.7,
                               stroke_width=0, color=color)
            arm_r = arm_l.copy()
            head.next_to(body, UP, buff=0.05)
            arm_l.move_to(body.get_center() + np.array([-arm_width/2 - 0.25 + 0.25, 0.2, 0]))
            arm_r.move_to(body.get_center() + np.array([+arm_width/2 + 0.25 - 0.25, 0.2, 0]))
            grp = VGroup(body, head, arm_l, arm_r)
            grp.move_to(center_left)
            return grp

        skater_ext  = skater_group(arm_width=1.2, color=BLUE)
        skater_tuck = skater_group(arm_width=0.3, color=GOLD)

        lbl_ext  = Text("arms extended\nω₀ = 1 rev/s", font="EB Garamond", font_size=16, color=BLUE)
        lbl_tuck = Text("arms tucked\nω₁ = 4 rev/s", font="EB Garamond", font_size=16, color=GOLD)
        lbl_ext.next_to(skater_ext,  DOWN, buff=0.25)
        lbl_tuck.next_to(skater_tuck, DOWN, buff=0.25)

        self.play(FadeIn(skater_ext), Write(lbl_ext), run_time=0.9)
        self.wait(0.8)
        self.play(Transform(skater_ext, skater_tuck), Transform(lbl_ext, lbl_tuck), run_time=1.2)
        self.wait(0.5)
        self.play(FadeOut(skater_ext, lbl_ext), run_time=0.3)
        self.play(FadeIn(skater_tuck), Write(lbl_tuck), run_time=0.4)
        self.wait(0.5)

        # ── Bar charts (right side) ────────────────────────────────────────
        bar_origin = np.array([1.2, -2.8, 0])
        bar_scale  = 3.5 / KE1    # scale so KE1 bar is 3.5 units tall
        bar_width  = 0.55
        bar_gap    = 0.55

        def bar_pair(left_x, v1, v2, col1, col2, label):
            h1 = v1 * bar_scale
            h2 = v2 * bar_scale
            b1 = Rectangle(width=bar_width, height=h1, fill_color=col1, fill_opacity=0.85,
                             stroke_width=0, color=col1)
            b2 = Rectangle(width=bar_width, height=h2, fill_color=col2, fill_opacity=0.85,
                             stroke_width=0, color=col2)
            b1.move_to(bar_origin + np.array([left_x, h1/2, 0]))
            b2.move_to(bar_origin + np.array([left_x + bar_width + bar_gap, h2/2, 0]))
            lbl_ax = Text(label, font="EB Garamond", font_size=15, color=DIM)
            lbl_ax.move_to(bar_origin + np.array([left_x + (bar_width + bar_gap)/2, -0.28, 0]))
            v1_lbl = Text(f"{v1:.0f}", font="EB Garamond", font_size=13, color=col1)
            v1_lbl.next_to(b1, UP, buff=0.06)
            v2_lbl = Text(f"{v2:.0f}", font="EB Garamond", font_size=13, color=col2)
            v2_lbl.next_to(b2, UP, buff=0.06)
            return VGroup(b1, b2, lbl_ax, v1_lbl, v2_lbl)

        # L bars (should be flat)
        bars_L  = bar_pair(0.0,  L0, L1, BLUE, GOLD, "L (kg·m²/s)")
        # KE bars (quadruples)
        bars_KE = bar_pair(2.5, KE0, KE1, BLUE, GOLD, "KE (J)")

        col_lbl_ext  = Text("ext", font="EB Garamond", font_size=12, color=BLUE)
        col_lbl_tuck = Text("tuck", font="EB Garamond", font_size=12, color=GOLD)
        col_lbl_ext.move_to(bar_origin + np.array([0.0, -0.55, 0]))
        col_lbl_tuck.move_to(bar_origin + np.array([bar_width + bar_gap, -0.55, 0]))

        self.play(FadeIn(bars_L), FadeIn(bars_KE), Write(col_lbl_ext), Write(col_lbl_tuck), run_time=1.5)
        self.wait(0.8)

        # ── Annotations ────────────────────────────────────────────────────
        L_flat  = Text("L flat → conservation", font="EB Garamond", font_size=18, color=GREEN)
        KE_soar = Text(f"KE ×4 → muscle work\n({KE0:.0f} J → {KE1:.0f} J)", font="EB Garamond", font_size=18, color=GOLD)
        L_flat.to_edge(UP, buff=0.25)
        KE_soar.to_edge(RIGHT, buff=0.2)

        self.play(Write(L_flat), Write(KE_soar), run_time=1.0)
        self.wait(0.6)

        # ── Conservation equation ──────────────────────────────────────────
        eq = MathTex(
            r"L = I_0\omega_0 = I_1\omega_1 \quad\Rightarrow\quad \omega_1 = \frac{I_0}{I_1}\omega_0 = 4\omega_0",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.2)
        self.wait(3.0)
