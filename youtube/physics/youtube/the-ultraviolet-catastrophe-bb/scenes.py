import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

DARK_BG = "#1a1a1a"
BLUE = "#58C4DD"
BROWN = "#CD853F"
HIGHLIGHT = "#F0E442"
VIOLET = "#8833AA"

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
    return Rectangle(width=16, height=9).set_fill(DARK_BG, 1).set_stroke(width=0)

def light_txt(t, size=36, **kw):
    return Text(t, font=FONT, font_size=size, color="#E0DDD5", **kw)


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 2.32)
        series = Text("Bear's Notes", font=FONT, font_size=28, color=BROWN).move_to(UP * 1.2)
        title = Text("The Ultraviolet Catastrophe", font=FONT, font_size=48, color="#E0DDD5").move_to(DOWN * 0.2)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=BROWN, stroke_width=1.5).move_to(DOWN * 0.9)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 4.7 + DOWN * 0.9)
        self.play(FadeIn(series), Write(title), run_time=0.9)
        self.play(Create(rule), FadeIn(tick), run_time=0.6)
        self.wait(dur - 1.5)


class H01_GlowingObject(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 4.78)

        obj = Circle(radius=0.8, color="#333333", fill_opacity=1).move_to(ORIGIN)
        self.play(GrowFromCenter(obj), run_time=0.4)

        # Warming from dark to blue-hot
        def warm_color(t):
            # t from 0 to 1: dark orange to white-blue
            r = int(50 + 180 * t)
            g = int(30 + 130 * t)
            b = int(20 + 220 * t)
            return f"#{r:02x}{g:02x}{b:02x}"

        # Glow rays
        rays = VGroup(*[
            Line(ORIGIN, (np.cos(a) * 1.4) * RIGHT + (np.sin(a) * 1.4) * UP,
                 color=BLUE, stroke_width=1.5, stroke_opacity=0.5)
            for a in np.linspace(0, TAU, 12, endpoint=False)])

        self.play(
            obj.animate.set_fill(BLUE, 0.8).set_stroke(BLUE, 2),
            Create(rays),
            run_time=1.5)
        self.wait(dur - 1.9)


class H02_InfiniteGlow(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 3.16)

        obj = Circle(radius=0.8, color=BLUE, fill_opacity=0.8).move_to(ORIGIN)
        rays = VGroup(*[
            Line(ORIGIN, (np.cos(a) * 1.4) * RIGHT + (np.sin(a) * 1.4) * UP,
                 color=BLUE, stroke_width=1.5, stroke_opacity=0.5)
            for a in np.linspace(0, TAU, 12, endpoint=False)])
        self.add(obj, rays)

        # Rays shoot to edges of frame
        self.play(rays.animate.scale(5, about_point=ORIGIN).set_opacity(0.2), run_time=0.8)

        infinite_lbl = Text("infinite", font=FONT, font_size=52, color=HIGHLIGHT).move_to(UP * 2)
        self.play(Write(infinite_lbl), run_time=0.5)
        self.play(FadeOut(infinite_lbl), run_time=0.4)
        self.wait(dur - 1.7)


