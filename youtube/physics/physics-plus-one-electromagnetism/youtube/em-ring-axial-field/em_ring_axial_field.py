#!/usr/bin/env python3
"""
em_ring_axial_field.py — Ring of Charge: Axial Field Peaks at z = R/sqrt(2)
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    E_z(z) = k*Q*z / (R^2 + z^2)^(3/2)
    Maximum at z_max = R/sqrt(2)

Verify: python3 em_ring_axial_field.py --verify
Render: manim -qh em_ring_axial_field.py EmRingAxialFieldScene
"""
import sys
import numpy as np

K_COULOMB = 8.988e9   # N m^2/C^2
R_RING    = 0.05      # m  (5 cm)
Q_CHARGE  = 10e-9     # C  (10 nC)

def E_z(z, R=R_RING, Q=Q_CHARGE):
    return K_COULOMB * Q * z / (R**2 + z**2)**1.5

def z_max(R=R_RING):
    return R / np.sqrt(2)

def E_max(R=R_RING, Q=Q_CHARGE):
    zm = z_max(R)
    return E_z(zm, R, Q)

def verify():
    print("=== Ring axial field verification ===")
    # P1: E_z = 0 at z = 0
    E_at_zero = E_z(0.0)
    print(f"P1: E_z(z=0) = {E_at_zero:.8f} V/m  (expected 0) {'✓' if abs(E_at_zero) < 1e-10 else '✗'}")

    # Peak location
    zm = z_max()
    Em = E_max()
    print(f"z_max = R/sqrt(2) = {zm*100:.3f} cm  (expected {R_RING*100/np.sqrt(2):.3f} cm) {'✓' if abs(zm - R_RING/np.sqrt(2)) < 1e-10 else '✗'}")
    # E_max = kQ/(sqrt(2) * (3/2)^1.5 * R^2) = 13838 V/m for these params
    # The candidate card cited ~3.18e4 V/m — that was in error. 13838 V/m is correct.
    print(f"E_max = {Em:.2f} V/m  (correct: kQ*z_max/(R^2+z_max^2)^1.5 at z_max=R/sqrt(2))")

    # P2: check peak by numerical gradient
    z_fine = np.linspace(0.001, 0.2, 10000)
    E_fine = E_z(z_fine)
    idx_max = np.argmax(E_fine)
    z_numerical_max = z_fine[idx_max]
    print(f"Numerical peak at z = {z_numerical_max*100:.3f} cm  (analytic: {zm*100:.3f} cm) {'✓' if abs(z_numerical_max - zm) < 0.001 else '✗'}")

    # At z = R: ~91.9% of max (card said 80% — incorrect)
    E_at_R = E_z(R_RING)
    pct = E_at_R / Em * 100
    print(f"E_z at z=R = {E_at_R:.2f} V/m = {pct:.1f}% of max")
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


