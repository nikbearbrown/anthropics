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


def atomic_surface(y=-1.8, n=8, amp=0.22, spacing=0.7):
    """Returns a VMobject representing a bumpy atomic surface."""
    xs = [i * spacing - n * spacing / 2 for i in range(n)]
    bumps = VGroup(*[
        Circle(radius=amp, color=INK, stroke_width=0).set_fill(INK, opacity=0.18).move_to([x, y + amp, 0])
        for x in xs
    ])
    return bumps


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 5.28)
        series = ink_txt("Bear's Notes", size=52)
        title = ink_txt("Why One Extra Atom of Distance\nCuts a Tunneling Current Tenfold", size=36)
        title.next_to(series, DOWN, buff=0.5)
        accent = Line(LEFT * 5, RIGHT * 5, color=TERRA, stroke_width=3).next_to(series, DOWN, buff=0.15)
        self.play(FadeIn(series), run_time=1.0)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(title), run_time=1.5)
        self.wait(dur - 3.0)


class H01_TipAndAtom(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 3.71)
        surface = atomic_surface()
        tip_body = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5)
        tip_body.rotate(PI).shift(UP * 1.6)
        person = ink_txt("(amazed!)", size=26, color=TERRA).shift(LEFT * 4.5 + UP * 0.5)
        label = ink_txt("single atom\ndetected", size=24, color=SLATE).shift(RIGHT * 4 + UP * 0.5)
        self.play(FadeIn(surface), FadeIn(tip_body), run_time=0.8)
        self.play(FadeIn(person), FadeIn(label), run_time=0.6)
        self.wait(dur - 1.4)


class H02_TipLifts(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 4.62)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.6)
        # meter
        meter_circle = Circle(radius=0.7, color=INK, stroke_width=2).shift(RIGHT * 4.5 + UP * 0.5)
        needle = Line(meter_circle.get_center(),
                      meter_circle.get_center() + UP * 0.6, color=SLATE, stroke_width=3)
        meter_label = ink_txt("I", size=28).next_to(meter_circle, DOWN, buff=0.1)
        self.add(surface, tip, meter_circle, needle, meter_label)
        self.play(
            tip.animate.shift(UP * 0.7),
            Rotate(needle, angle=-PI * 0.7, about_point=meter_circle.get_center()),
            run_time=1.2,
        )
        drop = ink_txt("÷ 10", size=36, color=RED).next_to(meter_circle, RIGHT, buff=0.3)
        self.play(FadeIn(drop), run_time=0.5)
        self.wait(dur - 1.7)


class A01_TipAboveSurface(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.76)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.2)
        gap_brace = BraceBetweenPoints(
            UP * 0.35, DOWN * 0.18, direction=RIGHT, color=TERRA
        )
        gap_label = ink_txt("gap d", size=24, color=TERRA).next_to(gap_brace, RIGHT, buff=0.1)
        self.play(FadeIn(surface), FadeIn(tip), run_time=0.8)
        self.play(Create(gap_brace), FadeIn(gap_label), run_time=0.6)
        self.wait(dur - 1.4)


class A02_TunnelLink(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 3.47)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.2)
        tunnel_link = DashedLine(DOWN * 0.1, UP * 0.35, color=SLATE, stroke_width=4,
                                  dash_length=0.1).shift(LEFT * 0.05)
        # gauge
        gauge_circ = Circle(radius=0.6, color=INK, stroke_width=2).shift(RIGHT * 4 + UP * 0.8)
        needle = Line(gauge_circ.get_center(),
                      gauge_circ.get_center() + UP * 0.5, color=SLATE, stroke_width=3)
        gauge_label = ink_txt("I", size=26).next_to(gauge_circ, DOWN, buff=0.1)
        self.add(surface, tip)
        self.play(Create(tunnel_link), run_time=0.6)
        self.play(Create(gauge_circ), GrowFromPoint(needle, gauge_circ.get_center()),
                  FadeIn(gauge_label), run_time=0.7)
        self.wait(dur - 1.3)


class A03_ExponentialLadder(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 6.27)
        steps = [
            ("d",   "I = 1"),
            ("2d",  "I = 1/10"),
            ("3d",  "I = 1/100"),
        ]
        rows = VGroup()
        for i, (gap, curr) in enumerate(steps):
            g = ink_txt(f"gap = {gap}", size=30).shift(LEFT * 2 + DOWN * i * 1.1)
            arrow = Arrow(LEFT * 0.3, RIGHT * 0.3, color=INK, stroke_width=3, buff=0)
            arrow.next_to(g, RIGHT, buff=0.2)
            c = ink_txt(curr, size=30, color=SLATE).next_to(arrow, RIGHT, buff=0.2)
            rows.add(VGroup(g, arrow, c))
        rows.move_to(ORIGIN)
        title = ink_txt("equal distance steps:", size=28, color=INK).next_to(rows, UP, buff=0.4)
        for row in rows:
            self.play(FadeIn(row), run_time=0.7)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(dur - len(rows) * 0.7 - 0.5)


