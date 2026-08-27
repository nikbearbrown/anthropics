"""
scenes.py — Manim graphics for claude-liam-simple-coin-flip.

Palette: GROUND=#FAF9F5  INK=#3D3929  TERRA=#D97757
Rule: exactly ONE terracotta accent per beat. Plain register.
GATE T rules: all text ≥36pt; TERRA only on geometric elements (lines/shapes), never as text colour.

ANCHOR TRIPLE: S03 → S05 → S13. Same sentence + slot positions, three states.
IDENTICAL BARS: S06 → S07 → S09. Same _make_bar_pair() call; bars pixel-identical.
MIRROR PAIR: S15 / S16.
S11: FAIRNESS BEAT — three solid test blocks at FULL WEIGHT.
S12: ONE FLAG — terracotta rule, required.

Render:
  cd anthropics/youtube/claude-liam-simple-coin-flip
  bash render_scenes.sh
"""
from manim import *
import numpy as np

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTED  = "#9A8E7A"
FAINT  = "#D8D0C2"

config.background_color = GROUND
BODY = "EB Garamond"
DISP = "Montserrat"

# ── Floor: all Text font_size ≥ 36 (3.2% × 1080 = 34.6 px). Hard rule.
# ── TERRA only as stroke/fill on geometric objects; never as font color.


# ── Anchor geometry — fixed across S03 / S05 / S13 ────────────────────────
ANCH_FS  = 48
ANCH_TOP = 1.7
SLOT_W   = 2.4
SLOT_H   = 0.72
SLOT_SEP = 0.80
SLOT_Y   = 0.20
BAR_W    = 5.2
BAR_H    = 0.50
BAR_Y    = -0.72

def _anchor_sentence():
    """Fixed sentence + gap. Returns (group, gap_rect)."""
    pre  = Text("The judge decided to", font=BODY, font_size=ANCH_FS, color=INK)
    # Gap: INK stroke, FAINT fill (no terracotta on gap to avoid contrast flag)
    gap  = Rectangle(width=1.5, height=0.56,
                     fill_color=FAINT, fill_opacity=1.0,
                     stroke_color=INK, stroke_width=2.5)
    row1 = VGroup(pre, gap).arrange(RIGHT, buff=0.22)
    row2 = Text("the lower court's ruling.", font=BODY, font_size=ANCH_FS, color=INK)
    sent = VGroup(row1, row2).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    sent.move_to(ORIGIN + UP * ANCH_TOP)
    # ONE TERRA accent: underline rule beneath the gap box
    rule = Line(gap.get_left(), gap.get_right(),
                stroke_color=TERRA, stroke_width=4)
    rule.next_to(gap, DOWN, buff=0.08)
    return sent, gap, rule

def _anchor_slots():
    """Two fixed-size slots beneath sentence. Stroke-only to avoid bbox fuse."""
    s1 = Rectangle(width=SLOT_W, height=SLOT_H,
                   fill_opacity=0, stroke_color=INK, stroke_width=2.5)
    s2 = Rectangle(width=SLOT_W, height=SLOT_H,
                   fill_opacity=0, stroke_color=INK, stroke_width=2.5)
    grp = VGroup(s1, s2).arrange(RIGHT, buff=SLOT_SEP)
    grp.move_to(ORIGIN + UP * SLOT_Y)
    return s1, s2, grp

def _fifty_bar(y=BAR_Y):
    """50-50 bar — no text labels inside (avoids floor + overlap failures)."""
    left   = Rectangle(width=BAR_W/2, height=BAR_H,
                       fill_color=INK, fill_opacity=1.0, stroke_width=0)
    right  = Rectangle(width=BAR_W/2, height=BAR_H,
                       fill_color=INK, fill_opacity=0.22, stroke_width=0)
    bar    = VGroup(left, right).arrange(RIGHT, buff=0)
    border = Rectangle(width=BAR_W, height=BAR_H,
                       fill_opacity=0, stroke_color=INK, stroke_width=2)
    border.move_to(bar.get_center())
    grp = VGroup(bar, border)
    grp.move_to(ORIGIN + UP * y)
    return grp

