import json
from pathlib import Path
from manim import *
import numpy as np

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED_COL = "#C0392B"
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


# INTRO has render=none — skip

class A00_NotAboutCat(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A00", 3.71)
        # Cat icon with crossed-out storybook
        cat_circle = Circle(radius=0.45, color=SLATE, fill_opacity=0.4).shift(LEFT * 2.5)
        # Cat ears
        ear_l = Triangle(color=SLATE, fill_opacity=0.6).scale(0.2).shift(LEFT * 2.9 + UP * 0.65)
        ear_r = Triangle(color=SLATE, fill_opacity=0.6).scale(0.2).shift(LEFT * 2.1 + UP * 0.65)
        cat = VGroup(cat_circle, ear_l, ear_r)

        book = Rectangle(width=1.2, height=1.5, color=INK, fill_opacity=0.15).shift(RIGHT * 2.0)
        book_label = ink_txt("story\nbook", size=18).next_to(book, UP, buff=0.1)
        cross1 = Line(book.get_corner(UL), book.get_corner(DR), color=RED_COL, stroke_width=5)
        cross2 = Line(book.get_corner(UR), book.get_corner(DL), color=RED_COL, stroke_width=5)

        label = ink_txt("not really about\na cat!", size=26, color=INK)
        label.shift(DOWN * 2.5)

        self.play(Create(cat), run_time=dur * 0.25)
        self.play(Create(book), Write(book_label), run_time=dur * 0.25)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.2)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A01_WhereObservationBegins(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.29)
        q_mark = ink_txt("?", size=96, color=TERRA).shift(UP * 0.3)
        obs_label = ink_txt("where does\nobservation begin?", size=28)
        obs_label.shift(DOWN * 2.0)

        self.play(Write(q_mark), run_time=dur * 0.5)
        self.play(Write(obs_label), run_time=dur * 0.35)
        self.wait(dur * 0.15)


class A02_SealedBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 3.42)
        box = Rectangle(width=3.5, height=2.5, color=INK, fill_opacity=0.12).shift(ORIGIN)
        box_label = ink_txt("sealed box", size=24).next_to(box, DOWN, buff=0.25)

        # Quantum trigger icon inside box
        trigger = Circle(radius=0.35, color=TERRA, fill_opacity=0.7).shift(RIGHT * 0.5)
        trigger_label = ink_txt("quantum\ntrigger", size=20, color=INK).next_to(trigger, DOWN, buff=0.2)

        # Question mark — outcome unknown
        q = ink_txt("?", size=48, color=SLATE).shift(LEFT * 0.8)

        self.play(Create(box), Write(box_label), run_time=dur * 0.4)
        self.play(FadeIn(trigger), Write(trigger_label), run_time=dur * 0.3)
        self.play(Write(q), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A03_TwoBranches(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 3.11)
        # Event node branching into two records
        node = Dot(radius=0.2, color=SLATE).shift(LEFT * 2.5)
        branch_up = Line(node.get_right(), RIGHT * 0.5 + UP * 1.3, color=SLATE, stroke_width=3)
        branch_dn = Line(node.get_right(), RIGHT * 0.5 + DOWN * 1.3, color=SLATE, stroke_width=3)

        card_up = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.12).shift(RIGHT * 2.0 + UP * 1.3)
        card_dn = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.12).shift(RIGHT * 2.0 + DOWN * 1.3)

        event_label = ink_txt("quantum event", size=20).next_to(node, LEFT, buff=0.2)
        label = ink_txt("two possible\nrecords", size=24, color=INK).shift(RIGHT * 3.8)

        self.play(FadeIn(node), Write(event_label), run_time=dur * 0.3)
        self.play(Create(branch_up), Create(branch_dn), run_time=dur * 0.25)
        self.play(Create(card_up), Create(card_dn), Write(label), run_time=dur * 0.3)
        self.wait(dur * 0.15)


