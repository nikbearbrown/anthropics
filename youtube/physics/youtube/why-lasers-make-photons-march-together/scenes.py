import json
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

def excited_atom(pos, label="*"):
    circle = Circle(radius=0.35, color=INK, stroke_width=2).set_fill(TERRA, opacity=0.4).move_to(pos)
    star = Text(label, font=FONT, font_size=20, color=RED).move_to(pos + UP * 0.42)
    return VGroup(circle, star)


class A00_ExcitedAtoms(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 3.06)
        atoms = VGroup(*[excited_atom(LEFT * 2 + (i - 1.5) * RIGHT * 1.2) for i in range(4)])
        label = ink_txt("atoms pumped\nwith extra energy", size=28, color=INK).shift(RIGHT * 3.5)
        pump = Arrow(DOWN * 1.5, DOWN * 0.6, color=TERRA, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.3).shift(LEFT * 3)
        pump_label = ink_txt("pump", size=22, color=INK).next_to(pump, LEFT, buff=0.1)
        self.play(LaggedStart(*[FadeIn(a) for a in atoms], lag_ratio=0.15), run_time=0.8)
        self.play(FadeIn(label), GrowArrow(pump), FadeIn(pump_label), run_time=0.6)
        self.wait(dur - 1.4)


class A01_EmittedPhoton(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.16)
        atom = excited_atom(LEFT * 2)
        photon = Arrow(LEFT * 1.5, RIGHT * 2, color=SLATE, stroke_width=5, buff=0,
                       max_tip_length_to_length_ratio=0.18)
        photon_label = ink_txt("photon", size=26, color=SLATE).next_to(photon, UP, buff=0.1)
        self.add(atom)
        self.play(GrowArrow(photon), FadeIn(photon_label), run_time=0.8)
        self.wait(dur - 0.8)


class A02_StimulatedAtom(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 2.74)
        incoming = Arrow(LEFT * 5, LEFT * 1.4, color=SLATE, stroke_width=5, buff=0,
                         max_tip_length_to_length_ratio=0.15)
        atom = excited_atom(ORIGIN)
        self.play(GrowArrow(incoming), run_time=0.6)
        self.play(FadeIn(atom), run_time=0.4)
        out1 = Arrow(RIGHT * 0.4, RIGHT * 2.5 + UP * 0.6, color=SLATE, stroke_width=5, buff=0,
                     max_tip_length_to_length_ratio=0.18)
        out2 = Arrow(RIGHT * 0.4, RIGHT * 2.5 + DOWN * 0.6, color=SLATE, stroke_width=5, buff=0,
                     max_tip_length_to_length_ratio=0.18)
        self.play(GrowArrow(out1), GrowArrow(out2), run_time=0.5)
        self.wait(dur - 1.5)


class A03_CopiedDirection(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.11)
        p1 = Arrow(LEFT * 3, RIGHT * 0, color=SLATE, stroke_width=5, buff=0,
                   max_tip_length_to_length_ratio=0.18)
        p2 = Arrow(LEFT * 3, RIGHT * 0, color=SLATE, stroke_width=5, buff=0,
                   max_tip_length_to_length_ratio=0.18).shift(DOWN * 0.5)
        l1 = ink_txt("photon 1", size=24, color=SLATE).next_to(p1, UP, buff=0.1)
        l2 = ink_txt("photon 2 — same direction", size=24, color=TERRA).next_to(p2, DOWN, buff=0.1)
        self.play(GrowArrow(p1), FadeIn(l1), run_time=0.7)
        self.play(GrowArrow(p2), FadeIn(l2), run_time=0.7)
        self.wait(dur - 1.4)


