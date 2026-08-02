#!/usr/bin/env python3
"""
em_equipotentials.py — Equipotentials: E Always Perpendicular to V Contours
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    V(r) = k*q/r  (single charge)
    E = -nabla V  (gradient points down from high V)
    Equipotentials: V = const (spheres for single charge)
    Work = q*delta_V = 0 along equipotential

Verify: python3 em_equipotentials.py --verify
Render: manim -qh em_equipotentials.py EmEquipotentialsScene
"""
import sys
import numpy as np

K_COULOMB = 8.988e9
Q_CHARGE  = 1e-9    # 1 nC

def V_single(r):
    return K_COULOMB * Q_CHARGE / r

def r_of_V(V_val):
    return K_COULOMB * Q_CHARGE / V_val

def verify():
    print("=== Equipotentials verification ===")
    # P1: V at r=0.1m = 90 V
    V_10 = V_single(0.1)
    print(f"P1: V(r=0.1 m) = {V_10:.1f} V  (expected 90 V) {'✓' if abs(V_10 - 90) < 1 else '✗'}")
    # V at r=0.2m = 45 V (half)
    V_20 = V_single(0.2)
    print(f"   V(r=0.2 m) = {V_20:.1f} V  (expected 45 V) {'✓' if abs(V_20 - 45) < 0.5 else '✗'}")

    # P2: Work moving q=1nC from 90V to 45V shell = q*delta_V
    delta_V = V_10 - V_20
    W = Q_CHARGE * delta_V
    print(f"P2: Work 90V->45V = {W:.2e} J = {W*1e9:.1f} nJ  (expected 45 nJ) {'✓' if abs(W - 45e-9) < 1e-9 else '✗'}")

    # Equipotential radii for 180, 90, 45, 22.5 V
    for V_tgt in [180, 90, 45, 22.5]:
        r = r_of_V(V_tgt)
        print(f"  r(V={V_tgt:.0f} V) = {r*100:.2f} cm")
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


