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

class A00_SchrodingerAndCat(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 5.93)
        # Schrödinger figure (simple)
        head = Circle(radius=0.4, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 3 + UP * 1.5)
        body = Rectangle(width=0.6, height=1.0, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 3 + UP * 0.4)
        name = ink_txt("Schrödinger", size=24, color=INK).next_to(body, DOWN, buff=0.2)
        # cat figure
        cat_body = Ellipse(width=1.2, height=0.7, color=SLATE, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 2 + UP * 0.3)
        cat_head = Circle(radius=0.35, color=SLATE, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 2 + UP * 1.1)
        cat_label = ink_txt("? cat", size=26, color=SLATE).next_to(cat_body, DOWN, buff=0.2)
        question = ink_txt("invented quantum\nmechanics, then…", size=26, color=TERRA).shift(UP * 0.5)
        self.play(FadeIn(VGroup(head, body, name)), run_time=0.7)
        self.play(FadeIn(VGroup(cat_body, cat_head, cat_label)), run_time=0.7)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(dur - 1.9)


class A01_SealedBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 5.02)
        box = Rectangle(width=3.5, height=2.5, color=INK, stroke_width=4).set_fill(CREAM, 1)
        cat_icon = ink_txt("🐱", size=48).move_to(box.get_center() + LEFT * 0.5)
        trigger = Circle(radius=0.3, color=RED, stroke_width=2).set_fill(RED, opacity=0.3)
        trigger.move_to(box.get_center() + RIGHT * 0.8)
        trigger_label = ink_txt("quantum\ntrigger", size=20, color=RED).next_to(trigger, DOWN, buff=0.1)
        sealed = ink_txt("sealed box", size=26, color=INK).next_to(box, DOWN, buff=0.25)
        self.play(Create(box), run_time=0.7)
        self.play(FadeIn(cat_icon), run_time=0.4)
        self.play(FadeIn(trigger), FadeIn(trigger_label), run_time=0.5)
        self.play(FadeIn(sealed), run_time=0.4)
        self.wait(dur - 2.0)


class A02_AliveDead(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.13)
        alive_card = Rectangle(width=2.5, height=1.5, color=SLATE, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2.5)
        dead_card = Rectangle(width=2.5, height=1.5, color=RED, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 2.5)
        alive_text = ink_txt("ALIVE", size=36, color=SLATE).move_to(alive_card)
        dead_text = ink_txt("DEAD", size=36, color=RED).move_to(dead_card)
        label = ink_txt("common sense: two choices", size=26, color=INK).shift(DOWN * 1.8)
        self.play(Create(alive_card), Create(dead_card), run_time=0.7)
        self.play(FadeIn(alive_text), FadeIn(dead_text), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.6)


class A03_SuperpositionCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 4.44)
        alive_card = Rectangle(width=2.5, height=1.5, color=SLATE, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2.5)
        dead_card = Rectangle(width=2.5, height=1.5, color=RED, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 2.5)
        alive_text = ink_txt("ALIVE", size=36, color=SLATE).move_to(alive_card)
        dead_text = ink_txt("DEAD", size=36, color=RED).move_to(dead_card)
        both_card = Rectangle(width=3.0, height=1.5, color=TERRA, stroke_width=4).set_fill(TERRA, opacity=0.1)
        both_text = ink_txt("ALIVE + DEAD\n(superposition)", size=28, color=TERRA).move_to(both_card)
        label = ink_txt("quantum theory:\nboth at once", size=26, color=TERRA).shift(DOWN * 2.0)
        self.add(alive_card, dead_card, alive_text, dead_text)
        self.play(Transform(VGroup(alive_card, dead_card), both_card),
                  Transform(VGroup(alive_text, dead_text), both_text), run_time=1.0)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.5)


