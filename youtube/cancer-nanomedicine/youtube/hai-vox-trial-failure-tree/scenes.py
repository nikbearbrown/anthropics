"""scenes.py — Manim graphics for hai-vox-trial-failure-tree.

Humanitarians palette: ground #F3EBDD / ink #2F2A26 / teal #1F6F5C /
crimson #BF3339 / slate #3E5559 / gold #F5D061.

Editorial flat diagrams — flat rectangles, hairline strokes, serif labels.
No gradients, no shadows, no glows. TEAL = fix / good / diagnosable.
CRIMSON = failure / ambiguity / unattributable.

Render one:
  cd <reel>
  manim -ql --fps 24 scenes.py B04_BinaryEndpoint
Render all:
  python3 render_scenes.py
"""
from manim import *

GROUND  = "#F3EBDD"
INK     = "#2F2A26"
TEAL    = "#1F6F5C"
CRIMSON = "#BF3339"
SLATE_  = "#3E5559"
GOLD    = "#F5D061"

config.background_color = GROUND

SERIF   = "EB Garamond"
DISPLAY = "Montserrat"


def _chip(text, fill, size=28, buff=0.20, width=None):
    """Solid-fill chip: DISPLAY caps, white text."""
    t = Text(text.upper(), font=DISPLAY, color=WHITE,
             font_size=int(size * 0.9), weight="MEDIUM")
    box = SurroundingRectangle(t, buff=buff)
    if width is not None and box.width < width:
        box.stretch_to_fit_width(width)
    box.set_fill(fill, 1).set_stroke(width=0)
    return VGroup(box, t)


def _box(text, stroke=INK, size=30, buff=0.28, width=None, height=None):
    """Serif-labeled outline box on the ground."""
    t = Text(text, font=SERIF, color=INK, font_size=size)
    box = SurroundingRectangle(t, buff=buff)
    if width is not None and box.width < width:
        box.stretch_to_fit_width(width)
    if height is not None and box.height < height:
        box.stretch_to_fit_height(height)
    box.set_fill(GROUND, 1).set_stroke(stroke, 2.0)
    return VGroup(box, t)


def _title(text, size=42):
    return Text(text, font=SERIF, color=INK, font_size=size, weight=BOLD)


def _label(text, size=22, color=INK):
    return Text(text, font=SERIF, color=color, font_size=size, slant=ITALIC)


def _line(a, b, color=INK, width=2.2):
    return Line(a, b, color=color, stroke_width=width)


def _arrow(a, b, color=TEAL, width=5.0, tip=0.22):
    return Arrow(a, b, color=color, stroke_width=width,
                 buff=0.06, tip_length=tip)


class B04_BinaryEndpoint(Scene):
    """One box RESPONSE ENDPOINT → two arms → WORKED / DIDN'T. ~12.5s."""

    def construct(self):
        top = _box("RESPONSE ENDPOINT", stroke=SLATE_, size=34, width=5.4)
        top.move_to(UP * 2.6)
        good = _chip("WORKED", TEAL, size=32, buff=0.30)
        bad  = _chip("DIDN'T", CRIMSON, size=32, buff=0.30)
        good.move_to(LEFT * 3.4 + DOWN * 1.6)
        bad.move_to(RIGHT * 3.4 + DOWN * 1.6)

        arm_l = _line(top[0].get_corner(DL) + RIGHT * 0.8,
                      good[0].get_top(), color=SLATE_)
        arm_r = _line(top[0].get_corner(DR) + LEFT * 0.8,
                      bad[0].get_top(), color=SLATE_)

        subtitle = _label("one bit: yes or no — no mechanism, no cause", size=24)
        subtitle.next_to(top, UP, buff=0.35)

        self.play(FadeIn(subtitle, run_time=0.6))
        self.play(FadeIn(top, run_time=0.8))
        self.play(Create(arm_l), Create(arm_r), run_time=1.4)
        self.play(FadeIn(good, run_time=0.8), FadeIn(bad, run_time=0.8))
        self.wait(8.5)


