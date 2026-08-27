"""
scenes.py — Manim graphics for claude-liam-simple-secret-key.

Palette: GROUND=#FAF9F5 (cream)  INK=#3D3929 (warm ink)  TERRA=#D97757 (terracotta)
Rule: exactly ONE terracotta accent per beat. No gradients. No gloss.

S03 + S14 are THE ANCHOR PAIR — identical composition, only the verdict mark changes.
S05 + S06 are ONE SPLIT-PANEL; S06 holds S05's final frame.
S15 + S16 are MIRRORED HALVES of one structure.
S11 carries the reel's ONLY inference FLAG (terracotta marker).

Render all:
  cd anthropics/youtube/claude-liam-simple-secret-key
  bash render_scenes.sh
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTED  = "#9A8E7A"   # secondary / greyed — never an accent colour
FAINT  = "#D8D0C2"   # very light ink for blank / placeholder elements

config.background_color = GROUND
DISP = "Montserrat"
BODY = "EB Garamond"
MONO = "PT Mono"


# ─────────────────────────────────────────── shared anchor geometry ───────

def _make_paper():
    """Paper document — shared by S03 and S14. Positioned at LEFT zone."""
    paper = RoundedRectangle(corner_radius=0.05, width=2.8, height=3.6,
                              fill_color=WHITE, fill_opacity=1,
                              stroke_color=INK, stroke_width=2)
    paper.shift(LEFT * 2.8)
    lines = VGroup(*[
        Line(LEFT * 0.95, RIGHT * 0.95, stroke_color=FAINT, stroke_width=1.2)
        for _ in range(8)
    ])
    lines.arrange(DOWN, buff=0.28)
    lines.move_to(paper.get_center() + DOWN * 0.25)
    return VGroup(paper, lines)


def _make_table():
    """Empty committee table + chairs — shared by S03 and S14. RIGHT zone."""
    table = Ellipse(width=3.4, height=1.7,
                    fill_color=GROUND, fill_opacity=1,
                    stroke_color=INK, stroke_width=2)
    table.shift(RIGHT * 2.8)
    chairs = VGroup()
    for i, cx in enumerate([-0.9, 0, 0.9]):
        for cy_off, row_off in [(1.2, 0), (-1.2, 0)]:
            c = Rectangle(width=0.46, height=0.36,
                          fill_color=GROUND, fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
            c.move_to(table.get_center() + np.array([cx, cy_off, 0]))
            chairs.add(c)
    return VGroup(table, chairs)


def _make_verdict_mark(terra_label: str):
    """Terracotta verdict mark at fixed position on paper. Text-only — no fill rectangle."""
    txt = Text(terra_label, font=DISP, weight="BOLD", font_size=52, color=TERRA)
    txt.move_to(LEFT * 2.8 + UP * 0.55)
    rule = Line(txt.get_left(), txt.get_right(), stroke_color=TERRA, stroke_width=3)
    rule.next_to(txt, DOWN, buff=0.10)
    return VGroup(txt, rule)


# ──────────────────────────────────────────── scene classes ───────────────

class S01_VerdictCard(Scene):
    """A detector says AI wrote this. There is no way for you to check that. ~4.4s"""
    def construct(self):
        verdict = Text("DETECTED", font=DISP, weight="BOLD",
                       font_size=80, color=INK)
        verdict.shift(LEFT * 2.5)

        # TERRA = the one accent: underline rule on verdict
        rule = Line(verdict.get_left(), verdict.get_right(),
                    stroke_color=TERRA, stroke_width=5)
        rule.next_to(verdict, DOWN, buff=0.18)

        # Flat boundary — no seam, no opening
        boundary = Line(UP * 3.8, DOWN * 3.8, stroke_color=INK, stroke_width=3)
        boundary.shift(RIGHT * 2.0)

        # Viewer's hand/arrow stopped at boundary
        reach = Arrow(LEFT * 1.0, LEFT * 0.08, color=MUTED,
                      stroke_width=2.5, tip_length=0.25, buff=0)
        reach.shift(RIGHT * 1.6)

        lbl = Text("no way in", font=BODY, font_size=26, color=MUTED)
        lbl.next_to(boundary, RIGHT, buff=0.35)

        self.play(Write(verdict), run_time=0.5)
        self.play(Create(rule), run_time=0.3)
        self.play(Create(boundary), run_time=0.4)
        self.play(GrowArrow(reach), run_time=0.5)
        self.play(FadeIn(lbl), run_time=0.3)
        self.wait(2.3)


class S02_ThreeLockedOut(Scene):
    """Three parties locked out, one inside with the key. ~6.9s"""
    def construct(self):
        # Vertical boundary
        wall = Line(UP * 3.8, DOWN * 3.8, stroke_color=INK, stroke_width=3)
        wall.shift(RIGHT * 0.2)

        # Left: three locked-out parties
        labels_left = ["YOU", "UNIVERSITY", "COURT"]
        left_group = VGroup()
        for lbl in labels_left:
            t = Text(lbl, font=DISP, weight="BOLD", font_size=34, color=INK)
            # lock glyph
            lock = Square(side_length=0.28, fill_color=MUTED, fill_opacity=0.4,
                          stroke_color=MUTED, stroke_width=1.5)
            lock.next_to(t, LEFT, buff=0.22)
            left_group.add(VGroup(lock, t))
        left_group.arrange(DOWN, buff=0.55)
        left_group.shift(LEFT * 2.6)

        # Right: provider with key (INK) + TERRA underline accent
        provider_lbl = Text("PROVIDER", font=DISP, weight="BOLD",
                            font_size=34, color=INK)
        # TERRA accent: thin underline under PROVIDER label
        provider_rule = Line(provider_lbl.get_left(), provider_lbl.get_right(),
                             stroke_color=TERRA, stroke_width=4)
        provider_rule.next_to(provider_lbl, DOWN, buff=0.12)
        # Key shape (INK — structural, not the accent)
        key_circle = Circle(radius=0.22, fill_color=INK,
                            fill_opacity=1, stroke_width=0)
        key_shaft  = Rectangle(width=0.55, height=0.14,
                               fill_color=INK, fill_opacity=1, stroke_width=0)
        key_shaft.next_to(key_circle, RIGHT, buff=-0.1)
        key_tooth  = Rectangle(width=0.12, height=0.18,
                               fill_color=INK, fill_opacity=1, stroke_width=0)
        key_tooth.next_to(key_shaft, DOWN + RIGHT, buff=-0.35, aligned_edge=RIGHT)
        key = VGroup(key_circle, key_shaft, key_tooth)
        key.next_to(provider_rule, DOWN, buff=0.3)
        right_group = VGroup(provider_lbl, provider_rule, key)
        right_group.shift(RIGHT * 2.6)

        self.play(Create(wall), run_time=0.4)
        self.play(LaggedStart(
            *[FadeIn(g, shift=RIGHT * 0.1) for g in left_group],
            lag_ratio=0.25, run_time=1.2))
        self.play(FadeIn(provider_lbl, shift=LEFT * 0.1), run_time=0.5)
        self.play(Create(provider_rule), run_time=0.3)
        self.play(FadeIn(key, scale=1.15), run_time=0.5)
        self.wait(4.0)



class S03_AnchorPlanted(Scene):
    """THE ANCHOR — flagged paper, empty committee table. ~5.6s"""
    def construct(self):
        paper  = _make_paper()
        stamp  = _make_verdict_mark("FLAGGED")   # TERRA accent
        table  = _make_table()

        self.play(FadeIn(paper), run_time=0.5)
        self.play(FadeIn(stamp, scale=1.1), run_time=0.5)
        self.play(FadeIn(table), run_time=0.6)
        self.wait(4.0)


class S04_WrongGuess(Scene):
    """The natural assumption: watermark is a signature everyone can verify. ~7.9s"""
    def construct(self):
        # Padlock (anyone's mental model of 'verified')
        lock_body = RoundedRectangle(corner_radius=0.1, width=1.2, height=1.0,
                                      fill_color=FAINT, fill_opacity=1,
                                      stroke_color=INK, stroke_width=2)
        lock_arch  = Arc(radius=0.38, start_angle=0, angle=PI,
                         stroke_color=INK, stroke_width=2)
        lock_arch.next_to(lock_body, UP, buff=-0.18)
        padlock = VGroup(lock_arch, lock_body)
        padlock.shift(LEFT * 4.0)

        # Certificate
        cert = RoundedRectangle(corner_radius=0.08, width=2.0, height=2.6,
                                 fill_color=WHITE, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2)
        # INK header on certificate (structural — not the accent)
        cert_hdr = Rectangle(width=2.0, height=0.45,
                             fill_color=INK, fill_opacity=1, stroke_width=0)
        cert_hdr.move_to(cert.get_top() + DOWN * 0.225)
        cert_lbl = Text("CERTIFICATE", font=DISP, weight="BOLD",
                        font_size=18, color=GROUND)
        cert_lbl.move_to(cert_hdr.get_center())
        # TERRA accent: thin rule at bottom of certificate
        cert_rule = Line(cert.get_left() + RIGHT * 0.1,
                         cert.get_right() + LEFT * 0.1,
                         stroke_color=TERRA, stroke_width=3)
        cert_rule.move_to(cert.get_bottom() + UP * 0.14)
        cert_grp = VGroup(cert, cert_hdr, cert_lbl, cert_rule)
        cert_grp.shift(LEFT * 1.5)

        # Green public tick
        tick = Text("✓", font=DISP, font_size=72, color="#2A7A3B")
        tick.shift(RIGHT * 1.2)

        # Three small viewers
        viewers = VGroup()
        for dx in [-0.6, 0, 0.6]:
            dot = Dot(radius=0.14, color=INK)
            dot.shift(RIGHT * (3.2 + dx) + DOWN * 0.3)
            viewers.add(dot)

        # Arrows from tick to each viewer
        arrows = VGroup(*[
            Arrow(tick.get_right(), v.get_left(), stroke_width=1.5,
                  tip_length=0.16, color=MUTED, buff=0.05)
            for v in viewers
        ])

        self.play(FadeIn(padlock), run_time=0.4)
        self.play(FadeIn(cert_grp), run_time=0.5)
        self.play(Write(tick), run_time=0.4)
        self.play(FadeIn(viewers), run_time=0.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.2, run_time=0.9))
        self.wait(5.4)


class S05_SplitPanel(Scene):
    """Same announcement: images got open signature, text got secret key. ~10.8s"""
    def construct(self):
        # Header
        hdr = Text("same announcement", font=BODY, font_size=32, color=MUTED)
        hdr.to_edge(UP, buff=0.55)
        div = Line(hdr.get_left(), hdr.get_right(),
                   stroke_color=MUTED, stroke_width=1)
        div.next_to(hdr, DOWN, buff=0.18)

        # Left panel: IMAGE → OPEN STANDARD → public tick
        left_bg = Rectangle(width=3.2, height=5.0, fill_color=WHITE,
                             fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        left_bg.shift(LEFT * 2.7 + DOWN * 0.4)

        img_icon = Square(side_length=0.7, fill_color=FAINT, fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
        img_icon.move_to(left_bg.get_center() + UP * 1.5)

        badge = RoundedRectangle(corner_radius=0.12, width=2.0, height=0.52,
                                  fill_color=FAINT, fill_opacity=1,
                                  stroke_color=INK, stroke_width=1.5)
        badge.move_to(left_bg.get_center() + UP * 0.5)
        badge_lbl = Text("OPEN STANDARD", font=DISP, weight="BOLD",
                         font_size=18, color=INK)
        badge_lbl.move_to(badge.get_center())
        badge_grp = VGroup(badge, badge_lbl)

        tick = Text("✓", font=DISP, font_size=64, color="#2A7A3B")
        tick.move_to(left_bg.get_center() + DOWN * 0.7)
        pub_lbl = Text("public", font=BODY, font_size=26, color=INK)
        pub_lbl.next_to(tick, DOWN, buff=0.1)

        left_panel = VGroup(left_bg, img_icon, badge_grp, tick, pub_lbl)

        # Right panel: TEXT BLOCK → SEALED KEY → "API — LATER" (TERRA)
        right_bg = Rectangle(width=3.2, height=5.0, fill_color=WHITE,
                              fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        right_bg.shift(RIGHT * 2.7 + DOWN * 0.4)

        txt_lines = VGroup(*[
            Line(LEFT * 1.0, RIGHT * 1.0, stroke_color=FAINT, stroke_width=1.5)
            for _ in range(4)
        ])
        txt_lines.arrange(DOWN, buff=0.3)
        txt_lines.move_to(right_bg.get_center() + UP * 1.4)

        # Sealed key icon (circle + shaft, muted = locked/secret)
        key_c = Circle(radius=0.22, fill_color=MUTED, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.5, height=0.13, fill_color=MUTED, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.1)
        key_t = Rectangle(width=0.12, height=0.17, fill_color=MUTED, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.35, aligned_edge=RIGHT)
        sealed_key = VGroup(key_c, key_s, key_t)
        sealed_key.move_to(right_bg.get_center() + UP * 0.3)

        # TERRA accent: large "API — LATER" text (the one accent for this beat)
        api_lbl = Text("API — LATER", font=DISP, weight="BOLD",
                       font_size=36, color=TERRA)
        api_lbl.move_to(right_bg.get_center() + DOWN * 0.85)

        right_panel = VGroup(right_bg, txt_lines, sealed_key, api_lbl)

        # Divider between panels
        mid_div = Line(UP * 2.4, DOWN * 3.8, stroke_color=INK, stroke_width=1.5)

        self.play(FadeIn(hdr), Create(div), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(right_bg), Create(mid_div), run_time=0.4)
        self.play(FadeIn(img_icon), FadeIn(txt_lines), run_time=0.5)
        self.play(FadeIn(badge_grp), FadeIn(sealed_key), run_time=0.5)
        self.play(Write(tick), FadeIn(pub_lbl), run_time=0.5)
        self.play(FadeIn(api_lbl), run_time=0.5)
        self.wait(8.0)   # hold the comparison


class S06_HoldFrame(Scene):
    """If text watermarks were signatures, they would have used a signature. ~4.1s
    Holds S05's final frame. One side has a public tick; the other does not."""
    def construct(self):
        # Reproduce S05's final composition statically ─ same objects, no animation
        hdr = Text("same announcement", font=BODY, font_size=32, color=MUTED)
        hdr.to_edge(UP, buff=0.55)
        div = Line(hdr.get_left(), hdr.get_right(),
                   stroke_color=MUTED, stroke_width=1)
        div.next_to(hdr, DOWN, buff=0.18)

        left_bg  = Rectangle(width=3.2, height=5.0, fill_color=WHITE,
                              fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        left_bg.shift(LEFT * 2.7 + DOWN * 0.4)
        img_icon = Square(side_length=0.7, fill_color=FAINT, fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
        img_icon.move_to(left_bg.get_center() + UP * 1.5)
        badge = RoundedRectangle(corner_radius=0.12, width=2.0, height=0.52,
                                  fill_color=FAINT, fill_opacity=1,
                                  stroke_color=INK, stroke_width=1.5)
        badge.move_to(left_bg.get_center() + UP * 0.5)
        badge_lbl = Text("OPEN STANDARD", font=DISP, weight="BOLD",
                         font_size=18, color=INK)
        badge_lbl.move_to(badge.get_center())
        tick = Text("✓", font=DISP, font_size=64, color="#2A7A3B")
        tick.move_to(left_bg.get_center() + DOWN * 0.7)
        pub_lbl = Text("public", font=BODY, font_size=26, color=INK)
        pub_lbl.next_to(tick, DOWN, buff=0.1)

        right_bg = Rectangle(width=3.2, height=5.0, fill_color=WHITE,
                              fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        right_bg.shift(RIGHT * 2.7 + DOWN * 0.4)
        txt_lines = VGroup(*[
            Line(LEFT * 1.0, RIGHT * 1.0, stroke_color=FAINT, stroke_width=1.5)
            for _ in range(4)
        ])
        txt_lines.arrange(DOWN, buff=0.3)
        txt_lines.move_to(right_bg.get_center() + UP * 1.4)
        key_c  = Circle(radius=0.22, fill_color=MUTED, fill_opacity=1, stroke_width=0)
        key_s  = Rectangle(width=0.5, height=0.13, fill_color=MUTED, fill_opacity=1,
                            stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.1)
        key_t  = Rectangle(width=0.12, height=0.17, fill_color=MUTED, fill_opacity=1,
                            stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.35, aligned_edge=RIGHT)
        sealed_key = VGroup(key_c, key_s, key_t)
        sealed_key.move_to(right_bg.get_center() + UP * 0.3)
        api_lbl = Text("API — LATER", font=DISP, weight="BOLD",
                       font_size=36, color=TERRA)
        api_lbl.move_to(right_bg.get_center() + DOWN * 0.85)
        mid_div = Line(UP * 2.4, DOWN * 3.8, stroke_color=INK, stroke_width=1.5)

        # Instantaneous reveal of the frozen S05 frame
        self.add(hdr, div, left_bg, right_bg, mid_div,
                 img_icon, VGroup(badge, badge_lbl), tick, pub_lbl,
                 txt_lines, sealed_key, api_lbl)
        self.wait(4.1)


class S07_OneKeyTwoJobs(Scene):
    """The watermark key does two jobs at once. ~4.0s"""
    def construct(self):
        # Central key
        key_c = Circle(radius=0.32, fill_color=INK, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.72, height=0.18, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.12)
        key_t = Rectangle(width=0.16, height=0.24, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.48, aligned_edge=RIGHT)
        key = VGroup(key_c, key_s, key_t)
        key.move_to(ORIGIN + UP * 0.3)

        # WRITE arrow (left-down)
        write_arrow = Arrow(key.get_bottom() + LEFT * 0.3,
                            LEFT * 2.6 + DOWN * 1.8,
                            color=MUTED, stroke_width=2.5,
                            tip_length=0.28, buff=0.1)
        write_lbl = Text("WRITE", font=DISP, weight="BOLD",
                         font_size=36, color=MUTED)
        write_lbl.next_to(write_arrow.get_end(), DOWN, buff=0.2)

        # READ arrow — TERRA (the detection path, the one accent)
        read_arrow = Arrow(key.get_bottom() + RIGHT * 0.3,
                           RIGHT * 2.6 + DOWN * 1.8,
                           color=TERRA, stroke_width=2.5,
                           tip_length=0.28, buff=0.1)
        read_lbl = Text("READ", font=DISP, weight="BOLD",
                        font_size=36, color=TERRA)
        read_lbl.next_to(read_arrow.get_end(), DOWN, buff=0.2)

        self.play(FadeIn(key, scale=1.1), run_time=0.4)
        self.play(GrowArrow(write_arrow), FadeIn(write_lbl), run_time=0.5)
        self.play(GrowArrow(read_arrow), FadeIn(read_lbl), run_time=0.5)
        self.wait(2.6)


class S08_WriteThenRead(Scene):
    """Key seeds a nudge during writing; same key re-counts during reading. ~7.9s"""
    def construct(self):
        key_c = Circle(radius=0.22, fill_color=INK, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.5, height=0.13, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.1)
        key_t = Rectangle(width=0.12, height=0.17, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.35, aligned_edge=RIGHT)
        key = VGroup(key_c, key_s, key_t)

        # Phase 1 — WRITE
        phase1_lbl = Text("WRITE", font=DISP, weight="BOLD",
                          font_size=40, color=MUTED)
        phase1_lbl.to_edge(UP, buff=0.7).shift(LEFT * 3.0)
        key1 = key.copy().shift(LEFT * 3.0 + DOWN * 0.2)
        arrow1 = Arrow(key1.get_bottom(), LEFT * 3.0 + DOWN * 1.5,
                       color=MUTED, stroke_width=2, tip_length=0.2, buff=0.05)
        # Text placeholder: FAINT document lines (no INK text = no checker blobs)
        doc_lines = VGroup(*[
            Line(LEFT * 1.2, RIGHT * 1.2, stroke_color=FAINT, stroke_width=2)
            for _ in range(4)
        ])
        doc_lines.arrange(DOWN, buff=0.28)
        doc_lines.shift(LEFT * 0.0 + DOWN * 1.6)

        # Phase 2 — READ: TERRA on the arrow only (one accent = the detection path)
        phase2_lbl = Text("READ", font=DISP, weight="BOLD",
                          font_size=40, color=MUTED)
        phase2_lbl.to_edge(UP, buff=0.7).shift(RIGHT * 3.0)
        key2 = key.copy().shift(RIGHT * 3.0 + DOWN * 0.2)
        arrow2 = Arrow(key2.get_bottom(), RIGHT * 3.0 + DOWN * 1.5,
                       color=TERRA, stroke_width=2.5, tip_length=0.2, buff=0.05)
        count_lbl = Text("counting…", font=BODY, font_size=40, color=MUTED)
        count_lbl.shift(RIGHT * 3.0 + DOWN * 2.3)

        self.play(FadeIn(phase1_lbl), FadeIn(key1), run_time=0.4)
        self.play(GrowArrow(arrow1), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.08) for l in doc_lines],
                              lag_ratio=0.15, run_time=0.9))
        self.wait(0.9)
        self.play(FadeIn(phase2_lbl), FadeIn(key2), run_time=0.4)
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(FadeIn(count_lbl), run_time=0.4)
        self.wait(4.2)


