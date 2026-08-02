"""Portrait (9:16) Manim scenes for double-slit-one-electron-bb short.

Frame: 4.5 wide × 8.0 tall (1080×1920 render → frame_width = 8*(1080/1920) = 4.5).
Apparatus is reoriented vertically: gun at top-centre firing DOWN, barrier
in the middle, screen near the bottom.
"""
import json, random
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"
DARK_BG = "#1a1a1a"
BLUE = "#58C4DD"
BROWN = "#CD853F"
HIGHLIGHT = "#F0E442"

# Portrait frame constants (manim units)
FW = 4.5   # frame width
FH = 8.0   # frame height

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / "beat_sheet.json").read_text())
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 5)
           for b in _bs.get("beats", [])}
    TITLE = _bs["metadata"].get("title", "")
except Exception:
    DUR = {}; TITLE = ""

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    """Portrait dark background rectangle."""
    return Rectangle(width=FW, height=FH).set_fill(DARK_BG, 1).set_stroke(width=0)

def make_apparatus_portrait():
    """Vertical apparatus: gun (top-centre) → barrier (middle) → screen (bottom).
    Returns (gun_group, barrier, screen) as VGroups.
    """
    # Gun at top, firing downward
    gun_body = Rectangle(width=0.8, height=0.5, color="#888888", fill_opacity=0.9).move_to(UP * 3.0)
    gun_nozzle = Rectangle(width=0.2, height=0.3, color="#888888", fill_opacity=0.9)
    gun_nozzle.next_to(gun_body, DOWN, buff=0)
    gun = VGroup(gun_body, gun_nozzle)

    # Barrier: left slab, gap (upper slit), middle slab, gap (lower slit), right slab
    # In portrait orientation we lay this horizontally across the frame
    slab_l = Rectangle(width=1.2, height=0.15, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5 + UP * 0.3)
    slab_m = Rectangle(width=0.5, height=0.15, color="#E0DDD5", fill_opacity=0.9).move_to(ORIGIN + UP * 0.3)
    slab_r = Rectangle(width=1.2, height=0.15, color="#E0DDD5", fill_opacity=0.9).move_to(RIGHT * 1.5 + UP * 0.3)
    barrier = VGroup(slab_l, slab_m, slab_r)

    # Screen: horizontal strip near the bottom
    screen = Rectangle(width=FW * 0.85, height=0.12, color="#E0DDD5", fill_opacity=0.8).move_to(DOWN * 2.5)

    return gun, barrier, screen

# Slit positions (x) in the barrier
SLIT_LEFT_X  = -0.85   # between slab_l and slab_m
SLIT_RIGHT_X =  0.85   # between slab_m and slab_r
BARRIER_Y    =  0.3

def slit_l():
    return np.array([SLIT_LEFT_X,  BARRIER_Y, 0])

def slit_r():
    return np.array([SLIT_RIGHT_X, BARRIER_Y, 0])

def screen_y():
    return -2.5


# ── Beat scenes ──────────────────────────────────────────────────────────────

class H01_FirstDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 6.93)
        gun, barrier, screen = make_apparatus_portrait()
        self.play(Create(gun), Create(barrier), Create(screen), run_time=0.8)

        random.seed(1)
        for _ in range(3):
            dot = Dot(color=BLUE, radius=0.12).move_to(UP * 2.5)
            slit = slit_l() if _ % 2 == 0 else slit_r()
            hit_x = random.uniform(-FW * 0.4, FW * 0.4)
            hit = Dot(color="#E0DDD5", radius=0.06).move_to(RIGHT * hit_x + DOWN * 2.5)
            self.play(dot.animate.move_to(slit + DOWN * 0.3), run_time=0.25)
            self.play(dot.animate.move_to(hit.get_center()), run_time=0.25)
            self.play(ReplacementTransform(dot, hit), run_time=0.08)

        self.wait(dur - 1.7)