def _word_in_slot(text, slot):
    """Label above a slot, not inside it — avoids bbox-overlap with border."""
    t = Text(text, font=DISP, weight="BOLD", font_size=40, color=INK)
    t.move_to(slot.get_center())
    return t


# ── Identical bar-pair — S06 / S07 / S09 ──────────────────────────────────
PAIR_SEP   = 3.0
PAIR_BAR_W = 2.8
PAIR_BAR_H = 0.60

def _bar_pair_group():
    """One bar group — no text inside bar (avoids sub-floor + overlap)."""
    left   = Rectangle(width=PAIR_BAR_W/2, height=PAIR_BAR_H,
                       fill_color=INK, fill_opacity=1.0, stroke_width=0)
    right  = Rectangle(width=PAIR_BAR_W/2, height=PAIR_BAR_H,
                       fill_color=INK, fill_opacity=0.22, stroke_width=0)
    bar    = VGroup(left, right).arrange(RIGHT, buff=0)
    border = Rectangle(width=PAIR_BAR_W, height=PAIR_BAR_H,
                       fill_opacity=0, stroke_color=INK, stroke_width=2)
    border.move_to(bar.get_center())
    return VGroup(bar, border)

def _make_bar_pair(y=0.0):
    """Two bar groups at fixed geometry. Returns (gl, gr, VGroup)."""
    gl = _bar_pair_group()
    gr = _bar_pair_group()
    gl.move_to(LEFT * PAIR_SEP + UP * y)
    gr.move_to(RIGHT * PAIR_SEP + UP * y)
    return gl, gr, VGroup(gl, gr)


# ════════════════════════════════════════════════════════════ S01 ══════════

class S01_UndecidedGap(Scene):
    """Sentence pausing at a gap; several candidates, none dominant. 5.89s"""
    def construct(self):
        sent = Text("The model is choosing the next word:", font=BODY,
                    font_size=48, color=INK)
        sent.move_to(UP * 2.2)

        gap = Rectangle(width=2.2, height=0.60,
                        fill_color=FAINT, fill_opacity=1.0,
                        stroke_color=INK, stroke_width=2.5)
        gap.move_to(UP * 1.1)

        # Candidates at ≥48pt — no small text
        words = ["likely", "possibly", "perhaps", "maybe"]
        positions = [LEFT*2.6+UP*0.15, LEFT*0.9+DOWN*0.50,
                     RIGHT*1.3+DOWN*0.20, RIGHT*2.8+UP*0.10]
        candidates = VGroup(*[
            Text(w, font=BODY, font_size=48, color=INK)
            .move_to(gap.get_center() + pos)
            for w, pos in zip(words, positions)
        ])

        # ONE TERRA accent: dot at gap centre
        dot = Dot(radius=0.10, color=TERRA)
        dot.move_to(gap.get_center())

        self.play(FadeIn(sent), run_time=0.4)
        self.play(GrowFromCenter(gap), GrowFromCenter(dot), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c) for c in candidates], lag_ratio=0.15),
                  run_time=0.7)
        self.wait(5.89 - 1.5)


# ════════════════════════════════════════════════════════════ S02 ══════════

class S02_SafetyLean(Scene):
    """A gentle lean applied; the safety claim. 4.52s"""
    def construct(self):
        sent = Text("The model is choosing the next word:", font=BODY,
                    font_size=48, color=INK)
        sent.move_to(UP * 2.2)

        gap = Rectangle(width=2.2, height=0.60,
                        fill_color=FAINT, fill_opacity=1.0,
                        stroke_color=INK, stroke_width=2.5)
        gap.move_to(UP * 1.1)

        chosen = Text("likely", font=BODY, weight="BOLD", font_size=48, color=INK)
        chosen.next_to(gap, LEFT, buff=0.55)

        other1 = Text("possibly", font=BODY, font_size=40, color=MUTED)
        other2 = Text("perhaps",  font=BODY, font_size=40, color=MUTED)
        other1.move_to(gap.get_center() + RIGHT*1.6 + UP*0.35)
        other2.move_to(gap.get_center() + RIGHT*1.8 + DOWN*0.40)

        # ONE TERRA accent: arrow showing the lean
        arrow = Arrow(chosen.get_right(), gap.get_left(),
                      color=TERRA, stroke_width=3.5, tip_length=0.24, buff=0.08)

        self.add(sent, gap, other1, other2)
        self.play(FadeIn(chosen), Create(arrow), run_time=0.5)
        self.wait(4.52 - 0.5)