class S09_PublishBreaks(Scene):
    """Publish the key and anyone can forge or scrub the mark. ~6.2s"""
    def construct(self):
        # Key at top — published (open)
        key_c = Circle(radius=0.26, fill_color=INK, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.6, height=0.16, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.12)
        key_t = Rectangle(width=0.14, height=0.2, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.4, aligned_edge=RIGHT)
        key = VGroup(key_c, key_s, key_t)
        key.to_edge(UP, buff=1.2)

        pub_lbl = Text("PUBLISHED", font=DISP, weight="BOLD",
                       font_size=24, color=INK)
        pub_lbl.next_to(key, RIGHT, buff=0.4)

        # Branch arrow
        branch_down = Line(key.get_bottom(), key.get_bottom() + DOWN * 1.0,
                           stroke_color=INK, stroke_width=2)
        split_l = Line(branch_down.get_end(),
                       branch_down.get_end() + DOWN * 1.2 + LEFT * 2.5,
                       stroke_color=INK, stroke_width=2)
        split_r = Line(branch_down.get_end(),
                       branch_down.get_end() + DOWN * 1.2 + RIGHT * 2.5,
                       stroke_color=INK, stroke_width=2)

        # Left: FORGED — TERRA (the one accent)
        forged_lbl = Text("FORGED", font=DISP, weight="BOLD",
                          font_size=36, color=TERRA)
        forged_lbl.move_to(split_l.get_end() + DOWN * 0.5)

        # Right: SCRUBBED — muted
        scrubbed_lbl = Text("SCRUBBED", font=DISP, weight="BOLD",
                            font_size=36, color=MUTED)
        scrubbed_lbl.move_to(split_r.get_end() + DOWN * 0.5)

        self.play(FadeIn(key, scale=1.1), FadeIn(pub_lbl), run_time=0.5)
        self.play(Create(branch_down), run_time=0.3)
        self.play(Create(split_l), Create(split_r), run_time=0.4)
        self.play(Write(forged_lbl), run_time=0.4)
        self.play(FadeIn(scrubbed_lbl), run_time=0.4)
        self.wait(4.2)


