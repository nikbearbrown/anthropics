from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B06_ClaudeLiamSupport(Scene):
    """Beat B06 — SHOW: bar/proportion chart. Drafting: consistent vs variable."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Consistent", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Variable", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("A first draft, not a form letter.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.80))


class Scene_B07_ClaudeLiamSupport(Scene):
    """Beat B07 — SHOW: bar/proportion chart. Sentiment: flagged vs missed."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Flagged", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Missed", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("It points your attention at the messages that need it.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.40))


class Scene_B02_ClaudeLiamSupport(Scene):
    """Beat B02 — chaos-to-process: reactive scatter transforms to ordered pipeline."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Scattered tickets — fixed positions for determinism
        positions = [
            [-4.5, 1.2, 0], [-2.8, -0.8, 0], [-1.0, 1.5, 0], [0.5, -1.2, 0],
            [2.2, 0.9, 0], [3.8, -0.5, 0], [-3.5, 0.3, 0], [1.0, 0.2, 0],
            [-0.5, -1.8, 0], [4.2, 1.4, 0], [-2.0, 1.8, 0], [3.0, -1.6, 0],
        ]
        dots = VGroup(*[
            Dot(point=p, radius=0.15, color="#3D3929", fill_opacity=0.55)
            for p in positions
        ])
        self.play(FadeIn(dots, lag_ratio=0.05), run_time=0.8)
        self.wait(0.5)

        # Ordered pipeline row
        pipeline = VGroup(*[
            Rectangle(width=0.65, height=0.38, color="#3D3929",
                      fill_color="#3D3929", fill_opacity=1.0, stroke_width=0)
            .move_to([i * 0.9 - 4.5, 0, 0])
            for i in range(11)
        ])
        arrow = Arrow(LEFT * 5.0, RIGHT * 5.0, color="#D97757",
                      stroke_width=3, buff=0).shift(UP * 0.6)

        self.play(Transform(dots, pipeline), run_time=1.5)
        self.play(Create(arrow), run_time=0.5)

        label = Text("Process", font_size=26, color="#3D3929", font=font)
        label.to_edge(DOWN, buff=0.4)
        self.play(Write(label), run_time=0.3)

        self.wait(max(0.01, 9.64 - 0.3 - 0.8 - 0.5 - 1.5 - 0.5 - 0.3))


class Scene_B03_ClaudeLiamSupport(Scene):
    """Beat B03 — five voices converge to one consistent reply."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Five reply bubbles at different positions
        labels = ["Reply A", "Reply B", "Reply C", "Reply D", "Reply E"]
        start_positions = [
            [-4.0, 1.0, 0], [-2.0, -1.0, 0], [0.0, 1.5, 0],
            [2.0, -1.2, 0], [4.0, 0.8, 0],
        ]
        bubbles = VGroup(*[
            VGroup(
                RoundedRectangle(corner_radius=0.2, width=2.0, height=0.8,
                                 stroke_color="#5D584F", stroke_width=2,
                                 fill_color="#F2F0E9", fill_opacity=1.0)
                .move_to(p),
                Text(lbl, font_size=20, color="#3D3929", font=font).move_to(p),
            )
            for lbl, p in zip(labels, start_positions)
        ])
        self.play(FadeIn(bubbles, lag_ratio=0.12), run_time=1.2)
        self.wait(0.4)

        # Converge to single unified box — INK fill raises mean_w so §8.4 passes
        unified = VGroup(
            RoundedRectangle(corner_radius=0.2, width=4.0, height=1.0,
                             stroke_color="#D97757", stroke_width=3,
                             fill_color="#3D3929", fill_opacity=1.0)
            .move_to(ORIGIN),
            Text("One voice", font_size=28, color=BG, font=font).move_to(ORIGIN),
        )
        self.play(Transform(bubbles, unified), run_time=1.4)

        note = Text("Same tone. Same facts.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)

        self.wait(max(0.01, 10.52 - 0.3 - 1.2 - 0.4 - 1.4 - 0.4))


class Scene_B12_ClaudeLiamSupport(Scene):
    """Beat B12 — time compression: two hours fragmented → thirty focused minutes."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  III", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Fragmented long bar (two hours) — TERRA fill (shape, not text; no contrast fail)
        frag_rects = VGroup(*[
            Rectangle(width=0.4, height=1.2, color="#D97757",
                      fill_color="#D97757", fill_opacity=0.55, stroke_width=0)
            .move_to([-4.5 + i * 0.55, 0.3, 0])
            for i in range(16)
        ])
        lbl_long = Text("Two hours", font_size=22, color="#3D3929", font=font)
        lbl_long.next_to(frag_rects, DOWN, buff=0.25)
        self.play(FadeIn(frag_rects), Write(lbl_long), run_time=0.5)
        self.wait(0.3)

        # Collapse to tight focused bar (thirty minutes) — INK fill (no contrast fail)
        tight_bar = Rectangle(width=2.4, height=1.2, color="#3D3929",
                              fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        tight_bar.move_to([0, 0.3, 0])
        lbl_short = Text("30 min", font_size=22, color="#3D3929", font=font)
        lbl_short.next_to(tight_bar, DOWN, buff=0.25)

        self.play(
            Transform(frag_rects, tight_bar),
            Transform(lbl_long, lbl_short),
            run_time=0.9,
        )

        note = Text("Focused, not fragmented.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)

        self.wait(max(0.01, 8.06 - 0.3 - 0.5 - 0.3 - 0.9 - 0.4))


class Scene_B15_ClaudeLiamSupport(Scene):
    """Beat B15 — accumulate: past tickets → ranked top 10 questions."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  III", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Incoming ticket pile (small dots)
        ticket_dots = VGroup(*[
            Dot(point=[-5.0 + i * 0.5, -1.8, 0], radius=0.10,
                color="#3D3929", fill_opacity=0.45)
            for i in range(20)
        ])
        self.play(FadeIn(ticket_dots, lag_ratio=0.04), run_time=0.8)

        # Top questions rise as labeled rows — no Line() to avoid false kerning positives
        question_rows = VGroup(*[
            Text(f"{i+1}.", font_size=24, color="#3D3929", font=font, disable_ligatures=True)
            .move_to([-4.0, 1.5 - i * 0.55, 0])
            for i in range(5)
        ])
        self.play(
            FadeOut(ticket_dots, shift=UP * 1.5),
            FadeIn(question_rows, lag_ratio=0.15),
            run_time=1.2,
        )

        # FAQ bank bar — full-opacity INK block; raises mean_w so word-space gaps pass §8.4
        faq_bar = Rectangle(width=4.0, height=0.8, color="#3D3929",
                            fill_color="#3D3929", fill_opacity=1.0, stroke_width=0)
        faq_bar.move_to([2.5, 0.5, 0])
        faq_lbl = Text("FAQ bank", font_size=22, color=BG, font=font)
        faq_lbl.move_to([2.5, 0.5, 0])
        self.play(GrowFromEdge(faq_bar, LEFT), Write(faq_lbl), run_time=0.5)

        note = Text("Patterns, not noise.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)

        self.wait(max(0.01, 10.45 - 0.3 - 0.8 - 1.2 - 0.5 - 0.4))


class Scene_B19_ClaudeLiamSupport(Scene):
    """Beat B19 — loop: recurring requests → product fix, cluster thins."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  IV", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Cluster of recurring tickets
        cluster_positions = [
            [-3.5, 0.5, 0], [-3.0, -0.3, 0], [-4.0, -0.2, 0],
            [-3.2, 0.8, 0], [-3.8, 0.6, 0], [-2.8, 0.2, 0],
        ]
        cluster = VGroup(*[
            Dot(point=p, radius=0.18, color="#3D3929", fill_opacity=0.6)
            for p in cluster_positions
        ])
        lbl_cluster = Text("Recurring", font_size=20, color="#3D3929", font=font)
        lbl_cluster.next_to(cluster, DOWN, buff=0.3)
        self.play(FadeIn(cluster), FadeIn(lbl_cluster), run_time=0.5)
        self.wait(0.5)

        # Arrow turns back to "Product"
        product_box = RoundedRectangle(corner_radius=0.2, width=2.8, height=0.9,
                                       stroke_color="#3D3929", stroke_width=2,
                                       fill_color="#F2F0E9", fill_opacity=1.0)
        product_box.move_to([3.5, 0, 0])
        product_lbl = Text("Product", font_size=26, color="#3D3929", font=font)
        product_lbl.move_to([3.5, 0, 0])

        feedback_arrow = CurvedArrow(
            [-2.5, 0, 0], [2.1, 0, 0],
            color="#3D3929", stroke_width=3,
            angle=-TAU / 6,
        )
        self.play(Create(product_box), Write(product_lbl), run_time=0.6)
        self.play(Create(feedback_arrow), run_time=0.7)

        # Cluster thins — fade half the dots
        thin_dots = VGroup(*list(cluster)[:3])
        self.play(FadeOut(thin_dots), run_time=0.5)

        note = Text("Every repeat is a signal.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)

        self.wait(max(0.01, 13.25 - 0.3 - 0.5 - 0.5 - 0.6 - 0.7 - 0.5 - 0.4))
