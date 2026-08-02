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

def make_wave(sigma=1.0, k0=3.0, x_range=(-5, 5), n=400, y_offset=0.0):
    xs = np.linspace(*x_range, n)
    ys = np.exp(-xs**2 / (2 * sigma**2)) * np.cos(k0 * xs)
    pts = [np.array([x * 0.7, y * 0.7 + y_offset, 0]) for x, y in zip(xs, ys)]
    mob = VMobject(color=SLATE, stroke_width=2.5)
    mob.set_points_smoothly(pts)
    return mob


class A00_MysteryLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 4.13)
        fog = ink_txt("mystery?", size=48, color=SLATE)
        cross = Cross(fog, color=RED, stroke_width=5)
        wave_clue = ink_txt("→ it's just waves", size=36, color=INK).next_to(fog, DOWN, buff=0.6)
        self.play(FadeIn(fog), run_time=0.5)
        self.play(Create(cross), run_time=0.5)
        self.play(FadeIn(wave_clue), run_time=0.5)
        self.wait(dur - 1.5)


class A01_SimpleWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 1.99)
        wave = make_wave(sigma=100, k0=3.0)
        label = ink_txt("waves already know this", size=28, color=INK).shift(DOWN * 2.0)
        self.play(Create(wave), run_time=0.8)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.2)


class A02_LongWaveSpacing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 2.77)
        wave = make_wave(sigma=100, k0=2.5, y_offset=0.5)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        # crest spacing bracket
        # two crests at x = 0 and x = 2pi/k = ~2.5
        k = 2.5; lam = 2 * PI / k
        brace = BraceBetweenPoints(
            np.array([0.0, 0.5, 0]), np.array([lam * 0.7, 0.5, 0]), direction=UP, color=INK
        )
        brace_label = ink_txt("λ — clear", size=24, color=INK).next_to(brace, UP, buff=0.1)
        self.play(Create(x_axis), Create(wave), run_time=0.8)
        self.play(Create(brace), FadeIn(brace_label), run_time=0.5)
        self.wait(dur - 1.3)


class A03_ClearFrequency(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 2.74)
        wave = make_wave(sigma=100, k0=2.5, y_offset=0.3)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        freq_label = ink_txt("clear k (frequency/momentum)", size=26, color=INK).shift(DOWN * 2.0)
        self.add(x_axis, wave)
        self.play(FadeIn(freq_label), run_time=0.5)
        self.wait(dur - 0.5)


class A04_LongWaveSpread(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.11)
        wave = make_wave(sigma=100, k0=2.5, y_offset=0.3)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        spread_brace = Brace(wave, direction=UP, color=RED)
        spread_label = ink_txt("position: spread everywhere", size=26, color=RED).next_to(spread_brace, UP, buff=0.1)
        self.add(x_axis, wave)
        self.play(Create(spread_brace), FadeIn(spread_label), run_time=0.7)
        self.wait(dur - 0.7)