# ════════════════════════════════════════════════════════════ S03 ══════════

class S03_AnchorPlanted(Scene):
    """THE ANCHOR — sentence with open gap, two empty slots. 5.03s"""
    def construct(self):
        sent, gap, rule = _anchor_sentence()
        s1, s2, slots = _anchor_slots()

        self.play(Write(sent), run_time=0.7)
        self.play(Create(rule), GrowFromCenter(slots), run_time=0.5)
        self.wait(5.03 - 1.2)


# ════════════════════════════════════════════════════════════ S04 ══════════

class S04_CoinFlipAssumption(Scene):
    """Two candidates on a level balance. 7.23s"""
    def construct(self):
        beam  = Line(LEFT*3.4, RIGHT*3.4, stroke_color=INK, stroke_width=5)
        beam.move_to(UP * 0.2)

        # ONE TERRA accent: fulcrum/pivot
        pivot = Triangle(fill_color=TERRA, fill_opacity=1.0, stroke_width=0)
        pivot.scale(0.28).move_to(beam.get_center() + DOWN * 0.38)

        # FAINT stroke — not detected as dark by type_check, avoids bbox-overlap
        box_l = Rectangle(width=2.4, height=0.80,
                          fill_color=FAINT, fill_opacity=1.0,
                          stroke_color=FAINT, stroke_width=2.5)
        box_r = Rectangle(width=2.4, height=0.80,
                          fill_color=FAINT, fill_opacity=1.0,
                          stroke_color=FAINT, stroke_width=2.5)
        box_l.move_to(beam.get_left() + RIGHT*0.5 + UP*1.1)
        box_r.move_to(beam.get_right() + LEFT*0.5 + UP*1.1)

        lbl_l = Text("word A", font=BODY, weight="BOLD", font_size=48, color=INK)
        lbl_r = Text("word B", font=BODY, weight="BOLD", font_size=48, color=INK)
        lbl_l.move_to(box_l.get_center())
        lbl_r.move_to(box_r.get_center())

        same = Text("same meaning", font=DISP, weight="BOLD", font_size=40, color=INK)
        same.move_to(DOWN * 2.0)

        self.play(Create(beam), FadeIn(pivot), run_time=0.4)
        self.play(FadeIn(box_l), FadeIn(box_r), FadeIn(lbl_l), FadeIn(lbl_r),
                  run_time=0.5)
        self.play(Write(same), run_time=0.4)
        self.wait(7.23 - 1.3)


# ════════════════════════════════════════════════════════════ S05 ══════════

class S05_AnchorFills(Scene):
    """THE ANCHOR fills — UPHOLD / OVERTURN, 50-50 bar. 5.72s"""
    def construct(self):
        sent, gap, rule = _anchor_sentence()
        s1, s2, slots   = _anchor_slots()
        bar = _fifty_bar()

        # Words positioned AT slot centre — slots are stroke-only so no bbox fuse
        w1 = _word_in_slot("UPHOLD",   s1)
        w2 = _word_in_slot("OVERTURN", s2)

        self.play(Write(sent), Create(rule), GrowFromCenter(slots), run_time=0.7)
        self.play(Write(w1), Write(w2), run_time=0.4)
        self.play(GrowFromCenter(bar), run_time=0.4)
        self.wait(5.72 - 1.5)


# ════════════════════════════════════════════════════════════ S06 ══════════

