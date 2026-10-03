from manim import *

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


def _act(scene, label):
    act = Text(label, font_size=30, color=INK, font=FONT)
    act.to_edge(UP, buff=0.35)
    scene.play(FadeIn(act), run_time=0.3)
    return act


def _caption(scene, text):
    cap = Text(text, font_size=32, color=INK, font=FONT)
    cap.scale(min(1.0, 12.0 / max(0.1, cap.width)))
    cap.to_edge(DOWN, buff=0.55)
    scene.play(Write(cap), run_time=0.6)
    return cap


def _two_bar(scene, left_label, left_h, right_label, right_h,
             right_accent=True):
    ax = Axes(
        x_range=[0, 3, 1],
        y_range=[0, 100, 25],
        x_length=8,
        y_length=4,
        axis_config={"color": INK, "stroke_width": 2},
        tips=False,
    )
    ax.shift(DOWN * 0.35)
    scene.play(Create(ax), run_time=0.4)

    origin = ax.c2p(0, 0)
    pt1 = ax.c2p(1, left_h)
    pt2 = ax.c2p(2, right_h)
    bar_w = 0.7

    bar1 = Rectangle(width=bar_w, height=abs(pt1[1] - origin[1]),
                     color=INK, fill_color=INK,
                     fill_opacity=0.85, stroke_width=0)
    bar1.move_to([pt1[0], (pt1[1] + origin[1]) / 2, 0])
    right_color = TERRA if right_accent else INK
    bar2 = Rectangle(width=bar_w, height=abs(pt2[1] - origin[1]),
                     color=right_color, fill_color=right_color,
                     fill_opacity=0.85, stroke_width=0)
    bar2.move_to([pt2[0], (pt2[1] + origin[1]) / 2, 0])

    lbl1 = Text(left_label, font_size=30, color=INK, font=FONT)
    lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
    lbl2 = Text(right_label, font_size=30, color=INK, font=FONT)
    lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

    scene.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.7)
    scene.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.7)


def _layer_stack(scene, layers, accent_top=True):
    n = len(layers)
    layer_h = 1.2
    layer_w = 10.0
    start_y = (n - 1) * layer_h / 2

    for i, lbl in enumerate(reversed(layers)):
        y = start_y - i * layer_h
        is_top = (i == n - 1)
        color = TERRA if (accent_top and is_top) else INK
        box = Rectangle(
            width=layer_w,
            height=layer_h * 0.85,
            color=color,
            stroke_width=2,
            fill_color=color,
            fill_opacity=0.10 if not is_top else 0.14,
        )
        box.move_to(UP * y)
        txt = Text(lbl, font_size=34, color=INK, font=FONT)
        txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
        txt.move_to(box)
        scene.play(FadeIn(box), Write(txt), run_time=0.55)


def _three_lines(scene, line1, line2, line3, accent_line=1):
    l1 = Text(line1, font_size=54, color=INK, font=FONT)
    l1.scale(min(1.0, 12.0 / max(0.1, l1.width)))
    l1.shift(UP * 1.6)
    scene.play(Write(l1), run_time=0.55)

    l2 = Text(line2, font_size=42, color=INK, font=FONT)
    l2.scale(min(1.0, 12.0 / max(0.1, l2.width)))
    l2.shift(UP * 0.1)
    scene.play(Write(l2), run_time=0.5)

    l3 = Text(line3, font_size=42, color=INK, font=FONT)
    l3.scale(min(1.0, 12.0 / max(0.1, l3.width)))
    l3.shift(DOWN * 1.4)
    scene.play(Write(l3), run_time=0.5)

    # Terracotta spark on the accent line
    accent = [l1, l2, l3][max(0, min(2, accent_line))]
    spark = Line(LEFT * 0.7, RIGHT * 0.7, color=TERRA, stroke_width=4)
    spark.next_to(accent, UP, buff=0.35)
    scene.play(Create(spark), run_time=0.3)


class Scene_B02_NbbAiCreative(Scene):
    """B02 — THE QUESTION. 80 hours of iteration vs the authorship threshold."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE QUESTION")
        _two_bar(self, "80 hours", 82, "Authorship", 22, right_accent=True)
        _caption(self, "Iteration is not authorship.")
        self.wait(1.0)


class Scene_B03_NbbAiCreative(Scene):
    """B03 — THE PROBLEM. Aesthetic defaults fill every uncontested decision."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE PROBLEM")
        _three_lines(
            self,
            "Aesthetic defaults.",
            "The model fills the silence.",
            "The model's decision is not yours.",
            accent_line=2,
        )
        self.wait(1.0)


class Scene_B04_NbbAiCreative(Scene):
    """B04 — THE PROBLEM. Marcus picks from eight options; the model authors the piece."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE PROBLEM")
        _three_lines(
            self,
            "Picking is not authoring.",
            "The blue palette? The model chose.",
            "The centered layout? The model chose.",
            accent_line=0,
        )
        self.wait(1.0)


class Scene_B05_NbbAiCreative(Scene):
    """B05 — THE MECHANISM. Nicholas's void — fluent surface, absent author."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE MECHANISM")
        _layer_stack(
            self,
            [
                "Polished output",
                "The void underneath",
                "No one decided",
            ],
            accent_top=True,
        )
        _caption(self, "Fluent form, absent author.")
        self.wait(1.0)


class Scene_B06_NbbAiCreative(Scene):
    """B06 — THE MECHANISM. Authorship = decisions written down; iterations without them = nothing."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE MECHANISM")
        _two_bar(self, "Iterations", 30, "Decisions", 85, right_accent=True)
        _caption(self, "Small load-bearing decisions are what author the work.")
        self.wait(1.0)


class Scene_B07_NbbAiCreative(Scene):
    """B07 — THE MECHANISM. The fix is writing down; intent cannot be delegated."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE MECHANISM")
        _three_lines(
            self,
            "Not less AI.",
            "Write it down first.",
            "Intent cannot be delegated.",
            accent_line=2,
        )
        self.wait(1.0)


class Scene_B08_NbbAiCreative(Scene):
    """B08 — THE EXAMPLE. Seth's two builds — one prompt vs three files first."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE EXAMPLE")
        _layer_stack(
            self,
            [
                "One prompt. No files.",
                "Three files first",
                "Same Claude. Different agent.",
            ],
            accent_top=True,
        )
        _caption(self, "Build two: the work was his.")
        self.wait(1.0)


class Scene_B09_NbbAiCreative(Scene):
    """B09 — THE PRACTICE. Before Claude touches the file: made of / looks like / for."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "THE PRACTICE")
        _layer_stack(
            self,
            [
                "Made of",
                "Looks like",
                "For",
            ],
            accent_top=True,
        )
        _caption(self, "Silence is delegation.")
        self.wait(1.0)


class Scene_B10_NbbAiCreative(Scene):
    """B10 — RECAP. AI executes, you judge, write the judgment first."""
    def construct(self):
        self.camera.background_color = BG
        _act(self, "RECAP")
        _three_lines(
            self,
            "AI: execution.",
            "You: judgment.",
            "Write the judgment first.",
            accent_line=2,
        )
        self.wait(1.0)
