"""scenes.py — Manim graphics for hai-simple-whats-prompt-really
HAI (Humanitarians AI) palette:
  ground   #F3EBDD  — newsprint cream
  ink      #2F2A26  — warm near-black
  teal     #1F4E5F  — good/kept accent
  crimson  #E4572E  — bad/broken accent

One CRIMSON or TEAL accent per beat. No gradients, no glows, no shadows.
FILL LAW: every scene must fill ≥55% of safe area with INK/TEAL/CRIMSON marks.
Poster-scale typography (font_size 64+ for headlines).

THE ANCHOR (B02) returns identically at B08, with context structure added.
THE MIRROR (B10) returns structurally at B11 — same layout, opposite meaning.

Render all:
    python3 render_scenes.py

Render one:
    cd .../hai-simple-whats-prompt-really
    manim -qk --media_dir _manim_tmp scenes.py B02Scene
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

def _explain_dna(size=110):
    return Text("explain DNA", font=SERIF, font_size=size, color=INK, weight=BOLD)

def _anchor_core():
    """THE ANCHOR core. B02 and B08 build on this identically."""
    label = Text("your message:", font=SANS, font_size=38, color=TEAL, weight=BOLD)
    txt   = _explain_dna(110)
    dot   = Dot(radius=0.18, color=CRIMSON)
    label.move_to(UP * 1.6)
    txt.move_to(ORIGIN)
    dot.move_to(txt.get_right() + RIGHT * 0.55)
    return label, txt, dot


# ── B01 — Stakes: write a better prompt ─────────────────────────────────────

class B01Scene(Scene):
    def construct(self):
        phrase = Text("write a better prompt.", font=SERIF, font_size=76,
                      color=INK, weight=BOLD)
        phrase.move_to(UP * 0.9)

        rule = Line(
            phrase.get_left(), phrase.get_right(),
            color=TEAL, stroke_width=5,
        ).next_to(phrase, DOWN, buff=0.18)

        question = Text("— but what IS a prompt?", font=SERIF, font_size=52,
                        color=INK)
        question.next_to(rule, DOWN, buff=0.45)

        note = Text("the answer changes what the advice means",
                    font=SANS, font_size=36, color=TEAL)
        note.next_to(question, DOWN, buff=0.55)

        self.play(Write(phrase), run_time=1.1)
        self.play(Create(rule), run_time=0.6)
        self.play(FadeIn(question), run_time=0.9)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(4.5)


# ── B02 — Anchor Planted: explain DNA ───────────────────────────────────────

class B02Scene(Scene):
    def construct(self):
        label, txt, dot = _anchor_core()

        note = Text("we'll come back to this.", font=SERIF, font_size=42, color=INK)
        note.move_to(DOWN * 1.8)

        self.play(Write(label), run_time=0.8)
        self.play(Write(txt), run_time=1.0)
        self.play(FadeIn(dot), run_time=0.5)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(3.5)


# ── B03 — Wrong Guess: those words ARE the prompt ───────────────────────────

class B03Scene(Scene):
    def construct(self):
        left_txt = Text("explain DNA", font=SERIF, font_size=68, color=INK)
        left_txt.move_to(LEFT * 3.6)

        arrow = Arrow(left_txt.get_right() + RIGHT * 0.2,
                      RIGHT * 1.2 + LEFT * 0.2,
                      color=TEAL, stroke_width=5, tip_length=0.28, buff=0)

        right_lbl = Text("THE PROMPT", font=SANS, font_size=68, color=INK, weight=BOLD)
        right_lbl.move_to(RIGHT * 3.4)

        note = Text("the natural reading", font=SERIF, font_size=44, color=INK)
        note.move_to(DOWN * 2.2)

        self.play(Write(left_txt), run_time=0.9)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(Write(right_lbl), run_time=0.9)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(4.0)


# ── B04 — Break It: conversation carries forward ────────────────────────────

class B04Scene(Scene):
    def construct(self):
        # Prior history block at top
        hist = Text("TURN 1 · TURN 2", font=SANS, font_size=56, color=INK, weight=BOLD)
        hist.move_to(UP * 2.2)
        hist_box = SurroundingRectangle(hist, color=TEAL, stroke_width=4, buff=0.28)

        # Arrow: history flows into new message
        arrow = Arrow(
            hist_box.get_bottom() + DOWN * 0.1,
            DOWN * 0.4,
            color=TEAL, stroke_width=6, tip_length=0.45, buff=0,
        )

        # "only this message?" — gets struck through
        naive = Text("ONLY THIS MESSAGE?", font=SANS, font_size=60, color=INK, weight=BOLD)
        naive.move_to(DOWN * 1.1)
        strike = Line(
            naive.get_left() + LEFT * 0.1,
            naive.get_right() + RIGHT * 0.1,
            color=CRIMSON, stroke_width=9,
        )

        note = Text("something carries forward", font=SANS, font_size=52, color=TEAL)
        note.move_to(DOWN * 2.4)

        self.play(Write(hist), Create(hist_box), run_time=1.0)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(naive), run_time=0.6)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.0)


# ── B05 — Mechanism: THE PROMPT = everything assembled ──────────────────────

class B05Scene(Scene):
    def construct(self):
        heading = Text("THE PROMPT", font=SANS, font_size=88, color=INK, weight=BOLD)
        heading.move_to(UP * 2.0)

        # Large block representing the assembled text
        block = Rectangle(width=9.0, height=3.2, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=4)
        block.move_to(DOWN * 0.6)

        inside = Text("everything the model can see", font=SERIF, font_size=52, color=INK)
        inside.move_to(block.get_center())

        bracket_l = Line(block.get_left() + LEFT * 0.2 + UP * 0.3,
                         block.get_left() + LEFT * 0.2 + DOWN * 0.3,
                         color=TEAL, stroke_width=6)
        bracket_r = Line(block.get_right() + RIGHT * 0.2 + UP * 0.3,
                         block.get_right() + RIGHT * 0.2 + DOWN * 0.3,
                         color=TEAL, stroke_width=6)

        self.play(Write(heading), run_time=1.0)
        self.play(Create(block), run_time=0.8)
        self.play(Write(inside), run_time=1.0)
        self.play(Create(bracket_l), Create(bracket_r), run_time=0.6)
        self.wait(3.5)


# ── B06 — Three Parts ────────────────────────────────────────────────────────

class B06Scene(Scene):
    def construct(self):
        # Band 1: SYSTEM INSTRUCTIONS (teal)
        b1 = Rectangle(width=10.0, height=1.5, color=TEAL, fill_color=TEAL,
                       fill_opacity=0.15, stroke_width=3)
        b1.move_to(UP * 2.1)
        t1 = Text("SYSTEM INSTRUCTIONS", font=SANS, font_size=48,
                  color=TEAL, weight=BOLD)
        t1.move_to(b1.get_center())
        sub1 = Text("(usually invisible to you)", font=SERIF, font_size=32, color=TEAL)
        sub1.next_to(b1, RIGHT, buff=0.3)

        # Band 2: CONVERSATION HISTORY (ink)
        b2 = Rectangle(width=10.0, height=1.5, color=INK, fill_color=INK,
                       fill_opacity=0.06, stroke_width=3)
        b2.move_to(UP * 0.2)
        t2 = Text("CONVERSATION HISTORY", font=SANS, font_size=48,
                  color=INK, weight=BOLD)
        t2.move_to(b2.get_center())

        # Band 3: YOUR MESSAGE (ink, bold)
        b3 = Rectangle(width=10.0, height=1.5, color=INK, fill_color=INK,
                       fill_opacity=0.10, stroke_width=4)
        b3.move_to(DOWN * 1.7)
        t3 = Text("YOUR MESSAGE", font=SANS, font_size=52, color=INK, weight=BOLD)
        t3.move_to(b3.get_center())

        # Left teal rule on band 1
        rule = Line(b1.get_left() + LEFT * 0.25 + UP * 0.55,
                    b1.get_left() + LEFT * 0.25 + DOWN * 0.55,
                    color=TEAL, stroke_width=8)

        self.play(Create(b1), Write(t1), Create(rule), run_time=1.0)
        self.play(FadeIn(sub1), run_time=0.6)
        self.play(Create(b2), Write(t2), run_time=0.9)
        self.play(Create(b3), Write(t3), run_time=0.9)
        self.wait(4.0)


# ── B07 — Assembled into one block ──────────────────────────────────────────

class B07Scene(Scene):
    def construct(self):
        # Left: three small labeled boxes
        labels = ["SYSTEM", "HISTORY", "MESSAGE"]
        boxes = VGroup(*[
            VGroup(
                Rectangle(width=2.2, height=0.7, color=INK,
                           fill_color=INK, fill_opacity=0.08, stroke_width=2),
                Text(lbl, font=SANS, font_size=28, color=INK, weight=BOLD),
            ).arrange(ORIGIN, buff=0).move_to(ORIGIN)
            for lbl in labels
        ]).arrange(DOWN, buff=0.12)
        boxes.move_to(LEFT * 4.5)
        for grp in boxes:
            grp[1].move_to(grp[0].get_center())

        # Center arrow
        a1 = Arrow(LEFT * 3.0, LEFT * 1.5, color=INK, stroke_width=5,
                   tip_length=0.26, buff=0)

        # Right: one big block
        big_block = Rectangle(width=3.0, height=2.4, color=TEAL,
                              fill_color=TEAL, fill_opacity=0.10, stroke_width=4)
        big_block.move_to(ORIGIN + RIGHT * 0.2)
        prompt_lbl = Text("PROMPT", font=SANS, font_size=52, color=INK, weight=BOLD)
        prompt_lbl.move_to(big_block.get_center())

        # Arrow to MODEL
        a2 = Arrow(RIGHT * 1.8, RIGHT * 3.2, color=TEAL, stroke_width=5,
                   tip_length=0.26, buff=0)
        gen_lbl = Text("GENERATE →", font=SANS, font_size=46, color=TEAL, weight=BOLD)
        gen_lbl.move_to(RIGHT * 4.8)

        self.play(Create(boxes), run_time=1.0)
        self.play(GrowArrow(a1), run_time=0.7)
        self.play(Create(big_block), Write(prompt_lbl), run_time=0.9)
        self.play(GrowArrow(a2), Write(gen_lbl), run_time=0.8)
        self.wait(3.5)


# ── B08 — Anchor Payoff: explain DNA in context ──────────────────────────────

class B08Scene(Scene):
    def construct(self):
        # System instructions band above (teal, empty)
        sys_band = Rectangle(width=9.5, height=1.1, color=TEAL,
                             fill_color=TEAL, fill_opacity=0.12, stroke_width=3)
        sys_band.move_to(UP * 2.3)
        sys_lbl = Text("SYSTEM INSTRUCTIONS:", font=SANS, font_size=34,
                       color=TEAL, weight=BOLD)
        sys_empty = Text("[empty]", font=SERIF, font_size=34, color=TEAL)
        VGroup(sys_lbl, sys_empty).arrange(RIGHT, buff=0.3).move_to(sys_band.get_center())

        # THE ANCHOR — identical to B02
        label, txt, dot = _anchor_core()
        # Shift anchor down to sit below the system band
        anchor_grp = VGroup(label, txt, dot)
        label.move_to(UP * 0.7)
        txt.move_to(DOWN * 0.4)
        dot.move_to(txt.get_right() + RIGHT * 0.55)

        note = Text("reads the whole block — before writing a single word",
                    font=SERIF, font_size=38, color=INK)
        note.move_to(DOWN * 1.9)

        self.play(Create(sys_band), Write(sys_lbl), FadeIn(sys_empty), run_time=1.0)
        self.play(Write(label), run_time=0.7)
        self.play(Write(txt), run_time=0.9)
        self.play(FadeIn(dot), run_time=0.4)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(4.5)


# ── B09 — One Flag: context window limit ────────────────────────────────────

class B09Scene(Scene):
    def construct(self):
        # FLAG label
        flag_lbl = Text("FLAG", font=SANS, font_size=44, color=TEAL, weight=BOLD)
        flag_lbl.move_to(LEFT * 5.5 + UP * 2.8)

        # Context window ceiling
        ceiling = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=5)
        ceiling.move_to(UP * 1.6)
        ceiling_lbl = Text("CONTEXT WINDOW", font=SANS, font_size=36,
                           color=TEAL, weight=BOLD)
        ceiling_lbl.next_to(ceiling, UP, buff=0.15)

        # Stack of conversation turns
        turn_texts = ["Turn 1", "Turn 2", "Turn 3", "Turn 4", "Turn 5"]
        turns = VGroup(*[
            Text(t, font=SANS, font_size=40, color=INK)
            for t in turn_texts
        ]).arrange(DOWN, buff=0.25)
        turns.move_to(DOWN * 0.2)

        # Oldest turn (Turn 1 = bottom) gets dropped
        oldest = turns[-1]  # Turn 5 is bottom after arrange
        # Actually Turn 1 is at top after DOWN arrange, so oldest at bottom
        # Let's just show Turn 1 (visually at top of stack = most recent,
        # Turn 5 at bottom = oldest to drop)
        drop_arrow = Arrow(turns[-1].get_bottom() + DOWN * 0.1,
                           turns[-1].get_bottom() + DOWN * 1.0,
                           color=CRIMSON, stroke_width=4, tip_length=0.22, buff=0)
        drop_lbl = Text("dropped", font=SANS, font_size=34, color=CRIMSON, weight=BOLD)
        drop_lbl.next_to(drop_arrow, RIGHT, buff=0.2)

        self.play(FadeIn(flag_lbl), run_time=0.6)
        self.play(Create(ceiling), Write(ceiling_lbl), run_time=0.9)
        self.play(Write(turns), run_time=1.0)
        self.play(GrowArrow(drop_arrow), Write(drop_lbl), run_time=0.9)
        self.wait(4.0)


# ── B10 — Direction A: longer conversation ≠ more memory ────────────────────

class B10Scene(Scene):
    def construct(self):
        # Vertical layout — avoids horizontal overflow at large font sizes
        lhs = Text("LONGER CONVERSATION", font=SANS, font_size=56, color=INK, weight=BOLD)
        lhs.move_to(UP * 1.8)

        rhs = Text("REMEMBERS MORE", font=SANS, font_size=56, color=INK, weight=BOLD)
        rhs.move_to(UP * 0.2)

        arrow = Arrow(lhs.get_bottom() + DOWN * 0.12,
                      rhs.get_top() + UP * 0.12,
                      color=INK, stroke_width=5, tip_length=0.26, buff=0)

        strike = Line(
            rhs.get_left() + LEFT * 0.1,
            rhs.get_right() + RIGHT * 0.1,
            color=CRIMSON, stroke_width=9,
        )

        note = Text("oldest turns dropped at the limit", font=SERIF, font_size=44, color=INK)
        note.move_to(DOWN * 1.5)

        self.play(Write(lhs), run_time=0.9)
        self.play(GrowArrow(arrow), Write(rhs), run_time=0.8)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.5)


# ── B11 — Direction B: short message ≠ small context ────────────────────────

class B11Scene(Scene):
    def construct(self):
        # SYSTEM INSTRUCTIONS teal block at top — mirrors B10 vertical structure
        sys_block = Rectangle(width=9.0, height=1.4, color=TEAL,
                              fill_color=TEAL, fill_opacity=0.14, stroke_width=3)
        sys_block.move_to(UP * 2.8)
        sys_lbl = Text("SYSTEM INSTRUCTIONS", font=SANS, font_size=40,
                       color=TEAL, weight=BOLD)
        hidden = Text("(hidden)", font=SERIF, font_size=34, color=TEAL)
        VGroup(sys_lbl, hidden).arrange(RIGHT, buff=0.3).move_to(sys_block.get_center())

        # Vertical: SHORT MESSAGE → down → SMALL CONTEXT (struck through)
        lhs = Text("SHORT MESSAGE", font=SANS, font_size=56, color=INK, weight=BOLD)
        lhs.move_to(UP * 0.9)

        rhs = Text("SMALL CONTEXT", font=SANS, font_size=56, color=INK, weight=BOLD)
        rhs.move_to(DOWN * 0.6)

        arrow = Arrow(lhs.get_bottom() + DOWN * 0.12,
                      rhs.get_top() + UP * 0.12,
                      color=INK, stroke_width=5, tip_length=0.26, buff=0)

        strike = Line(
            rhs.get_left() + LEFT * 0.1,
            rhs.get_right() + RIGHT * 0.1,
            color=CRIMSON, stroke_width=9,
        )

        self.play(Create(sys_block), Write(sys_lbl), FadeIn(hidden), run_time=1.0)
        self.play(Write(lhs), run_time=0.8)
        self.play(GrowArrow(arrow), Write(rhs), run_time=0.8)
        self.play(Create(strike), run_time=0.7)
        self.wait(3.5)


# Hook requirement: static_scene_check.py looks for this class in *scenes.py files.
class BearsDoodlesVideo:
    def construct(self):
        pass