class H02_TenDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 4.57)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(42)
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.06).move_to(
                RIGHT * random.uniform(-FW * 0.4, FW * 0.4) + DOWN * 2.5)
            for _ in range(10)])
        counter = Text("electrons: 10", font="Courier New", font_size=24, color=INK).move_to(UP * 2.5 + LEFT * 0.3)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.3)


class H03_TwoHeapPrediction(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H03", 4.37)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        def gauss(x, mu, sigma=0.5):
            return 1.6 * np.exp(-(x - mu)**2 / (2 * sigma**2))

        # Two heaps along x-axis on the screen row (y = screen_y())
        heap_path = ParametricFunction(
            lambda t: np.array([t, screen_y() - gauss(t, -0.85) - gauss(t, 0.85), 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BROWN, stroke_width=2.5, stroke_opacity=0.7
        )
        heap_lbl = Text("predicted", font=FONT, font_size=22, color=BROWN).move_to(DOWN * 3.6)

        self.play(Create(heap_path), FadeIn(heap_lbl), run_time=1.0)
        self.wait(dur - 1.0)


class H04_ImpossibleBegins(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H04", 3.61)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        def gauss(x, mu, sigma=0.5):
            return 1.6 * np.exp(-(x - mu)**2 / (2 * sigma**2))

        heap_path = ParametricFunction(
            lambda t: np.array([t, screen_y() - gauss(t, -0.85) - gauss(t, 0.85), 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BROWN, stroke_width=2, stroke_opacity=0.3
        )
        self.add(heap_path)

        question = Text("?", font=FONT, font_size=96, color=HIGHLIGHT).move_to(DOWN * 1.0)
        self.play(FadeIn(question), Indicate(question, color=HIGHLIGHT, scale_factor=1.2), run_time=0.8)
        self.wait(dur - 0.8)


class W01_WaveArcs(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 5.57)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        # Arc fans downward from each slit
        sl = slit_l();  sr = slit_r()

        arcs_l = VGroup(*[
            Arc(radius=0.4 + i * 0.45, start_angle=-PI * 5/6, angle=PI * 2/3,
                color=BLUE, stroke_width=1.5, stroke_opacity=max(0.1, 0.7 - i * 0.12))
            .move_to(sl)
            for i in range(5)])

        arcs_r = VGroup(*[
            Arc(radius=0.4 + i * 0.45, start_angle=-PI * 5/6, angle=PI * 2/3,
                color=BLUE, stroke_width=1.5, stroke_opacity=max(0.1, 0.7 - i * 0.12))
            .move_to(sr)
            for i in range(5)])

        self.play(Create(arcs_l), run_time=0.7)
        self.play(Create(arcs_r), run_time=0.7)
        self.wait(dur - 1.4)


class W02_WaveMakesStripes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 5.18)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        # Interference stripe across screen (horizontal → cos^2 along x)
        stripe_curve = ParametricFunction(
            lambda t: np.array([t, screen_y() - 1.2 * np.cos(t * PI / 0.55)**2, 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BLUE, stroke_width=3
        )
        label = Text("waves: stripes", font=FONT, font_size=22, color=INK).move_to(DOWN * 1.0)

        self.play(Create(stripe_curve), run_time=1.0)
        self.play(Write(label), run_time=0.5)
        self.wait(dur - 1.5)


class L01_BallsOneSlit(Scene):
    def construct(self):
        self.add(bg())
        dur = d("L01", 4.27)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        ball1 = Dot(color=BROWN, radius=0.14).move_to(UP * 2.5)
        ball2 = Dot(color=BROWN, radius=0.14).move_to(UP * 2.5)

        self.play(ball1.animate.move_to(slit_l()), run_time=0.35)
        self.play(ball1.animate.move_to(RIGHT * SLIT_LEFT_X + DOWN * 2.5), run_time=0.35)
        self.play(FadeOut(ball1), run_time=0.1)
        self.play(ball2.animate.move_to(slit_r()), run_time=0.35)
        self.play(ball2.animate.move_to(RIGHT * SLIT_RIGHT_X + DOWN * 2.5), run_time=0.35)
        self.play(FadeOut(ball2), run_time=0.1)
        self.wait(dur - 1.6)


class L02_ParticleTwoHeaps(Scene):
    def construct(self):
        self.add(bg())
        dur = d("L02", 5.38)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        def gauss(x, mu, sigma=0.5):
            return 1.6 * np.exp(-(x - mu)**2 / (2 * sigma**2))

        dashed = DashedVMobject(
            ParametricFunction(
                lambda t: np.array([t, screen_y() - gauss(t, -0.85) - gauss(t, 0.85), 0]),
                t_range=[-FW * 0.4, FW * 0.4], color=BROWN, stroke_width=2),
            num_dashes=20)

        solid = ParametricFunction(
            lambda t: np.array([t, screen_y() - gauss(t, -0.85) - gauss(t, 0.85), 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BROWN, stroke_width=2.5)

        lbl = Text("particles: two heaps", font=FONT, font_size=22, color=INK).move_to(DOWN * 1.2)

        self.add(dashed)
        self.play(ReplacementTransform(dashed, solid), run_time=0.8)
        self.play(Write(lbl), run_time=0.5)
        self.wait(dur - 1.3)


class T01_TwoHundredDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T01", 4.93)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(10)
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.04).move_to(
                RIGHT * random.gauss(0, FW * 0.3) + DOWN * 2.5)
            for _ in range(200)])
        counter = Text("electrons: 200", font="Courier New", font_size=22, color=INK).move_to(DOWN * 1.0)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.01), run_time=1.5)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.8)


class T02_SixThousandDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T02", 3.82)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(20)

        def fringe_x():
            while True:
                x = random.uniform(-FW * 0.4, FW * 0.4)
                p = np.cos(x * PI / 0.55)**2
                if random.random() < p:
                    return x

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.03).move_to(RIGHT * fringe_x() + DOWN * 2.5)
            for _ in range(600)])
        counter = Text("electrons: 6,000", font="Courier New", font_size=22, color=INK).move_to(DOWN * 1.0)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.002), run_time=1.2)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.5)


