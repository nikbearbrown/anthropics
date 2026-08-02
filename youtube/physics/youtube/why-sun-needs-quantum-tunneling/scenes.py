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

# INTRO is render:none — skip.

class A00_SunNotFire(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 2.46)
        sun = Circle(radius=1.5, color=TERRA, stroke_width=4).set_fill(TERRA, opacity=0.15)
        fire_label = ink_txt("ordinary fire?", size=30, color=RED)
        cross = Cross(fire_label, color=RED, stroke_width=5)
        group = VGroup(fire_label, cross).next_to(sun, RIGHT, buff=0.5)
        self.play(Create(sun), run_time=0.5)
        self.play(FadeIn(fire_label), Create(cross), run_time=0.6)
        self.wait(dur - 1.1)


class A01_BonfireEmpties(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.47)
        sun = Circle(radius=1.2, color=TERRA, stroke_width=4).set_fill(TERRA, opacity=0.15).shift(LEFT * 2)
        # fuel gauge
        gauge_bg = Rectangle(width=0.5, height=2.0, color=INK, stroke_width=2).set_fill(CREAM, 1).shift(RIGHT * 3)
        fuel = Rectangle(width=0.46, height=2.0, color=TERRA, stroke_width=0).set_fill(TERRA, opacity=0.7)
        fuel.align_to(gauge_bg, DOWN).shift(RIGHT * 3)
        gauge_label = ink_txt("fuel", size=22, color=INK).next_to(gauge_bg, DOWN, buff=0.1)
        empty = ink_txt("EMPTY\nin ~5000 years", size=22, color=RED).next_to(gauge_bg, RIGHT, buff=0.2)
        self.add(sun, gauge_bg, fuel, gauge_label)
        self.play(fuel.animate.scale([1, 0.01, 1]).align_to(gauge_bg, DOWN), run_time=1.0)
        self.play(FadeIn(empty), run_time=0.4)
        self.wait(dur - 1.4)


class A02_BillionsOfYears(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 2.51)
        sun = Circle(radius=1.2, color=TERRA, stroke_width=4).set_fill(TERRA, opacity=0.15).shift(LEFT * 2)
        timeline = Line(LEFT * 1, RIGHT * 4, color=INK, stroke_width=3)
        tick_labels = VGroup(*[
            ink_txt(f"{i}B yr", size=20, color=SLATE).shift(RIGHT * (i - 1) * 1.0 + DOWN * 0.5)
            for i in range(1, 5)
        ])
        ticks = VGroup(*[
            Line(UP * 0.15, DOWN * 0.15, color=INK, stroke_width=2).shift(RIGHT * (i - 1) * 1.0)
            for i in range(1, 5)
        ])
        arrow_now = Arrow(RIGHT * 3.5 + UP * 0.6, RIGHT * 3.0, color=TERRA, stroke_width=3, buff=0.1,
                          max_tip_length_to_length_ratio=0.4)
        now_label = ink_txt("now", size=22, color=TERRA).next_to(arrow_now.get_start(), UP, buff=0.05)
        self.add(sun)
        self.play(Create(timeline), FadeIn(ticks), FadeIn(tick_labels), run_time=0.8)
        self.play(GrowArrow(arrow_now), FadeIn(now_label), run_time=0.4)
        self.wait(dur - 1.2)


class A03_CoreEngine(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 2.22)
        sun_outer = Circle(radius=2.0, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.08)
        core = Circle(radius=0.7, color=RED, stroke_width=2).set_fill(RED, opacity=0.3)
        core_label = ink_txt("core\nengine", size=24, color=RED).next_to(core, RIGHT, buff=0.2)
        self.play(Create(sun_outer), run_time=0.5)
        self.play(Create(core), FadeIn(core_label), run_time=0.5)
        self.wait(dur - 1.0)


class A04_HydrogenNucleiSqueeze(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.37)
        sun_outer = Circle(radius=2.0, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.08)
        core = Circle(radius=0.7, color=RED, stroke_width=2).set_fill(RED, opacity=0.2)
        p1 = Circle(radius=0.25, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.7).shift(LEFT * 0.5)
        p2 = Circle(radius=0.25, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.7).shift(RIGHT * 0.5)
        lp = MathTex(r"p^+", font_size=20, color=INK).move_to(p1)
        rp = MathTex(r"p^+", font_size=20, color=INK).move_to(p2)
        pressure = ink_txt("enormous\npressure", size=22, color=RED).shift(DOWN * 2.2)
        self.add(sun_outer, core)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(lp), FadeIn(rp), run_time=0.5)
        self.play(
            p1.animate.shift(RIGHT * 0.35),
            p2.animate.shift(LEFT * 0.35),
            lp.animate.shift(RIGHT * 0.35),
            rp.animate.shift(LEFT * 0.35),
            run_time=0.8,
        )
        self.play(FadeIn(pressure), run_time=0.4)
        self.wait(dur - 1.7)