class A04_TriggerFiredBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 2.46)
        node = Dot(radius=0.2, color=SLATE).shift(LEFT * 2.5)
        branch_up = Line(node.get_right(), RIGHT * 0.5 + UP * 1.3, color=SLATE, stroke_width=3)
        branch_dn = Line(node.get_right(), RIGHT * 0.5 + DOWN * 1.3, color=SLATE, stroke_width=2, stroke_opacity=0.4)
        card_up = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.2).shift(RIGHT * 2.0 + UP * 1.3)
        card_up_label = ink_txt("trigger FIRED", size=20, color=INK).move_to(card_up)
        card_dn = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.1).shift(RIGHT * 2.0 + DOWN * 1.3)
        self.add(node, branch_up, branch_dn, card_dn)

        self.play(Create(card_up), Write(card_up_label), run_time=dur * 0.7)
        self.wait(dur * 0.3)


class A05_TriggerQuietBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 2.93)
        node = Dot(radius=0.2, color=SLATE).shift(LEFT * 2.5)
        branch_up = Line(node.get_right(), RIGHT * 0.5 + UP * 1.3, color=SLATE, stroke_width=2, stroke_opacity=0.6)
        branch_dn = Line(node.get_right(), RIGHT * 0.5 + DOWN * 1.3, color=SLATE, stroke_width=3)
        card_up = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.15).shift(RIGHT * 2.0 + UP * 1.3)
        card_up_label = ink_txt("trigger FIRED", size=20, color=INK).move_to(card_up)
        card_dn = Rectangle(width=2.5, height=0.9, color=SLATE, fill_opacity=0.2).shift(RIGHT * 2.0 + DOWN * 1.3)
        card_dn_label = ink_txt("trigger quiet", size=20, color=SLATE).move_to(card_dn)
        self.add(node, branch_up, branch_dn, card_up, card_up_label)

        self.play(Create(card_dn), Write(card_dn_label), run_time=dur * 0.65)
        self.wait(dur * 0.35)


class A06_CatConnectedToBranches(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 2.82)
        # Cat marker connected to both branches
        node = Dot(radius=0.2, color=SLATE).shift(LEFT * 2.5)
        branch_up = Line(node.get_right(), RIGHT * 0.5 + UP * 1.2, color=SLATE, stroke_width=3)
        branch_dn = Line(node.get_right(), RIGHT * 0.5 + DOWN * 1.2, color=SLATE, stroke_width=3)
        card_up = Rectangle(width=2.2, height=0.8, color=SLATE, fill_opacity=0.15).shift(RIGHT * 2.0 + UP * 1.2)
        card_dn = Rectangle(width=2.2, height=0.8, color=SLATE, fill_opacity=0.15).shift(RIGHT * 2.0 + DOWN * 1.2)
        self.add(node, branch_up, branch_dn, card_up, card_dn)

        cat_dot = Dot(radius=0.25, color=INK, fill_opacity=0.7).shift(LEFT * 4.5)
        cat_label = ink_txt("cat", size=24).next_to(cat_dot, DOWN, buff=0.1)
        cat_line_up = DashedLine(cat_dot.get_right(), card_up.get_left(), color=INK, stroke_width=2)
        cat_line_dn = DashedLine(cat_dot.get_right(), card_dn.get_left(), color=INK, stroke_width=2)

        not_separate = ink_txt("cat is NOT\nseparate from branches", size=22, color=INK)
        not_separate.shift(DOWN * 2.8)

        self.play(FadeIn(cat_dot), Write(cat_label), run_time=dur * 0.3)
        self.play(Create(cat_line_up), Create(cat_line_dn), run_time=dur * 0.35)
        self.play(Write(not_separate), run_time=dur * 0.3)
        self.wait(dur * 0.05)


