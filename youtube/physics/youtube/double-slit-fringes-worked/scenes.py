import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

CANVAS = "#F8F6F0"
INK_DARK = "#1a1a1a"
ACCENT = "#5A5653"
RED = "#C0392B"

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
    return Rectangle(width=16, height=9).set_fill(CANVAS, 1).set_stroke(width=0)

def ink(t, size=32, color=INK_DARK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def acc(t, size=32, color=ACCENT, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def make_slit_screen():
    """Two slits (barrier) and a screen on the right."""
    barrier_top = Rectangle(width=0.2, height=1.8, color=INK_DARK, fill_opacity=0.9).move_to(LEFT * 1.5 + UP * 2.1)
    barrier_mid = Rectangle(width=0.2, height=1.0, color=INK_DARK, fill_opacity=0.9).move_to(LEFT * 1.5)
    barrier_bot = Rectangle(width=0.2, height=1.8, color=INK_DARK, fill_opacity=0.9).move_to(LEFT * 1.5 + DOWN * 2.1)
    screen = Rectangle(width=0.15, height=5, color=INK_DARK, fill_opacity=0.8).move_to(RIGHT * 4.5)
    return VGroup(barrier_top, barrier_mid, barrier_bot), screen


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 3.9)

        series = acc("Bear's Notes", 28).move_to(UP * 1.5)
        title = ink("The Double Slit: How Far Apart Are the Stripes?", 32).move_to(DOWN * 0.0)
        self.play(Write(series), Write(title), run_time=1.2)
        self.wait(dur - 1.2)


class H01_FringePattern(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 4.91)

        narr = ink("One electron at a time still piles up into stripes.", 26).move_to(UP * 3)
        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        # Faint fringe pattern
        fringe = ParametricFunction(
            lambda t: np.array([4.5 + 1.2 * np.cos(t * PI / 0.55)**2, t, 0]),
            t_range=[-2.2, 2.2], color=ACCENT, stroke_width=2, stroke_opacity=0.5)

        self.play(Write(narr), Create(fringe), run_time=1.0)
        self.wait(dur - 1.0)


class H02_DeltaYBracket(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 3.73)

        barrier, screen = make_slit_screen()
        fringe = ParametricFunction(
            lambda t: np.array([4.5 + 1.2 * np.cos(t * PI / 0.55)**2, t, 0]),
            t_range=[-2.2, 2.2], color=ACCENT, stroke_width=2)
        self.add(barrier, screen, fringe)

        narr = ink("And the spacing of those stripes is predictable.", 26).move_to(UP * 3)

        # Bracket on fringes
        brace = DoubleArrow(RIGHT * 5.3 + UP * 0.55, RIGHT * 5.3 + DOWN * 0.55,
                            color=RED, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.12)
        brace_lbl = MathTex(r"\Delta y", color=RED, font_size=28).next_to(brace, RIGHT, buff=0.2)

        self.play(Write(narr), Create(brace), Write(brace_lbl), run_time=0.8)
        self.wait(dur - 0.8)


class A01_WaveSpreadsFromSlits(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 4.99)

        barrier, screen = make_slit_screen()
        self.play(Create(barrier), Create(screen), run_time=0.5)

        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1

        arcs_a = VGroup(*[
            Arc(radius=0.4 + i * 0.5, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=ACCENT, stroke_width=1.5, stroke_opacity=0.7 - i * 0.08)
            .move_to(slit_a)
            for i in range(6)])
        arcs_b = VGroup(*[
            Arc(radius=0.4 + i * 0.5, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=ACCENT, stroke_width=1.5, stroke_opacity=0.7 - i * 0.08)
            .move_to(slit_b)
            for i in range(6)])

        self.play(Create(arcs_a), Create(arcs_b), run_time=1.0)
        self.wait(dur - 1.5)


class A02_BrightFringePathDiff(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 4.2)

        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1
        bright_pt = RIGHT * 4.5 + UP * 0.55  # first-order bright fringe

        path1 = DashedLine(slit_a, bright_pt, color=RED, stroke_width=2, dash_length=0.15)
        path2 = DashedLine(slit_b, bright_pt, color=ACCENT, stroke_width=2, dash_length=0.15)
        bright_dot = Dot(color=RED, radius=0.12).move_to(bright_pt)

        diff_lbl = MathTex(r"\Delta\ell = \lambda", color=RED, font_size=28).move_to(RIGHT * 2 + DOWN * 1.5)

        self.play(Create(path1), Create(path2), GrowFromCenter(bright_dot), run_time=0.8)
        self.play(Write(diff_lbl), run_time=0.5)
        self.wait(dur - 1.3)


class M01_PinWavelength(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M01", 2.28)

        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        narr = ink("Let's pin the wavelength down.", 26).move_to(UP * 3)
        self.play(Write(narr), run_time=0.5)
        self.wait(dur - 0.5)


class M02_DeBroglieFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M02", 4.65)

        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        eq = MathTex(r"\lambda = \frac{h}{p}", color=ACCENT, font_size=52).move_to(RIGHT * 2.5 + UP * 1.5)
        self.play(Write(eq), run_time=1.0)
        self.wait(dur - 1.0)


class M03_MaximaCondition(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M03", 4.5)

        eq1 = MathTex(r"\lambda = \frac{h}{p}", color=ACCENT, font_size=44).move_to(RIGHT * 2.5 + UP * 2.0)
        self.add(eq1)

        eq2 = MathTex(r"d\sin\theta = m\lambda", color=INK_DARK, font_size=44).move_to(RIGHT * 2.5 + UP * 0.7)
        self.play(Write(eq2), run_time=1.0)
        self.wait(dur - 1.0)


class M04_FringeSpacingResult(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M04", 5.59)

        eq1 = MathTex(r"\lambda = \frac{h}{p}", color=ACCENT, font_size=38).move_to(RIGHT * 2.5 + UP * 2.5)
        eq2 = MathTex(r"d\sin\theta = m\lambda", color=INK_DARK, font_size=38).move_to(RIGHT * 2.5 + UP * 1.5)
        self.add(eq1, eq2)

        result = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=52).move_to(RIGHT * 2.5 + UP * 0.0)
        box = SurroundingRectangle(result, color=ACCENT, stroke_width=2.5, buff=0.3)

        self.play(Write(result), run_time=1.0)
        self.play(Create(box), run_time=0.5)
        self.wait(dur - 1.5)


class W01_HundredVolts(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 3.33)

        result = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=44).move_to(UP * 2.8)
        self.add(result)

        given_lbl = ink("electron accelerated through 100 V", 26).move_to(UP * 1.0)
        self.play(Write(given_lbl), run_time=0.6)
        self.wait(dur - 0.6)


class W02_LambdaComputed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 4.74)

        result = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=40).move_to(UP * 2.8)
        given_lbl = ink("100 V electron", 24).move_to(UP * 2.0)
        self.add(result, given_lbl)

        lambda_eq = MathTex(r"\lambda = \frac{h}{p} \approx 0.12\,\text{nm}", color=ACCENT, font_size=40)
        lambda_eq.move_to(UP * 0.8)
        self.play(Write(lambda_eq), run_time=1.0)
        self.wait(dur - 1.0)


