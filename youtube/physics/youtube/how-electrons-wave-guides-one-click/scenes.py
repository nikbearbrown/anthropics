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

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


# INTRO has render=none — skip

class A00_NoRouteCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 3.29)
        electron = Dot(radius=0.25, color=SLATE).shift(LEFT * 1.0)
        e_label = ink_txt("electron", size=24).next_to(electron, DOWN, buff=0.2)

        route_card = Rectangle(width=1.2, height=0.8, color=INK, fill_opacity=0.15)
        route_card.shift(RIGHT * 1.5 + UP * 0.3)
        route_txt = ink_txt("route\ncard", size=18)
        route_txt.move_to(route_card)

        cross1 = Line(route_card.get_corner(UL), route_card.get_corner(DR), color=RED_COL, stroke_width=5)
        cross2 = Line(route_card.get_corner(UR), route_card.get_corner(DL), color=RED_COL, stroke_width=5)

        label = ink_txt("no tiny route card!", size=26, color=RED_COL)
        label.shift(DOWN * 2.5)

        self.play(FadeIn(electron), Write(e_label), run_time=dur * 0.3)
        self.play(Create(route_card), Write(route_txt), run_time=dur * 0.25)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.2)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class A01_SpreadingWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.84)
        # Spreading probability wave with possible landing marks
        source = Dot(radius=0.2, color=SLATE).shift(LEFT * 3.0)

        rings = VGroup(*[
            Circle(radius=0.6 * (i + 1), color=SLATE, stroke_width=2 - i * 0.3, stroke_opacity=0.8 - i * 0.15)
            .shift(LEFT * 3.0)
            for i in range(4)
        ])

        # Landing marks spread out
        marks = VGroup(*[
            Dot(radius=0.1, color=TERRA).shift(LEFT * 3.0 + RIGHT * 2.5 + UP * (i - 2) * 0.7)
            for i in range(5)
        ])
        mark_label = ink_txt("possible\nlandings", size=20, color=TERRA)
        mark_label.shift(RIGHT * 1.5 + DOWN * 2.0)

        self.play(FadeIn(source), run_time=dur * 0.15)
        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.15), run_time=dur * 0.4)
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.12), run_time=dur * 0.3)
        self.play(Write(mark_label), run_time=dur * 0.1)
        self.wait(dur * 0.05)


class A02_NotMaterial(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 3.37)
        # Same wave, add "not material" label
        source = Dot(radius=0.2, color=SLATE).shift(LEFT * 3.0)
        rings = VGroup(*[
            Circle(radius=0.6 * (i + 1), color=SLATE, stroke_width=2 - i * 0.3, stroke_opacity=0.7)
            .shift(LEFT * 3.0)
            for i in range(4)
        ])
        marks = VGroup(*[
            Dot(radius=0.1, color=TERRA).shift(LEFT * 3.0 + RIGHT * 2.5 + UP * (i - 2) * 0.7)
            for i in range(5)
        ])
        self.add(source, rings, marks)

        not_label = ink_txt("NOT material smeared out", size=26, color=RED_COL)
        not_label.shift(DOWN * 2.8)
        cross = Line(not_label.get_left(), not_label.get_right(), color=RED_COL, stroke_width=3)

        prob_label = ink_txt("probability landscape", size=26, color=SLATE)
        prob_label.shift(DOWN * 3.5)

        self.play(Write(not_label), run_time=dur * 0.4)
        self.play(Write(prob_label), run_time=dur * 0.35)
        self.wait(dur * 0.25)


