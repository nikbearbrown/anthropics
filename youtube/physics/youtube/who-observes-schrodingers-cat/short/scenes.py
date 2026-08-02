"""Portrait (9:16) Manim scenes for who-observes-schrodingers-cat Short.

Render all beats at 4K portrait (2160x3840):
  manim -qk --fps 24 -r 2160,3840 scenes.py \
    A00_NotAboutCat A01_WhereObservationBegins A02_SealedBox A03_TwoBranches \
    A04_TriggerFiredBranch A05_TriggerQuietBranch A06_CatConnectedToBranches \
    A07_ExperienceFollowsEvent A08_FiredTriggerPair A09_QuietTriggerPair \
    A10_MixedRecordCrossedOut A11_EntanglementLabel A12_ObserverLinkedToRecord \
    A13_ObserverBelongsToBranch A14_CollapseSelectsHistory A15_FinalObserverQuestion \
    A16_OneOutcomeBecomesReal A17_ManyBranchTree A18_MeasurementProblem

Then copy each <Scene>.mp4 → manim/<BID>.mp4.
"""
import json
from pathlib import Path
from manim import *
import numpy as np

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED_COL = "#C0392B"
FONT = "EB Garamond"

# 9:16 portrait 4K config (2160x3840)
config.frame_width  = 9
config.frame_height = 16
config.pixel_width  = 2160
config.pixel_height = 3840

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

def ink_txt(t, size=48, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class A00_NotAboutCat(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 3.63)
        # Portrait: cat top, book bottom
        cat_circle = Circle(radius=0.55, color=SLATE, fill_opacity=0.4).shift(UP * 3.0)
        ear_l = Triangle(color=SLATE, fill_opacity=0.6).scale(0.22).shift(UP * 3.7 + LEFT * 0.35)
        ear_r = Triangle(color=SLATE, fill_opacity=0.6).scale(0.22).shift(UP * 3.7 + RIGHT * 0.35)
        cat = VGroup(cat_circle, ear_l, ear_r)

        book = Rectangle(width=2.0, height=2.4, color=INK, fill_opacity=0.15).shift(DOWN * 0.5)
        book_label = ink_txt("storybook", size=40).next_to(book, UP, buff=0.2)
        cross1 = Line(book.get_corner(UL), book.get_corner(DR), color=RED_COL, stroke_width=6)
        cross2 = Line(book.get_corner(UR), book.get_corner(DL), color=RED_COL, stroke_width=6)

        label = ink_txt("not really\nabout a cat!", size=44, color=INK)
        label.shift(DOWN * 3.5)

        self.play(Create(cat), run_time=dur * 0.25)
        self.play(Create(book), Write(book_label), run_time=dur * 0.25)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.2)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A01_WhereObservationBegins(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.37)
        q_mark = ink_txt("?", size=144, color=SLATE).shift(UP * 2.0)
        obs_label = ink_txt("where does\nobservation begin?", size=48, color=INK)
        obs_label.shift(DOWN * 1.5)

        self.play(Write(q_mark), run_time=dur * 0.5)
        self.play(Write(obs_label), run_time=dur * 0.35)
        self.wait(dur * 0.15)