class A04_CollapseToOne(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.84)
        both_card = Rectangle(width=3.0, height=1.5, color=SLATE, stroke_width=4).set_fill(CREAM, 1)
        both_text = ink_txt("ALIVE + DEAD", size=28, color=INK).move_to(both_card)
        arrow = Arrow(UP * 1.5, ORIGIN, color=INK, stroke_width=4, buff=0.15,
                      max_tip_length_to_length_ratio=0.3)
        open_label = ink_txt("open box!", size=28, color=INK).next_to(arrow, RIGHT, buff=0.2)
        result = Rectangle(width=2.5, height=1.5, color=SLATE, stroke_width=3).set_fill(CREAM, 1)
        result.shift(DOWN * 2.0)
        result_text = ink_txt("ALIVE", size=36, color=SLATE).move_to(result)
        self.add(both_card, both_text)
        self.play(GrowArrow(arrow), FadeIn(open_label), run_time=0.6)
        self.play(FadeIn(result), FadeIn(result_text), run_time=0.6)
        self.wait(dur - 1.2)


class A05_AbsurdNotCute(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 3.19)
        schro = ink_txt("Schrödinger:", size=32, color=INK).shift(UP * 0.5)
        quote = ink_txt('"This is absurd!"', size=36, color=RED).shift(DOWN * 0.3)
        box_icon = Rectangle(width=2.0, height=1.2, color=INK, stroke_width=3).shift(RIGHT * 4 + UP * 0.5)
        self.play(FadeIn(schro), run_time=0.5)
        self.play(FadeIn(quote), run_time=0.5)
        self.play(FadeIn(box_icon), run_time=0.4)
        self.wait(dur - 1.4)


class A06_TinyObjectsReallyCanSuperpose(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 3.19)
        particle = Dot(color=TERRA, radius=0.2).shift(ORIGIN)
        ghosts = VGroup(*[
            Dot(color=SLATE, radius=0.15, fill_opacity=0.3).shift(
                RIGHT * np.cos(i * TAU / 6) * 1.2 + UP * np.sin(i * TAU / 6) * 1.2
            )
            for i in range(6)
        ])
        label = ink_txt("tiny objects really\ncan be in many states", size=28, color=SLATE).shift(DOWN * 2)
        self.play(FadeIn(particle), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(g) for g in ghosts], lag_ratio=0.1), run_time=0.8)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.6)


class A07_WavePacketPosition(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 4.55)
        # wave packet
        xs = np.linspace(-5, 5, 400)
        ys = np.exp(-xs**2 / 2) * np.cos(3 * xs)
        pts = [np.array([x * 0.8, y * 0.8, 0]) for x, y in zip(xs, ys)]
        packet = VMobject(color=SLATE, stroke_width=3)
        packet.set_points_smoothly(pts)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        x_label = ink_txt("position x", size=24, color=INK).next_to(x_axis.get_end(), RIGHT, buff=0.1)
        packet.shift(DOWN * 0.5)
        label = ink_txt("wavelength stretches\nacross positions", size=26, color=SLATE).shift(DOWN * 2.5)
        self.play(Create(x_axis), FadeIn(x_label), run_time=0.5)
        self.play(Create(packet), run_time=1.0)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.9)


class A08_NarrowPacketManyWavelengths(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.36)
        xs = np.linspace(-5, 5, 400)
        # narrow packet
        ys = np.exp(-xs**2 * 4) * np.cos(3 * xs)
        pts = [np.array([x * 0.8, y * 0.8, 0]) for x, y in zip(xs, ys)]
        narrow = VMobject(color=TERRA, stroke_width=3)
        narrow.set_points_smoothly(pts)
        x_axis = Line(LEFT * 4, RIGHT * 4, color=INK, stroke_width=2).shift(DOWN * 0.5)
        narrow.shift(DOWN * 0.5)
        # fan of wavelength components below
        fan = VGroup(*[
            FunctionGraph(lambda t, k=i: 0.3 * np.sin((3 + k) * t),
                          x_range=[-2, 2], color=SLATE, stroke_width=1.5)
            .shift(DOWN * (2.5 + i * 0.35))
            for i in range(3)
        ])
        label = ink_txt("narrow x → many wavelengths\n= spread in momentum", size=24, color=INK).shift(RIGHT * 3.5 + UP * 0.5)
        self.add(x_axis)
        self.play(Create(narrow), run_time=0.8)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.3)


