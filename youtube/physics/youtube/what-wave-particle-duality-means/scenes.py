import json
from pathlib import Path
from manim import *
import numpy as np

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED_COL = "#C0392B"
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


# INTRO has render=none — skip

class A00_SingleCleanPath(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 2.77)
        ground = Line(LEFT * 4.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5, color=INK, stroke_width=3)
        path = Line(LEFT * 3.5 + DOWN * 1.5, RIGHT * 3.0 + DOWN * 1.5, color=SLATE, stroke_width=5)
        endpoint = Dot(radius=0.2, color=INK).shift(RIGHT * 3.0 + DOWN * 1.5)
        label = ink_txt("big objects:\none clean story", size=26)
        label.shift(UP * 1.5)

        self.play(Create(ground), run_time=dur * 0.2)
        self.play(Create(path), FadeIn(endpoint), run_time=dur * 0.5)
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A01_MarbleOnTrack(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 2.87)
        ground = Line(LEFT * 4.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5, color=INK, stroke_width=3)
        path = Line(LEFT * 3.5 + DOWN * 1.5, RIGHT * 3.0 + DOWN * 1.5, color=SLATE, stroke_width=5)
        endpoint = Dot(radius=0.2, color=INK).shift(RIGHT * 3.0 + DOWN * 1.5)
        self.add(ground, path, endpoint)

        marble = Circle(radius=0.3, color=INK, fill_opacity=0.75).shift(LEFT * 3.5 + DOWN * 1.2)
        m_label = ink_txt("marble", size=22).next_to(marble, UP, buff=0.15)
        stop_label = ink_txt("one stop", size=22, color=TERRA).next_to(endpoint, UP, buff=0.15)

        self.play(FadeIn(marble), Write(m_label), run_time=dur * 0.45)
        self.play(Write(stop_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A02_RippleStory(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 2.46)
        source = Dot(radius=0.15, color=SLATE).shift(ORIGIN)
        ring = Circle(radius=0.8, color=SLATE, stroke_width=3).shift(ORIGIN)
        label = ink_txt("a ripple:\nthe opposite story", size=26)
        label.shift(UP * 2.5)

        self.play(FadeIn(source), run_time=dur * 0.2)
        self.play(Create(ring), Write(label), run_time=dur * 0.6)
        self.wait(dur * 0.2)


class A03_ManyRippleRings(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.16)
        source = Dot(radius=0.15, color=SLATE).shift(ORIGIN)
        self.add(source)

        rings = VGroup(*[
            Circle(radius=0.8 * (i + 1), color=SLATE, stroke_width=3 - i * 0.4, stroke_opacity=0.9 - i * 0.2)
            for i in range(4)
        ])
        label = ink_txt("spreads everywhere\nat once", size=26)
        label.shift(UP * 3.0)

        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.2), run_time=dur * 0.65)
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.1)


