"""scenes.py — atom-and-laser-quantize-worked
Bears Notes deep-worked example: standing waves → laser modes → particle-in-box.
All beats render=manim.  Math via MathTex (LaTeX).
"""
import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
ACCENT = "#5A5653"   # warm slate — accent wave / box
RED    = "#C0392B"   # punchline numbers
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', '')
except Exception:
    DUR = {}; TITLE = ''

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def ink_tex(t, size=40, **kw):
    return MathTex(t, font_size=size, color=INK, **kw)

def accent_tex(t, size=40, **kw):
    return MathTex(t, font_size=size, color=ACCENT, **kw)

def red_tex(t, size=40, **kw):
    return MathTex(t, font_size=size, color=RED, **kw)


# ── Geometry helpers ───────────────────────────────────────────────────────────
WALL_H = 3.0
WALL_X_L = -4.0
WALL_X_R =  4.0
WAVE_Y = -0.5   # y of the baseline between walls

def make_walls(color=INK):
    wall_l = Line([WALL_X_L, WAVE_Y - WALL_H / 2, 0],
                  [WALL_X_L, WAVE_Y + WALL_H / 2, 0],
                  color=color, stroke_width=6)
    wall_r = Line([WALL_X_R, WAVE_Y - WALL_H / 2, 0],
                  [WALL_X_R, WAVE_Y + WALL_H / 2, 0],
                  color=color, stroke_width=6)
    return VGroup(wall_l, wall_r)

def standing_wave(n=1, amplitude=0.9, color=ACCENT, x_pts=300):
    """n half-waves between WALL_X_L and WALL_X_R."""
    L = WALL_X_R - WALL_X_L
    xs = np.linspace(WALL_X_L, WALL_X_R, x_pts)
    ys = amplitude * np.sin(n * np.pi * (xs - WALL_X_L) / L)
    pts = [[x, WAVE_Y + y, 0] for x, y in zip(xs, ys)]
    return VMobject(color=color, stroke_width=3).set_points_smoothly(pts)

def mismatched_wave(phase_offset=0.4, amplitude=0.8, color=RED, x_pts=300):
    """A wave that does NOT vanish at the walls."""
    L = WALL_X_R - WALL_X_L
    xs = np.linspace(WALL_X_L, WALL_X_R, x_pts)
    k = 1.3 * np.pi / L   # not an integer multiple → mismatch
    ys = amplitude * np.sin(k * (xs - WALL_X_L) + phase_offset)
    pts = [[x, WAVE_Y + y, 0] for x, y in zip(xs, ys)]
    return VMobject(color=color, stroke_width=3).set_points_smoothly(pts)


# ── INTRO ──────────────────────────────────────────────────────────────────────
class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        series = ink_txt("Bear's Notes", size=32).move_to([0, 1.8, 0])
        title = ink_txt("Why an Atom and a Laser\nQuantize for the Same Reason",
                        size=42, line_spacing=1.3).move_to([0, -0.2, 0])
        # motif: small standing wave under the title
        wave = standing_wave(n=2, amplitude=0.35, color=ACCENT)
        wave.move_to([0, -2.0, 0])
        self.play(Write(series), run_time=0.8)
        self.play(Write(title), run_time=d("INTRO", 4.33) * 0.6)
        self.play(Create(wave), run_time=d("INTRO", 4.33) * 0.25)
        self.wait(d("INTRO", 4.33) * 0.05)


# ── H01 ───────────────────────────────────────────────────────────────────────
class H01_Hook(Scene):
    def construct(self):
        self.add(bg())
        left = ink_txt("laser: exact colours", size=34).move_to([-3.2, 0.8, 0])
        right = ink_txt("atom: exact energies", size=34).move_to([3.2, 0.8, 0])
        # Spectral lines motif under each
        n_lines = 5
        colors_l = ["#e74c3c", "#e67e22", "#2ecc71", "#3498db", "#9b59b6"]
        lines_l = VGroup(*[
            Line([WALL_X_L + 0.3 + 1.2 * i, -0.3, 0],
                 [WALL_X_L + 0.3 + 1.2 * i, -1.5, 0],
                 color=c, stroke_width=5)
            for i, c in enumerate(colors_l)
        ])
        lines_r = VGroup(*[
            Line([0.5 + 1.2 * i, -0.3, 0], [0.5 + 1.2 * i, -1.5, 0],
                 color=ACCENT, stroke_width=5)
            for i in range(n_lines)
        ])
        self.play(Write(left), Write(right), run_time=d("H01", 4.82) * 0.5)
        self.play(Create(lines_l), Create(lines_r), run_time=d("H01", 4.82) * 0.4)
        self.wait(d("H01", 4.82) * 0.1)


