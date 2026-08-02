import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

# Brown Blue palette
DARK_BG = "#1a1a1a"
BLUE = "#58C4DD"
BROWN = "#CD853F"
HIGHLIGHT = "#F0E442"

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

def make_apparatus():
    """Return (gun, barrier, screen) as separate mobjects."""
    gun = Rectangle(width=0.6, height=1.0, color="#888888", fill_opacity=0.9).move_to(LEFT * 5.5)
    gun_nozzle = Rectangle(width=0.3, height=0.2, color="#888888", fill_opacity=0.9)
    gun_nozzle.next_to(gun, RIGHT, buff=0)

    # barrier: top segment, gap, middle segment, gap, bottom segment
    barrier_top = Rectangle(width=0.2, height=1.8, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5 + UP * 2.2)
    barrier_mid = Rectangle(width=0.2, height=1.0, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5)
    barrier_bot = Rectangle(width=0.2, height=1.8, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5 + DOWN * 2.2)
    barrier = VGroup(barrier_top, barrier_mid, barrier_bot)

    screen = Rectangle(width=0.15, height=5, color="#E0DDD5", fill_opacity=0.8).move_to(RIGHT * 4.5)

    return VGroup(gun, gun_nozzle), barrier, screen


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 3.46)
        series = Text("Bear's Notes", font=FONT, font_size=28, color=BROWN).move_to(UP * 1.2)
        title = Text("One Electron Interferes With Itself",
                     font=FONT, font_size=44, color="#E0DDD5").move_to(DOWN * 0.2)
        rule = Line(LEFT * 4, RIGHT * 4, color=BROWN, stroke_width=1.5).move_to(DOWN * 0.9)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 4.2 + DOWN * 0.9)
        self.play(FadeIn(series), run_time=0.4)
        self.play(Write(title), run_time=1.2)
        self.play(Create(rule), FadeIn(tick), run_time=0.7)
        self.wait(dur - 2.3)


class H01_FirstDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 6.93)
        gun, barrier, screen = make_apparatus()
        self.play(Create(gun), Create(barrier), Create(screen), run_time=0.8)

        for _ in range(2):
            dot = Dot(color=BLUE, radius=0.15).move_to(gun.get_center() + RIGHT * 0.5)
            hit = Dot(color="#E0DDD5", radius=0.06).move_to(RIGHT * 4.5 + UP * np.random.uniform(-1.5, 1.5))
            self.play(dot.animate.move_to(LEFT * 1.5 + dot.get_y() * UP), run_time=0.3)
            self.play(dot.animate.move_to(hit.get_center()), run_time=0.3)
            self.play(ReplacementTransform(dot, hit), run_time=0.1)

        self.wait(dur - 1.5)


class H02_TenDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 4.57)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Place 10 scattered dots
        import random
        random.seed(42)
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.05).move_to(RIGHT * 4.5 + UP * random.uniform(-2, 2))
            for _ in range(10)])

        counter = Text("electrons: 10", font="Courier New", font_size=22, color=INK).move_to(LEFT * 5 + DOWN * 3.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.3)