class A03_ProbLandscape(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.11)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 2, 0.5],
                    x_length=6, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 0.5 + DOWN * 0.5)
        x_lbl = ink_txt("position", size=20).next_to(axes.x_axis, DOWN, buff=0.2)
        y_lbl = ink_txt("probability", size=20).next_to(axes.y_axis, LEFT, buff=0.2)

        prob_curve = axes.plot(
            lambda x: 1.5 * np.exp(-((x - 2.5) ** 2) / 0.8),
            color=SLATE, stroke_width=4
        )
        click_mark = Dot(radius=0.15, color=TERRA).move_to(axes.c2p(2.5, 1.5))
        click_label = ink_txt("future click", size=20, color=TERRA)
        click_label.next_to(click_mark, UR, buff=0.1)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=dur * 0.45)
        self.play(Create(prob_curve), run_time=dur * 0.35)
        self.play(FadeIn(click_mark), Write(click_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A04_HighParts(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 2.82)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 2, 0.5],
                    x_length=6, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 0.5 + DOWN * 0.5)
        prob_curve = axes.plot(
            lambda x: 1.5 * np.exp(-((x - 2.5) ** 2) / 0.8),
            color=SLATE, stroke_width=4
        )
        self.add(axes, prob_curve)

        arrow = Arrow(axes.c2p(2.5, 2.0), axes.c2p(2.5, 1.6), color=TERRA, buff=0.05)
        high_label = ink_txt("more likely here", size=22, color=TERRA)
        high_label.shift(UP * 2.5)

        self.play(GrowArrow(arrow), Write(high_label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A05_LowParts(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 2.87)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 2, 0.5],
                    x_length=6, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 0.5 + DOWN * 0.5)
        prob_curve = axes.plot(
            lambda x: 1.5 * np.exp(-((x - 2.5) ** 2) / 0.8),
            color=SLATE, stroke_width=4
        )
        self.add(axes, prob_curve)

        arrow_high = Arrow(axes.c2p(2.5, 2.0), axes.c2p(2.5, 1.6), color=TERRA, buff=0.05)
        high_label = ink_txt("more likely", size=20, color=TERRA).shift(UP * 2.5)
        self.add(arrow_high, high_label)

        arrow_low = Arrow(axes.c2p(0.5, -0.5), axes.c2p(0.5, 0.1), color=SLATE, buff=0.05)
        low_label = ink_txt("less likely", size=20, color=SLATE).shift(LEFT * 2.8 + DOWN * 0.5)

        self.play(GrowArrow(arrow_low), Write(low_label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A06_DetectorOneDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 2.74)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        d_label = ink_txt("detector", size=22).next_to(detector, DOWN, buff=0.2)

        dot = Dot(radius=0.22, color=RED_COL).shift(RIGHT * 3.0 + UP * 0.5)
        dot_label = ink_txt("one click!", size=24, color=RED_COL)
        dot_label.next_to(dot, LEFT, buff=0.2)

        self.play(Create(detector), Write(d_label), run_time=dur * 0.45)
        self.play(FadeIn(dot), Write(dot_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A07_CollapseArrow(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 3.16)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 2, 0.5],
                    x_length=5, y_length=2.5,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 1.5 + DOWN * 0.3)
        prob_curve = axes.plot(
            lambda x: 1.5 * np.exp(-((x - 2.5) ** 2) / 0.8),
            color=SLATE, stroke_width=3, stroke_opacity=0.5
        )
        self.add(axes, prob_curve)

        detector = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=5).shift(RIGHT * 3.2)
        dot = Dot(radius=0.22, color=RED_COL).shift(RIGHT * 3.2 + UP * 0.3)
        self.add(detector, dot)

        collapse_arrow = Arrow(LEFT * 0.5 + DOWN * 0.5, RIGHT * 2.5 + UP * 0.3,
                               color=TERRA, stroke_width=4, buff=0.1)
        collapse_label = ink_txt("collapses\nto one result", size=22, color=TERRA)
        collapse_label.shift(DOWN * 2.5)

        self.play(GrowArrow(collapse_arrow), run_time=dur * 0.5)
        self.play(Write(collapse_label), run_time=dur * 0.35)
        self.wait(dur * 0.15)


class A08_AnotherDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 2.87)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        dot1 = Dot(radius=0.18, color=RED_COL).shift(RIGHT * 3.0 + UP * 0.5)
        self.add(detector, dot1)

        dot2 = Dot(radius=0.18, color=RED_COL).shift(RIGHT * 3.0 + DOWN * 0.8)
        label = ink_txt("another run,\nanother dot", size=22)
        label.shift(LEFT * 1.5 + DOWN * 0.5)

        self.play(FadeIn(dot2), run_time=dur * 0.4)
        self.play(Write(label), run_time=dur * 0.4)
        self.wait(dur * 0.2)