class A07_ExperienceFollowsEvent(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 3.79)
        branch_up = Line(LEFT * 1.5 + UP * 1.0, RIGHT * 1.5 + UP * 1.0, color=TERRA, stroke_width=4)
        branch_dn = Line(LEFT * 1.5 + DOWN * 1.0, RIGHT * 1.5 + DOWN * 1.0, color=SLATE, stroke_width=4)

        up_label = ink_txt("fired  →  cat sees result", size=32, color=INK).shift(UP * 1.35)
        dn_label = ink_txt("quiet  →  cat sees nothing", size=32, color=SLATE).shift(DOWN * 1.35)

        arrow = Arrow(LEFT * 1.5 + UP * 0.2, LEFT * 1.5 + DOWN * 0.2, color=INK, buff=0.05)
        follows = ink_txt("experience\nfollows event", size=32)
        follows.shift(LEFT * 3.5)

        self.play(Create(branch_up), Write(up_label), run_time=dur * 0.3)
        self.play(Create(branch_dn), Write(dn_label), run_time=dur * 0.3)
        self.play(GrowArrow(arrow), Write(follows), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A08_FiredTriggerPair(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 3.11)
        # Fired trigger + cat sees result = paired
        trigger_box = Rectangle(width=2.2, height=0.9, color=TERRA, fill_opacity=0.2).shift(LEFT * 2.5 + UP * 0.5)
        trigger_label = ink_txt("trigger FIRED", size=20, color=TERRA).move_to(trigger_box)

        cat_box = Rectangle(width=2.2, height=0.9, color=TERRA, fill_opacity=0.2).shift(RIGHT * 2.5 + UP * 0.5)
        cat_label = ink_txt("cat sees\nresult", size=20, color=TERRA).move_to(cat_box)

        link = DoubleArrow(trigger_box.get_right(), cat_box.get_left(), color=TERRA, buff=0.05)

        pair_label = ink_txt("always paired", size=22, color=TERRA).shift(DOWN * 1.5)

        self.play(Create(trigger_box), Write(trigger_label), run_time=dur * 0.3)
        self.play(Create(link), run_time=dur * 0.2)
        self.play(Create(cat_box), Write(cat_label), run_time=dur * 0.3)
        self.play(Write(pair_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A09_QuietTriggerPair(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A09", 2.87)
        # Quiet trigger + cat sees nothing
        trigger_box = Rectangle(width=2.2, height=0.9, color=SLATE, fill_opacity=0.2).shift(LEFT * 2.5 + DOWN * 0.5)
        trigger_label = ink_txt("trigger quiet", size=20, color=SLATE).move_to(trigger_box)

        cat_box = Rectangle(width=2.2, height=0.9, color=SLATE, fill_opacity=0.2).shift(RIGHT * 2.5 + DOWN * 0.5)
        cat_label = ink_txt("cat sees\nnothing", size=20, color=SLATE).move_to(cat_box)

        link = DoubleArrow(trigger_box.get_right(), cat_box.get_left(), color=SLATE, buff=0.05)

        self.play(Create(trigger_box), Write(trigger_label), run_time=dur * 0.35)
        self.play(Create(link), run_time=dur * 0.2)
        self.play(Create(cat_box), Write(cat_label), run_time=dur * 0.35)
        self.wait(dur * 0.1)


class A10_MixedRecordCrossedOut(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A10", 3.71)
        # Mixed record crossed out
        mixed_box = Rectangle(width=3.5, height=1.0, color=RED_COL, fill_opacity=0.15)
        mixed_label = ink_txt("fired BUT unseen", size=22, color=INK).next_to(mixed_box, UP, buff=0.15)
        cross1 = Line(mixed_box.get_corner(UL), mixed_box.get_corner(DR), color=RED_COL, stroke_width=5)
        cross2 = Line(mixed_box.get_corner(UR), mixed_box.get_corner(DL), color=RED_COL, stroke_width=5)

        no_label = ink_txt("does NOT belong!", size=26, color=INK).shift(DOWN * 2.0)

        self.play(Create(mixed_box), Write(mixed_label), run_time=dur * 0.35)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.25)
        self.play(Write(no_label), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A11_EntanglementLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A11", 3.84)
        # Two linked record boxes with entanglement label
        box_a = Rectangle(width=2.2, height=0.9, color=SLATE, fill_opacity=0.2).shift(LEFT * 2.5)
        label_a = ink_txt("triggered record", size=18, color=INK).move_to(box_a)
        box_b = Rectangle(width=2.2, height=0.9, color=SLATE, fill_opacity=0.2).shift(RIGHT * 2.5)
        label_b = ink_txt("quiet record", size=18, color=SLATE).move_to(box_b)

        ent_label = ink_txt("ENTANGLEMENT", size=30, color=INK).shift(UP * 2.0)
        ent_sub = ink_txt("not ordinary ignorance", size=22, color=SLATE).shift(UP * 1.2)

        link = DoubleArrow(box_a.get_right(), box_b.get_left(), color=SLATE, buff=0.05, stroke_width=4)

        self.play(Create(box_a), Create(box_b), Write(label_a), Write(label_b), run_time=dur * 0.25)
        self.play(Create(link), run_time=dur * 0.3)
        self.play(Write(ent_label), run_time=dur * 0.3)
        self.play(Write(ent_sub), run_time=dur * 0.25)
        self.wait(dur * 0.15)


class A12_ObserverLinkedToRecord(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A12", 3.6)
        # Box opened, observer linked to shared record
        box = Rectangle(width=2.5, height=2.5, color=INK, fill_opacity=0.1, stroke_width=3)
        box.shift(LEFT * 1.5)
        record = ink_txt("record\n(branch)", size=20, color=TERRA).move_to(box)

        observer = Circle(radius=0.35, color=SLATE, fill_opacity=0.5).shift(RIGHT * 3.0)
        obs_label = ink_txt("observer", size=20).next_to(observer, DOWN, buff=0.15)

        link_arrow = Arrow(box.get_right(), observer.get_left(), color=TERRA, buff=0.05, stroke_width=4)
        link_label = ink_txt("opening the box\nlinks observer", size=22, color=TERRA)
        link_label.shift(DOWN * 2.5)

        self.play(Create(box), Write(record), run_time=dur * 0.3)
        self.play(Create(observer), Write(obs_label), run_time=dur * 0.25)
        self.play(GrowArrow(link_arrow), run_time=dur * 0.25)
        self.play(Write(link_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A13_ObserverBelongsToBranch(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A13", 2.93)
        branch_up = Rectangle(width=5.0, height=1.0, color=SLATE, fill_opacity=0.15).shift(UP * 1.0)
        branch_dn = Rectangle(width=5.0, height=1.0, color=SLATE, fill_opacity=0.15).shift(DOWN * 1.0)
        up_txt = ink_txt("branch A: fired + cat saw + observer A", size=18, color=INK).move_to(branch_up)
        dn_txt = ink_txt("branch B: quiet + cat nothing + observer B", size=18, color=SLATE).move_to(branch_dn)

        obs_label = ink_txt("observer belongs\nto a branch too", size=26, color=INK)
        obs_label.shift(DOWN * 2.8)

        self.play(Create(branch_up), Write(up_txt), run_time=dur * 0.35)
        self.play(Create(branch_dn), Write(dn_txt), run_time=dur * 0.35)
        self.play(Write(obs_label), run_time=dur * 0.25)
        self.wait(dur * 0.05)


class A14_CollapseSelectsHistory(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A14", 3.0)
        # Two histories, one highlighted / selected
        hist_a = Rectangle(width=3.5, height=1.0, color=SLATE, fill_opacity=0.15).shift(UP * 1.2)
        hist_a_lbl = ink_txt("history A", size=22, color=SLATE).move_to(hist_a)

        hist_b = Rectangle(width=3.5, height=1.0, color=SLATE, fill_opacity=0.5, stroke_width=4).shift(DOWN * 0.5)
        hist_b_lbl = ink_txt("history B  ✓", size=22, color=INK).move_to(hist_b)

        selected = ink_txt("collapse → one shared\nhistory (seems to)", size=24)
        selected.shift(DOWN * 2.5)

        self.play(Create(hist_a), Write(hist_a_lbl), run_time=dur * 0.3)
        self.play(Create(hist_b), Write(hist_b_lbl), run_time=dur * 0.3)
        self.play(Write(selected), run_time=dur * 0.3)
        self.wait(dur * 0.1)


class A15_FinalObserverQuestion(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A15", 3.47)
        q_chain = VGroup(*[
            Dot(radius=0.18, color=SLATE).shift(LEFT * 3.5 + RIGHT * i * 1.5)
            for i in range(4)
        ])
        arrows = VGroup(*[
            Arrow(q_chain[i].get_right(), q_chain[i + 1].get_left(), color=SLATE, buff=0.05)
            for i in range(3)
        ])
        labels = VGroup(*[
            ink_txt(t, size=16).next_to(q_chain[i], DOWN, buff=0.15)
            for i, t in enumerate(["atom", "detector", "cat", "you"])
        ])

        big_q = ink_txt("?", size=72, color=INK).shift(RIGHT * 3.8 + UP * 0.3)
        final_label = ink_txt("quantum theory\ndoes not name\nthe final observer", size=24, color=INK)
        final_label.shift(DOWN * 2.5)

        self.play(LaggedStart(*[FadeIn(d) for d in q_chain], lag_ratio=0.15), run_time=dur * 0.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
                  LaggedStart(*[Write(l) for l in labels], lag_ratio=0.15), run_time=dur * 0.3)
        self.play(Write(big_q), run_time=dur * 0.2)
        self.play(Write(final_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A16_OneOutcomeBecomesReal(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A16", 3.84)
        outcome_box = Rectangle(width=3.0, height=1.2, color=SLATE, fill_opacity=0.2)
        outcome_label = ink_txt("one outcome\nbecomes real", size=24, color=INK).move_to(outcome_box)

        unknown = Rectangle(width=3.0, height=1.2, color=RED_COL, fill_opacity=0.12).shift(DOWN * 2.0)
        unk_label = ink_txt("mechanism: ???", size=22, color=RED_COL).move_to(unknown)

        self.play(Create(outcome_box), Write(outcome_label), run_time=dur * 0.45)
        self.play(Create(unknown), Write(unk_label), run_time=dur * 0.4)
        self.wait(dur * 0.15)


class A17_ManyBranchTree(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A17", 4.13)
        # Tree of branches growing out
        root = Dot(radius=0.2, color=SLATE).shift(LEFT * 4.0)

        level1 = [LEFT * 2.0 + UP * 1.0, LEFT * 2.0 + DOWN * 1.0]
        level2 = [
            ORIGIN + UP * 1.8, ORIGIN + UP * 0.6,
            ORIGIN + DOWN * 0.6, ORIGIN + DOWN * 1.8
        ]
        level3 = [RIGHT * 2.0 + UP * (2.1 - i * 0.7) for i in range(5)]

        l1_dots = VGroup(*[Dot(radius=0.15, color=SLATE).shift(p) for p in level1])
        l2_dots = VGroup(*[Dot(radius=0.12, color=SLATE).shift(p) for p in level2])
        l3_dots = VGroup(*[Dot(radius=0.10, color=TERRA, fill_opacity=0.8).shift(p) for p in level3])

        branches_0 = VGroup(*[Line(root.get_right(), p, color=SLATE, stroke_width=3) for p in level1])
        branches_1 = VGroup(*[
            Line(level1[i // 2], level2[i], color=SLATE, stroke_width=2)
            for i in range(4)
        ])

        tree_label = ink_txt("every branch continues\n(many-worlds idea)", size=24, color=INK)
        tree_label.shift(DOWN * 3.0)

        self.play(FadeIn(root), run_time=dur * 0.1)
        self.play(Create(branches_0), Create(l1_dots), run_time=dur * 0.25)
        self.play(Create(branches_1), Create(l2_dots), run_time=dur * 0.25)
        self.play(LaggedStart(*[FadeIn(d) for d in l3_dots], lag_ratio=0.1), run_time=dur * 0.2)
        self.play(Write(tree_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A18_MeasurementProblem(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A18", 3.19)
        # Final summary: measurement problem
        cat_icon = VGroup(
            Circle(radius=0.35, color=SLATE, fill_opacity=0.4),
            Triangle(color=SLATE, fill_opacity=0.6).scale(0.18).shift(LEFT * 0.25 + UP * 0.5),
            Triangle(color=SLATE, fill_opacity=0.6).scale(0.18).shift(RIGHT * 0.25 + UP * 0.5),
        ).shift(LEFT * 3.0)

        arrow = Arrow(cat_icon.get_right(), RIGHT * 0.0, color=INK, buff=0.1, stroke_width=4)

        mp_box = Rectangle(width=3.5, height=1.5, color=SLATE, fill_opacity=0.18).shift(RIGHT * 2.5)
        mp_label = ink_txt("measurement\nproblem", size=26, color=INK).move_to(mp_box)

        points_label = ink_txt("Schrödinger's cat\npoints AT this", size=22)
        points_label.shift(DOWN * 2.5)

        self.play(Create(cat_icon), run_time=dur * 0.3)
        self.play(GrowArrow(arrow), run_time=dur * 0.2)
        self.play(Create(mp_box), Write(mp_label), run_time=dur * 0.3)
        self.play(Write(points_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)