class A05_ShortPulseLocation(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 2.51)
        pulse = make_wave(sigma=0.6, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        brace = BraceBetweenPoints(
            np.array([-0.5, 0.0, 0]), np.array([0.5, 0.0, 0]), direction=UP, color=INK
        )
        brace_label = ink_txt("Δx — small", size=24, color=INK).next_to(brace, UP, buff=0.1)
        self.play(Create(x_axis), Create(pulse), run_time=0.7)
        self.play(Create(brace), FadeIn(brace_label), run_time=0.4)
        self.wait(dur - 1.1)


class A06_AmbiguousSpacing(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 3.34)
        pulse = make_wave(sigma=0.6, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        # multiple possible spacings shown as question marks
        q_marks = VGroup(*[
            ink_txt("?", size=32, color=RED).shift(RIGHT * (i - 1) * 1.2 + DOWN * 0.9)
            for i in range(3)
        ])
        label = ink_txt("crests don't repeat →\nambiguous λ (spacing)", size=26, color=RED).shift(DOWN * 2.3)
        self.add(x_axis, pulse)
        self.play(LaggedStart(*[FadeIn(q) for q in q_marks], lag_ratio=0.2), run_time=0.7)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.2)


class A07_TradeoffArrow(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 2.69)
        sharp_x = ink_txt("sharp x (position)", size=30, color=INK).shift(LEFT * 2.5 + UP * 0.5)
        smear_k = ink_txt("smeared k (frequency)", size=30, color=RED).shift(RIGHT * 2.5 + UP * 0.5)
        arrow = Arrow(sharp_x.get_right(), smear_k.get_left(), color=INK, stroke_width=3, buff=0.1,
                      max_tip_length_to_length_ratio=0.3)
        label = ink_txt("tradeoff — inherent to waves", size=26, color=SLATE).shift(DOWN * 1.5)
        self.play(FadeIn(sharp_x), FadeIn(smear_k), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.4)


class A08_ReverseTradeoff(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 2.4)
        sharp_x = ink_txt("sharp x", size=30, color=INK).shift(LEFT * 2.5 + UP * 0.8)
        smear_k = ink_txt("smeared k", size=30, color=RED).shift(RIGHT * 2.5 + UP * 0.8)
        sharp_k = ink_txt("sharp k", size=30, color=INK).shift(RIGHT * 2.5 + DOWN * 0.3)
        smear_x = ink_txt("smeared x", size=30, color=RED).shift(LEFT * 2.5 + DOWN * 0.3)
        arr1 = Arrow(sharp_x.get_right(), smear_k.get_left(), color=INK, stroke_width=3, buff=0.1,
                     max_tip_length_to_length_ratio=0.3)
        arr2 = Arrow(sharp_k.get_left(), smear_x.get_right(), color=INK, stroke_width=3, buff=0.1,
                     max_tip_length_to_length_ratio=0.3)
        self.play(FadeIn(sharp_x), FadeIn(smear_k), GrowArrow(arr1), run_time=0.5)
        self.play(FadeIn(sharp_k), FadeIn(smear_x), GrowArrow(arr2), run_time=0.5)
        self.wait(dur - 1.0)


class A09_ParticleWavePacket(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.19)
        packet = make_wave(sigma=1.0, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        particle_dot = Dot(color=TERRA, radius=0.18)
        label = ink_txt("quantum particle = wave packet", size=28, color=SLATE).shift(DOWN * 2.2)
        self.play(Create(x_axis), Create(packet), run_time=0.8)
        self.play(FadeIn(particle_dot), run_time=0.3)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.5)


class A10_PositionBracket(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 2.74)
        packet = make_wave(sigma=1.0, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        brace = BraceBetweenPoints(
            np.array([-0.7, 0.0, 0]), np.array([0.7, 0.0, 0]), direction=UP, color=INK
        )
        pos_label = ink_txt("Δx (position)", size=26, color=INK).next_to(brace, UP, buff=0.1)
        self.add(x_axis, packet)
        self.play(Create(brace), FadeIn(pos_label), run_time=0.6)
        self.wait(dur - 0.6)


class A11_MomentumFrequency(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.42)
        packet = make_wave(sigma=1.0, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        brace_x = BraceBetweenPoints(
            np.array([-0.7, 0.0, 0]), np.array([0.7, 0.0, 0]), direction=UP, color=INK
        )
        pos_label = ink_txt("Δx", size=22, color=INK).next_to(brace_x, UP, buff=0.05)
        # k-space bar
        k_bar = Line(LEFT * 1.5 + DOWN * 2.0, RIGHT * 1.5 + DOWN * 2.0, color=RED, stroke_width=4)
        k_label = ink_txt("Δk → Δp = ℏΔk (momentum)", size=24, color=RED).next_to(k_bar, DOWN, buff=0.1)
        self.add(x_axis, packet, brace_x, pos_label)
        self.play(Create(k_bar), FadeIn(k_label), run_time=0.7)
        self.wait(dur - 0.7)


class A12_NarrowPacketManyFreq(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 3.11)
        # narrow packet
        narrow = make_wave(sigma=0.4, k0=3.0)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        # frequency components below
        components = VGroup(*[
            make_wave(sigma=100, k0=2.0 + i * 0.8, y_offset=-1.0 - i * 0.5)
            for i in range(3)
        ])
        label = ink_txt("narrow x → many k needed", size=26, color=RED).shift(DOWN * 2.8)
        self.play(Create(x_axis), Create(narrow), run_time=0.6)
        self.play(LaggedStart(*[Create(c) for c in components], lag_ratio=0.2), run_time=0.8)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.8)


class A13_ManyMomenta(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 2.74)
        ks = [2.0, 2.5, 3.0, 3.5, 4.0]
        arrows = VGroup(*[
            Arrow(ORIGIN, RIGHT * k * 0.4, color=SLATE, stroke_width=3, buff=0,
                  max_tip_length_to_length_ratio=0.25).shift(UP * (i - 2) * 0.7)
            for i, k in enumerate(ks)
        ])
        label = ink_txt("many k → many possible p", size=28, color=RED).shift(DOWN * 2.2)
        dp_label = ink_txt("Δp large", size=30, color=RED).shift(RIGHT * 3.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), run_time=0.8)
        self.play(FadeIn(label), FadeIn(dp_label), run_time=0.5)
        self.wait(dur - 1.3)


class A14_UncertaintySummary(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 2.64)
        formula = ink_txt("Δx · Δp ≥ ℏ/2", size=48, color=INK)
        subtitle = ink_txt("wave bookkeeping", size=30, color=SLATE).next_to(formula, DOWN, buff=0.4)
        self.play(FadeIn(formula), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(dur - 1.2)


class A15_NotInvented(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 2.82)
        formula = ink_txt("Δx · Δp ≥ ℏ/2", size=44, color=INK).shift(UP * 0.8)
        not_invented = ink_txt("quantum did not invent this\n— waves had it first", size=26, color=SLATE).shift(DOWN * 0.5)
        self.add(formula)
        self.play(FadeIn(not_invented), run_time=0.7)
        self.wait(dur - 0.7)


class A16_UnavoidableForParticles(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A16", 2.59)
        formula = ink_txt("Δx · Δp ≥ ℏ/2", size=44, color=INK).shift(UP * 0.8)
        unavoidable = ink_txt("quantum made it unavoidable\nfor particles — no escape", size=28, color=RED).shift(DOWN * 0.5)
        self.add(formula)
        self.play(FadeIn(unavoidable), run_time=0.7)
        self.wait(dur - 0.7)