class B06_ThreeFailures(Scene):
    """CRIMSON NEGATIVE at top → three CRIMSON branch boxes. ~9.6s."""

    def construct(self):
        top = _chip("NEGATIVE RESPONSE", CRIMSON, size=32, buff=0.32)
        top.move_to(UP * 2.6)

        d = _box("DELIVERY\nFAILURE", stroke=CRIMSON, size=28, width=3.0, height=1.6)
        p = _box("PAYLOAD\nFAILURE",  stroke=CRIMSON, size=28, width=3.0, height=1.6)
        b = _box("BIOLOGY\nFAILURE",  stroke=CRIMSON, size=28, width=3.0, height=1.6)
        d.move_to(LEFT * 4.2 + DOWN * 1.6)
        p.move_to(DOWN * 1.6)
        b.move_to(RIGHT * 4.2 + DOWN * 1.6)

        l1 = _line(top[0].get_bottom() + LEFT * 0.4, d[0].get_top(), color=CRIMSON)
        l2 = _line(top[0].get_bottom(),              p[0].get_top(), color=CRIMSON)
        l3 = _line(top[0].get_bottom() + RIGHT * 0.4, b[0].get_top(), color=CRIMSON)

        self.play(FadeIn(top, run_time=0.8))
        self.play(Create(l1), Create(l2), Create(l3), run_time=1.6)
        self.play(FadeIn(d), FadeIn(p), FadeIn(b), run_time=1.4)
        self.wait(5.5)


class _FailureBranchScene(Scene):
    """Base: highlight one branch, show a mini-diagram + FIX arrow."""

    HIGHLIGHT = "DELIVERY"
    DIAG_LABEL = "PARTICLE NEVER ARRIVED"
    FIX_TEXT   = "FIX: REDESIGN THE PARTICLE"
    HOLD_S     = 6.0
    LEFT_BLURB = "particle diverts to liver / spleen"
    LEFT_TARGET_TEXT = "LIVER / SPLEEN"
    RIGHT_TARGET_TEXT = "TUMOR (no signal)"
    LEFT_COLOR  = CRIMSON
    RIGHT_COLOR = CRIMSON

    def construct(self):
        # Header: which branch is being examined
        branch = _chip(f"{self.HIGHLIGHT} FAILURE", CRIMSON, size=28)
        branch.move_to(UP * 3.1)

        # Diagram row
        source = _box("PARTICLE\nINJECTED", stroke=SLATE_, size=24,
                      width=2.6, height=1.6)
        left   = _box(self.LEFT_TARGET_TEXT, stroke=self.LEFT_COLOR,
                      size=24, width=2.8, height=1.4)
        right  = _box(self.RIGHT_TARGET_TEXT, stroke=self.RIGHT_COLOR,
                      size=24, width=2.8, height=1.4)
        source.move_to(LEFT * 5.0 + UP * 0.4)
        left.move_to(UP * 1.4)
        right.move_to(RIGHT * 4.6 + UP * 0.4)

        arr_left  = _arrow(source[0].get_right(), left[0].get_left(),
                           color=self.LEFT_COLOR)
        arr_right = _arrow(source[0].get_right(), right[0].get_left(),
                           color=self.RIGHT_COLOR)

        cap = _label(self.DIAG_LABEL, size=26)
        cap.move_to(DOWN * 1.2)

        # Fix arrow (TEAL)
        fix_arrow = _arrow(LEFT * 1.8 + DOWN * 2.4,
                            RIGHT * 1.8 + DOWN * 2.4, color=TEAL, tip=0.30)
        fix_label = Text(self.FIX_TEXT, font=DISPLAY, color=TEAL,
                         font_size=26, weight="MEDIUM")
        fix_label.next_to(fix_arrow, DOWN, buff=0.20)

        self.play(FadeIn(branch, run_time=0.6))
        self.play(FadeIn(source, run_time=0.7))
        self.play(Create(arr_left), Create(arr_right), run_time=1.2)
        self.play(FadeIn(left), FadeIn(right), run_time=0.8)
        self.play(Write(cap, run_time=0.8))
        self.play(Create(fix_arrow), run_time=0.7)
        self.play(FadeIn(fix_label, run_time=0.5))
        self.wait(self.HOLD_S)


class B07_DeliveryFailure(_FailureBranchScene):
    HIGHLIGHT = "DELIVERY"
    DIAG_LABEL = "PARTICLE NEVER ARRIVED"
    FIX_TEXT   = "FIX: REDESIGN THE PARTICLE"
    LEFT_TARGET_TEXT  = "LIVER / SPLEEN"
    RIGHT_TARGET_TEXT = "TUMOR (no signal)"
    LEFT_COLOR  = CRIMSON
    RIGHT_COLOR = CRIMSON
    HOLD_S = 5.5


