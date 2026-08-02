from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY   = "#56B4E9"
BLUE  = "#0072B2"
GREEN = "#009E73"
VERM  = "#D55E00"
GRAY  = "#7c7c7c"

# Cap radii shrinking left→right (Manim units)
CAP_R = [0.32, 0.22, 0.12, 0.04]

# X-positions for the four chromosome glyphs
GLYPH_XS = [-5.0, -2.5, 0.0, 2.5]
ARM = 0.70  # half-arm length of the X

def make_glyph(x, y, cap_radius, arm=ARM, cap_color=GREEN, line_color=BLUE):
    """Build one chromosome X-glyph: two crossing lines + 4 cap dots."""
    g = VGroup(
        Line([x - arm, y + arm, 0], [x + arm, y - arm, 0],
             color=line_color, stroke_width=4.5),
        Line([x - arm, y - arm, 0], [x + arm, y + arm, 0],
             color=line_color, stroke_width=4.5),
    )
    if cap_radius > 0.005:
        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
            g.add(Dot([x + dx * arm, y + dy * arm, 0],
                      radius=cap_radius, color=cap_color, fill_opacity=0.9))
    return g


# ============================================================
# B05_TelomereCrisis — initial animation
#   LaggedStart glyph reveal → fork split → X-mark → Flash
# ============================================================
class B05_TelomereCrisis(Scene):
    def construct(self):
        glyphs = VGroup()
        for i, (x, cr) in enumerate(zip(GLYPH_XS, CAP_R)):
            cap_col = GREEN if i < 3 else VERM
            g = make_glyph(x, 0, cr, cap_color=cap_col)
            glyphs.add(g)

        # Connector arrows between glyphs
        connectors = VGroup()
        for i in range(3):
            x0 = GLYPH_XS[i] + ARM + 0.05
            x1 = GLYPH_XS[i + 1] - ARM - 0.05
            connectors.add(Arrow([x0, 0, 0], [x1, 0, 0],
                                 buff=0, color=GRAY,
                                 stroke_width=2.5,
                                 max_tip_length_to_length_ratio=0.18))

        # 1. LaggedStart reveal glyphs + connectors
        self.play(
            LaggedStart(
                *[FadeIn(g, shift=RIGHT * 0.25) for g in glyphs],
                lag_ratio=0.22, run_time=1.8,
            )
        )
        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in connectors],
                lag_ratio=0.20, run_time=0.9,
            )
        )
        self.wait(0.2)

        # 2. Fork split from branch point (right of last glyph)
        bp = np.array([GLYPH_XS[-1] + ARM + 0.15, 0, 0])
        fork_up = Line(bp, bp + np.array([1.6, 1.1, 0]),
                       color=GRAY, stroke_width=3.0)
        fork_down = Line(bp, bp + np.array([1.6, -1.1, 0]),
                         color=GRAY, stroke_width=3.0)
        self.play(GrowFromPoint(VGroup(fork_up, fork_down), bp), run_time=0.7)

        # 3. Survivor glyph (upper — uneven GREEN caps)
        sv_x = bp[0] + 1.6 + ARM + 0.3
        sv_y = 1.1
        survivor = make_glyph(sv_x, sv_y, 0.20, cap_color=GREEN)
        # Override: add one small cap to make it "uneven"
        survivor.add(Dot([sv_x - ARM, sv_y + ARM, 0],
                         radius=0.30, color=GREEN, fill_opacity=0.85))
        # Scar line (VERM)
        scar = Line([sv_x - 0.35, sv_y + 0.05, 0],
                    [sv_x + 0.35, sv_y + 0.05, 0],
                    color=VERM, stroke_width=5)

        # Dead-end X-mark (lower)
        de_cx = bp[0] + 1.6 + 0.25
        de_cy = -1.1
        dead_end = VGroup(
            Line([de_cx - 0.18, de_cy + 0.18, 0],
                 [de_cx + 0.18, de_cy - 0.18, 0],
                 color=VERM, stroke_width=6.5),
            Line([de_cx - 0.18, de_cy - 0.18, 0],
                 [de_cx + 0.18, de_cy + 0.18, 0],
                 color=VERM, stroke_width=6.5),
        )

        self.play(
            FadeIn(survivor, shift=UP * 0.2),
            FadeIn(dead_end),
            run_time=0.6,
        )
        self.play(FadeIn(scar), run_time=0.3)

        # 4. Flash the dead-end X-mark to emphasize majority outcome
        self.play(
            Flash(dead_end.get_center(), color=VERM,
                  line_length=0.22, num_lines=12, flash_radius=0.45),
            run_time=0.5,
        )
        self.wait(0.8)


