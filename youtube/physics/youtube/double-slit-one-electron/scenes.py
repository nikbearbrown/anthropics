import json
from pathlib import Path
from manim import *
import numpy as np

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
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
        dur = d("INTRO", 3.99)
        series = ink_txt("Bear's Notes", size=40)
        title = ink_txt("Why One Electron at a Time\nStill Builds Stripes", size=30)
        title.next_to(series, DOWN, buff=0.5)
        grp = VGroup(series, title).move_to(ORIGIN)
        self.play(FadeIn(series), run_time=dur * 0.4)
        self.play(FadeIn(title), run_time=dur * 0.4)
        self.wait(dur * 0.2)


class H01_ElectronGun(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 5.42)
        gun = Rectangle(width=1.5, height=0.8, color=INK, fill_opacity=0.5).shift(LEFT * 4.5)
        gun_label = ink_txt("electron gun", size=20)
        gun_label.next_to(gun, DOWN, buff=0.2)

        electron = Dot(radius=0.18, color=SLATE).shift(LEFT * 3.5)
        arrow = Arrow(gun.get_right(), electron.get_center() + RIGHT * 2.5, color=SLATE, buff=0.05)
        alone_label = ink_txt("one at a time", size=24)
        alone_label.shift(UP * 1.5)

        self.play(Create(gun), Write(gun_label), run_time=dur * 0.3)
        self.play(FadeIn(electron), run_time=dur * 0.2)
        self.play(Create(arrow), run_time=dur * 0.25)
        self.play(Write(alone_label), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class H02_SingleDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 4.61)
        screen = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=4).shift(RIGHT * 3.0)
        screen_label = ink_txt("screen", size=22)
        screen_label.next_to(screen, DOWN, buff=0.2)

        dot = Dot(radius=0.18, color=SLATE).shift(RIGHT * 3.0 + UP * 0.3)

        shrug = ink_txt("just one dot?", size=26)
        shrug.shift(LEFT * 1.0 + DOWN * 1.5)

        self.play(Create(screen), Write(screen_label), run_time=dur * 0.3)
        self.play(FadeIn(dot), run_time=dur * 0.2)
        self.play(Write(shrug), run_time=dur * 0.25)
        self.wait(dur * 0.25)


class A01_SlitsSetup(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 4.31)
        # Two-slit barrier and detector screen
        slit_top = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 1.8)
        slit_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bot = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 1.8)

        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        label_barrier = ink_txt("two slits", size=22)
        label_barrier.next_to(slit_top, LEFT, buff=0.3)
        label_screen = ink_txt("detector", size=22)
        label_screen.next_to(screen, DOWN, buff=0.2)

        self.play(Create(slit_top), Create(slit_mid), Create(slit_bot), run_time=dur * 0.35)
        self.play(Write(label_barrier), run_time=dur * 0.2)
        self.play(Create(screen), Write(label_screen), run_time=dur * 0.3)
        self.wait(dur * 0.15)


class A02_FirstDots(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.2)
        slit_top = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 1.8)
        slit_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bot = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 1.8)
        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(slit_top, slit_mid, slit_bot, screen)

        np.random.seed(42)
        dots = VGroup(*[
            Dot(radius=0.12, color=SLATE).shift(RIGHT * 3.5 + UP * np.random.uniform(-2.5, 2.5))
            for _ in range(6)
        ])
        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.15),
                  run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A03_HundredDots(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.73)
        slit_top = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 1.8)
        slit_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bot = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 1.8)
        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(slit_top, slit_mid, slit_bot, screen)

        np.random.seed(7)
        dots = VGroup(*[
            Dot(radius=0.08, color=SLATE, fill_opacity=0.7).shift(RIGHT * 3.5 + UP * np.random.uniform(-2.5, 2.5))
            for _ in range(100)
        ])
        counter = ink_txt("100", size=32, color=TERRA)
        counter.shift(LEFT * 4.5 + UP * 2.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.01),
                  run_time=dur * 0.6)
        self.play(Write(counter), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A04_FringesEmerge(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 4.76)
        slit_top = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 1.8)
        slit_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bot = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 1.8)
        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(slit_top, slit_mid, slit_bot, screen)

        # Interference probability: sample from |cos(3y)|^2
        np.random.seed(99)
        dots = []
        attempts = 0
        while len(dots) < 400 and attempts < 20000:
            y = np.random.uniform(-2.8, 2.8)
            p = np.cos(3 * y) ** 2
            if np.random.random() < p:
                x_jitter = np.random.uniform(-0.05, 0.05)
                dots.append(Dot(radius=0.06, color=SLATE, fill_opacity=0.6)
                            .shift(RIGHT * (3.5 + x_jitter) + UP * y))
            attempts += 1

        dot_grp = VGroup(*dots)
        counter = ink_txt("70,000", size=32, color=TERRA)
        counter.shift(LEFT * 4.5 + UP * 2.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.005),
                  run_time=dur * 0.7)
        self.play(Write(counter), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A05_InterferenceCurve(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.71)
        slit_top = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 1.8)
        slit_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bot = Rectangle(width=0.25, height=1.5, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 1.8)
        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(slit_top, slit_mid, slit_bot, screen)

        # Dots from A04 (static)
        np.random.seed(99)
        dots = []
        attempts = 0
        while len(dots) < 300 and attempts < 15000:
            y = np.random.uniform(-2.8, 2.8)
            p = np.cos(3 * y) ** 2
            if np.random.random() < p:
                dots.append(Dot(radius=0.06, color=SLATE, fill_opacity=0.5)
                            .shift(RIGHT * 3.5 + UP * y))
            attempts += 1
        self.add(*dots)

        # Intensity curve
        curve = ParametricFunction(
            lambda t: np.array([3.5 + 0.5 * np.cos(3 * t) ** 2, t, 0]),
            t_range=[-2.8, 2.8], color=SLATE, stroke_width=4
        )
        curve_label = ink_txt("interference\npattern", size=22, color=SLATE)
        curve_label.shift(LEFT * 1.5 + DOWN * 2.5)

        self.play(Create(curve), run_time=dur * 0.6)
        self.play(Write(curve_label), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A06_WavesThroughBothSlits(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 4.93)
        slit_top_pos = LEFT * 0.5 + UP * 1.0
        slit_bot_pos = LEFT * 0.5 + DOWN * 1.0

        slit_bar_top = Rectangle(width=0.25, height=1.2, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 2.1)
        slit_bar_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bar_bot = Rectangle(width=0.25, height=1.2, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 2.1)
        self.add(slit_bar_top, slit_bar_mid, slit_bar_bot)

        # Incoming wavefront
        wave_in = Arc(radius=1.0, angle=PI * 0.6, start_angle=-PI * 0.3,
                      color=SLATE, stroke_width=3).shift(LEFT * 3.5)
        wave_in2 = Arc(radius=1.6, angle=PI * 0.6, start_angle=-PI * 0.3,
                       color=SLATE, stroke_width=2).shift(LEFT * 3.5)

        # Circular ripples from each slit
        ripple1a = Circle(radius=0.8, color=SLATE, stroke_width=2).shift(slit_top_pos)
        ripple1b = Circle(radius=1.4, color=SLATE, stroke_width=1.5).shift(slit_top_pos)
        ripple2a = Circle(radius=0.8, color=SLATE, stroke_width=2).shift(slit_bot_pos)
        ripple2b = Circle(radius=1.4, color=SLATE, stroke_width=1.5).shift(slit_bot_pos)

        label = ink_txt("each electron\nwaves through both", size=22, color=SLATE)
        label.shift(RIGHT * 3.5 + UP * 2.5)

        self.play(Create(wave_in), Create(wave_in2), run_time=dur * 0.25)
        self.play(
            Create(ripple1a), Create(ripple1b),
            Create(ripple2a), Create(ripple2b),
            run_time=dur * 0.4
        )
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.1)