class A04_TipTracing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.16)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI)
        tip.shift(UP * 1.2 + LEFT * 2.8)
        gauge_circ = Circle(radius=0.6, color=INK, stroke_width=2).shift(RIGHT * 5.5 + UP * 0.8)
        needle = Line(gauge_circ.get_center(),
                      gauge_circ.get_center() + UP * 0.5, color=SLATE, stroke_width=3)
        self.add(surface, gauge_circ, needle)
        self.play(FadeIn(tip), run_time=0.4)
        self.play(tip.animate.shift(RIGHT * 5.6), run_time=dur - 0.4, rate_func=linear)


class A05_NeedleSwings(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.62)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.2)
        gauge_circ = Circle(radius=0.6, color=INK, stroke_width=2).shift(RIGHT * 5 + UP * 0.8)
        needle = Line(gauge_circ.get_center(),
                      gauge_circ.get_center() + UP * 0.5, color=SLATE, stroke_width=3)
        self.add(surface, tip, gauge_circ, needle)
        # needle swings high then low
        self.play(Rotate(needle, angle=PI * 0.5, about_point=gauge_circ.get_center()), run_time=0.7)
        self.play(Rotate(needle, angle=-PI * 0.8, about_point=gauge_circ.get_center()), run_time=0.7)
        self.play(Rotate(needle, angle=PI * 0.6, about_point=gauge_circ.get_center()), run_time=0.7)
        self.play(Rotate(needle, angle=-PI * 0.4, about_point=gauge_circ.get_center()), run_time=0.6)
        self.wait(dur - 2.7)


class A06_TinyHeightBigSwing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 4.91)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.2 + LEFT * 0.35)
        # small bracket on tip height
        height_brace = BraceBetweenPoints(DOWN * 0.12, UP * 0.3, direction=LEFT, color=INK)
        height_label = ink_txt("~1 Å", size=22, color=INK).next_to(height_brace, LEFT, buff=0.1)
        gauge_circ = Circle(radius=0.8, color=INK, stroke_width=2).shift(RIGHT * 4.5 + UP * 0.5)
        needle = Line(gauge_circ.get_center(),
                      gauge_circ.get_center() + UP * 0.7, color=SLATE, stroke_width=3)
        swing = ink_txt("× 10 swing!", size=32, color=RED).next_to(gauge_circ, DOWN, buff=0.2)
        self.add(surface, tip)
        self.play(Create(height_brace), FadeIn(height_label), run_time=0.6)
        self.play(Create(gauge_circ), GrowFromPoint(needle, gauge_circ.get_center()), run_time=0.5)
        self.play(Rotate(needle, angle=-PI * 0.8, about_point=gauge_circ.get_center()), run_time=0.7)
        self.play(FadeIn(swing), run_time=0.5)
        self.wait(dur - 2.3)


class A07_CurrentPeaksMapAtoms(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 4.78)
        surface = atomic_surface()
        # current trace peaks over atoms
        n = 8; spacing = 0.7
        xs = [(i - n // 2) * spacing for i in range(n)]
        profile_pts = []
        for x in xs:
            profile_pts.append(np.array([x, 0.0, 0]))
            profile_pts.append(np.array([x, 0.8, 0]))
            profile_pts.append(np.array([x + spacing * 0.45, 0.0, 0]))
        profile = VMobject(color=INK, stroke_width=3)
        profile.set_points_smoothly(profile_pts)
        label = ink_txt("current peaks = atom positions", size=42).shift(DOWN * 2.5)
        self.add(surface)
        self.play(Create(profile), run_time=1.2)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.7)


class A08_OneAtomCloserTenTimes(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.31)
        surface = atomic_surface()
        tip = Triangle(color=INK, stroke_width=3, fill_opacity=0.15).scale(0.5).rotate(PI).shift(UP * 1.2)
        label = ink_txt("one atom closer,\nten times the current", size=50)
        label.shift(DOWN * 2.8)
        self.add(surface, tip)
        self.play(FadeIn(label), run_time=0.8)
        self.wait(dur - 0.8)
