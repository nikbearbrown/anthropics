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

def make_axes():
    axes = Axes(
        x_range=[0, 10, 2], y_range=[0, 6, 2],
        x_length=7, y_length=4.5,
        axis_config={"color": INK_DARK, "include_ticks": False},
        tips=True)
    axes.move_to(LEFT * 0.5 + DOWN * 0.5)
    x_lbl = Text("frequency →", font=FONT, font_size=20, color=INK_DARK).next_to(axes, DOWN, buff=0.3)
    y_lbl = Text("brightness", font=FONT, font_size=20, color=INK_DARK).next_to(axes, LEFT, buff=0.2)
    return axes, x_lbl, y_lbl

def planck_curve(axes, nu0=3.5, amplitude=2.2):
    def planck(x):
        if x < 0.05: return 0
        return amplitude * x**3 / (np.exp(x / nu0) - 1 + 1e-9)
    return axes.plot(planck, x_range=[0.05, 10], color=ACCENT, stroke_width=3)

def rj_curve(axes, amplitude=0.07):
    return axes.plot(lambda x: amplitude * x**2, x_range=[0, 10],
                     color=RED, stroke_width=3)


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 5.09)

        series = acc("Bear's Notes", 28).move_to(UP * 2.0)
        title = ink("The Ultraviolet Catastrophe: Why Quantizing Energy Fixes It", 28).move_to(UP * 0.8)

        # Motif: two curves
        axes, x_lbl, y_lbl = make_axes()
        axes.scale(0.4).move_to(RIGHT * 4 + DOWN * 0.5)

        self.play(Write(series), Write(title), run_time=1.2)
        self.wait(dur - 1.2)


class H01_ClassicalRunaway(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 4.44)

        narr = ink("Classical physics said a warm object's glow should blast you with UV.", 24).move_to(UP * 3)
        axes, x_lbl, y_lbl = make_axes()
        self.play(Write(narr), Create(axes), Write(x_lbl), Write(y_lbl), run_time=0.8)
        rj = rj_curve(axes)
        self.play(Create(rj), run_time=0.8)
        self.wait(dur - 1.6)


class H02_PlanckFixes(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 4.13)

        narr = ink("It doesn't — Planck's fix: energy in chunks.", 26).move_to(UP * 3)
        axes, x_lbl, y_lbl = make_axes()
        self.play(Write(narr), Create(axes), Write(x_lbl), Write(y_lbl), run_time=0.6)
        planck = planck_curve(axes)
        self.play(Create(planck), run_time=0.8)
        self.wait(dur - 1.4)


class A01_RealCurvePlot(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 5.09)

        axes, x_lbl, y_lbl = make_axes()
        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=0.6)

        planck = planck_curve(axes)
        self.play(Create(planck), run_time=1.5)
        self.wait(dur - 2.1)


class A02_RunawayShoots(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 4.68)

        axes, x_lbl, y_lbl = make_axes()
        planck = planck_curve(axes)
        self.add(axes, x_lbl, y_lbl, planck)

        rj = rj_curve(axes)
        rj_lbl = Text("classical: ultraviolet catastrophe", font=FONT, font_size=20, color=RED)
        rj_lbl.move_to(RIGHT * 4 + UP * 2.5)

        self.play(Create(rj), Write(rj_lbl), run_time=1.2)
        self.wait(dur - 1.2)