# ============================================================
# B07_TelomereCrisisFlow — revision: caps shrink in motion
#   Caps animate via .scale() as each glyph appears → fork →
#   Circle glow on survivor caps → Flash pulse on dead-end X
# ============================================================
class B07_TelomereCrisisFlow(Scene):
    def construct(self):
        # Build glyphs with FULL-SIZE caps initially, then shrink
        START_R = 0.32  # all start at max cap size

        glyphs = VGroup()
        cap_groups = []  # store cap dot groups for individual scaling
        for i, x in enumerate(GLYPH_XS):
            cap_col = GREEN if i < 3 else VERM
            # Lines only (no caps yet)
            lines = VGroup(
                Line([x - ARM, ARM, 0], [x + ARM, -ARM, 0],
                     color=BLUE, stroke_width=4.5),
                Line([x - ARM, -ARM, 0], [x + ARM, ARM, 0],
                     color=BLUE, stroke_width=4.5),
            )
            caps = VGroup(*[
                Dot([x + dx * ARM, dy * ARM, 0],
                    radius=START_R, color=cap_col, fill_opacity=0.9)
                for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]
            ])
            g = VGroup(lines, caps)
            glyphs.add(g)
            cap_groups.append(caps)

        # Target scale for each stage relative to start_r
        target_scales = [r / START_R for r in CAP_R]

        # Connectors
        connectors = VGroup()
        for i in range(3):
            x0 = GLYPH_XS[i] + ARM + 0.05
            x1 = GLYPH_XS[i + 1] - ARM - 0.05
            connectors.add(Arrow([x0, 0, 0], [x1, 0, 0],
                                 buff=0, color=GRAY, stroke_width=2.5,
                                 max_tip_length_to_length_ratio=0.18))

        # 1. Reveal each glyph then immediately shrink its caps
        for i, (g, caps, ts) in enumerate(zip(glyphs, cap_groups, target_scales)):
            self.play(FadeIn(g, shift=RIGHT * 0.2), run_time=0.35)
            if ts < 0.99:
                self.play(caps.animate.scale(max(ts, 0.05)), run_time=0.3)
            if i < 3:
                self.play(GrowArrow(connectors[i]), run_time=0.25)

        self.wait(0.2)

        # 2. Fork split
        bp = np.array([GLYPH_XS[-1] + ARM + 0.15, 0, 0])
        fork_up = Line(bp, bp + np.array([1.6, 1.1, 0]),
                       color=GRAY, stroke_width=3.0)
        fork_down = Line(bp, bp + np.array([1.6, -1.1, 0]),
                         color=GRAY, stroke_width=3.0)
        self.play(GrowFromPoint(VGroup(fork_up, fork_down), bp), run_time=0.7)

        # 3. Survivor branch
        sv_x = bp[0] + 1.6 + ARM + 0.3
        sv_y = 1.1
        survivor = make_glyph(sv_x, sv_y, 0.20, cap_color=GREEN)
        scar = Line([sv_x - 0.35, sv_y + 0.05, 0],
                    [sv_x + 0.35, sv_y + 0.05, 0],
                    color=VERM, stroke_width=5)

        # Dead-end X-mark
        de_cx = bp[0] + 1.6 + 0.25
        de_cy = -1.1
        dead_end = VGroup(
            Line([de_cx - 0.18, de_cy + 0.18, 0],
                 [de_cx + 0.18, de_cy - 0.18, 0],
                 color=VERM, stroke_width=6.5),
            Line([de_cx - 0.18, de_cy - 0.18, 0],
                 [de_cx + 0.18, de_cy + 0.18, 0],
                 color=VERM, stroke_width=6.5),
        )

        self.play(FadeIn(survivor), FadeIn(dead_end), run_time=0.5)
        self.play(FadeIn(scar), run_time=0.3)

        # 4. Circle glow on survivor's caps (GREEN)
        glow = Circle(radius=0.55, color=GREEN, stroke_width=3.5,
                      stroke_opacity=0.7).move_to([sv_x, sv_y, 0])
        self.play(Create(glow), run_time=0.4)
        self.play(glow.animate.set_stroke(opacity=0.0), run_time=0.4)

        # 5. Pulse / Flash the dead-end X-mark
        self.play(
            Flash(dead_end.get_center(), color=VERM,
                  line_length=0.22, num_lines=12, flash_radius=0.45),
            run_time=0.5,
        )
        self.wait(0.8)

class STD_B01_claude_liam_telomere_cris(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-telomere-crisis.
    Narration: 'Telomeres are the repetitive caps on chromosome ends. Every cell division erodes'
    Duration: 13.7s  Lines: 3  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Telomere Crisis"
        body_lines = ["Telomeres are the repetitive caps on", "chromosome ends", "Every cell division erodes them a little"]
        spark_str = "This plate shows four stages of that erosion \u2014 each chromoso"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=34)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 4.31)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_telomere_cris(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-telomere-crisis.
    Narration: 'At crisis, most cells die — the vast majority dead end. But rarely, one cell rea'
    Duration: 12.9s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Telomere Crisis"
        body_lines = ["At crisis, most cells die \u2014 the vast", "majority dead end", "But rarely, one cell reactivates", "telomerase, survives with a scrambled", "genome, and that\u2026"]
        spark_str = "We're animating that one-in-a-million bottleneck"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.43)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_telomere_cris(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-telomere-crisis.
    Narration: 'The motion taught: it is a numbers game. The erosion is relentless, the fork ine'
    Duration: 18.4s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Telomere Crisis"
        body_lines = ["The motion taught: it is a numbers game", "The erosion is relentless, the fork inevitable,", "and the surviving lineage is the one that\u2026", "Claude ported four glyph stages, a fork split,", "and a flash in one prompt"]
        spark_str = "The revision added motion to the erosion \u2014 caps that literal"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.52)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