class S10_TesterVouched(Scene):
    """Key stays secret; the tester and the vouched-for are the same party. ~7.2s"""
    def construct(self):
        # Provider boundary — TERRA stroke is the ONE accent
        boundary = Rectangle(width=5.5, height=4.0,
                             fill_color=WHITE, fill_opacity=1,
                             stroke_color=TERRA, stroke_width=3.5)
        boundary.shift(RIGHT * 0.8 + DOWN * 0.1)

        # Key inside (INK — structural, not the accent)
        key_c = Circle(radius=0.28, fill_color=INK, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.65, height=0.17, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.12)
        key_t = Rectangle(width=0.15, height=0.22, fill_color=INK, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.42, aligned_edge=RIGHT)
        key = VGroup(key_c, key_s, key_t)
        key.shift(RIGHT * 0.8 + UP * 0.6)

        # The tester and vouched-for: same shape (overlapping circles)
        shape_a = Circle(radius=0.5, fill_color=FAINT, fill_opacity=1,
                         stroke_color=INK, stroke_width=1.8)
        shape_a.shift(RIGHT * 0.1 + DOWN * 0.9)
        shape_b = Circle(radius=0.5, fill_color=FAINT, fill_opacity=1,
                         stroke_color=INK, stroke_width=1.8)
        shape_b.shift(RIGHT * 1.5 + DOWN * 0.9)
        same_lbl = Text("same party", font=BODY, font_size=24, color=MUTED)
        same_lbl.next_to(VGroup(shape_a, shape_b), DOWN, buff=0.2)

        # Label
        provider_lbl = Text("PROVIDER", font=DISP, weight="BOLD",
                            font_size=22, color=MUTED)
        provider_lbl.next_to(boundary, UP, buff=0.15)

        # Left: closed-out label
        closed = Text("outside", font=BODY, font_size=26, color=MUTED)
        closed.shift(LEFT * 3.5)

        self.play(FadeIn(boundary), run_time=0.4)
        self.play(FadeIn(provider_lbl), run_time=0.3)
        self.play(FadeIn(key, scale=1.15), run_time=0.5)
        self.play(FadeIn(shape_a), FadeIn(shape_b), run_time=0.5)
        self.play(FadeIn(same_lbl), run_time=0.3)
        self.play(FadeIn(closed), run_time=0.3)
        self.wait(4.9)