class A09_DotsTraceWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.16)
        detector = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=5).shift(RIGHT * 3.0)
        self.add(detector)

        np.random.seed(55)
        dots = []
        attempts = 0
        while len(dots) < 60 and attempts < 5000:
            y = np.random.uniform(-2.5, 2.5)
            p = np.exp(-((y - 0.0) ** 2) / 1.2)
            if np.random.random() < p:
                dots.append(Dot(radius=0.1, color=SLATE, fill_opacity=0.7).shift(RIGHT * 3.0 + UP * y))
            attempts += 1

        # Probability envelope
        envelope = ParametricFunction(
            lambda t: np.array([3.0 + 0.5 * np.exp(-(t ** 2) / 1.2), t, 0]),
            t_range=[-2.5, 2.5], color=TERRA, stroke_width=4
        )

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.04), run_time=dur * 0.6)
        self.play(Create(envelope), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A10_WaveGuidesStats(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 2.95)
        # Wave on left, crossed-out hidden bead on right
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1],
                    x_length=4, y_length=2.5,
                    axis_config={"color": INK, "include_tip": False}).shift(LEFT * 2.0)
        prob = axes.plot(lambda x: 1.5 * np.exp(-((x - 2.0) ** 2) / 0.8),
                         color=SLATE, stroke_width=4)
        wave_label = ink_txt("the wave", size=22, color=SLATE).shift(LEFT * 2.5 + UP * 2.0)
        self.add(axes, prob, wave_label)

        bead = Circle(radius=0.25, color=INK, fill_opacity=0.5).shift(RIGHT * 2.5 + UP * 0.2)
        bead_label = ink_txt("hidden bead", size=20).next_to(bead, DOWN, buff=0.15)
        cross1 = Line(bead.get_corner(UL), bead.get_corner(DR), color=RED_COL, stroke_width=4)
        cross2 = Line(bead.get_corner(UR), bead.get_corner(DL), color=RED_COL, stroke_width=4)

        self.play(Create(bead), Write(bead_label), run_time=dur * 0.35)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.3)
        self.wait(dur * 0.35)


class A11_WaveMoves(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 2.77)
        axes = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=7, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.5)
        wave = axes.plot(lambda x: np.exp(-((x - 1.5) ** 2) / 0.5) * np.cos(6 * (x - 1.5)),
                         color=SLATE, stroke_width=4)
        motion = Arrow(LEFT * 2.0 + DOWN * 1.5, RIGHT * 2.0 + DOWN * 1.5, color=TERRA, stroke_width=4)
        motion_label = ink_txt("wave moves →", size=24, color=TERRA).shift(DOWN * 2.5)

        self.play(Create(axes), Create(wave), run_time=dur * 0.5)
        self.play(GrowArrow(motion), Write(motion_label), run_time=dur * 0.4)
        self.wait(dur * 0.1)


class A12_QMRulebook(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 3.34)
        axes = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=7, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.5)
        wave = axes.plot(lambda x: np.exp(-((x - 1.5) ** 2) / 0.5) * np.cos(6 * (x - 1.5)),
                         color=SLATE, stroke_width=4)
        motion = Arrow(LEFT * 2.0 + DOWN * 1.5, RIGHT * 2.0 + DOWN * 1.5, color=TERRA, stroke_width=4)
        self.add(axes, wave, motion)

        qm_label = ink_txt("Quantum Mechanics\n= rulebook for this wave", size=26)
        qm_label.shift(UP * 2.5)

        self.play(Write(qm_label), run_time=dur * 0.65)
        self.wait(dur * 0.35)


class A13_Summary(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 3.58)
        map_box = Rectangle(width=3.5, height=1.5, color=SLATE, fill_opacity=0.15).shift(LEFT * 2.0)
        map_label = ink_txt("spread-out\npossibility map", size=22, color=SLATE)
        map_label.move_to(map_box)

        arrow = Arrow(map_box.get_right(), RIGHT * 0.5, color=TERRA, buff=0.05, stroke_width=4)

        detect_box = Rectangle(width=2.5, height=1.5, color=RED_COL, fill_opacity=0.15).shift(RIGHT * 2.5)
        detect_label = ink_txt("one sharp\ndetection", size=22, color=RED_COL)
        detect_label.move_to(detect_box)

        self.play(FadeIn(map_box), Write(map_label), run_time=dur * 0.35)
        self.play(GrowArrow(arrow), run_time=dur * 0.25)
        self.play(FadeIn(detect_box), Write(detect_label), run_time=dur * 0.3)
        self.wait(dur * 0.1)
