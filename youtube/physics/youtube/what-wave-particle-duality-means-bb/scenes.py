import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

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

def make_compact_lab():
    gun = Rectangle(width=0.5, height=0.8, color="#888888", fill_opacity=0.8).move_to(LEFT * 5)
    barrier_top = Rectangle(width=0.2, height=1.5, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5 + UP * 2)
    barrier_mid = Rectangle(width=0.2, height=0.8, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5)
    barrier_bot = Rectangle(width=0.2, height=1.5, color="#E0DDD5", fill_opacity=0.9).move_to(LEFT * 1.5 + DOWN * 2)
    screen = Rectangle(width=0.15, height=4.5, color="#E0DDD5", fill_opacity=0.8).move_to(RIGHT * 4.5)
    return gun, VGroup(barrier_top, barrier_mid, barrier_bot), screen


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 3.58)
        series = Text("Bear's Notes", font=FONT, font_size=28, color=BROWN).move_to(UP * 1.5)
        title = Text("What Wave–Particle Duality Actually Means",
                     font=FONT, font_size=40, color="#E0DDD5").move_to(DOWN * 0.0)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=BROWN, stroke_width=1.5).move_to(DOWN * 0.8)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 4.7 + DOWN * 0.8)
        self.play(FadeIn(series), Write(title), run_time=1.0)
        self.play(Create(rule), FadeIn(tick), run_time=0.6)
        self.wait(dur - 1.6)


class H01_BallWithRipples(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 5.33)

        ball = Circle(radius=0.4, color=BROWN, fill_opacity=0.8).move_to(ORIGIN)
        ripples = VGroup(*[
            Circle(radius=0.4 + i * 0.55, color=BLUE, stroke_width=1.5, stroke_opacity=0.8 - i * 0.15)
            .move_to(ORIGIN)
            for i in range(1, 5)])

        self.play(GrowFromCenter(ball), run_time=0.5)
        self.play(Create(ripples), run_time=1.0)
        self.wait(dur - 1.5)


class H02_CoreAndCoatLabels(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 3.66)

        ball = Circle(radius=0.4, color=BROWN, fill_opacity=0.8).move_to(ORIGIN)
        ripples = VGroup(*[
            Circle(radius=0.4 + i * 0.55, color=BLUE, stroke_width=1.5, stroke_opacity=0.8 - i * 0.15)
            .move_to(ORIGIN)
            for i in range(1, 5)])
        self.add(ball, ripples)

        core_lbl = Text("the core", font=FONT, font_size=24, color="#E0DDD5")
        core_lbl.move_to(LEFT * 3 + UP * 0.5)
        core_ptr = Line(core_lbl.get_right(), ball.get_left(), color="#E0DDD5", stroke_width=1.5)

        coat_lbl = Text("the coat", font=FONT, font_size=24, color=BLUE)
        coat_lbl.move_to(LEFT * 3 + DOWN * 0.8)
        coat_ptr = Line(coat_lbl.get_right(), ripples[1].get_left(), color=BLUE, stroke_width=1.5)

        self.play(Write(core_lbl), Create(core_ptr), Write(coat_lbl), Create(coat_ptr), run_time=0.8)
        self.wait(dur - 0.8)