class H03_RoomWithVioletRays(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H03", 4.68)

        # Room outline
        room = Square(side_length=4, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        figure = Dot(color="#E0DDD5", radius=0.2).move_to(ORIGIN)

        # Violet arrows from walls inward
        violet_arrows = VGroup(
            Arrow(LEFT * 2 + UP * 0.5, LEFT * 0.5 + UP * 0.2, color=VIOLET, buff=0),
            Arrow(LEFT * 2 + DOWN * 0.5, LEFT * 0.5 + DOWN * 0.2, color=VIOLET, buff=0),
            Arrow(RIGHT * 2 + UP * 0.5, RIGHT * 0.5 + UP * 0.2, color=VIOLET, buff=0),
            Arrow(RIGHT * 2 + DOWN * 0.5, RIGHT * 0.5 + DOWN * 0.2, color=VIOLET, buff=0),
            Arrow(UP * 2 + LEFT * 0.3, UP * 0.5 + LEFT * 0.1, color=VIOLET, buff=0),
            Arrow(DOWN * 2 + RIGHT * 0.3, DOWN * 0.5 + RIGHT * 0.1, color=VIOLET, buff=0),
        )

        self.play(Create(room), GrowFromCenter(figure), run_time=0.6)
        self.play(Create(violet_arrows), run_time=0.8)
        self.wait(dur - 1.4)


class H04_QuestionMark(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H04", 4.83)

        room = Square(side_length=4, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        figure = Dot(color="#E0DDD5", radius=0.2).move_to(ORIGIN)
        self.add(room, figure)

        question = Text("?", font=FONT, font_size=72, color=HIGHLIGHT).move_to(RIGHT * 3.5 + UP * 2)
        self.play(FadeIn(question), run_time=0.4)
        self.play(Indicate(question, color=HIGHLIGHT, scale_factor=1.2), run_time=0.6)
        self.wait(dur - 1.0)


class M01_CavityStandingWave(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M01", 4.13)

        box = Rectangle(width=5, height=2.5, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        self.play(Create(box), run_time=0.5)

        t = ValueTracker(0)
        wave = always_redraw(lambda: ParametricFunction(
            lambda x: np.array([x * 2.3, 0.6 * np.sin(PI * (x + 1) / 2) * np.cos(t.get_value()), 0]),
            t_range=[-1, 1], color=BLUE, stroke_width=3))

        self.add(wave)
        self.play(t.animate.set_value(TAU * 2), run_time=dur - 0.5, rate_func=linear)


class M02_FewLowModes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M02", 3.79)

        box = Rectangle(width=5, height=2.5, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        self.add(box)

        modes = VGroup(*[
            ParametricFunction(
                lambda x, n=n: np.array([x * 2.3, (0.5 - n * 0.1) * np.sin(n * PI * (x + 1) / 2), 0]),
                t_range=[-1, 1], color=BLUE, stroke_width=2.5, stroke_opacity=0.8 - n * 0.1)
            .shift(UP * (1.0 - n * 0.8))
            for n in range(1, 4)])

        count = Text("3", font="Courier New", font_size=28, color=INK).move_to(RIGHT * 4 + UP * 3)

        self.play(Create(modes[0]), run_time=0.3)
        self.play(Create(modes[1]), run_time=0.3)
        self.play(Create(modes[2]), FadeIn(count), run_time=0.3)
        self.wait(dur - 0.9)


class M03_ManyHighModes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M03", 5.04)

        box = Rectangle(width=5, height=2.5, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        self.add(box)

        # Many tightly packed modes
        modes = VGroup(*[
            ParametricFunction(
                lambda x, n=n: np.array([x * 2.3, 0.2 * np.sin(n * PI * (x + 1) / 2), 0]),
                t_range=[-1, 1], color=BLUE, stroke_width=1.5, stroke_opacity=0.6)
            .shift(UP * (1.0 - n * 0.25))
            for n in range(1, 12)])

        count_tracker = ValueTracker(3)
        count = always_redraw(lambda: Text(
            str(int(count_tracker.get_value())),
            font="Courier New", font_size=28, color=INK).move_to(RIGHT * 4 + UP * 3))

        self.add(count)
        self.play(LaggedStart(*[Create(m) for m in modes], lag_ratio=0.05), run_time=1.5)
        self.play(count_tracker.animate.set_value(121), run_time=1.5, rate_func=rate_functions.ease_in_quad)
        self.wait(dur - 3.0)


class M04_EquipartitionTokens(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M04", 4.21)

        box = Rectangle(width=5, height=2.5, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        self.add(box)

        # Modes with tokens
        modes = VGroup(*[
            Line(LEFT * 2.4 + UP * (0.9 - n * 0.3), RIGHT * 2.4 + UP * (0.9 - n * 0.3),
                 color=BLUE, stroke_width=2, stroke_opacity=0.7)
            for n in range(6)])
        self.add(modes)

        # Equal energy tokens (kT coins)
        tokens = VGroup(*[
            Circle(radius=0.15, color=HIGHLIGHT, fill_opacity=0.8)
            .move_to(RIGHT * 3.2 + UP * (0.9 - n * 0.3))
            for n in range(6)])

        self.play(LaggedStart(*[FadeIn(t) for t in tokens], lag_ratio=0.1), run_time=1.0)
        lbl = Text("same share", font=FONT, font_size=24, color=INK).move_to(DOWN * 2)
        self.play(Write(lbl), run_time=0.5)
        self.wait(dur - 1.5)


class M05_DenseModesFunded(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M05", 4.6)

        box = Rectangle(width=5, height=2.5, color="#E0DDD5", stroke_width=2).move_to(ORIGIN)
        modes = VGroup(*[
            Line(LEFT * 2.4 + UP * (1.1 - n * 0.22), RIGHT * 2.4 + UP * (1.1 - n * 0.22),
                 color=BLUE, stroke_width=1.5, stroke_opacity=0.6)
            for n in range(10)])
        tokens = VGroup(*[
            Circle(radius=0.1, color=HIGHLIGHT, fill_opacity=0.8)
            .move_to(RIGHT * 2.7 + UP * (1.1 - n * 0.22))
            for n in range(10)])
        self.add(box, modes, tokens)

        # Highlight sweeps
        sweep = Rectangle(width=6, height=0.15, color=HIGHLIGHT, fill_opacity=0.3, stroke_width=0)
        sweep.move_to(UP * 1.2)
        self.play(sweep.animate.move_to(DOWN * 1.2), run_time=1.5, rate_func=linear)
        self.wait(dur - 1.5)


class P01_AxesAndRunawayStart(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P01", 4.78)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)

        x_lbl = Text("frequency →", font=FONT, font_size=22, color="#E0DDD5").next_to(axes, DOWN, buff=0.3)
        y_lbl = Text("brightness", font=FONT, font_size=22, color="#E0DDD5").next_to(axes, LEFT, buff=0.2)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=1.0)

        # Rayleigh-Jeans starts
        rj_partial = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 3],
                               color=BLUE, stroke_width=3)
        self.play(Create(rj_partial), run_time=1.0)
        self.wait(dur - 2.0)


class P02_RunawayToUV(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P02", 4.18)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)
        x_lbl = Text("frequency →", font=FONT, font_size=22, color="#E0DDD5").next_to(axes, DOWN, buff=0.3)
        self.add(axes, x_lbl)

        # Full runaway curve
        rj_full = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10],
                            color=BLUE, stroke_width=3)

        # UV band at right
        uv_rect = Rectangle(width=1.5, height=5.2, color=VIOLET, fill_opacity=0.2, stroke_width=0)
        uv_rect.align_to(axes, RIGHT).align_to(axes, DOWN).shift(UP * 0.05)
        uv_lbl = Text("UV", font=FONT, font_size=20, color=VIOLET).move_to(uv_rect.get_top() + UP * 0.3)

        self.play(Create(rj_full), FadeIn(uv_rect), FadeIn(uv_lbl), run_time=1.5)
        self.wait(dur - 1.5)


class P03_RealHump(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P03", 4.68)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)
        rj_full = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10], color=BLUE, stroke_width=2)

        # Planck/real hump: B(nu) ~ nu^3 / (exp(nu/nu0) - 1)
        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        planck_curve = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=3)

        self.add(axes, rj_full)
        self.play(Create(planck_curve), run_time=1.2)
        self.wait(dur - 1.2)


class P04_TwoCurvesLabelled(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P04", 4.86)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)

        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        rj = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10], color=BLUE, stroke_width=2)
        planck_c = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=3)
        self.add(axes, rj, planck_c)

        lbl_cl = Text("classical", font=FONT, font_size=22, color=BLUE).move_to(RIGHT * 4 + UP * 3)
        lbl_re = Text("reality", font=FONT, font_size=22, color=BROWN).move_to(RIGHT * 1 + UP * 2)

        self.play(Write(lbl_cl), Write(lbl_re), run_time=0.8)
        self.wait(dur - 0.8)


class D01_ThreeStepCards(Scene):
    def construct(self):
        self.add(bg())
        dur = d("D01", 3.58)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=5, y_length=3.5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 2.5 + DOWN * 0.5)

        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        rj = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10], color=BLUE, stroke_width=1.5)
        planck_c = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=2)
        self.add(axes, rj, planck_c)

        cards = VGroup(
            Text("count modes", font=FONT, font_size=22, color="#E0DDD5"),
            Text("equal share", font=FONT, font_size=22, color="#E0DDD5"),
            Text("any energy", font=FONT, font_size=22, color="#E0DDD5"),
        ).arrange(DOWN, buff=0.4).move_to(RIGHT * 4)

        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.2), run_time=0.8)
        self.wait(dur - 0.8)


