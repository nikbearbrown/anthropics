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

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 6.35)
        series = ink_txt("Bear's Notes", size=52)
        title = ink_txt("Why Mixing Two Frozen Quantum States\nMakes Probability Slosh", size=34)
        title.next_to(series, DOWN, buff=0.5)
        accent = Line(LEFT * 5, RIGHT * 5, color=TERRA, stroke_width=3).next_to(series, DOWN, buff=0.15)
        self.play(FadeIn(series), run_time=1.0)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(title), run_time=1.5)
        self.wait(dur - 3.0)


class H01_StillCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 5.46)
        box = Rectangle(width=3.0, height=2.0, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 1)
        # single hump cloud (centred ellipse)
        cloud = Ellipse(width=1.8, height=0.7, color=SLATE, stroke_width=0).set_fill(SLATE, opacity=0.55)
        cloud.move_to(box.get_center())
        person = ink_txt("(you)", size=26, color=SLATE).next_to(box, LEFT, buff=0.5)
        still = ink_txt("perfectly still", size=24, color=INK).next_to(box, DOWN, buff=0.25)
        self.play(FadeIn(box), FadeIn(person), run_time=0.8)
        self.play(FadeIn(cloud), run_time=0.6)
        self.play(FadeIn(still), run_time=0.4)
        self.wait(dur - 1.8)


class H02_SloshingCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 4.49)
        box = Rectangle(width=3.5, height=2.0, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 1)
        cloud = Ellipse(width=1.6, height=0.7, color=SLATE, stroke_width=0).set_fill(SLATE, opacity=0.6)
        cloud.move_to(box.get_center() + LEFT * 0.8)
        person = ink_txt("(startled!)", size=24, color=TERRA).next_to(box, LEFT, buff=0.4)
        label = ink_txt("sloshes!", size=28, color=RED).next_to(box, DOWN, buff=0.25)
        self.play(FadeIn(box), FadeIn(person), run_time=0.7)
        self.play(FadeIn(cloud), run_time=0.4)
        self.play(
            cloud.animate.move_to(box.get_center() + RIGHT * 0.8),
            run_time=1.0, rate_func=there_and_back
        )
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 2.5)


class A01_DrawWell(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 2.09)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        label = ink_txt("particle in a box", size=26).next_to(well, UP, buff=0.3)
        self.play(Create(well), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.1)


class A02_GroundStateCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.91)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        # half-sine probability hump
        xs = np.linspace(-2.5, 2.5, 200)
        ys = -1.5 + 1.4 * np.sin(np.pi * (xs + 2.5) / 5.0) ** 2
        pts = [np.array([x, y, 0]) for x, y in zip(xs, ys)]
        cloud_curve = VMobject(color=SLATE, stroke_width=0)
        cloud_curve.set_points_as_corners(pts)
        filled = cloud_curve.copy().set_fill(SLATE, opacity=0.5).set_stroke(width=0)
        label = ink_txt("ground state\n|ψ|² — one hump, frozen", size=24, color=SLATE).shift(RIGHT * 3.5 + UP * 0.5)
        self.add(well)
        self.play(Create(cloud_curve), run_time=1.0)
        self.add(filled)
        self.remove(cloud_curve)
        self.play(FadeIn(label), run_time=0.6)
        self.wait(dur - 1.6)


class A03_FirstExcitedCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 4.08)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        xs = np.linspace(-2.5, 2.5, 200)
        ys = -1.5 + 1.4 * np.sin(2 * np.pi * (xs + 2.5) / 5.0) ** 2
        filled = VMobject(stroke_width=0).set_fill(TERRA, opacity=0.5)
        filled.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("first excited state\ntwo lobes, also frozen", size=24, color=TERRA).shift(RIGHT * 3.5 + UP * 0.5)
        self.add(well)
        self.play(FadeIn(filled), run_time=0.8)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.3)


class A04_TwoClocks(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 5.33)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        # frozen ground state cloud
        xs = np.linspace(-2.5, 2.5, 200)
        ys_gs = -1.5 + 1.4 * np.sin(np.pi * (xs + 2.5) / 5.0) ** 2
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.5)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys_gs)])
        # argand inset: two hands
        circle = Circle(radius=0.7, color=INK, stroke_width=2).shift(RIGHT * 5 + UP * 0.5)
        hand1 = Line(circle.get_center(), circle.get_center() + UP * 0.6, color=INK, stroke_width=3)
        hand2 = Line(circle.get_center(), circle.get_center() + RIGHT * 0.6, color=TERRA, stroke_width=3)
        inset_label = ink_txt("ω₁   ω₂", size=22, color=INK).next_to(circle, DOWN, buff=0.15)
        self.add(well, cloud)
        self.play(Create(circle), run_time=0.5)
        self.play(GrowFromPoint(hand1, circle.get_center()),
                  GrowFromPoint(hand2, circle.get_center()), run_time=0.5)
        self.play(FadeIn(inset_label), run_time=0.4)
        self.play(
            Rotate(hand1, angle=TAU * 0.5, about_point=circle.get_center()),
            Rotate(hand2, angle=TAU * 1.2, about_point=circle.get_center()),
            run_time=dur - 1.4,
        )


