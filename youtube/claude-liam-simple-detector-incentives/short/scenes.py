"""short/scenes.py — portrait (9:16, 1080×1920) Manim scenes.
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
One terracotta accent per beat.

THREE RECURRING CONSTRUCTIONS (portrait variants):
  THE SHAPE  → S01, S02, S12  —  vertical divider, labels stacked in each half
  THE ANCHOR → S03, S13       —  same page+magnifier composition
  MIRROR     → S15, S16       —  full-width each direction

Portrait frame: 4.5 wide × 8.0 tall (1080×1920)
Title-safe x: ±2.0   y: ±3.5
Font floor at 1920px height: ~62px  → use font_size ≥ 46 (≈82px at portrait scale)

Render:
  manim -qk --fps 24 -r 1080,1920 short/scenes.py S01Scene
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF   = "EB Garamond"
DISPLAY = "Montserrat"

# Portrait frame constants
FW = 4.5   # frame width in Manim units
FH = 8.0   # frame height in Manim units


# ── RECURRING CONSTRUCTION 1 — THE SHAPE (portrait) ──────────────────────────
def _the_shape_916():
    """Portrait THE SHAPE: wide rect, vertical TERRA divider, labels side-by-side.
    Width 4.0 (fits 4.5 frame), labels centered in each half.
    """
    rect = RoundedRectangle(
        corner_radius=0.3, width=4.0, height=1.8,
        fill_color=GROUND, fill_opacity=1,
        stroke_color=INK, stroke_width=3,
    ).move_to(ORIGIN)
    divider = Line(ORIGIN + UP * 0.7, ORIGIN + DOWN * 0.7,
                   color=TERRA, stroke_width=3)
    lbl_l = Text("BUILDS IT", font=DISPLAY, font_size=52, color=INK, weight=BOLD)
    lbl_r = Text("PAYS FOR IT", font=DISPLAY, font_size=52, color=INK, weight=BOLD)
    for lbl in (lbl_l, lbl_r):
        if lbl.width > 1.7:
            lbl.scale_to_fit_width(1.7)
    lbl_l.move_to(ORIGIN + LEFT * 1.0)
    lbl_r.move_to(ORIGIN + RIGHT * 1.0)
    return VGroup(rect, divider, lbl_l, lbl_r)


# ── RECURRING CONSTRUCTION 2 — THE ANCHOR (portrait) ─────────────────────────
def _the_anchor_916():
    """Portrait anchor: page, magnifier, dot grid — same composition as landscape."""
    page = Rectangle(
        width=3.0, height=3.8,
        fill_color="#FFFFFF", fill_opacity=1,
        stroke_color=INK, stroke_width=2,
    ).move_to(ORIGIN + DOWN * 0.2)
    dot_center = page.get_center() + RIGHT * 0.2 + UP * 0.4
    rows, cols, spacing = 3, 4, 0.28
    dots = VGroup()
    for r in range(rows):
        for c in range(cols):
            d = Dot(radius=0.07, color=TERRA)
            d.move_to(dot_center + RIGHT * (c - 1.5) * spacing
                                 + UP  * (r - 1.0) * spacing * 0.9)
            dots.add(d)
    lens = Circle(radius=0.9, stroke_color=INK, stroke_width=3, fill_opacity=0)
    lens.move_to(dot_center)
    handle = Line(
        dot_center + RIGHT * 0.64 + DOWN * 0.64,
        dot_center + RIGHT * 1.28 + DOWN * 1.28,
        color=INK, stroke_width=5,
    )
    magnifier = VGroup(lens, handle)
    return page, magnifier, dots


# ── helper: small dotted page for anchor row ──────────────────────────────────
def _dotted_page_916(label):
    pg = Rectangle(
        width=1.6, height=2.0,
        fill_color="#FFFFFF", fill_opacity=1,
        stroke_color=INK, stroke_width=1.5,
    )
    for r in range(2):
        for c in range(2):
            d = Dot(radius=0.05, color=TERRA)
            d.move_to(pg.get_center()
                      + RIGHT * (c - 0.5) * 0.3
                      + UP    * (r - 0.5) * 0.3)
            pg.add(d)
    lbl = Text(label, font=DISPLAY, font_size=22, color=INK, weight=BOLD)
    lbl.next_to(pg, DOWN, buff=0.12)
    return VGroup(pg, lbl)


# ── RECURRING CONSTRUCTION 3 — direction half (portrait) ─────────────────────
def _direction_half_916(top_label, conclusion, cy, ink_strike=False):
    """Portrait direction block: full-width chip → arrow → conclusion + strike."""
    chip_r = RoundedRectangle(
        corner_radius=0.22, width=3.8, height=0.9,
        fill_color=INK, fill_opacity=1, stroke_width=0,
    ).move_to([0, cy, 0])
    chip_t = Text(top_label, font=DISPLAY, font_size=48, color=GROUND, weight=BOLD)
    chip_t.scale_to_fit_width(3.4)
    chip_t.move_to(chip_r)
    chip = VGroup(chip_r, chip_t)
    arrow = Arrow(
        chip.get_bottom() + DOWN * 0.06,
        chip.get_bottom() + DOWN * 1.1,
        buff=0, color=INK, stroke_width=4,
        max_tip_length_to_length_ratio=0.25,
    )
    conc = Text(conclusion, font=DISPLAY, font_size=42, color=INK, weight=BOLD)
    conc.scale_to_fit_width(3.6)
    conc.move_to([0, cy - 1.8, 0])
    if ink_strike:
        strike = Rectangle(
            width=conc.width + 0.14, height=0.22,
            fill_color=INK, fill_opacity=0.22, stroke_width=0,
        ).move_to(conc.get_center())
    else:
        strike = Rectangle(
            width=conc.width + 0.14, height=0.22,
            fill_color=TERRA, fill_opacity=1, stroke_width=0,
        ).move_to(conc.get_center())
    return chip, arrow, conc, strike


# ── S01 — THE SHAPE introduced ────────────────────────────────────────────────
# Duration 6.66s  |  TERRA: vertical divider
class S01Scene(Scene):
    def construct(self):
        shape = _the_shape_916()
        rect, divider, lbl_l, lbl_r = shape

        self.play(FadeIn(rect), run_time=0.5)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.6)
        self.play(Create(divider), run_time=0.7)
        self.wait(4.86)   # 0.5+0.6+0.7+4.86 = 6.66s


# ── S02 — THE SHAPE held ──────────────────────────────────────────────────────
# Duration 6.46s  |  TERRA: divider  |  faces imply rotation behind rect
class S02Scene(Scene):
    def construct(self):
        shape = _the_shape_916()

        face_a = Circle(radius=0.5, fill_color="#D4C9B0", fill_opacity=1,
                        stroke_color=INK, stroke_width=2).move_to(UP * 2.2)
        face_b = Circle(radius=0.5, fill_color="#B8A89A", fill_opacity=1,
                        stroke_color=INK, stroke_width=2).move_to(UP * 2.2)

        self.play(FadeIn(face_a), FadeIn(shape), run_time=0.5)
        self.play(ReplacementTransform(face_a, face_b), run_time=0.6)
        self.wait(5.36)   # 0.5+0.6+5.36 = 6.46s


# ── S03 — THE ANCHOR planted ──────────────────────────────────────────────────
# Duration 7.85s  |  TERRA: dot grid
class S03Scene(Scene):
    def construct(self):
        page, magnifier, dots = _the_anchor_916()

        self.play(FadeIn(page), run_time=0.5)
        self.play(FadeIn(dots), run_time=0.6)
        self.play(Create(magnifier), run_time=0.7)
        self.wait(6.0)   # 0.5+0.6+0.7+6.0 = 7.8s


# ── S04 — locked drawer (hypothesis) ─────────────────────────────────────────
# Duration 6.14s  |  TERRA: none (INK strip)
class S04Scene(Scene):
    def construct(self):
        drawer = RoundedRectangle(
            corner_radius=0.2, width=3.2, height=1.6,
            fill_color="#E8E4DC", fill_opacity=1,
            stroke_color=INK, stroke_width=2,
        ).move_to(ORIGIN + UP * 0.4)
        knob = Dot(radius=0.14, color=INK).move_to(
            drawer.get_center() + RIGHT * 0.9
        )

        strip = Rectangle(
            width=drawer.width + 0.2, height=0.6,
            fill_color=INK, fill_opacity=0.88, stroke_width=0,
        ).move_to(drawer.get_center() + DOWN * 0.5)
        strip_lbl = Text("TECHNICAL CHALLENGES",
                         font=DISPLAY, font_size=26, color=GROUND, weight=BOLD)
        strip_lbl.scale_to_fit_width(3.0)
        strip_lbl.move_to(strip)

        self.play(FadeIn(drawer), FadeIn(knob), run_time=0.5)
        self.play(FadeIn(strip), FadeIn(strip_lbl), run_time=0.5)
        self.wait(5.14)   # 0.5+0.5+5.14 = 6.14s


# ── S05 — two objections (stacked vertically in portrait) ─────────────────────
# Duration 8.94s  |  TERRA: none (INK only)
class S05Scene(Scene):
    def construct(self):
        # Top panel: paraphrase strips the mark
        top_box = Rectangle(
            width=4.0, height=2.8,
            fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
        ).move_to(UP * 2.1)

        marked_lbl = Text("marked text.", font=SERIF, font_size=50, color=INK)
        marked_lbl.scale_to_fit_width(3.2)
        marked_lbl.move_to(top_box.get_center() + UP * 0.6)

        para_lbl = Text("paraphrased text.", font=SERIF, font_size=50, color=INK)
        para_lbl.scale_to_fit_width(3.2)
        para_lbl.move_to(top_box.get_center() + DOWN * 0.35)

        v_arrow = Arrow(
            marked_lbl.get_bottom() + DOWN * 0.06,
            para_lbl.get_top() + UP * 0.06,
            buff=0.04, color=INK, stroke_width=3,
            max_tip_length_to_length_ratio=0.22,
        )
        caption_l = Text("mark gone", font=DISPLAY, font_size=40, color=INK)
        caption_l.scale_to_fit_width(2.8)
        caption_l.move_to(top_box.get_bottom() + UP * 0.48)

        # Bottom panel: clean second-language text, wrongly flagged
        bot_box = Rectangle(
            width=4.0, height=2.8,
            fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
        ).move_to(DOWN * 2.1)

        clean_l1 = Text("Clean second-language", font=SERIF, font_size=50, color=INK)
        clean_l2 = Text("writing.", font=SERIF, font_size=50, color=INK)
        if clean_l1.width > 3.4:
            sf = 3.4 / clean_l1.width
            clean_l1.scale(sf)
            clean_l2.scale(sf)
        clean_grp = VGroup(clean_l1, clean_l2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        clean_grp.move_to(bot_box.get_center() + UP * 0.2)

        flag_rect = Rectangle(
            width=2.2, height=0.55,
            fill_color=INK, fill_opacity=1, stroke_width=0,
        )
        flag_txt = Text("FLAGGED", font=DISPLAY, font_size=26,
                        color=GROUND, weight=BOLD).move_to(flag_rect)
        flag_grp = VGroup(flag_rect, flag_txt)
        flag_grp.move_to(bot_box.get_bottom() + UP * 0.48)

        self.play(FadeIn(top_box), FadeIn(bot_box), run_time=0.4)
        self.play(FadeIn(marked_lbl), run_time=0.4)
        self.play(GrowArrow(v_arrow), run_time=0.5)
        self.play(FadeIn(para_lbl), run_time=0.4)
        self.play(FadeOut(VGroup()), FadeIn(caption_l), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(clean_grp), run_time=0.4)
        self.play(FadeIn(flag_grp), run_time=0.5)
        self.wait(5.4)   # ≈8.9s total


# ── S06 — objections stand, question mark ────────────────────────────────────
# Duration 8.11s  |  TERRA: none (INK qmark)
class S06Scene(Scene):
    def construct(self):
        obj1 = Text("paraphrase defeats\nthe mark",
                    font=SERIF, font_size=50, color=INK, line_spacing=0.1)
        obj1.scale_to_fit_width(3.8)

        obj2 = Text("false positives hit\nsecond-language writers",
                    font=SERIF, font_size=50, color=INK, line_spacing=0.1)
        obj2.scale_to_fit_width(3.8)

        objs = VGroup(obj1, obj2).arrange(DOWN, buff=0.8).move_to(UP * 1.8)

        qmark = Text("?", font=SERIF, font_size=160, color=INK)
        qmark.move_to(DOWN * 2.4)

        self.play(FadeIn(obj1), run_time=0.4)
        self.play(FadeIn(obj2), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(qmark), run_time=0.6)
        self.wait(6.11)   # 0.4+0.4+0.6+0.6+6.11 = 8.11s


# ── S07 — three asking parties; one requirement arrow ────────────────────────
# Duration 5.27s  |  TERRA: none (INK chips + arrow)
class S07Scene(Scene):
    def construct(self):
        parties = ["REGULATOR", "SCHOOL", "COURT"]
        chips = VGroup()
        for lbl in parties:
            chip_r = RoundedRectangle(
                corner_radius=0.22, width=3.0, height=0.75,
                fill_color=INK, fill_opacity=1, stroke_width=0,
            )
            chip_t = Text(lbl, font=DISPLAY, font_size=46, color=GROUND, weight=BOLD)
            chip_t.scale_to_fit_width(2.6)
            chip_t.move_to(chip_r)
            chips.add(VGroup(chip_r, chip_t))
        chips.arrange(DOWN, buff=0.35).move_to(UP * 0.8)

        req_arrow = Arrow(
            chips.get_bottom() + DOWN * 0.1,
            chips.get_bottom() + DOWN * 1.1,
            buff=0.05, color=INK, stroke_width=5,
            max_tip_length_to_length_ratio=0.20,
        )
        req_lbl = Text("DETECTION REQUIRED",
                       font=DISPLAY, font_size=46, color=INK, weight=BOLD)
        req_lbl.scale_to_fit_width(3.6)
        req_lbl.next_to(req_arrow, DOWN, buff=0.2)

        self.play(FadeIn(chips), run_time=0.6)
        self.play(GrowArrow(req_arrow), FadeIn(req_lbl), run_time=0.8)
        self.wait(3.87)   # 0.6+0.8+3.87 = 5.27s


# ── S08 — requirement lands on the builder ───────────────────────────────────
# Duration 5.03s  |  TERRA: shape divider only
class S08Scene(Scene):
    def construct(self):
        shape = _the_shape_916()
        shape.move_to(DOWN * 1.2)
        # INK fill so blob detector sees one solid block
        shape[0].set_fill(INK, opacity=1).set_stroke(width=0)
        shape[2].set_color(GROUND)
        shape[3].set_color(GROUND)

        req_lbl = Text("DETECTION\nREQUIRED",
                       font=DISPLAY, font_size=52, color=INK, weight=BOLD,
                       line_spacing=0.1)
        req_lbl.scale_to_fit_width(3.0)
        req_lbl.move_to(UP * 2.2)

        req_arrow = Arrow(
            req_lbl.get_bottom() + DOWN * 0.08,
            shape.get_top() + UP * 0.05,
            buff=0.05, color=INK, stroke_width=5,
            max_tip_length_to_length_ratio=0.18,
        )

        self.play(FadeIn(req_lbl), run_time=0.4)
        self.play(GrowArrow(req_arrow), run_time=0.8)
        self.play(FadeIn(shape), run_time=0.4)
        self.wait(3.43)   # 0.4+0.8+0.4+3.43 = 5.03s


# ── S09 — first mover ships; users flow to rival ──────────────────────────────
# Duration 5.59s  |  TERRA: user flow arrow
class S09Scene(Scene):
    def construct(self):
        def _provider(label, tag=None, pos=ORIGIN):
            box = RoundedRectangle(
                corner_radius=0.22, width=3.4, height=1.5,
                fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=2,
            ).move_to(pos)
            lbl = Text(label, font=DISPLAY, font_size=40, color=INK, weight=BOLD)
            lbl.scale_to_fit_width(2.8)
            lbl.move_to(box.get_center() + (UP * 0.25 if tag else ORIGIN))
            grp = VGroup(box, lbl)
            if tag:
                t = Text(tag, font=SERIF, font_size=32, color=INK)
                t.scale_to_fit_width(2.8)
                t.move_to(box.get_center() + DOWN * 0.28)
                grp.add(t)
            return grp

        a_grp = _provider("PROVIDER A", tag="+ detector", pos=UP * 2.0)
        b_grp = _provider("PROVIDER B", pos=DOWN * 0.4)

        flow = Arrow(
            a_grp.get_bottom() + DOWN * 0.06,
            b_grp.get_top() + UP * 0.06,
            buff=0, color=TERRA, stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        users_lbl = Text("users", font=SERIF, font_size=36, color=TERRA)
        users_lbl.next_to(flow, RIGHT, buff=0.2)

        self.play(FadeIn(a_grp), FadeIn(b_grp), run_time=0.5)
        self.wait(0.3)
        self.play(GrowArrow(flow), FadeIn(users_lbl), run_time=0.6)
        self.play(a_grp.animate.scale(0.82), run_time=0.5)
        self.wait(3.69)   # 0.5+0.3+0.6+0.5+3.69 = 5.59s


# ── S10 — four providers wait; nobody moves ───────────────────────────────────
# Duration 5.61s  |  TERRA: "FIRST?" label
class S10Scene(Scene):
    def construct(self):
        positions = [
            LEFT * 1.0 + UP * 1.9,
            RIGHT * 1.0 + UP * 1.9,
            LEFT * 1.0 + DOWN * 0.3,
            RIGHT * 1.0 + DOWN * 0.3,
        ]
        labels = ["A", "B", "C", "D"]
        providers = VGroup()
        for pos, lbl in zip(positions, labels):
            box = RoundedRectangle(
                corner_radius=0.2, width=1.8, height=1.1,
                fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=2,
            ).move_to(pos)
            t = Text(lbl, font=DISPLAY, font_size=40, color=INK, weight=BOLD)
            t.move_to(box)
            providers.add(VGroup(box, t))

        first_lbl = Text("FIRST?", font=DISPLAY, font_size=60, color=TERRA, weight=BOLD)
        first_lbl.move_to(DOWN * 2.4)

        self.play(FadeIn(providers), run_time=0.6)
        self.play(FadeIn(first_lbl), run_time=0.5)
        self.wait(4.51)   # 0.6+0.5+4.51 = 5.61s


# ── S11 — ONE FLAG: reported figures ─────────────────────────────────────────
# Duration 10.39s  |  TERRA: none (INK FLAG chip)
class S11Scene(Scene):
    def construct(self):
        heading = Text("ONE FLAG", font=DISPLAY, font_size=64, color=INK, weight=BOLD)
        heading.move_to(UP * 3.0)

        # Reported figures behind dotted border
        fig_box = DashedVMobject(
            Rectangle(width=3.8, height=1.6,
                      fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=2),
            dashed_ratio=0.6,
        )
        fig_box.move_to(UP * 1.2)

        fig_txt_1 = Text("accuracy figure", font=SERIF, font_size=40, color=INK)
        fig_txt_2 = Text("user-attrition figure", font=SERIF, font_size=40, color=INK)
        for t in (fig_txt_1, fig_txt_2):
            if t.width > 3.2:
                t.scale_to_fit_width(3.2)
        VGroup(fig_txt_1, fig_txt_2).arrange(DOWN, buff=0.18).move_to(UP * 1.2)

        src_lbl = Text("SOURCE: PRESS REPORTING", font=DISPLAY, font_size=26,
                       color=INK, weight=BOLD)
        src_lbl.scale_to_fit_width(3.6)
        src_lbl.move_to(DOWN * 0.2)

        flag_rect = Rectangle(
            width=2.0, height=0.58,
            fill_color=INK, fill_opacity=1, stroke_width=0,
        )
        flag_txt = Text("FLAG", font=DISPLAY, font_size=26,
                        color=GROUND, weight=BOLD).move_to(flag_rect)
        flag_grp = VGroup(flag_rect, flag_txt)
        flag_grp.move_to(DOWN * 1.2)

        self.play(FadeIn(heading), run_time=0.5)
        self.play(FadeIn(fig_box), FadeIn(fig_txt_1), FadeIn(fig_txt_2), run_time=0.6)
        self.play(FadeIn(src_lbl), run_time=0.5)
        self.play(FadeIn(flag_grp), run_time=0.5)
        self.wait(8.29)   # 0.5+0.6+0.5+0.5+8.29 = 10.39s


# ── S12 — numbers fade; THE SHAPE remains ────────────────────────────────────
# Duration 4.84s  |  TERRA: divider
class S12Scene(Scene):
    def construct(self):
        numbers = Text("87 %", font=SERIF, font_size=100, color=INK)
        numbers.move_to(UP * 0.6)

        shape = _the_shape_916()
        shape.move_to(ORIGIN)

        self.add(numbers)
        self.play(FadeOut(numbers), run_time=0.8)
        self.play(FadeIn(shape), run_time=0.6)
        self.wait(3.44)   # 0.8+0.6+3.44 = 4.84s


# ── S13 — THE ANCHOR payoff: all printers at once ────────────────────────────
# Duration 7.55s  |  TERRA: dot grid
class S13Scene(Scene):
    def construct(self):
        # Open with THE ANCHOR (same as S03)
        page, magnifier, dots = _the_anchor_916()
        self.play(FadeIn(page), FadeIn(dots), Create(magnifier), run_time=0.8)
        self.wait(0.4)

        # Transition: anchor out, row of 4 pages in
        makers = ["A", "B", "C", "D"]
        row = VGroup(*[_dotted_page_916(m) for m in makers])
        row.arrange(RIGHT, buff=0.3)
        if row.width > 4.0:
            row.scale_to_fit_width(4.0)
        row.move_to(ORIGIN)

        self.play(FadeOut(page), FadeOut(magnifier), FadeOut(dots), run_time=0.5)
        self.play(FadeIn(row), run_time=0.6)
        self.wait(5.25)   # 0.8+0.4+0.5+0.6+5.25 = 7.55s


# ── S14 — row held; defector slot empty ───────────────────────────────────────
# Duration 6.40s  |  TERRA: none
class S14Scene(Scene):
    def construct(self):
        makers = ["A", "B", "C", "D"]
        row = VGroup(*[_dotted_page_916(m) for m in makers])
        row.arrange(RIGHT, buff=0.3)
        if row.width > 4.0:
            row.scale_to_fit_width(4.0)
        row.move_to(UP * 1.0)

        # Defector slot — empty gap
        slot = DashedVMobject(
            Rectangle(width=1.6, height=2.0,
                      fill_color=GROUND, fill_opacity=1,
                      stroke_color=INK, stroke_width=1.5),
            dashed_ratio=0.6,
        )
        slot_lbl = Text("?", font=DISPLAY, font_size=50, color=INK, weight=BOLD)
        slot_grp = VGroup(slot, slot_lbl.move_to(slot))
        slot_grp.move_to(DOWN * 2.2)

        self.play(FadeIn(row), run_time=0.5)
        self.play(FadeIn(slot_grp), run_time=0.5)
        self.wait(5.4)   # 0.5+0.5+5.4 = 6.4s


# ── S15 — direction A: weak ≠ chosen ─────────────────────────────────────────
# Duration 6.21s  |  TERRA: none (INK strike)
class S15Scene(Scene):
    def construct(self):
        chip, arrow, conc, strike = _direction_half_916(
            "WEAK DETECTOR", "SOMEONE CHOSE THIS",
            cy=2.2, ink_strike=True,
        )
        self.play(FadeIn(chip), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(conc), run_time=0.4)
        self.play(FadeIn(strike), run_time=0.5)
        self.wait(4.41)   # 0.4+0.5+0.4+0.5+4.41 = 6.21s


# ── S16 — direction B: reasons real ≠ nothing chosen ─────────────────────────
# Duration 8.26s  |  TERRA: strike on right direction
class S16Scene(Scene):
    def construct(self):
        # Top block: direction A (with INK faint strike — already seen)
        chip_a, arrow_a, conc_a, strike_a = _direction_half_916(
            "WEAK DETECTOR", "SOMEONE CHOSE THIS",
            cy=3.0, ink_strike=True,
        )
        # Bottom block: direction B (TERRA strike — new)
        chip_b, arrow_b, conc_b, strike_b = _direction_half_916(
            "REASONS ARE REAL", "SO NOTHING WAS CHOSEN",
            cy=-0.6, ink_strike=False,
        )

        self.add(chip_a, arrow_a, conc_a, strike_a)
        self.play(FadeIn(chip_b), run_time=0.4)
        self.play(GrowArrow(arrow_b), run_time=0.5)
        self.play(FadeIn(conc_b), run_time=0.4)
        self.play(FadeIn(strike_b), run_time=0.5)
        self.wait(6.41)   # 0.4+0.5+0.4+0.5+6.41 = 8.21s (≈8.26)