class D02_CountingChecked(Scene):
    def construct(self):
        self.add(bg())
        dur = d("D02", 4.41)

        cards = VGroup(
            Text("count modes", font=FONT, font_size=22, color="#E0DDD5"),
            Text("equal share", font=FONT, font_size=22, color="#E0DDD5"),
            Text("any energy", font=FONT, font_size=22, color="#E0DDD5"),
        ).arrange(DOWN, buff=0.4).move_to(RIGHT * 4)
        self.add(cards)

        check = Text("✓", font=FONT, font_size=28, color="#88CC88").next_to(cards[0], LEFT, buff=0.3)
        self.play(FadeIn(check), run_time=0.4)
        self.play(cards[0].animate.set_opacity(0.3), run_time=0.5)
        self.wait(dur - 0.9)


class D03_AnyEnergyCulprit(Scene):
    def construct(self):
        self.add(bg())
        dur = d("D03", 4.96)

        cards = VGroup(
            Text("count modes", font=FONT, font_size=22, color="#E0DDD5", fill_opacity=0.3),
            Text("equal share", font=FONT, font_size=22, color="#E0DDD5"),
            Text("any energy", font=FONT, font_size=22, color=HIGHLIGHT),
        ).arrange(DOWN, buff=0.4).move_to(RIGHT * 4)
        self.add(cards)

        # Continuous slider
        slider_track = Line(RIGHT * 0.5 + DOWN * 1.5, RIGHT * 2.5 + DOWN * 1.5, color="#E0DDD5", stroke_width=2)
        slider_dot = Dot(color=HIGHLIGHT, radius=0.12).move_to(RIGHT * 0.5 + DOWN * 1.5)

        self.play(FadeIn(cards[2]), Create(slider_track), GrowFromCenter(slider_dot), run_time=0.6)
        self.play(slider_dot.animate.move_to(RIGHT * 2.5 + DOWN * 1.5), run_time=0.8)
        self.play(slider_dot.animate.move_to(RIGHT * 1.2 + DOWN * 1.5), run_time=0.5)
        self.wait(dur - 1.9)