class H03_TwoHeapPrediction(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H03", 4.37)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Classical two-heap prediction: two gaussians at screen
        heap_curve = ParametricFunction(
            lambda t: np.array([
                4.5,
                t,
                0
            ]),
            t_range=[-3, 3], color=BROWN, stroke_width=1, stroke_opacity=0.3
        )

        # Build gaussian humps
        def gauss(t, mu, sigma=0.5):
            return 1.8 * np.exp(-(t - mu)**2 / (2 * sigma**2))

        heap_path = ParametricFunction(
            lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
            t_range=[-3, 3], color=BROWN, stroke_width=2.5, stroke_opacity=0.7
        )
        heap_lbl = Text("predicted", font=FONT, font_size=20, color=BROWN).move_to(RIGHT * 6.5 + UP * 0.5)

        self.play(Create(heap_path), FadeIn(heap_lbl), run_time=1.0)
        self.wait(dur - 1.0)


class H04_ImpossibleBegins(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H04", 3.61)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        def gauss(t, mu, sigma=0.5):
            return 1.8 * np.exp(-(t - mu)**2 / (2 * sigma**2))

        heap_path = ParametricFunction(
            lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
            t_range=[-3, 3], color=BROWN, stroke_width=2.5, stroke_opacity=0.3
        )
        self.add(heap_path)

        question = Text("?", font=FONT, font_size=72, color=HIGHLIGHT).move_to(RIGHT * 3 + UP * 0.5)
        self.play(FadeIn(question), Indicate(question, color=HIGHLIGHT, scale_factor=1.2), run_time=0.8)
        self.wait(dur - 0.8)


class W01_WaveArcs(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 5.57)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Arc fans from each slit
        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1

        arcs_a = VGroup(*[
            Arc(radius=0.5 + i * 0.6, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.7 - i * 0.1)
            .move_to(slit_a)
            for i in range(5)])

        arcs_b = VGroup(*[
            Arc(radius=0.5 + i * 0.6, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.7 - i * 0.1)
            .move_to(slit_b)
            for i in range(5)])

        self.play(Create(arcs_a), run_time=0.7)
        self.play(Create(arcs_b), run_time=0.7)
        self.wait(dur - 1.4)


class W02_WaveMakesStripes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 5.18)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Intensity curve (cos^2)
        stripe_curve = ParametricFunction(
            lambda t: np.array([4.5 + 1.5 * np.cos(t * PI / 0.6)**2, t, 0]),
            t_range=[-2.5, 2.5], color=BLUE, stroke_width=3
        )
        label = Text("waves: stripes", font=FONT, font_size=22, color=INK).move_to(LEFT * 4.5 + UP * 3.5)

        self.play(Create(stripe_curve), run_time=1.0)
        self.play(Write(label), run_time=0.5)
        self.wait(dur - 1.5)


class L01_BallsOneSlit(Scene):
    def construct(self):
        self.add(bg())
        dur = d("L01", 4.27)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Blue arcs fade
        ball1 = Dot(color=BROWN, radius=0.18).move_to(gun.get_center() + RIGHT * 0.5)
        ball2 = Dot(color=BROWN, radius=0.18).move_to(gun.get_center() + RIGHT * 0.5)
        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1

        self.play(ball1.animate.move_to(slit_a), run_time=0.4)
        self.play(ball1.animate.move_to(RIGHT * 4.5 + UP * 1.0), run_time=0.4)
        self.play(ball2.animate.move_to(slit_b), run_time=0.4)
        self.play(ball2.animate.move_to(RIGHT * 4.5 + DOWN * 1.0), run_time=0.4)
        self.wait(dur - 1.6)


class L02_ParticleTwoHeaps(Scene):
    def construct(self):
        self.add(bg())
        dur = d("L02", 5.38)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Dashed expectation → solid brown heaps
        def gauss(t, mu, sigma=0.5):
            return 1.8 * np.exp(-(t - mu)**2 / (2 * sigma**2))

        dashed = DashedVMobject(
            ParametricFunction(
                lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
                t_range=[-3, 3], color=BROWN, stroke_width=2),
            num_dashes=20)

        solid = ParametricFunction(
            lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
            t_range=[-3, 3], color=BROWN, stroke_width=2.5)

        lbl1 = Text("waves: stripes", font=FONT, font_size=20, color=INK).move_to(LEFT * 4 + UP * 3.5)
        lbl2 = Text("particles: two heaps", font=FONT, font_size=20, color=INK).move_to(LEFT * 4 + UP * 3.0)

        self.add(dashed, lbl1)
        self.play(ReplacementTransform(dashed, solid), run_time=0.8)
        self.play(Write(lbl2), run_time=0.5)
        self.wait(dur - 1.3)


class T01_TwoHundredDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T01", 4.93)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        import random
        random.seed(10)
        # 200 dots with slight clustering toward center bands
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.04).move_to(
                RIGHT * 4.5 + UP * random.gauss(0, 1.2))
            for _ in range(200)])

        counter_old = Text("electrons: 10", font="Courier New", font_size=20, color=INK).move_to(LEFT * 5 + DOWN * 3.5)
        counter_new = Text("electrons: 200", font="Courier New", font_size=20, color=INK).move_to(LEFT * 5 + DOWN * 3.5)

        self.add(counter_old)
        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.01), run_time=1.5)
        self.play(ReplacementTransform(counter_old, counter_new), run_time=0.3)
        self.wait(dur - 1.8)