# ── H02 ───────────────────────────────────────────────────────────────────────
class H02_OneRule(Scene):
    def construct(self):
        self.add(bg())
        headline = ink_txt("Both come from one rule:", size=36).move_to([0, 1.5, 0])
        rule = ink_txt("a wave has to fit between two walls", size=36, slant=ITALIC).move_to([0, 0.5, 0])
        walls = make_walls(color=INK)
        wave = standing_wave(n=2, amplitude=0.8, color=ACCENT)
        self.play(Write(headline), run_time=0.7)
        self.play(Write(rule), run_time=1.0)
        self.play(Create(walls), Create(wave), run_time=d("H02", 4.18) * 0.5)
        self.wait(d("H02", 4.18) * 0.1)


# ── A01 ───────────────────────────────────────────────────────────────────────
class A01_WallsMismatched(Scene):
    def construct(self):
        self.add(bg())
        walls = make_walls()
        bad_wave = mismatched_wave()
        lbl = ink_txt("most wavelengths cancel", size=30).move_to([0, 2.2, 0])
        self.play(Create(walls), run_time=0.7)
        self.play(Create(bad_wave), Write(lbl), run_time=d("A01", 4.54) * 0.7)
        self.play(bad_wave.animate.set_opacity(0.2).set_color(INK),
                  run_time=d("A01", 4.54) * 0.2)
        self.wait(d("A01", 4.54) * 0.1)


# ── A02 ───────────────────────────────────────────────────────────────────────
class A02_StandingWave(Scene):
    def construct(self):
        self.add(bg())
        walls = make_walls()
        bad_wave = mismatched_wave().set_opacity(0.2).set_color(INK)
        self.add(walls, bad_wave)
        good = standing_wave(n=1, amplitude=0.9, color=ACCENT)
        zeros_l = Dot([WALL_X_L, WAVE_Y, 0], radius=0.1, color=ACCENT)
        zeros_r = Dot([WALL_X_R, WAVE_Y, 0], radius=0.1, color=ACCENT)
        lbl = ink_txt("standing wave — zero at both walls", size=28).move_to([0, 2.2, 0])
        self.play(Create(good), FadeIn(zeros_l), FadeIn(zeros_r), Write(lbl),
                  run_time=d("A02", 4.29) * 0.85)
        self.wait(d("A02", 4.29) * 0.15)


# ── M01 ───────────────────────────────────────────────────────────────────────
class M01_SharedRule(Scene):
    def construct(self):
        self.add(bg())
        headline = ink_txt("The shared rule:", size=34).move_to([0, 2.8, 0])
        # Two branch labels
        laser_lbl = ink_txt("laser cavity", size=30, color=ACCENT).move_to([-3.5, -0.5, 0])
        atom_lbl = ink_txt("electron in box", size=30, color=ACCENT).move_to([3.5, -0.5, 0])
        # Arrow from centre to each
        arr_l = Arrow([0, 0.2, 0], [-2.8, -0.3, 0], color=INK, buff=0.05, tip_length=0.15)
        arr_r = Arrow([0, 0.2, 0], [2.8, -0.3, 0], color=INK, buff=0.05, tip_length=0.15)
        self.play(Write(headline), run_time=0.6)
        self.play(Create(arr_l), Create(arr_r),
                  Write(laser_lbl), Write(atom_lbl),
                  run_time=d("M01", 3.88) * 0.8)
        self.wait(d("M01", 3.88) * 0.2)


