#!/usr/bin/env python3
"""
physics_dipole_field_falloff.py — Dipole Field 1/r³ vs Monopole 1/r²
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    q = 1 nC, d = 0.01 m → p = 10⁻¹¹ C·m
    E_axis = 2kp/r³,  E_monopole = kq/r²
    At r=0.05 m: E_axis = 1440 N/C, E_mono = 3600 N/C

Render:
    cd physics/youtube/physics-dipole-field-falloff
    manim -qh physics_dipole_field_falloff.py DipoleFieldScene
"""
import sys
import numpy as np

K_E = 9e9    # N·m²/C²
Q   = 1e-9   # C
D   = 0.01   # m
P   = Q * D  # dipole moment

def E_monopole(r): return K_E * Q / r**2
def E_dipole_axis(r): return 2 * K_E * P / r**3


def verify():
    print("=== Dipole Field Falloff verification ===")
    for r in [0.05, 0.10, 0.20]:
        em = E_monopole(r)
        ed = E_dipole_axis(r)
        print(f"  r={r:.2f} m: E_mono={em:.1f} N/C, E_dipole={ed:.1f} N/C, ratio={ed/em:.4f}")
    # P1: at r=0.05, E_axis = 1440 N/C
    r1 = 0.05
    assert abs(E_dipole_axis(r1) - 1440) < 1, f"P1 failed: {E_dipole_axis(r1)}"
    # P2: ratio at r=0.10 vs r=0.05 for each
    drop_mono = E_monopole(0.05)/E_monopole(0.10)
    drop_dip  = E_dipole_axis(0.05)/E_dipole_axis(0.10)
    print(f"  Doubling r: monopole drops by {drop_mono:.1f}×, dipole drops by {drop_dip:.1f}× (ratio = {drop_dip/drop_mono:.2f})")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class DipoleFieldScene(Scene):
    """Dipole field-line figure-eight + log-log falloff comparison."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._field_lines()
        self._falloff_comparison()

    def _title(self):
        t1 = Text("Electric Dipole Field", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("1/r³ falloff — faster than a point charge's 1/r²", font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"E_{\rm axis} = \frac{2kp}{r^3} \qquad p = qd", color=BLUE, font_size=30)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _field_lines(self):
        """Draw approximate dipole field-line figure-eight pattern."""
        # Place charges
        pos_charge = Dot(UP*0.8, color=BLUE, radius=0.18)
        neg_charge = Dot(DOWN*0.8, color=BROWN, radius=0.18)
        lbl_pos = MathTex(r"+q", color=BLUE, font_size=22).next_to(pos_charge, RIGHT, buff=0.1)
        lbl_neg = MathTex(r"-q", color=BROWN, font_size=22).next_to(neg_charge, RIGHT, buff=0.1)
        self.play(FadeIn(pos_charge, neg_charge, lbl_pos, lbl_neg), run_time=0.8)

        # Draw parametric dipole field lines (approximate closed curves)
        lines = []
        for angle_deg in range(0, 360, 30):
            angle = np.radians(angle_deg)
            # Parametric field line in dipole approximation (polar coords)
            thetas = np.linspace(0.1, np.pi - 0.1, 80)
            # r = r0 * sin²(theta) — standard dipole field line
            r0 = 1.5
            rs = r0 * np.sin(thetas)**2
            xs = rs * np.sin(thetas) * np.cos(angle)
            ys = rs * np.cos(thetas)
            pts = np.array([[x, y, 0] for x, y in zip(xs, ys)])
            col = BLUE if angle_deg < 180 else BROWN
            line = VMobject(color=col, stroke_width=1.8, stroke_opacity=0.7)
            line.set_points_smoothly(pts)
            lines.append(line)

        self.play(*[Create(l) for l in lines], run_time=2.5)
        hdr = Text(
            "Dipole field lines — figure-eight from +q to −q",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(hdr), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(*lines, pos_charge, neg_charge, lbl_pos, lbl_neg, hdr), run_time=0.5)

    def _falloff_comparison(self):
        ax = Axes(
            x_range=[0.04, 0.25, 0.05],
            y_range=[0, 4000, 1000],
            x_length=10,
            y_length=5.2,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.4)
        lx = MathTex(r"r\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"E\;(\mathrm{N/C})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Field strength vs distance  (q = 1 nC, d = 1 cm)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        rs = np.linspace(0.05, 0.24, 500)
        em = E_monopole(rs)
        ed = E_dipole_axis(rs)

        pts_m = np.array([ax.c2p(r, min(e, 3900)) for r, e in zip(rs, em)])
        pts_d = np.array([ax.c2p(r, min(e, 3900)) for r, e in zip(rs, ed)])

        crv_m = VMobject(color=BLUE,  stroke_width=3.0).set_points_smoothly(pts_m)
        crv_d = VMobject(color=BROWN, stroke_width=3.0).set_points_smoothly(pts_d)

        lbl_m = Text("Monopole  1/r²", font="EB Garamond", font_size=20, color=BLUE)
        lbl_m.move_to(ax.c2p(0.14, 1200))
        lbl_d = Text("Dipole  1/r³", font="EB Garamond", font_size=20, color=BROWN)
        lbl_d.move_to(ax.c2p(0.18, 400))

        self.play(Create(crv_m), Write(lbl_m), run_time=1.5)
        self.play(Create(crv_d), Write(lbl_d), run_time=1.5)

        # Dots at r=0.05 m
        d_m = Dot(ax.c2p(0.05, E_monopole(0.05)), color=BLUE, radius=0.10)
        d_d = Dot(ax.c2p(0.05, E_dipole_axis(0.05)), color=BROWN, radius=0.10)
        lbl_vals = MathTex(r"r=0.05\,\mathrm{m}:\;3600\;\mathrm{vs}\;1440\,\mathrm{N/C}",
                           color=GOLD, font_size=20).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(d_m, d_d), Write(lbl_vals), run_time=0.8)

        final = Text(
            "Dipole field falls one extra power of r — cancellation at large distances",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.wait(1.5)
        self.play(FadeOut(lbl_vals), Write(final), run_time=0.9)
        self.wait(2.5)
