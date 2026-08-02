import json
import numpy as np
from pathlib import Path
from manim import *

CREAM = "#FAF9F5"
DARK  = "#1a1a1a"
BLUE  = "#2A6FB0"
RED   = "#C0392B"
ACNT  = "#5A5653"
FONT  = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', 'Photoelectric Effect')
except Exception:
    DUR = {}; TITLE = 'Photoelectric Effect'

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink(t, size=36, color=DARK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def red(t, size=36, color=RED, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def blue(t, size=36, color=BLUE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class INTRO_PhotoTitle(Scene):
    def construct(self):
        dur = d('INTRO', 5)
        self.add(bg())
        brand = ink("Bear's Notes", 32, color=ACNT).shift(UP * 2.8)
        title = ink("The Photoelectric Effect:", 44, color=DARK).shift(UP * 1.2)
        sub   = ink("Why Colour Beats Brightness", 36, color=BLUE).shift(UP * 0.0)
        plate = Rectangle(width=3, height=0.4, color=DARK, stroke_width=3).set_fill(DARK, 0.8).shift(DOWN * 1.2)
        photon = Dot(radius=0.2, color=BLUE, fill_opacity=1).shift(DOWN * 0.4)
        self.play(FadeIn(brand), run_time=0.4)
        self.play(FadeIn(title), FadeIn(sub), run_time=0.8)
        self.play(FadeIn(plate), FadeIn(photon), run_time=0.5)
        self.wait(max(0.1, dur - 1.7))


class H01_RedBlue(Scene):
    def construct(self):
        dur = d('H01', 5)
        self.add(bg())
        label = ink("A blinding red lamp frees no electrons —", 28).shift(UP * 3.2)
        label2 = ink("a faint blue one frees them instantly.", 28, color=BLUE).shift(UP * 2.5)
        plate = Rectangle(width=4, height=0.4, color=DARK, stroke_width=3).set_fill(DARK, 0.8).shift(DOWN * 0.5)
        # Red side
        red_dot = Dot(radius=0.22, color=RED, fill_opacity=1).shift(LEFT * 3.5 + UP * 1.0)
        red_lbl = ink("bright red", 22, color=RED).shift(LEFT * 3.5 + UP * 1.6)
        no_elec = red("✗", 36).shift(LEFT * 3.5 + DOWN * 1.4)
        # Blue side
        blue_dot = Dot(radius=0.14, color=BLUE, fill_opacity=1).shift(RIGHT * 2.5 + UP * 1.0)
        blue_lbl = ink("faint blue", 22, color=BLUE).shift(RIGHT * 2.5 + UP * 1.6)
        elec = Dot(radius=0.12, color=ACNT, fill_opacity=1).shift(RIGHT * 3.2 + DOWN * 1.2)
        arrow = Arrow(RIGHT * 2.5 + UP * 0.2, RIGHT * 3.0 + DOWN * 1.0, color=ACNT, buff=0.1, stroke_width=2)
        self.play(FadeIn(label), FadeIn(label2), run_time=0.6)
        self.play(FadeIn(plate), run_time=0.3)
        self.play(FadeIn(red_dot), FadeIn(red_lbl), FadeIn(no_elec), run_time=0.6)
        self.play(FadeIn(blue_dot), FadeIn(blue_lbl), GrowArrow(arrow), FadeIn(elec), run_time=0.8)
        self.wait(max(0.1, dur - 2.3))


class H02_Packets(Scene):
    def construct(self):
        dur = d('H02', 5)
        self.add(bg())
        label = ink("Light's energy arrives in fixed, colour-sized packets.", 30).shift(UP * 3.2)
        label.set_max_width(13)
        # Big blue packet
        b_box = Rectangle(width=1.6, height=1.6, color=BLUE, stroke_width=3).set_fill(BLUE, 0.25).shift(LEFT * 1.5)
        b_lbl = ink("blue\npacket", 24, color=BLUE).move_to(LEFT * 1.5)
        b_e   = ink("high E", 20, color=BLUE).shift(LEFT * 1.5 + DOWN * 1.2)
        # Small red packet
        r_box = Rectangle(width=0.9, height=0.9, color=RED, stroke_width=3).set_fill(RED, 0.25).shift(RIGHT * 2.5)
        r_lbl = ink("red\npacket", 22, color=RED).move_to(RIGHT * 2.5)
        r_e   = ink("low E", 20, color=RED).shift(RIGHT * 2.5 + DOWN * 0.9)
        self.play(FadeIn(label), run_time=0.4)
        self.play(FadeIn(b_box), FadeIn(b_lbl), run_time=0.5)
        self.play(FadeIn(r_box), FadeIn(r_lbl), run_time=0.5)
        self.play(FadeIn(b_e), FadeIn(r_e), run_time=0.4)
        self.wait(max(0.1, dur - 1.8))


class A01_PacketsDrop(Scene):
    def construct(self):
        dur = d('A01', 5)
        self.add(bg())
        label = ink("Each packet carries energy set by its colour.", 28).shift(UP * 3.3)
        plate = Rectangle(width=7, height=0.4, color=DARK, stroke_width=3).set_fill(DARK, 0.8).shift(DOWN * 1.5)
        pkts = VGroup(*[
            Dot(radius=0.18, color=BLUE if i % 2 == 0 else RED, fill_opacity=1)
            .shift(LEFT * 3.0 + RIGHT * i * 1.4 + UP * 1.2)
            for i in range(5)
        ])
        self.play(FadeIn(label), FadeIn(plate), run_time=0.5)
        self.play(FadeIn(pkts), run_time=0.7)
        self.play(pkts.animate.shift(DOWN * 2.4), run_time=0.8)
        self.wait(max(0.1, dur - 2.0))


class A02_Bars(Scene):
    def construct(self):
        dur = d('A02', 4)
        self.add(bg())
        label = ink("Red packets are weak; blue packets are strong.", 28).shift(UP * 3.3)
        # Energy bars
        r_bar = Rectangle(width=1.0, height=1.0, color=RED, stroke_width=2).set_fill(RED, 0.5).shift(LEFT * 2.0 + DOWN * 0.3)
        r_lbl = ink("red", 22, color=RED).shift(LEFT * 2.0 + DOWN * 1.1)
        b_bar = Rectangle(width=1.0, height=2.4, color=BLUE, stroke_width=2).set_fill(BLUE, 0.5).shift(RIGHT * 2.0 + UP * 0.4)
        b_lbl = ink("blue", 22, color=BLUE).shift(RIGHT * 2.0 + DOWN * 1.1)
        y_lbl = ink("energy", 22, color=DARK).rotate(PI/2).shift(LEFT * 4.5)
        self.play(FadeIn(label), FadeIn(y_lbl), run_time=0.4)
        self.play(FadeIn(r_bar), FadeIn(r_lbl), run_time=0.5)
        self.play(FadeIn(b_bar), FadeIn(b_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.4))


class A03_Threshold(Scene):
    def construct(self):
        dur = d('A03', 5)
        self.add(bg())
        label = ink("One packet must clear the escape energy.", 28).shift(UP * 3.3)
        # Bars
        r_bar = Rectangle(width=1.0, height=1.0, color=RED, stroke_width=2).set_fill(RED, 0.4).shift(LEFT * 2.0 + DOWN * 0.3)
        b_bar = Rectangle(width=1.0, height=2.4, color=BLUE, stroke_width=2).set_fill(BLUE, 0.4).shift(RIGHT * 2.0 + UP * 0.4)
        # Threshold line
        thr = DashedLine(LEFT * 5, RIGHT * 5, color=ACNT, stroke_width=2.5).shift(UP * 0.88)
        thr_lbl = ink("escape energy φ", 22, color=ACNT).shift(RIGHT * 4.5 + UP * 1.2)
        # Verdict labels
        r_x = red("✗ trapped", 22).shift(LEFT * 2.0 + DOWN * 1.5)
        b_ok = blue("✓ ejects!", 22).shift(RIGHT * 2.0 + DOWN * 1.5)
        self.play(FadeIn(label), FadeIn(r_bar), FadeIn(b_bar), run_time=0.6)
        self.play(Create(thr), FadeIn(thr_lbl), run_time=0.6)
        self.play(FadeIn(r_x), FadeIn(b_ok), run_time=0.5)
        self.wait(max(0.1, dur - 1.7))


class M01_FormulaIntro(Scene):
    def construct(self):
        dur = d('M01', 3)
        self.add(bg())
        label = ink("Let's turn that into a formula.", 36).shift(UP * 1.0)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(max(0.1, dur - 0.5))


class M02_EhfFormula(Scene):
    def construct(self):
        dur = d('M02', 5)
        self.add(bg())
        label = ink("A packet's energy:", 28).shift(UP * 3.0)
        f = MathTex(r"E = hf = \frac{hc}{\lambda}", font_size=72, color=DARK).shift(UP * 1.0)
        note = ink("h = Planck's constant", 24, color=ACNT).shift(DOWN * 0.8)
        self.play(FadeIn(label), Write(f), run_time=1.0)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


class M03_Phi(Scene):
    def construct(self):
        dur = d('M03', 5)
        self.add(bg())
        f = MathTex(r"E = hf = \frac{hc}{\lambda}", font_size=60, color=DARK).shift(UP * 2.5)
        phi_lbl = ink("Work function φ = escape cost", 28, color=ACNT).shift(UP * 0.5)
        phi_eq  = MathTex(r"\phi", font_size=72, color=ACNT).shift(DOWN * 0.6)
        self.play(FadeIn(f), run_time=0.4)
        self.play(FadeIn(phi_lbl), Write(phi_eq), run_time=0.8)
        self.wait(max(0.1, dur - 1.2))


class M04_Kmax(Scene):
    def construct(self):
        dur = d('M04', 5)
        self.add(bg())
        f1 = MathTex(r"E = hf = \frac{hc}{\lambda}", font_size=48, color=DARK).shift(UP * 2.8)
        phi_lbl = ink("φ = escape cost", 24, color=ACNT).shift(UP * 1.5)
        result = MathTex(r"K_{\max} = hf - \phi", font_size=72, color=DARK).shift(UP * 0.3)
        box = SurroundingRectangle(result, color=RED, stroke_width=3, buff=0.2)
        note = ink("Kinetic energy of the freed electron", 24, color=ACNT).shift(DOWN * 1.2)
        self.play(FadeIn(f1), FadeIn(phi_lbl), run_time=0.4)
        self.play(Write(result), run_time=0.8)
        self.play(Create(box), FadeIn(note), run_time=0.5)
        self.wait(max(0.1, dur - 1.7))


class M05_ThresholdFreq(Scene):
    def construct(self):
        dur = d('M05', 6)
        self.add(bg())
        f_main = MathTex(r"K_{\max} = hf - \phi", font_size=60, color=DARK).shift(UP * 2.5)
        label  = ink("Below threshold frequency f₀ — nothing escapes:", 26).shift(UP * 1.0)
        f_thr  = MathTex(r"f_0 = \frac{\phi}{h}", font_size=72, color=ACNT).shift(DOWN * 0.3)
        note   = ink("colour too low → packet always < φ", 24, color=RED).shift(DOWN * 1.8)
        self.play(FadeIn(f_main), FadeIn(label), run_time=0.5)
        self.play(Write(f_thr), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.1, dur - 1.7))


class W01_Givens(Scene):
    def construct(self):
        dur = d('W01', 6)
        self.add(bg())
        label = ink("Sodium: worked numbers", 34, color=DARK).shift(UP * 3.0)
        given = MathTex(r"\phi_{\text{Na}} \approx 2.28\ \text{eV}", font_size=60, color=ACNT).shift(UP * 1.2)
        hc_val = ink("hc = 1240 eV·nm", 26, color=DARK).shift(UP * 0.1)
        box_eq = MathTex(r"K_{\max} = hf - \phi", font_size=52, color=DARK).shift(DOWN * 1.0)
        box_r  = SurroundingRectangle(box_eq, color=RED, stroke_width=2, buff=0.15)
        self.play(FadeIn(label), Write(given), run_time=0.8)
        self.play(FadeIn(hc_val), FadeIn(box_eq), Create(box_r), run_time=0.7)
        self.wait(max(0.1, dur - 1.5))


class W02_BlueEnergy(Scene):
    def construct(self):
        dur = d('W02', 7)
        self.add(bg())
        given = MathTex(r"\phi_{\text{Na}} \approx 2.28\ \text{eV}", font_size=44, color=ACNT).shift(UP * 3.0)
        label = blue("Blue photon at 450 nm:", 28).shift(UP * 1.8)
        calc  = MathTex(r"E_{\text{blue}} = \frac{hc}{450\ \text{nm}} = \frac{1240}{450}\ \text{eV}", font_size=52, color=BLUE).shift(UP * 0.5)
        result= MathTex(r"\approx 2.76\ \text{eV}", font_size=60, color=BLUE).shift(DOWN * 0.8)
        self.play(FadeIn(given), FadeIn(label), run_time=0.5)
        self.play(Write(calc), run_time=0.8)
        self.play(Write(result), run_time=0.6)
        self.wait(max(0.1, dur - 1.9))


class W03_BlueEject(Scene):
    def construct(self):
        dur = d('W03', 7)
        self.add(bg())
        e_blue = MathTex(r"E_{\text{blue}} \approx 2.76\ \text{eV}", font_size=44, color=BLUE).shift(UP * 3.0)
        phi    = MathTex(r"\phi_{\text{Na}} \approx 2.28\ \text{eV}", font_size=44, color=ACNT).shift(UP * 2.1)
        calc   = MathTex(r"K = 2.76 - 2.28 \approx 0.48\ \text{eV}", font_size=56, color=DARK).shift(UP * 0.6)
        verdict = blue("✓ electron ejected!", 32).shift(DOWN * 0.8)
        box    = SurroundingRectangle(verdict, color=BLUE, stroke_width=2, buff=0.15)
        self.play(FadeIn(e_blue), FadeIn(phi), run_time=0.5)
        self.play(Write(calc), run_time=0.8)
        self.play(FadeIn(verdict), Create(box), run_time=0.6)
        self.wait(max(0.1, dur - 1.9))


class W04_RedEnergy(Scene):
    def construct(self):
        dur = d('W04', 7)
        self.add(bg())
        phi   = MathTex(r"\phi_{\text{Na}} \approx 2.28\ \text{eV}", font_size=44, color=ACNT).shift(UP * 3.0)
        label = red("Red photon at 700 nm:", 28).shift(UP * 1.8)
        calc  = MathTex(r"E_{\text{red}} = \frac{1240}{700}\ \text{eV}", font_size=52, color=RED).shift(UP * 0.5)
        result= MathTex(r"\approx 1.77\ \text{eV}", font_size=60, color=RED).shift(DOWN * 0.8)
        self.play(FadeIn(phi), FadeIn(label), run_time=0.5)
        self.play(Write(calc), run_time=0.8)
        self.play(Write(result), run_time=0.6)
        self.wait(max(0.1, dur - 1.9))


class W05_RedNoEject(Scene):
    def construct(self):
        dur = d('W05', 5)
        self.add(bg())
        e_red = MathTex(r"E_{\text{red}} \approx 1.77\ \text{eV}", font_size=52, color=RED).shift(UP * 2.2)
        phi   = MathTex(r"\phi_{\text{Na}} \approx 2.28\ \text{eV}", font_size=52, color=ACNT).shift(UP * 1.0)
        comp  = MathTex(r"1.77 < 2.28", font_size=64, color=RED).shift(DOWN * 0.3)
        verdict = red("✗ no ejection, ever!", 32).shift(DOWN * 1.6)
        box   = SurroundingRectangle(verdict, color=RED, stroke_width=2, buff=0.15)
        self.play(FadeIn(e_red), FadeIn(phi), run_time=0.5)
        self.play(Write(comp), run_time=0.5)
        self.play(FadeIn(verdict), Create(box), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


class W06_Cutoff(Scene):
    def construct(self):
        dur = d('W06', 7)
        self.add(bg())
        label = ink("Cutoff wavelength for sodium:", 28).shift(UP * 3.0)
        calc  = MathTex(r"\lambda_0 = \frac{hc}{\phi} = \frac{1240}{2.28}\ \text{nm}", font_size=56, color=DARK).shift(UP * 1.4)
        result= MathTex(r"\approx 544\ \text{nm}", font_size=64, color=ACNT).shift(UP * 0.0)
        # Spectrum strip
        strip_colors = [RED, "#FF6600", "#FFCC00", "#00CC44", BLUE, "#6600CC"]
        strips = VGroup(*[
            Rectangle(width=1.3, height=0.5, color=c).set_fill(c, 1.0).shift(LEFT * 3.25 + RIGHT * i * 1.3 + DOWN * 1.5)
            for i, c in enumerate(strip_colors)
        ])
        marker = DashedLine(DOWN * 1.1, DOWN * 2.0, color=DARK, stroke_width=3).shift(RIGHT * 0.4)
        mk_lbl = ink("544 nm", 20, color=DARK).shift(RIGHT * 0.4 + DOWN * 2.3)
        self.play(FadeIn(label), Write(calc), run_time=0.8)
        self.play(Write(result), run_time=0.5)
        self.play(FadeIn(strips), Create(marker), FadeIn(mk_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 2.0))


class P01_ManyRed(Scene):
    def construct(self):
        dur = d('P01', 5)
        self.add(bg())
        label = ink("More brightness = more packets, not more energy each.", 28).shift(UP * 3.0)
        label.set_max_width(13)
        plate = Rectangle(width=7, height=0.4, color=DARK, stroke_width=3).set_fill(DARK, 0.8).shift(DOWN * 1.5)
        pkts  = VGroup(*[
            Dot(radius=0.18, color=RED, fill_opacity=0.9)
            .shift(LEFT * 3.0 + RIGHT * i * 1.0 + UP * 1.5)
            for i in range(7)
        ])
        nope  = VGroup(*[red("✗", 22).shift(LEFT * 3.0 + RIGHT * i * 1.0 + DOWN * 2.2) for i in range(7)])
        self.play(FadeIn(label), FadeIn(plate), run_time=0.4)
        self.play(FadeIn(pkts), run_time=0.5)
        self.play(pkts.animate.shift(DOWN * 2.6), run_time=0.7)
        self.play(FadeIn(nope), run_time=0.4)
        self.wait(max(0.1, dur - 2.0))


class P02_DimBlue(Scene):
    def construct(self):
        dur = d('P02', 5)
        self.add(bg())
        label = ink("A dim blue lamp: one hit, one ejection.", 30).shift(UP * 3.2)
        plate = Rectangle(width=7, height=0.4, color=DARK, stroke_width=3).set_fill(DARK, 0.8).shift(DOWN * 0.8)
        red_row = VGroup(*[Dot(radius=0.15, color=RED, fill_opacity=0.7).shift(LEFT * 3.0 + RIGHT * i * 1.0 + UP * 1.5) for i in range(7)])
        blue_pkt = Dot(radius=0.22, color=BLUE, fill_opacity=1).shift(RIGHT * 3.0 + UP * 1.5)
        elec = Dot(radius=0.14, color=ACNT, fill_opacity=1).shift(RIGHT * 4.2 + DOWN * 1.8)
        arrow = Arrow(RIGHT * 3.0 + UP * 0.2, RIGHT * 4.0 + DOWN * 1.5, color=ACNT, buff=0.1, stroke_width=2)
        ok_lbl = blue("✓", 42).shift(RIGHT * 3.5 + DOWN * 2.4)
        self.play(FadeIn(label), FadeIn(plate), FadeIn(red_row), run_time=0.5)
        self.play(FadeIn(blue_pkt), run_time=0.3)
        self.play(GrowArrow(arrow), FadeIn(elec), FadeIn(ok_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 1.5))


class P03_Photon(Scene):
    def construct(self):
        dur = d('P03', 6)
        self.add(bg())
        label = ink("This forced light to be quantized —", 30).shift(UP * 2.8)
        label2 = ink("Einstein's 1905 photon.", 30, color=BLUE).shift(UP * 2.0)
        pkt = Circle(radius=0.4, color=BLUE, fill_color=BLUE, fill_opacity=0.3, stroke_width=3).shift(UP * 0.2)
        pkt_lbl = blue("photon", 28).shift(UP * 0.2)
        eq    = MathTex(r"E = hf", font_size=52, color=DARK).shift(DOWN * 1.2)
        year  = ink("A. Einstein, 1905", 24, color=ACNT).shift(DOWN * 2.2)
        self.play(FadeIn(label), FadeIn(label2), run_time=0.5)
        self.play(FadeIn(pkt), FadeIn(pkt_lbl), run_time=0.5)
        self.play(Write(eq), FadeIn(year), run_time=0.7)
        self.wait(max(0.1, dur - 1.7))


class R01_BoxedEq(Scene):
    def construct(self):
        dur = d('R01', 5)
        self.add(bg())
        label = ink("The whole story is one line:", 30).shift(UP * 3.0)
        result = MathTex(r"K_{\max} = hf - \phi", font_size=80, color=DARK).shift(UP * 0.8)
        box    = SurroundingRectangle(result, color=RED, stroke_width=4, buff=0.25)
        self.play(FadeIn(label), run_time=0.3)
        self.play(Write(result), run_time=0.8)
        self.play(Create(box), run_time=0.4)
        self.wait(max(0.1, dur - 1.5))


class R02_Recap(Scene):
    def construct(self):
        dur = d('R02', 5)
        self.add(bg())
        result = MathTex(r"K_{\max} = hf - \phi", font_size=64, color=DARK).shift(UP * 2.5)
        box    = SurroundingRectangle(result, color=RED, stroke_width=3, buff=0.2)
        lines = VGroup(
            blue("Colour → energy per hit", 30),
            ink("Brightness → number of hits", 28),
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)
        self.play(FadeIn(result), FadeIn(box), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(l) for l in lines], lag_ratio=0.4), run_time=0.9)
        self.wait(max(0.1, dur - 1.4))


class OUTRO_Thanks(Scene):
    def construct(self):
        dur = d('OUTRO', 6)
        self.add(bg())
        thanks = ink("Thanks for watching", 36).shift(UP * 1.5)
        channel = blue("youtube.com/@NikBearBrown", 28).shift(UP * 0.4)
        title_r = ink("The Photoelectric Effect:\nWhy Colour Beats Brightness", 28).shift(DOWN * 1.0)
        title_r.set_max_width(12)
        self.play(FadeIn(thanks), FadeIn(channel), run_time=0.6)
        self.play(FadeIn(title_r), run_time=0.5)
        self.wait(max(0.1, dur - 1.1))
