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

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 3.16)
        series = ink_txt("Bear's Notes", size=40)
        title = ink_txt("The Ultraviolet Catastrophe", size=34)
        title.next_to(series, DOWN, buff=0.5)
        grp = VGroup(series, title).move_to(ORIGIN)
        self.play(FadeIn(series), run_time=dur * 0.4)
        self.play(FadeIn(title), run_time=dur * 0.4)
        self.wait(dur * 0.2)


class H01_EverythingGlows(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 6.4)
        # Campfire with glow lines (INK silhouette to avoid TERRA contrast failures)
        fire_body = Triangle(color=INK, fill_opacity=0.85).scale(0.6).shift(ORIGIN)
        fire_body2 = Triangle(color=SLATE, fill_opacity=0.7).scale(0.4).shift(UP * 0.15)
        fire = VGroup(fire_body, fire_body2)

        glow_lines = VGroup(*[
            Line(ORIGIN + UP * 0.5, ORIGIN + UP * 0.5 + (UP * 0.8 + RIGHT * (i - 2) * 0.25),
                 color=INK, stroke_width=2, stroke_opacity=0.5)
            for i in range(5)
        ])

        person = VGroup(
            Circle(radius=0.25, color=INK, fill_opacity=0.6).shift(LEFT * 2.5 + UP * 1.0),
            Line(LEFT * 2.5 + UP * 0.75, LEFT * 2.5 + DOWN * 0.5, color=INK, stroke_width=4),
        )

        label = ink_txt("everything warm glows", size=28)
        label.shift(DOWN * 2.5)

        self.play(Create(fire), Create(person), run_time=dur * 0.35)
        self.play(Create(glow_lines), run_time=dur * 0.35)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class H02_ClassicalPrediction(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 6.5)
        # Classical theory predicts UV blasting toward person
        rays = VGroup(*[
            Arrow(LEFT * 3.5 + UP * (i - 2) * 0.7, LEFT * 0.5 + UP * (i - 2) * 0.4,
                  color=RED_COL, stroke_width=3, buff=0.05)
            for i in range(5)
        ])
        person = VGroup(
            Circle(radius=0.25, color=INK, fill_opacity=0.6).shift(RIGHT * 1.5 + UP * 1.0),
            Line(RIGHT * 1.5 + UP * 0.75, RIGHT * 1.5 + DOWN * 0.5, color=INK, stroke_width=4),
        )
        uv_label = ink_txt("UV rays", size=24, color=RED_COL)
        uv_label.shift(LEFT * 3.8 + UP * 2.5)
        pred_label = ink_txt("classical prediction:\ninfinite UV blast!", size=26, color=RED_COL)
        pred_label.shift(DOWN * 3.0)

        self.play(Create(person), run_time=dur * 0.2)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.1), run_time=dur * 0.4)
        self.play(Write(uv_label), run_time=dur * 0.15)
        self.play(Write(pred_label), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class A02_Axes(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.41)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3)

        self.play(Create(axes), run_time=dur * 0.5)
        self.play(Write(x_label), Write(y_label), run_time=dur * 0.35)
        self.wait(dur * 0.15)


class A03_FewLowFreqWaves(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 4.73)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        # 3 sine arcs near low-frequency end
        waves = VGroup(*[
            ParametricFunction(
                lambda t, n=n: np.array([0.3 + t * 0.25, 0.2 * np.sin(n * t * PI) + 0.3 + n * 0.15, 0]),
                t_range=[0, 1], color=SLATE, stroke_width=3
            )
            for n in [1, 2, 3]
        ])
        # Position them above the low-frequency region of the x-axis
        waves_pos = VGroup(*[
            axes.plot(lambda x, n=n: 0.15 * np.sin(n * x * 2) + 0.4 + n * 0.1,
                      x_range=[0.1, 1.2], color=SLATE, stroke_width=3)
            for n in [1, 2, 3]
        ])
        label = ink_txt("few modes at low frequency", size=22, color=SLATE)
        label.shift(RIGHT * 3.0 + UP * 2.5)

        self.play(LaggedStart(*[Create(w) for w in waves_pos], lag_ratio=0.2), run_time=dur * 0.6)
        self.play(Write(label), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A04_ManyHighFreqWaves(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 4.96)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)

        # Low-freq waves
        low_waves = VGroup(*[
            axes.plot(lambda x, n=n: 0.15 * np.sin(n * x * 2) + 0.4 + n * 0.1,
                      x_range=[0.1, 1.2], color=SLATE, stroke_width=3)
            for n in [1, 2, 3]
        ])
        self.add(axes, x_label, y_label, low_waves)

        # Many more waves packed in at higher frequency
        high_waves = VGroup(*[
            axes.plot(lambda x, n=n: 0.08 * np.sin(n * x * 4) + 0.2,
                      x_range=[1.5 + i * 0.3, 2.2 + i * 0.3], color=SLATE, stroke_width=2, stroke_opacity=0.8)
            for i, n in enumerate(range(3, 12))
        ])

        # f^2 count guide
        count_guide = axes.plot(lambda x: 0.15 * x ** 2,
                                x_range=[0.1, 4.5], color=TERRA, stroke_width=2,
                                stroke_opacity=0.6)
        count_label = ink_txt("count ∝ f²", size=20, color=TERRA)
        count_label.shift(RIGHT * 3.5 + UP * 2.8)

        self.play(LaggedStart(*[Create(w) for w in high_waves], lag_ratio=0.05), run_time=dur * 0.45)
        self.play(Create(count_guide), Write(count_label), run_time=dur * 0.35)
        self.wait(dur * 0.2)


