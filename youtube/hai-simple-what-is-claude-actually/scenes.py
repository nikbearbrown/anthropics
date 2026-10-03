"""scenes.py — Manim graphics for hai-simple-what-is-claude-actually
HAI (Humanitarians AI) palette:
  ground   #F3EBDD  — newsprint cream
  ink      #2F2A26  — warm near-black
  teal     #1F4E5F  — good/kept accent
  crimson  #E4572E  — bad/broken accent

One CRIMSON or TEAL accent per beat. No gradients, no glows, no shadows.
FILL LAW: every scene must fill ≥55% of safe area with INK/TEAL/CRIMSON marks.
Poster-scale typography (font_size 64+ for headlines).

THE ANCHOR (B03) returns identically at B09, with training examples added.
THE MIRROR (B10) returns structurally at B11 — same layout, opposite meaning.

Render all:
    python3 render_scenes.py

Render one:
    cd .../hai-simple-what-is-claude-actually
    manim -qh --fps 24 -r 1920,1080 scenes.py B03Scene
"""
from manim import *
import numpy as np

GROUND  = "#F3EBDD"
INK     = "#2F2A26"
TEAL    = "#1F4E5F"
CRIMSON = "#E4572E"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"

# Title-safe constants (Manim frame: 14.222 × 8.0 units)
SAFE_W = 12.4
SAFE_H = 6.6


# ── Shared helpers ──────────────────────────────────────────────────────────

def _paris(size=130):
    return Text("PARIS", font=SERIF, font_size=size, color=INK, weight=BOLD)

def _anchor_group():
    """THE ANCHOR composition. B03 and B09 call this identically.
    Returns (q_text, arrow, paris_text).
    """
    q = Text("capital of France?", font=SERIF, font_size=60, color=INK)
    q.move_to(LEFT * 3.5)

    paris = _paris(120)
    paris.move_to(RIGHT * 3.2)

    # Dotted arrow (dashed)
    arrow = DashedLine(
        start=q.get_right() + RIGHT * 0.3,
        end=paris.get_left() + LEFT * 0.3,
        color=INK, stroke_width=4, dash_length=0.18,
    )
    # One crimson dot on the arrowhead
    dot = Dot(point=paris.get_left() + LEFT * 0.35, color=CRIMSON, radius=0.10)

    return q, arrow, dot, paris


# ── B01 — Stakes: You use it. But what is it? ───────────────────────────────

class B01Scene(Scene):
    def construct(self):
        # PROMPT → ? (what is it, really?)
        prompt_lbl = Text("PROMPT", font=SANS, font_size=56, color=INK, weight=BOLD)
        arrow = Arrow(LEFT * 1.2, RIGHT * 1.2, color=INK, stroke_width=5,
                      tip_length=0.28, buff=0)
        resp_lbl = Text("RESPONSE", font=SANS, font_size=56, color=INK, weight=BOLD)

        group = VGroup(prompt_lbl, arrow, resp_lbl).arrange(RIGHT, buff=0.6)
        group.move_to(ORIGIN + DOWN * 0.4)

        question = Text("?", font=SERIF, font_size=240, color=CRIMSON)
        question.move_to(ORIGIN + UP * 1.5)

        self.play(Write(prompt_lbl), run_time=1.0)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(Write(resp_lbl), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(question, shift=DOWN * 0.4), run_time=0.9)
        self.wait(3.5)


# ── B02 — Wrong Guess: SEARCH ENGINE ────────────────────────────────────────

class B02Scene(Scene):
    def construct(self):
        heading = Text("SEARCH ENGINE", font=SANS, font_size=88, color=INK, weight=BOLD)
        heading.move_to(UP * 1.8)

        # Flow: QUERY → INDEX → ANSWER
        q_box  = Text("QUERY",  font=SANS, font_size=52, color=INK)
        idx_box = Text("INDEX", font=SANS, font_size=52, color=TEAL)
        ans_box = Text("ANSWER", font=SANS, font_size=52, color=INK)

        a1 = Arrow(RIGHT * 0.1, RIGHT * 0.1, color=INK, stroke_width=4,
                   tip_length=0.22, buff=0)
        a2 = Arrow(RIGHT * 0.1, RIGHT * 0.1, color=INK, stroke_width=4,
                   tip_length=0.22, buff=0)

        flow = VGroup(q_box, a1, idx_box, a2, ans_box).arrange(RIGHT, buff=0.55)
        flow.move_to(DOWN * 0.7)

        note = Text("the natural reading", font=SERIF, font_size=44, color=INK,
                    slant=ITALIC)
        note.move_to(DOWN * 2.4)

        self.play(Write(heading), run_time=1.2)
        self.play(
            Write(q_box), GrowArrow(a1), Write(idx_box),
            GrowArrow(a2), Write(ans_box),
            run_time=1.8
        )
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.5)


