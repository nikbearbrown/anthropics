import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

# Bears Notes worked-example palette
CANVAS = "#F8F6F0"
INK_DARK = "#1a1a1a"
ACCENT = "#5A5653"   # warm slate
RED = "#C0392B"      # forbidden / n^2 highlight
MATH_FONT = "Shadows Into Light"

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

def make_ladder(n_rungs=4, spacing=0.9, even=True):
    """Return a VGroup of horizontal rungs. even=True → equal spacing."""
    rungs = VGroup()
    for i in range(n_rungs):
        if even:
            y = -1.5 + i * spacing
        else:
            y = -1.5 + (i**2) * 0.4   # n^2 spacing
        rungs.add(Line(LEFT * 0.7, RIGHT * 0.7, color=ACCENT, stroke_width=3).move_to(UP * y))
    return rungs

def make_box_and_wave(n=1, box_center=LEFT * 3, width=2.5, height=1.5):
    left_wall = Line(box_center + LEFT * width / 2 + DOWN * height / 2,
                     box_center + LEFT * width / 2 + UP * height / 2,
                     color=INK_DARK, stroke_width=3)
    right_wall = Line(box_center + RIGHT * width / 2 + DOWN * height / 2,
                      box_center + RIGHT * width / 2 + UP * height / 2,
                      color=INK_DARK, stroke_width=3)
    wave = ParametricFunction(
        lambda t: np.array([
            box_center[0] - width / 2 + (t + 1) * width / 2,
            (height * 0.35) * np.sin(n * PI * t),
            0]),
        t_range=[-1, 1], color=ACCENT, stroke_width=2.5)
    return VGroup(left_wall, right_wall), wave


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 3.86)

        # Energy ladder fan motif
        ladder_hero = make_ladder(5, even=False)
        ladder_hero.scale(0.7).move_to(LEFT * 5.5)

        series = Text("Bear's Notes", font=FONT, font_size=28, color=ACCENT).move_to(UP * 1.5)
        title = Text("Why Quantum Energy Levels Grow as n²",
                     font=FONT, font_size=36, color=INK_DARK).move_to(DOWN * 0.0)

        self.play(FadeIn(series), Create(ladder_hero), Write(title), run_time=1.5)
        self.wait(dur - 1.5)


class H01_EvenLadder(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 5.08)

        ladder = make_ladder(4, spacing=0.9, even=True).move_to(ORIGIN)
        narr = ink("You'd expect a ladder to be evenly spaced.", 26).move_to(UP * 3)

        self.play(Write(narr), run_time=0.6)
        self.play(Create(ladder), run_time=0.8)
        self.wait(dur - 1.4)


class H02_FanningLadder(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 3.95)

        # n^2 spaced rungs
        rungs = VGroup(*[
            Line(LEFT * 0.7, RIGHT * 0.7, color=ACCENT, stroke_width=3)
            .move_to(UP * (-1.8 + i**2 * 0.45))
            for i in range(1, 5)])
        narr = ink("But a quantum box's rungs fan apart.", 26).move_to(UP * 3)

        self.play(Write(narr), run_time=0.5)
        self.play(Create(rungs), run_time=0.8)
        self.wait(dur - 1.3)


class A01_BoxAndFirstWave(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 4.95)

        walls, wave = make_box_and_wave(n=1, box_center=LEFT * 1)
        n_lbl = ink("n = 1", 24).move_to(LEFT * 1 + DOWN * 1.2)

        self.play(Create(walls), run_time=0.6)
        self.play(Create(wave), Write(n_lbl), run_time=0.6)
        self.wait(dur - 1.2)


