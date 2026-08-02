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

class A00_ClassicalBall(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 2.12)
        # Hill profile
        hill = ParametricFunction(
            lambda t: np.array([t, max(0, 1.8 * np.exp(-(t ** 2) / 0.4)), 0]),
            t_range=[-3.5, 3.5], color=INK, stroke_width=4
        )
        ground = Line(LEFT * 4.5 + DOWN * 0.1, RIGHT * 4.5 + DOWN * 0.1, color=INK, stroke_width=3)

        ball = Circle(radius=0.25, color=SLATE, fill_opacity=0.8).shift(LEFT * 3.0 + UP * 0.15)
        block_label = ink_txt("BLOCKED", size=26, color=RED_COL).shift(UP * 2.5)

        self.play(Create(ground), Create(hill), run_time=dur * 0.5)
        self.play(FadeIn(ball), Write(block_label), run_time=dur * 0.4)
        self.wait(dur * 0.1)


class A01_StartingEnergyLine(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.29)
        hill = ParametricFunction(
            lambda t: np.array([t, max(0, 1.8 * np.exp(-(t ** 2) / 0.4)), 0]),
            t_range=[-3.5, 3.5], color=INK, stroke_width=4
        )
        ground = Line(LEFT * 4.5 + DOWN * 0.1, RIGHT * 4.5 + DOWN * 0.1, color=INK, stroke_width=3)
        ball = Circle(radius=0.25, color=SLATE, fill_opacity=0.8).shift(LEFT * 3.0 + UP * 0.15)
        self.add(ground, hill, ball)

        energy_line = DashedLine(LEFT * 4.0 + UP * 0.8, RIGHT * 4.0 + UP * 0.8,
                                 color=TERRA, stroke_width=3)
        e_label = ink_txt("E (starting energy)", size=22, color=TERRA)
        e_label.next_to(energy_line, RIGHT, buff=0.15)

        self.play(Create(energy_line), Write(e_label), run_time=dur * 0.6)
        self.wait(dur * 0.4)