class S11_OneFlag(Scene):
    """THE ONE FLAG — two futures: sealed detector vs published verifier. ~10.8s"""
    def construct(self):
        # TERRA "ONE FLAG" text — the reel's only hedge; large text is the accent
        flag_txt = Text("ONE FLAG", font=DISP, weight="BOLD",
                        font_size=52, color=TERRA)
        flag_txt.to_edge(UP, buff=0.55)
        flag_rule = Line(flag_txt.get_left(), flag_txt.get_right(),
                         stroke_color=TERRA, stroke_width=3)
        flag_rule.next_to(flag_txt, DOWN, buff=0.12)
        flag_sub = Text("deployment choice, not a law of the maths",
                        font=BODY, font_size=26, color=INK)
        flag_sub.next_to(flag_rule, DOWN, buff=0.22)

        # Left panel: sealed detector
        left_box = Rectangle(width=3.0, height=3.8, fill_color=WHITE,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        left_box.shift(LEFT * 2.8 + DOWN * 0.7)
        left_hdr = Text("SEALED", font=DISP, weight="BOLD",
                         font_size=30, color=INK)
        left_hdr.next_to(left_box, UP, buff=0.15)
        # Lock icon inside
        lock_body = RoundedRectangle(corner_radius=0.08, width=0.9, height=0.75,
                                      fill_color=FAINT, fill_opacity=1,
                                      stroke_color=INK, stroke_width=1.5)
        lock_arch = Arc(radius=0.28, start_angle=0, angle=PI,
                        stroke_color=INK, stroke_width=1.5)
        lock_arch.next_to(lock_body, UP, buff=-0.14)
        lock_icon = VGroup(lock_arch, lock_body)
        lock_icon.move_to(left_box.get_center() + UP * 0.3)
        lock_sub = Text("company only", font=BODY, font_size=22, color=MUTED)
        lock_sub.next_to(lock_icon, DOWN, buff=0.35)

        # Right panel: published verifier
        right_box = Rectangle(width=3.0, height=3.8, fill_color=WHITE,
                               fill_opacity=1, stroke_color=INK, stroke_width=2)
        right_box.shift(RIGHT * 2.8 + DOWN * 0.7)
        right_hdr = Text("VERIFIABLE", font=DISP, weight="BOLD",
                          font_size=30, color=INK)
        right_hdr.next_to(right_box, UP, buff=0.15)
        # Open lock icon
        open_lock_body = RoundedRectangle(corner_radius=0.08, width=0.9, height=0.75,
                                           fill_color=FAINT, fill_opacity=1,
                                           stroke_color=INK, stroke_width=1.5)
        open_arch = Arc(radius=0.28, start_angle=0, angle=PI,
                        stroke_color=INK, stroke_width=1.5)
        open_arch.next_to(open_lock_body, UP, buff=-0.14)
        open_arch.shift(RIGHT * 0.28)   # shifted open = unlocked
        open_icon = VGroup(open_arch, open_lock_body)
        open_icon.move_to(right_box.get_center() + UP * 0.3)
        open_sub = Text("anyone runs locally", font=BODY, font_size=22, color=MUTED)
        open_sub.next_to(open_icon, DOWN, buff=0.35)

        self.play(Write(flag_txt), run_time=0.5)
        self.play(Create(flag_rule), run_time=0.3)
        self.play(FadeIn(flag_sub), run_time=0.4)
        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.5)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(FadeIn(lock_icon), FadeIn(open_icon), run_time=0.5)
        self.play(FadeIn(lock_sub), FadeIn(open_sub), run_time=0.4)
        self.wait(8.1)


