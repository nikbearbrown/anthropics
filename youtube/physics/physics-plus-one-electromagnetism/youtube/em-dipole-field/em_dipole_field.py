#!/usr/bin/env python3
"""
em_dipole_field.py — Electric Dipole Field: 1/r^3 vs Single Charge 1/r^2
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    Single: E = k*q/r^2
    Dipole axial: E_axis = 2*k*q*d/r^3  (r >> d)
    Dipole equatorial: E_eq = k*q*d/r^3  (r >> d)
    k = 8.988e9 N m^2/C^2

Verify: python3 em_dipole_field.py --verify
Render: manim -qh em_dipole_field.py EmDipoleFieldScene
"""
import sys
import numpy as np

K_COULOMB = 8.988e9  # N m^2/C^2
Q_CHARGE  = 1e-9     # C  (1 nC)
D_DIPOLE  = 0.01     # m  (1 cm separation)

def E_single(r):
    return K_COULOMB * Q_CHARGE / r**2

def E_dipole_axis(r):
    """Far-field approximation: 2kqd/r^3"""
    return 2 * K_COULOMB * Q_CHARGE * D_DIPOLE / r**3

def E_dipole_equatorial(r):
    """Far-field approximation: kqd/r^3"""
    return K_COULOMB * Q_CHARGE * D_DIPOLE / r**3

def verify():
    print("=== Electric dipole verification ===")
    r_test = 0.1  # m
    E_s  = E_single(r_test)
    E_da = E_dipole_axis(r_test)
    E_de = E_dipole_equatorial(r_test)

    print(f"At r = {r_test} m:")
    print(f"  E_single = {E_s:.1f} V/m  (expected 900 V/m) {'✓' if abs(E_s - 900) < 5 else '✗'}")
    print(f"  E_dipole_axis = {E_da:.1f} V/m  (expected 180 V/m) {'✓' if abs(E_da - 180) < 2 else '✗'}")
    print(f"  E_dipole_eq   = {E_de:.1f} V/m  (expected 90 V/m)")

    # P1: ratio E_single/E_dipole at r=0.1m = 5
    ratio = E_s / E_da
    print(f"P1: E_single/E_dipole_axis = {ratio:.2f}  (expected 5.0) {'✓' if abs(ratio - 5.0) < 0.1 else '✗'}")

    # P2: axial/equatorial = 2
    ratio2 = E_da / E_de
    print(f"P2: E_axis/E_equatorial = {ratio2:.2f}  (expected 2.0) {'✓' if abs(ratio2 - 2.0) < 0.01 else '✗'}")

    # Distance scaling: double r
    r2 = 0.2
    E_s2  = E_single(r2)
    E_da2 = E_dipole_axis(r2)
    print(f"\nDouble distance (r=0.2 m): E_single={E_s2:.1f} (÷{E_s/E_s2:.0f}), E_dipole_axis={E_da2:.1f} (÷{E_da/E_da2:.0f})")
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