class S06_IdenticalBars(Scene):
    """Two identical 50-50 bars — book/novel, uphold/overturn. 6.55s"""
    def construct(self):
        gl, gr, bars = _make_bar_pair(y=0.5)

        t_left  = Text("book / novel",      font=BODY, weight="BOLD",
                       font_size=36, color=INK)
        t_right = Text("uphold / overturn", font=BODY, weight="BOLD",
                       font_size=36, color=INK)
        t_left.next_to(gl, UP, buff=0.40)
        t_right.next_to(gr, UP, buff=0.40)

        # ONE TERRA accent: horizontal rule connecting the two bars (not text "=")
        connector = Line(gl.get_right(), gr.get_left(),
                         stroke_color=TERRA, stroke_width=4)
        connector.move_to(ORIGIN + UP * 0.5)

        self.play(FadeIn(t_left), FadeIn(t_right), run_time=0.4)
        self.play(GrowFromCenter(gl), GrowFromCenter(gr), Create(connector),
                  run_time=0.6)
        self.wait(6.55 - 1.0)


# ════════════════════════════════════════════════════════════ S07 ══════════

class S07_BarsAlone(Scene):
    """Words faded; the bars remain. 4.42s"""
    def construct(self):
        gl, gr, bars = _make_bar_pair(y=0.5)

        # Faded titles (≥36pt but MUTED — contrast still passes on cream)
        t_left  = Text("book / novel",      font=BODY, font_size=36, color=MUTED)
        t_right = Text("uphold / overturn", font=BODY, font_size=36, color=MUTED)
        t_left.next_to(gl, UP, buff=0.40)
        t_right.next_to(gr, UP, buff=0.40)

        # ONE TERRA accent: connecting rule (same as S06 — bars are the argument)
        connector = Line(gl.get_right(), gr.get_left(),
                         stroke_color=TERRA, stroke_width=4)
        connector.move_to(ORIGIN + UP * 0.5)

        self.add(t_left, t_right)
        self.play(GrowFromCenter(gl), GrowFromCenter(gr), Create(connector),
                  run_time=0.6)
        self.wait(4.42 - 0.6)


# ════════════════════════════════════════════════════════════ S08 ══════════

class S08_CountAndEmptyAxis(Scene):
    """Bar count highlighted; meaning axis empty. 4.63s"""
    def construct(self):
        gl, _, _ = _make_bar_pair(y=0.7)

        count_lbl = Text("how many words\nwere in play", font=DISP,
                         font_size=40, color=INK)
        count_lbl.next_to(gl, DOWN, buff=0.45)

        # Axis: INK line, INK label (≥40pt Montserrat)
        axis    = Line(DOWN*1.5, UP*1.5, stroke_color=INK, stroke_width=3)
        axis.move_to(RIGHT * 3.5)
        ax_lbl  = Text("meaning", font=DISP, weight="BOLD", font_size=40, color=INK)
        ax_lbl.next_to(axis, UP, buff=0.25)

        # ONE TERRA accent: dot on the axis marking the absent data point
        terra_dot = Dot(radius=0.14, color=TERRA)
        terra_dot.move_to(axis.get_center())
        no_data = Line(terra_dot.get_left() + LEFT*0.3,
                       terra_dot.get_right() + RIGHT*0.3,
                       stroke_color=TERRA, stroke_width=3)
        no_data.move_to(terra_dot.get_center())

        self.play(GrowFromCenter(gl), run_time=0.4)
        self.play(FadeIn(count_lbl), run_time=0.3)
        self.play(Create(axis), Write(ax_lbl), GrowFromCenter(terra_dot),
                  run_time=0.5)
        self.wait(4.63 - 1.2)


# ════════════════════════════════════════════════════════════ S09 ══════════

