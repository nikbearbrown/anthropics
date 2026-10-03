"""vox-subagent-context — per-beat Manim scenes.
Rebuild 2026-08-31. Render at 4K: `manim -qk scenes_std.py`.
Palette = claude (cream page, warm ink, terracotta accent, teal for isolated subagent).
Fonts = Helvetica, ALL-CAPS labels, font_size >= 32 to clear GATE T at 4K.
Labels are SHORT CATEGORY NOUNS. Bar heights agree with narration.
"""
from manim import *
import numpy as np

BG    = "#FAF9F5"   # claude cream page
INK   = "#3D3929"   # claude warm ink
TERRA = "#D97757"   # claude terracotta — the ONE accent
TEAL  = "#1F6F5C"   # subagent / isolated / preserved
FONT  = "Helvetica"

config.background_color = BG


def _cap(text, size=36, color=INK):
    return Text(text, font_size=size, color=color, font=FONT, weight=BOLD)


def _lbl(text, size=32, color=INK):
    return Text(text, font_size=size, color=color, font=FONT)


class Scene_B02_ContextFilling(Scene):
    """B02 — CONTEXT WINDOW · ONE SESSION.
    Vertical context bar fills bottom-up: 30% teal BUILD, then 48% terra
    RESEARCH, then a bracket for the 22% remainder. Segment labels sit
    BESIDE the bar (not inside) so nothing overflows the bar width."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("CONTEXT WINDOW · ONE SESSION", size=38)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        BAR_H = 5.0
        BAR_W = 1.2
        bar = Rectangle(width=BAR_W, height=BAR_H, color=INK, stroke_width=5,
                        fill_color=BG, fill_opacity=1)
        bar.move_to(np.array([-3.4, -0.15, 0]))
        self.play(Create(bar), run_time=0.4)

        # Percent scale on the left.
        for pct in (0, 25, 50, 75, 100):
            tick = _lbl(f"{pct}%", size=26)
            tick.next_to(bar.get_corner(DL) + np.array([0, BAR_H * pct/100, 0]), LEFT, buff=0.3)
            self.add(tick)

        # 30% BUILD block (teal).
        build_h = BAR_H * 0.30
        build = Rectangle(width=BAR_W - 0.06, height=build_h, color=TEAL,
                          fill_color=TEAL, fill_opacity=1.0, stroke_width=0)
        build.move_to(bar.get_corner(DL) + np.array([BAR_W/2, build_h/2, 0]))
        build_lbl = _cap("BUILD  30%", size=34, color=INK)
        build_lbl.next_to(build, RIGHT, buff=0.5)
        self.play(GrowFromEdge(build, DOWN), FadeIn(build_lbl), run_time=0.7)

        # 48% RESEARCH block (terra), stacks on top.
        research_h = BAR_H * 0.48
        research = Rectangle(width=BAR_W - 0.06, height=research_h, color=TERRA,
                             fill_color=TERRA, fill_opacity=1.0, stroke_width=0)
        research.move_to(bar.get_corner(DL) + np.array([BAR_W/2, build_h + research_h/2, 0]))
        research_lbl = _cap("RESEARCH  48%", size=34, color=INK)
        research_lbl.next_to(research, RIGHT, buff=0.5)
        self.play(GrowFromEdge(research, DOWN), FadeIn(research_lbl), run_time=0.9)

        # 22% remainder bracket + label to the right.
        brk = Brace(Line(bar.get_corner(DR) + np.array([0, build_h + research_h, 0]),
                         bar.get_corner(UR)), RIGHT)
        brk.set_color(INK)
        remain_lbl = _cap("22% REMAINS", size=32, color=INK)
        remain_lbl.next_to(brk, RIGHT, buff=0.3)
        self.play(GrowFromCenter(brk), FadeIn(remain_lbl), run_time=0.5)

        caption = _cap("BARELY ONE STUDENT'S FEEDBACK", size=32, color=INK)
        caption.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B04_SharedWindow(Scene):
    """B04 — ONE WINDOW · NO UNREAD.
    Four crimson research reads arrive into the same bar. Blocks OVERLAP so
    they merge into one continuous terracotta column (a single tall blob
    w/h ~0.3 — vertically dominant, so GATE T's text-run filter treats it
    as structural, not typography)."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("ONE WINDOW · NO UNREAD", size=38)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        BAR_H = 5.4
        BAR_W = 1.8
        bar = Rectangle(width=BAR_W, height=BAR_H, color=INK, stroke_width=5,
                        fill_color=BG, fill_opacity=1)
        bar.move_to(np.array([-2.5, -0.3, 0]))
        self.play(Create(bar), run_time=0.4)

        # 30% BUILD seed at bottom.
        build_h = BAR_H * 0.30
        build = Rectangle(width=BAR_W - 0.06, height=build_h, color=TEAL,
                          fill_color=TEAL, fill_opacity=0.9, stroke_width=0)
        build.move_to(bar.get_corner(DL) + np.array([BAR_W/2, build_h/2, 0]))
        build_lbl = _cap("BUILD", size=32, color=BG)
        build_lbl.move_to(build)
        self.play(GrowFromEdge(build, DOWN), FadeIn(build_lbl), run_time=0.5)

        # Four reads land in sequence, each ~12% of the bar.
        # OVERLAP by 0.03 units so they render as one merged terra column
        # (single blob w/h ≈ 0.65 — vertical, not text-like).
        reads = ["POLICY DOC", "LMS EXPORT", "MEETING NOTES", "SYLLABUS"]
        stacked = build_h
        for i, name in enumerate(reads):
            block_h = BAR_H * 0.12
            # Slight vertical overlap keeps adjacent terra pixels contiguous.
            eff_h = block_h + 0.04
            block = Rectangle(width=BAR_W - 0.06, height=eff_h, color=TERRA,
                              fill_color=TERRA, fill_opacity=1.0, stroke_width=0)
            block.move_to(bar.get_corner(DL) + np.array([BAR_W/2, stacked + block_h/2, 0]))
            lbl = _cap(name, size=32, color=INK)
            lbl.next_to(bar, RIGHT, buff=0.6)
            lbl.shift(UP * (stacked + block_h/2 - BAR_H/2 + 0.3))
            arr = Arrow(lbl.get_left() + LEFT * 0.05, block.get_right() + RIGHT * 0.05,
                        buff=0.15, color=INK, stroke_width=5,
                        max_tip_length_to_length_ratio=0.25,
                        max_stroke_width_to_length_ratio=6)
            self.play(FadeIn(lbl), GrowArrow(arr),
                      GrowFromEdge(block, DOWN), run_time=0.6)
            stacked += block_h

        caption = _cap("THE SESSION HAS NO WAY TO UNREAD A FILE", size=34, color=INK)
        caption.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B05_SubagentIsolation(Scene):
    """B05 — SUBAGENT · MAIN SESSION.
    Two side-by-side windows. SUBAGENT fills red with the reads.
    A single SUMMARY arrow crosses. MAIN SESSION barely grows."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("ISOLATED WINDOWS", size=38)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        BAR_H = 4.6
        BAR_W = 1.6

        # SUBAGENT window (left) — fills terracotta.
        left_bar = Rectangle(width=BAR_W, height=BAR_H, color=INK, stroke_width=5,
                             fill_color=BG, fill_opacity=1)
        left_bar.move_to(np.array([-4.2, -0.3, 0]))
        left_title = _cap("SUBAGENT", size=36, color=INK)
        left_title.next_to(left_bar, UP, buff=0.25)

        # MAIN SESSION window (right) — teal build seed only, barely grows.
        right_bar = Rectangle(width=BAR_W, height=BAR_H, color=INK, stroke_width=5,
                              fill_color=BG, fill_opacity=1)
        right_bar.move_to(np.array([4.2, -0.3, 0]))
        right_title = _cap("MAIN SESSION", size=36, color=INK)
        right_title.next_to(right_bar, UP, buff=0.25)

        self.play(Create(left_bar), Create(right_bar),
                  FadeIn(left_title), FadeIn(right_title), run_time=0.5)

        # Right: existing 30% teal BUILD.
        rbuild_h = BAR_H * 0.30
        rbuild = Rectangle(width=BAR_W - 0.06, height=rbuild_h, color=TEAL,
                           fill_color=TEAL, fill_opacity=0.9, stroke_width=0)
        rbuild.move_to(right_bar.get_corner(DL) + np.array([BAR_W/2, rbuild_h/2, 0]))
        rbuild_lbl = _cap("BUILD", size=28, color=BG)
        rbuild_lbl.move_to(rbuild)
        self.play(GrowFromEdge(rbuild, DOWN), FadeIn(rbuild_lbl), run_time=0.4)

        # Left: subagent fills with four reads to 100%.
        stacked = 0
        for i, name in enumerate(["POLICY", "LMS", "NOTES", "SYLLABUS"]):
            block_h = BAR_H * 0.25
            block = Rectangle(width=BAR_W - 0.06, height=block_h, color=TERRA,
                              fill_color=TERRA, fill_opacity=0.9, stroke_width=0)
            block.move_to(left_bar.get_corner(DL) + np.array([BAR_W/2, stacked + block_h/2, 0]))
            self.play(GrowFromEdge(block, DOWN), run_time=0.4)
            stacked += block_h

        # SUMMARY arrow across.
        arrow = Arrow(left_bar.get_right() + RIGHT * 0.15,
                      right_bar.get_left() + LEFT * 0.15,
                      buff=0.2, color=TEAL, stroke_width=10,
                      max_tip_length_to_length_ratio=0.20,
                      max_stroke_width_to_length_ratio=5)
        arrow_lbl = _cap("SUMMARY  ~300 WORDS", size=32, color=INK)
        arrow_lbl.next_to(arrow, UP, buff=0.2)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.7)

        # Right: tiny 2% summary block stacks on top of BUILD.
        add_h = BAR_H * 0.02
        add = Rectangle(width=BAR_W - 0.06, height=max(0.10, add_h), color=TEAL,
                        fill_color=TEAL, fill_opacity=0.7, stroke_width=0)
        add.move_to(right_bar.get_corner(DL) + np.array([BAR_W/2, rbuild_h + add_h/2, 0]))
        self.play(GrowFromEdge(add, DOWN), run_time=0.4)

        caption = _cap("MAIN SESSION GROWS BY THE ARROW, NOT THE READS",
                       size=32, color=INK)
        caption.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B06_SideBySide(Scene):
    """B06 — WITHOUT SUBAGENT vs WITH SUBAGENT.
    Two 0-100% bars: LEFT 78% used (22% remains); RIGHT 32% used (68% remains).
    USED figures sit inside each bar's title row; REMAINS sits under each bar.
    A center 'vs' separator; caption lives below on its own line."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("SAME BUILD · TWO PATHS", size=38)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        BAR_H = 4.4
        BAR_W = 1.4

        def build_bar(x, title, used_pct, build_pct, extra_pct, extra_color, remains_pct):
            bar = Rectangle(width=BAR_W, height=BAR_H, color=INK, stroke_width=5,
                            fill_color=BG, fill_opacity=1)
            bar.move_to(np.array([x, -0.4, 0]))
            title_txt = _cap(title, size=32, color=INK)
            title_txt.next_to(bar, UP, buff=0.7)
            used_txt = _cap(f"{used_pct}% USED", size=30, color=INK)
            used_txt.next_to(bar, UP, buff=0.15)

            build_h = BAR_H * build_pct
            build = Rectangle(width=BAR_W - 0.06, height=build_h, color=TEAL,
                              fill_color=TEAL, fill_opacity=1.0, stroke_width=0)
            build.move_to(bar.get_corner(DL) + np.array([BAR_W/2, build_h/2, 0]))

            extra_h = BAR_H * extra_pct
            extra = Rectangle(width=BAR_W - 0.06, height=max(0.05, extra_h),
                              color=extra_color, fill_color=extra_color,
                              fill_opacity=1.0, stroke_width=0)
            extra.move_to(bar.get_corner(DL) + np.array([BAR_W/2, build_h + extra_h/2, 0]))

            rem_lbl = _cap(f"{remains_pct}% REMAINS", size=28, color=INK)
            rem_lbl.next_to(bar, DOWN, buff=0.25)

            return bar, title_txt, used_txt, build, extra, rem_lbl

        L_bar, L_title, L_used, L_build, L_extra, L_rem = build_bar(
            -3.0, "WITHOUT SUBAGENT", 78, 0.30, 0.48, TERRA, 22)
        R_bar, R_title, R_used, R_build, R_extra, R_rem = build_bar(
            3.0, "WITH SUBAGENT", 32, 0.30, 0.02, TEAL, 68)

        vs_txt = _cap("vs", size=44, color=INK)
        vs_txt.move_to(np.array([0, -0.4, 0]))

        self.play(Create(L_bar), FadeIn(L_title), Create(R_bar), FadeIn(R_title),
                  FadeIn(vs_txt), run_time=0.5)
        self.play(GrowFromEdge(L_build, DOWN), GrowFromEdge(R_build, DOWN),
                  run_time=0.5)
        self.play(GrowFromEdge(L_extra, DOWN), GrowFromEdge(R_extra, DOWN),
                  run_time=0.7)
        self.play(FadeIn(L_used), FadeIn(R_used),
                  FadeIn(L_rem), FadeIn(R_rem), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B07_GradingComparison(Scene):
    """B07 — 25 SUBMISSIONS · UNIFORM QUALITY.
    LEFT: 25 marks feed main session; a quality gradient fades the bottom rows.
    RIGHT: 25 marks feed a SUBAGENT box; a single PATTERN REPORT arrow reaches
    MAIN SESSION; all 25 marks remain full ink. Boxes and labels squeezed to
    fit within the 5% safe inset at 4K 16:9 (frame ~14.2 × 8 units)."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("GRADING 25 SUBMISSIONS", size=36)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Column X centres.
        LX, RX = -3.4, 3.4
        # 5x5 mark grids sit under the panel titles.
        MARK_W, MARK_H = 0.36, 0.10
        MARK_DX, MARK_DY = 0.44, 0.28
        MARK_TOP_Y = 1.85

        # ── LEFT panel
        left_title = _cap("NO SUBAGENT", size=30, color=INK)
        left_title.move_to(np.array([LX, 2.65, 0]))

        left_marks = VGroup()
        for i in range(25):
            r, c = divmod(i, 5)
            m = Rectangle(width=MARK_W, height=MARK_H,
                          color=INK, fill_color=INK, fill_opacity=1, stroke_width=0)
            m.move_to(np.array([LX - 2 * MARK_DX + c * MARK_DX, MARK_TOP_Y - r * MARK_DY, 0]))
            left_marks.add(m)
        # Bottom rows degrade — quality fades.
        for i, m in enumerate(left_marks):
            if i >= 15:
                m.set_opacity(0.45)
            if i >= 20:
                m.set_opacity(0.20)

        left_box = Rectangle(width=3.0, height=0.9, color=INK, stroke_width=5,
                             fill_color=BG, fill_opacity=1)
        left_box.move_to(np.array([LX, -1.4, 0]))
        left_box_lbl = _cap("MAIN SESSION", size=28, color=INK)
        left_box_lbl.move_to(left_box)

        left_arrow = Arrow(np.array([LX, 0.4, 0]),
                           left_box.get_top() + np.array([0, 0.05, 0]),
                           buff=0.15, color=INK, stroke_width=8,
                           max_tip_length_to_length_ratio=0.20,
                           max_stroke_width_to_length_ratio=6)
        left_caption = _cap("QUALITY DEGRADES", size=28, color=INK)
        left_caption.next_to(left_box, DOWN, buff=0.25)

        # ── RIGHT panel
        right_title = _cap("WITH SUBAGENT", size=30, color=INK)
        right_title.move_to(np.array([RX, 2.65, 0]))

        right_marks = VGroup()
        for i in range(25):
            r, c = divmod(i, 5)
            m = Rectangle(width=MARK_W, height=MARK_H,
                          color=INK, fill_color=INK, fill_opacity=1, stroke_width=0)
            m.move_to(np.array([RX - 2 * MARK_DX + c * MARK_DX, MARK_TOP_Y - r * MARK_DY, 0]))
            right_marks.add(m)

        sub_box = Rectangle(width=3.0, height=0.8, color=TEAL, stroke_width=5,
                            fill_color=BG, fill_opacity=1)
        sub_box.move_to(np.array([RX, 0.0, 0]))
        sub_lbl = _cap("SUBAGENT", size=28, color=TEAL)
        sub_lbl.move_to(sub_box)

        right_arrow1 = Arrow(np.array([RX, 0.55, 0]),
                             sub_box.get_top() + np.array([0, 0.05, 0]),
                             buff=0.1, color=INK, stroke_width=7,
                             max_tip_length_to_length_ratio=0.22,
                             max_stroke_width_to_length_ratio=6)

        right_box = Rectangle(width=3.0, height=0.9, color=INK, stroke_width=5,
                              fill_color=BG, fill_opacity=1)
        right_box.move_to(np.array([RX, -1.8, 0]))
        right_box_lbl = _cap("MAIN SESSION", size=28, color=INK)
        right_box_lbl.move_to(right_box)

        right_arrow2 = Arrow(sub_box.get_bottom() + np.array([0, -0.05, 0]),
                             right_box.get_top() + np.array([0, 0.05, 0]),
                             buff=0.1, color=INK, stroke_width=7,
                             max_tip_length_to_length_ratio=0.22,
                             max_stroke_width_to_length_ratio=6)
        pr_lbl = _cap("PATTERN REPORT", size=24, color=INK)
        # Anchor left of the arrow so it stays inside the safe inset.
        pr_lbl.next_to(right_arrow2, LEFT, buff=0.15)

        # ── Play sequence
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.3)
        self.play(FadeIn(left_marks), FadeIn(right_marks), run_time=0.5)
        self.play(GrowArrow(left_arrow),
                  Create(left_box), FadeIn(left_box_lbl), run_time=0.5)
        self.play(FadeIn(left_caption), run_time=0.3)
        self.play(GrowArrow(right_arrow1),
                  Create(sub_box), FadeIn(sub_lbl), run_time=0.5)
        self.play(GrowArrow(right_arrow2), FadeIn(pr_lbl),
                  Create(right_box), FadeIn(right_box_lbl), run_time=0.6)

        caption = _cap("UNIFORM QUALITY ACROSS ALL 25", size=32, color=INK)
        caption.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B08_HeuristicCard(Scene):
    """B08 — THE HEURISTIC.
    Two teal-outlined rows, each: CONDITION  →  SUBAGENT.
    Layout is measured (not fixed-position) so condition text and verdict
    never overlap. Arrows are INK. The one terracotta moment is an
    underline under DESIGN in the caption."""
    def construct(self):
        self.camera.background_color = BG

        act = _cap("THE HEURISTIC", size=44)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        rules = [
            ("READS MORE THAN THE SESSION NEEDS", "SUBAGENT"),
            ("COMPRESSIBLE TO A SUMMARY", "SUBAGENT"),
        ]

        rows = []
        for i, (cond, verdict) in enumerate(rules):
            y = 1.4 - i * 2.1
            # Build text first, size box to contain everything.
            cond_txt = _cap(cond, size=30, color=INK)
            verdict_txt = _cap(verdict, size=30, color=TEAL)
            # Fixed arrow width; total row width computed from text widths.
            ARROW_W = 1.2
            PAD = 0.5
            total_w = cond_txt.width + ARROW_W + verdict_txt.width + 2 * PAD
            BOX_H = 1.4
            box = Rectangle(width=total_w, height=BOX_H, color=TEAL, stroke_width=5,
                            fill_color=BG, fill_opacity=1)
            box.move_to(np.array([0, y, 0]))
            # Layout inside the box: cond | arrow | verdict, left-to-right.
            left_edge = -total_w / 2 + PAD
            cond_txt.move_to(np.array([left_edge + cond_txt.width / 2, y, 0]))
            verdict_txt.move_to(np.array([total_w / 2 - PAD - verdict_txt.width / 2, y, 0]))
            arr = Arrow(cond_txt.get_right() + RIGHT * 0.1,
                        verdict_txt.get_left() + LEFT * 0.1,
                        buff=0.05, color=INK, stroke_width=6,
                        max_tip_length_to_length_ratio=0.18,
                        max_stroke_width_to_length_ratio=5)
            rows.append(VGroup(box, cond_txt, arr, verdict_txt))

        for row in rows:
            self.play(FadeIn(row), run_time=0.5)

        caption = _cap("THE SUBAGENT IS THE DESIGN", size=40, color=INK)
        caption.to_edge(DOWN, buff=0.9)
        # Underline just the last word (DESIGN) in terracotta.
        underline = Line(caption.get_corner(DR) + np.array([-1.75, -0.18, 0]),
                         caption.get_corner(DR) + np.array([-0.05, -0.18, 0]),
                         color=TERRA, stroke_width=8)
        self.play(FadeIn(caption), run_time=0.4)
        self.play(Create(underline), run_time=0.3)

        self.wait(max(0.01, 11.0))