class H03_ScaleMismatch(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H03", 8.62)

        ball = Circle(radius=0.4, color=BROWN, fill_opacity=0.8).move_to(ORIGIN)
        ripples = VGroup(*[
            Circle(radius=0.4 + i * 0.55, color=BLUE, stroke_width=1.5, stroke_opacity=0.6 - i * 0.1)
            .move_to(ORIGIN)
            for i in range(1, 5)])
        self.add(ball, ripples)

        # Brace over ripple span
        brace = Brace(ripples[-1], direction=UP, color=BLUE)
        brace_lbl = MathTex(r"0.167\,\text{nm}", color=BLUE, font_size=30).next_to(brace, UP, buff=0.2)

        # Tiny tick at ball
        tick = Dot(radius=0.04, color="#E0DDD5").move_to(ball.get_center())
        tick_lbl = Text("÷ 60,000", font=FONT, font_size=22, color="#E0DDD5").next_to(tick, DOWN, buff=0.5)

        self.play(Create(brace), Write(brace_lbl), run_time=1.0)
        self.play(FadeIn(tick), Write(tick_lbl), run_time=0.8)
        self.wait(dur - 1.8)


class H04_CartoonDimmed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H04", 4.78)

        ball = Circle(radius=0.4, color=BROWN, fill_opacity=0.8).move_to(ORIGIN)
        ripples = VGroup(*[
            Circle(radius=0.4 + i * 0.55, color=BLUE, stroke_width=1.5, stroke_opacity=0.5 - i * 0.08)
            .move_to(ORIGIN)
            for i in range(1, 5)])
        cartoon = VGroup(ball, ripples)
        self.add(cartoon)

        self.play(cartoon.animate.set_opacity(0.35), run_time=0.6)
        question = Text("?", font=FONT, font_size=72, color=HIGHLIGHT).move_to(RIGHT * 3)
        self.play(FadeIn(question), run_time=0.4)
        self.play(Indicate(question, color=HIGHLIGHT), run_time=0.5)
        self.wait(dur - 1.5)


class M01_InterrogationRoom(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M01", 3.66)
        gun, barrier, screen = make_compact_lab()
        self.play(Create(gun), Create(barrier), Create(screen), run_time=1.0)
        self.wait(dur - 1.0)


class M02_TravelQuestion(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M02", 6.71)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Quick streaks
        for _ in range(3):
            streak = Line(gun.get_right(), screen.get_left(), color=BLUE, stroke_width=1, stroke_opacity=0.3)
            self.add(streak)

        # Striped curve
        stripe_curve = ParametricFunction(
            lambda t: np.array([4.5 + 1.5 * np.cos(t * PI / 0.6)**2, t, 0]),
            t_range=[-2.5, 2.5], color=BLUE, stroke_width=2.5)

        q1_lbl = Text("how do you travel? → stripes", font=FONT, font_size=20, color=INK)
        q1_lbl.move_to(LEFT * 4 + UP * 3.5)

        self.play(Create(stripe_curve), run_time=1.0)
        self.play(Write(q1_lbl), run_time=0.6)
        self.wait(dur - 1.6)


class M03_WhereQuestion(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M03", 6.95)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        q1_lbl = Text("how do you travel? → stripes", font=FONT, font_size=20, color=INK).move_to(LEFT * 4 + UP * 3.5)
        self.add(q1_lbl)

        # One electron, one dot
        electron = Dot(color=BLUE, radius=0.15).move_to(gun.get_center() + RIGHT * 0.5)
        hit = Dot(color="#E0DDD5", radius=0.08).move_to(RIGHT * 4.5 + UP * 0.6)

        self.play(electron.animate.move_to(LEFT * 1.5), run_time=0.4)
        self.play(electron.animate.move_to(hit.get_center()), run_time=0.4)
        self.play(ReplacementTransform(electron, hit), run_time=0.1)

        q2_lbl = Text("where are you? → one whole dot", font=FONT, font_size=20, color=INK)
        q2_lbl.next_to(q1_lbl, DOWN, buff=0.3)
        self.play(Write(q2_lbl), run_time=0.6)
        self.wait(dur - 1.5)


class S01_SecretRouteStruck(Scene):
    def construct(self):
        self.add(bg())
        dur = d("S01", 6.64)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        def gauss(t, mu, sigma=0.5):
            return 1.6 * np.exp(-(t - mu)**2 / (2 * sigma**2))

        heap_dashed = DashedVMobject(
            ParametricFunction(
                lambda t: np.array([4.5 + gauss(t, 1.0) + gauss(t, -1.0), t, 0]),
                t_range=[-3, 3], color=BROWN, stroke_width=2),
            num_dashes=20)

        self.play(Create(heap_dashed), run_time=0.8)
        strike = Line(heap_dashed.get_left() + DOWN * 1, heap_dashed.get_right() + UP * 1,
                      color="#C8102E", stroke_width=3)
        self.play(Create(strike), run_time=0.6)
        self.play(heap_dashed.animate.set_opacity(0.2), strike.animate.set_opacity(0.5), run_time=0.5)
        self.wait(dur - 1.9)


class S02_SpreadWaveStruck(Scene):
    def construct(self):
        self.add(bg())
        dur = d("S02", 7.78)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Half-dot glyph (fractional detection)
        half_dot = Arc(radius=0.4, start_angle=0, angle=PI, color=BLUE).set_fill(BLUE, 0.6).move_to(RIGHT * 4.5 + DOWN * 1.0)
        self.play(GrowFromCenter(half_dot), run_time=0.6)
        strike = Cross(half_dot, color="#C8102E", stroke_width=3)
        self.play(Create(strike), run_time=0.5)
        self.play(VGroup(half_dot, strike).animate.set_opacity(0.2), run_time=0.5)
        self.wait(dur - 1.6)


class S03_BothFail(Scene):
    def construct(self):
        self.add(bg())
        dur = d("S03", 5.69)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Both struck items already at low opacity
        self.wait(dur * 0.5)
        # Brief stillness on clean lab
        self.wait(dur * 0.5)


class A01_WavePacketGlides(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 5.28)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Clean blue wave packet
        t_track = ValueTracker(0)

        def make_packet(x_offset):
            sigma = 0.8
            return ParametricFunction(
                lambda t: np.array([x_offset + t, 0.5 * np.exp(-t**2 / (2 * sigma**2)) * np.sin(t * 5), 0]),
                t_range=[-2, 2], color=BLUE, stroke_width=3)

        packet = make_packet(-5)
        self.add(packet)

        self.play(packet.animate.shift(RIGHT * 9), run_time=dur - 0.3, rate_func=linear)


class A02_MapOfPossibility(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 6.92)

        map_lbl = Text("a map of possibility", font=FONT, font_size=32, color="#E0DDD5").move_to(UP * 0.8)
        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=60).move_to(DOWN * 0.5)

        self.play(Write(map_lbl), run_time=0.8)
        self.play(Write(psi_sq), run_time=1.0)
        self.wait(dur - 1.8)


class A03_DotIsAnswer(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A03", 5.93)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Packet arrives → dot
        sigma = 0.8
        packet = ParametricFunction(
            lambda t: np.array([-4 + t, 0.5 * np.exp(-t**2 / (2 * sigma**2)) * np.sin(t * 5), 0]),
            t_range=[-2, 2], color=BLUE, stroke_width=3)
        self.add(packet)

        hit = Dot(color="#E0DDD5", radius=0.12).move_to(RIGHT * 4.5 + UP * 0.6)

        self.play(packet.animate.shift(RIGHT * 8.5), run_time=1.5, rate_func=linear)
        self.play(GrowFromCenter(hit), FadeOut(packet), run_time=0.4)
        self.wait(dur - 1.9)


class A04_DualityDefinition(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A04", 7.34)

        line1 = Text("wave-shaped possibilities", font=FONT, font_size=30, color=BLUE).move_to(UP * 0.6)
        line2 = Text("particle-shaped results", font=FONT, font_size=30, color="#E0DDD5").move_to(DOWN * 0.3)

        self.play(Write(line1), run_time=0.8)
        self.play(Write(line2), run_time=0.8)
        self.wait(dur - 1.6)


class Y01_RepairCartoon(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y01", 7.05)

        # Hook cartoon returns, small
        ball = Circle(radius=0.25, color=BROWN, fill_opacity=0.8).move_to(LEFT * 3.5)
        ripples = VGroup(*[
            Circle(radius=0.25 + i * 0.3, color=BLUE, stroke_width=1, stroke_opacity=0.5)
            .move_to(LEFT * 3.5)
            for i in range(1, 4)])
        cartoon = VGroup(ball, ripples)
        self.add(cartoon)

        # Ball fades, ripples morph into wave packet
        sigma = 0.5
        packet = ParametricFunction(
            lambda t: np.array([LEFT[0] * 3.5 + t, 0.4 * np.exp(-t**2 / (2 * sigma**2)) * np.sin(t * 6), 0]),
            t_range=[-1.5, 1.5], color=BLUE, stroke_width=2.5)

        self.play(FadeOut(ball), run_time=0.6)
        self.play(ReplacementTransform(ripples, packet), run_time=1.0)
        self.wait(dur - 1.6)


class Y02_AlwaysWaveAlwaysDot(Scene):
    def construct(self):
        self.add(bg())
        dur = d("Y02", 8.36)
        gun, barrier, screen = make_compact_lab()
        self.add(gun, barrier, screen)

        # Repaired packet glides → dot
        sigma = 0.7
        packet = ParametricFunction(
            lambda t: np.array([-4 + t, 0.5 * np.exp(-t**2 / (2 * sigma**2)) * np.sin(t * 5), 0]),
            t_range=[-2, 2], color=BLUE, stroke_width=3)
        self.add(packet)

        hit = Dot(color="#E0DDD5", radius=0.12).move_to(RIGHT * 4.5 + UP * 0.6)

        self.play(packet.animate.shift(RIGHT * 8.5), run_time=2.5, rate_func=linear)
        self.play(GrowFromCenter(hit), FadeOut(packet), run_time=0.4)
        self.wait(dur - 2.9)


class N01_ScaleCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N01", 9.74)

        lambda_lbl = MathTex(r"\lambda = 0.167\,\text{nm}", color=BLUE, font_size=44).move_to(UP * 0.8)
        atom_scale = Text("atom-spacing scale", font=FONT, font_size=28, color="#E0DDD5").move_to(DOWN * 0.3)

        self.play(Write(lambda_lbl), run_time=1.0)
        self.play(Write(atom_scale), run_time=0.7)
        self.wait(dur - 1.7)


class N02_ChipsAndLasers(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N02", 9.14)

        lambda_lbl = MathTex(r"\lambda = 0.167\,\text{nm}", color=BLUE, font_size=38).move_to(UP * 1.2)
        atom_scale = Text("atom-spacing scale", font=FONT, font_size=24, color="#E0DDD5").move_to(UP * 0.4)
        self.add(lambda_lbl, atom_scale)

        chip_lbl = Text("chips & lasers are built on the wave", font=FONT, font_size=26, color="#888888")
        chip_lbl.move_to(DOWN * 0.6)
        self.play(Write(chip_lbl), run_time=0.8)
        self.wait(dur - 0.8)


class B01_CloseCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B01", 6.11)

        line1 = Text("wave-shaped possibilities", font=FONT, font_size=28, color=BLUE).move_to(UP * 1.2)
        line2 = Text("particle-shaped results", font=FONT, font_size=28, color="#E0DDD5").move_to(UP * 0.4)
        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=44).move_to(DOWN * 0.4)

        tag1 = Text("next · the wave function", font=FONT, font_size=22, color="#888888").move_to(DOWN * 1.5)
        tag2 = Text("next · Schrödinger's equation", font=FONT, font_size=22, color="#888888").move_to(DOWN * 2.2)

        self.play(Write(line1), Write(line2), run_time=0.8)
        self.play(Write(psi_sq), run_time=0.5)
        self.play(LaggedStart(FadeIn(tag1), FadeIn(tag2), lag_ratio=0.3), run_time=0.7)
        self.wait(dur - 2.0)


class B02_Exercise(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B02", 5.98)

        line1 = Text("wave-shaped possibilities / particle-shaped results",
                     font=FONT, font_size=22, color="#E0DDD5").move_to(UP * 2.5)
        self.add(line1)

        exercise = Text(
            "Find a ball-with-ripples picture in a textbook or video,\nand say precisely what it gets wrong.",
            font=FONT, font_size=26, color=HIGHLIGHT, line_spacing=1.4).move_to(ORIGIN)

        self.play(Write(exercise), run_time=1.5)
        self.wait(dur - 1.5)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 6.71)

        line1 = Text("wave-shaped possibilities", font=FONT, font_size=26, color=BLUE).move_to(UP * 1.5)
        line2 = Text("particle-shaped results", font=FONT, font_size=26, color="#E0DDD5").move_to(UP * 0.7)
        psi_sq = MathTex(r"|\psi|^2", color=BLUE, font_size=38).move_to(DOWN * 0.1)
        self.add(line1, line2, psi_sq)

        title = Text("What Wave–Particle Duality Actually Means",
                     font=FONT, font_size=24, color="#E0DDD5", fill_opacity=0.7).move_to(UP * 3.5)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(dur - 0.5)