class A04_ElectronMixesBoth(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.11)
        track_label = ink_txt("one track", size=24).shift(LEFT * 3.0 + UP * 1.0)
        spread_label = ink_txt("spread out", size=24).shift(RIGHT * 3.0 + UP * 1.0)

        electron = Dot(radius=0.3, color=SLATE).shift(ORIGIN)
        e_label = ink_txt("electron", size=26, color=SLATE).next_to(electron, DOWN, buff=0.2)

        arrow_l = Arrow(electron.get_left(), track_label.get_bottom(), color=SLATE, buff=0.1)
        arrow_r = Arrow(electron.get_right(), spread_label.get_bottom(), color=SLATE, buff=0.1)

        title = ink_txt("mixes BOTH", size=30, color=TERRA).shift(DOWN * 2.0)

        self.play(Write(track_label), Write(spread_label), run_time=dur * 0.3)
        self.play(FadeIn(electron), Write(e_label), run_time=dur * 0.25)
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=dur * 0.25)
        self.play(Write(title), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A05_SpreadingProbWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 3.79)
        electron = Dot(radius=0.25, color=SLATE).shift(LEFT * 3.0)
        self.add(electron)

        rings = VGroup(*[
            Circle(radius=0.7 * (i + 1), color=SLATE, stroke_width=2, stroke_opacity=0.8 - i * 0.15)
            .shift(LEFT * 3.0)
            for i in range(4)
        ])
        label = ink_txt("probability wave\n(before detection)", size=24, color=SLATE)
        label.shift(RIGHT * 1.5 + UP * 2.5)

        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.2), run_time=dur * 0.6)
        self.play(Write(label), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A06_NotSmeared(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 3.16)
        electron = Dot(radius=0.25, color=SLATE).shift(LEFT * 3.0)
        rings = VGroup(*[
            Circle(radius=0.7 * (i + 1), color=SLATE, stroke_width=2, stroke_opacity=0.7)
            .shift(LEFT * 3.0)
            for i in range(4)
        ])
        self.add(electron, rings)

        warning = ink_txt("NOT smeared\nelectron-stuff!", size=26, color=RED_COL)
        warning.shift(RIGHT * 1.5 + UP * 1.0)

        self.play(Write(warning), run_time=dur * 0.65)
        self.wait(dur * 0.35)


class A07_ArrivalMap(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 2.51)
        electron = Dot(radius=0.25, color=SLATE).shift(LEFT * 3.0)
        rings = VGroup(*[
            Circle(radius=0.7 * (i + 1), color=SLATE, stroke_width=2, stroke_opacity=0.7)
            .shift(LEFT * 3.0)
            for i in range(4)
        ])
        self.add(electron, rings)

        map_label = ink_txt("map of where\none arrival may happen", size=24, color=SLATE)
        map_label.shift(RIGHT * 1.5 + UP * 0.5)
        arrow = Arrow(map_label.get_left(), LEFT * 1.0, color=SLATE, buff=0.1)

        self.play(Write(map_label), run_time=dur * 0.6)
        self.play(GrowArrow(arrow), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A08_DetectionOneDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 3.29)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        d_label = ink_txt("detector", size=22).next_to(detector, DOWN, buff=0.2)
        self.add(detector, d_label)

        dot = Dot(radius=0.25, color=SLATE).shift(RIGHT * 3.0 + UP * 0.5)
        dot_label = ink_txt("one dot\n(particle)", size=24, color=SLATE)
        dot_label.next_to(dot, LEFT, buff=0.3)

        self.play(FadeIn(dot), run_time=dur * 0.45)
        self.play(Write(dot_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A09_ManyDotsPattern(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.24)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        self.add(detector)

        np.random.seed(42)
        dots = []
        attempts = 0
        while len(dots) < 80 and attempts < 5000:
            y = np.random.uniform(-2.5, 2.5)
            p = np.exp(-(y ** 2) / 1.0)
            if np.random.random() < p:
                dots.append(Dot(radius=0.1, color=SLATE, fill_opacity=0.7).shift(RIGHT * 3.0 + UP * y))
            attempts += 1

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.03),
                  run_time=dur * 0.75)
        self.wait(dur * 0.25)


class A10_WavePredictsCurve(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 3.19)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        self.add(detector)

        np.random.seed(42)
        dots = []
        attempts = 0
        while len(dots) < 80 and attempts < 5000:
            y = np.random.uniform(-2.5, 2.5)
            p = np.exp(-(y ** 2) / 1.0)
            if np.random.random() < p:
                dots.append(Dot(radius=0.1, color=SLATE, fill_opacity=0.6).shift(RIGHT * 3.0 + UP * y))
            attempts += 1
        self.add(*dots)

        prob_curve = ParametricFunction(
            lambda t: np.array([3.0 + 0.7 * np.exp(-(t ** 2) / 1.0), t, 0]),
            t_range=[-2.5, 2.5], color=TERRA, stroke_width=5
        )
        prob_label = ink_txt("wave predicts\nthis pattern", size=22, color=TERRA)
        prob_label.shift(LEFT * 0.5 + UP * 2.5)

        self.play(Create(prob_curve), run_time=dur * 0.55)
        self.play(Write(prob_label), run_time=dur * 0.3)
        self.wait(dur * 0.15)


class A11_SingleClickLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 2.95)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        self.add(detector)

        np.random.seed(42)
        dots = []
        attempts = 0
        while len(dots) < 80 and attempts < 5000:
            y = np.random.uniform(-2.5, 2.5)
            p = np.exp(-(y ** 2) / 1.0)
            if np.random.random() < p:
                dots.append(Dot(radius=0.1, color=SLATE, fill_opacity=0.5).shift(RIGHT * 3.0 + UP * y))
            attempts += 1
        self.add(*dots)

        highlighted = Dot(radius=0.22, color=RED_COL).shift(RIGHT * 3.0 + UP * 0.15)
        click_label = ink_txt("the particle:\nsingle click", size=24, color=RED_COL)
        click_label.shift(LEFT * 1.0 + DOWN * 1.5)
        arrow = Arrow(click_label.get_right(), highlighted.get_center(), color=RED_COL, buff=0.1)

        self.play(FadeIn(highlighted), run_time=dur * 0.3)
        self.play(Write(click_label), GrowArrow(arrow), run_time=dur * 0.5)
        self.wait(dur * 0.2)


