import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED = "#C0392B"
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

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


def make_well(L=2.5, floor_y=-1.8, wall_h=2.8):
    lw = Line([- L, floor_y, 0], [-L, floor_y + wall_h, 0], color=INK, stroke_width=5)
    rw = Line([L, floor_y, 0], [L, floor_y + wall_h, 0], color=INK, stroke_width=5)
    fl = Line([-L, floor_y, 0], [L, floor_y, 0], color=INK, stroke_width=5)
    return VGroup(lw, rw, fl), L, floor_y


def half_sine_arch(L=2.5, floor_y=-1.8, amp=1.4, color=SLATE, n=200):
    xs = np.linspace(-L, L, n)
    ys = floor_y + amp * np.sin(np.pi * (xs + L) / (2 * L)) ** 2
    pts = [np.array([x, y, 0]) for x, y in zip(xs, ys)]
    mob = VMobject(stroke_width=0).set_fill(color, opacity=0.55)
    mob.set_points_as_corners(pts)
    return mob


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 3.89)
        series = ink_txt("Bear's Notes", size=52)
        title = ink_txt("Why a Particle in a Box\nCannot Sit Still", size=40)
        title.next_to(series, DOWN, buff=0.5)
        accent = Line(LEFT * 5, RIGHT * 5, color=TERRA, stroke_width=3).next_to(series, DOWN, buff=0.15)
        self.play(FadeIn(series), run_time=0.8)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(title), run_time=1.2)
        self.wait(dur - 2.4)


class H01_MarbleInBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 4.55)
        box = Square(side_length=2.5, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 0.5)
        marble = Circle(radius=0.25, color=INK, stroke_width=2).set_fill(INK, opacity=0.5)
        marble.move_to(box.get_bottom() + UP * 0.28)
        still_label = ink_txt("perfectly still", size=26, color=INK).next_to(box, DOWN, buff=0.25)
        person = ink_txt("(classic)", size=24, color=SLATE).next_to(box, LEFT, buff=0.5)
        self.play(FadeIn(box), FadeIn(person), run_time=0.6)
        self.play(marble.animate.move_to(box.get_center() + DOWN * 0.8), run_time=0.7)
        self.play(FadeIn(still_label), run_time=0.4)
        self.wait(dur - 1.7)


class H02_JitteringParticle(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 4.08)
        box = Square(side_length=2.5, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 0.5)
        particle = Circle(radius=0.2, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.7)
        particle.move_to(box.get_center() + DOWN * 0.5)
        person = ink_txt("(puzzled)", size=24, color=RED).next_to(box, LEFT, buff=0.4)
        label = ink_txt("refuses to sit still!", size=26, color=RED).next_to(box, DOWN, buff=0.25)
        self.play(FadeIn(box), FadeIn(person), run_time=0.6)
        self.play(FadeIn(particle), run_time=0.3)
        # jitter
        for _ in range(4):
            offset = np.array([np.random.uniform(-0.5, 0.5),
                                np.random.uniform(-0.5, 0.5), 0])
            self.play(particle.animate.move_to(box.get_center() + offset),
                      run_time=0.25, rate_func=linear)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 2.3)


class A01_WallsZeroCondition(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 4.73)
        well, L, fy = make_well()
        # zero markers at base of each wall
        dot_l = Dot(point=[-L, fy, 0], color=RED, radius=0.1)
        dot_r = Dot(point=[L, fy, 0], color=RED, radius=0.1)
        zero_l = ink_txt("ψ = 0", size=22, color=RED).next_to(dot_l, LEFT, buff=0.15)
        zero_r = ink_txt("ψ = 0", size=22, color=RED).next_to(dot_r, RIGHT, buff=0.15)
        title = ink_txt("wave must vanish at each wall", size=26, color=INK).shift(UP * 2.8)
        self.play(Create(well), run_time=0.8)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.4)
        self.play(FadeIn(zero_l), FadeIn(zero_r), run_time=0.4)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(dur - 2.0)


class A02_FlatLineFails(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.55)
        well, L, fy = make_well()
        flat = Line([-L, fy, 0], [L, fy, 0], color=RED, stroke_width=5)
        explanation = ink_txt("flat = zero everywhere\n= no particle", size=26, color=RED).shift(RIGHT * 3.5 + UP * 0.8)
        self.add(well)
        self.play(Create(flat), run_time=0.6)
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(FadeOut(flat), run_time=0.8)
        self.wait(dur - 1.9)


class A03_HalfSineArch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 5.38)
        well, L, fy = make_well()
        arch = half_sine_arch(L=L, floor_y=fy, color=SLATE)
        label = ink_txt("smallest wave\nthat fits: n=1", size=26, color=SLATE).shift(RIGHT * 4 + UP * 0.5)
        self.add(well)
        self.play(FadeIn(arch), run_time=1.2)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.7)