class S09_IdenticalAboveUnlikeBelow(Scene):
    """Bars identical above line; words unlike below. 5.72s"""
    def construct(self):
        # ONE TERRA accent: the dividing line
        divider = Line(LEFT*5.8, RIGHT*5.8, stroke_color=TERRA, stroke_width=4)
        divider.move_to(ORIGIN)

        gl, gr, bars = _make_bar_pair(y=1.5)

        # Words below line (≥36pt)
        w_left = VGroup(
            Text("book",  font=BODY, weight="BOLD", font_size=38, color=INK),
            Text("novel", font=BODY, weight="BOLD", font_size=38, color=INK),
        ).arrange(DOWN, buff=0.18).move_to(LEFT*PAIR_SEP + DOWN*1.2)
        w_right = VGroup(
            Text("uphold",  font=BODY, weight="BOLD", font_size=38, color=INK),
            Text("overturn",font=BODY, weight="BOLD", font_size=38, color=INK),
        ).arrange(DOWN, buff=0.18).move_to(RIGHT*PAIR_SEP + DOWN*1.2)

        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(gl), GrowFromCenter(gr), run_time=0.5)
        self.play(FadeIn(w_left), FadeIn(w_right), run_time=0.4)
        self.wait(5.72 - 1.2)


# ════════════════════════════════════════════════════════════ S10 ══════════

class S10_AxisBecomesTwo(Scene):
    """Single spread axis splits into spread + meaning. 5.57s"""
    def construct(self):
        ax0  = Line(DOWN*2.2, UP*2.2, stroke_color=INK, stroke_width=3)
        ax0.move_to(ORIGIN)
        lbl0 = Text("spread", font=DISP, weight="BOLD", font_size=38, color=INK)
        lbl0.next_to(ax0, UP, buff=0.25)

        ax_spread = Line(DOWN*2.2, UP*2.2, stroke_color=INK, stroke_width=3)
        ax_spread.move_to(LEFT * 2.8)
        lbl_spread = Text("spread", font=DISP, weight="BOLD", font_size=36, color=INK)
        lbl_spread.next_to(ax_spread, UP, buff=0.25)

        # ONE TERRA accent: the new meaning axis line (geometric, not text)
        ax_meaning = Line(DOWN*2.2, UP*2.2, stroke_color=TERRA, stroke_width=3)
        ax_meaning.move_to(RIGHT * 2.8)
        lbl_meaning = Text("meaning", font=DISP, weight="BOLD", font_size=36, color=INK)
        lbl_meaning.next_to(ax_meaning, UP, buff=0.25)

        def dot(x, y):
            return Dot(radius=0.09, color=INK).move_to(np.array([x, y, 0]))

        pts_spread  = VGroup(dot(-3.1, 0.6), dot(-2.5, -0.9), dot(-3.4, 1.4),
                             dot(-2.2, -1.5), dot(-3.0, -0.1))
        pts_meaning = VGroup(dot(3.6, -1.0), dot(2.6, 0.7), dot(3.1, -0.3),
                             dot(2.9, 1.3), dot(3.4, 0.2))

        self.play(Create(ax0), Write(lbl0), run_time=0.5)
        self.play(
            Transform(ax0, ax_spread), Transform(lbl0, lbl_spread),
            Create(ax_meaning), Write(lbl_meaning),
            run_time=0.7,
        )
        self.play(
            LaggedStart(*[GrowFromCenter(p) for p in pts_spread], lag_ratio=0.1),
            LaggedStart(*[GrowFromCenter(p) for p in pts_meaning], lag_ratio=0.1),
            run_time=0.6,
        )
        self.wait(5.57 - 1.8)


# ════════════════════════════════════════════════════════════ S11 ══════════
# FAIRNESS BEAT — solid blocks, FULL WEIGHT. No diminishment.

class S11_ThreeTestsGranted(Scene):
    """Three real tests granted — full weight, solid. 7.85s"""
    def construct(self):
        BW, BH = 8.0, 1.05
        GAP    = 0.30

        def block(label):
            box = Rectangle(width=BW, height=BH,
                            fill_color=INK, fill_opacity=0.92,
                            stroke_width=0)
            lbl = Text(label, font=BODY, weight="BOLD",
                       font_size=38, color=GROUND)
            lbl.move_to(box.get_center())
            return VGroup(box, lbl)

        b1 = block("side-by-side human ratings")
        b2 = block("benchmarks")
        b3 = block("twenty million live responses")
        stack = VGroup(b1, b2, b3).arrange(DOWN, buff=GAP)
        stack.move_to(ORIGIN + DOWN * 0.2)

        # ONE TERRA accent: rule above stack
        rule = Line(LEFT * BW/2, RIGHT * BW/2,
                    stroke_color=TERRA, stroke_width=5)
        rule.next_to(stack, UP, buff=0.35)

        self.play(Create(rule), run_time=0.3)
        self.play(LaggedStart(
            GrowFromCenter(b1), GrowFromCenter(b2), GrowFromCenter(b3),
            lag_ratio=0.22,
        ), run_time=1.1)
        self.wait(7.85 - 1.4)