class T02_SixThousandDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T02", 3.82)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        import random
        random.seed(20)

        def fringe_y():
            """Generate y positions following a cos^2 pattern."""
            while True:
                y = random.uniform(-2.5, 2.5)
                p = np.cos(y * PI / 0.6)**2
                if random.random() < p:
                    return y

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.03).move_to(RIGHT * 4.5 + UP * fringe_y())
            for _ in range(600)])  # Represent 6000 with 600

        counter = Text("electrons: 6,000", font="Courier New", font_size=20, color=INK).move_to(LEFT * 5 + DOWN * 3.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.002), run_time=1.2)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.5)


class T03_SeventyThousandDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T03", 4.93)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        import random
        random.seed(30)

        def fringe_y():
            while True:
                y = random.uniform(-2.5, 2.5)
                p = np.cos(y * PI / 0.6)**2
                if random.random() < p:
                    return y

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * 4.5 + UP * fringe_y())
            for _ in range(1000)])  # Dense representation

        counter = Text("electrons: 70,000", font="Courier New", font_size=20, color=INK).move_to(LEFT * 5 + DOWN * 3.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.001), run_time=1.5)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.8)


class T04_StripeOverlay(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T04", 4.07)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Pre-existing fringe dots (dense)
        import random
        random.seed(30)

        def fringe_y():
            while True:
                y = random.uniform(-2.5, 2.5)
                p = np.cos(y * PI / 0.6)**2
                if random.random() < p:
                    return y

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * 4.5 + UP * fringe_y())
            for _ in range(800)])
        self.add(dots)

        stripe_curve = ParametricFunction(
            lambda t: np.array([4.5 + 1.5 * np.cos(t * PI / 0.6)**2, t, 0]),
            t_range=[-2.5, 2.5], color=BLUE, stroke_width=2.5, stroke_opacity=0.8
        )
        self.play(Create(stripe_curve), run_time=1.0)
        self.wait(dur - 1.0)