class A05_FuseToHelium(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 3.16)
        p1 = Circle(radius=0.28, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.7).shift(LEFT * 1.2)
        p2 = Circle(radius=0.28, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.7).shift(RIGHT * 1.2)
        lp = ink_txt("p⁺", size=18, color=INK).move_to(p1)
        rp = ink_txt("p⁺", size=18, color=INK).move_to(p2)
        he = Circle(radius=0.55, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.5)
        he_label = ink_txt("He", size=28, color=INK)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(lp), FadeIn(rp), run_time=0.5)
        self.play(
            Transform(VGroup(p1, p2, lp, rp), VGroup(he, he_label)),
            run_time=0.8,
        )
        result = ink_txt("helium!", size=32, color=TERRA).shift(RIGHT * 3)
        self.play(FadeIn(result), run_time=0.4)
        self.wait(dur - 1.7)


class A06_FusionEnergy(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 3.37)
        he = Circle(radius=0.55, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.5)
        he_label = ink_txt("He", size=28, color=INK)
        rays = VGroup(*[
            Arrow(ORIGIN, np.array([np.cos(a), np.sin(a), 0]) * 1.6, color=TERRA,
                  stroke_width=3, buff=0.6, max_tip_length_to_length_ratio=0.3)
            for a in np.linspace(0, TAU, 8, endpoint=False)
        ])
        emc2 = ink_txt("E = mc²", size=32, color=TERRA).shift(DOWN * 2.2)
        self.add(he, he_label)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.05), run_time=0.8)
        self.play(FadeIn(emc2), run_time=0.4)
        self.wait(dur - 1.2)


class A07_TwoPositiveNuclei(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 3.29)
        p1 = Circle(radius=0.35, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.6).shift(LEFT * 2)
        p2 = Circle(radius=0.35, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.6).shift(RIGHT * 2)
        plus1 = ink_txt("+", size=32, color=RED).move_to(p1)
        plus2 = ink_txt("+", size=32, color=RED).move_to(p2)
        label = ink_txt("both positive →\nelectrostatic repulsion", size=28, color=RED).shift(DOWN * 2)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(plus1), FadeIn(plus2), run_time=0.7)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.2)


class A08_CoulombBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 3.47)  # A08
        dur = d("A08", 3.47)
        # Coulomb barrier curve
        xs = np.linspace(0.3, 5.0, 200)
        ys = 1.5 / xs  # 1/r Coulomb
        pts = [np.array([x - 2.5, y * 0.8, 0]) for x, y in zip(xs, ys)]
        barrier = VMobject(color=RED, stroke_width=3)
        barrier.set_points_smoothly(pts)
        x_axis = Line(LEFT * 2.5, RIGHT * 3, color=INK, stroke_width=2).shift(DOWN * 0.5)
        x_label = ink_txt("distance", size=22, color=INK).next_to(x_axis.get_end(), RIGHT, buff=0.1)
        y_label = ink_txt("V(r)", size=22, color=RED).shift(LEFT * 3 + UP * 1.5)
        p1 = Dot(color=SLATE, radius=0.2).shift(LEFT * 2 + DOWN * 0.5)
        p2 = Dot(color=SLATE, radius=0.2).shift(RIGHT * 1.5 + DOWN * 0.5)
        label = ink_txt("Coulomb barrier", size=26, color=RED).shift(RIGHT * 2.5 + UP * 1.8)
        self.play(Create(x_axis), FadeIn(x_label), FadeIn(y_label), run_time=0.5)
        self.play(Create(barrier), run_time=0.8)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(label), run_time=0.5)
        self.wait(dur - 1.8)


class A09_ClassicalBounce(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.06)
        xs = np.linspace(0.3, 5.0, 200)
        ys = 1.5 / xs
        pts = [np.array([x - 2.5, y * 0.8, 0]) for x, y in zip(xs, ys)]
        barrier = VMobject(color=RED, stroke_width=3)
        barrier.set_points_smoothly(pts)
        x_axis = Line(LEFT * 2.5, RIGHT * 3, color=INK, stroke_width=2).shift(DOWN * 0.5)
        incoming = Arrow(RIGHT * 2.5, LEFT * 0.3, color=SLATE, stroke_width=4, buff=0,
                         max_tip_length_to_length_ratio=0.2).shift(DOWN * 0.5)
        bounce = Arrow(LEFT * 0.3, RIGHT * 2.5, color=SLATE, stroke_width=4, buff=0,
                       max_tip_length_to_length_ratio=0.2).shift(DOWN * 1.0)
        label = ink_txt("classical: bounce", size=26, color=INK).shift(DOWN * 2.5)
        self.add(x_axis, barrier)
        self.play(GrowArrow(incoming), run_time=0.5)
        self.play(GrowArrow(bounce), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.4)


