"""scenes.py — Manim graphics for claude-liam-simple-watermark
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
One terracotta accent per beat. No gradients, no glows, no shadows.

Render all:
  python3 render_scenes.py

Render one:
  cd anthropics/youtube/claude-liam-simple-watermark
  manim -qh --fps 24 -r 1920,1080 scenes.py S01Scene
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"

# ── ANCHOR paragraph — shared by S03 and S10 ────────────────────────────────
# All text INK (passes contrast §8.3). TERRA underlines mark the changed words.
def _build_anchor_paragraph():
    """Two-line anchor VGroup. Both S03 and S10 call this identically.
    Returns (para, highlights) — highlights is a VGroup of TERRA underlines.

    Single Text() per line so Pango includes natural inter-word advance widths
    (buff=0 on separate span Text() objects omits trailing-space advance, causing
    words to fuse visually: 'She hadfinishedthe report,').  Glyph index slicing
    locates each target word for a full-width TERRA underline.
    """
    line1 = Text("She had finished the report,",
                 font=SERIF, font_size=42, color=INK)
    line2 = Text("and the results were promising.",
                 font=SERIF, font_size=42, color=INK)
    para = VGroup(line1, line2).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
    para.scale_to_fit_width(10.0)   # enforce safe-zone: 10 units ≈ 1350px

    # Glyph indices confirmed via submobject position debug (fi-ligature = 1 glyph):
    # line1: "She"=0:3, "had"=3:6, "finished"=6:13, "the"=13:16, "report,"=16:23
    # line2: "and"=0:3, "the"=3:6, "results"=6:13, "were"=13:17, "promising."=17:27
    hl1 = VGroup(*line1[6:13])   # "finished"
    hl2 = VGroup(*line2[13:17])  # "were"

    def ul(part):
        # Underline spans the full rendered width of the target word.
        return Line(
            [part.get_left()[0],  part.get_bottom()[1] - 0.09, 0],
            [part.get_right()[0], part.get_bottom()[1] - 0.09, 0],
            color=TERRA, stroke_width=4,
        )
    highlights = VGroup(ul(hl1), ul(hl2))
    return para, highlights


def _anchor_box(para):
    """INK hairline bracket — TERRA underlines are the accent, not this box."""
    rect = SurroundingRectangle(
        para, buff=0.3,
        color=INK, stroke_width=2,
        corner_radius=0.12, fill_opacity=0
    )
    return rect


# ── S01 — text block, mark implied not shown ───────────────────────────────
# Duration 4.25s
class S01Scene(Scene):
    def construct(self):
        para = Text(
            "Future Claude models leave an invisible\nmark in the text they write.",
            font=SERIF, font_size=58, color=INK, line_spacing=1.35,
        ).move_to(ORIGIN)
        self.add(para)
        self.wait(0.75)

        # Terracotta underline sweeps left to right beneath the text
        left  = para.get_bottom() + LEFT  * (para.width / 2) + DOWN * 0.18
        right = para.get_bottom() + RIGHT * (para.width / 2) + DOWN * 0.18
        ul = Line(left, right, color=TERRA, stroke_width=6)
        self.play(Create(ul), run_time=1.1)
        self.wait(0.45)
        self.play(FadeOut(ul, run_time=0.9))
        self.wait(1.05)   # ≈ 4.25s total


# ── S02 — three things crossed off ──────────────────────────────────────────
# Duration 5.72s
class S02Scene(Scene):
    def construct(self):
        labels = ["HIDDEN CHARACTERS", "EXTRA COST", "YOUR IDENTITY"]
        chips = []
        for lbl in labels:
            rect = RoundedRectangle(
                corner_radius=0.28, width=6.5, height=1.1,
                fill_color=GROUND, fill_opacity=1,
                stroke_color=INK, stroke_width=2,
            )
            txt = Text(lbl, font=SERIF, font_size=48, color=INK, weight=BOLD)
            txt.move_to(rect)
            chips.append(VGroup(rect, txt))

        # Vertical stack — horizontal row (3×4.8+buffs=15.5) exceeds 14.22 frame width
        row = VGroup(*chips).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        self.play(FadeIn(row), run_time=0.4)
        self.wait(0.25)

        for c in chips:
            strike = Line(
                c.get_left() + LEFT * 0.06,
                c.get_right() + RIGHT * 0.06,
                color=TERRA, stroke_width=5,
            )
            self.play(Create(strike), run_time=0.55)
            self.wait(0.7)

        self.wait(0.92)   # ≈ 5.72s total


# ── S03 — ANCHOR PLANTED (paragraph, two words underlined) ──────────────────
# Duration 5.74s  ← S10 derives from this exact layout
class S03Scene(Scene):
    def construct(self):
        eyebrow = Text("hold on to this", font=SANS, font_size=24,
                        color=INK, weight=BOLD).shift(UP * 3.0)
        para, highlights = _build_anchor_paragraph()
        para.move_to(ORIGIN + DOWN * 0.2)
        box = _anchor_box(para)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Write(para), run_time=1.8)
        self.wait(0.5)
        self.play(Create(box), Create(highlights), run_time=0.6)
        self.wait(2.44)   # ≈ 5.74s total


# ── S04 — ghost characters between letters ──────────────────────────────────
# Duration 5.95s
class S04Scene(Scene):
    def construct(self):
        word = Text("invisible", font=SERIF, font_size=96, color=INK)
        word.move_to(ORIGIN)
        self.add(word)
        self.wait(0.5)

        # Ghost zero-width-style glyphs drawn between letters at low opacity
        # We approximate with small faint terracotta dots between letter positions
        ghosts = []
        letter_xs = [word.get_left()[0] + (i + 0.5) * word.width / 9
                     for i in range(8)]  # 8 gaps for 9-letter word
        for x in letter_xs:
            g = Text("·", font=SERIF, font_size=32, color=TERRA)
            g.move_to([x, word.get_center()[1] + 0.1, 0])
            g.set_opacity(0)
            ghosts.append(g)

        ghost_group = VGroup(*ghosts)
        self.add(ghost_group)

        # Fade ghosts up one by one — sell the wrong model
        self.play(
            *[g.animate.set_opacity(0.55) for g in ghosts],
            lag_ratio=0.12, run_time=1.8
        )
        caption = Text("invisible spaces between letters?", font=SERIF,
                        font_size=34, color=INK).shift(DOWN * 2.2)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2.45)   # ≈ 5.95s total


# ── S05 — retyped clean; mark survives ──────────────────────────────────────
# Duration 6.95s
class S05Scene(Scene):
    def construct(self):
        # Start: show the ghost scene from S04 (briefly)
        word = Text("invisible", font=SERIF, font_size=96, color=INK).move_to(ORIGIN + UP * 0.5)
        ghost_row = Text("· · · · · · · ·", font=SERIF, font_size=28, color=TERRA)
        ghost_row.set_opacity(0.55).move_to(word.get_center())
        self.add(word, ghost_row)
        self.wait(0.3)

        # Ghost glyphs fail to appear in the retyped version → fade them out
        self.play(FadeOut(ghost_row), run_time=0.7)

        # Retype the word into a plain field below
        field_bg = RoundedRectangle(corner_radius=0.2, width=6.5, height=1.0,
                                    fill_color=GROUND, fill_opacity=1,
                                    stroke_color=INK, stroke_width=1.5)
        field_bg.shift(DOWN * 1.4)
        self.play(FadeIn(field_bg), run_time=0.3)

        typed = ""
        letters = list("invisible")
        typed_mob = always_redraw(lambda: Text(typed, font=SERIF, font_size=52, color=INK)
                                  .move_to(field_bg))
        self.add(typed_mob)
        for ch in letters:
            typed += ch
            self.wait(0.18)

        self.wait(0.3)
        # The mark survives — terracotta underline sweeps the retyped word
        field_w = field_bg.width - 0.6
        left  = field_bg.get_bottom() + LEFT  * (field_w / 2) + DOWN * 0.08
        right = field_bg.get_bottom() + RIGHT * (field_w / 2) + DOWN * 0.08
        ul = Line(left, right, color=TERRA, stroke_width=6)
        self.play(Create(ul), run_time=1.0)
        self.wait(0.62)   # ≈ 6.95s total


# ── S06 — word-by-word build, then fork ─────────────────────────────────────
# Duration 5.16s
class S06Scene(Scene):
    def construct(self):
        # Sentence at y=0.8; fork labels at y=[1.8, 0.2, -1.1] — none at y=0.8
        # so the horizontal text-scan band for the sentence never intersects a label
        # (prevents false kerning fail from stem blobs at the same y-level).
        words = ["Claude", "writes", "one", "word", "at", "a", "time,", "and…"]
        cur_x = -5.5
        word_mobs = []
        for w in words:
            m = Text(w, font=SERIF, font_size=46, color=INK)
            m.move_to([cur_x + m.width / 2, 0.8, 0])
            cur_x += m.width + 0.06
            word_mobs.append(m)

        for m in word_mobs:
            self.play(FadeIn(m), run_time=0.22)
            self.wait(0.09)

        # Fork into three candidates
        fork_x = word_mobs[-1].get_right()[0] + 0.4
        fork_y = 0.8
        candidates = ["quickly.", "softly.", "well."]
        ys = [1.8, 0.2, -1.1]
        branch_dots = []
        for cand, y in zip(candidates, ys):
            stem = Line([fork_x, fork_y, 0], [fork_x + 0.5, y, 0],
                        color=INK, stroke_width=2.5)
            label = Text(cand, font=SERIF, font_size=46, color=INK)
            label.move_to([fork_x + 0.5 + label.width / 2 + 0.1, y, 0])
            branch_dots.extend([stem, label])

        self.play(*[FadeIn(b) for b in branch_dots], run_time=0.8)
        self.wait(1.31)   # ≈ 5.16s total


# ── S07 — two branches, a die picks one ─────────────────────────────────────
# Duration 5.63s
class S07Scene(Scene):
    def construct(self):
        # Sentence stem
        stem_txt = Text("The weather today was cold and",
                        font=SERIF, font_size=46, color=INK)
        stem_txt.move_to(ORIGIN + UP * 1.1 + LEFT * 1.0)
        self.add(stem_txt)

        # Fork y positions
        fork_x = stem_txt.get_right()[0] + 0.3
        fork_y = stem_txt.get_center()[1]
        branch_data = [("overcast.", 1.8), ("grey.", 0.4)]

        branches = VGroup()
        labels   = VGroup()
        for cand, y in branch_data:
            line = Line([fork_x, fork_y, 0], [fork_x + 1.0, y, 0],
                        color=INK, stroke_width=1.5)
            lbl  = Text(cand, font=SERIF, font_size=46, color=INK)
            lbl.move_to([fork_x + 1.0 + lbl.width / 2 + 0.12, y, 0])
            branches.add(line)
            labels.add(lbl)

        self.play(Create(branches), FadeIn(labels), run_time=0.7)
        self.wait(0.4)

        # Die: INK square + larger INK dot (TERRA dot at radius=0.08 was 22px at 1080p,
        # below the 35px min-size floor; INK at radius=0.18 = 49px diameter, passes).
        die = VGroup(
            Square(side_length=0.55, fill_color=GROUND, fill_opacity=1,
                   stroke_color=INK, stroke_width=3),
            Dot(radius=0.18, color=INK),
        )
        die.move_to([fork_x + 0.5, fork_y, 0])
        self.play(FadeIn(die), run_time=0.3)

        # Die "tumbles" to pick "overcast"
        chosen_y = branch_data[0][1]
        self.play(
            die.animate.move_to([fork_x + 1.05, chosen_y, 0]),
            run_time=0.8
        )
        # Highlight chosen branch — TERRA underline is the one accent for this beat.
        # (set_color(TERRA) on text fails §8.3 contrast 2.74:1 < 4.5:1; underline is structural.)
        chosen_lbl = labels[0]
        ul = Line(
            [chosen_lbl.get_left()[0],  chosen_lbl.get_bottom()[1] - 0.09, 0],
            [chosen_lbl.get_right()[0], chosen_lbl.get_bottom()[1] - 0.09, 0],
            color=TERRA, stroke_width=4,
        )
        self.play(Create(ul), run_time=0.4)
        self.wait(2.3)   # ≈ 5.63s total


# ── S08 — die swapped for a key ─────────────────────────────────────────────
# Duration 6.17s
class S08Scene(Scene):
    def construct(self):
        # Same stem as S07
        stem_txt = Text("The weather today was cold and",
                        font=SERIF, font_size=46, color=INK)
        stem_txt.move_to(ORIGIN + UP * 1.1 + LEFT * 1.0)
        self.add(stem_txt)

        fork_x = stem_txt.get_right()[0] + 0.3
        fork_y = stem_txt.get_center()[1]
        branch_data = [("overcast.", 1.8), ("grey.", 0.4)]

        for cand, y in branch_data:
            line = Line([fork_x, fork_y, 0], [fork_x + 1.0, y, 0],
                        color=INK, stroke_width=1.5)
            lbl  = Text(cand, font=SERIF, font_size=46, color=INK)
            lbl.move_to([fork_x + 1.0 + lbl.width / 2 + 0.12, y, 0])
            self.add(line, lbl)

        # Die fades in then out
        die = VGroup(
            Square(side_length=0.55, fill_color=GROUND, fill_opacity=1,
                   stroke_color=INK, stroke_width=2),
            Dot(radius=0.08, color=INK),
        )
        die.move_to([fork_x + 0.5, fork_y, 0])
        self.play(FadeIn(die), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(die), run_time=0.5)

        # Key icon (circle + stem + teeth) in INK — TERRA wire is the one accent
        key_circle = Circle(radius=0.28, stroke_color=INK, stroke_width=3,
                            fill_opacity=0)
        key_stem   = Line(RIGHT * 0.28, RIGHT * 0.85, color=INK, stroke_width=3)
        key_tooth1 = Line(RIGHT * 0.55 + DOWN * 0.0, RIGHT * 0.55 + DOWN * 0.18,
                          color=INK, stroke_width=3)
        key_tooth2 = Line(RIGHT * 0.72 + DOWN * 0.0, RIGHT * 0.72 + DOWN * 0.13,
                          color=INK, stroke_width=3)
        key = VGroup(key_circle, key_stem, key_tooth1, key_tooth2)
        key.move_to([fork_x + 0.5, fork_y, 0])

        context = Text("cold and", font=SERIF, font_size=46, color=INK)
        context.move_to(stem_txt.get_right() + LEFT * 1.2 + DOWN * 1.3)
        wire = DashedLine(context.get_top(), key.get_bottom(),
                          color=TERRA, stroke_width=1.5, dash_length=0.12)

        self.play(Create(key), run_time=0.6)
        self.play(FadeIn(context), Create(wire), run_time=0.7)
        self.wait(3.07)   # ≈ 6.17s total


# ── S09 — sequence of choices checked against key ───────────────────────────
# Duration 5.10s
class S09Scene(Scene):
    def construct(self):
        n = 14
        sq_size = 0.46
        gap = 0.12
        total_w = n * sq_size + (n - 1) * gap

        squares = VGroup()
        for i in range(n):
            sq = Square(
                side_length=sq_size,
                fill_color=GROUND, fill_opacity=1,
                stroke_color=INK, stroke_width=1.5,
            )
            squares.add(sq)
        squares.arrange(RIGHT, buff=gap).move_to(ORIGIN + UP * 0.7)
        self.add(squares)

        # Key sweeps left to right, each square ticks (turns terracotta)
        for i, sq in enumerate(squares):
            self.play(
                sq.animate.set_fill(TERRA, opacity=0.55)
                         .set_stroke(TERRA),
                run_time=0.12
            )

        self.wait(0.2)

        # Confidence bar fills beneath
        bar_bg = Rectangle(width=total_w, height=0.28,
                            fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=1.5)
        bar_bg.next_to(squares, DOWN, buff=0.45)
        self.add(bar_bg)

        bar_fill = Rectangle(width=0.01, height=0.28,
                              fill_color=TERRA, fill_opacity=0.85,
                              stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT).align_to(bar_bg, DOWN)
        self.add(bar_fill)
        self.play(
            bar_fill.animate.stretch_to_fit_width(total_w).align_to(bar_bg, LEFT),
            run_time=1.0
        )
        label = Text("PATTERN CONFIRMED", font=SANS, font_size=22,
                      color=TERRA, weight=BOLD)
        label.next_to(bar_bg, DOWN, buff=0.25)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(0.78)   # ≈ 5.10s total


# ── S10 — ANCHOR PAYOFF (identical to S03, confidence bar barely moves) ─────
# Duration 7.83s
class S10Scene(Scene):
    def construct(self):
        eyebrow = Text("hold on to this", font=SANS, font_size=24,
                        color=INK, weight=BOLD).shift(UP * 3.0)
        para, highlights = _build_anchor_paragraph()
        para.move_to(ORIGIN + DOWN * 0.2)
        box = _anchor_box(para)

        # Show the anchor — same layout as S03
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.add(para, box, highlights)
        self.wait(0.8)

        # Confidence bar appears beneath — and barely moves
        bar_w = para.width + 0.7
        bar_bg = Rectangle(width=bar_w, height=0.22,
                            fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=1.5)
        bar_bg.next_to(box, DOWN, buff=0.45)
        self.add(bar_bg)

        # Bar fills only 2 of 14 notches worth (~14% = 2 changed words out of ~14)
        bar_fill = Rectangle(width=0.01, height=0.22,
                              fill_color=INK, fill_opacity=0.35,
                              stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT).align_to(bar_bg, DOWN)
        self.add(bar_fill)
        self.play(
            bar_fill.animate.stretch_to_fit_width(bar_w * 0.13)
                            .align_to(bar_bg, LEFT),
            run_time=1.2
        )
        label = Text("a handful is not a pattern", font=SANS, font_size=22,
                      color=INK)
        label.next_to(bar_bg, DOWN, buff=0.25)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(4.08)   # ≈ 7.83s total


# ── S11 — forks that collapse to one branch ──────────────────────────────────
# Duration 6.06s
class S11Scene(Scene):
    def construct(self):
        rows = [
            ("Principia ___ →", "MATHEMATICA"),
            ("2  +  2  =", "4"),
            ("def add(a, b):   →", "return a + b"),
        ]

        row_mobs = []
        for i, (stem, answer) in enumerate(rows):
            y = 1.4 - i * 1.5
            stem_t = Text(stem, font=SERIF, font_size=46, color=INK)
            stem_t.move_to([-2.8, y, 0], aligned_edge=LEFT)
            ans_t  = Text(answer, font=SERIF, font_size=46, color=INK, weight=BOLD)
            ans_t.move_to([stem_t.get_right()[0] + 0.3 + ans_t.width / 2, y, 0])
            row_mobs.append((stem_t, ans_t))

        for stem_t, ans_t in row_mobs:
            self.play(FadeIn(stem_t), run_time=0.3)
            self.wait(0.1)
            self.play(Write(ans_t), run_time=0.60)
            ul = Line(ans_t.get_left() + DOWN * 0.12,
                      ans_t.get_right() + DOWN * 0.12,
                      color=TERRA, stroke_width=4)
            self.play(Create(ul), run_time=0.20)
            self.wait(0.25)

        caption = Text("no free choice — nowhere for the mark to live",
                        font=SERIF, font_size=46, color=INK)
        caption.shift(DOWN * 2.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(1.21)   # 3×(0.3+0.1+0.60+0.20+0.25)+0.5+1.21 ≈ 6.06s


# ── S12 — DIRECTION A: mark found, wrong conclusion struck ──────────────────
# Duration 4.84s
class S12Scene(Scene):
    def construct(self):
        _direction_beat(
            self,
            top_label="MARK FOUND",
            conclusion="A HUMAN DID NOT WRITE THIS",
            reasons=[],
            side="left",
            duration=4.84,
        )


# ── S13 — DIRECTION B: no mark, wrong conclusion struck + three reasons ──────
# Duration 5.74s
class S13Scene(Scene):
    def construct(self):
        _direction_beat(
            self,
            top_label="NO MARK FOUND",
            conclusion="CLAUDE WASN'T INVOLVED",
            reasons=["TOO SHORT", "TOO FACTUAL", "TOO LIGHTLY EDITED"],
            side="right",
            duration=5.74,
        )


def _direction_beat(scene, top_label, conclusion, reasons, side, duration):
    """Shared layout for S12 / S13.  side='left' → content left-dominant;
    side='right' → content right-dominant (mirrored).  The two beats read as
    companion halves of the same idea."""
    sign = -1 if side == "left" else 1
    cx = sign * 0.8  # horizontal centre of content

    # Top chip: MARK FOUND or NO MARK FOUND
    chip_rect = RoundedRectangle(corner_radius=0.28, width=4.5, height=0.85,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
    chip_txt  = Text(top_label, font=SANS, font_size=28, color=INK, weight=BOLD)
    chip_txt.move_to(chip_rect)
    chip = VGroup(chip_rect, chip_txt)
    chip.move_to([cx, 2.0, 0])

    tick = Text("✓", font=SANS, font_size=36, color=INK)
    tick.next_to(chip, LEFT if side == "right" else RIGHT, buff=0.18)

    # Arrow pointing toward conclusion — stroke_width=3, ratio=0.25 gives tip ~64px at 4K (>35px floor)
    arrow = Arrow(
        chip.get_bottom() + DOWN * 0.1,
        chip.get_bottom() + DOWN * 1.05,
        buff=0, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.25
    )

    # Conclusion text
    conc = Text(conclusion, font=SANS, font_size=28, color=INK, weight=BOLD)
    conc.move_to(chip.get_bottom() + DOWN * 1.5)

    # Strikethrough in TERRA
    strike = Line(
        conc.get_left() + LEFT * 0.08,
        conc.get_right() + RIGHT * 0.08,
        color=TERRA, stroke_width=5,
    )

    scene.play(FadeIn(chip), FadeIn(tick), run_time=0.45)
    scene.play(GrowArrow(arrow), run_time=0.45)
    scene.play(FadeIn(conc), run_time=0.35)
    scene.play(Create(strike), run_time=0.55)

    if reasons:
        reason_mobs = VGroup(*[
            Text(r, font=SANS, font_size=22, color=INK)
            for r in reasons
        ]).arrange(DOWN, buff=0.22)
        reason_mobs.next_to(conc, DOWN, buff=0.55)
        scene.play(FadeIn(reason_mobs, lag_ratio=0.4), run_time=0.7)
        scene.wait(duration - 0.45 - 0.45 - 0.35 - 0.55 - 0.7)
    else:
        scene.wait(duration - 0.45 - 0.45 - 0.35 - 0.55)