class A02_ForbiddenFarValley(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 3.71)
        hill = ParametricFunction(
            lambda t: np.array([t, max(0, 2.5 * np.exp(-(t ** 2) / 0.25)), 0]),
            t_range=[-3.5, 3.5], color=INK, stroke_width=4
        )
        ground = Line(LEFT * 4.5 + DOWN * 0.1, RIGHT * 4.5 + DOWN * 0.1, color=INK, stroke_width=3)
        ball = Circle(radius=0.25, color=SLATE, fill_opacity=0.8).shift(LEFT * 3.0 + UP * 0.15)
        energy_line = DashedLine(LEFT * 4.0 + UP * 0.8, RIGHT * 4.0 + UP * 0.8,
                                 color=TERRA, stroke_width=3)
        self.add(ground, hill, ball, energy_line)

        # Far valley shaded forbidden
        forbidden = Rectangle(width=2.0, height=3.0, color=RED_COL, fill_opacity=0.15,
                               stroke_width=0).shift(RIGHT * 3.0 + UP * 1.0)
        forbidden_label = ink_txt("forbidden!", size=22, color=RED_COL).shift(RIGHT * 3.0 + UP * 2.8)

        self.play(FadeIn(forbidden), Write(forbidden_label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A03_WaveNotDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 4.62)
        # Wave packet on the left approaching barrier
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=8, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.3)
        # Barrier
        barrier = Rectangle(width=0.8, height=3.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 1.2)
        barrier_label = ink_txt("barrier\n(V > E)", size=20).next_to(barrier, UP, buff=0.2)

        # Wave packet
        wave_pkt = axes.plot(
            lambda x: np.exp(-((x + 2.5) ** 2) / 0.4) * np.cos(8 * (x + 2.5)),
            color=SLATE, stroke_width=4
        )

        # Crossed-out certainty dot
        dot = Circle(radius=0.22, color=INK, fill_opacity=0.7).shift(LEFT * 2.5 + DOWN * 1.5)
        cross1 = Line(dot.get_corner(UL), dot.get_corner(DR), color=RED_COL, stroke_width=4)
        cross2 = Line(dot.get_corner(UR), dot.get_corner(DL), color=RED_COL, stroke_width=4)
        dot_label = ink_txt("not a\ncertainty dot", size=20, color=RED_COL).shift(LEFT * 2.5 + DOWN * 2.8)

        label = ink_txt("quantum particle = wave", size=26, color=SLATE).shift(UP * 2.5)

        self.play(Create(axes), Create(barrier), Write(barrier_label), run_time=dur * 0.3)
        self.play(Create(wave_pkt), run_time=dur * 0.25)
        self.play(FadeIn(dot), Create(cross1), Create(cross2), Write(dot_label), run_time=dur * 0.25)
        self.play(Write(label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A04_MostWaveLeft(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 2.22)
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=8, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.3)
        barrier = Rectangle(width=0.8, height=3.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 1.2)
        self.add(axes, barrier)

        # Large wave on left
        left_wave = axes.plot(
            lambda x: 1.0 * np.exp(-((x + 1.5) ** 2) / 0.6) * np.cos(6 * (x + 1.5)),
            color=SLATE, stroke_width=5
        )
        label = ink_txt("most wave in left valley", size=24, color=SLATE).shift(LEFT * 2.5 + UP * 2.2)

        self.play(Create(left_wave), run_time=dur * 0.5)
        self.play(Write(label), run_time=dur * 0.35)
        self.wait(dur * 0.15)


class A05_TailLeaksIn(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 2.17)
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=8, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.3)
        barrier = Rectangle(width=0.8, height=3.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 1.2)
        left_wave = axes.plot(
            lambda x: 1.0 * np.exp(-((x + 1.5) ** 2) / 0.6) * np.cos(6 * (x + 1.5)),
            color=SLATE, stroke_width=5
        )
        self.add(axes, barrier, left_wave)

        # Exponentially decaying tail inside barrier
        decay_tail = axes.plot(
            lambda x: 0.6 * np.exp(-(x - 0.1) * 3) * np.cos(2 * x) if 0.1 <= x <= 0.9 else 0,
            x_range=[0.1, 0.9], color=TERRA, stroke_width=4
        )
        label = ink_txt("tail leaks in!", size=24, color=TERRA).shift(RIGHT * 0.5 + UP * 2.2)

        self.play(Create(decay_tail), Write(label), run_time=dur * 0.8)
        self.wait(dur * 0.2)


class A06_TailReachesFarSide(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 2.35)
        axes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=8, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.3)
        barrier = Rectangle(width=0.8, height=3.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 1.2)
        left_wave = axes.plot(
            lambda x: 1.0 * np.exp(-((x + 1.5) ** 2) / 0.6) * np.cos(6 * (x + 1.5)),
            color=SLATE, stroke_width=5
        )
        self.add(axes, barrier, left_wave)

        # Small transmitted wave on far side
        right_wave = axes.plot(
            lambda x: 0.25 * np.exp(-((x - 2.0) ** 2) / 0.4) * np.cos(6 * (x - 2.0)),
            color=TERRA, stroke_width=4
        )
        label = ink_txt("tail reaches far side", size=24, color=TERRA).shift(RIGHT * 2.5 + UP * 2.2)

        self.play(Create(right_wave), Write(label), run_time=dur * 0.75)
        self.wait(dur * 0.25)