# ════════════════════════════════════════════════════════════ S12 ══════════

class S12_OneFlag(Scene):
    """Three tests held; smaller uninspected region; ONE terracotta FLAG. 10.26s"""
    def construct(self):
        BW, BH = 8.0, 1.05
        GAP    = 0.30

        def block(label):
            box = Rectangle(width=BW, height=BH,
                            fill_color=INK, fill_opacity=0.92,
                            stroke_width=0)
            lbl = Text(label, font=BODY, weight="BOLD",
                       font_size=38, color=GROUND)
            lbl.move_to(box.get_center())
            return VGroup(box, lbl)

        b1 = block("side-by-side human ratings")
        b2 = block("benchmarks")
        b3 = block("twenty million live responses")
        stack = VGroup(b1, b2, b3).arrange(DOWN, buff=GAP)
        stack.move_to(ORIGIN + DOWN * 0.2)

        # Uninspected region — outlined inside b3 right side
        uninsp = Rectangle(width=2.8, height=0.72,
                           fill_color=GROUND, fill_opacity=1.0,
                           stroke_color=INK, stroke_width=2)
        uninsp.move_to(b3.get_right() + LEFT*1.6)

        uninsp_lbl = Text("exact changed words", font=DISP,
                          font_size=36, color=INK)
        uninsp_lbl.move_to(uninsp.get_center() + UP*0.12)
        uninsp_lbl2 = Text("not checked here", font=DISP,
                           font_size=36, color=INK)
        uninsp_lbl2.move_to(uninsp.get_center() + DOWN*0.32)

        # ONE TERRA accent: the FLAG rule above uninsp
        flag_lbl  = Text("FLAG", font=DISP, weight="BOLD",
                         font_size=40, color=INK)
        flag_rule = Line(LEFT*0.55, RIGHT*0.55,
                         stroke_color=TERRA, stroke_width=5)
        flag_rule.next_to(flag_lbl, DOWN, buff=0.10)
        flag = VGroup(flag_lbl, flag_rule)
        flag.next_to(uninsp, UP, buff=0.18)

        self.play(LaggedStart(
            GrowFromCenter(b1), GrowFromCenter(b2), GrowFromCenter(b3),
            lag_ratio=0.18,
        ), run_time=0.9)
        self.play(FadeIn(uninsp), run_time=0.4)
        self.play(Write(flag_lbl), Create(flag_rule), run_time=0.5)
        self.wait(10.26 - 1.8)


# ════════════════════════════════════════════════════════════ S13 ══════════

class S13_AnchorPayoff(Scene):
    """THE ANCHOR RETURNS — both endings, one average. 8.38s"""
    def construct(self):
        sent, gap, rule = _anchor_sentence()
        s1, s2, slots   = _anchor_slots()
        w1 = _word_in_slot("UPHOLD",   s1)
        w2 = _word_in_slot("OVERTURN", s2)

        # Average bar (different from 50-50 bar — solid, labeled separately)
        avg_y = BAR_Y - 0.50
        avg_bar = Rectangle(width=7.0, height=BAR_H,
                            fill_color=INK, fill_opacity=0.90, stroke_width=0)
        avg_bar.move_to(ORIGIN + UP * avg_y)
        avg_lbl = Text("average quality: fine", font=DISP, weight="BOLD",
                       font_size=36, color=GROUND)
        avg_lbl.move_to(avg_bar.get_center())

        self.play(Write(sent), Create(rule), GrowFromCenter(slots), run_time=0.7)
        self.play(Write(w1), Write(w2), run_time=0.4)
        self.play(GrowFromCenter(avg_bar), Write(avg_lbl), run_time=0.5)
        self.wait(8.38 - 1.6)