class F01_DiscreteLadder(Scene):
    def construct(self):
        self.add(bg())
        dur = d("F01", 4.21)

        # Continuous slider → discrete ladder
        slider_track = Line(RIGHT * 0.5 + DOWN * 1.5, RIGHT * 2.5 + DOWN * 1.5, color="#E0DDD5", stroke_width=2)
        slider_dot = Dot(color=HIGHLIGHT, radius=0.12).move_to(RIGHT * 1.0 + DOWN * 1.5)
        self.add(slider_track, slider_dot)

        # Discrete rungs
        rungs = VGroup(*[
            Line(LEFT * 0.5 + DOWN * (1.0 - n * 0.6), RIGHT * 0.5 + DOWN * (1.0 - n * 0.6),
                 color=BLUE, stroke_width=3)
            for n in range(6)])

        lbl = Text("0", font="Courier New", font_size=18, color=INK).next_to(rungs[-1], LEFT, buff=0.2)

        self.play(
            ReplacementTransform(VGroup(slider_track, slider_dot), rungs),
            run_time=1.2)
        self.play(FadeIn(lbl), run_time=0.3)
        self.wait(dur - 1.5)


class F02_ChunkLabelEhnu(Scene):
    def construct(self):
        self.add(bg())
        dur = d("F02", 6.16)

        rungs = VGroup(*[
            Line(LEFT * 0.5 + DOWN * (1.0 - n * 0.6), RIGHT * 0.5 + DOWN * (1.0 - n * 0.6),
                 color=BLUE, stroke_width=3)
            for n in range(6)])
        self.add(rungs)

        # Bracket one gap
        brace = BraceBetweenPoints(rungs[0].get_center(), rungs[1].get_center(), direction=RIGHT)
        eq = MathTex(r"E = h\nu", color=HIGHLIGHT, font_size=40).next_to(brace, RIGHT, buff=0.2)

        self.play(Create(brace), Write(eq), run_time=1.2)
        self.wait(dur - 1.2)