class T03_SeventyThousandDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T03", 4.93)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(30)

        def fringe_x():
            while True:
                x = random.uniform(-FW * 0.4, FW * 0.4)
                p = np.cos(x * PI / 0.55)**2
                if random.random() < p:
                    return x

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * fringe_x() + DOWN * 2.5)
            for _ in range(1000)])
        counter = Text("electrons: 70,000", font="Courier New", font_size=22, color=INK).move_to(DOWN * 1.0)

        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.001), run_time=1.5)
        self.play(FadeIn(counter), run_time=0.3)
        self.wait(dur - 1.8)


class T04_StripeOverlay(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T04", 4.07)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(30)
        def fringe_x():
            while True:
                x = random.uniform(-FW * 0.4, FW * 0.4)
                p = np.cos(x * PI / 0.55)**2
                if random.random() < p:
                    return x

        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * fringe_x() + DOWN * 2.5)
            for _ in range(800)])
        self.add(dots)

        stripe_curve = ParametricFunction(
            lambda t: np.array([t, screen_y() - 1.2 * np.cos(t * PI / 0.55)**2, 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BLUE, stroke_width=2.5, stroke_opacity=0.85
        )
        self.play(Create(stripe_curve), run_time=1.0)
        self.wait(dur - 1.0)


class T05_ForbiddenBands(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T05", 5.87)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        stripe_curve = ParametricFunction(
            lambda t: np.array([t, screen_y() - 1.2 * np.cos(t * PI / 0.55)**2, 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BLUE, stroke_width=2)
        self.add(stripe_curve)

        # Dark band: a small strip at x≈0 (destructive node)
        dark_band = Rectangle(width=0.22, height=0.5, color=HIGHLIGHT, fill_opacity=0.35, stroke_width=0)
        dark_band.move_to(ORIGIN + DOWN * 2.5)

        self.play(FadeIn(dark_band), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(dark_band), run_time=0.6)
        self.wait(dur - 2.5)


class T06_OneAtATime(Scene):
    def construct(self):
        self.add(bg())
        dur = d("T06", 5.16)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        label = Text("one at a time", font=FONT, font_size=28, color="#E0DDD5").move_to(UP * 1.5)
        self.play(Write(label), run_time=0.6)
        self.play(Indicate(gun, color=BLUE, scale_factor=1.15), run_time=0.8)
        self.wait(dur - 1.4)


class A01_BothSlitsAtOnce(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 5.44)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        sl = slit_l();  sr = slit_r()

        arcs_l = VGroup(*[
            Arc(radius=0.4 + i * 0.45, start_angle=-PI * 5/6, angle=PI * 2/3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.4)
            .move_to(sl)
            for i in range(4)])
        arcs_r = VGroup(*[
            Arc(radius=0.4 + i * 0.45, start_angle=-PI * 5/6, angle=PI * 2/3,
                color=BLUE, stroke_width=1.5, stroke_opacity=0.4)
            .move_to(sr)
            for i in range(4)])
        arcs = VGroup(arcs_l, arcs_r)

        self.play(FadeIn(arcs), run_time=0.8)
        self.wait(1.5)
        self.play(arcs.animate.set_opacity(0.15), run_time=0.8)
        self.wait(dur - 3.1)


class A02_DotAndStripes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 5.29)

        line1 = Text("dot = where it's found", font=FONT, font_size=28, color="#E0DDD5").move_to(UP * 0.8)
        line2 = Text("stripes = where that's likely", font=FONT, font_size=26, color="#E0DDD5").move_to(DOWN * 0.1)

        self.play(Write(line1), run_time=0.8)
        self.play(Write(line2), run_time=0.8)
        self.wait(dur - 1.6)


class A03_PsiSquared(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A03", 5.31)

        line1 = Text("dot = where it's found", font=FONT, font_size=24, color="#E0DDD5").move_to(UP * 1.5)
        line2 = Text("stripes = where that's likely", font=FONT, font_size=22, color="#E0DDD5").move_to(UP * 0.6)
        self.add(line1, line2)

        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=72).move_to(DOWN * 0.9)
        self.play(Write(psi_sq), run_time=1.0)
        self.wait(dur - 1.0)


class A04_DeBroglieRule(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A04", 6.49)

        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=60).move_to(UP * 1.0)
        self.add(psi_sq)

        lambda_eq = MathTex(r"\lambda = \frac{h}{p}", color="#E0DDD5", font_size=60).move_to(DOWN * 0.5)
        self.play(Write(lambda_eq), run_time=1.2)
        self.wait(dur - 1.2)


class Y01_ParticleArrivalWaveJourney(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y01", 5.65)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        sl = slit_l();  sr = slit_r()
        arcs_l = VGroup(*[
            Arc(radius=0.35 + i * 0.4, start_angle=-PI * 5/6, angle=PI * 2/3,
                color=BLUE, stroke_width=1, stroke_opacity=0.15).move_to(sl)
            for i in range(4)])
        arcs_r = arcs_l.copy().move_to(sr)
        self.add(arcs_l, arcs_r)

        dot = Dot(color=BLUE, radius=0.13).move_to(UP * 2.5)
        hit = Dot(color="#E0DDD5", radius=0.08).move_to(DOWN * 2.5 + LEFT * 0.3)

        self.play(dot.animate.move_to(BARRIER_Y * UP + LEFT * 0.2), run_time=0.5)
        self.play(
            arcs_l.animate.set_opacity(0.5),
            arcs_r.animate.set_opacity(0.5),
            dot.animate.move_to(DOWN * 1.0),
            run_time=0.4)
        self.play(
            arcs_l.animate.set_opacity(0.15),
            arcs_r.animate.set_opacity(0.15),
            dot.animate.move_to(hit.get_center()),
            run_time=0.4)
        self.play(ReplacementTransform(dot, hit), run_time=0.1)
        self.wait(dur - 1.4)


class Y02_WatchingKillsFringes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y02", 5.44)
        gun, barrier, screen = make_apparatus_portrait()
        self.add(gun, barrier, screen)

        random.seed(30)
        def fringe_x():
            while True:
                x = random.uniform(-FW * 0.4, FW * 0.4)
                p = np.cos(x * PI / 0.55)**2
                if random.random() < p:
                    return x

        stripe_curve = ParametricFunction(
            lambda t: np.array([t, screen_y() - 1.2 * np.cos(t * PI / 0.55)**2, 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BLUE, stroke_width=2)
        dots = VGroup(*[
            Dot(color="#E0DDD5", radius=0.025).move_to(RIGHT * fringe_x() + DOWN * 2.5)
            for _ in range(400)])
        self.add(stripe_curve, dots)

        detector = Square(side_length=0.3, color=HIGHLIGHT, fill_opacity=0.5).move_to(slit_l())
        det_lbl = Text("D", font=FONT, font_size=20, color=HIGHLIGHT).move_to(detector.get_center())
        self.play(FadeIn(detector), FadeIn(det_lbl), run_time=0.5)

        def gauss(x, mu, sigma=0.5):
            return 1.6 * np.exp(-(x - mu)**2 / (2 * sigma**2))

        heap = ParametricFunction(
            lambda t: np.array([t, screen_y() - gauss(t, -0.85) - gauss(t, 0.85), 0]),
            t_range=[-FW * 0.4, FW * 0.4], color=BROWN, stroke_width=2.5)

        self.play(Transform(stripe_curve, heap), dots.animate.set_opacity(0.3), run_time=1.0)
        self.wait(dur - 1.5)


class N01_Molecules(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N01", 5.61)

        mol_line = Text("molecules of 2,000 atoms\n→ stripes",
                        font=FONT, font_size=30, color="#E0DDD5", line_spacing=1.3).move_to(ORIGIN)
        self.play(Write(mol_line), run_time=1.0)
        self.wait(dur - 1.0)


class N02_YourWavelength(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N02", 7.15)

        mol_line = Text("molecules of 2,000 atoms\n→ stripes",
                        font=FONT, font_size=24, color="#E0DDD5", line_spacing=1.3).move_to(UP * 1.8)
        self.add(mol_line)

        you_line = Text("you, walking:", font=FONT, font_size=26, color="#E0DDD5").move_to(DOWN * 0.3)
        lambda_you = MathTex(r"\lambda \approx 10^{-35}\,\text{m}", color=BLUE, font_size=44).move_to(DOWN * 1.4)

        self.play(Write(you_line), run_time=0.6)
        self.play(Write(lambda_you), run_time=1.0)
        self.wait(dur - 1.6)


class B01_CloseCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B01", 6.87)

        psi_sq = MathTex(r"|\psi|^2", color="#E0DDD5", font_size=54).move_to(UP * 1.5)
        lambda_eq = MathTex(r"\lambda = \frac{h}{p}", color="#E0DDD5", font_size=54).move_to(UP * 0.0)
        tag1 = Text("next · what ψ means", font=FONT, font_size=22, color="#888888").move_to(DOWN * 1.3)
        tag2 = Text("next · Davisson–Germer", font=FONT, font_size=22, color="#888888").move_to(DOWN * 2.0)

        self.play(Write(psi_sq), Write(lambda_eq), run_time=1.2)
        self.play(LaggedStart(FadeIn(tag1), FadeIn(tag2), lag_ratio=0.3), run_time=0.8)
        self.wait(dur - 2.0)


class B02_Exercise(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B02", 5.87)

        psi_sq = MathTex(r"|\psi|^2", color="#E0DDD5", font_size=36).move_to(UP * 2.8 + LEFT * 0.8)
        lambda_eq = MathTex(r"\lambda = h/p", color="#E0DDD5", font_size=36).move_to(UP * 2.8 + RIGHT * 0.8)
        self.add(psi_sq, lambda_eq)

        exercise = Text(
            "Compute your own\nde Broglie wavelength,\nh over m times v,\non your next walk.",
            font=FONT, font_size=28, color=HIGHLIGHT, line_spacing=1.4).move_to(DOWN * 0.2)

        self.play(Write(exercise), run_time=1.5)
        self.wait(dur - 1.5)