class A04_MatchingLabels(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 3.89)
        props = ["direction", "color (wavelength)", "phase", "polarization"]
        labels = VGroup(*[
            ink_txt(f"✓ {p}", size=28, color=INK if i % 2 == 0 else SLATE)
            for i, p in enumerate(props)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(ORIGIN)
        title = ink_txt("both photons share:", size=30).next_to(labels, UP, buff=0.3)
        self.play(FadeIn(title), run_time=0.4)
        for lab in labels:
            self.play(FadeIn(lab), run_time=0.35)
        self.wait(dur - len(labels) * 0.35 - 0.4)


class A05_StimulatedEmissionLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 2.35)
        label = ink_txt("Stimulated Emission", size=44, color=TERRA)
        underline = Line(label.get_left(), label.get_right(), color=TERRA, stroke_width=3).next_to(label, DOWN, buff=0.1)
        self.play(FadeIn(label), Create(underline), run_time=0.9)
        self.wait(dur - 0.9)


class A06_Mirrors(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 2.77)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK, stroke_width=2).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK, stroke_width=2).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        cavity_label = ink_txt("laser cavity", size=26).shift(UP * 2)
        photon = Arrow(LEFT * 4, RIGHT * 4, color=TERRA, stroke_width=5, buff=0,
                       max_tip_length_to_length_ratio=0.12)
        self.play(FadeIn(left_mirror), FadeIn(right_mirror), FadeIn(cavity_label), run_time=0.7)
        self.play(GrowArrow(photon), run_time=0.5)
        self.wait(dur - 1.2)


class A07_NudgedAtoms(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 2.93)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        atoms = VGroup(*[excited_atom(LEFT * 2 + i * RIGHT * 1.3) for i in range(3)])
        beam = Arrow(LEFT * 4, RIGHT * 4, color=TERRA, stroke_width=5, buff=0,
                     max_tip_length_to_length_ratio=0.12)
        nudge_label = ink_txt("each pass nudges more atoms", size=26, color=TERRA).shift(DOWN * 2)
        self.add(left_mirror, right_mirror, atoms, beam)
        self.play(FadeIn(nudge_label), run_time=0.5)
        self.wait(dur - 0.5)


class A08_PhotonCrowd(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 3.16)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        beams = VGroup(*[
            Arrow(LEFT * 4, RIGHT * 4, color=TERRA, stroke_width=4, buff=0,
                  max_tip_length_to_length_ratio=0.08).shift(UP * (i - 1) * 0.4)
            for i in range(3)
        ])
        crowd_label = ink_txt("bright crowd of\nidentical photons", size=28, color=SLATE).shift(DOWN * 2.5)
        self.add(left_mirror, right_mirror)
        self.play(LaggedStart(*[GrowArrow(b) for b in beams], lag_ratio=0.2),
                  FadeIn(crowd_label), run_time=1.4)
        self.wait(dur - 1.4)


class A09_UnlabeledPhotons(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 2.46)
        p1 = Circle(radius=0.4, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.3).shift(LEFT * 1.5)
        p2 = Circle(radius=0.4, color=TERRA, stroke_width=3).set_fill(TERRA, opacity=0.3).shift(RIGHT * 1.5)
        equals = ink_txt("≡", size=48).shift(ORIGIN)
        label = ink_txt("photons have no label", size=28, color=SLATE).shift(DOWN * 1.5)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(equals), FadeIn(label), run_time=1.1)
        self.wait(dur - 1.1)


class A10_SameStatePattern(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 3.24)
        state_box = Rectangle(width=3.5, height=1.5, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.08)
        p1 = Circle(radius=0.35, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.4).shift(LEFT * 0.8)
        p2 = Circle(radius=0.35, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.4).shift(RIGHT * 0.8)
        label = ink_txt("one shared state", size=28, color=SLATE).next_to(state_box, DOWN, buff=0.25)
        count = ink_txt("= counts as 1 pattern", size=24, color=INK).next_to(label, DOWN, buff=0.15)
        self.play(Create(state_box), run_time=0.5)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.5)
        self.play(FadeIn(label), FadeIn(count), run_time=0.5)
        self.wait(dur - 1.5)


class A11_DifferentStates(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.11)
        box1 = Rectangle(width=1.8, height=1.5, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.08).shift(LEFT * 2.5)
        box2 = Rectangle(width=1.8, height=1.5, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.08).shift(RIGHT * 2.5)
        p1 = Circle(radius=0.35, color=SLATE, stroke_width=2).set_fill(SLATE, opacity=0.4).move_to(box1)
        p2 = Circle(radius=0.35, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.4).move_to(box2)
        label = ink_txt("different states → fewer matching paths", size=26, color=RED).shift(DOWN * 1.8)
        self.play(Create(box1), Create(box2), FadeIn(p1), FadeIn(p2), FadeIn(label), run_time=1.3)
        self.wait(dur - 1.3)


