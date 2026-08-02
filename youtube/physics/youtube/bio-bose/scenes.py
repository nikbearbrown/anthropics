import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', 'S. N. Bose')
except Exception:
    DUR = {}; TITLE = 'S. N. Bose'

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class B02_BoseTitle(Scene):
    def construct(self):
        dur = d('B02', 5)
        self.add(bg())
        name = ink_txt("Satyendra Nath Bose", 52).shift(UP * 1.2)
        dates = ink_txt("1894 – 1974", 32, color=TERRA).shift(UP * 0.1)
        subtitle = ink_txt("Counted light differently\nand changed quantum mechanics forever", 28).shift(DOWN * 1.2)
        subtitle.set_max_width(11)
        self.play(FadeIn(name), run_time=0.8)
        self.play(FadeIn(dates), Write(subtitle), run_time=1.2)
        self.wait(max(0.1, dur - 2.0))


class B03_BoseEinstein(Scene):
    def construct(self):
        dur = d('B03', 5)
        self.add(bg())
        # Bose-Einstein distribution: show particles piling into the same state
        label = ink_txt("Bose-Einstein Statistics", 38).shift(UP * 3.2)
        caption = ink_txt("Identical quantum particles prefer to share the same state", 26).shift(DOWN * 3.2)
        caption.set_max_width(13)
        # Draw boxes representing quantum states
        state_colors = [TERRA if i == 0 else INK for i in range(5)]
        states = VGroup(*[
            VGroup(
                Square(side_length=1.2, color=INK, stroke_width=2).set_fill(CREAM, 1),
                ink_txt(f"state {i+1}", 18)
            ).arrange(DOWN, buff=0.05).shift(LEFT * 3.6 + RIGHT * i * 1.8 + DOWN * 0.3)
            for i in range(5)
        ])
        # Particles: many in state 1, fewer in others
        particle_counts = [6, 2, 1, 1, 0]
        particles = VGroup()
        for i, count in enumerate(particle_counts):
            cx = -3.6 + i * 1.8
            for j in range(count):
                p = Circle(radius=0.18, color=TERRA, fill_color=TERRA, fill_opacity=0.9, stroke_width=1)
                p.move_to([cx, 0.5 + j * 0.42, 0])
                particles.add(p)
        self.play(FadeIn(label), Create(states), run_time=1.0)
        self.play(FadeIn(particles), FadeIn(caption), run_time=1.5)
        self.wait(max(0.1, dur - 2.5))


class B04_BoseFormula(Scene):
    def construct(self):
        dur = d('B04', 5)
        self.add(bg())
        label = ink_txt("Bose-Einstein Distribution", 36).shift(UP * 3.0)
        formula = MathTex(
            r"\bar{n}(\varepsilon) = \frac{1}{e^{(\varepsilon - \mu)/k_B T} - 1}",
            color=INK, font_size=64
        ).shift(UP * 0.5)
        note = ink_txt("Number of particles in a state of energy ε", 26).shift(DOWN * 1.6)
        key = ink_txt("Key: denominator e^x − 1 (bosons pile up at low T)", 24, color=TERRA).shift(DOWN * 2.5)
        key.set_max_width(12)
        self.play(FadeIn(label), Write(formula), run_time=1.5)
        self.play(FadeIn(note), FadeIn(key), run_time=1.0)
        self.wait(max(0.1, dur - 2.5))


class B05_BEC(Scene):
    def construct(self):
        dur = d('B05', 5)
        self.add(bg())
        label = ink_txt("Bose-Einstein Condensate", 38).shift(UP * 3.2)
        subtitle = ink_txt("Near absolute zero, bosons collapse into the same ground state", 26).shift(UP * 2.2)
        subtitle.set_max_width(13)
        # Two panels: warm (spread out) vs cold (all in ground state)
        warm_label = ink_txt("Warm", 28).shift(LEFT * 3.5 + DOWN * 0.3)
        cold_label = terra_txt("Ultra-cold (BEC)", 28).shift(RIGHT * 2.5 + DOWN * 0.3)
        divider = Line(UP * 1.5, DOWN * 2.5, color=INK, stroke_width=1.5)
        # Warm: scattered particles
        warm_dots = VGroup(*[
            Dot(point=[-3.5 + np.random.uniform(-1.5, 1.5), np.random.uniform(-2.5, 1.0), 0],
                radius=0.1, color=INK, fill_opacity=0.6)
            for _ in range(12)
        ])
        # Cold: all clustered together
        cold_dots = VGroup(*[
            Dot(point=[2.5 + np.random.uniform(-0.3, 0.3), -1.5 + np.random.uniform(-0.2, 0.2), 0],
                radius=0.12, color=TERRA, fill_opacity=0.9)
            for _ in range(12)
        ])
        np.random.seed(42)
        self.play(FadeIn(label), FadeIn(subtitle), Create(divider), run_time=0.8)
        self.play(FadeIn(warm_dots), FadeIn(warm_label), FadeIn(cold_dots), FadeIn(cold_label), run_time=1.5)
        self.wait(max(0.1, dur - 2.3))


class B06_BoseDates(Scene):
    def construct(self):
        dur = d('B06', 5)
        self.add(bg())
        events = [
            ("1924", "Mailed paper to Einstein on quantum statistics"),
            ("1924-25", "Einstein extended it → predicted BEC"),
            ("1925", "Paper published in Zeitschrift für Physik"),
            ("1995", "BEC first observed (Cornell & Wieman, Nobel 2001)"),
        ]
        title = ink_txt("Legacy", 38).shift(UP * 3.2)
        timeline = VGroup(*[
            VGroup(
                terra_txt(year, 28),
                ink_txt(event, 24).set_max_width(9)
            ).arrange(RIGHT, buff=0.4).shift(DOWN * (i * 1.2 - 1.0))
            for i, (year, event) in enumerate(events)
        ])
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(row) for row in timeline], lag_ratio=0.3), run_time=dur * 0.7)
        self.wait(max(0.1, dur * 0.3))