class A02_SealedBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 3.46)
        box = Rectangle(width=5.0, height=4.0, color=INK, fill_opacity=0.12)
        box_label = ink_txt("sealed box", size=44).next_to(box, DOWN, buff=0.3)

        trigger = Circle(radius=0.5, color=TERRA, fill_opacity=0.7).shift(RIGHT * 0.7)
        trigger_label = ink_txt("quantum\ntrigger", size=38, color=INK).next_to(trigger, DOWN, buff=0.2)
        q = ink_txt("?", size=72, color=SLATE).shift(LEFT * 1.2)

        self.play(Create(box), Write(box_label), run_time=dur * 0.4)
        self.play(FadeIn(trigger), Write(trigger_label), run_time=dur * 0.3)
        self.play(Write(q), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A03_TwoBranches(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.29)
        # Vertical branching: node at top, two cards below
        node = Dot(radius=0.25, color=SLATE).shift(UP * 4.0)

        branch_l = Line(node.get_bottom(), LEFT * 1.8 + UP * 1.8, color=SLATE, stroke_width=3)
        branch_r = Line(node.get_bottom(), RIGHT * 1.8 + UP * 1.8, color=SLATE, stroke_width=3)

        card_l = Rectangle(width=3.0, height=1.2, color=SLATE, fill_opacity=0.12).shift(LEFT * 1.8 + UP * 0.8)
        card_r = Rectangle(width=3.0, height=1.2, color=SLATE, fill_opacity=0.12).shift(RIGHT * 1.8 + UP * 0.8)

        event_label = ink_txt("quantum\nevent", size=40).next_to(node, UP, buff=0.1)
        label = ink_txt("two possible\nrecords", size=44, color=INK).shift(DOWN * 1.5)

        self.play(FadeIn(node), Write(event_label), run_time=dur * 0.3)
        self.play(Create(branch_l), Create(branch_r), run_time=dur * 0.25)
        self.play(Create(card_l), Create(card_r), Write(label), run_time=dur * 0.3)
        self.wait(dur * 0.15)


class A04_TriggerFiredBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 2.69)
        # Two cards stacked: top (fired, highlighted), bottom (quiet, dim)
        card_top = Rectangle(width=5.5, height=1.5, color=INK, fill_opacity=0.2).shift(UP * 2.0)
        card_top_label = ink_txt("trigger FIRED", size=48, color=INK).move_to(card_top)
        card_bot = Rectangle(width=5.5, height=1.5, color=SLATE, fill_opacity=0.1).shift(DOWN * 0.5)

        self.add(card_bot)
        self.play(Create(card_top), Write(card_top_label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A05_TriggerQuietBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 3.16)
        card_top = Rectangle(width=5.5, height=1.5, color=INK, fill_opacity=0.15).shift(UP * 2.0)
        card_top_label = ink_txt("trigger FIRED", size=48, color=INK).move_to(card_top)
        card_bot = Rectangle(width=5.5, height=1.5, color=SLATE, fill_opacity=0.2).shift(DOWN * 0.5)
        card_bot_label = ink_txt("trigger quiet", size=48, color=SLATE).move_to(card_bot)

        self.add(card_top, card_top_label)
        self.play(Create(card_bot), Write(card_bot_label), run_time=dur * 0.65)
        self.wait(dur * 0.35)


class A06_CatConnectedToBranches(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 3.03)
        card_top = Rectangle(width=4.5, height=1.2, color=SLATE, fill_opacity=0.15).shift(UP * 2.5)
        card_bot = Rectangle(width=4.5, height=1.2, color=SLATE, fill_opacity=0.15).shift(UP * 0.5)
        self.add(card_top, card_bot)

        cat_dot = Dot(radius=0.35, color=INK, fill_opacity=0.7).shift(DOWN * 2.0)
        cat_label = ink_txt("cat", size=44).next_to(cat_dot, DOWN, buff=0.15)
        line_top = DashedLine(cat_dot.get_top(), card_top.get_bottom(), color=INK, stroke_width=2)
        line_bot = DashedLine(cat_dot.get_top(), card_bot.get_bottom(), color=INK, stroke_width=2)

        not_sep = ink_txt("cat is NOT\nseparate", size=44, color=INK).shift(DOWN * 4.0)

        self.play(FadeIn(cat_dot), Write(cat_label), run_time=dur * 0.3)
        self.play(Create(line_top), Create(line_bot), run_time=dur * 0.35)
        self.play(Write(not_sep), run_time=dur * 0.3)
        self.wait(dur * 0.05)


class A07_ExperienceFollowsEvent(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 3.63)
        # Portrait: two horizontal bands stacked vertically
        band_top = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=5).shift(UP * 2.5)
        band_bot = Line(LEFT * 3.5, RIGHT * 3.5, color=SLATE, stroke_width=5).shift(UP * 0.5)

        up_label = ink_txt("fired  →  cat sees result", size=40, color=INK).shift(UP * 3.4)
        dn_label = ink_txt("quiet  →  cat sees nothing", size=40, color=SLATE).shift(UP * 1.4)

        arrow = Arrow(UP * 2.2, UP * 0.8, color=INK, buff=0.05).shift(LEFT * 3.8)
        follows = ink_txt("experience\nfollows event", size=44, color=INK)
        follows.shift(DOWN * 2.0)

        self.play(Create(band_top), Write(up_label), run_time=dur * 0.3)
        self.play(Create(band_bot), Write(dn_label), run_time=dur * 0.3)
        self.play(GrowArrow(arrow), Write(follows), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A08_FiredTriggerPair(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 3.33)
        # Stack trigger (top) and cat (bottom) with arrow between
        trigger_box = Rectangle(width=5.0, height=1.4, color=INK, fill_opacity=0.2).shift(UP * 3.0)
        trigger_label = ink_txt("trigger FIRED", size=48, color=INK).move_to(trigger_box)

        link = Arrow(UP * 2.0, UP * 0.8, color=INK, buff=0.05)

        cat_box = Rectangle(width=5.0, height=1.4, color=INK, fill_opacity=0.2).shift(UP * 0.0)
        cat_label = ink_txt("cat sees result", size=48, color=INK).move_to(cat_box)

        pair_label = ink_txt("always paired", size=44, color=INK).shift(DOWN * 2.0)

        self.play(Create(trigger_box), Write(trigger_label), run_time=dur * 0.3)
        self.play(GrowArrow(link), run_time=dur * 0.2)
        self.play(Create(cat_box), Write(cat_label), run_time=dur * 0.3)
        self.play(Write(pair_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A09_QuietTriggerPair(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 3.2)
        trigger_box = Rectangle(width=5.0, height=1.4, color=SLATE, fill_opacity=0.2).shift(UP * 2.0)
        trigger_label = ink_txt("trigger quiet", size=48, color=SLATE).move_to(trigger_box)

        link = Arrow(UP * 1.2, UP * 0.0, color=SLATE, buff=0.05)

        cat_box = Rectangle(width=5.0, height=1.4, color=SLATE, fill_opacity=0.2).shift(DOWN * 0.8)
        cat_label = ink_txt("cat sees nothing", size=44, color=SLATE).move_to(cat_box)

        self.play(Create(trigger_box), Write(trigger_label), run_time=dur * 0.35)
        self.play(GrowArrow(link), run_time=dur * 0.2)
        self.play(Create(cat_box), Write(cat_label), run_time=dur * 0.35)
        self.wait(dur * 0.1)


class A10_MixedRecordCrossedOut(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 3.8)
        mixed_box = Rectangle(width=5.5, height=1.6, color=RED_COL, fill_opacity=0.15).shift(UP * 1.5)
        mixed_label = ink_txt("fired BUT unseen", size=44, color=INK).next_to(mixed_box, UP, buff=0.2)
        cross1 = Line(mixed_box.get_corner(UL), mixed_box.get_corner(DR), color=RED_COL, stroke_width=6)
        cross2 = Line(mixed_box.get_corner(UR), mixed_box.get_corner(DL), color=RED_COL, stroke_width=6)

        no_label = ink_txt("does NOT\nbelong!", size=52, color=INK).shift(DOWN * 1.5)

        self.play(Create(mixed_box), Write(mixed_label), run_time=dur * 0.35)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.25)
        self.play(Write(no_label), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A11_EntanglementLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.73)
        box_a = Rectangle(width=5.5, height=1.4, color=SLATE, fill_opacity=0.2).shift(UP * 2.5)
        label_a = ink_txt("triggered record", size=44, color=INK).move_to(box_a)
        box_b = Rectangle(width=5.5, height=1.4, color=SLATE, fill_opacity=0.2).shift(UP * 0.5)
        label_b = ink_txt("quiet record", size=44, color=SLATE).move_to(box_b)

        link = DoubleArrow(box_a.get_bottom(), box_b.get_top(), color=SLATE, buff=0.05, stroke_width=4)

        ent_label = ink_txt("ENTANGLEMENT", size=52, color=INK).shift(DOWN * 1.5)
        ent_sub = ink_txt("not ordinary ignorance", size=40, color=SLATE).shift(DOWN * 2.8)

        self.play(Create(box_a), Create(box_b), Write(label_a), Write(label_b), run_time=dur * 0.25)
        self.play(Create(link), run_time=dur * 0.2)
        self.play(Write(ent_label), run_time=dur * 0.3)
        self.play(Write(ent_sub), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class A12_ObserverLinkedToRecord(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 3.63)
        box = Rectangle(width=4.0, height=3.0, color=INK, fill_opacity=0.1, stroke_width=3).shift(UP * 2.5)
        record = ink_txt("record\n(branch)", size=44, color=INK).move_to(box)

        observer = Circle(radius=0.5, color=SLATE, fill_opacity=0.5).shift(DOWN * 0.5)
        obs_label = ink_txt("observer", size=44).next_to(observer, DOWN, buff=0.2)

        link_arrow = Arrow(box.get_bottom(), observer.get_top(), color=INK, buff=0.05, stroke_width=4)
        link_label = ink_txt("opening the box\nlinks observer", size=44, color=INK)
        link_label.shift(DOWN * 2.8)

        self.play(Create(box), Write(record), run_time=dur * 0.3)
        self.play(Create(observer), Write(obs_label), run_time=dur * 0.25)
        self.play(GrowArrow(link_arrow), run_time=dur * 0.25)
        self.play(Write(link_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A13_ObserverBelongsToBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 3.26)
        branch_top = Rectangle(width=7.5, height=1.8, color=SLATE, fill_opacity=0.15).shift(UP * 2.5)
        branch_bot = Rectangle(width=7.5, height=1.8, color=SLATE, fill_opacity=0.15).shift(UP * 0.0)
        up_txt = ink_txt("fired + cat saw\n+ observer A", size=40, color=INK).move_to(branch_top)
        dn_txt = ink_txt("quiet + cat nothing\n+ observer B", size=40, color=SLATE).move_to(branch_bot)

        obs_label = ink_txt("observer belongs\nto a branch too", size=48, color=INK)
        obs_label.shift(DOWN * 2.8)

        self.play(Create(branch_top), Write(up_txt), run_time=dur * 0.35)
        self.play(Create(branch_bot), Write(dn_txt), run_time=dur * 0.35)
        self.play(Write(obs_label), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A14_CollapseSelectsHistory(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 3.07)
        hist_a = Rectangle(width=5.5, height=1.4, color=SLATE, fill_opacity=0.15).shift(UP * 2.5)
        hist_a_lbl = ink_txt("history A", size=48, color=SLATE).move_to(hist_a)

        hist_b = Rectangle(width=5.5, height=1.4, color=INK, fill_opacity=0.5, stroke_width=4).shift(UP * 0.5)
        hist_b_lbl = ink_txt("history B  ✓", size=48, color=INK).move_to(hist_b)

        selected = ink_txt("collapse → one shared\nhistory (seems to)", size=44, color=INK)
        selected.shift(DOWN * 2.0)

        self.play(Create(hist_a), Write(hist_a_lbl), run_time=dur * 0.3)
        self.play(Create(hist_b), Write(hist_b_lbl), run_time=dur * 0.3)
        self.play(Write(selected), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A15_FinalObserverQuestion(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 3.61)
        # Vertical chain: atom → detector → cat → you
        labels_text = ["atom", "detector", "cat", "you"]
        y_positions = [UP * 4.5, UP * 2.0, DOWN * 0.5, DOWN * 3.0]

        chain_dots = VGroup(*[
            Dot(radius=0.22, color=SLATE).shift(p)
            for p in y_positions
        ])
        chain_arrows = VGroup(*[
            Arrow(y_positions[i] + DOWN * 0.3, y_positions[i + 1] + UP * 0.3,
                  color=SLATE, buff=0.05)
            for i in range(3)
        ])
        chain_labels = VGroup(*[
            ink_txt(t, size=44).next_to(chain_dots[i], RIGHT, buff=0.4)
            for i, t in enumerate(labels_text)
        ])

        big_q = ink_txt("?", size=96, color=INK).shift(RIGHT * 2.5 + DOWN * 3.0)
        final_label = ink_txt("quantum theory\ndoes not name\nthe final observer", size=44, color=INK)
        final_label.shift(LEFT * 1.5 + DOWN * 5.5)

        self.play(LaggedStart(*[FadeIn(dot) for dot in chain_dots], lag_ratio=0.15), run_time=dur * 0.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in chain_arrows], lag_ratio=0.15),
                  LaggedStart(*[Write(l) for l in chain_labels], lag_ratio=0.15), run_time=dur * 0.3)
        self.play(Write(big_q), run_time=dur * 0.2)
        self.play(Write(final_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A16_OneOutcomeBecomesReal(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A16", 3.95)
        outcome_box = Rectangle(width=5.5, height=1.8, color=SLATE, fill_opacity=0.2).shift(UP * 2.0)
        outcome_label = ink_txt("one outcome\nbecomes real", size=48, color=INK).move_to(outcome_box)

        unknown = Rectangle(width=5.5, height=1.8, color=RED_COL, fill_opacity=0.12).shift(DOWN * 0.5)
        unk_label = ink_txt("mechanism: ???", size=48, color=RED_COL).move_to(unknown)

        self.play(Create(outcome_box), Write(outcome_label), run_time=dur * 0.45)
        self.play(Create(unknown), Write(unk_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A17_ManyBranchTree(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A17", 4.39)
        # Vertical tree: root at top, branches down
        root = Dot(radius=0.25, color=SLATE).shift(UP * 5.0)

        level1 = [UP * 3.0 + LEFT * 1.5, UP * 3.0 + RIGHT * 1.5]
        level2 = [UP * 1.0 + LEFT * 2.5, UP * 1.0 + LEFT * 0.8,
                  UP * 1.0 + RIGHT * 0.8, UP * 1.0 + RIGHT * 2.5]
        level3 = [DOWN * 1.0 + LEFT * 3.0 + RIGHT * i * 1.5 for i in range(5)]

        l1_dots = VGroup(*[Dot(radius=0.18, color=SLATE).shift(p) for p in level1])
        l2_dots = VGroup(*[Dot(radius=0.14, color=SLATE).shift(p) for p in level2])
        l3_dots = VGroup(*[Dot(radius=0.12, color=TERRA, fill_opacity=0.8).shift(p) for p in level3])

        branches_0 = VGroup(*[Line(root.get_bottom(), p, color=SLATE, stroke_width=3) for p in level1])
        branches_1 = VGroup(*[
            Line(level1[i // 2], level2[i], color=SLATE, stroke_width=2)
            for i in range(4)
        ])

        tree_label = ink_txt("every branch continues\n(many-worlds idea)", size=44, color=INK)
        tree_label.shift(DOWN * 3.0)

        self.play(FadeIn(root), run_time=dur * 0.1)
        self.play(Create(branches_0), Create(l1_dots), run_time=dur * 0.25)
        self.play(Create(branches_1), Create(l2_dots), run_time=dur * 0.25)
        self.play(LaggedStart(*[FadeIn(dot) for dot in l3_dots], lag_ratio=0.1), run_time=dur * 0.2)
        self.play(Write(tree_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A18_MeasurementProblem(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A18", 3.18)
        # Portrait: cat top, arrow down, measurement box middle, label below
        cat_icon = VGroup(
            Circle(radius=0.45, color=SLATE, fill_opacity=0.4).shift(UP * 4.0),
            Triangle(color=SLATE, fill_opacity=0.6).scale(0.22).shift(UP * 4.62 + LEFT * 0.3),
            Triangle(color=SLATE, fill_opacity=0.6).scale(0.22).shift(UP * 4.62 + RIGHT * 0.3),
        )

        arrow = Arrow(UP * 3.3, UP * 1.8, color=INK, buff=0.05, stroke_width=5)

        mp_box = Rectangle(width=5.5, height=1.8, color=SLATE, fill_opacity=0.18).shift(UP * 0.7)
        mp_label = ink_txt("measurement\nproblem", size=48, color=INK).move_to(mp_box)

        points_label = ink_txt("Schrödinger's cat\npoints AT this", size=44, color=INK)
        points_label.shift(DOWN * 2.0)

        self.play(Create(cat_icon), run_time=dur * 0.3)
        self.play(GrowArrow(arrow), run_time=dur * 0.2)
        self.play(Create(mp_box), Write(mp_label), run_time=dur * 0.3)
        self.play(Write(points_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)