class A09_BigObjectTinyWavelength(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 4.62)
        cat_box = Rectangle(width=2.0, height=1.2, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2)
        cat_label = ink_txt("cat\n(~1 kg)", size=24, color=INK).move_to(cat_box)
        arrow = Arrow(LEFT * 0, RIGHT * 1.5, color=INK, stroke_width=3, buff=0.1,
                      max_tip_length_to_length_ratio=0.3)
        wavelength = ink_txt("λ ~ 10⁻³⁵ m", size=26, color=RED).shift(RIGHT * 3.5)
        invisible = ink_txt("(invisible)", size=22, color=RED).next_to(wavelength, DOWN, buff=0.1)
        label = ink_txt("cat-scale: wave behavior\ncompletely vanishes", size=26, color=SLATE).shift(DOWN * 2.2)
        self.play(Create(cat_box), FadeIn(cat_label), run_time=0.7)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(wavelength), FadeIn(invisible), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 2.0)


class A10_ScaleComparison(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 3.6)
        items = [
            ("cat (~0.5 m)", 3.5, INK),
            ("atom (~1 Å)", 0.8, SLATE),
            ("de Broglie λ (cat)", 0.02, RED),
        ]
        bars = VGroup()
        labels_grp = VGroup()
        for i, (name, width, col) in enumerate(items):
            bar = Rectangle(width=width, height=0.5, color=col, stroke_width=2).set_fill(col, opacity=0.3)
            bar.move_to([-3.5 + width / 2, 1.0 - i * 1.0, 0])
            lbl = ink_txt(name, size=26, color=col).next_to(bar, RIGHT, buff=0.15)
            bars.add(bar)
            labels_grp.add(lbl)
        title = ink_txt("scale comparison", size=28, color=INK).shift(UP * 2.5)
        self.play(FadeIn(title), run_time=0.4)
        for bar, lbl in zip(bars, labels_grp):
            self.play(Create(bar), FadeIn(lbl), run_time=0.4)
        self.wait(dur - 0.4 * len(bars) - 0.4)


class A11_DoubleSlit(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 4.49)
        # source
        source = Dot(color=SLATE, radius=0.15).shift(LEFT * 4.5)
        # barrier with two slits
        barrier = Rectangle(width=0.3, height=3.0, color=INK, stroke_width=3).set_fill(INK, opacity=0.7)
        slit1 = Rectangle(width=0.35, height=0.35, color=CREAM, stroke_width=0).set_fill(CREAM, 1).shift(UP * 0.7)
        slit2 = Rectangle(width=0.35, height=0.35, color=CREAM, stroke_width=0).set_fill(CREAM, 1).shift(DOWN * 0.7)
        slits = VGroup(barrier, slit1, slit2)
        # screen
        screen = Line(UP * 2, DOWN * 2, color=INK, stroke_width=4).shift(RIGHT * 4)
        dot = Dot(color=TERRA, radius=0.15).shift(RIGHT * 4 + UP * 0.3)
        label = ink_txt("one electron → one dot", size=26, color=SLATE).shift(DOWN * 2.5)
        self.play(FadeIn(source), Create(slits), Create(screen), run_time=0.9)
        self.play(FadeIn(dot), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.8)


class A12_InterferenceFringes(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 4.21)
        barrier = Rectangle(width=0.3, height=3.0, color=INK, stroke_width=3).set_fill(INK, opacity=0.7)
        slit1 = Rectangle(width=0.35, height=0.35, color=CREAM).set_fill(CREAM, 1).shift(UP * 0.7)
        slit2 = Rectangle(width=0.35, height=0.35, color=CREAM).set_fill(CREAM, 1).shift(DOWN * 0.7)
        slits = VGroup(barrier, slit1, slit2)
        screen = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=4).shift(RIGHT * 4)
        # interference fringe pattern
        ys = np.linspace(-2.2, 2.2, 9)
        fringes = VGroup(*[
            Dot(color=SLATE, radius=0.12, fill_opacity=0.9 if i % 2 == 0 else 0.2).shift(RIGHT * 4 + UP * y)
            for i, y in enumerate(ys)
        ])
        label = ink_txt("many electrons → stripes", size=26, color=SLATE).shift(DOWN * 2.8)
        self.add(slits, screen)
        self.play(LaggedStart(*[FadeIn(f) for f in fringes], lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.4)


class A13_BlockOneSlit(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 2.22)
        barrier = Rectangle(width=0.3, height=3.0, color=INK, stroke_width=3).set_fill(INK, opacity=0.7)
        slit1_blocked = Rectangle(width=0.35, height=0.35, color=RED).set_fill(RED, opacity=0.8).shift(UP * 0.7)
        slit2 = Rectangle(width=0.35, height=0.35, color=CREAM).set_fill(CREAM, 1).shift(DOWN * 0.7)
        slits = VGroup(barrier, slit1_blocked, slit2)
        screen = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=4).shift(RIGHT * 4)
        # single-slit spread
        spread = VGroup(*[
            Dot(color=SLATE, radius=0.12, fill_opacity=max(0.1, 0.9 - abs(y))).shift(RIGHT * 4 + UP * y)
            for y in np.linspace(-1.5, 1.5, 7)
        ])
        label = ink_txt("block one slit → stripes vanish", size=26, color=RED).shift(DOWN * 2.8)
        self.play(FadeIn(slits), Create(screen), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(s) for s in spread], lag_ratio=0.05), run_time=0.5)
        self.play(FadeIn(label), run_time=0.3)
        self.wait(dur - 1.3)


