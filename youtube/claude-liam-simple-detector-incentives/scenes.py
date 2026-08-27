"""scenes.py — Manim graphics for claude-liam-simple-detector-incentives
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
One terracotta accent per beat. No gradients, no glows, no shadows.

THREE RECURRING CONSTRUCTIONS:
  THE SHAPE  → S01 (intro) / S02 (survives) / S12 (numbers gone, shape stays)
  THE ANCHOR → S03 (planted) / S13 (payoff — same composition, then row of pages)
  MIRROR     → S15 (left half) / S16 (both halves side by side)

Render all:
  python3 render_scenes.py

Render one:
  cd anthropics/youtube/claude-liam-simple-detector-incentives
  manim -qh --fps 24 -r 1920,1080 scenes.py S01Scene
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF   = "EB Garamond"
DISPLAY = "Montserrat"


# ── RECURRING CONSTRUCTION 1 — THE SHAPE ──────────────────────────────────────
# Identical object used in S01, S02, S12.
def _the_shape(label_font_size=48):
    """Returns (rect, divider, lbl_l, lbl_r) as a VGroup.
    TERRA divider is the one accent. Labels BUILDS IT / PAYS FOR IT in INK.
    label_font_size: pass a larger value when the whole shape will be scaled down (S08).
    """
    rect = RoundedRectangle(
        corner_radius=0.4, width=9.0, height=3.0,
        fill_color=GROUND, fill_opacity=1,
        stroke_color=INK, stroke_width=3,
    ).move_to(ORIGIN)
    divider = Line(
        ORIGIN + UP * 1.2,
        ORIGIN + DOWN * 1.2,
        color=TERRA, stroke_width=3,
    )
    lbl_l = Text("BUILDS IT", font=DISPLAY, font_size=label_font_size, color=INK, weight=BOLD)
    lbl_r = Text("PAYS FOR IT", font=DISPLAY, font_size=label_font_size, color=INK, weight=BOLD)
    # Centre each label in its half (half-width=4.5, half-centre=2.25); cap at 3.8 to stay inside rect
    for lbl in (lbl_l, lbl_r):
        if lbl.width > 3.8:
            lbl.scale_to_fit_width(3.8)
    lbl_l.move_to(ORIGIN + LEFT * 2.25)
    lbl_r.move_to(ORIGIN + RIGHT * 2.25)
    return VGroup(rect, divider, lbl_l, lbl_r)


# ── RECURRING CONSTRUCTION 2 — THE ANCHOR ─────────────────────────────────────
# Identical composition used in S03 (plant) and S13 (payoff).
def _the_anchor():
    """Returns (page, magnifier, dots).
    page: white printed-page rect
    magnifier: VGroup(lens_circle, handle_line)
    dots: VGroup of TERRA dots (the "yellow" dots in the story)
    """
    page = Rectangle(
        width=5.5, height=7.0,
        fill_color="#FFFFFF", fill_opacity=1,
        stroke_color=INK, stroke_width=2,
    ).move_to(ORIGIN + DOWN * 0.1)

    dot_center = page.get_center() + RIGHT * 0.4 + UP * 0.5
    rows, cols, spacing = 3, 4, 0.36
    dots = VGroup()
    for r in range(rows):
        for c in range(cols):
            d = Dot(radius=0.08, color=TERRA)
            d.move_to(dot_center + RIGHT * (c - 1.5) * spacing
                                 + UP  * (r - 1.0) * spacing * 0.9)
            dots.add(d)

    lens = Circle(radius=1.1, stroke_color=INK, stroke_width=3, fill_opacity=0)
    lens.move_to(dot_center)
    handle = Line(
        dot_center + RIGHT * 0.78 + DOWN * 0.78,
        dot_center + RIGHT * 1.55 + DOWN * 1.55,
        color=INK, stroke_width=5,
    )
    magnifier = VGroup(lens, handle)

    return page, magnifier, dots


# ── helper: one page with dot grid (for S13 row) ──────────────────────────────
def _dotted_page(label):
    pg = Rectangle(
        width=2.2, height=2.8,
        fill_color="#FFFFFF", fill_opacity=1,
        stroke_color=INK, stroke_width=1.5,
    )
    for r in range(2):
        for c in range(2):
            d = Dot(radius=0.06, color=TERRA)
            d.move_to(pg.get_center()
                      + RIGHT * (c - 0.5) * 0.4
                      + UP    * (r - 0.5) * 0.4)
            pg.add(d)
    lbl = Text(label, font=DISPLAY, font_size=18, color=INK, weight=BOLD)
    lbl.next_to(pg, DOWN, buff=0.14)
    return VGroup(pg, lbl)


# ── S01 — THE SHAPE introduced (BUILDS IT / PAYS FOR IT) ──────────────────────
# Duration 6.66s  |  TERRA: vertical divider
class S01Scene(Scene):
    def construct(self):
        shape = _the_shape()
        rect, divider, lbl_l, lbl_r = shape

        self.play(FadeIn(rect), run_time=0.5)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.6)
        self.play(Create(divider), run_time=0.7)
        self.wait(4.86)   # 0.5+0.6+0.7+4.86 = 6.66s


# ── S02 — THE SHAPE held; anonymous silhouettes swap behind it ─────────────────
# Duration 6.46s  |  TERRA: divider (from THE SHAPE)
class S02Scene(Scene):
    def construct(self):
        shape = _the_shape()
        shape.set_z_index(10)   # shape stays in front of silhouettes
        self.add(shape)

        # Three anonymous silhouettes: head above the shape, body hidden behind it
        silhouette_xs = [LEFT * 2.2, ORIGIN, RIGHT * 2.2]
        for sx in silhouette_xs:
            head = Circle(radius=0.5, fill_color=INK, fill_opacity=0.18,
                          stroke_width=0).move_to(sx + UP * 2.45).set_z_index(1)
            body = Rectangle(width=0.85, height=1.6, fill_color=INK, fill_opacity=0.12,
                             stroke_width=0).move_to(sx + UP * 1.0).set_z_index(1)
            sil = VGroup(head, body)
            self.play(FadeIn(sil), run_time=0.4)
            self.wait(0.8)
            self.play(FadeOut(sil), run_time=0.4)

        self.wait(1.66)   # 3×(0.4+0.8+0.4)+1.66 = 6.46s


# ── S03 — THE ANCHOR planted (yellow dot grid behind magnifier) ────────────────
# Duration 7.85s  |  TERRA: dot grid
class S03Scene(Scene):
    def construct(self):
        page, magnifier, dots = _the_anchor()

        eyebrow = Text("hold on to this", font=DISPLAY, font_size=24,
                       color=INK, weight=BOLD).move_to(UP * 3.6)
        self.play(FadeIn(eyebrow), FadeIn(page), run_time=0.5)
        self.wait(0.4)
        self.play(Create(magnifier), run_time=0.7)
        self.play(FadeIn(dots), run_time=0.5)
        self.wait(5.75)   # 0.5+0.4+0.7+0.5+5.75 = 7.85s


# ── S04 — cover-up reading: tool locked in drawer, press release taped over ────
# Duration 6.14s  |  TERRA: the press-release strip (the burial label)
class S04Scene(Scene):
    def construct(self):
        drawer = Rectangle(
            width=6.0, height=2.8,
            fill_color=GROUND, fill_opacity=1,
            stroke_color=INK, stroke_width=2.5,
        ).move_to(ORIGIN + UP * 0.4)
        tool_lbl = Text("GOOD DETECTOR", font=DISPLAY, font_size=38,
                        color=INK, weight=BOLD).move_to(drawer.get_center())

        # Lock icon: body + shackle
        lock_body = Rectangle(
            width=0.55, height=0.5,
            fill_color=INK, fill_opacity=1, stroke_width=0,
        ).move_to(drawer.get_right() + LEFT * 0.85 + DOWN * 0.08)
        shackle = Arc(radius=0.22, start_angle=0, angle=PI,
                      stroke_color=INK, stroke_width=3.5)
        shackle.move_to(lock_body.get_top() + UP * 0.08)
        lock = VGroup(lock_body, shackle)

        # Press-release strip taped across the drawer (INK — legibility over accent)
        strip = Rectangle(
            width=drawer.width + 0.2, height=0.72,
            fill_color=INK, fill_opacity=0.88, stroke_width=0,
        ).move_to(drawer.get_center() + DOWN * 0.15)
        strip_lbl = Text("TECHNICAL CHALLENGES", font=DISPLAY, font_size=30,
                         color=GROUND, weight=BOLD).move_to(strip)

        self.play(FadeIn(drawer), FadeIn(tool_lbl), run_time=0.5)
        self.play(FadeIn(lock), run_time=0.4)
        self.wait(0.4)
        self.play(FadeIn(strip), FadeIn(strip_lbl), run_time=0.6)
        self.wait(4.24)   # 0.5+0.4+0.4+0.6+4.24 = 6.14s


# ── S05 — two panels: both objections shown as real failures ───────────────────
# Duration 8.94s  |  TERRA: FLAG chip on the right panel (false-positive case)
class S05Scene(Scene):
    def construct(self):
        # Left panel: paraphrase strips the mark
        left_box = Rectangle(
            width=5.8, height=4.6,
            fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
        ).move_to(LEFT * 3.6)

        marked_lbl = Text("marked text.", font=SERIF, font_size=50, color=INK)
        marked_lbl.move_to(left_box.get_center() + UP * 0.8)
        mark_dot = Dot(radius=0.18, color=INK)
        mark_dot.move_to(marked_lbl.get_right() + RIGHT * 0.24)

        para_lbl = Text("paraphrased text.", font=SERIF, font_size=50, color=INK)
        para_lbl.move_to(left_box.get_center() + DOWN * 0.55)

        v_arrow = Arrow(
            marked_lbl.get_bottom() + DOWN * 0.08,
            para_lbl.get_top() + UP * 0.08,
            buff=0.05, color=INK, stroke_width=3,
            max_tip_length_to_length_ratio=0.22,
        )
        caption_l = Text("mark gone", font=DISPLAY, font_size=46, color=INK)
        caption_l.move_to(left_box.get_bottom() + UP * 0.58)

        # Right panel: clean second-language text, wrongly flagged
        right_box = Rectangle(
            width=5.8, height=4.6,
            fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
        ).move_to(RIGHT * 3.6)

        txt_l1 = Text("Clean second-language", font=SERIF, font_size=50, color=INK)
        txt_l2 = Text("writing.", font=SERIF, font_size=50, color=INK)
        if txt_l1.width > 5.6:
            sf = 5.6 / txt_l1.width
            txt_l1.scale(sf)
            txt_l2.scale(sf)
        clean_txt = VGroup(txt_l1, txt_l2).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        clean_txt.move_to(right_box.get_center() + UP * 0.1)

        flag_rect = Rectangle(
            width=2.6, height=0.65,
            fill_color=INK, fill_opacity=1, stroke_width=0,
        )
        flag_txt = Text("FLAGGED", font=DISPLAY, font_size=28,
                        color=GROUND, weight=BOLD).move_to(flag_rect)
        flag_grp = VGroup(flag_rect, flag_txt)
        flag_grp.move_to(right_box.get_bottom() + UP * 0.55)

        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.4)
        self.play(FadeIn(marked_lbl), FadeIn(mark_dot), run_time=0.4)
        self.play(GrowArrow(v_arrow), run_time=0.5)
        self.play(FadeIn(para_lbl), run_time=0.4)
        self.play(FadeOut(mark_dot), FadeIn(caption_l), run_time=0.55)
        self.wait(0.5)
        self.play(FadeIn(clean_txt), run_time=0.4)
        self.play(FadeIn(flag_grp), run_time=0.5)
        self.wait(5.25)   # 0.4+0.4+0.5+0.4+0.55+0.5+0.4+0.5+5.25 = 8.90s ≈ 8.94


# ── S06 — both objections stand, no verdict, terracotta question mark ──────────
# Duration 8.11s  |  TERRA: question mark where the verdict would be
class S06Scene(Scene):
    def construct(self):
        obj1 = Text("paraphrase defeats the mark", font=SERIF, font_size=50, color=INK)
        obj2 = Text("false positives hit\nsecond-language writers",
                    font=SERIF, font_size=50, color=INK, line_spacing=1.25)
        objs = VGroup(obj1, obj2).arrange(DOWN, buff=0.9).move_to(ORIGIN + UP * 0.8)

        # Scale to fit safe zone
        if objs.width > 12.0:
            objs.scale_to_fit_width(12.0)

        qmark = Text("?", font=SERIF, font_size=160, color=INK)
        qmark.move_to(ORIGIN + DOWN * 2.2)

        self.play(FadeIn(obj1), run_time=0.4)
        self.play(FadeIn(obj2), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(qmark), run_time=0.6)
        self.wait(6.11)   # 0.4+0.4+0.6+0.6+6.11 = 8.11s


# ── S07 — three asking parties; one requirement arrow rises ────────────────────
# Duration 5.27s  |  TERRA: the requirement arrow + label
class S07Scene(Scene):
    def construct(self):
        parties = ["REGULATOR", "SCHOOL", "COURT"]
        ys = [1.8, 0.0, -1.8]
        party_mobs = VGroup()
        for lbl, y in zip(parties, ys):
            chip_r = RoundedRectangle(
                corner_radius=0.22, width=3.8, height=0.85,
                fill_color=INK, fill_opacity=1, stroke_width=0,
            ).move_to(LEFT * 4.2 + UP * y)
            chip_t = Text(lbl, font=DISPLAY, font_size=50, color=GROUND, weight=BOLD)
            chip_t.scale_to_fit_width(3.4)
            chip_t.move_to(chip_r)
            party_mobs.add(VGroup(chip_r, chip_t))

        req_arrow = Arrow(
            LEFT * 1.5, RIGHT * 1.5,
            buff=0, color=INK, stroke_width=5,
            max_tip_length_to_length_ratio=0.16,
        ).move_to(ORIGIN)
        req_lbl = Text("DETECTION REQUIRED", font=DISPLAY, font_size=50,
                       color=INK, weight=BOLD)
        req_lbl.scale_to_fit_width(4.8)
        req_lbl.next_to(req_arrow, UP, buff=0.22)

        self.play(FadeIn(party_mobs), run_time=0.6)
        self.wait(0.3)
        self.play(GrowArrow(req_arrow), FadeIn(req_lbl), run_time=0.7)
        self.wait(3.67)   # 0.6+0.3+0.7+3.67 = 5.27s


# ── S08 — requirement travels across frame and lands on THE SHAPE ──────────────
# Duration 5.03s  |  TERRA: the requirement arrow (same as S07)
class S08Scene(Scene):
    def construct(self):
        shape = _the_shape(label_font_size=80)
        shape.scale(0.62).move_to(RIGHT * 3.6)
        # INK fill + GROUND labels so the rect+text merge into one blob (avoids bbox-overlap)
        shape[0].set_fill(INK, opacity=1).set_stroke(width=0)
        shape[2].set_color(GROUND)
        shape[3].set_color(GROUND)
        self.add(shape)

        req_lbl = Text("DETECTION\nREQUIRED", font=DISPLAY, font_size=50,
                       color=INK, weight=BOLD, line_spacing=1.2)
        req_lbl.scale_to_fit_width(2.8)
        req_lbl.move_to(LEFT * 4.8)

        req_arrow = Arrow(
            LEFT * 3.0, shape.get_left() + LEFT * 0.05,
            buff=0.05, color=INK, stroke_width=5,
            max_tip_length_to_length_ratio=0.18,
        )

        self.play(FadeIn(req_lbl), run_time=0.4)
        self.play(GrowArrow(req_arrow), run_time=0.8)
        self.wait(3.83)   # 0.4+0.8+3.83 = 5.03s


# ── S09 — first mover ships; users flow to the unmarked rival ─────────────────
# Duration 5.59s  |  TERRA: the user-flow arrow
class S09Scene(Scene):
    def construct(self):
        def _provider(label, tag=None, pos=ORIGIN):
            box = RoundedRectangle(
                corner_radius=0.28, width=3.4, height=2.0,
                fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=2,
            ).move_to(pos)
            lbl = Text(label, font=DISPLAY, font_size=26, color=INK, weight=BOLD)
            lbl.move_to(box.get_center() + (UP * 0.3 if tag else ORIGIN))
            grp = VGroup(box, lbl)
            if tag:
                t = Text(tag, font=SERIF, font_size=20, color=INK)
                t.move_to(box.get_center() + DOWN * 0.35)
                grp.add(t)
            return grp

        a_grp = _provider("PROVIDER A", tag="+ detector", pos=LEFT * 4.2)
        b_grp = _provider("PROVIDER B", pos=RIGHT * 4.2)

        # Flow arrow (TERRA)
        flow = Arrow(
            LEFT * 2.2, RIGHT * 2.2,
            buff=0, color=TERRA, stroke_width=4,
            max_tip_length_to_length_ratio=0.10,
        ).move_to(ORIGIN + DOWN * 0.1)
        users_lbl = Text("users", font=SERIF, font_size=26, color=TERRA)
        users_lbl.next_to(flow, UP, buff=0.18)

        self.play(FadeIn(a_grp), FadeIn(b_grp), run_time=0.5)
        self.wait(0.3)
        self.play(GrowArrow(flow), FadeIn(users_lbl), run_time=0.6)
        self.play(a_grp.animate.scale(0.80).move_to(LEFT * 4.2), run_time=0.5)
        self.wait(3.69)   # 0.5+0.3+0.6+0.5+3.69 = 5.59s


# ── S10 — four providers wait; nobody steps forward ───────────────────────────
# Duration 5.61s  |  TERRA: the "FIRST?" label (unclaimed centre)
class S10Scene(Scene):
    def construct(self):
        positions = [
            LEFT * 3.8 + UP * 2.1,
            RIGHT * 3.8 + UP * 2.1,
            LEFT * 3.8 + DOWN * 2.1,
            RIGHT * 3.8 + DOWN * 2.1,
        ]
        providers = VGroup()
        for pos in positions:
            box = RoundedRectangle(
                corner_radius=0.22, width=2.8, height=1.4,
                fill_color=GROUND, fill_opacity=1, stroke_color=INK, stroke_width=2,
            ).move_to(pos)
            lbl = Text("ready", font=SERIF, font_size=24, color=INK)
            lbl.move_to(box.get_center())
            providers.add(VGroup(box, lbl))

        centre_q = Text("FIRST?", font=DISPLAY, font_size=52, color=TERRA, weight=BOLD)
        centre_q.move_to(ORIGIN)

        self.play(FadeIn(providers), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(centre_q), run_time=0.5)
        self.wait(4.11)   # 0.6+0.4+0.5+4.11 = 5.61s


# ── S11 — THE ONE FLAG (reported figures in dotted border) ─────────────────────
# Duration 10.39s  |  TERRA: the FLAG chip (the reel's only hedge marker)
class S11Scene(Scene):
    def construct(self):
        fig1 = Text("~96% accuracy", font=SERIF, font_size=58, color=INK)
        fig2 = Text("~30% would leave", font=SERIF, font_size=52, color=INK)
        figs = VGroup(fig1, fig2).arrange(DOWN, buff=0.75).move_to(ORIGIN + UP * 0.5)

        dashed_border = DashedVMobject(
            Rectangle(width=9.0, height=4.2, stroke_color=INK, stroke_width=2.5),
            num_dashes=44, dashed_ratio=0.6,
        ).move_to(ORIGIN + UP * 0.35)

        caption = Text("reported, not published", font=SERIF, font_size=30, color=INK)
        caption.next_to(dashed_border, DOWN, buff=0.38)

        # FLAG — solid INK chip, no TERRA (TERRA dot grid + dashed border are the accent)
        flag_rect = Rectangle(
            width=2.4, height=0.65,
            fill_color=INK, fill_opacity=1, stroke_width=0,
        )
        flag_txt = Text("FLAG", font=DISPLAY, font_size=26, color=GROUND, weight=BOLD)
        flag_txt.move_to(flag_rect)
        flag_grp = VGroup(flag_rect, flag_txt)
        flag_grp.move_to(dashed_border.get_corner(UL) + RIGHT * 1.45 + DOWN * 0.44)

        self.play(Create(dashed_border), run_time=0.8)
        self.play(FadeIn(figs, lag_ratio=0.5), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(flag_grp), run_time=0.5)
        self.wait(7.19)   # 0.8+0.9+0.5+0.5+0.5+7.19 = 10.39s


# ── S12 — figures fade; THE SHAPE remains unlabelled by any number ─────────────
# Duration 4.84s  |  TERRA: divider (from THE SHAPE)
class S12Scene(Scene):
    def construct(self):
        # Start with ghost of S11 (the numbers + dashed border)
        fig1 = Text("~96% accuracy", font=SERIF, font_size=58, color=INK)
        fig2 = Text("~30% would leave", font=SERIF, font_size=52, color=INK)
        figs = VGroup(fig1, fig2).arrange(DOWN, buff=0.75).move_to(ORIGIN + UP * 0.5)

        dashed_border = DashedVMobject(
            Rectangle(width=9.0, height=4.2, stroke_color=INK, stroke_width=2.5),
            num_dashes=44, dashed_ratio=0.6,
        ).move_to(ORIGIN + UP * 0.35)

        self.add(figs, dashed_border)

        # Numbers fade; THE SHAPE appears
        shape = _the_shape()
        self.play(FadeOut(figs), FadeOut(dashed_border), run_time=0.9)
        self.play(FadeIn(shape), run_time=0.6)
        self.wait(3.34)   # 0.9+0.6+3.34 = 4.84s


# ── S13 — THE ANCHOR RETURNS (same composition → widens to row of pages) ───────
# Duration 7.55s  |  TERRA: dot grid (same anchor accent as S03)
class S13Scene(Scene):
    def construct(self):
        page, magnifier, dots = _the_anchor()

        # Exact S03 composition
        self.play(FadeIn(page), run_time=0.4)
        self.play(Create(magnifier), run_time=0.5)
        self.play(FadeIn(dots), run_time=0.4)
        self.wait(1.0)

        # Widen: S03 elements fade, row of pages from different makers appears
        self.play(FadeOut(page), FadeOut(magnifier), FadeOut(dots), run_time=0.5)

        makers = ["A", "B", "C", "D"]
        all_pages = VGroup(*[_dotted_page(m) for m in makers])
        all_pages.arrange(RIGHT, buff=0.55).move_to(ORIGIN + DOWN * 0.1)

        self.play(FadeIn(all_pages, lag_ratio=0.3), run_time=1.2)
        self.wait(3.56)   # 0.4+0.5+0.4+1.0+0.5+1.2+3.56 = 7.55s (≈ 7.55)


# ── S14 — row of pages held; empty defector slot ─────────────────────────────
# Duration 6.40s  |  TERRA: dot grids on the filled pages
class S14Scene(Scene):
    def construct(self):
        makers = ["A", "B", "C", "D"]
        filled = VGroup(*[_dotted_page(m) for m in makers]).arrange(RIGHT, buff=0.55)

        empty_pg = Rectangle(
            width=2.2, height=2.8,
            fill_color=GROUND, fill_opacity=1,
            stroke_color=INK, stroke_width=1.5, stroke_opacity=0.4,
        )
        def_lbl = Text("defector?", font=SERIF, font_size=18, color=INK)
        def_lbl.next_to(empty_pg, DOWN, buff=0.14)
        empty_grp = VGroup(empty_pg, def_lbl)

        row = VGroup(filled, empty_grp).arrange(RIGHT, buff=0.55)
        row.move_to(ORIGIN + DOWN * 0.1)

        self.add(filled)
        self.play(FadeIn(empty_grp), run_time=0.6)
        self.wait(5.8)   # 0.6+5.8 = 6.4s


# ── shared: half-frame direction beat ─────────────────────────────────────────
def _direction_half(top_label, conclusion, cx, ink_strike=False):
    """Build one half of the S15/S16 direction layout centred on cx.
    ink_strike=True → grey faint strike (already-established).
    Returns (chip, arrow, conc, strike).
    """
    chip_r = RoundedRectangle(
        corner_radius=0.26, width=5.6, height=1.0,
        fill_color=INK, fill_opacity=1, stroke_width=0,
    ).move_to([cx, 2.4, 0])
    chip_t = Text(top_label, font=DISPLAY, font_size=28, color=GROUND, weight=BOLD)
    chip_t.scale_to_fit_width(5.2)
    chip_t.move_to(chip_r)
    chip = VGroup(chip_r, chip_t)

    arrow = Arrow(
        chip.get_bottom() + DOWN * 0.08,
        chip.get_bottom() + DOWN * 1.15,
        buff=0, color=INK, stroke_width=4,
        max_tip_length_to_length_ratio=0.25,
    )

    conc = Text(conclusion, font=DISPLAY, font_size=30, color=INK, weight=BOLD)
    conc.scale_to_fit_width(5.3)
    conc.move_to([cx, chip.get_bottom()[1] - 1.65, 0])

    # Rectangle strike — thick enough (≥35px) for type checker; covers x-height
    if ink_strike:
        strike = Rectangle(
            width=conc.width + 0.18, height=0.27,
            fill_color=INK, fill_opacity=0.22, stroke_width=0,
        ).move_to(conc.get_center())
    else:
        strike = Rectangle(
            width=conc.width + 0.18, height=0.27,
            fill_color=TERRA, fill_opacity=1, stroke_width=0,
        ).move_to(conc.get_center())

    return chip, arrow, conc, strike


# ── S15 — DIRECTION A: weak detector doesn't prove anyone chose it ─────────────
# Duration 6.21s  |  TERRA: the struck conclusion (SOMEONE CHOSE THIS)
class S15Scene(Scene):
    def construct(self):
        chip, arrow, conc, strike = _direction_half(
            "WEAK DETECTOR", "SOMEONE CHOSE THIS", cx=0.0
        )
        self.play(FadeIn(chip), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(conc), run_time=0.35)
        self.play(FadeIn(strike), run_time=0.55)
        self.wait(4.41)   # 0.4+0.5+0.35+0.55+4.41 = 6.21s


# ── S16 — DIRECTION B: both conclusions side by side ──────────────────────────
# Duration 8.26s  |  TERRA: the NEW right-side strike (one fresh accent)
# Left side shown in INK (established from S15); right side builds with TERRA strike.
class S16Scene(Scene):
    def construct(self):
        # Left (already established — INK faint strike)
        chip_l, arrow_l, conc_l, strike_l = _direction_half(
            "WEAK DETECTOR", "SOMEONE CHOSE THIS",
            cx=-3.2, ink_strike=True,
        )
        # Right (new — TERRA strike)
        chip_r, arrow_r, conc_r, strike_r = _direction_half(
            "REASONS ARE REAL", "SO NOTHING WAS CHOSEN",
            cx=3.2, ink_strike=False,
        )

        # Left side is already in frame (established)
        self.add(chip_l, arrow_l, conc_l, strike_l)

        # Build right side
        self.play(FadeIn(chip_r), run_time=0.4)
        self.play(GrowArrow(arrow_r), run_time=0.5)
        self.play(FadeIn(conc_r), run_time=0.35)
        self.play(Create(strike_r), run_time=0.55)
        self.wait(6.46)   # 0.4+0.5+0.35+0.55+6.46 = 8.26s