# ── M02 ───────────────────────────────────────────────────────────────────────
class M02_SharedFormula(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=72)
        box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.3)
        lbl = ink_txt("n half-wavelengths fit exactly", size=30).next_to(box, DOWN, buff=0.4)
        self.play(Write(rule_tex), Create(box), run_time=d("M02", 3.01) * 0.85)
        self.play(Write(lbl), run_time=0.5)
        self.wait(d("M02", 3.01) * 0.15)


# ── M03 ───────────────────────────────────────────────────────────────────────
class M03_LaserBranch(Scene):
    def construct(self):
        self.add(bg())
        # Shared rule at top
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=52).move_to([0, 3.2, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.2)
        # Laser derivation
        laser_header = ink_txt("Laser cavity", size=30, color=ACCENT).move_to([-0.5, 1.8, 0])
        laser_tex = ink_tex(r"f_n = \frac{nc}{2L}", size=58).move_to([0, 0.5, 0])
        self.play(Write(rule_tex), Create(rule_box), run_time=0.6)
        self.play(Write(laser_header), run_time=0.4)
        self.play(Write(laser_tex), run_time=d("M03", 5.46) * 0.75)
        self.wait(d("M03", 5.46) * 0.15)


# ── M04 ───────────────────────────────────────────────────────────────────────
class M04_AtomBranch(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=46).move_to([0, 3.5, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.2)
        laser_header = ink_txt("Laser", size=28, color=ACCENT).move_to([-3.8, 2.0, 0])
        laser_tex = ink_tex(r"f_n = \frac{nc}{2L}", size=44).move_to([-3.8, 1.0, 0])
        atom_header = ink_txt("Electron in box", size=28, color=ACCENT).move_to([3.0, 2.0, 0])
        atom_tex = ink_tex(r"E_n = \frac{n^2 h^2}{8 m L^2}", size=44).move_to([3.0, 0.8, 0])
        self.add(rule_tex, rule_box, laser_header, laser_tex)
        self.play(Write(atom_header), run_time=0.5)
        self.play(Write(atom_tex), run_time=d("M04", 6.61) * 0.8)
        self.wait(d("M04", 6.61) * 0.15)


# ── W01 ───────────────────────────────────────────────────────────────────────
class W01_NumbersSetup(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=46).move_to([0, 3.5, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.2)
        # Two column headers
        laser_col = ink_txt("Laser cavity", size=30, color=ACCENT).move_to([-3.5, 2.0, 0])
        atom_col = ink_txt("Electron in box", size=30, color=ACCENT).move_to([3.5, 2.0, 0])
        divider = Line([0, 1.5, 0], [0, -3.5, 0], color=INK, stroke_width=1.5)
        lbl = ink_txt("Put numbers on both", size=34).move_to([0, -0.5, 0])
        self.play(Write(rule_tex), Create(rule_box), run_time=0.5)
        self.play(Write(laser_col), Write(atom_col), Create(divider),
                  Write(lbl), run_time=d("W01", 1.73) * 0.9)
        self.wait(d("W01", 1.73) * 0.1)


# ── W02 ───────────────────────────────────────────────────────────────────────
class W02_LaserNumbers(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=40).move_to([0, 3.5, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.15)
        laser_col = ink_txt("Laser cavity", size=28, color=ACCENT).move_to([-3.5, 2.5, 0])
        atom_col = ink_txt("Electron in box", size=28, color=ACCENT).move_to([3.5, 2.5, 0])
        divider = Line([0, 2.0, 0], [0, -3.5, 0], color=INK, stroke_width=1.0)
        self.add(rule_tex, rule_box, laser_col, atom_col, divider)
        # L = 0.30 m, mode spacing
        l_given = ink_tex(r"L = 0.30\;\text{m}", size=38).move_to([-3.5, 1.3, 0])
        spacing_tex = red_tex(r"\Delta f = \frac{c}{2L} \approx 500\;\text{MHz}", size=40
                              ).move_to([-3.5, 0.1, 0])
        self.play(Write(l_given), run_time=0.6)
        self.play(Write(spacing_tex), run_time=d("W02", 6.66) * 0.75)
        self.wait(d("W02", 6.66) * 0.15)


# ── W03 ───────────────────────────────────────────────────────────────────────
class W03_ModeCount(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=40).move_to([0, 3.5, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.15)
        laser_col = ink_txt("Laser cavity", size=28, color=ACCENT).move_to([-3.5, 2.5, 0])
        atom_col = ink_txt("Electron in box", size=28, color=ACCENT).move_to([3.5, 2.5, 0])
        divider = Line([0, 2.0, 0], [0, -3.5, 0], color=INK, stroke_width=1.0)
        l_given = ink_tex(r"L = 0.30\;\text{m}", size=38).move_to([-3.5, 1.3, 0])
        spacing_tex = red_tex(r"\Delta f \approx 500\;\text{MHz}", size=38).move_to([-3.5, 0.1, 0])
        self.add(rule_tex, rule_box, laser_col, atom_col, divider, l_given, spacing_tex)
        lam_given = ink_tex(r"\lambda = 632.8\;\text{nm}", size=36).move_to([-3.5, -1.0, 0])
        n_tex = red_tex(r"n = \frac{2L}{\lambda} \approx 9.5\times10^5", size=36
                        ).move_to([-3.5, -2.1, 0])
        self.play(Write(lam_given), run_time=0.5)
        self.play(Write(n_tex), run_time=d("W03", 6.46) * 0.75)
        self.wait(d("W03", 6.46) * 0.15)


# ── W04 ───────────────────────────────────────────────────────────────────────
class W04_AtomNumbers(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=40).move_to([0, 3.5, 0])
        rule_box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.15)
        laser_col = ink_txt("Laser cavity", size=28, color=ACCENT).move_to([-3.5, 2.5, 0])
        atom_col = ink_txt("Electron in box", size=28, color=ACCENT).move_to([3.5, 2.5, 0])
        divider = Line([0, 2.0, 0], [0, -3.5, 0], color=INK, stroke_width=1.0)
        # left column existing (dimmed)
        left_stuff = VGroup(
            ink_tex(r"L = 0.30\;\text{m}", size=34).move_to([-3.5, 1.3, 0]),
            red_tex(r"\Delta f \approx 500\;\text{MHz}", size=34).move_to([-3.5, 0.4, 0]),
            red_tex(r"n \approx 9.5\times10^5", size=30).move_to([-3.5, -0.4, 0]),
        ).set_opacity(0.5)
        self.add(rule_tex, rule_box, laser_col, atom_col, divider, left_stuff)
        l_box = ink_tex(r"L = 1\;\text{nm}", size=38).move_to([3.5, 1.3, 0])
        e1_tex = red_tex(r"E_1 \approx 0.38\;\text{eV}", size=40).move_to([3.5, 0.1, 0])
        e2_tex = red_tex(r"E_2 \approx 1.5\;\text{eV}", size=40).move_to([3.5, -1.1, 0])
        self.play(Write(l_box), run_time=0.5)
        self.play(Write(e1_tex), run_time=d("W04", 8.64) * 0.4)
        self.play(Write(e2_tex), run_time=d("W04", 8.64) * 0.35)
        self.wait(d("W04", 8.64) * 0.1)


# ── P01 ───────────────────────────────────────────────────────────────────────
class P01_Ladders(Scene):
    def construct(self):
        self.add(bg())
        headline = ink_txt("Widen the box → rungs crowd closer", size=32).move_to([0, 3.2, 0])

        def energy_ladder(cx, L_label, n_levels=5, gap=0.7, label_side=LEFT):
            grp = VGroup()
            for i in range(1, n_levels + 1):
                y = -2.0 + (i - 1) * gap
                rung = Line([cx - 0.8, y, 0], [cx + 0.8, y, 0],
                            color=ACCENT, stroke_width=3)
                lbl = ink_txt(f"n={i}", size=20).next_to(rung, label_side, buff=0.1)
                grp.add(rung, lbl)
            header = ink_txt(L_label, size=26).move_to([cx, -2.0 + n_levels * gap + 0.4, 0])
            grp.add(header)
            return grp

        # Small L → wide gaps
        ladder_s = energy_ladder(-4.0, "small L (atom)", gap=0.85)
        # Big L → tight gaps
        ladder_b = energy_ladder(3.5, "large L (laser)", gap=0.42, n_levels=8, label_side=RIGHT)

        self.play(Write(headline), run_time=0.5)
        self.play(Create(ladder_s), Create(ladder_b), run_time=d("P01", 4.71) * 0.85)
        self.wait(d("P01", 4.71) * 0.15)


# ── P02 ───────────────────────────────────────────────────────────────────────
class P02_Recap(Scene):
    def construct(self):
        self.add(bg())
        headline = ink_txt("Widen the box → rungs crowd closer", size=32).move_to([0, 3.2, 0])

        def energy_ladder(cx, L_label, n_levels=5, gap=0.7, label_side=LEFT):
            grp = VGroup()
            for i in range(1, n_levels + 1):
                y = -2.0 + (i - 1) * gap
                rung = Line([cx - 0.8, y, 0], [cx + 0.8, y, 0],
                            color=ACCENT, stroke_width=3)
                lbl = ink_txt(f"n={i}", size=20).next_to(rung, label_side, buff=0.1)
                grp.add(rung, lbl)
            header = ink_txt(L_label, size=26).move_to([cx, -2.0 + n_levels * gap + 0.4, 0])
            grp.add(header)
            return grp

        ladder_s = energy_ladder(-4.0, "small L (atom)", gap=0.85)
        ladder_b = energy_ladder(3.5, "large L (laser)", gap=0.42, n_levels=8, label_side=RIGHT)
        self.add(headline, ladder_s, ladder_b)
        recap = ink_txt("Same rule  ·  two scales  ·  one mechanism", size=30,
                        slant=ITALIC).move_to([0, -3.5, 0])
        self.play(Write(recap), run_time=d("P02", 4.82) * 0.85)
        self.wait(d("P02", 4.82) * 0.15)


# ── R01 ───────────────────────────────────────────────────────────────────────
class R01_BoxedRule(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=88)
        box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.5, stroke_width=4)
        tagline = ink_txt("One rule sets them both.", size=34).next_to(box, DOWN, buff=0.5)
        self.play(Write(rule_tex), Create(box), run_time=d("R01", 2.35) * 0.85)
        self.play(Write(tagline), run_time=0.4)
        self.wait(d("R01", 2.35) * 0.1)


# ── R02 ───────────────────────────────────────────────────────────────────────
class R02_OnlyFit(Scene):
    def construct(self):
        self.add(bg())
        rule_tex = accent_tex(r"\frac{n\lambda}{2} = L", size=72).move_to([0, 1.0, 0])
        box = SurroundingRectangle(rule_tex, color=ACCENT, buff=0.4, stroke_width=4)
        self.add(rule_tex, box)
        close = ink_txt("Only the waves that fit are allowed to exist.", size=34
                        ).move_to([0, -1.0, 0])
        self.play(Write(close), run_time=d("R02", 3.2) * 0.85)
        self.wait(d("R02", 3.2) * 0.15)


# ── OUTRO ─────────────────────────────────────────────────────────────────────
class OUTRO_Card(Scene):
    def construct(self):
        self.add(bg())
        series = ink_txt("Bear's Notes", size=36).move_to([0, 1.5, 0])
        title = ink_txt("Why an Atom and a Laser\nQuantize for the Same Reason",
                        size=36, line_spacing=1.3).move_to([0, 0.0, 0])
        channel = ink_txt("youtube.com/@NikBearBrown", size=26, color=ACCENT).move_to([0, -1.8, 0])
        thanks = ink_txt("Thanks for watching", size=32).move_to([0, -2.8, 0])
        self.play(Write(series), run_time=0.5)
        self.play(Write(title), Write(channel), run_time=d("OUTRO", 5.48) * 0.7)
        self.play(Write(thanks), run_time=0.5)
        self.wait(d("OUTRO", 5.48) * 0.1)