class S12_ProbingInfers(Scene):
    """Probes strike the box from outside; its shape fills in as dotted outline. ~8.0s"""
    def construct(self):
        # Sealed box
        box = Rectangle(width=3.2, height=3.2, fill_color=WHITE,
                        fill_opacity=1, stroke_color=INK, stroke_width=3)
        box.shift(RIGHT * 1.5)

        # Key blank inside (secret stays blank)
        blank = Rectangle(width=1.2, height=0.6, fill_color=FAINT,
                          fill_opacity=1, stroke_color=MUTED, stroke_width=1)
        blank.move_to(box.get_center())
        blank_lbl = Text("key", font=BODY, font_size=20, color=MUTED)
        blank_lbl.move_to(blank.get_center())

        # Probes from left
        probe_starts = [LEFT * 5.5 + UP * 1.0, LEFT * 5.5, LEFT * 5.5 + DOWN * 1.0]
        probe_ends   = [box.get_left() + UP * 1.0, box.get_left(), box.get_left() + DOWN * 1.0]
        probes = VGroup(*[
            Arrow(s, e, stroke_width=2, tip_length=0.2, color=MUTED, buff=0.05)
            for s, e in zip(probe_starts, probe_ends)
        ])

        # TERRA dotted inferred outline (structure fills in)
        inferred = DashedVMobject(
            Rectangle(width=2.6, height=2.6, stroke_color=TERRA, stroke_width=2.5),
            num_dashes=24
        )
        inferred.move_to(box.get_center())

        self.play(FadeIn(box), run_time=0.4)
        self.play(FadeIn(blank), FadeIn(blank_lbl), run_time=0.3)
        self.play(LaggedStart(*[GrowArrow(p) for p in probes],
                              lag_ratio=0.25, run_time=1.0))
        self.play(Create(inferred), run_time=1.0)
        self.wait(5.3)