class A14_WaveThroughBothSlits(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 4.6)
        barrier = Rectangle(width=0.3, height=3.0, color=INK, stroke_width=3).set_fill(INK, opacity=0.7)
        slit1 = Rectangle(width=0.35, height=0.35, color=CREAM).set_fill(CREAM, 1).shift(UP * 0.7)
        slit2 = Rectangle(width=0.35, height=0.35, color=CREAM).set_fill(CREAM, 1).shift(DOWN * 0.7)
        slits = VGroup(barrier, slit1, slit2)
        screen = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=4).shift(RIGHT * 4)
        wave1 = Arc(radius=1.5, start_angle=-PI / 3, angle=2 * PI / 3,
                    color=SLATE, stroke_width=2).move_to(UP * 0.7)
        wave2 = Arc(radius=1.5, start_angle=-PI / 3, angle=2 * PI / 3,
                    color=TERRA, stroke_width=2).move_to(DOWN * 0.7)
        single_dot = Dot(color=TERRA, radius=0.15).shift(RIGHT * 4 + UP * 0.6)
        label = ink_txt("possibility wave: both slits\none landing: single dot", size=26, color=SLATE).shift(DOWN * 2.8)
        self.add(slits, screen)
        self.play(Create(wave1), Create(wave2), run_time=0.9)
        self.play(FadeIn(single_dot), run_time=0.4)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.7)


class A15_ElectronCloudMolecule(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 5.04)
        atoms = VGroup(*[
            Circle(radius=0.35, color=INK, stroke_width=2).set_fill(CREAM, 1).shift(LEFT * (2 - i) * 1.0)
            for i in range(5)
        ])
        cloud = Ellipse(width=5.0, height=1.0, color=SLATE, stroke_width=0).set_fill(SLATE, opacity=0.25)
        label = ink_txt("electrons spread across atoms\n(superposition in materials)", size=26, color=SLATE).shift(DOWN * 2)
        self.play(FadeIn(atoms), run_time=0.7)
        self.play(FadeIn(cloud), run_time=0.6)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.8)