class A04_CurvatureEnergy(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 4.86)
        well, L, fy = make_well()
        arch = half_sine_arch(L=L, floor_y=fy, color=SLATE)
        # curvature glyph at peak
        peak_y = fy + 1.4
        curv_mark = Arc(radius=0.6, start_angle=PI, angle=-PI, color=TERRA, stroke_width=3).move_to([0, peak_y, 0])
        curv_label = ink_txt("curvature", size=24, color=TERRA).next_to(curv_mark, UP, buff=0.15)
        energy_label = ink_txt("= kinetic\nenergy E₁", size=24, color=TERRA).next_to(curv_mark, RIGHT, buff=0.5)
        self.add(well, arch)
        self.play(Create(curv_mark), FadeIn(curv_label), run_time=0.7)
        self.play(FadeIn(energy_label), run_time=0.5)
        self.wait(dur - 1.2)


class A05_CannotFlatten(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.91)
        well, L, fy = make_well()
        arch = half_sine_arch(L=L, floor_y=fy, amp=1.4, color=SLATE)
        arch_flat = half_sine_arch(L=L, floor_y=fy, amp=0.3, color=SLATE)
        label = ink_txt("walls forbid going flat", size=28, color=RED).shift(DOWN * 2.8)
        self.add(well, arch)
        self.play(FadeIn(label), run_time=0.4)
        self.play(arch.animate.become(arch_flat), run_time=0.8)
        self.play(arch.animate.become(half_sine_arch(L=L, floor_y=fy, amp=1.4, color=SLATE)),
                  run_time=0.8)
        self.wait(dur - 2.0)


class A06_GroundStateEnergy(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 4.73)
        well, L, fy = make_well()
        arch = half_sine_arch(L=L, floor_y=fy, color=SLATE)
        e_level_y = fy + 1.4
        e_line = DashedLine([-L + 0.1, e_level_y, 0], [L - 0.1, e_level_y, 0],
                             color=TERRA, stroke_width=3, dash_length=0.2)
        e_label = ink_txt("E₁ > 0\n(ground state)", size=26, color=TERRA).next_to(e_line, RIGHT, buff=0.15)
        floor_label = ink_txt("E = 0 ←", size=22, color=RED).shift(RIGHT * 3.5 + DOWN * 1.7)
        self.add(well, arch)
        self.play(Create(e_line), run_time=0.7)
        self.play(FadeIn(e_label), FadeIn(floor_label), run_time=0.5)
        self.wait(dur - 1.2)


class A07_SqueezedBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 4.83)
        well_wide, L_wide, fy = make_well(L=2.5)
        arch_wide = half_sine_arch(L=L_wide, floor_y=fy, amp=1.4, color=SLATE)
        # narrow version
        L_narrow = 1.4
        well_narrow, _, _ = make_well(L=L_narrow)
        arch_narrow = half_sine_arch(L=L_narrow, floor_y=fy, amp=1.8, color=SLATE)
        e_narrow = fy + 1.8
        e_line = DashedLine([-L_narrow + 0.1, e_narrow, 0], [L_narrow - 0.1, e_narrow, 0],
                             color=TERRA, stroke_width=3, dash_length=0.2)
        e_label = ink_txt("E₁ rises!", size=26, color=TERRA).next_to(e_line, RIGHT, buff=0.15)
        self.add(well_wide, arch_wide)
        self.play(
            well_wide.animate.become(well_narrow),
            arch_wide.animate.become(arch_narrow),
            run_time=1.2,
        )
        self.play(Create(e_line), FadeIn(e_label), run_time=0.6)
        self.wait(dur - 1.8)


class A08_GroundStateLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.91)
        L = 1.6; fy = -1.8
        well, _, _ = make_well(L=L)
        arch = half_sine_arch(L=L, floor_y=fy, amp=1.8, color=SLATE)
        e_y = fy + 1.8
        e_line = DashedLine([-L + 0.1, e_y, 0], [L - 0.1, e_y, 0],
                             color=TERRA, stroke_width=3, dash_length=0.2)
        label = ink_txt("E₁  ground state\n(never zero)", size=30, color=TERRA).shift(RIGHT * 3.8 + UP * 0.5)
        arrow = Arrow(label.get_left(), e_line.get_right() + LEFT * 0.2, color=TERRA, stroke_width=2,
                      buff=0.1, max_tip_length_to_length_ratio=0.3)
        self.add(well, arch, e_line)
        self.play(FadeIn(label), GrowArrow(arrow), run_time=0.8)
        self.wait(dur - 0.8)