class A07_ProbabilityEnvelope(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 4.48)
        slit_top_pos = LEFT * 0.5 + UP * 1.0
        slit_bot_pos = LEFT * 0.5 + DOWN * 1.0
        slit_bar_top = Rectangle(width=0.25, height=1.2, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + UP * 2.1)
        slit_bar_mid = Rectangle(width=0.25, height=0.6, color=INK, fill_opacity=0.9).shift(LEFT * 0.5)
        slit_bar_bot = Rectangle(width=0.25, height=1.2, color=INK, fill_opacity=0.9).shift(LEFT * 0.5 + DOWN * 2.1)
        ripple1a = Circle(radius=0.8, color=SLATE, stroke_width=2, fill_opacity=0).shift(slit_top_pos)
        ripple2a = Circle(radius=0.8, color=SLATE, stroke_width=2, fill_opacity=0).shift(slit_bot_pos)
        self.add(slit_bar_top, slit_bar_mid, slit_bar_bot, ripple1a, ripple2a)

        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(screen)

        prob_curve = ParametricFunction(
            lambda t: np.array([3.5 + 0.6 * np.cos(3 * t) ** 2, t, 0]),
            t_range=[-2.8, 2.8], color=TERRA, stroke_width=5
        )
        label = ink_txt("probability\nenvelope", size=22, color=TERRA)
        label.shift(RIGHT * 4.5 + DOWN * 2.5)

        self.play(Create(prob_curve), run_time=dur * 0.6)
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A08_DotsUnderEnvelope(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.61)
        screen = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        prob_curve = ParametricFunction(
            lambda t: np.array([3.5 + 0.6 * np.cos(3 * t) ** 2, t, 0]),
            t_range=[-2.8, 2.8], color=TERRA, stroke_width=3, stroke_opacity=0.5
        )
        self.add(screen, prob_curve)

        np.random.seed(77)
        dots = []
        attempts = 0
        while len(dots) < 200 and attempts < 10000:
            y = np.random.uniform(-2.8, 2.8)
            p = np.cos(3 * y) ** 2
            if np.random.random() < p:
                dots.append(Dot(radius=0.08, color=SLATE, fill_opacity=0.65)
                            .shift(RIGHT * 3.5 + UP * y))
            attempts += 1

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.01),
                  run_time=dur * 0.8)
        self.wait(dur * 0.2)


class A09_WaveAndDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 4.67)
        # Show one wave traveling and collapsing to a dot
        axes = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=6, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 0.5)

        wave = axes.plot(lambda x: np.exp(-((x - 1.5) ** 2) / 0.4) * np.cos(8 * (x - 1.5)),
                         color=SLATE, stroke_width=3)

        prob_envelope = ParametricFunction(
            lambda t: np.array([3.5 + 0.6 * np.cos(3 * t) ** 2, t, 0]),
            t_range=[-1.3, 1.3], color=TERRA, stroke_width=2, stroke_opacity=0.4
        ).shift(RIGHT * 0.5)

        dot = Dot(radius=0.2, color=SLATE).shift(RIGHT * 3.0 + UP * 0.3)

        label = ink_txt("wave → probability → one dot", size=24)
        label.shift(DOWN * 2.5)

        self.play(Create(axes), Create(wave), run_time=dur * 0.35)
        self.play(FadeOut(wave), FadeIn(dot), run_time=dur * 0.3)
        self.play(Create(prob_envelope), run_time=dur * 0.2)
        self.play(Write(label), run_time=dur * 0.1)
        self.wait(dur * 0.05)