class F03_LowFreqAgreement(Scene):
    def construct(self):
        self.add(bg())
        dur = d("F03", 4.78)

        # Axes with both curves
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)

        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        rj = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10], color=BLUE, stroke_width=2)
        planck_c = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=2)
        self.add(axes, rj, planck_c)

        # Fine ladder (left, low freq)
        fine_rung = VGroup(*[
            Line(LEFT * 0.8 + UP * (1.0 - n * 0.15), LEFT * 0.5 + UP * (1.0 - n * 0.15),
                 color=BLUE, stroke_width=2)
            for n in range(8)])
        self.add(fine_rung)

        # Flash agreement region
        agree_rect = Rectangle(width=1.5, height=5, color=HIGHLIGHT, fill_opacity=0.15, stroke_width=0)
        agree_rect.align_to(axes, LEFT).align_to(axes, DOWN).shift(UP * 0.05, RIGHT * 0.05)
        self.play(FadeIn(agree_rect), run_time=0.5)
        self.play(FadeOut(agree_rect), run_time=0.5)
        self.wait(dur - 1.0)


class F04_HighFreqExpensive(Scene):
    def construct(self):
        self.add(bg())
        dur = d("F04", 5.04)

        # Wide ladder (high freq)
        wide_rungs = VGroup(*[
            Line(LEFT * 0.5 + UP * (1.0 - n * 1.2), RIGHT * 0.5 + UP * (1.0 - n * 1.2),
                 color=BLUE, stroke_width=3)
            for n in range(4)])
        self.add(wide_rungs)

        # Price tag on lowest UV rung
        uv_lbl = Text("UV", font=FONT, font_size=24, color=VIOLET).next_to(wide_rungs[0], RIGHT, buff=0.3)
        price_tag = Text("$$$", font=FONT, font_size=26, color=HIGHLIGHT).next_to(wide_rungs[0], RIGHT, buff=1.0)

        uv_band = Rectangle(width=0.3, height=0.1, color=VIOLET, fill_opacity=0.4, stroke_width=0)
        uv_band.move_to(wide_rungs[0].get_center())

        self.play(FadeIn(wide_rungs), run_time=0.5)
        self.play(FadeIn(uv_lbl), FadeIn(price_tag), run_time=0.6)
        self.wait(dur - 1.1)