class A12_OccupiedStateFavored(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 4.0)
        # occupied vs empty state
        occ_box = Rectangle(width=2.5, height=1.5, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.1).shift(LEFT * 2.5)
        empty_box = Rectangle(width=2.5, height=1.5, color=INK, stroke_width=2).set_fill(CREAM, 1).shift(RIGHT * 2.5)
        p_occ = Circle(radius=0.35, color=TERRA, stroke_width=2).set_fill(TERRA, opacity=0.5).move_to(occ_box.get_center())
        occ_label = ink_txt("occupied\n(preferred!)", size=24, color=TERRA).next_to(occ_box, DOWN, buff=0.2)
        empty_label = ink_txt("empty", size=24, color=INK).next_to(empty_box, DOWN, buff=0.2)
        check = ink_txt("✓", size=48, color=TERRA).next_to(occ_box, UP, buff=0.1)
        rule = ink_txt("bosons bunch: joining\noccupied state favored", size=26, color=SLATE).shift(DOWN * 2.5)
        self.play(Create(occ_box), Create(empty_box), run_time=0.6)
        self.play(FadeIn(p_occ), FadeIn(occ_label), FadeIn(empty_label), run_time=0.5)
        self.play(FadeIn(check), run_time=0.3)
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(dur - 1.9)


class A13_MatchingLightTriggers(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 3.66)
        atom = excited_atom(LEFT * 1.5)
        incoming = Arrow(LEFT * 4.5, LEFT * 2, color=TERRA, stroke_width=5, buff=0,
                         max_tip_length_to_length_ratio=0.18)
        in_label = ink_txt("matching\nphoton", size=22, color=INK).next_to(incoming, UP, buff=0.1)
        result = ink_txt("easier to trigger →\ncopy emitted", size=26, color=SLATE).shift(RIGHT * 3)
        emitted = Arrow(LEFT * 0.8, RIGHT * 1.5, color=SLATE, stroke_width=4, buff=0,
                        max_tip_length_to_length_ratio=0.15)
        self.play(FadeIn(atom), GrowArrow(incoming), FadeIn(in_label), run_time=0.9)
        self.play(FadeIn(result), GrowArrow(emitted), run_time=0.5)
        self.wait(dur - 1.4)


class A14_CavityRewards(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 3.06)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        beams = VGroup(*[
            Arrow(LEFT * 4, RIGHT * 4, color=TERRA, stroke_width=3 + i, buff=0,
                  max_tip_length_to_length_ratio=0.08).shift(UP * (i - 1) * 0.35)
            for i in range(3)
        ])
        reward = ink_txt("same pattern\nrewarded every pass", size=26, color=SLATE).shift(DOWN * 2.5)
        self.add(left_mirror, right_mirror)
        self.play(LaggedStart(*[GrowArrow(b) for b in beams], lag_ratio=0.2),
                  FadeIn(reward), run_time=1.2)
        self.wait(dur - 1.2)


class A15_OutputCoupler(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 2.95)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        # partial opening in right mirror
        gap = Rectangle(width=0.22, height=0.6, color=CREAM, stroke_width=0).set_fill(CREAM, 1).shift(RIGHT * 4.5)
        opening_label = ink_txt("output\ncoupler", size=22, color=INK).next_to(right_mirror, UP, buff=0.15)
        escape = Arrow(RIGHT * 4.6, RIGHT * 6, color=SLATE, stroke_width=5, buff=0,
                       max_tip_length_to_length_ratio=0.25)
        self.add(left_mirror, right_mirror)
        self.play(FadeIn(gap), FadeIn(opening_label), run_time=0.5)
        self.play(GrowArrow(escape), run_time=0.5)
        self.wait(dur - 1.0)


class A16_CoherentBeam(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A16", 2.77)
        left_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.6).shift(LEFT * 4.5)
        right_mirror = Rectangle(width=0.2, height=2.5, color=INK).set_fill(SLATE, opacity=0.3).shift(RIGHT * 4.5)
        gap = Rectangle(width=0.22, height=0.6, color=CREAM).set_fill(CREAM, 1).shift(RIGHT * 4.5)
        beam = Arrow(RIGHT * 4.6, RIGHT * 6.5, color=SLATE, stroke_width=7, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        coherent = ink_txt("coherent laser light", size=32, color=INK).shift(DOWN * 2.5)
        self.add(left_mirror, right_mirror, gap)
        self.play(GrowArrow(beam), FadeIn(coherent), run_time=1.2)
        self.wait(dur - 1.2)