# ── B03 — Anchor Planted: capital of France? → PARIS ────────────────────────

class B03Scene(Scene):
    def construct(self):
        q, arrow, dot, paris = _anchor_group()
        label = Text("that feels like retrieval", font=SERIF, font_size=44, color=INK,
                     slant=ITALIC)
        label.move_to(DOWN * 2.2)

        self.play(Write(q), run_time=1.0)
        self.play(Create(arrow), FadeIn(dot), run_time=0.9)
        self.play(Write(paris), run_time=0.9)
        self.play(FadeIn(label), run_time=0.8)
        self.wait(4.0)


# ── B04 — Break It: No index ────────────────────────────────────────────────

class B04Scene(Scene):
    def construct(self):
        # Three phrasings on the left
        p1 = Text("capital of France?",      font=SERIF, font_size=44, color=INK)
        p2 = Text("France's capital city?",  font=SERIF, font_size=44, color=INK)
        p3 = Text("where is the Eiffel Tower?", font=SERIF, font_size=44, color=INK)
        phrases = VGroup(p1, p2, p3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        phrases.move_to(LEFT * 3.2 + DOWN * 0.1)

        paris = _paris(100)
        paris.move_to(RIGHT * 3.8)

        # Fan lines converge to a single point, then one arrow to PARIS.
        # Avoids arrow-start blobs overlapping phrase text edges.
        conv = LEFT * 1.0 + DOWN * 0.1
        fan_lines = VGroup(*[
            Line(ph.get_right() + RIGHT * 0.2, conv,
                 color=INK, stroke_width=3)
            for ph in phrases
        ])
        main_arrow = Arrow(conv, paris.get_left() + LEFT * 0.2,
                           color=INK, stroke_width=4, tip_length=0.24, buff=0)

        # INDEX box that gets struck through
        idx_box = Text("INDEX", font=SANS, font_size=68, color=INK, weight=BOLD)
        idx_box.move_to(ORIGIN + UP * 2.2)

        strike = Line(
            idx_box.get_left() + LEFT * 0.1,
            idx_box.get_right() + RIGHT * 0.1,
            color=CRIMSON, stroke_width=8,
        )
        no_idx = Text("No index", font=SANS, font_size=48, color=CRIMSON, weight=BOLD)
        no_idx.move_to(ORIGIN + UP * 2.2 + DOWN * 0.95)

        self.play(Write(phrases), run_time=1.2)
        self.play(Create(fan_lines), GrowArrow(main_arrow),
                  Write(paris), run_time=1.2)
        self.play(FadeIn(idx_box), run_time=0.7)
        self.wait(0.3)
        self.play(Create(strike), Write(no_idx), run_time=0.9)
        self.wait(3.5)


# ── B05 — Mechanism 1: Text corpus → Neural network → Next word ─────────────

class B05Scene(Scene):
    def construct(self):
        # Left: corpus block of dots
        corpus_lbl = Text("HUGE TEXT CORPUS", font=SANS, font_size=52, color=INK,
                          weight=BOLD)
        corpus_lbl.move_to(LEFT * 4.5 + UP * 1.6)

        dots = VGroup(*[
            Dot(point=LEFT * 4.5 + RIGHT * (i % 7) * 0.32 + DOWN * (i // 7) * 0.32
                + DOWN * 0.5 + LEFT * 1.0, color=INK, radius=0.06)
            for i in range(35)
        ])

        # Centre: neural network (3 nodes triangle)
        n1 = Dot(point=ORIGIN + UP * 0.8,   color=INK, radius=0.18)
        n2 = Dot(point=ORIGIN + DOWN * 0.5 + LEFT * 0.7,  color=INK, radius=0.18)
        n3 = Dot(point=ORIGIN + DOWN * 0.5 + RIGHT * 0.7, color=INK, radius=0.18)
        edges = VGroup(
            Line(n1.get_center(), n2.get_center(), color=INK, stroke_width=3),
            Line(n1.get_center(), n3.get_center(), color=INK, stroke_width=3),
            Line(n2.get_center(), n3.get_center(), color=INK, stroke_width=3),
        )
        net_label = Text("NEURAL\nNETWORK", font=SANS, font_size=36, color=INK,
                         weight=BOLD).move_to(ORIGIN + DOWN * 1.5)

        # Right: arrow → NEXT WORD?
        teal_arrow = Arrow(RIGHT * 1.4, RIGHT * 3.5, color=TEAL, stroke_width=6,
                           tip_length=0.30, buff=0)
        next_lbl = Text("NEXT\nWORD?", font=SANS, font_size=64, color=TEAL,
                        weight=BOLD).move_to(RIGHT * 4.8 + UP * 0.1)

        self.play(FadeIn(corpus_lbl), Create(dots), run_time=1.1)
        self.play(
            Create(VGroup(n1, n2, n3, *edges)),
            FadeIn(net_label),
            run_time=1.1
        )
        self.play(GrowArrow(teal_arrow), Write(next_lbl), run_time=1.0)
        self.wait(4.0)


# ── B06 — Mechanism 2: Training step 2 shapes predictions ───────────────────

class B06Scene(Scene):
    def construct(self):
        # Left column: raw predictions
        pred_lbl = Text("PREDICTIONS", font=SANS, font_size=52, color=INK, weight=BOLD)
        pred_lbl.move_to(LEFT * 4.0 + UP * 1.8)

        words_left = VGroup(*[
            Text(w, font=SERIF, font_size=46, color=INK)
            for w in ["respond", "answer", "explain", "describe", "say"]
        ]).arrange(DOWN, buff=0.18).move_to(LEFT * 4.0 + DOWN * 0.4)

        # Centre: teal arrow
        step_arrow = Arrow(LEFT * 1.6, RIGHT * 1.6, color=TEAL, stroke_width=6,
                           tip_length=0.28, buff=0)
        step_lbl = Text("TRAINING STEP 2", font=SANS, font_size=38, color=TEAL,
                        weight=BOLD).next_to(step_arrow, UP, buff=0.15)

        # Right column: shaped predictions
        shaped_lbl = Text("SHAPED", font=SANS, font_size=52, color=INK, weight=BOLD)
        shaped_lbl.move_to(RIGHT * 4.0 + UP * 1.8)

        key_words = ["helpful", "honest", "harmless"]
        words_right = VGroup(*[
            Text(w, font=SERIF, font_size=46,
                 color=TEAL if w in key_words else INK)
            for w in ["respond", "helpful", "honest", "harmless", "say"]
        ]).arrange(DOWN, buff=0.18).move_to(RIGHT * 4.0 + DOWN * 0.4)

        self.play(FadeIn(pred_lbl), Write(words_left), run_time=1.2)
        self.play(GrowArrow(step_arrow), FadeIn(step_lbl), run_time=0.9)
        self.play(FadeIn(shaped_lbl), Write(words_right), run_time=1.2)
        self.wait(4.5)


# ── B07 — Mechanism 3: Generates, not retrieves ──────────────────────────────

class B07Scene(Scene):
    def construct(self):
        # Input box
        in_lbl = Text("YOUR\nMESSAGE", font=SANS, font_size=52, color=INK, weight=BOLD)
        in_lbl.move_to(LEFT * 4.5)

        # RETRIEVES struck through — moved up to clear out_arrow below
        retrieves = Text("RETRIEVES", font=SANS, font_size=80, color=INK, weight=BOLD)
        retrieves.move_to(ORIGIN + UP * 1.0)
        strike = Line(
            retrieves.get_left() + LEFT * 0.05,
            retrieves.get_right() + RIGHT * 0.05,
            color=CRIMSON, stroke_width=9,
        )

        # GENERATES below
        generates = Text("GENERATES", font=SANS, font_size=80, color=INK, weight=BOLD)
        generates.move_to(ORIGIN + DOWN * 0.4)

        # Arrow and RESPONSE pushed far right so they don't share x-range with RETRIEVES
        out_arrow = Arrow(RIGHT * 2.6, RIGHT * 4.6, color=INK, stroke_width=5,
                          tip_length=0.26, buff=0)
        out_arrow.move_to(RIGHT * 3.6 + DOWN * 0.4)
        out_lbl = Text("RESPONSE", font=SANS, font_size=52, color=INK, weight=BOLD)
        out_lbl.move_to(RIGHT * 5.6 + DOWN * 0.4)

        self.play(FadeIn(in_lbl), run_time=0.8)
        self.play(Write(retrieves), run_time=0.8)
        self.play(Create(strike), run_time=0.6)
        self.play(Write(generates), run_time=0.8)
        self.play(GrowArrow(out_arrow), Write(out_lbl), run_time=0.9)
        self.wait(4.0)


# ── B08 — One Flag: Cutoff timeline ─────────────────────────────────────────

class B08Scene(Scene):
    def construct(self):
        # Timeline base
        timeline = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=4)
        timeline.move_to(DOWN * 0.4)

        # Left: TRAINING DATA
        train_lbl = Text("TRAINING DATA", font=SANS, font_size=52, color=INK,
                         weight=BOLD)
        train_lbl.move_to(LEFT * 3.8 + UP * 0.5)

        # Crimson cutoff line
        cutoff = Line(ORIGIN + DOWN * 1.2, ORIGIN + UP * 1.5,
                      color=CRIMSON, stroke_width=7)
        cutoff.move_to(ORIGIN + DOWN * 0.4)

        # Right: TODAY
        today_lbl = Text("TODAY", font=SANS, font_size=52, color=INK)
        today_lbl.move_to(RIGHT * 3.8 + UP * 0.5)

        # Below: "No live web access"
        no_web = Text("No live web access", font=SANS, font_size=48, color=CRIMSON,
                      weight=BOLD)
        no_web.move_to(DOWN * 1.9)

        # FLAG pill
        flag_bg = RoundedRectangle(width=2.4, height=0.65, corner_radius=0.32,
                                   fill_color=CRIMSON, fill_opacity=1.0,
                                   stroke_width=0)
        flag_txt = Text("FLAG", font=SANS, font_size=38, color=GROUND, weight=BOLD)
        flag_pill = VGroup(flag_bg, flag_txt).arrange(ORIGIN)
        flag_pill.move_to(RIGHT * 4.8 + UP * 2.4)

        self.play(Create(timeline), run_time=0.8)
        self.play(FadeIn(train_lbl), FadeIn(today_lbl), run_time=0.9)
        self.play(Create(cutoff), run_time=0.7)
        self.play(FadeIn(no_web), run_time=0.8)
        self.play(FadeIn(flag_pill), run_time=0.7)
        self.wait(5.5)


# ── B09 — Anchor Payoff: THE ANCHOR RETURNS ─────────────────────────────────

class B09Scene(Scene):
    def construct(self):
        q, arrow, dot, paris = _anchor_group()

        # Training examples beneath
        ex1 = Text("\"…the capital of France is Paris…\"", font=SERIF,
                   font_size=38, color=INK)
        ex2 = Text("\"…Paris, capital of France…\"",       font=SERIF,
                   font_size=38, color=INK)
        examples = VGroup(ex1, ex2).arrange(DOWN, buff=0.22)
        examples.move_to(DOWN * 2.2)

        # IN THE WEIGHTS label
        weights_lbl = Text("IN THE WEIGHTS", font=SANS, font_size=48, color=TEAL,
                           weight=BOLD)
        weights_lbl.move_to(RIGHT * 3.2 + DOWN * 1.0)

        # Animate: anchor appears (same as B03), then additions
        self.play(Write(q), run_time=1.0)
        self.play(Create(arrow), FadeIn(dot), run_time=0.9)
        self.play(Write(paris), run_time=0.9)
        self.wait(0.3)
        self.play(FadeIn(examples), run_time=1.0)
        self.play(Write(weights_lbl), run_time=0.9)
        self.wait(3.5)


# ── B10 — Both Directions A: PREDICT NEXT WORD → branches ───────────────────

class B10Scene(Scene):
    def construct(self):
        # No bounding box — text label only (box causes blob-containment §8.6b)
        center_lbl = Text("PREDICT NEXT WORD", font=SANS, font_size=64, color=INK,
                          weight=BOLD)
        center_lbl.move_to(ORIGIN + UP * 1.2)

        # Underline instead of box to separate the label from branch arrows
        underline = Line(
            center_lbl.get_left() + DOWN * 0.08,
            center_lbl.get_right() + DOWN * 0.08,
            color=INK, stroke_width=4,
        )

        # Three branch targets — moved down to give clear separation from label
        code_lbl     = Text("CODE",       font=SANS, font_size=60, color=TEAL, weight=BOLD)
        trans_lbl    = Text("TRANSLATE",  font=SANS, font_size=60, color=TEAL, weight=BOLD)
        summ_lbl     = Text("SUMMARIZE",  font=SANS, font_size=60, color=TEAL, weight=BOLD)

        code_lbl.move_to(LEFT  * 4.5 + DOWN * 1.3)
        trans_lbl.move_to(ORIGIN + DOWN * 2.0)
        summ_lbl.move_to(RIGHT * 4.5 + DOWN * 1.3)

        a1 = Arrow(center_lbl.get_bottom() + LEFT  * 1.8,
                   code_lbl.get_top()  + UP * 0.15,
                   color=TEAL, stroke_width=5, tip_length=0.24, buff=0.1)
        a2 = Arrow(center_lbl.get_bottom(),
                   trans_lbl.get_top() + UP * 0.15,
                   color=TEAL, stroke_width=5, tip_length=0.24, buff=0.1)
        a3 = Arrow(center_lbl.get_bottom() + RIGHT * 1.8,
                   summ_lbl.get_top()  + UP * 0.15,
                   color=TEAL, stroke_width=5, tip_length=0.24, buff=0.1)

        self.play(FadeIn(center_lbl), Create(underline), run_time=1.0)
        self.play(
            LaggedStart(
                GrowArrow(a1), Write(code_lbl),
                GrowArrow(a2), Write(trans_lbl),
                GrowArrow(a3), Write(summ_lbl),
                lag_ratio=0.18,
            ),
            run_time=2.0
        )
        self.wait(4.0)


# ── B11 — Both Directions B: PLAUSIBLE ≠ VERIFIED ───────────────────────────

class B11Scene(Scene):
    def construct(self):
        # Left: PLAUSIBLE
        plausible = Text("PLAUSIBLE", font=SANS, font_size=76, color=INK, weight=BOLD)
        plausible.move_to(LEFT * 4.0 + UP * 0.5)

        # Centre: ≠ in crimson
        neq = Text("≠", font=SERIF, font_size=200, color=CRIMSON)
        neq.move_to(ORIGIN + UP * 0.3)

        # Right: VERIFIED in TEAL, struck through
        verified = Text("VERIFIED", font=SANS, font_size=76, color=TEAL, weight=BOLD)
        verified.move_to(RIGHT * 4.0 + UP * 0.5)
        v_strike = Line(
            verified.get_left() + LEFT * 0.05,
            verified.get_right() + RIGHT * 0.05,
            color=CRIMSON, stroke_width=8,
        )

        # Below: confident wrong answers
        subtext = Text("confident wrong answers", font=SERIF, font_size=48, color=INK,
                       slant=ITALIC)
        subtext.move_to(DOWN * 2.3)

        self.play(Write(plausible), run_time=0.9)
        self.play(Write(neq), run_time=0.7)
        self.play(Write(verified), run_time=0.9)
        self.play(Create(v_strike), run_time=0.6)
        self.play(FadeIn(subtext), run_time=0.8)
        self.wait(4.0)


# ── Required stub ────────────────────────────────────────────────────────────

class BearsDoodlesVideo:
    def construct(self):
        pass