class S13_WorstOfBoth(Scene):
    """Secret enough to block the honest checker, not secret enough to stop the attacker. ~7.9s"""
    def construct(self):
        # Box divided: solid left wall, dotted right section
        solid_wall = Rectangle(width=2.0, height=4.2, fill_color=WHITE,
                               fill_opacity=1, stroke_color=MUTED, stroke_width=3)
        solid_wall.shift(LEFT * 0.6)
        dotted_section = DashedVMobject(
            Rectangle(width=2.0, height=4.2, stroke_color=MUTED, stroke_width=2),
            num_dashes=20)
        dotted_section.shift(RIGHT * 2.2)
        # Fill for dotted
        dot_fill = Rectangle(width=2.0, height=4.2, fill_color=WHITE,
                             fill_opacity=1, stroke_width=0)
        dot_fill.shift(RIGHT * 2.2)

        # Honest checker (left): blocked; label ABOVE dot to stay in title-safe zone
        checker_dot = Dot(radius=0.22, color=INK)
        checker_dot.shift(LEFT * 4.0)
        checker_lbl = Text("CHECKER", font=DISP, weight="BOLD",
                           font_size=36, color=INK)
        checker_lbl.next_to(checker_dot, UP, buff=0.25)
        blocked_arrow = Arrow(LEFT * 3.5, LEFT * 2.05, color=MUTED,
                              stroke_width=2, tip_length=0.2, buff=0.05)
        blocked_x = Text("✕", font=DISP, font_size=44, color=MUTED)
        blocked_x.move_to(LEFT * 1.55)

        # Attacker (right): label ABOVE dot; label centered so it stays in safe box
        attacker_dot = Dot(radius=0.22, color=INK)
        attacker_dot.shift(RIGHT * 4.0)
        attacker_lbl = Text("ATTACKER", font=DISP, weight="BOLD",
                            font_size=36, color=INK)
        attacker_lbl.next_to(attacker_dot, UP, buff=0.25)
        # TERRA accent: thin horizontal rule marking the gap the attacker exploits
        # Height = 5px, length ~405px → aspect ratio 81:1 → flat-bar (§8.3 skip)
        entry_rule = Line(RIGHT * 1.2, RIGHT * 4.5,
                          stroke_color=TERRA, stroke_width=5)
        entry_rule.shift(DOWN * 1.6)

        self.play(FadeIn(dot_fill), Create(solid_wall), Create(dotted_section), run_time=0.6)
        self.play(FadeIn(checker_dot), FadeIn(checker_lbl), run_time=0.4)
        self.play(GrowArrow(blocked_arrow), Write(blocked_x), run_time=0.5)
        self.play(FadeIn(attacker_dot), FadeIn(attacker_lbl), run_time=0.4)
        self.play(Create(entry_rule), run_time=0.5)
        self.wait(5.4)


