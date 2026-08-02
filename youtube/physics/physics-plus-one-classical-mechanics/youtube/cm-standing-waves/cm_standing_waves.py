#!/usr/bin/env python3
"""
cm_standing_waves.py — Standing Waves: Harmonics and n=1..4 Node Structure
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    f_n = n * v / (2L),  v = sqrt(F_T/mu)
    Nodes at x = k*L/n, k=0..n
    Antinodes at x = (2k+1)*L/(2n)

Verify: python3 cm_standing_waves.py --verify
Render: manim -qh cm_standing_waves.py CmStandingWavesScene
"""
import sys
import numpy as np

L = 1.0       # m
V_WAVE = 200  # m/s  (typical guitar string)

def f_n(n):
    return n * V_WAVE / (2 * L)

def node_positions(n):
    return [k * L / n for k in range(n + 1)]

def antinode_positions(n):
    return [(2*k + 1) * L / (2*n) for k in range(n)]

def standing_wave(x, n, t, A=1.0):
    return A * np.sin(n * np.pi * x / L) * np.cos(2 * np.pi * f_n(n) * t)

def verify():
    print("=== Standing waves verification ===")
    for n in range(1, 5):
        f = f_n(n)
        nodes = node_positions(n)
        antinodes = antinode_positions(n)
        print(f"n={n}: f={f:.0f} Hz, {len(nodes)-2} interior nodes at {[f'{p:.3f}' for p in nodes[1:-1]]}")
    # P1: n=3, 2 interior nodes at L/3 and 2L/3
    nodes3 = node_positions(3)
    assert abs(nodes3[1] - L/3) < 1e-9, f"Node 1 wrong: {nodes3[1]}"
    assert abs(nodes3[2] - 2*L/3) < 1e-9, f"Node 2 wrong: {nodes3[2]}"
    print(f"P1: n=3 interior nodes at L/3={L/3:.4f}, 2L/3={2*L/3:.4f} ✓")
    # P2: f4/f1 = 4
    ratio = f_n(4) / f_n(1)
    print(f"P2: f4/f1 = {ratio:.1f}  (expected 4.0) {'✓' if ratio == 4.0 else '✗'}")
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

HARMONIC_COLORS = [BLUE, GOLD, BROWN, DIM]


class CmStandingWavesScene(Scene):
    """
    String with n=1..4 harmonics drawn sequentially.
    Nodes (red dots), antinodes (max displacement), frequency bar chart.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._harmonics()
        self._spectrum()
        self._finale()

    def _title(self):
        t = Text("Standing Waves: Harmonics n = 1 to 4",
                 font="EB Garamond", font_size=56, color=INK)
        s = Text(
            "Nodes and antinodes are fixed in space.\n"
            "Frequencies form an exact integer series: f_n = n × f₁",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _harmonics(self):
        x_vals = np.linspace(0, L, 300)
        string_y_base = 1.5  # display y center for n=1

        all_mobs = []
        for n, col in enumerate(HARMONIC_COLORS, start=1):
            # Vertical offset so harmonics don't overlap
            y_center = 2.5 - (n - 1) * 1.6

            # String at rest (equilibrium)
            eq_line = Line(
                np.array([-5, y_center, 0]),
                np.array([5, y_center, 0]),
                color=DIM, stroke_width=0.5, stroke_opacity=0.3,
            )

            # Scale: string spans -5 to 5 display units
            def x_to_display(x):
                return -5 + x * 10 / L

            # Standing wave shape (t=pi/2 for max displacement)
            A = 0.6
            y_wave = A * np.sin(n * np.pi * x_vals / L)

            # Map to display coords
            pts = np.array([[x_to_display(xi), y_center + yi, 0]
                            for xi, yi in zip(x_vals, y_wave)])
            wave_mob = VMobject(color=col, stroke_width=3)
            wave_mob.set_points_smoothly(pts)

            # Mirror (negative half)
            pts_neg = np.array([[x_to_display(xi), y_center - yi, 0]
                                for xi, yi in zip(x_vals, y_wave)])
            wave_mob_neg = VMobject(color=col, stroke_width=1.5, stroke_opacity=0.4)
            wave_mob_neg.set_points_smoothly(pts_neg)

            # Node dots (fixed boundary nodes included)
            node_dots = VGroup(*[
                Dot(np.array([x_to_display(xn), y_center, 0]),
                    color=BROWN, radius=0.12)
                for xn in node_positions(n)
            ])

            # Antinode dots
            antinode_dots = VGroup(*[
                Dot(np.array([x_to_display(xa), y_center + A * np.sin(n * np.pi * xa / L), 0]),
                    color=GOLD, radius=0.08)
                for xa in antinode_positions(n)
            ])

            # Label
            fn_val = f_n(n)
            fn_lbl = MathTex(rf"n={n},\ f={fn_val:.0f}\,\mathrm{{Hz}}", color=col, font_size=22)
            fn_lbl.move_to(np.array([6.5, y_center, 0]))

            row_mobs = [eq_line, wave_mob, wave_mob_neg, node_dots, antinode_dots, fn_lbl]
            all_mobs.extend(row_mobs)

            self.play(Create(wave_mob), Create(wave_mob_neg),
                      FadeIn(node_dots), FadeIn(antinode_dots),
                      Write(fn_lbl), run_time=0.9)
            self.wait(0.6)

        # Annotate
        node_note = Text("● nodes: zero displacement",
                         font="EB Garamond", font_size=18, color=BROWN).to_edge(DOWN, buff=0.5)
        anti_note = Text("● antinodes: max displacement",
                         font="EB Garamond", font_size=18, color=GOLD)
        anti_note.next_to(node_note, RIGHT, buff=0.5)
        self.play(Write(node_note), Write(anti_note), run_time=0.8)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in all_mobs], FadeOut(node_note, anti_note), run_time=0.4)

    def _spectrum(self):
        # Bar chart: f_1=100, f_2=200, f_3=300, f_4=400 Hz
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 450, 100],
            x_length=7,
            y_length=4,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.15),
        ).center()
        lx = Text("Harmonic n", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"f_n\;(\mathrm{Hz})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Frequency spectrum", font="EB Garamond", font_size=22, color=DIM).next_to(ax, UP, buff=0.1)

        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        for n, col in enumerate(HARMONIC_COLORS, start=1):
            fn_val = f_n(n)
            bar = Rectangle(
                width=0.4,
                height=ax.c2p(0, fn_val)[1] - ax.c2p(0, 0)[1],
                fill_color=col, fill_opacity=0.8, stroke_width=0,
            )
            bar.align_to(ax.c2p(n, 0), DOWN + LEFT)
            bar.shift(RIGHT * 0.0)
            # Position bar centered at x=n
            bar.move_to(ax.c2p(n, fn_val / 2))
            bar.set_width(0.4)

            n_lbl = Text(str(n), font="EB Garamond", font_size=18, color=col)
            n_lbl.next_to(bar, DOWN, buff=0.1)
            f_lbl = MathTex(rf"{fn_val:.0f}", color=col, font_size=18)
            f_lbl.next_to(bar, UP, buff=0.05)

            self.play(FadeIn(bar), Write(n_lbl), Write(f_lbl), run_time=0.5)

        ratio_lbl = MathTex(r"f_n = n f_1", color=GOLD, font_size=30).to_edge(DOWN, buff=0.3)
        self.play(Write(ratio_lbl), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(ax, lx, ly, hdr, ratio_lbl), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"f_n = \frac{n v}{2L}",
            r"\quad v = \sqrt{F_T/\mu}",
            r"\quad n = 1,2,3,\ldots",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
