"""
Portrait (9:16) Manim scenes for the Short.
Derived from the parent reel's scenes.py — layout reflowed for 1080x1920.
Run via:
  manim -qk short/scenes.py H01_StillCloud --output_file H01.mp4
  (remotion_scenes.py does NOT invoke this; run.sh or art run does)
"""
import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED   = "#C0392B"
FONT  = "EB Garamond"

# Portrait frame dimensions (Manim units)
FW, FH = 9.0, 16.0

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
except Exception:
    DUR = {}

def d(bid, default=5.0):
    return DUR.get(bid, default)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class PortraitConfig(Scene):
    """Base class: sets the camera to 9:16 portrait."""
    def setup(self):
        self.camera.frame_width  = FW
        self.camera.frame_height = FH
        self.camera.background_color = CREAM


class H01_StillCloud(PortraitConfig):
    def construct(self):
        dur = d("H01", 5.65)
        box   = Rectangle(width=4.0, height=2.5, color=INK, stroke_width=3
                          ).set_fill(CREAM, 1).shift(UP * 1.5)
        cloud = Ellipse(width=2.4, height=0.9, color=SLATE, stroke_width=0
                        ).set_fill(SLATE, opacity=0.55).move_to(box.get_center())
        person = ink_txt("(you)", size=32, color=SLATE).next_to(box, DOWN, buff=0.4)
        still  = ink_txt("perfectly still", size=28, color=INK).next_to(person, DOWN, buff=0.3)
        self.play(FadeIn(box), FadeIn(person), run_time=0.8)
        self.play(FadeIn(cloud), run_time=0.6)
        self.play(FadeIn(still), run_time=0.4)
        self.wait(dur - 1.8)


class H02_SloshingCloud(PortraitConfig):
    def construct(self):
        dur = d("H02", 4.74)
        box   = Rectangle(width=4.5, height=2.5, color=INK, stroke_width=3
                          ).set_fill(CREAM, 1).shift(UP * 1.5)
        cloud = Ellipse(width=2.0, height=0.9, color=SLATE, stroke_width=0
                        ).set_fill(SLATE, opacity=0.6
                        ).move_to(box.get_center() + LEFT * 0.9)
        person = ink_txt("(startled!)", size=30, color=TERRA).next_to(box, DOWN, buff=0.4)
        label  = ink_txt("sloshes!", size=34, color=RED).next_to(person, DOWN, buff=0.3)
        self.play(FadeIn(box), FadeIn(person), run_time=0.7)
        self.play(FadeIn(cloud), run_time=0.4)
        self.play(
            cloud.animate.move_to(box.get_center() + RIGHT * 0.9),
            run_time=1.0, rate_func=there_and_back
        )
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 2.5)


class A01_DrawWell(PortraitConfig):
    def construct(self):
        dur   = d("A01", 2.6)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        label = ink_txt("particle in a box", size=34).next_to(well, UP, buff=0.5)
        self.play(Create(well), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.1)


class A02_GroundStateCloud(PortraitConfig):
    def construct(self):
        dur   = d("A02", 5.03)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        xs = np.linspace(-2.0, 2.0, 200)
        ys = -2.0 + 1.6 * np.sin(np.pi * (xs + 2.0) / 4.0) ** 2
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.5)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("ground state\n|ψ|² — one hump,\nfrozen", size=30, color=SLATE
                        ).next_to(well, UP, buff=0.4)
        self.add(well)
        self.play(Create(cloud), run_time=1.0)
        self.play(FadeIn(label), run_time=0.6)
        self.wait(dur - 1.6)


class A03_FirstExcitedCloud(PortraitConfig):
    def construct(self):
        dur   = d("A03", 4.44)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        xs = np.linspace(-2.0, 2.0, 200)
        ys = -2.0 + 1.6 * np.sin(2 * np.pi * (xs + 2.0) / 4.0) ** 2
        filled = VMobject(stroke_width=0).set_fill(TERRA, opacity=0.5)
        filled.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("first excited state\ntwo lobes,\nalso frozen", size=30, color=TERRA
                        ).next_to(well, UP, buff=0.4)
        self.add(well)
        self.play(FadeIn(filled), run_time=0.8)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.3)


class A04_TwoClocks(PortraitConfig):
    def construct(self):
        dur   = d("A04", 5.16)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        xs    = np.linspace(-2.0, 2.0, 200)
        ys_gs = -2.0 + 1.6 * np.sin(np.pi * (xs + 2.0) / 4.0) ** 2
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.5)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys_gs)])
        # Argand inset: two hands — placed above the well
        circle = Circle(radius=1.0, color=INK, stroke_width=2).shift(UP * 5.0)
        hand1  = Line(circle.get_center(), circle.get_center() + UP * 0.85, color=INK, stroke_width=3)
        hand2  = Line(circle.get_center(), circle.get_center() + RIGHT * 0.85, color=TERRA, stroke_width=3)
        inset_label = ink_txt("ω₁   ω₂", size=28, color=INK).next_to(circle, DOWN, buff=0.2)
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