class S14_AnchorPayoff(Scene):
    """THE ANCHOR RETURNS — same composition, verdict now signed letterhead. ~7.2s"""
    def construct(self):
        # IDENTICAL composition to S03
        paper  = _make_paper()
        stamp  = _make_verdict_mark("SIGNED")   # TERRA accent — same position as S03
        table  = _make_table()

        # Small annotation: "company letterhead" below the stamp
        ann = Text("company letterhead", font=BODY, font_size=20, color=MUTED)
        ann.next_to(stamp, DOWN, buff=0.22)

        # Identical animation sequence as S03
        self.play(FadeIn(paper), run_time=0.5)
        self.play(FadeIn(stamp, scale=1.1), run_time=0.5)
        self.play(FadeIn(ann), run_time=0.3)
        self.play(FadeIn(table), run_time=0.6)
        self.wait(5.3)


class S15_DetectedLimits(Scene):
    """DETECTED doesn't prove the maths held — four unverifiable assumptions. ~8.0s"""
    def construct(self):
        # DETECTED header with TERRA accent
        detected = Text("DETECTED", font=DISP, weight="BOLD",
                        font_size=60, color=INK)
        detected.to_edge(UP, buff=0.8)
        det_rule = Line(detected.get_left(), detected.get_right(),
                        stroke_color=TERRA, stroke_width=5)
        det_rule.next_to(detected, DOWN, buff=0.15)

        # Four assumptions with empty checkboxes
        assumptions = [
            "right key",
            "right version",
            "right threshold",
            "that exact text",
        ]
        rows = VGroup()
        for text in assumptions:
            box = Square(side_length=0.38, stroke_color=INK, stroke_width=2,
                         fill_color=GROUND, fill_opacity=1)
            lbl = Text(text, font=BODY, font_size=32, color=INK)
            row = VGroup(box, lbl)
            row.arrange(RIGHT, buff=0.3, aligned_edge=LEFT)
            rows.add(row)
        rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        rows.shift(LEFT * 1.0 + DOWN * 0.5)

        note = Text("nobody can tick these", font=BODY, font_size=24, color=MUTED)
        note.to_edge(DOWN, buff=0.6)

        self.play(Write(detected), run_time=0.5)
        self.play(Create(det_rule), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(row, shift=RIGHT * 0.1) for row in rows],
                              lag_ratio=0.25, run_time=1.4))
        self.play(FadeIn(note), run_time=0.4)
        self.wait(5.4)


