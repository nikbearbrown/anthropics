from manim import *
import numpy as np

BG    = "#F2F0E9"
INK   = "#3D3929"
TEAL  = "#1F6F5C"
CRIM  = "#BF3339"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class B02_ClaudeLiamVox(Scene):
    """B02 — three sessions, CLAUDE.md grows 47 → 80 → 220 lines."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("CLAUDE.md grows across three sessions",
                     font=FONT, font_size=34, color=INK)
        title.to_edge(UP, buff=0.8)
        self.play(FadeIn(title), run_time=0.4)

        ax = Axes(x_range=[0, 4, 1], y_range=[0, 260, 50],
                  x_length=8.5, y_length=4.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  y_axis_config={"include_numbers": True,
                                 "font_size": 20},
                  tips=False)
        ax.shift(DOWN * 0.4)
        y_label = Text("lines", font=FONT, font_size=20, color=INK)
        y_label.rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.3)
        self.play(Create(ax), FadeIn(y_label), run_time=0.5)

        bars_data = [(1, 47, TEAL, "Session  1", "47"),
                     (2, 80, TEAL, "Session  2", "80"),
                     (3, 220, CRIM, "Session  3", "220")]
        bar_w = 0.55
        for (x, val, col, lbl, num) in bars_data:
            origin = ax.c2p(0, 0)
            pt = ax.c2p(x, val)
            h = abs(pt[1] - origin[1])
            bar = Rectangle(width=bar_w, height=h,
                            color=col, fill_color=col,
                            fill_opacity=0.85, stroke_width=0)
            bar.move_to([pt[0], (pt[1] + origin[1]) / 2, 0])
            label = Text(lbl, font=FONT, font_size=22, color=INK)
            label.next_to(ax.c2p(x, 0), DOWN, buff=0.3)
            num_lbl = Text(num, font=FONT, font_size=22, color=col)
            num_lbl.next_to(bar, UP, buff=0.15)
            self.play(GrowFromEdge(bar, DOWN),
                      FadeIn(label), FadeIn(num_lbl),
                      run_time=0.6)

        cap = Text("Past 200 lines: the file is now noise around the rule",
                   font=FONT, font_size=22, color=CRIM)
        cap.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(cap), run_time=0.5)

        self.wait(max(0.01, 15.5))


class B04_ClaudeLiamVox(Scene):
    """B04 — signal vs noise: the rule prominent in a short file, buried in a long one."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Signal vs noise: attention for the rule",
                     font=FONT, font_size=34, color=INK)
        title.to_edge(UP, buff=0.8)
        self.play(FadeIn(title), run_time=0.4)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7.5, y_length=4.3,
                  axis_config={"color": INK, "stroke_width": 2},
                  y_axis_config={"include_numbers": True,
                                 "font_size": 20},
                  tips=False)
        ax.shift(DOWN * 0.3)
        y_lbl = Text("attention %", font=FONT, font_size=20, color=INK)
        y_lbl.rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.3)
        self.play(Create(ax), FadeIn(y_lbl), run_time=0.4)

        origin = ax.c2p(0, 0)
        bars_data = [(1, 78, TEAL, "Short file", "78%"),
                     (2, 22, CRIM, "Long file", "22%")]
        bar_w = 0.75
        for (x, val, col, lbl, num) in bars_data:
            pt = ax.c2p(x, val)
            h = abs(pt[1] - origin[1])
            bar = Rectangle(width=bar_w, height=h,
                            color=col, fill_color=col,
                            fill_opacity=0.85, stroke_width=0)
            bar.move_to([pt[0], (pt[1] + origin[1]) / 2, 0])
            label = Text(lbl, font=FONT, font_size=24, color=INK)
            label.next_to(ax.c2p(x, 0), DOWN, buff=0.3)
            num_lbl = Text(num, font=FONT, font_size=24, color=col)
            num_lbl.next_to(bar, UP, buff=0.15)
            self.play(GrowFromEdge(bar, DOWN),
                      FadeIn(label), FadeIn(num_lbl),
                      run_time=0.7)

        cap = Text("Every entry added dilutes every other entry",
                   font=FONT, font_size=22, color=INK)
        cap.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(cap), run_time=0.5)

        self.wait(max(0.01, 15.5))