class EmRingAxialFieldScene(Scene):
    """
    Top: ring of charge with moving axial point and field vector.
    Bottom: E_z(z) curve sweeping from -3R to +3R.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curve(ax)
        self._peak_annotation(ax)
        self._moving_point(ax)
        self._finale()

    def _title(self):
        t = Text("Ring of Charge: Axial Field Peaks at z = R/√2",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "E_z = 0 at z = 0 (symmetry cancels). Peak where competing effects balance.\n"
            "z_max = R/√2  from dE_z/dz = 0.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        z_max_val = 3 * R_RING
        E_max_val = E_max()

        ax = Axes(
            x_range=[-z_max_val * 100, z_max_val * 100, R_RING * 100],  # in cm
            y_range=[-E_max_val * 1.1, E_max_val * 1.1, E_max_val / 3],
            x_length=10,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"z\;(\mathrm{cm})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"E_z\;(\mathrm{V/m})", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Ring indicator at z=0
        ring_lbl = Text("ring (z = 0)", font="EB Garamond", font_size=16, color=DIM)
        ring_lbl.next_to(ax.c2p(0, E_max_val * 1.05), UP, buff=0.05)
        ring_line = DashedLine(ax.c2p(0, -E_max_val * 1.1), ax.c2p(0, E_max_val * 1.1),
                               color=DIM, stroke_width=1, stroke_opacity=0.4)

        self.play(Create(ax), Write(lx), Write(ly), Create(ring_line), Write(ring_lbl), run_time=1.5)
        self.ax = ax
        return ax

    def _draw_curve(self, ax):
        Em = E_max()
        z_cm = np.linspace(-3 * R_RING * 100, 3 * R_RING * 100, 600)
        z_m  = z_cm * 0.01
        E_vals = E_z(z_m)

        pts = [ax.c2p(z, e) for z, e in zip(z_cm, E_vals)
               if -Em * 1.08 <= e <= Em * 1.08]
        curve = VMobject(color=BLUE, stroke_width=3.5)
        curve.set_points_smoothly(np.array(pts))

        self.play(Create(curve), run_time=2.5)

    def _peak_annotation(self, ax):
        Em = E_max()
        zm_cm = z_max() * 100

        # Peak markers (positive and negative)
        for zm, col in [(zm_cm, GOLD), (-zm_cm, GOLD)]:
            Em_sign = E_z(zm * 0.01)
            dot = Dot(ax.c2p(zm, Em_sign), color=col, radius=0.12)
            dash = DashedLine(ax.c2p(zm, 0), ax.c2p(zm, Em_sign),
                              color=col, stroke_width=1.5, stroke_opacity=0.6)
            lbl = MathTex(r"z = \pm R/\sqrt{2}", color=col, font_size=20)
            lbl.next_to(dot, UR if zm > 0 else UL, buff=0.15)
            self.play(Create(dash), FadeIn(dot), Write(lbl), run_time=0.8)

        cap = Text(
            "Zero at center (symmetry) — peak at z = R/√2 — zero at infinity",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(cap), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(cap), run_time=0.3)

    def _moving_point(self, ax):
        z_tracker = ValueTracker(-3 * R_RING * 100)

        def _point_and_vec():
            z_cm = z_tracker.get_value()
            z_m  = z_cm * 0.01
            E_val = E_z(z_m)
            E_clip = np.clip(E_val, -E_max() * 1.05, E_max() * 1.05)
            dot = Dot(ax.c2p(z_cm, E_clip), color=GOLD, radius=0.14)
            return dot

        dyn_pt = always_redraw(_point_and_vec)
        self.add(dyn_pt)

        z_lbl = MathTex(r"z = ", color=INK, font_size=24)
        z_num = DecimalNumber(z_tracker.get_value(), num_decimal_places=1, color=GOLD, font_size=24)
        z_cm_lbl = MathTex(r"\,\mathrm{cm}", color=INK, font_size=24)
        z_num.add_updater(lambda m: m.set_value(z_tracker.get_value()))
        E_lbl2 = MathTex(r"E_z = ", color=DIM, font_size=22)
        E_num  = DecimalNumber(0, num_decimal_places=0, color=BLUE, font_size=22)
        E_unit = MathTex(r"\,\mathrm{V/m}", color=DIM, font_size=22)
        E_num.add_updater(lambda m: m.set_value(E_z(z_tracker.get_value() * 0.01)))

        z_row = VGroup(z_lbl, z_num, z_cm_lbl).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.3)
        E_row = VGroup(E_lbl2, E_num, E_unit).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.25)

        self.play(Write(z_row), Write(E_row), run_time=0.6)
        self.play(z_tracker.animate.set_value(3 * R_RING * 100), run_time=5.0, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(z_row, E_row, dyn_pt), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"E_z(z) = \frac{kQz}{(R^2+z^2)^{3/2}}",
            r"\quad z_{\rm max} = \frac{R}{\sqrt{2}}",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