class Y01_CantAffordUV(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y01", 4.36)

        wide_rungs = VGroup(*[
            Line(LEFT * 0.5 + UP * (1.0 - n * 1.2), RIGHT * 0.5 + UP * (1.0 - n * 1.2),
                 color=BLUE, stroke_width=3)
            for n in range(4)])
        uv_lbl = Text("UV", font=FONT, font_size=24, color=VIOLET).next_to(wide_rungs[0], RIGHT, buff=0.3)
        self.add(wide_rungs, uv_lbl)

        # Thermal budget bar falls short
        budget = Rectangle(width=0.4, height=0.8, color=BROWN, fill_opacity=0.8)
        budget.align_to(wide_rungs[-1], DOWN).move_to(LEFT * 1 + DOWN * 0.5)
        budget_lbl = Text("thermal\nbudget", font=FONT, font_size=18, color=BROWN).next_to(budget, LEFT, buff=0.2)

        self.play(GrowFromEdge(budget, DOWN), FadeIn(budget_lbl), run_time=0.8)
        # Budget can't reach UV rung
        self.play(budget.animate.set_color("#888888"), wide_rungs[0].animate.set_opacity(0.2), run_time=0.6)
        self.wait(dur - 1.4)


class Y02_RunawayMorphsToHump(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y02", 5.02)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)

        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        rj = axes.plot(lambda x: 0.08 * x**2, x_range=[0, 10], color=BLUE, stroke_width=3)
        planck_c = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=3)
        self.add(axes, planck_c, rj)

        self.play(Transform(rj, planck_c), run_time=2.0)
        self.wait(dur - 2.0)


class Y03_OneCleanHump(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y03", 4.44)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 8, 2],
            x_length=7, y_length=5,
            axis_config={"color": "#E0DDD5", "include_ticks": False},
            tips=True).move_to(LEFT * 1 + DOWN * 0.5)

        nu0 = 3.5
        def planck(x):
            if x < 0.01: return 0
            return 2.5 * x**3 / (np.exp(x / nu0) - 1 + 1e-9)

        planck_c = axes.plot(planck, x_range=[0.1, 10], color=BROWN, stroke_width=3)
        self.add(axes, planck_c)
        self.wait(dur)


class S01_RatioWidget(Scene):
    def construct(self):
        self.add(bg())
        dur = d("S01", 4.26)

        ratio = MathTex(r"\frac{h\nu}{k_B T}", color="#E0DDD5", font_size=64).move_to(ORIGIN)
        top_lbl = Text("chunk cost", font=FONT, font_size=22, color=HIGHLIGHT).move_to(UP * 1.5)
        bot_lbl = Text("warmth", font=FONT, font_size=22, color=BROWN).move_to(DOWN * 1.5)

        self.play(Write(ratio), run_time=1.0)
        self.play(FadeIn(top_lbl), FadeIn(bot_lbl), run_time=0.6)
        self.wait(dur - 1.6)


class S02_TwoRegimes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("S02", 5.25)

        ratio = MathTex(r"\frac{h\nu}{k_B T}", color="#E0DDD5", font_size=52).move_to(UP * 1.5)
        self.add(ratio)

        axis = NumberLine(x_range=[0, 10, 2], length=8, color="#E0DDD5",
                          include_ticks=False).move_to(DOWN * 0.5)
        cl_lbl = Text("classical", font=FONT, font_size=24, color=BLUE).move_to(LEFT * 3 + DOWN * 1.3)
        q_lbl = Text("quantum", font=FONT, font_size=24, color=HIGHLIGHT).move_to(RIGHT * 3 + DOWN * 1.3)

        marker = Triangle(color=HIGHLIGHT, fill_opacity=0.9).scale(0.2)
        marker.move_to(axis.n2p(1) + DOWN * 0.3)

        self.play(Create(axis), Write(cl_lbl), Write(q_lbl), run_time=0.8)
        self.play(GrowFromCenter(marker), run_time=0.3)
        self.play(marker.animate.move_to(axis.n2p(9) + DOWN * 0.3), run_time=1.2)
        self.play(marker.animate.move_to(axis.n2p(1) + DOWN * 0.3), run_time=1.0)
        self.wait(dur - 3.3)


class B01_CloseCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B01", 4.96)

        eq = MathTex(r"E = h\nu", color="#E0DDD5", font_size=60).move_to(UP * 0.5)

        # Ladder icon below
        rungs = VGroup(*[
            Line(LEFT * 0.8 + DOWN * (1.0 + n * 0.4), RIGHT * 0.8 + DOWN * (1.0 + n * 0.4),
                 color=BLUE, stroke_width=2.5)
            for n in range(4)])

        self.play(Write(eq), run_time=1.0)
        self.play(Create(rungs), run_time=0.6)
        self.wait(dur - 1.6)


class B02_DeferredTags(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B02", 5.25)

        eq = MathTex(r"E = h\nu", color="#E0DDD5", font_size=52).move_to(UP * 1.5)
        self.add(eq)

        tag1 = Text("coming next · Planck's formula", font=FONT, font_size=22, color="#888888").move_to(ORIGIN)
        tag2 = Text("coming next · the photon", font=FONT, font_size=22, color="#888888").move_to(DOWN * 0.7)

        self.play(LaggedStart(FadeIn(tag1), FadeIn(tag2), lag_ratio=0.4), run_time=0.8)
        self.wait(dur - 0.8)


class B03_Exercise(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B03", 6.09)

        eq = MathTex(r"E = h\nu", color="#E0DDD5", font_size=44).move_to(UP * 2.5)
        self.add(eq)

        exercise = Text(
            "Estimate E = hν for green light (550 nm).\nCompare to kT at room temperature.",
            font=FONT, font_size=26, color=HIGHLIGHT, line_spacing=1.4).move_to(ORIGIN)

        self.play(Write(exercise), run_time=1.5)
        self.wait(dur - 1.5)