class A10_TunnelHatch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 2.74)
        xs = np.linspace(0.3, 5.0, 200)
        ys = 1.5 / xs
        pts = [np.array([x - 2.5, y * 0.8, 0]) for x, y in zip(xs, ys)]
        barrier = VMobject(color=RED, stroke_width=3)
        barrier.set_points_smoothly(pts)
        x_axis = Line(LEFT * 2.5, RIGHT * 3, color=INK, stroke_width=2).shift(DOWN * 0.5)
        hatch = DashedLine(LEFT * 0.3, RIGHT * 1.0, color=SLATE, stroke_width=4,
                            dash_length=0.12).shift(DOWN * 0.5)
        hatch_label = ink_txt("quantum\ntunnel", size=22, color=SLATE).next_to(hatch, DOWN, buff=0.1)
        self.add(x_axis, barrier)
        self.play(Create(hatch), FadeIn(hatch_label), run_time=0.7)
        self.wait(dur - 0.7)


class A11_TunnelingPath(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.0)
        xs = np.linspace(0.3, 5.0, 200)
        ys = 1.5 / xs
        pts = [np.array([x - 2.5, y * 0.8, 0]) for x, y in zip(xs, ys)]
        barrier = VMobject(color=RED, stroke_width=3)
        barrier.set_points_smoothly(pts)
        x_axis = Line(LEFT * 2.5, RIGHT * 3, color=INK, stroke_width=2).shift(DOWN * 0.5)
        tunnel_path = DashedLine(LEFT * 1.5 + DOWN * 0.5, RIGHT * 2.0 + DOWN * 0.5,
                                  color=SLATE, stroke_width=4, dash_length=0.15)
        through_dot = Dot(color=TERRA, radius=0.2).shift(RIGHT * 2 + DOWN * 0.5)
        label = ink_txt("tunneled through!", size=26, color=TERRA).shift(DOWN * 2)
        self.add(x_axis, barrier)
        self.play(Create(tunnel_path), run_time=0.7)
        self.play(FadeIn(through_dot), run_time=0.3)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.4)


class A12_TinyChanceOnePair(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 2.64)
        p1 = Dot(color=SLATE, radius=0.2).shift(LEFT * 0.5)
        p2 = Dot(color=SLATE, radius=0.2).shift(RIGHT * 0.5)
        tiny = MathTex(r"\text{tunnel probability} \approx 10^{-40} \text{ per pair}", font_size=28, color=RED).shift(DOWN * 1.5)
        label = ink_txt("one pair:", size=26, color=INK).shift(UP * 1.5)
        self.play(FadeIn(label), FadeIn(p1), FadeIn(p2), run_time=0.6)
        self.play(FadeIn(tiny), run_time=0.5)
        self.wait(dur - 1.1)


class A13_ManyPairsSun(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 2.69)
        sun = Circle(radius=2.2, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.08)
        pairs = VGroup(*[
            VGroup(
                Dot(color=SLATE, radius=0.08).shift(np.array([
                    np.random.uniform(-1.5, 1.5),
                    np.random.uniform(-1.5, 1.5), 0
                ])),
            )
            for _ in range(40)
        ])
        label = MathTex(r"10^{57} \text{ pairs in the Sun}", font_size=26, color=INK).shift(DOWN * 2.8)
        self.play(Create(sun), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(p) for p in pairs], lag_ratio=0.03), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.6)


class A14_SteadyFusion(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 3.53)
        sun = Circle(radius=2.2, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.08)
        glow = Circle(radius=1.5, color=TERRA, stroke_width=0).set_fill(TERRA, opacity=0.35)
        tiny = MathTex(r"\text{tiny} \times 10^{57} =", font_size=30, color=INK).shift(LEFT * 3.5 + UP * 0.5)
        steady = ink_txt("steady fusion!", size=36, color=TERRA).shift(RIGHT * 0.5 + UP * 0.5)
        self.add(sun)
        self.play(FadeIn(glow), run_time=0.6)
        self.play(FadeIn(tiny), FadeIn(steady), run_time=0.7)
        self.wait(dur - 1.3)


class A15_QuantumLeakSunlight(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 2.95)
        sun = Circle(radius=1.5, color=TERRA, stroke_width=4).set_fill(TERRA, opacity=0.15).shift(LEFT * 3)
        # sunlight beam leaking out
        beam = Rectangle(width=4.0, height=0.6, color=TERRA, stroke_width=0).set_fill(TERRA, opacity=0.35).shift(RIGHT * 1.5 + UP * 0.0)
        tunnel_icon = DashedLine(LEFT * 0.5, RIGHT * 0.5, color=SLATE, stroke_width=3,
                                  dash_length=0.1).shift(LEFT * 0.3)
        label = ink_txt("tomorrow's sunlight:\npartly a quantum leak", size=28, color=SLATE).shift(DOWN * 2.3)
        self.play(Create(sun), FadeIn(beam), run_time=0.6)
        self.play(Create(tunnel_icon), run_time=0.4)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.5)