class B08_PayloadFailure(_FailureBranchScene):
    HIGHLIGHT = "PAYLOAD"
    DIAG_LABEL = "PAYLOAD RELEASED EARLY"
    FIX_TEXT   = "FIX: REDESIGN THE RELEASE"
    LEFT_TARGET_TEXT  = "CIRCULATION (burst)"
    RIGHT_TARGET_TEXT = "TUMOR (reached)"
    LEFT_COLOR  = CRIMSON
    RIGHT_COLOR = TEAL
    HOLD_S = 7.5


class B09_BiologyFailure(_FailureBranchScene):
    HIGHLIGHT = "BIOLOGY"
    DIAG_LABEL = "TUMOR DID NOT RESPOND"
    FIX_TEXT   = "FIX: TRY A DIFFERENT TARGET"
    LEFT_TARGET_TEXT  = "TUMOR (delivered)"
    RIGHT_TARGET_TEXT = "CELLS ✗"
    LEFT_COLOR  = TEAL
    RIGHT_COLOR = CRIMSON
    HOLD_S = 6.0


class B10_FullTree(Scene):
    """Full failure tree with TEAL fix arrows + a CRIMSON blindfold bar
    labeled RESPONSE ONLY — CANNOT SEE BELOW THIS LINE. ~13.9s."""

    def construct(self):
        # Blindfold bar at very top
        bar = Rectangle(width=13.2, height=0.72,
                        fill_color=CRIMSON, fill_opacity=0.85,
                        stroke_width=0)
        bar.move_to(UP * 3.35)
        bar_txt = Text("RESPONSE ONLY — CANNOT SEE BELOW THIS LINE",
                       font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
        bar_txt.move_to(bar)

        # NEGATIVE node
        neg = _chip("NEGATIVE RESPONSE", CRIMSON, size=26, buff=0.30)
        neg.move_to(UP * 2.05)

        # Three branch boxes
        d = _box("DELIVERY\nFAILURE", stroke=CRIMSON, size=24, width=2.9, height=1.3)
        p = _box("PAYLOAD\nFAILURE",  stroke=CRIMSON, size=24, width=2.9, height=1.3)
        b = _box("BIOLOGY\nFAILURE",  stroke=CRIMSON, size=24, width=2.9, height=1.3)
        d.move_to(LEFT * 4.4 + DOWN * 0.2)
        p.move_to(DOWN * 0.2)
        b.move_to(RIGHT * 4.4 + DOWN * 0.2)

        l1 = _line(neg[0].get_bottom() + LEFT * 0.3,
                   d[0].get_top(), color=CRIMSON)
        l2 = _line(neg[0].get_bottom(), p[0].get_top(), color=CRIMSON)
        l3 = _line(neg[0].get_bottom() + RIGHT * 0.3,
                   b[0].get_top(), color=CRIMSON)

        # Fix arrows + fix labels
        fx1 = _arrow(d[0].get_bottom(),
                     d[0].get_bottom() + DOWN * 0.9, color=TEAL, tip=0.25)
        fx2 = _arrow(p[0].get_bottom(),
                     p[0].get_bottom() + DOWN * 0.9, color=TEAL, tip=0.25)
        fx3 = _arrow(b[0].get_bottom(),
                     b[0].get_bottom() + DOWN * 0.9, color=TEAL, tip=0.25)

        lb1 = Text("FIX THE\nPARTICLE",     font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        lb2 = Text("FIX THE\nRELEASE",      font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        lb3 = Text("A DIFFERENT\nTARGET",   font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        lb1.next_to(fx1, DOWN, buff=0.16)
        lb2.next_to(fx2, DOWN, buff=0.16)
        lb3.next_to(fx3, DOWN, buff=0.16)

        self.play(FadeIn(bar), Write(bar_txt), run_time=0.9)
        self.play(FadeIn(neg), run_time=0.7)
        self.play(Create(l1), Create(l2), Create(l3), run_time=1.2)
        self.play(FadeIn(d), FadeIn(p), FadeIn(b), run_time=1.0)
        self.play(Create(fx1), Create(fx2), Create(fx3), run_time=1.2)
        self.play(FadeIn(lb1), FadeIn(lb2), FadeIn(lb3), run_time=0.8)
        self.wait(7.5)


class B12_TwoPrograms(Scene):
    """Two-column comparison. Illustrative numbers. ~28.8s."""

    def construct(self):
        note = _label("ILLUSTRATIVE — numbers are for structure, not the record",
                      size=20)
        note.move_to(UP * 3.5)

        # Column headers
        a_h = _chip("PROGRAM A", SLATE_, size=26)
        b_h = _chip("PROGRAM B", SLATE_, size=26)
        a_h.move_to(LEFT * 3.6 + UP * 2.6)
        b_h.move_to(RIGHT * 3.6 + UP * 2.6)

        # Divider
        div = _line(UP * 3.0, DOWN * 3.5, color=SLATE_, width=1.2)
        div.set_stroke(opacity=0.4)

        # PROGRAM A: response only, closed
        a_resp = _box("7% RESPONSE", stroke=CRIMSON, size=28,
                      width=3.4, height=1.0)
        a_resp.move_to(LEFT * 3.6 + UP * 1.0)
        a_closed = _chip("CLOSED", CRIMSON, size=30, buff=0.30, width=3.4)
        a_closed.move_to(LEFT * 3.6 + DOWN * 0.4)
        a_note = _label("no mechanism, no next step", size=22)
        a_note.next_to(a_closed, DOWN, buff=0.5)

        # PROGRAM B: tracer cohort → bar chart → diagnose → redesign → 21%
        b_cohort = _box("TRACER COHORT FIRST  (10 pts)",
                        stroke=SLATE_, size=20, width=4.4, height=0.75)
        b_cohort.move_to(RIGHT * 3.6 + UP * 1.6)

        # Tiny bar chart (compact) — bar bases at DOWN * 0.35
        base_y = -0.35
        bar_w = 0.55
        bar_h_liver = 1.0
        bar_h_tumor = 0.10
        liver_bar = Rectangle(width=bar_w, height=bar_h_liver,
                              fill_color=CRIMSON, fill_opacity=1,
                              stroke_width=0)
        tumor_bar = Rectangle(width=bar_w, height=bar_h_tumor,
                              fill_color=TEAL, fill_opacity=1,
                              stroke_width=0)
        # Position bars side-by-side, aligned along their bottom edge
        liver_bar.move_to(RIGHT * 2.6 + UP * (base_y + bar_h_liver / 2))
        tumor_bar.move_to(RIGHT * 4.6 + UP * (base_y + bar_h_tumor / 2))
        liver_lbl = Text("LIVER 75%+", font=DISPLAY, color=INK,
                         font_size=15, weight="MEDIUM")
        tumor_lbl = Text("TUMOR <3%",  font=DISPLAY, color=INK,
                         font_size=15, weight="MEDIUM")
        liver_lbl.next_to(liver_bar, UP, buff=0.08)
        tumor_lbl.next_to(tumor_bar, UP, buff=0.08)

        b_diag = _chip("DELIVERY FAILURE DIAGNOSED", CRIMSON,
                       size=18, buff=0.20, width=4.4)
        b_diag.move_to(RIGHT * 3.6 + DOWN * 1.7)
        b_fix = _chip("REDESIGN PEG", TEAL, size=20, buff=0.20, width=2.6)
        b_fix.move_to(RIGHT * 3.6 + DOWN * 2.5)
        b_out = _chip("21% RESPONSE", TEAL, size=24, buff=0.24, width=3.4)
        b_out.move_to(RIGHT * 3.6 + DOWN * 3.3)

        self.play(FadeIn(note, run_time=0.5))
        self.play(FadeIn(a_h), FadeIn(b_h), Create(div), run_time=1.2)
        # A column
        self.play(FadeIn(a_resp, run_time=0.8))
        self.play(FadeIn(a_closed, run_time=0.7))
        self.play(FadeIn(a_note, run_time=0.5))
        # B column
        self.play(FadeIn(b_cohort, run_time=0.8))
        self.play(GrowFromEdge(liver_bar, DOWN),
                  GrowFromEdge(tumor_bar, DOWN), run_time=1.0)
        self.play(FadeIn(liver_lbl), FadeIn(tumor_lbl), run_time=0.6)
        self.play(FadeIn(b_diag, run_time=0.8))
        self.play(FadeIn(b_fix, run_time=0.7))
        self.play(FadeIn(b_out, run_time=0.9))
        self.wait(18.0)