class T05_ForbiddenBands(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T05", 5.87)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Stripe overlay present
        stripe_curve = ParametricFunction(
            lambda t: np.array([4.5 + 1.5 * np.cos(t * PI / 0.6)**2, t, 0]),
            t_range=[-2.5, 2.5], color=BLUE, stroke_width=2)
        self.add(stripe_curve)

        # Highlight a dark (zero) band
        # cos^2 = 0 when t*PI/0.6 = PI/2, so t = 0.3
        dark_band = Rectangle(width=2.5, height=0.25, color=HIGHLIGHT, fill_opacity=0.35, stroke_width=0)
        dark_band.move_to(RIGHT * 3.7 + UP * 0.3)

        self.play(FadeIn(dark_band), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(dark_band), run_time=0.6)
        self.wait(dur - 2.5)


class T06_OneAtATime(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T06", 5.16)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        label = Text("one at a time", font=FONT, font_size=24, color="#E0DDD5").next_to(gun, UP, buff=0.3)
        self.play(Write(label), run_time=0.6)
        self.play(Indicate(gun, color=BLUE, scale_factor=1.15), run_time=0.8)
        self.wait(dur - 1.4)


class A01_BothSlitsAtOnce(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 5.44)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1

        arcs_a = VGroup(*[
            Arc(radius=0.5 + i * 0.6, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.4)
            .move_to(slit_a)
            for i in range(5)])

        arcs_b = VGroup(*[
            Arc(radius=0.5 + i * 0.6, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.4)
            .move_to(slit_b)
            for i in range(5)])

        arcs = VGroup(arcs_a, arcs_b)

        self.play(FadeIn(arcs, run_time=0.8))
        self.wait(1.5)
        self.play(arcs.animate.set_opacity(0.15), run_time=0.8)
        self.wait(dur - 3.1)


class A02_DotAndStripes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 5.29)

        # Side card
        card_line1 = Text("dot = where it's found", font=FONT, font_size=26, color="#E0DDD5")
        card_line2 = Text("stripes = where that's likely", font=FONT, font_size=26, color="#E0DDD5")
        card = VGroup(card_line1, card_line2).arrange(DOWN, buff=0.4).move_to(RIGHT * 2)

        self.play(Write(card_line1), run_time=0.8)
        self.play(Write(card_line2), run_time=0.8)
        self.wait(dur - 1.6)


class A03_PsiSquared(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A03", 5.31)

        card_line1 = Text("dot = where it's found", font=FONT, font_size=22, color="#E0DDD5").move_to(UP * 0.8)
        card_line2 = Text("stripes = where that's likely", font=FONT, font_size=22, color="#E0DDD5").move_to(UP * 0.1)
        self.add(card_line1, card_line2)

        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=64).move_to(DOWN * 1.2)
        self.play(Write(psi_sq), run_time=1.0)
        self.wait(dur - 1.0)


class A04_DeBroglieRule(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A04", 6.49)

        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=52).move_to(UP * 0.8)
        self.add(psi_sq)

        lambda_eq = MathTex(r"\lambda = \frac{h}{p}", color="#E0DDD5", font_size=52).move_to(DOWN * 0.5)
        self.play(Write(lambda_eq), run_time=1.2)
        self.wait(dur - 1.2)


class Y01_ParticleArrivalWaveJourney(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y01", 5.65)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        slit_a = LEFT * 1.5 + UP * 1.1
        slit_b = LEFT * 1.5 + DOWN * 1.1
        arcs_a = VGroup(*[
            Arc(radius=0.4 + i * 0.5, start_angle=-PI / 3, angle=PI * 2 / 3,
                color=BLUE, stroke_width=1, stroke_opacity=0.15).move_to(slit_a)
            for i in range(5)])
        arcs_b = arcs_a.copy().move_to(slit_b)
        self.add(arcs_a, arcs_b)

        dot = Dot(color=BLUE, radius=0.15).move_to(gun.get_center() + RIGHT * 0.5)
        hit = Dot(color="#E0DDD5", radius=0.07).move_to(RIGHT * 4.5 + UP * 0.6)

        self.play(dot.animate.move_to(LEFT * 1.5), run_time=0.5)
        # Arcs pulse as electron crosses
        self.play(
            arcs_a.animate.set_opacity(0.5),
            arcs_b.animate.set_opacity(0.5),
            dot.animate.move_to(RIGHT * 1.5),
            run_time=0.4)
        self.play(
            arcs_a.animate.set_opacity(0.15),
            arcs_b.animate.set_opacity(0.15),
            dot.animate.move_to(hit.get_center()),
            run_time=0.4)
        self.play(ReplacementTransform(dot, hit), run_time=0.1)
        self.wait(dur - 1.4)


class Y02_WatchingKillsFringes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y02", 5.44)
        gun, barrier, screen = make_apparatus()
        self.add(gun, barrier, screen)

        # Fringe pattern present
        stripe_curve = ParametricFunction(
            lambda t: np.array([4.5 + 1.5 * np.cos(t * PI / 0.6)**2, t, 0]),
            t_range=[-2.5, 2.5], color=BLUE, stroke_width=2)

        # Import some dots
        import random
        random.seed(30)
        def fringe_y():
            while True:
                y = random.uniform(-2.5, 2.5)
                p = np.cos(y * PI / 0.6)**2
                if random.random() < p:
                    return y
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * 4.5 + UP * fringe_y())
            for _ in range(400)])
        self.add(stripe_curve, dots)

        # Detector glyph at upper slit
        detector = Square(side_length=0.35, color=HIGHLIGHT, fill_opacity=0.5).move_to(LEFT * 1.5 + UP * 1.1)
        detector_lbl = Text("D", font=FONT, font_size=18, color=HIGHLIGHT).move_to(detector.get_center())
        self.play(FadeIn(detector), FadeIn(detector_lbl), run_time=0.5)

        # Stripes morph to heaps
        def gauss(t, mu, sigma=0.5):
            return 1.8 * np.exp(-(t - mu)**2 / (2 * sigma**2))
        heap = ParametricFunction(
            lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
            t_range=[-3, 3], color=BROWN, stroke_width=2.5)

        self.play(Transform(stripe_curve, heap), dots.animate.set_opacity(0.3), run_time=1.0)
        self.wait(dur - 1.5)