class A12_DualitySummary(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 4.26)
        # Two-column layout
        wave_box = Rectangle(width=3.0, height=2.0, color=SLATE, fill_opacity=0.12).shift(LEFT * 2.5)
        wave_label = ink_txt("wave-shaped\npossibilities", size=22, color=SLATE).move_to(wave_box)

        plus = ink_txt("+", size=36).shift(ORIGIN)

        particle_box = Rectangle(width=3.0, height=2.0, color=RED_COL, fill_opacity=0.12).shift(RIGHT * 2.5)
        particle_label = ink_txt("particle-shaped\nresults", size=22, color=RED_COL).move_to(particle_box)

        duality = ink_txt("= wave-particle duality", size=28, color=TERRA).shift(DOWN * 2.5)

        self.play(FadeIn(wave_box), Write(wave_label), run_time=dur * 0.3)
        self.play(Write(plus), run_time=dur * 0.1)
        self.play(FadeIn(particle_box), Write(particle_label), run_time=dur * 0.3)
        self.play(Write(duality), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A13_WhisperAnalogy(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 3.53)
        # Sound rings spreading to several ears, one receives
        source = Dot(radius=0.15, color=INK).shift(LEFT * 3.5)
        rings = VGroup(*[
            Circle(radius=0.6 * (i + 1), color=SLATE, stroke_width=2, stroke_opacity=0.7)
            .shift(LEFT * 3.5)
            for i in range(3)
        ])

        # Several ear markers
        ears = VGroup(*[
            Circle(radius=0.22, color=INK, fill_opacity=0.3).shift(RIGHT * (1.0 + i * 1.5) + UP * (i - 1) * 0.8)
            for i in range(3)
        ])

        # One ear highlighted (receives)
        receiver = Circle(radius=0.22, color=TERRA, fill_opacity=0.8).shift(RIGHT * 2.5 + DOWN * 0.8)
        recv_label = ink_txt("one\nearful!", size=20, color=TERRA).next_to(receiver, RIGHT, buff=0.1)

        self.play(FadeIn(source), LaggedStart(*[Create(r) for r in rings], lag_ratio=0.2),
                  run_time=dur * 0.4)
        self.play(Create(ears), run_time=dur * 0.25)
        self.play(FadeIn(receiver), Write(recv_label), run_time=dur * 0.25)
        self.wait(dur * 0.1)


class A14_PondRipple(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 4.21)
        # Pond ripple with leaves, one receives
        source = Dot(radius=0.15, color=SLATE).shift(LEFT * 3.0 + DOWN * 0.5)
        rings = VGroup(*[
            Circle(radius=0.7 * (i + 1), color=SLATE, stroke_width=2, stroke_opacity=0.7)
            .shift(LEFT * 3.0 + DOWN * 0.5)
            for i in range(3)
        ])

        leaves = VGroup(*[
            Ellipse(width=0.5, height=0.3, color=INK, fill_opacity=0.4)
            .shift(RIGHT * (0.5 + i * 1.5) + UP * ((i % 2) * 0.6 - 0.3))
            for i in range(3)
        ])

        # One leaf chosen
        chosen = Ellipse(width=0.5, height=0.3, color=TERRA, fill_opacity=0.9).shift(RIGHT * 2.0 + UP * 0.3)
        chosen_label = ink_txt("chosen!", size=22, color=TERRA).next_to(chosen, UP, buff=0.1)

        self.play(FadeIn(source), LaggedStart(*[Create(r) for r in rings], lag_ratio=0.15),
                  run_time=dur * 0.4)
        self.play(Create(leaves), run_time=dur * 0.25)
        self.play(FadeIn(chosen), Write(chosen_label), run_time=dur * 0.25)
        self.wait(dur * 0.1)


class A15_StrangeButReal(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 3.53)
        wave_box = Rectangle(width=3.0, height=2.0, color=SLATE, fill_opacity=0.12).shift(LEFT * 2.5)
        wave_label = ink_txt("wave-shaped\npossibilities", size=22, color=SLATE).move_to(wave_box)
        plus = ink_txt("+", size=36).shift(ORIGIN)
        particle_box = Rectangle(width=3.0, height=2.0, color=RED_COL, fill_opacity=0.12).shift(RIGHT * 2.5)
        particle_label = ink_txt("particle-shaped\nresults", size=22, color=RED_COL).move_to(particle_box)
        self.add(wave_box, wave_label, plus, particle_box, particle_label)

        strange_label = ink_txt("strange — but really true", size=28, color=TERRA)
        strange_label.shift(DOWN * 2.8)
        qm_label = ink_txt("(quantum mechanics confirms)", size=22)
        qm_label.shift(DOWN * 3.5)

        self.play(Write(strange_label), run_time=dur * 0.5)
        self.play(Write(qm_label), run_time=dur * 0.35)
        self.wait(dur * 0.15)