class A02_WaveMorphs(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 4.2)

        walls, _ = make_box_and_wave(n=1, box_center=LEFT * 1)
        self.add(walls)

        n_tracker = ValueTracker(1)
        n_lbl = always_redraw(lambda: ink(f"n = {int(n_tracker.get_value())}", 24).move_to(LEFT * 1 + DOWN * 1.2))

        wave = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                LEFT[0] * 1 - 1.25 + (t + 1) * 1.25,
                0.5 * np.sin(int(n_tracker.get_value()) * PI * t),
                0]),
            t_range=[-1, 1], color=ACCENT, stroke_width=2.5))

        self.add(wave, n_lbl)
        for n in [2, 3, 4]:
            self.play(n_tracker.animate.set_value(n), run_time=0.8)
        self.wait(dur - 3 * 0.8)


class A03_EnergyAxis(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A03", 3.97)

        walls, wave = make_box_and_wave(n=3, box_center=LEFT * 2.5)
        self.add(walls, wave)

        # Energy axis on the right with rungs at 1,4,9,16
        axis = NumberLine(x_range=[0, 18, 4], length=5,
                          color=INK_DARK, include_ticks=False).rotate(PI/2).move_to(RIGHT * 2)

        rung_labels = [(1, "1"), (4, "4"), (9, "9"), (16, "16")]
        rungs = VGroup(*[
            VGroup(
                Line(LEFT * 0.4, RIGHT * 0.4, color=ACCENT, stroke_width=2.5)
                .move_to(axis.n2p(val)),
                ink(lbl, 20, color=RED).next_to(axis.n2p(val), RIGHT, buff=0.3)
            )
            for val, lbl in rung_labels])

        self.play(Create(axis), run_time=0.5)
        self.play(LaggedStart(*[Create(r) for r in rungs], lag_ratio=0.2), run_time=1.0)
        self.wait(dur - 1.5)


class A04_GapArrows(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A04", 3.2)

        axis = NumberLine(x_range=[0, 18, 4], length=5,
                          color=INK_DARK, include_ticks=False).rotate(PI/2).move_to(RIGHT * 2)
        rungs = VGroup(*[
            Line(LEFT * 0.4, RIGHT * 0.4, color=ACCENT, stroke_width=2.5).move_to(axis.n2p(val))
            for val in [1, 4, 9, 16]])
        self.add(axis, rungs)

        # Gap arrows
        gaps = [(1, 4, "3"), (4, 9, "5"), (9, 16, "7")]
        gap_arrows = VGroup(*[
            VGroup(
                DoubleArrow(axis.n2p(a) + LEFT * 0.7, axis.n2p(b) + LEFT * 0.7,
                            color=RED, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.15),
                MathTex(lbl, color=RED, font_size=24).move_to(axis.n2p((a + b) / 2) + LEFT * 1.3)
            )
            for a, b, lbl in gaps])

        self.play(Create(gap_arrows), run_time=0.8)
        self.wait(dur - 0.8)


class M01_CleanSlate(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M01", 2.82)

        walls, wave = make_box_and_wave(n=2, box_center=LEFT * 3)
        narr = ink("Let's turn that picture into a formula.", 26).move_to(UP * 3)

        self.play(Write(narr), Create(walls), Create(wave), run_time=0.8)
        self.wait(dur - 0.8)


class M02_LabelLAndHalfWaves(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M02", 3.9)

        walls, wave = make_box_and_wave(n=2, box_center=LEFT * 3)
        self.add(walls, wave)

        # L brace
        brace = Brace(VGroup(walls[0], walls[1]), direction=DOWN, color=INK_DARK)
        l_lbl = MathTex(r"L", color=INK_DARK, font_size=36).next_to(brace, DOWN, buff=0.2)
        n_lbl = ink("n half-waves", 22).move_to(LEFT * 3 + UP * 0.8)

        self.play(Create(brace), Write(l_lbl), Write(n_lbl), run_time=0.8)
        self.wait(dur - 0.8)


class M03_LambdaFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M03", 3.65)

        walls, wave = make_box_and_wave(n=2, box_center=LEFT * 3.5)
        brace = Brace(VGroup(walls[0], walls[1]), direction=DOWN, color=INK_DARK)
        l_lbl = MathTex(r"L", color=INK_DARK, font_size=32).next_to(brace, DOWN, buff=0.15)
        self.add(walls, wave, brace, l_lbl)

        eq = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=48).move_to(RIGHT * 2 + UP * 1.5)
        self.play(Write(eq), run_time=1.0)
        self.wait(dur - 1.0)


class M04_ShorterLambda(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M04", 3.07)

        walls, wave = make_box_and_wave(n=2, box_center=LEFT * 3.5)
        brace = Brace(VGroup(walls[0], walls[1]), direction=DOWN, color=INK_DARK)
        l_lbl = MathTex(r"L", color=INK_DARK, font_size=32).next_to(brace, DOWN, buff=0.15)
        eq = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=44).move_to(RIGHT * 2 + UP * 1.5)
        self.add(walls, wave, brace, l_lbl, eq)

        self.play(Indicate(eq, color=ACCENT), run_time=0.6)
        # Wave compresses slightly to show n grows
        _, wave2 = make_box_and_wave(n=3, box_center=LEFT * 3.5)
        self.play(Transform(wave, wave2), run_time=0.8)
        self.wait(dur - 1.4)


class M05_MomentumFromLambda(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M05", 4.59)

        eq1 = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=44).move_to(UP * 1.5)
        self.add(eq1)

        eq2 = MathTex(r"p = \frac{h}{\lambda}", color=INK_DARK, font_size=44).move_to(UP * 0.2)
        self.play(Write(eq2), run_time=1.0)
        self.wait(dur - 1.0)


class M06_KineticEnergy(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M06", 5.4)

        eq1 = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=38).move_to(UP * 2.0)
        eq2 = MathTex(r"p = \frac{h}{\lambda}", color=INK_DARK, font_size=38).move_to(UP * 1.0)
        self.add(eq1, eq2)

        eq3 = MathTex(r"E = \frac{p^2}{2m}", color=INK_DARK, font_size=44).move_to(DOWN * 0.3)
        self.play(Write(eq3), run_time=1.0)
        self.wait(dur - 1.0)


class M07_Substitute(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M07", 3.29)

        eq1 = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=36).move_to(UP * 2.2)
        eq2 = MathTex(r"p = \frac{h}{\lambda}", color=INK_DARK, font_size=36).move_to(UP * 1.3)
        eq3 = MathTex(r"E = \frac{p^2}{2m}", color=INK_DARK, font_size=36).move_to(UP * 0.4)
        self.add(eq1, eq2, eq3)

        eq_sub = MathTex(r"E_n = \frac{(h/\lambda_n)^2}{2m}", color=ACCENT, font_size=40).move_to(DOWN * 0.8)
        self.play(Write(eq_sub), run_time=0.8)
        self.wait(dur - 0.8)


class M08_ResultFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M08", 4.5)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=56).move_to(ORIGIN)
        box = SurroundingRectangle(result, color=ACCENT, stroke_width=2.5, buff=0.3)

        self.play(Write(result), run_time=1.2)
        self.play(Create(box), run_time=0.6)
        self.wait(dur - 1.8)


class M09_HighlightNSquared(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M09", 7.02)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=52).move_to(UP * 0.5)
        box = SurroundingRectangle(result, color=ACCENT, stroke_width=2.5, buff=0.3)
        self.add(result, box)

        self.play(Indicate(result, color=RED, scale_factor=1.15), run_time=0.6)

        # Trace n^2 back to lambda_n = 2L/n
        lambda_eq = MathTex(r"\lambda_n = \frac{2L}{n}", color=ACCENT, font_size=34).move_to(DOWN * 1.5)
        arrow = Arrow(result.get_bottom(), lambda_eq.get_top(), color=RED, buff=0.2, stroke_width=2)
        self.play(Write(lambda_eq), Create(arrow), run_time=1.0)
        self.wait(dur - 1.6)


class W01_NumberSetup(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 2.67)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=44).move_to(UP * 2.5)
        narr = ink("Now let's put real numbers on it.", 26).move_to(ORIGIN)

        self.play(Write(result), Write(narr), run_time=0.8)
        self.wait(dur - 0.8)


class W02_GivensElectron(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 3.46)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=40).move_to(UP * 2.5)
        self.add(result)

        givens = MathTex(r"L = 1\,\text{nm},\quad m = m_e", color=INK_DARK, font_size=36).move_to(UP * 0.8)
        self.play(Write(givens), run_time=0.8)
        self.wait(dur - 0.8)


class W03_E1Computed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W03", 5.16)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=38).move_to(UP * 2.5)
        givens = MathTex(r"L = 1\,\text{nm},\quad m = m_e", color=INK_DARK, font_size=32).move_to(UP * 1.6)
        self.add(result, givens)

        e1 = MathTex(r"E_1 \approx 0.38\,\text{eV}", color=ACCENT, font_size=40).move_to(UP * 0.3)
        self.play(Write(e1), run_time=0.8)

        # Mark rung on a mini axis
        mini_axis = NumberLine(x_range=[0, 7, 1], length=4,
                               color=INK_DARK, include_ticks=False).rotate(PI/2).move_to(RIGHT * 4)
        rung1 = Line(RIGHT * 3.7, RIGHT * 4.3, color=ACCENT, stroke_width=3).move_to(mini_axis.n2p(0.38))
        rung1_lbl = MathTex(r"E_1", color=ACCENT, font_size=24).next_to(rung1, LEFT, buff=0.2)
        self.play(Create(mini_axis), Create(rung1), Write(rung1_lbl), run_time=0.8)
        self.wait(dur - 1.6)


class W04_E2Computed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W04", 4.82)

        result = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=36).move_to(UP * 2.8)
        e1 = MathTex(r"E_1 \approx 0.38\,\text{eV}", color=ACCENT, font_size=36).move_to(UP * 1.8)
        self.add(result, e1)

        e2 = MathTex(r"E_2 = 4 E_1 \approx 1.5\,\text{eV}", color=ACCENT, font_size=40).move_to(UP * 0.5)
        self.play(Write(e2), run_time=0.8)

        mini_axis = NumberLine(x_range=[0, 7, 1], length=4,
                               color=INK_DARK, include_ticks=False).rotate(PI/2).move_to(RIGHT * 4)
        rung1 = Line(RIGHT * 3.7, RIGHT * 4.3, color=ACCENT, stroke_width=2.5).move_to(mini_axis.n2p(0.38))
        rung2 = Line(RIGHT * 3.7, RIGHT * 4.3, color=ACCENT, stroke_width=2.5).move_to(mini_axis.n2p(1.5))
        self.play(Create(mini_axis), Create(rung1), Create(rung2), run_time=0.6)
        self.wait(dur - 1.4)


class W05_GapArrow(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W05", 5.44)

        e1 = MathTex(r"E_1 \approx 0.38\,\text{eV}", color=ACCENT, font_size=36).move_to(UP * 2.5)
        e2 = MathTex(r"E_2 \approx 1.5\,\text{eV}", color=ACCENT, font_size=36).move_to(UP * 1.5)
        self.add(e1, e2)

        delta_e = MathTex(r"\Delta E = E_2 - E_1 \approx 1.1\,\text{eV}", color=RED, font_size=40)
        delta_e.move_to(DOWN * 0.0)

        mini_axis = NumberLine(x_range=[0, 7, 1], length=4,
                               color=INK_DARK, include_ticks=False).rotate(PI/2).move_to(RIGHT * 4)
        rung1 = Line(RIGHT * 3.7, RIGHT * 4.3, color=ACCENT, stroke_width=2.5).move_to(mini_axis.n2p(0.38))
        rung2 = Line(RIGHT * 3.7, RIGHT * 4.3, color=ACCENT, stroke_width=2.5).move_to(mini_axis.n2p(1.5))
        gap_arr = DoubleArrow(mini_axis.n2p(0.38) + LEFT * 0.5, mini_axis.n2p(1.5) + LEFT * 0.5,
                              color=RED, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.12)
        self.add(mini_axis, rung1, rung2)

        self.play(Write(delta_e), Create(gap_arr), run_time=0.8)
        self.wait(dur - 0.8)


class W06_PhotonEmitted(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W06", 3.11)

        delta_e = MathTex(r"\Delta E \approx 1.1\,\text{eV}", color=RED, font_size=40).move_to(UP * 1.0)
        self.add(delta_e)

        # Wavy photon arrow
        photon = ParametricFunction(
            lambda t: np.array([t, 0.2 * np.sin(t * 8), 0]),
            t_range=[-2, 2], color=ACCENT, stroke_width=3).move_to(DOWN * 0.5)
        photon_tip = Triangle(color=ACCENT, fill_opacity=1).scale(0.15).next_to(photon, RIGHT, buff=0)
        photon_lbl = ink("photon", 22).next_to(photon_tip, RIGHT, buff=0.2)

        self.play(Create(photon), FadeIn(photon_tip), Write(photon_lbl), run_time=0.8)
        self.wait(dur - 0.8)


class W07_PhotonWavelength(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W07", 4.74)

        delta_e = MathTex(r"\Delta E \approx 1.1\,\text{eV}", color=RED, font_size=36).move_to(UP * 2.0)
        self.add(delta_e)

        lam_eq = MathTex(r"\lambda = \frac{hc}{\Delta E} \approx 1100\,\text{nm}", color=ACCENT, font_size=44)
        lam_eq.move_to(UP * 0.5)
        self.play(Write(lam_eq), run_time=1.0)
        self.wait(dur - 1.0)


class W08_NearIR(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W08", 3.95)

        lam_eq = MathTex(r"\lambda \approx 1100\,\text{nm}", color=ACCENT, font_size=40).move_to(UP * 1.5)
        self.add(lam_eq)

        # Spectrum strip
        spec = Rectangle(width=8, height=0.5, color=INK_DARK, stroke_width=1.5).move_to(ORIGIN)
        # Color gradient suggestion via labels
        uv_lbl = ink("UV", 18, color=INK_DARK).move_to(spec.get_left() + RIGHT * 0.5)
        vis_lbl = ink("visible", 18, color=INK_DARK).move_to(spec.get_center())
        ir_lbl = ink("IR", 18, color=INK_DARK).move_to(spec.get_right() + LEFT * 0.5)

        marker = Triangle(color=RED, fill_opacity=1).scale(0.18)
        marker.move_to(spec.get_right() + LEFT * 0.7 + DOWN * 0.5)
        marker_lbl = MathTex(r"1100\,\text{nm}", color=RED, font_size=22).next_to(marker, DOWN, buff=0.2)

        self.play(Create(spec), FadeIn(uv_lbl), FadeIn(vis_lbl), FadeIn(ir_lbl), run_time=0.6)
        self.play(GrowFromCenter(marker), Write(marker_lbl), run_time=0.5)
        self.wait(dur - 1.1)


class P01_QuantumDot(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P01", 3.05)

        qdot = Square(side_length=0.8, color=ACCENT, fill_opacity=0.6).move_to(ORIGIN)
        qdot_lbl = ink("quantum dot", 24).next_to(qdot, DOWN, buff=0.3)

        self.play(GrowFromCenter(qdot), Write(qdot_lbl), run_time=0.7)
        self.wait(dur - 0.7)


class P02_ScalingRelation(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P02", 4.42)

        qdot = Square(side_length=0.7, color=ACCENT, fill_opacity=0.6).move_to(UP * 1.5)
        qdot_lbl = ink("quantum dot", 22).next_to(qdot, DOWN, buff=0.2)
        self.add(qdot, qdot_lbl)

        scaling = MathTex(r"E \propto \frac{1}{L^2}", color=RED, font_size=52).move_to(DOWN * 0.3)
        self.play(Write(scaling), run_time=1.0)
        self.wait(dur - 1.0)


class P03_SmallBlueVsLargeRed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P03", 4.63)

        # Small dot (high energy → blue glow)
        small_box = Square(side_length=0.5, color="#2222CC", fill_opacity=0.7).move_to(LEFT * 3)
        small_lbl = ink("small → blue", 22, color="#2222CC").next_to(small_box, DOWN, buff=0.3)
        small_rungs = VGroup(*[
            Line(LEFT * 3.4, LEFT * 2.6, color="#2222CC", stroke_width=2)
            .move_to(small_box.get_center() + RIGHT * 3.2 + UP * (i * 0.5 - 0.5))
            for i in range(4)])

        # Large dot (low energy → red glow)
        large_box = Square(side_length=1.2, color=RED, fill_opacity=0.5).move_to(RIGHT * 3)
        large_lbl = ink("large → red", 22, color=RED).next_to(large_box, DOWN, buff=0.3)
        large_rungs = VGroup(*[
            Line(RIGHT * 2.2, RIGHT * 3.8, color=RED, stroke_width=2)
            .move_to(large_box.get_center() + LEFT * 0.5 + RIGHT * 4 + UP * (i * 0.25 - 0.25))
            for i in range(3)])

        self.play(GrowFromCenter(small_box), Write(small_lbl), GrowFromCenter(large_box), Write(large_lbl), run_time=0.7)
        self.play(Create(small_rungs), Create(large_rungs), run_time=0.6)
        self.wait(dur - 1.3)


class P04_FormulaCallbackWithDots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P04", 4.01)

        formula = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=48).move_to(ORIGIN)
        box = SurroundingRectangle(formula, color=ACCENT, stroke_width=2, buff=0.25)

        self.play(Write(formula), Create(box), run_time=1.2)
        self.wait(dur - 1.2)


class R01_RecapEsimP2(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R01", 5.42)

        recap = ink("Rungs fan as n² because E lives in p².", 26).move_to(UP * 1.5)
        eq = MathTex(r"E \sim p^2", color=ACCENT, font_size=52).move_to(DOWN * 0.2)

        fanladder = VGroup(*[
            Line(LEFT * 0.6, RIGHT * 0.6, color=ACCENT, stroke_width=2.5)
            .move_to(RIGHT * 4 + UP * (-1.4 + i**2 * 0.42))
            for i in range(1, 5)])

        self.play(Write(recap), Write(eq), Create(fanladder), run_time=1.2)
        self.wait(dur - 1.2)


class R02_MomentumClimbs(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R02", 4.01)

        recap = ink("Momentum climbs with every half-wave you add.", 26).move_to(UP * 2.5)
        self.add(recap)

        # Box with wave adding half-waves
        walls, wave1 = make_box_and_wave(n=1, box_center=LEFT * 3)
        _, wave3 = make_box_and_wave(n=3, box_center=LEFT * 3)

        p_lbl1 = MathTex(r"p_1", color=INK_DARK, font_size=28).move_to(LEFT * 3 + DOWN * 1.3)
        p_lbl3 = MathTex(r"p_3", color=RED, font_size=28).move_to(LEFT * 3 + DOWN * 1.3)

        self.add(walls, wave1, p_lbl1)
        self.play(Transform(wave1, wave3), Transform(p_lbl1, p_lbl3), run_time=1.0)
        self.wait(dur - 1.0)


class R03_FinalFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R03", 3.88)

        formula = MathTex(r"E_n = \frac{n^2 h^2}{8 m L^2}", color=ACCENT, font_size=60).move_to(ORIGIN)
        box = SurroundingRectangle(formula, color=ACCENT, stroke_width=2.5, buff=0.35)

        self.play(Write(formula), Create(box), run_time=1.2)
        self.wait(dur - 1.2)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 5.48)

        thanks = ink("Thanks for watching", 28).move_to(UP * 1.5)
        title_lbl = ink("Particle in a Box: Where the n² Energy Formula Comes From", 22).move_to(UP * 0.4)
        channel = ink("youtube.com/@NikBearBrown", 22, color=ACCENT).move_to(DOWN * 0.5)

        self.play(Write(thanks), Write(title_lbl), Write(channel), run_time=1.2)
        self.wait(dur - 1.2)