class EmDipoleFieldScene(Scene):
    """
    Left: single charge field lines (radial).
    Right: dipole field lines (loops).
    Then: log-log E(r) comparison with slopes -2 vs -3.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._field_lines()
        self._log_log_plot()
        self._distance_demo()
        self._finale()

    def _title(self):
        t = Text("Electric Dipole: 1/r³ vs Single Charge 1/r²",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "Double the distance from a dipole: field drops by ×8.\n"
            "From a single charge: only ×4.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _field_lines(self):
        # Single charge: radial arrows from center
        center_l = LEFT * 3.5
        single_charge = Dot(center_l, color=BLUE, radius=0.2)
        plus = MathTex(r"+q", color=CANVAS, font_size=18).move_to(center_l)

        radial_arrows = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
            end = center_l + np.array([np.cos(angle), np.sin(angle), 0]) * 1.5
            arr = Arrow(center_l, end, color=BLUE, buff=0.2,
                        max_tip_length_to_length_ratio=0.15, stroke_width=2)
            radial_arrows.add(arr)

        single_lbl = Text("Single charge: 1/r²",
                          font="EB Garamond", font_size=18, color=BLUE)
        single_lbl.next_to(center_l + DOWN * 1.8, DOWN, buff=0.1)

        # Dipole: two charges + cardioid-ish field lines
        center_r = RIGHT * 3.5
        pos_c = center_r + LEFT * 0.4
        neg_c = center_r + RIGHT * 0.4
        pos_dot = Dot(pos_c, color=BLUE, radius=0.18)
        neg_dot = Dot(neg_c, color=BROWN, radius=0.18)
        plus_lbl = MathTex(r"+", color=CANVAS, font_size=20).move_to(pos_c)
        minus_lbl = MathTex(r"-", color=CANVAS, font_size=20).move_to(neg_c)

        # Approximate dipole field lines as arcs from + to -
        dipole_lines = VGroup()
        for r_scale in [0.8, 1.2, 1.8]:
            # Arc above
            arc_up = ArcBetweenPoints(
                pos_c + UP * 0.18,
                neg_c + UP * 0.18,
                angle=-r_scale * np.pi / 2,
                color=GOLD, stroke_width=2,
            )
            # Arc below
            arc_dn = ArcBetweenPoints(
                pos_c + DOWN * 0.18,
                neg_c + DOWN * 0.18,
                angle=r_scale * np.pi / 2,
                color=GOLD, stroke_width=2,
            )
            dipole_lines.add(arc_up, arc_dn)

        dipole_lbl = Text("Dipole: 1/r³",
                          font="EB Garamond", font_size=18, color=GOLD)
        dipole_lbl.next_to(center_r + DOWN * 1.8, DOWN, buff=0.1)

        all_mobs = [single_charge, plus, radial_arrows, single_lbl,
                    pos_dot, neg_dot, plus_lbl, minus_lbl, dipole_lines, dipole_lbl]

        self.play(
            FadeIn(single_charge), Write(plus), Create(radial_arrows), Write(single_lbl),
            FadeIn(pos_dot), FadeIn(neg_dot), Write(plus_lbl), Write(minus_lbl),
            Create(dipole_lines), Write(dipole_lbl),
            run_time=2.0,
        )
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.4)

    def _log_log_plot(self):
        r_vals = np.linspace(0.05, 0.5, 200)

        ax = Axes(
            x_range=[-1.4, -0.3, 0.5],  # log10(r) from 0.04 to 0.5 m
            y_range=[1, 5, 1],           # log10(E)
            x_length=8,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).center()
        lx = MathTex(r"\log_{10} r\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"\log_{10} E\;(\mathrm{V/m})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Single charge curve (slope -2)
        log_r = np.log10(r_vals)
        log_E_single = np.log10(E_single(r_vals))
        log_E_dipole = np.log10(np.maximum(E_dipole_axis(r_vals), 1e-10))

        pts_single = [ax.c2p(lr, le) for lr, le in zip(log_r, log_E_single)
                      if ax.y_range[0] <= le <= ax.y_range[1]]
        pts_dipole = [ax.c2p(lr, le) for lr, le in zip(log_r, log_E_dipole)
                      if ax.y_range[0] <= le <= ax.y_range[1]]

        c_single = VMobject(color=BLUE, stroke_width=3)
        c_single.set_points_smoothly(np.array(pts_single))
        c_dipole = VMobject(color=GOLD, stroke_width=3)
        c_dipole.set_points_smoothly(np.array(pts_dipole))

        # Slope labels
        s2_lbl = MathTex(r"\mathrm{slope}\ {-2}", color=BLUE, font_size=22)
        s2_lbl.move_to(ax.c2p(-0.8, 3.8))
        s3_lbl = MathTex(r"\mathrm{slope}\ {-3}", color=GOLD, font_size=22)
        s3_lbl.move_to(ax.c2p(-0.8, 2.2))

        # r=0.1 m marker
        r_mark = 0.1
        for r_v, col in [(r_mark, BLUE), (r_mark, GOLD)]:
            dot_s = Dot(ax.c2p(np.log10(r_v), np.log10(E_single(r_v))), color=BLUE, radius=0.1)
            dot_d = Dot(ax.c2p(np.log10(r_v), np.log10(E_dipole_axis(r_v))), color=GOLD, radius=0.1)
        mark_lbl = Text("r = 0.1 m:\n900 vs 180 V/m",
                        font="EB Garamond", font_size=16, color=DIM)
        mark_lbl.next_to(ax.c2p(np.log10(r_mark), 3.2), RIGHT, buff=0.2)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.2)
        self.play(Create(c_single), Write(s2_lbl), run_time=1.2)
        self.play(Create(c_dipole), Write(s3_lbl), run_time=1.2)
        self.play(FadeIn(dot_s), FadeIn(dot_d), Write(mark_lbl), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(ax, lx, ly, c_single, c_dipole, s2_lbl, s3_lbl,
                          dot_s, dot_d, mark_lbl), run_time=0.4)

    def _distance_demo(self):
        table_items = [
            ("r = 0.1 m", "E_single = 900 V/m", "E_dipole = 180 V/m", BLUE, GOLD),
            ("r = 0.2 m", "E_single = 225 V/m (÷4)", "E_dipole = 22.5 V/m (÷8)", BLUE, GOLD),
        ]
        mobs = []
        for r_str, e_s_str, e_d_str, cs, cd in table_items:
            r_m  = Text(r_str,  font="EB Garamond", font_size=24, color=INK)
            e_s  = Text(e_s_str, font="EB Garamond", font_size=22, color=cs)
            e_d  = Text(e_d_str, font="EB Garamond", font_size=22, color=cd)
            row  = VGroup(r_m, e_s, e_d).arrange(RIGHT, buff=0.5)
            mobs.append(row)
        VGroup(*mobs).arrange(DOWN, buff=0.5).center()
        for m in mobs:
            self.play(FadeIn(m), run_time=0.6)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in mobs], run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"E_{\rm single} \propto \frac{1}{r^2}",
            r"\quad E_{\rm dipole} \propto \frac{1}{r^3}",
            r"\quad \frac{E_{\rm axis}}{E_{\rm eq}} = 2",
            color=INK, font_size=30,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
