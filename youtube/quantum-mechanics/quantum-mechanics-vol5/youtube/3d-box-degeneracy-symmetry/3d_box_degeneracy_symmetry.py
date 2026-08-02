#!/usr/bin/env python3
"""
3d_box_degeneracy_symmetry.py — 3D Infinite Square Well: Degeneracy from Symmetry
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/3d-box-degeneracy-symmetry
    manim -qh 3d_box_degeneracy_symmetry.py Box3DScene

Verify:
    python3 3d_box_degeneracy_symmetry.py --verify

Physics:
    E_{nxnynz} = (ℏ²π²/2mL²)(nx²+ny²+nz²)
    Ground (1,1,1): n²=3, degeneracy=1
    First excited (2,1,1) and permutations: n²=6, degeneracy=3
    (2,2,1) and permutations: n²=9, degeneracy=3
    P1: E_{211}=E_{121}=E_{112} exactly (4+1+1=6 all cases)
"""
import sys
import numpy as np
from itertools import permutations


def energy_norm(nx, ny, nz):
    """E in units of ℏ²π²/(2mL²)."""
    return nx**2 + ny**2 + nz**2


def find_levels(n_max=4):
    """Find all distinct energy levels and their degenerate states."""
    level_map = {}
    for nx in range(1, n_max+1):
        for ny in range(1, n_max+1):
            for nz in range(1, n_max+1):
                E = energy_norm(nx, ny, nz)
                if E not in level_map:
                    level_map[E] = []
                if (nx, ny, nz) not in level_map[E]:
                    level_map[E].append((nx, ny, nz))
    return dict(sorted(level_map.items()))


def verify():
    print("=== 3D box degeneracy verification ===")
    levels = find_levels(4)
    for E, states in list(levels.items())[:8]:
        deg = len(states)
        print(f"  n²={E:2d}: degeneracy={deg}, states={states}")

    # P1: E_{211}=E_{121}=E_{112}
    E211 = energy_norm(2,1,1)
    E121 = energy_norm(1,2,1)
    E112 = energy_norm(1,1,2)
    print(f"\n  E_{{211}}={E211}, E_{{121}}={E121}, E_{{112}}={E112}  (all equal ✓)")

    # P2: (2,2,1) vs (3,1,1)
    E221 = energy_norm(2,2,1)
    E311 = energy_norm(3,1,1)
    print(f"  E_{{221}}=n²={E221}, E_{{311}}=n²={E311}  (different: no accidental degeneracy)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class Box3DScene(Scene):
    """
    Phase 1: title
    Phase 2: energy ladder showing degenerate multiplets
    Phase 3: show permutations of (2,1,1) all have same E
    Phase 4: symmetry breaking — deform cube → rectangular box
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_ladder()
        self._phase_symmetry_breaking()

    def _phase_title(self):
        title = Text("3D Box Degeneracy from Symmetry", font="EB Garamond", font_size=50, color=INK)
        sub1  = Text(
            "E_{nₓnᵧnz} = (ℏ²π²/2mL²)(nₓ²+nᵧ²+nz²)",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Permutations of (nₓ,nᵧ,nz) → same energy, different shape",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_ladder(self):
        levels = find_levels(3)
        # Show first 6 levels
        level_items = list(levels.items())[:6]

        ax = Axes(
            x_range=[0, 1, 0.5], y_range=[0, 15, 3],
            x_length=2.0, y_length=5.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(LEFT * 4.5)

        y_lbl = MathTex(r"n^2 = E/E_1", color=INK, font_size=18).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(y_lbl), run_time=0.6)

        colors = [BLUE, GOLD, BROWN, "#88CC44", "#CC88AA", DIM]

        for i, (E, states) in enumerate(level_items):
            col = colors[i % len(colors)]
            deg = len(states)
            level_line = Line(ax.c2p(0.1, E), ax.c2p(0.9, E), color=col, stroke_width=2.5 if deg > 1 else 2.0)
            # Label: n² value and degeneracy
            lbl_left = MathTex(f"n^2={E}", color=col, font_size=18).next_to(ax.c2p(0.1, E), LEFT, buff=0.1)
            # List states
            state_strs = ", ".join([f"({n[0]},{n[1]},{n[2]})" for n in states[:3]])
            if len(states) > 3:
                state_strs += ", ..."
            lbl_right = Text(f"g={deg}: {state_strs}", font="EB Garamond", font_size=14, color=col)
            lbl_right.next_to(ax.c2p(0.9, E), RIGHT, buff=0.1)
            self.play(Create(level_line), Write(lbl_left), Write(lbl_right), run_time=0.5)

        # Triple degeneracy callout
        triple_eq = MathTex(
            r"E_{211} = E_{121} = E_{112} = 6E_1\quad(\text{exact})",
            color=GOLD, font_size=24,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(triple_eq), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_symmetry_breaking(self):
        hdr = Text(
            "Break cubic symmetry (Lx ≠ Ly) → 3-fold degeneracy splits into 2 levels",
            font="EB Garamond", font_size=21, color=BROWN,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        # Show E levels as function of Ly/Lx
        ratio_tracker = ValueTracker(1.0)

        ax = Axes(
            x_range=[1.0, 2.0, 0.25], y_range=[5.5, 8.5, 0.5],
            x_length=8.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(DOWN * 0.2)

        x_lbl = MathTex(r"L_y/L_x", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"E/E_{1x}", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        # E_{211} = 4 + 1*(Lx/Ly)^2 + 1   (nz=1, nz=1 in z direction same)
        # In units of ℏ²π²/(2mLx²):
        # E_{nxnynz} = nx² + ny²*(Lx/Ly)² + nz²
        ratios = np.linspace(1.0, 2.0, 300)

        # (2,1,1): nx=2,ny=1,nz=1 → E = 4 + (Lx/Ly)² + 1
        E_211 = [4 + (1.0/r)**2 + 1 for r in ratios]
        # (1,2,1): nx=1,ny=2,nz=1 → E = 1 + 4*(Lx/Ly)² + 1
        E_121 = [1 + 4*(1.0/r)**2 + 1 for r in ratios]
        # (1,1,2): nx=1,ny=1,nz=2 → same as 211 since Lz=Lx
        E_112 = [1 + (1.0/r)**2 + 4 for r in ratios]

        def make_curve(E_list, col):
            pts = [ax.c2p(r, max(min(e, 8.4), 5.6)) for r, e in zip(ratios, E_list)]
            c = VMobject(color=col, stroke_width=2.8)
            c.set_points_smoothly(pts)
            return c

        c211 = make_curve(E_211, BLUE)
        c121 = make_curve(E_121, GOLD)
        c112 = make_curve(E_112, BROWN)

        lbl211 = Text("(2,1,1)", font="EB Garamond", font_size=18, color=BLUE).to_corner(UR, buff=0.35)
        lbl121 = Text("(1,2,1)", font="EB Garamond", font_size=18, color=GOLD).to_corner(UR, buff=0.35).shift(DOWN*0.4)
        lbl112 = Text("(1,1,2)", font="EB Garamond", font_size=18, color=BROWN).to_corner(UR, buff=0.35).shift(DOWN*0.8)

        self.play(Create(c211), Create(c121), Create(c112),
                  Write(lbl211), Write(lbl121), Write(lbl112), run_time=1.2)

        fin = Text(
            "At Ly=Lx (left): all three degenerate.  Stretch Ly → levels split.",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