class A16_SharedElectronCloud(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A16", 4.91)
        atomA = Circle(radius=0.4, color=INK, stroke_width=2).set_fill(CREAM, 1).shift(LEFT * 2)
        atomB = Circle(radius=0.4, color=INK, stroke_width=2).set_fill(CREAM, 1).shift(RIGHT * 2)
        labelA = ink_txt("A", size=30).move_to(atomA)
        labelB = ink_txt("B", size=30).move_to(atomB)
        bond_cloud = Ellipse(width=4.5, height=0.9, color=TERRA, stroke_width=0).set_fill(TERRA, opacity=0.3)
        label = ink_txt("one electron, both atoms", size=28, color=TERRA).shift(DOWN * 1.8)
        self.play(FadeIn(atomA), FadeIn(atomB), FadeIn(labelA), FadeIn(labelB), run_time=0.7)
        self.play(FadeIn(bond_cloud), run_time=0.6)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(dur - 1.7)


class A17_EnergyBands(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A17", 4.13)
        # atom lattice
        lattice = VGroup(*[
            Circle(radius=0.2, color=INK, stroke_width=2).set_fill(INK, opacity=0.2).shift(
                RIGHT * (i - 4) * 0.7 + UP * (j - 1) * 0.7
            )
            for i in range(9) for j in range(3)
        ])
        # energy bands (simplified)
        valence = Rectangle(width=6, height=0.5, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.3).shift(DOWN * 1.5 + RIGHT * 2)
        conduction = Rectangle(width=6, height=0.3, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.3).shift(DOWN * 0.7 + RIGHT * 2)
        v_label = ink_txt("valence band", size=20, color=SLATE).next_to(valence, RIGHT, buff=0.15)
        c_label = ink_txt("conduction band", size=20, color=TERRA).next_to(conduction, RIGHT, buff=0.15)
        self.play(FadeIn(lattice), run_time=0.6)
        self.play(Transform(lattice, VGroup(valence, conduction)),
                  FadeIn(v_label), FadeIn(c_label), run_time=1.0)
        self.wait(dur - 1.6)


class A18_BandGapTransistor(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A18", 3.84)
        gap_rect = Rectangle(width=4.0, height=1.5, color=INK, stroke_width=3).set_fill(CREAM, 1)
        gap_label = ink_txt("band gap", size=28, color=INK).next_to(gap_rect, UP, buff=0.2)
        # transistor symbol (simplified)
        transistor = VGroup(
            Line(LEFT * 0.5, RIGHT * 0.5, color=TERRA, stroke_width=4),
            Line(LEFT * 0.5, LEFT * 0.5 + UP * 0.6, color=TERRA, stroke_width=3),
            Line(LEFT * 0.5, LEFT * 0.5 + DOWN * 0.6, color=TERRA, stroke_width=3),
            Arrow(RIGHT * 0.3, RIGHT * 1.0, color=TERRA, stroke_width=3, buff=0,
                  max_tip_length_to_length_ratio=0.4),
        ).shift(RIGHT * 3.5)
        t_label = ink_txt("transistor", size=22, color=TERRA).next_to(transistor, DOWN, buff=0.2)
        arrow = Arrow(gap_rect.get_right(), transistor.get_left() + LEFT * 0.3,
                      color=INK, stroke_width=2, buff=0.1, max_tip_length_to_length_ratio=0.3)
        self.play(Create(gap_rect), FadeIn(gap_label), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(transistor), FadeIn(t_label), run_time=0.8)
        self.wait(dur - 1.4)


class A19_ComputerChips(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A19", 4.55)
        # chip grid
        chip = Rectangle(width=4.0, height=3.0, color=INK, stroke_width=3).set_fill(CREAM, 1)
        grid = VGroup(*[
            Line(LEFT * 1.9 + UP * (j * 0.35 - 1.0), RIGHT * 1.9 + UP * (j * 0.35 - 1.0),
                 color=SLATE, stroke_width=1)
            for j in range(9)
        ] + [
            Line(UP * 1.4 + RIGHT * (i * 0.5 - 1.75), DOWN * 1.4 + RIGHT * (i * 0.5 - 1.75),
                 color=SLATE, stroke_width=1)
            for i in range(8)
        ])
        label = ink_txt("transistors → chips\n→ this video", size=28, color=INK).shift(RIGHT * 4 + UP * 0.5)
        self.play(Create(chip), Create(grid), run_time=0.9)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 1.4)


class A20_CatVideoAndBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A20", 4.0)
        # laptop icon
        laptop_screen = Rectangle(width=2.5, height=1.8, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2.5 + UP * 0.4)
        laptop_base = Rectangle(width=2.8, height=0.2, color=INK, stroke_width=2).set_fill(INK, opacity=0.6).shift(LEFT * 2.5 + DOWN * 0.55)
        cat_on_screen = ink_txt("🐱▶", size=40).move_to(laptop_screen)
        # sealed box
        box = Rectangle(width=2.0, height=1.5, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 3 + UP * 0.3)
        box_label = ink_txt("?", size=48, color=SLATE).move_to(box)
        arrow = Arrow(RIGHT * 1.5, RIGHT * 1.9, color=INK, stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.35)
        punchline = ink_txt("cat videos run on\nSchrödinger's cat", size=28, color=SLATE).shift(DOWN * 2.3)
        self.play(Create(laptop_screen), Create(laptop_base), FadeIn(cat_on_screen), run_time=0.7)
        self.play(Create(box), FadeIn(box_label), GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(punchline), run_time=0.5)
        self.wait(dur - 1.8)