class A07_DetectionBeyondWall(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 2.93)
        barrier = Rectangle(width=0.8, height=4.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 0.5)
        detector = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        self.add(barrier, detector)

        dot = Dot(radius=0.22, color=RED_COL).shift(RIGHT * 3.5 + UP * 0.4)
        label = ink_txt("particle found\nbeyond the wall!", size=24, color=RED_COL)
        label.shift(RIGHT * 3.5 + DOWN * 2.0)

        self.play(FadeIn(dot), run_time=dur * 0.45)
        self.play(Write(label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A08_SmallNotZero(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 2.27)
        barrier = Rectangle(width=0.8, height=4.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.5 + UP * 0.5)
        detector = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=4).shift(RIGHT * 3.5)
        dot = Dot(radius=0.22, color=RED_COL).shift(RIGHT * 3.5 + UP * 0.4)
        self.add(barrier, detector, dot)

        label = ink_txt("T > 0\n(small, but not zero)", size=26, color=SLATE)
        label.shift(LEFT * 1.5 + DOWN * 2.0)

        self.play(Write(label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A09_WiderBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.42)
        # Two comparisons: narrow vs wide barrier
        # Narrow barrier
        narrow = Rectangle(width=0.5, height=3.0, color=INK, fill_opacity=0.4).shift(LEFT * 1.5 + UP * 0.5)
        n_tail = ParametricFunction(
            lambda t: np.array([-1.5 + 0.5 + t * 0.35, 0.5 * np.exp(-t * 3), 0]),
            t_range=[0, 1], color=TERRA, stroke_width=5
        )
        n_label = ink_txt("narrow\n→ more T", size=20, color=TERRA).shift(LEFT * 1.5 + UP * 2.8)

        # Wide barrier
        wide = Rectangle(width=1.8, height=3.0, color=INK, fill_opacity=0.4).shift(RIGHT * 2.0 + UP * 0.5)
        w_tail = ParametricFunction(
            lambda t: np.array([2.0 - 0.9 + t * 0.9, 0.5 * np.exp(-t * 6), 0]),
            t_range=[0, 1], color=TERRA, stroke_width=2, stroke_opacity=0.5
        )
        w_label = ink_txt("wide\n→ less T", size=20, color=RED_COL).shift(RIGHT * 2.0 + UP * 2.8)

        self.play(Create(narrow), Create(n_tail), Write(n_label), run_time=dur * 0.45)
        self.play(Create(wide), Create(w_tail), Write(w_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A10_LowerBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 2.82)
        # High barrier vs low barrier
        high = Rectangle(width=0.8, height=3.5, color=INK, fill_opacity=0.45).shift(LEFT * 2.0 + UP * 0.8)
        h_label = ink_txt("tall barrier\n→ tiny T", size=20, color=RED_COL).shift(LEFT * 2.0 + DOWN * 1.8)

        low = Rectangle(width=0.8, height=1.5, color=SLATE, fill_opacity=0.35).shift(RIGHT * 2.0 + UP * 0.25)
        l_label = ink_txt("low barrier\n→ more T", size=20, color=SLATE).shift(RIGHT * 2.0 + DOWN * 1.8)

        t_formula = ink_txt("T ≈ e^(-2κL)", size=28, color=TERRA)
        t_formula.shift(UP * 2.8)

        self.play(Create(high), Write(h_label), run_time=dur * 0.35)
        self.play(Create(low), Write(l_label), run_time=dur * 0.35)
        self.play(Write(t_formula), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A11_InsideForbiddenRegion(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.06)
        # Forbidden region shaded, particle dot inside
        barrier = Rectangle(width=1.5, height=4.0, color=INK, fill_opacity=0.3).shift(RIGHT * 0.3 + UP * 0.5)
        forbidden_shade = Rectangle(width=1.5, height=4.0, color=RED_COL, fill_opacity=0.12,
                                    stroke_width=0).shift(RIGHT * 0.3 + UP * 0.5)
        forbidden_label = ink_txt("forbidden region", size=20, color=RED_COL).shift(RIGHT * 0.3 + UP * 3.0)

        dot_inside = Dot(radius=0.22, color=TERRA).shift(RIGHT * 0.3 + UP * 0.8)
        dot_label = ink_txt("particle found\ninside!", size=22, color=TERRA).shift(RIGHT * 2.5 + UP * 0.8)

        self.play(Create(barrier), FadeIn(forbidden_shade), Write(forbidden_label), run_time=dur * 0.45)
        self.play(FadeIn(dot_inside), Write(dot_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A12_NotSecretTunnel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 2.27)
        # Cross out idea of a secret tunnel
        mountain = ParametricFunction(
            lambda t: np.array([t, max(0, 2.0 * (1 - t ** 2 / 4)), 0]),
            t_range=[-2.5, 2.5], color=INK, stroke_width=4
        )
        # A horizontal "tunnel" dotted line through the mountain
        fake_tunnel = DashedLine(LEFT * 2.0 + UP * 0.5, RIGHT * 2.0 + UP * 0.5,
                                 color=SLATE, stroke_width=3)
        tunnel_label = ink_txt("secret tunnel?", size=24).shift(DOWN * 1.5)

        cross1 = Line(LEFT * 2.5 + UP * 2.5, RIGHT * 2.5 + DOWN * 1.0, color=RED_COL, stroke_width=6)
        cross2 = Line(LEFT * 2.5 + DOWN * 1.0, RIGHT * 2.5 + UP * 2.5, color=RED_COL, stroke_width=6)

        no_label = ink_txt("NO tunnel!", size=28, color=RED_COL).shift(DOWN * 2.5)

        self.play(Create(mountain), Create(fake_tunnel), Write(tunnel_label), run_time=dur * 0.4)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.3)
        self.play(Write(no_label), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A13_WaveRefusesToStop(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 2.53)
        # Wave crossing a boundary smoothly
        axes = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 0.5],
                    x_length=7, y_length=3,
                    axis_config={"color": INK, "include_tip": False}).shift(DOWN * 0.5)
        boundary = Line(UP * 1.8, DOWN * 1.8, color=INK, stroke_width=4).shift(RIGHT * 0.5)

        left_wave = axes.plot(lambda x: np.cos(4 * x), x_range=[0, 2.8], color=SLATE, stroke_width=4)
        right_decay = axes.plot(
            lambda x: 0.6 * np.exp(-(x - 3.0) * 2.5) * np.cos(4 * x),
            x_range=[3.0, 5.8], color=TERRA, stroke_width=4
        )

        label = ink_txt("wave refuses to stop\ninstantly at boundary", size=22, color=TERRA)
        label.shift(UP * 2.5)

        self.play(Create(axes), Create(boundary), run_time=dur * 0.3)
        self.play(Create(left_wave), Create(right_decay), run_time=dur * 0.4)
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A14_ElectronsInNuclei(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 3.71)
        # Atom with electron cloud leaking into nucleus
        nucleus = Circle(radius=0.5, color=TERRA, fill_opacity=0.6).shift(ORIGIN)
        n_label = ink_txt("nucleus", size=20, color=TERRA).next_to(nucleus, DOWN, buff=0.2)

        orbit = Circle(radius=1.8, color=SLATE, stroke_width=2).shift(ORIGIN)
        e_label = ink_txt("electron\ncloud", size=20, color=SLATE).shift(RIGHT * 2.5 + UP * 1.0)

        # Electron probability inside nucleus
        inside_dot = Dot(radius=0.2, color=SLATE, fill_opacity=0.7).shift(UP * 0.25)
        inside_label = ink_txt("e⁻ found here\n(tunneling!)", size=20, color=SLATE)
        inside_label.shift(LEFT * 2.5 + UP * 1.5)

        self.play(Create(nucleus), Write(n_label), run_time=dur * 0.3)
        self.play(Create(orbit), Write(e_label), run_time=dur * 0.3)
        self.play(FadeIn(inside_dot), Write(inside_label), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A15_TunnelingSummary(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 3.42)
        impossible = ink_txt("classically impossible\npaths", size=26, color=RED_COL).shift(LEFT * 2.5)
        arrow = Arrow(impossible.get_right(), RIGHT * 0.5, color=TERRA, stroke_width=4, buff=0.1)
        tiny_prob = ink_txt("tiny\nprobabilities", size=26, color=SLATE).shift(RIGHT * 2.5)

        formula = ink_txt("T ≈ e^(-2κL)", size=30, color=TERRA)
        formula.shift(DOWN * 2.5)

        self.play(Write(impossible), run_time=dur * 0.3)
        self.play(GrowArrow(arrow), run_time=dur * 0.2)
        self.play(Write(tiny_prob), run_time=dur * 0.25)
        self.play(Write(formula), run_time=dur * 0.2)
        self.wait(dur * 0.05)