class M01_BrokenStep(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M01", 2.27)

        axes, x_lbl, y_lbl = make_axes()
        axes.scale(0.55).move_to(LEFT * 3.5 + DOWN * 0.5)
        self.add(axes, x_lbl.scale(0.55).next_to(axes, DOWN, buff=0.2),
                 y_lbl.scale(0.55).next_to(axes, LEFT, buff=0.15))

        narr = ink("Here's the broken step, and the fix.", 26).move_to(UP * 3)
        self.play(Write(narr), run_time=0.5)
        self.wait(dur - 0.5)


class M02_EquipartitionKT(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M02", 3.94)

        eq = MathTex(r"\bar{E} = kT", color=ACCENT, font_size=52).move_to(RIGHT * 3 + UP * 1.5)
        lbl = ink("each mode gets kT", 24).move_to(RIGHT * 3 + UP * 0.5)

        self.play(Write(eq), Write(lbl), run_time=0.8)
        self.wait(dur - 0.8)


class M03_ModeDivergence(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M03", 4.26)

        eq1 = MathTex(r"\bar{E} = kT", color=ACCENT, font_size=44).move_to(RIGHT * 3 + UP * 2.2)
        self.add(eq1)

        eq2 = MathTex(r"u \propto f^2 \cdot kT", color=RED, font_size=44).move_to(RIGHT * 3 + UP * 0.7)
        lbl = ink("→ diverges as f² × kT", 22, color=RED).move_to(RIGHT * 3 + DOWN * 0.2)

        self.play(Write(eq2), Write(lbl), run_time=1.0)
        self.wait(dur - 1.0)


class M04_PlanckRule(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M04", 4.08)

        eq1 = MathTex(r"u \propto f^2 \cdot kT", color=RED, font_size=38).move_to(UP * 2.5)
        self.add(eq1)

        eq2 = MathTex(r"E = hf", color=ACCENT, font_size=56).move_to(UP * 0.5)
        box = SurroundingRectangle(eq2, color=ACCENT, stroke_width=2.5, buff=0.3)
        lbl = ink("Planck's rule: energy in chunks", 24).move_to(DOWN * 0.8)

        self.play(Write(eq2), Create(box), Write(lbl), run_time=1.0)
        self.wait(dur - 1.0)


class M05_BoltzmannSuppression(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M05", 7.18)

        eq1 = MathTex(r"E = hf", color=ACCENT, font_size=44).move_to(UP * 2.5)
        self.add(eq1)

        supp = MathTex(r"e^{-hf/kT}", color=RED, font_size=52).move_to(UP * 0.5)
        lbl = ink("high-f modes: exponentially suppressed", 24).move_to(DOWN * 0.6)

        self.play(Write(supp), Write(lbl), run_time=1.2)

        # Visual: a bar that shrinks as hf/kT grows
        axes = NumberLine(x_range=[0, 200, 50], length=6, color=INK_DARK,
                          include_ticks=True, tick_size=0.08).move_to(DOWN * 2.0)
        x_lbl = ink("hf/kT ratio", 18).next_to(axes, DOWN, buff=0.2)
        self.play(Create(axes), Write(x_lbl), run_time=0.5)

        bar = Rectangle(width=2.5, height=0.4, color=ACCENT, fill_opacity=0.8)
        bar.align_to(axes.n2p(0), LEFT).move_to(axes.n2p(0) + UP * 0.3 + RIGHT * 1.25)
        self.play(GrowFromEdge(bar, LEFT), run_time=0.5)
        self.play(bar.animate.stretch_to_fit_width(0.05).set_opacity(0.1), run_time=1.0)
        self.wait(dur - 3.2)


class M06_PlanckLaw(Scene):
    def construct(self):
        self.add(bg())
        dur = d("M06", 2.59)

        eq1 = MathTex(r"E = hf", color=ACCENT, font_size=40).move_to(UP * 2.5)
        self.add(eq1)

        planck_law = MathTex(r"u \propto \frac{f^3}{e^{hf/kT}-1}", color=ACCENT, font_size=48).move_to(UP * 0.5)
        lbl = ink("peaks and falls to zero", 24).move_to(DOWN * 0.8)

        self.play(Write(planck_law), Write(lbl), run_time=0.8)
        self.wait(dur - 0.8)


class W01_RoomTemp(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 2.82)

        narr = ink("Numbers at room temperature, T = 300 K.", 26).move_to(UP * 2)
        given = MathTex(r"T = 300\,\text{K}", color=INK_DARK, font_size=44).move_to(UP * 0.3)

        self.play(Write(narr), Write(given), run_time=0.7)
        self.wait(dur - 0.7)


class W02_KTComputed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 4.26)

        given = MathTex(r"T = 300\,\text{K}", color=INK_DARK, font_size=38).move_to(UP * 2.5)
        self.add(given)

        kt_eq = MathTex(r"kT \approx 0.026\,\text{eV}", color=ACCENT, font_size=44).move_to(UP * 0.8)
        self.play(Write(kt_eq), run_time=0.8)
        self.wait(dur - 0.8)


class W03_UVRatio(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W03", 4.36)

        kt_eq = MathTex(r"kT \approx 0.026\,\text{eV}", color=ACCENT, font_size=38).move_to(UP * 2.5)
        self.add(kt_eq)

        ratio = MathTex(r"\frac{hf}{kT} \approx \frac{5}{0.026} \approx 193", color=RED, font_size=40)
        ratio.move_to(UP * 0.8)
        lbl = ink("UV chunk is 193× the thermal budget", 24, color=RED).move_to(DOWN * 0.3)

        self.play(Write(ratio), Write(lbl), run_time=1.0)
        self.wait(dur - 1.0)


class W04_ExponentialSuppression(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W04", 6.53)

        ratio = MathTex(r"\frac{hf}{kT} \approx 193", color=RED, font_size=38).move_to(UP * 2.5)
        self.add(ratio)

        supp = MathTex(r"e^{-193} \sim 10^{-84}", color=RED, font_size=52).move_to(UP * 0.8)
        lbl = ink("Essentially no ultraviolet at all.", 26).move_to(DOWN * 0.5)

        self.play(Write(supp), run_time=1.0)
        self.play(Write(lbl), run_time=0.6)
        self.wait(dur - 1.6)


class W05_WiensLaw(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W05", 5.15)

        wien = MathTex(r"\lambda_{\max} = \frac{b}{T}", color=ACCENT, font_size=52).move_to(UP * 1.0)
        self.play(Write(wien), run_time=1.0)
        self.wait(dur - 1.0)


class W06_TwoPeaks(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W06", 8.44)

        wien = MathTex(r"\lambda_{\max} = \frac{b}{T}", color=ACCENT, font_size=40).move_to(UP * 2.8)
        self.add(wien)

        # Two peaks on a spectrum strip
        spec = Rectangle(width=9, height=0.6, color=INK_DARK, stroke_width=1.5).move_to(ORIGIN)
        uv_lbl = ink("UV", 16).move_to(spec.get_left() + RIGHT * 0.5)
        vis_lbl = ink("visible", 16).move_to(spec.get_center() + LEFT * 0.5)
        ir_lbl = ink("IR", 16).move_to(spec.get_right() + LEFT * 0.8)

        # 300 K peak at ~9.7 µm (far IR, right side)
        peak_300k = Triangle(color=INK_DARK, fill_opacity=0.8).scale(0.2).move_to(spec.get_right() + LEFT * 1.0 + DOWN * 0.55)
        lbl_300k = MathTex(r"300\,\text{K} \to 9.7\,\mu\text{m}", color=INK_DARK, font_size=22).next_to(peak_300k, DOWN, buff=0.2)

        # 5800 K peak at ~0.5 µm (visible, center)
        peak_5800k = Triangle(color=ACCENT, fill_opacity=0.8).scale(0.2).move_to(spec.get_center() + LEFT * 0.5 + DOWN * 0.55)
        lbl_5800k = MathTex(r"5800\,\text{K} \to 0.5\,\mu\text{m}", color=ACCENT, font_size=22).next_to(peak_5800k, DOWN, buff=0.2)

        self.play(Create(spec), FadeIn(uv_lbl), FadeIn(vis_lbl), FadeIn(ir_lbl), run_time=0.6)
        self.play(GrowFromCenter(peak_300k), Write(lbl_300k), run_time=0.6)
        self.play(GrowFromCenter(peak_5800k), Write(lbl_5800k), run_time=0.6)
        self.wait(dur - 1.8)


class P01_PeakSlides(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P01", 5.2)

        axes, x_lbl, y_lbl = make_axes()
        self.add(axes, x_lbl, y_lbl)

        narr = ink("Hotter → peak slides toward visible.", 26).move_to(UP * 3.3)
        self.play(Write(narr), run_time=0.5)

        # Animate peak shifting leftward as temperature rises
        nu0_tracker = ValueTracker(5.0)

        def make_planck(nu0):
            return axes.plot(
                lambda x: 2.2 * x**3 / (np.exp(x / nu0) - 1 + 1e-9) if x > 0.05 else 0,
                x_range=[0.05, 10], color=ACCENT, stroke_width=3)

        curve = make_planck(5.0)
        self.add(curve)

        for nu0 in [4.0, 3.0, 2.0]:
            new_curve = make_planck(nu0)
            self.play(Transform(curve, new_curve), run_time=0.8)

        self.wait(dur - 2.4)


class R01_BoxedFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R01", 5.28)

        eq = MathTex(r"E = hf", color=ACCENT, font_size=64).move_to(UP * 0.5)
        box = SurroundingRectangle(eq, color=ACCENT, stroke_width=2.5, buff=0.4)
        lbl = ink("starves costly high-frequency modes", 26).move_to(DOWN * 0.8)

        self.play(Write(eq), Create(box), run_time=1.0)
        self.play(Write(lbl), run_time=0.6)
        self.wait(dur - 1.6)


class R02_RecapLine(Scene):
    def construct(self):
        self.add(bg())
        dur = d("R02", 2.93)

        eq = MathTex(r"E = hf", color=ACCENT, font_size=52).move_to(UP * 1.2)
        self.add(eq)

        recap = ink("No infinity — just a peak that climbs with temperature.", 26).move_to(ORIGIN)
        self.play(Write(recap), run_time=0.6)
        self.wait(dur - 0.6)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 5.02)

        thanks = ink("Thanks for watching", 28).move_to(UP * 1.5)
        title_lbl = ink("The Ultraviolet Catastrophe: Why Quantizing Energy Fixes It", 20).move_to(UP * 0.5)
        channel = acc("youtube.com/@NikBearBrown", 22).move_to(DOWN * 0.5)

        self.play(Write(thanks), Write(title_lbl), Write(channel), run_time=1.2)
        self.wait(dur - 1.2)