class B06_ClaudeLiamVox(Scene):
    """B06 — the three-move fix: Trim, Skills, Hooks."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("The three-move fix", font=FONT, font_size=36, color=INK)
        title.to_edge(UP, buff=0.8)
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("Trim",  "CLAUDE.md under 200 lines"),
            ("Skills","Move workflow content out"),
            ("Hooks", "Convert inviolable rules"),
        ]
        row_w, row_h = 9.5, 1.1
        y0 = 1.6
        step = 1.35

        for i, (k, v) in enumerate(rows):
            y = y0 - i * step
            box = RoundedRectangle(width=row_w, height=row_h,
                                    color=INK, stroke_width=2,
                                    fill_color=BG, fill_opacity=1,
                                    corner_radius=0.15)
            box.move_to(UP * y)
            key = Text(k, font=FONT, font_size=30, color=TEAL, weight=BOLD)
            key.next_to(box.get_left(), RIGHT, buff=0.6)
            val = Text(v, font=FONT, font_size=26, color=INK)
            val.next_to(key, RIGHT, buff=0.9)
            self.play(FadeIn(box), FadeIn(key), FadeIn(val), run_time=0.6)

        cap = Text("What remains is what belongs.",
                    font=FONT, font_size=22, color=TERRA)
        cap.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(cap), run_time=0.5)

        self.wait(max(0.01, 15.5))


class B07_ClaudeLiamVox(Scene):
    """B07 — the compliance meter: rule-following vs CLAUDE.md line count."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Compliance vs CLAUDE.md length",
                     font=FONT, font_size=34, color=INK)
        title.to_edge(UP, buff=0.8)
        self.play(FadeIn(title), run_time=0.4)

        ax = Axes(x_range=[0, 400, 100], y_range=[0, 100, 25],
                  x_length=9.0, y_length=4.3,
                  axis_config={"color": INK, "stroke_width": 2,
                               "include_numbers": True,
                               "font_size": 20},
                  tips=False)
        ax.shift(UP * 0.1)
        y_lbl = Text("rule adherence %", font=FONT, font_size=22, color=INK)
        y_lbl.rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.3)
        self.play(Create(ax), FadeIn(y_lbl), run_time=0.5)

        def f(x):
            if x <= 150:
                return 95 - (x / 150) * 3
            if x <= 200:
                return 92 - ((x - 150) / 50) * 7
            if x <= 300:
                return 85 - ((x - 200) / 100) * 40
            return max(15, 45 - ((x - 300) / 100) * 30)

        xs = np.linspace(0, 400, 120)
        pts = [ax.c2p(x, f(x)) for x in xs]

        # split path into two colors at x=250
        pts_hi = [ax.c2p(x, f(x)) for x in xs if x <= 250]
        pts_lo = [ax.c2p(x, f(x)) for x in xs if x >= 250]

        curve_hi = VMobject(color=TEAL, stroke_width=6).set_points_smoothly(pts_hi)
        curve_lo = VMobject(color=CRIM, stroke_width=6).set_points_smoothly(pts_lo)
        self.play(Create(curve_hi), run_time=1.2)
        self.play(Create(curve_lo), run_time=1.2)

        # milestone markers
        for (xv, note, col) in [(50, "high", TEAL),
                                (200, "dips", TERRA),
                                (300, "fails", CRIM)]:
            p = ax.c2p(xv, f(xv))
            dot = Dot(p, color=col, radius=0.09)
            tag = Text(note, font=FONT, font_size=22, color=col)
            tag.next_to(dot, UP, buff=0.2)
            self.play(FadeIn(dot), FadeIn(tag), run_time=0.4)

        x_lbl = Text("CLAUDE.md lines", font=FONT, font_size=22, color=INK)
        x_lbl.next_to(ax.x_axis, DOWN, buff=0.3)
        self.play(FadeIn(x_lbl), run_time=0.3)

        cap = Text("Signal-to-noise, not line count for its own sake",
                    font=FONT, font_size=22, color=TERRA)
        cap.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap), run_time=0.5)

        self.wait(max(0.01, 11))


class B08_ClaudeLiamVox(Scene):
    """B08 — the four-question audit table for each CLAUDE.md entry."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Audit each CLAUDE.md entry — four questions",
                     font=FONT, font_size=32, color=INK)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("Claude infers from code",  "cut",       CRIM),
            ("Changes session to session","TODO.md",   INK),
            ("A workflow",                "Skill",     TEAL),
            ("Must hold always",          "Hook",      TERRA),
        ]
        row_w, row_h = 10.0, 0.95
        y0 = 1.9
        step = 1.1

        for i, (q, ans, col) in enumerate(rows):
            y = y0 - i * step
            box = RoundedRectangle(width=row_w, height=row_h,
                                    color=INK, stroke_width=2,
                                    fill_color=BG, fill_opacity=1,
                                    corner_radius=0.12)
            box.move_to(UP * y)
            qtxt = Text(q, font=FONT, font_size=26, color=INK)
            qtxt.next_to(box.get_left(), RIGHT, buff=0.5)
            arrow = Text("->", font=FONT, font_size=26, color=INK)
            arrow.move_to(box.get_center() + RIGHT * 1.9)
            atxt = Text(ans, font=FONT, font_size=28, color=col, weight=BOLD)
            atxt.next_to(box.get_right(), LEFT, buff=0.5)
            self.play(FadeIn(box), FadeIn(qtxt), FadeIn(arrow), FadeIn(atxt),
                      run_time=0.55)

        cap = Text("What remains is what belongs.",
                    font=FONT, font_size=22, color=TERRA)
        cap.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(cap), run_time=0.4)

        self.wait(max(0.01, 10))
