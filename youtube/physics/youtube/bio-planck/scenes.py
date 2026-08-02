import json
from pathlib import Path
from manim import *
import numpy as np

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', 'Max Planck')
except Exception:
    DUR = {}; TITLE = 'Max Planck'

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class B02_PlanckTitle(Scene):
    def construct(self):
        dur = d('B02', 5)
        self.add(bg())
        name = ink_txt("Max Planck", 56).shift(UP * 1.2)
        dates = ink_txt("1858 – 1947", 32, color=TERRA).shift(UP * 0.1)
        subtitle = ink_txt("A careful physicist who accidentally\nstarted the quantum revolution", 30).shift(DOWN * 1.2)
        subtitle.set_max_width(11)
        self.play(FadeIn(name), run_time=0.8)
        self.play(FadeIn(dates), Write(subtitle), run_time=1.2)
        self.wait(max(0.1, dur - 2.0))


class B03_UVCatastrophe(Scene):
    def construct(self):
        dur = d('B03', 5)
        self.add(bg())
        label = ink_txt("The Ultraviolet Catastrophe", 36).shift(UP * 3.2)
        # Plot: Rayleigh-Jeans vs Planck
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 3, 1],
            x_length=10, y_length=5,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.5 + LEFT * 0.5)
        x_label = ink_txt("frequency ν", 24).next_to(axes, DOWN, buff=0.2)
        y_label = ink_txt("intensity", 24).rotate(PI / 2).next_to(axes, LEFT, buff=0.2)
        # Rayleigh-Jeans: proportional to ν²  (diverges)
        rj_curve = axes.plot(lambda x: 0.5 * x * x, x_range=[0.01, 2.2], color=INK, stroke_width=2.5)
        rj_label = ink_txt("Rayleigh-Jeans\n(classical — diverges!)", 22).move_to(axes.c2p(2.5, 2.5))
        # Planck: has a peak
        def planck(x):
            if x < 0.01:
                return 0
            return 2.0 * x**3 / (np.exp(2.0 * x) - 1)
        planck_curve = axes.plot(planck, x_range=[0.1, 4.8], color=TERRA, stroke_width=3)
        planck_label = terra_txt("Planck (1900)", 22).move_to(axes.c2p(1.5, 1.8))
        self.play(FadeIn(label), Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.8)
        self.play(Create(rj_curve), FadeIn(rj_label), run_time=1.0)
        self.play(Create(planck_curve), FadeIn(planck_label), run_time=1.2)
        self.wait(max(0.1, dur - 3.0))


class B04_PlanckFormula(Scene):
    def construct(self):
        dur = d('B04', 5)
        self.add(bg())
        label = ink_txt("Planck's Quantum Hypothesis", 38).shift(UP * 3.0)
        formula = MathTex(
            r"E = n h \nu \quad (n = 0, 1, 2, \ldots)",
            color=INK, font_size=64
        ).shift(UP * 0.8)
        explain = VGroup(
            ink_txt("h = Planck's constant = 6.626 × 10⁻³⁴ J·s", 26),
            ink_txt("ν = frequency of light", 26),
            terra_txt("Energy comes in discrete packets — quanta", 26),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 1.2)
        self.play(FadeIn(label), Write(formula), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(e) for e in explain], lag_ratio=0.4), run_time=1.5)
        self.wait(max(0.1, dur - 3.0))


class B05_PlanckApplications(Scene):
    def construct(self):
        dur = d('B05', 5)
        self.add(bg())
        label = ink_txt("Planck's constant is everywhere", 38).shift(UP * 3.0)
        apps = [
            ("Transistors", "Quantum tunneling in semiconductor gates"),
            ("Lasers", "Stimulated emission of quantized photons"),
            ("Solar cells", "Photons with E=hν eject electrons"),
            ("LED screens", "Electrons drop levels → emit photons"),
        ]
        items = VGroup(*[
            VGroup(
                terra_txt(app, 28),
                ink_txt(desc, 23).set_max_width(9).shift(DOWN * 0.4)
            ).arrange(DOWN, buff=0.05).shift(DOWN * (i * 1.5 - 1.8))
            for i, (app, desc) in enumerate(apps)
        ])
        self.play(FadeIn(label), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(item) for item in items], lag_ratio=0.35), run_time=dur * 0.75)
        self.wait(max(0.1, dur * 0.25))


class B06_PlanckDates(Scene):
    def construct(self):
        dur = d('B06', 5)
        self.add(bg())
        title = ink_txt("Timeline", 38).shift(UP * 3.2)
        events = [
            ("1900", "Introduced E=nhν to fit blackbody data"),
            ("1905", "Einstein applied it to photoelectric effect"),
            ("1913", "Bohr used quanta to explain atomic spectra"),
            ("1918", "Nobel Prize in Physics"),
        ]
        timeline = VGroup(*[
            VGroup(
                terra_txt(year, 28),
                ink_txt(event, 24).set_max_width(9)
            ).arrange(RIGHT, buff=0.4).shift(DOWN * (i * 1.2 - 1.0))
            for i, (year, event) in enumerate(events)
        ])
        self.play(FadeIn(title), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(row) for row in timeline], lag_ratio=0.3), run_time=dur * 0.75)
        self.wait(max(0.1, dur * 0.25))