class S16_NotDetectedLimits(Scene):
    """NOT DETECTED doesn't mean no AI — another key sits unread. ~6.3s
    Mirrors S15's construction."""
    def construct(self):
        # NOT DETECTED header (ink, no TERRA here — the absence is the point)
        not_detected = Text("NOT DETECTED", font=DISP, weight="BOLD",
                             font_size=54, color=INK)
        not_detected.to_edge(UP, buff=0.8)

        # Reader indicator (active detector)
        reader_dot = Circle(radius=0.32, fill_color=FAINT, fill_opacity=1,
                            stroke_color=INK, stroke_width=2)
        reader_dot.shift(LEFT * 1.5 + DOWN * 0.3)
        reader_lbl = Text("reader", font=BODY, font_size=22, color=MUTED)
        reader_lbl.next_to(reader_dot, DOWN, buff=0.15)

        # Second key — greyed (invisible, secret); TERRA accent on UNREAD label only
        key_c = Circle(radius=0.28, fill_color=MUTED, fill_opacity=1, stroke_width=0)
        key_s = Rectangle(width=0.65, height=0.17, fill_color=MUTED, fill_opacity=1,
                           stroke_width=0)
        key_s.next_to(key_c, RIGHT, buff=-0.12)
        key_t = Rectangle(width=0.15, height=0.22, fill_color=MUTED, fill_opacity=1,
                           stroke_width=0)
        key_t.next_to(key_s, DOWN + RIGHT, buff=-0.42, aligned_edge=RIGHT)
        second_key = VGroup(key_c, key_s, key_t)
        second_key.shift(RIGHT * 2.0 + DOWN * 0.3)

        unread_lbl = Text("UNREAD", font=DISP, weight="BOLD",
                          font_size=28, color=TERRA)
        unread_lbl.next_to(second_key, DOWN, buff=0.25)

        sub = Text("another company's key", font=BODY, font_size=24, color=MUTED)
        sub.next_to(second_key, UP, buff=0.2)

        note = Text("invisible to this reader, by design", font=BODY,
                    font_size=24, color=MUTED)
        note.to_edge(DOWN, buff=0.6)

        self.play(Write(not_detected), run_time=0.5)
        self.play(FadeIn(reader_dot), FadeIn(reader_lbl), run_time=0.4)
        self.play(FadeIn(second_key, scale=1.1), run_time=0.5)
        self.play(FadeIn(unread_lbl), FadeIn(sub), run_time=0.4)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(4.2)