class N01_Molecules(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N01", 5.61)

        mol_line = Text("molecules of 2,000 atoms → stripes", font=FONT, font_size=30, color="#E0DDD5")
        mol_line.move_to(UP * 0.5)
        self.play(Write(mol_line), run_time=1.0)
        self.wait(dur - 1.0)


class N02_YourWavelength(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N02", 7.15)

        mol_line = Text("molecules of 2,000 atoms → stripes", font=FONT, font_size=26, color="#E0DDD5").move_to(UP * 1.0)
        self.add(mol_line)

        you_line = Text("you, walking:", font=FONT, font_size=26, color="#E0DDD5").move_to(DOWN * 0.2)
        lambda_you = MathTex(r"\lambda \approx 10^{-35}\,\text{m}", color=BLUE, font_size=40).move_to(DOWN * 1.2)

        self.play(Write(you_line), run_time=0.6)
        self.play(Write(lambda_you), run_time=1.0)
        self.wait(dur - 1.6)


class B01_CloseCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B01", 6.87)

        psi_sq = MathTex(r"|\psi|^2", color="#E0DDD5", font_size=52).move_to(UP * 1.0)
        lambda_eq = MathTex(r"\lambda = \frac{h}{p}", color="#E0DDD5", font_size=52).move_to(DOWN * 0.2)
        tag1 = Text("next · what ψ means", font=FONT, font_size=24, color="#888888").move_to(DOWN * 1.5)
        tag2 = Text("next · Davisson–Germer", font=FONT, font_size=24, color="#888888").move_to(DOWN * 2.2)

        self.play(Write(psi_sq), Write(lambda_eq), run_time=1.2)
        self.play(LaggedStart(FadeIn(tag1), FadeIn(tag2), lag_ratio=0.3), run_time=0.8)
        self.wait(dur - 2.0)


class B02_Exercise(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B02", 5.87)

        psi_sq = MathTex(r"|\psi|^2", color="#E0DDD5", font_size=36).move_to(UP * 3.2 + LEFT * 2)
        lambda_eq = MathTex(r"\lambda = h/p", color="#E0DDD5", font_size=36).move_to(UP * 3.2 + RIGHT * 2)
        self.add(psi_sq, lambda_eq)

        exercise = Text(
            "Compute your own de Broglie wavelength,\nh over m times v, on your next walk.",
            font=FONT, font_size=28, color=HIGHLIGHT, line_spacing=1.4).move_to(ORIGIN)

        self.play(Write(exercise), run_time=1.5)
        self.wait(dur - 1.5)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 6.63)

        psi_sq = MathTex(r"|\psi|^2", color="#E0DDD5", font_size=44).move_to(UP * 1.5)
        lambda_eq = MathTex(r"\lambda = \frac{h}{p}", color="#E0DDD5", font_size=44).move_to(UP * 0.3)
        self.add(psi_sq, lambda_eq)

        title = Text("One Electron Interferes With Itself",
                     font=FONT, font_size=26, color="#E0DDD5", fill_opacity=0.7).move_to(UP * 3.5)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(dur - 0.5)