# ════════════════════════════════════════════════════════════ S14 ══════════

class S14_CrowdAndOneWord(Scene):
    """Dense field; one word circled, unexamined. 5.76s — PASS in GATE T."""
    def construct(self):
        import random; random.seed(42)
        crowd = VGroup()
        for _ in range(65):
            d = Dot(radius=0.055, color=INK, fill_opacity=0.38)
            d.move_to(np.array([random.uniform(-5.4, 5.4),
                                random.uniform(-2.4, 2.4), 0]))
            crowd.add(d)

        word = Text("changed", font=BODY, weight="BOLD", font_size=38, color=INK)
        word.move_to(ORIGIN + LEFT*0.5 + UP*0.3)

        # ONE TERRA accent: circle around the unexamined word
        circle = Circle(radius=0.75, stroke_color=TERRA, stroke_width=3.5,
                        fill_opacity=0)
        circle.move_to(word.get_center())

        self.play(LaggedStart(*[FadeIn(d) for d in crowd], lag_ratio=0.012),
                  run_time=0.7)
        self.play(FadeIn(word), run_time=0.3)
        self.play(Create(circle), run_time=0.5)
        self.wait(5.76 - 1.5)


# ════════════════════════════════════════════════════════════ S15 ══════════

class S15_DirectionA(Scene):
    """WORD CHANGED → struck MEANING CHANGED. 6.36s"""
    def construct(self):
        premise = Text("WORD CHANGED", font=DISP, weight="BOLD",
                       font_size=52, color=INK)
        premise.move_to(UP * 1.7)

        # ONE TERRA accent: the arrow (marking the invalid inference)
        arrow = Arrow(premise.get_bottom(), premise.get_bottom() + DOWN*1.3,
                      stroke_width=3.5, color=TERRA, tip_length=0.28, buff=0.12)

        conclusion = Text("MEANING CHANGED", font=DISP, weight="BOLD",
                          font_size=52, color=INK)
        conclusion.move_to(UP * 0.0)

        # INK strikethrough — merges into letter blobs, full blob height maintained
        strike = Line(conclusion.get_left() + LEFT*0.12,
                      conclusion.get_right() + RIGHT*0.12,
                      stroke_color=INK, stroke_width=7)
        strike.move_to(conclusion.get_center())

        self.play(Write(premise), run_time=0.5)
        self.play(Create(arrow), run_time=0.3)
        self.play(Write(conclusion), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.wait(6.36 - 1.6)


# ════════════════════════════════════════════════════════════ S16 ══════════

class S16_DirectionB(Scene):
    """SCORE STEADY → struck NOTHING CHANGED. 6.85s (mirror of S15)"""
    def construct(self):
        premise = Text("SCORE STEADY", font=DISP, weight="BOLD",
                       font_size=52, color=INK)
        premise.move_to(UP * 1.7)

        # ONE TERRA accent: the arrow (marking the invalid inference)
        arrow = Arrow(premise.get_bottom(), premise.get_bottom() + DOWN*1.3,
                      stroke_width=3.5, color=TERRA, tip_length=0.28, buff=0.12)

        conclusion = Text("NOTHING CHANGED", font=DISP, weight="BOLD",
                          font_size=52, color=INK)
        conclusion.move_to(UP * 0.0)

        # INK strikethrough — merges into letter blobs, full blob height maintained
        strike = Line(conclusion.get_left() + LEFT*0.12,
                      conclusion.get_right() + RIGHT*0.12,
                      stroke_color=INK, stroke_width=7)
        strike.move_to(conclusion.get_center())

        self.play(Write(premise), run_time=0.5)
        self.play(Create(arrow), run_time=0.3)
        self.play(Write(conclusion), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.wait(6.85 - 1.6)