class A05_EqualEnergyBars(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.31)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        # Equal-height energy bars along x-axis
        bars = VGroup(*[
            axes.get_vertical_line(axes.c2p(0.3 + i * 0.4, 0.5), line_func=Line,
                                   color=SLATE, stroke_width=3)
            for i in range(10)
        ])
        equal_label = ink_txt("equal energy per mode\n(equipartition)", size=22)
        equal_label.shift(RIGHT * 3.5 + UP * 2.8)

        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.07), run_time=dur * 0.6)
        self.play(Write(equal_label), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A06_RayleighJeansRunaway(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 5.85)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        # Rayleigh-Jeans: proportional to ν² * kT → diverges
        rj_curve = axes.plot(
            lambda x: 0.12 * x ** 2,
            x_range=[0.1, 5.8], color=RED_COL, stroke_width=5,
            use_smoothing=True
        )
        rj_label = ink_txt("Rayleigh-Jeans:\nB ∝ ν²kT → ∞", size=24, color=RED_COL)
        rj_label.shift(LEFT * 2.5 + UP * 3.0)

        catastrophe = ink_txt("UV CATASTROPHE", size=30, color=RED_COL)
        catastrophe.shift(RIGHT * 1.5 + UP * 3.0)

        self.play(Create(rj_curve), run_time=dur * 0.55)
        self.play(Write(rj_label), run_time=dur * 0.25)
        self.play(Write(catastrophe), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A07_MeasuredCurve(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 5.51)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        # Ghost of Rayleigh-Jeans
        rj_ghost = axes.plot(lambda x: 0.12 * x ** 2, x_range=[0.1, 5.0],
                             color=RED_COL, stroke_width=3, stroke_opacity=0.3)

        # Planck / measured curve: rises, peaks, falls
        def planck(x):
            if x < 0.05:
                return 0
            return (x ** 3) / (np.exp(1.5 * x) - 1) * 0.35

        planck_curve = axes.plot(planck, x_range=[0.1, 5.8], color=SLATE, stroke_width=5)
        planck_label = ink_txt("measured:\nrise, peak, fall", size=24, color=SLATE)
        planck_label.shift(RIGHT * 3.5 + UP * 2.8)

        self.play(FadeIn(rj_ghost), run_time=dur * 0.2)
        self.play(Create(planck_curve), run_time=dur * 0.55)
        self.play(Write(planck_label), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class A08_Staircase(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.86)
        # Smooth ramp (crossed out) vs discrete staircase
        ramp = axes = Line(LEFT * 2.5 + DOWN * 1.5, LEFT * 0.5 + UP * 1.5, color=RED_COL, stroke_width=4)
        cross1 = Line(LEFT * 2.5 + DOWN * 1.5, LEFT * 0.5 + UP * 1.5, color=RED_COL, stroke_width=4)
        cross2 = Line(LEFT * 2.5 + UP * 1.5, LEFT * 0.5 + DOWN * 1.5, color=RED_COL, stroke_width=4)
        ramp_label = ink_txt("continuous", size=22, color=RED_COL)
        ramp_label.shift(LEFT * 2.0 + DOWN * 2.2)

        # Staircase
        stair_steps = VGroup()
        for i in range(5):
            h = Rectangle(width=0.5, height=0.4 * (i + 1), color=SLATE, fill_opacity=0.7)
            h.next_to(RIGHT * (1.0 + i * 0.6) + DOWN * 1.5, UP, buff=0)
            stair_steps.add(h)

        stair_label = ink_txt("quantized\nchunks", size=22, color=SLATE)
        stair_label.shift(RIGHT * 2.5 + DOWN * 2.2)

        e_eq = ink_txt("E = nhν", size=32)
        e_eq.shift(DOWN * 3.3)

        self.play(Create(ramp), run_time=dur * 0.2)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.15)
        self.play(Write(ramp_label), run_time=dur * 0.1)
        self.play(LaggedStart(*[GrowFromEdge(s, DOWN) for s in stair_steps], lag_ratio=0.1),
                  run_time=dur * 0.3)
        self.play(Write(stair_label), run_time=dur * 0.1)
        self.play(Write(e_eq), run_time=dur * 0.1)
        self.wait(dur * 0.05)


class A09_GrowingChunks(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 5.2)
        # Chunks growing taller with frequency; price tag on UV
        num_chunks = 7
        chunks = VGroup()
        for i in range(num_chunks):
            h = 0.3 * (i + 1)
            bar = Rectangle(width=0.55, height=h, color=SLATE, fill_opacity=0.75)
            bar.move_to(RIGHT * (-2.5 + i * 0.9) + DOWN * (1.5 - h / 2))
            chunks.add(bar)

        freq_label = ink_txt("low ν", size=20).shift(LEFT * 2.5 + DOWN * 2.5)
        uv_label = ink_txt("UV (high ν)", size=20, color=RED_COL).shift(RIGHT * 2.5 + DOWN * 2.5)

        # Price tag on tallest chunk
        price_tag = VGroup(
            Rectangle(width=0.9, height=0.45, color=RED_COL, fill_opacity=0.2).shift(RIGHT * 3.2 + UP * 1.2),
            ink_txt("$$", size=20, color=RED_COL).shift(RIGHT * 3.2 + UP * 1.2),
        )

        self.play(LaggedStart(*[GrowFromEdge(c, DOWN) for c in chunks], lag_ratio=0.12),
                  run_time=dur * 0.45)
        self.play(Write(freq_label), Write(uv_label), run_time=dur * 0.2)
        self.play(FadeIn(price_tag), run_time=dur * 0.2)
        self.wait(dur * 0.15)


class A10_HighFreqEmpty(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 4.86)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        # Low-freq arcs (filled/solid)
        low_arcs = VGroup(*[
            axes.plot(lambda x, n=n: 0.12 * np.sin(n * x * 2) + 0.2,
                      x_range=[0.1 + i * 0.25, 0.9 + i * 0.25], color=SLATE, stroke_width=3)
            for i, n in enumerate([1, 2, 3])
        ])

        # High-freq arcs (empty / grey outline)
        high_arcs = VGroup(*[
            axes.plot(lambda x, n=n: 0.06 * np.sin(n * x * 6) + 0.1,
                      x_range=[2.0 + i * 0.45, 2.35 + i * 0.45], color=SLATE,
                      stroke_width=2, stroke_opacity=0.35)
            for i, n in enumerate(range(4, 10))
        ])

        cannot_label = ink_txt("unaffordable →\nstay empty", size=22, color=RED_COL)
        cannot_label.shift(RIGHT * 3.5 + UP * 2.5)

        self.add(low_arcs)
        self.play(LaggedStart(*[Create(a) for a in high_arcs], lag_ratio=0.1), run_time=dur * 0.4)
        self.play(Write(cannot_label), run_time=dur * 0.3)
        self.wait(dur * 0.3)


class A11_PlanckCurveResolves(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 4.6)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)
        x_label = ink_txt("frequency", size=24).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = ink_txt("brightness", size=24).next_to(axes.y_axis, LEFT, buff=0.3)
        self.add(axes, x_label, y_label)

        rj_start = axes.plot(lambda x: 0.12 * x ** 2, x_range=[0.1, 5.0],
                             color=RED_COL, stroke_width=4)

        def planck(x):
            if x < 0.05:
                return 0
            return (x ** 3) / (np.exp(1.5 * x) - 1) * 0.35

        planck_curve = axes.plot(planck, x_range=[0.1, 5.8], color=SLATE, stroke_width=5)

        self.add(rj_start)
        self.play(ReplacementTransform(rj_start, planck_curve), run_time=dur * 0.7)
        label = ink_txt("Planck's law", size=26, color=SLATE)
        label.shift(RIGHT * 3.2 + UP * 2.5)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A12_OneChunkHighlighted(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 5.25)
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4,
            axis_config={"color": INK, "include_tip": True},
        ).shift(LEFT * 0.5 + DOWN * 0.5)

        def planck(x):
            if x < 0.05:
                return 0
            return (x ** 3) / (np.exp(1.5 * x) - 1) * 0.35

        planck_curve = axes.plot(planck, x_range=[0.1, 5.8], color=SLATE, stroke_width=5)
        self.add(axes, planck_curve)

        # Highlight one discrete chunk near the peak
        chunk = Rectangle(width=0.35, height=0.5, color=TERRA, fill_opacity=0.85)
        chunk.move_to(axes.c2p(2.0, 0.25))

        chunk_label = ink_txt("E = hν\n(one quantum)", size=36)
        chunk_label.shift(LEFT * 2.0 + UP * 2.5)
        arrow = Arrow(chunk_label.get_bottom(), chunk.get_top(), color=INK, buff=0.1)

        key_idea = ink_txt("energy in chunks →\nfuse of quantum physics", size=26)
        key_idea.shift(DOWN * 3.2)

        self.play(FadeIn(chunk), run_time=dur * 0.25)
        self.play(Write(chunk_label), GrowArrow(arrow), run_time=dur * 0.35)
        self.play(Write(key_idea), run_time=dur * 0.3)
        self.wait(dur * 0.1)