class W03_GeomDandL(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W03", 4.54)

        result = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=38).move_to(UP * 2.8)
        lambda_eq = MathTex(r"\lambda \approx 0.12\,\text{nm}", color=ACCENT, font_size=36).move_to(UP * 2.0)
        self.add(result, lambda_eq)

        # Mark d and L on the geometry
        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        d_brace = DoubleArrow(LEFT * 1.5 + UP * 1.1, LEFT * 1.5 + DOWN * 1.1,
                              color=RED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        d_lbl = MathTex(r"d = 100\,\text{nm}", color=RED, font_size=26).next_to(d_brace, LEFT, buff=0.3)

        L_brace = DoubleArrow(LEFT * 1.5 + DOWN * 2.8, RIGHT * 4.5 + DOWN * 2.8,
                              color=ACCENT, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.05)
        L_lbl = MathTex(r"L = 0.5\,\text{m}", color=ACCENT, font_size=26).next_to(L_brace, DOWN, buff=0.2)

        self.play(Create(d_brace), Write(d_lbl), Create(L_brace), Write(L_lbl), run_time=1.0)
        self.wait(dur - 1.0)


class W04_FringeSpacingAnswer(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W04", 4.82)

        result = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=38).move_to(UP * 2.8)
        self.add(result)

        answer = MathTex(r"\Delta y = \frac{0.12\,\text{nm} \times 0.5\,\text{m}}{100\,\text{nm}} \approx 0.6\,\text{mm}",
                         color=RED, font_size=34).move_to(UP * 0.5)
        self.play(Write(answer), run_time=1.2)

        # Show fringe pattern with bracket
        barrier, screen = make_slit_screen()
        fringe = ParametricFunction(
            lambda t: np.array([4.5 + 1.0 * np.cos(t * PI / 0.55)**2, t, 0]),
            t_range=[-2.2, 2.2], color=ACCENT, stroke_width=2)
        brace = DoubleArrow(RIGHT * 5.3 + UP * 0.55, RIGHT * 5.3 + DOWN * 0.55,
                            color=RED, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.12)
        self.add(barrier, screen, fringe, brace)
        self.wait(dur - 1.2)


class P01_WideVsTight(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P01", 4.61)

        # Two patterns side by side
        # Wide fringes (slow electron, large lambda)
        wide = ParametricFunction(
            lambda t: np.array([-3 + 1.2 * np.cos(t * PI / 0.8)**2, t, 0]),
            t_range=[-2.5, 2.5], color=ACCENT, stroke_width=2)
        wide_lbl = ink("low energy\nwider stripes", 20).move_to(LEFT * 5 + UP * 3.2)

        # Tight fringes (fast electron, small lambda)
        tight = ParametricFunction(
            lambda t: np.array([3 + 1.2 * np.cos(t * PI / 0.35)**2, t, 0]),
            t_range=[-2.5, 2.5], color=RED, stroke_width=2)
        tight_lbl = ink("high energy\ntighter stripes", 20, color=RED).move_to(RIGHT * 1.5 + UP * 3.2)

        self.play(Create(wide), Write(wide_lbl), Create(tight), Write(tight_lbl), run_time=1.0)
        self.wait(dur - 1.0)


class P02_TonomuraDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P02", 6.29)

        barrier, screen = make_slit_screen()
        self.add(barrier, screen)

        narr = ink("Tonomura (1989): dots, one by one, building fringes.", 24).move_to(UP * 3.2)
        self.play(Write(narr), run_time=0.5)

        # Accumulate dots in fringe pattern
        import random
        random.seed(42)

        def fringe_y():
            while True:
                y = random.uniform(-2.3, 2.3)
                p = np.cos(y * PI / 0.55)**2
                if random.random() < p:
                    return y

        dots = VGroup(*[
            Dot(color=INK_DARK, radius=0.04).move_to(RIGHT * 4.5 + UP * fringe_y())
            for _ in range(200)])

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.01), run_time=3.0)
        self.wait(dur - 3.5)


class R01_StripeSpacing(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R01", 4.31)

        formula = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=60).move_to(UP * 0.5)
        box = SurroundingRectangle(formula, color=ACCENT, stroke_width=2.5, buff=0.35)

        self.play(Write(formula), Create(box), run_time=1.2)
        self.wait(dur - 1.2)


class R02_RandomAloneLawfulTogether(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R02", 3.9)

        formula = MathTex(r"\Delta y = \frac{\lambda L}{d}", color=ACCENT, font_size=48).move_to(UP * 1.5)
        self.add(formula)

        recap = ink("Random alone, lawful together — the wave sets the odds.", 26).move_to(ORIGIN)
        self.play(Write(recap), run_time=0.8)
        self.wait(dur - 0.8)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 5.48)

        thanks = ink("Thanks for watching", 28).move_to(UP * 1.5)
        title_lbl = ink("The Double Slit: How Far Apart Are the Stripes?", 22).move_to(UP * 0.5)
        channel = acc("youtube.com/@NikBearBrown", 22).move_to(DOWN * 0.5)

        self.play(Write(thanks), Write(title_lbl), Write(channel), run_time=1.2)
        self.wait(dur - 1.2)