class EmEquipotentialsScene(Scene):
    """
    Left: single charge — concentric equipotential circles + radial field lines.
    Right: dipole — distorted equipotentials + field lines.
    Test charge sliding along equipotential: potential stays flat.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._single_charge_panel()
        self._dipole_panel()
        self._work_demo()
        self._finale()

    def _title(self):
        t = Text("Equipotentials: E ⊥ V Contours Always",
                 font="EB Garamond", font_size=52, color=INK)
        s = Text(
            "E = −∇V  —  the field is steepest where equipotentials are closest.\n"
            "No work done moving a charge along an equipotential.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _single_charge_panel(self):
        center = LEFT * 3.0

        # Charge
        charge_dot = Dot(center, color=BLUE, radius=0.2)
        plus_lbl   = MathTex(r"+q", color=CANVAS, font_size=20).move_to(center)

        # Equipotential circles (labeled)
        V_levels = [180, 90, 45, 22.5]
        r_scale = 1.5  # display: r(90V) -> 1.0 display unit
        r_base  = r_of_V(90)  # m

        eq_circles = VGroup()
        V_labels   = VGroup()
        for V_tgt, col in zip(V_levels, [GOLD, BLUE, DIM, DIM]):
            r_m = r_of_V(V_tgt)
            r_disp = (r_m / r_base) * r_scale
            circle = Circle(radius=r_disp, color=col,
                            stroke_width=2, stroke_opacity=0.8)
            circle.move_to(center)
            eq_circles.add(circle)
            lbl = MathTex(rf"{V_tgt:.0f}\,\mathrm{{V}}", color=col, font_size=16)
            lbl.next_to(circle, UR, buff=0.05)
            V_labels.add(lbl)

        # Radial field lines
        field_arrows = VGroup()
        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            r_in  = 0.25
            r_out = 3.0 * r_scale
            start = center + np.array([np.cos(angle) * r_in, np.sin(angle) * r_in, 0])
            end   = center + np.array([np.cos(angle) * r_out, np.sin(angle) * r_out, 0])
            arr = Arrow(start, end, color=BLUE, buff=0,
                        max_tip_length_to_length_ratio=0.1, stroke_width=1.5)
            field_arrows.add(arr)

        hdr = Text("Single +q", font="EB Garamond", font_size=20, color=BLUE)
        hdr.next_to(center + DOWN * 3.2, DOWN, buff=0.05)

        note = Text("Concentric spheres — field lines radiate outward",
                    font="EB Garamond", font_size=16, color=DIM)
        note.next_to(hdr, DOWN, buff=0.1)

        self.play(
            FadeIn(charge_dot), Write(plus_lbl),
            Create(eq_circles), Write(V_labels),
            Create(field_arrows),
            Write(hdr), Write(note),
            run_time=2.5,
        )
        self.wait(2.0)
        self.play(FadeOut(charge_dot, plus_lbl, eq_circles, V_labels,
                          field_arrows, hdr, note), run_time=0.4)

    def _dipole_panel(self):
        center = ORIGIN
        sep = 0.6   # display separation

        pos_dot = Dot(center + LEFT * sep/2, color=BLUE, radius=0.18)
        neg_dot = Dot(center + RIGHT * sep/2, color=BROWN, radius=0.18)
        plus_l  = MathTex(r"+", color=CANVAS, font_size=22).move_to(pos_dot)
        minus_l = MathTex(r"-", color=CANVAS, font_size=22).move_to(neg_dot)

        # Schematic dipole equipotentials (concentric ovals distorted)
        dipole_lines = VGroup()
        for r_disp, alpha in [(0.8, 0.8), (1.4, 0.7), (2.2, 0.6)]:
            # Approximate as distorted ellipses
            theta = np.linspace(0, 2*np.pi, 200)
            x = r_disp * np.cos(theta)
            y = r_disp * alpha * np.sin(theta)
            pts = np.array([[xi, yi, 0] for xi, yi in zip(x, y)])
            m = VMobject(color=GOLD, stroke_width=1.8, stroke_opacity=0.7)
            m.set_points_smoothly(pts)
            dipole_lines.add(m)

        # Dipole field lines (arcs from + to -)
        field_arcs = VGroup()
        for r_arc, col in [(0.8, BLUE), (1.4, BLUE), (2.2, BLUE)]:
            arc_u = ArcBetweenPoints(
                center + LEFT * sep/2 + UP * 0.18,
                center + RIGHT * sep/2 + UP * 0.18,
                angle=-r_arc * np.pi / 1.8,
                color=col, stroke_width=1.5, stroke_opacity=0.6,
            )
            arc_d = ArcBetweenPoints(
                center + LEFT * sep/2 + DOWN * 0.18,
                center + RIGHT * sep/2 + DOWN * 0.18,
                angle=r_arc * np.pi / 1.8,
                color=col, stroke_width=1.5, stroke_opacity=0.6,
            )
            field_arcs.add(arc_u, arc_d)

        hdr = Text("Dipole +q/−q", font="EB Garamond", font_size=20, color=GOLD)
        hdr.to_edge(DOWN, buff=0.8)
        note = Text("Equipotentials still ⊥ field lines everywhere",
                    font="EB Garamond", font_size=17, color=DIM)
        note.next_to(hdr, DOWN, buff=0.1)

        self.play(
            FadeIn(pos_dot), FadeIn(neg_dot),
            Write(plus_l), Write(minus_l),
            Create(dipole_lines), Create(field_arcs),
            Write(hdr), Write(note),
            run_time=2.5,
        )
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)

    def _work_demo(self):
        # Plot V along an equipotential (flat) and along a field line (sloped)
        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 100, 25],
            x_length=8,
            y_length=4,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.15),
        ).center()
        lx = MathTex(r"s", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"V\;(\mathrm{V})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Voltage along path", font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.1)

        # Flat line (equipotential path)
        eq_path = Line(ax.c2p(0, 90), ax.c2p(1, 90), color=BLUE, stroke_width=3)
        eq_lbl  = Text("Equipotential path (W = 0)", font="EB Garamond", font_size=18, color=BLUE)
        eq_lbl.next_to(ax.c2p(0.5, 90), UP, buff=0.15)

        # Field-line path: V drops from 90 to 22.5 as r grows
        s_vals = np.linspace(0, 1, 200)
        # Map s to radial: r(0)=0.1m (90V) to r(1)=0.4m (22.5V)
        r_vals = 0.1 + s_vals * 0.3
        V_vals = V_single(r_vals)
        fl_pts = np.array([ax.c2p(s, np.clip(v, 0, 99)) for s, v in zip(s_vals, V_vals)])
        fl_path = VMobject(color=GOLD, stroke_width=3)
        fl_path.set_points_smoothly(fl_pts)
        fl_lbl  = Text("Field-line path (V changes → W ≠ 0)", font="EB Garamond", font_size=18, color=GOLD)
        fl_lbl.next_to(ax.c2p(0.6, 45), DR, buff=0.1)

        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)
        self.play(Create(eq_path), Write(eq_lbl), run_time=1.0)
        self.play(Create(fl_path), Write(fl_lbl), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(ax, lx, ly, hdr, eq_path, eq_lbl, fl_path, fl_lbl), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"\vec{E} = -\nabla V",
            r"\quad W = q\,\Delta V = 0\ \text{(on equipotential)}",
            color=INK, font_size=30,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