class A05_CombinedCloudStill(PortraitConfig):
    def construct(self):
        dur   = d("A05", 3.92)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        xs  = np.linspace(-2.0, 2.0, 200)
        psi = np.sin(np.pi * (xs + 2.0) / 4.0) + np.sin(2 * np.pi * (xs + 2.0) / 4.0)
        ys  = -2.0 + 0.9 * psi ** 2 / (np.max(psi ** 2) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("combined cloud", size=32, color=SLATE).next_to(well, UP, buff=0.4)
        self.add(well)
        self.play(FadeIn(cloud), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.1)


class A06_SloshingCloud(PortraitConfig):
    def construct(self):
        dur   = d("A06", 5.88)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well   = VGroup(lwall, rwall, floor)
        xs     = np.linspace(-2.0, 2.0, 200)
        L      = 4.0
        omega_diff = 2.0
        t_val  = ValueTracker(0)

        def make_cloud(t):
            phi2 = omega_diff * t
            psi  = (np.sin(np.pi * (xs + 2.0) / L) +
                    np.sin(2 * np.pi * (xs + 2.0) / L) * np.cos(phi2))
            ys   = -2.0 + 1.0 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
            mob  = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
            mob.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
            return mob

        cloud = make_cloud(0)
        cloud.add_updater(lambda m: m.become(make_cloud(t_val.get_value())))
        self.add(well, cloud)
        self.play(t_val.animate.set_value(TAU), run_time=dur - 0.3, rate_func=linear)
        self.wait(0.3)


class A07_HighlightAngleGap(PortraitConfig):
    def construct(self):
        dur   = d("A07", 4.92)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        # clock inset above the well
        circle    = Circle(radius=1.1, color=INK, stroke_width=2).shift(UP * 5.0)
        hand1     = Line(circle.get_center(), circle.get_center() + UP * 0.95, color=INK, stroke_width=3)
        hand2     = Line(circle.get_center(),
                         circle.get_center() + RIGHT * 0.75 + DOWN * 0.65, color=TERRA, stroke_width=3)
        angle_arc = Arc(radius=0.55, start_angle=PI / 2, angle=-PI / 4,
                        color=RED, stroke_width=3).shift(circle.get_center())
        gap_label = ink_txt("energy gap\ndrives beat", size=26, color=RED
                            ).next_to(circle, DOWN, buff=0.25)
        # sloshed cloud
        xs  = np.linspace(-2.0, 2.0, 200)
        L   = 4.0
        phi = PI * 0.6
        psi = (np.sin(np.pi * (xs + 2.0) / L) +
               np.sin(2 * np.pi * (xs + 2.0) / L) * np.cos(phi))
        ys  = -2.0 + 1.0 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.55)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        self.add(well, cloud)
        self.play(Create(circle),
                  GrowFromPoint(hand1, circle.get_center()),
                  GrowFromPoint(hand2, circle.get_center()), run_time=0.8)
        self.play(Create(angle_arc), FadeIn(gap_label), run_time=0.6)
        self.wait(dur - 1.4)


class A08_FrozenStatesMixMoves(PortraitConfig):
    def construct(self):
        dur   = d("A08", 4.54)
        lwall = Line(DOWN * 2.0 + LEFT * 2.0, UP * 2.0 + LEFT * 2.0, color=INK, stroke_width=4)
        rwall = Line(DOWN * 2.0 + RIGHT * 2.0, UP * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        floor = Line(DOWN * 2.0 + LEFT * 2.0, DOWN * 2.0 + RIGHT * 2.0, color=INK, stroke_width=4)
        well  = VGroup(lwall, rwall, floor)
        xs  = np.linspace(-2.0, 2.0, 200)
        L   = 4.0
        phi = PI * 1.1
        psi = (np.sin(np.pi * (xs + 2.0) / L) +
               np.sin(2 * np.pi * (xs + 2.0) / L) * np.cos(phi))
        ys  = -2.0 + 1.0 * psi ** 2 / (np.max(np.abs(psi ** 2)) + 0.01)
        cloud = VMobject(stroke_width=0).set_fill(SLATE, opacity=0.6)
        cloud.set_points_as_corners([np.array([x, y, 0]) for x, y in zip(xs, ys)])
        label = ink_txt("two frozen states,\nand the mix moves", size=36, color=RED
                        ).next_to(well, UP, buff=0.4)
        self.add(well, cloud)
        self.play(FadeIn(label), run_time=0.8)
        self.wait(dur - 0.8)