class A05_CombinedCloudStill(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 3.29)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        xs = np.linspace(-2.5, 2.5, 200)
        # combined superposition |ψ|² at t=0 (both phases zero)
        psi = np.sin(np.pi * (xs + 2.5) / 5.0) + np.sin(2 * np.pi * (xs + 2.5) / 5.0)
        ys = -1.5 + 0.8 * psi ** 2 / (np.max(psi ** 2) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("combined cloud", size=26, color=SLATE).shift(RIGHT * 4.5 + UP * 0.5)
        self.add(well)
        self.play(FadeIn(cloud), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.1)


class A06_SloshingCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 5.98)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        # animated sloshing via ValueTracker
        t_val = ValueTracker(0)
        xs = np.linspace(-2.5, 2.5, 200)
        L = 5.0
        omega_diff = 2.0  # beat frequency for animation

        def make_cloud(t):
            phi2 = omega_diff * t
            psi = (np.sin(np.pi * (xs + 2.5) / L) +
                   np.sin(2 * np.pi * (xs + 2.5) / L) * np.cos(phi2))
            ys = -1.5 + 0.9 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
            mob = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
            mob.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
            return mob

        cloud = make_cloud(0)

        def updater(m):
            t = t_val.get_value()
            new_cloud = make_cloud(t)
            m.become(new_cloud)

        cloud.add_updater(updater)
        self.add(well, cloud)
        self.play(t_val.animate.set_value(TAU), run_time=dur - 0.3, rate_func=linear)
        self.wait(0.3)


class A07_HighlightAngleGap(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 5.04)
        # Well with sloshing cloud (simplified static)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        # clock inset showing angle gap
        circle = Circle(radius=0.8, color=INK, stroke_width=2).shift(RIGHT * 5)
        hand1 = Line(circle.get_center(), circle.get_center() + UP * 0.7, color=INK, stroke_width=3)
        hand2 = Line(circle.get_center(), circle.get_center() + RIGHT * 0.55 + DOWN * 0.45,
                     color=TERRA, stroke_width=3)
        angle_arc = Arc(radius=0.4, start_angle=PI / 2, angle=-PI / 4,
                        color=RED, stroke_width=3).shift(circle.get_center())
        gap_label = ink_txt("energy gap\ndrives beat", size=22, color=RED).next_to(circle, DOWN, buff=0.2)
        # sloshed cloud left
        xs = np.linspace(-2.5, 2.5, 200)
        L = 5.0
        phi = PI * 0.6
        psi = (np.sin(np.pi * (xs + 2.5) / L) +
               np.sin(2 * np.pi * (xs + 2.5) / L) * np.cos(phi))
        ys = -1.5 + 0.9 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        self.add(well, cloud)
        self.play(Create(circle), GrowFromPoint(hand1, circle.get_center()),
                  GrowFromPoint(hand2, circle.get_center()), run_time=0.8)
        self.play(Create(angle_arc), FadeIn(gap_label), run_time=0.6)
        self.wait(dur - 1.4)


class A08_FrozenStatesMixMoves(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.62)
        left_wall = Line(DOWN * 1.5 + LEFT * 2.5, UP * 1.5 + LEFT * 2.5, color=INK, stroke_width=4)
        right_wall = Line(DOWN * 1.5 + RIGHT * 2.5, UP * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        floor = Line(DOWN * 1.5 + LEFT * 2.5, DOWN * 1.5 + RIGHT * 2.5, color=INK, stroke_width=4)
        well = VGroup(left_wall, right_wall, floor)
        xs = np.linspace(-2.5, 2.5, 200)
        L = 5.0
        phi = PI * 1.1
        psi = (np.sin(np.pi * (xs + 2.5) / L) +
               np.sin(2 * np.pi * (xs + 2.5) / L) * np.cos(phi))
        ys = -1.5 + 0.9 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.6)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("two frozen states,\nand the mix moves", size=30, color=RED).shift(RIGHT * 4 + UP * 0.6)
        self.add(well, cloud)
        self.play(FadeIn(label), run_time=0.8)
        self.wait(dur - 0.8)
