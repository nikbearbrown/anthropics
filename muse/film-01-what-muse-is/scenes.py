"""scenes.py — What Muse Is (Film 1 of the Muse series).
14 Manim scenes, M01–M14. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat."""
from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.25, width=11.5, height=2.6,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = VGroup(plate, t)
    if sub is not None:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


def bullet(pos, color=ACCENT, r=0.12):
    return Dot(point=[pos[0], pos[1], 0], radius=r, color=color)


def check_mark(pos, scale=1.0, color=GREEN):
    return VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4, color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


def labeled_box(label, pos, w=3.4, h=1.6, box_color=INK, label_size=36):
    box = Rectangle(width=w, height=h, stroke_color=box_color, stroke_width=4,
                    fill_color=CARD, fill_opacity=1).move_to(pos)
    lab = Text(label, font_size=label_size, color=INK).move_to(box.get_center())
    return VGroup(box, lab)


class M01_Bidea(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.3, width=12.4, height=6.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        hook = Text("one company builds the models", font_size=52, color=INK)
        hook2 = Text("and the harness?", font_size=52, color=ACCENT)
        hook.move_to([-0.0, 2.2, 0])
        hook2.next_to(hook, DOWN, buff=0.25)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=GREY, stroke_width=4).move_to([0, 1.1, 0])
        self.play(Write(hook), Create(rule))
        self.play(Write(hook2))
        b_models = labeled_box("models", [-3.4, -1.2, 0], box_color=ACCENT)
        b_harness = labeled_box("harness", [3.4, -1.2, 0], box_color=BLUE)
        self.play(Create(b_models[0]), Write(b_models[1]))
        self.play(Create(b_harness[0]), Write(b_harness[1]))
        arrow = Arrow(LEFT * 1.4, RIGHT * 1.4, color=INK, stroke_width=8).move_to([0, -1.2, 0])
        self.play(GrowArrow(arrow))
        merged = labeled_box("Meta", [0, -1.2, 0], w=4.2, h=1.8,
                             box_color=INK, label_size=44)
        self.play(FadeOut(b_models), FadeOut(b_harness), FadeOut(arrow),
                  Create(merged[0]), Write(merged[1]))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        head = Text("Four terms", font_size=48, color=INK).to_edge(UP, buff=0.7)
        head_rule = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
        head_rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(head_rule))
        terms = [
            ("Muse Spark", "Meta's managed model, called over the internet"),
            ("Muse Glimmer", "the open-weights model that runs on one graphics card"),
            ("Vertical integration", "one company building the models and the tools"),
            ("Token pricing", "paying per chunk of text, not per month"),
        ]
        xs = [-3.3, 3.3]
        ys = [0.9, -1.5]
        for i, (term, gloss) in enumerate(terms):
            x, y = xs[i % 2], ys[i // 2]
            card = RoundedRectangle(corner_radius=0.2, width=5.9, height=1.9,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, y, 0])
            dot = bullet([x - 2.55, y + 0.55, 0])
            t = Text(term, font_size=34, color=INK).move_to([x + 0.25, y + 0.55, 0])
            g = Text(gloss, font_size=24, color=GREY).move_to([x + 0.1, y - 0.45, 0])
            self.play(FadeIn(card), FadeIn(dot), Write(t), Write(g))
        self.wait(1.2)


class M03_B01(Scene):
    def construct(self):
        b_models = labeled_box("models", [-3.6, 0.4, 0], w=3.6, h=1.8, box_color=ACCENT)
        b_harness = labeled_box("harness", [3.6, 0.4, 0], w=3.6, h=1.8, box_color=BLUE)
        self.play(Create(b_models[0]), Write(b_models[1]))
        self.play(Create(b_harness[0]), Write(b_harness[1]))
        arrow = DoubleArrow(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=8).move_to([0, 0.4, 0])
        self.play(GrowArrow(arrow))
        merged = labeled_box("Meta", [0, 0.4, 0], w=5.2, h=2.0, box_color=INK, label_size=52)
        self.play(FadeOut(b_models), FadeOut(b_harness), FadeOut(arrow),
                  Create(merged[0]), Write(merged[1]))
        stack_arrow = Arrow(UP * 0.6, DOWN * 0.6, color=ACCENT, stroke_width=8).move_to([0, -2.2, 0])
        stack_lab = Text("the whole stack", font_size=32, color=INK).next_to(stack_arrow, DOWN, buff=0.25)
        self.play(GrowArrow(stack_arrow), Write(stack_lab))
        self.wait(1.2)


class M04_B02(Scene):
    def construct(self):
        marks = []
        for i, x in enumerate([-3.6, 0.0, 3.6]):
            sq = Square(side_length=1.6, stroke_color=GREY, stroke_width=4,
                        fill_color=CARD, fill_opacity=1).move_to([x, 0.6, 0])
            marks.append(sq)
            self.play(Create(sq))
        hl = SurroundingRectangle(marks[2], color=ACCENT, stroke_width=8, buff=0.25)
        lab = Text("a new option", font_size=40, color=ACCENT).move_to([3.6, -1.6, 0])
        tick = check_mark([3.6, -2.5, 0], scale=0.9)
        self.play(Create(hl), Write(lab))
        self.play(Create(tick[0]), Create(tick[1]))
        self.wait(1.2)


class M05_B03(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=7.6, height=2.4,
                                fill_color=ACCENT, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, 1.9, 0])
        title = Text("Muse Spark 1.2", font_size=52, color=CARD).move_to(card.get_center())
        self.play(FadeIn(card), Write(title))
        mods = ["text", "image", "video", "audio"]
        for i, m in enumerate(mods):
            x = -4.5 + i * 3.0
            dot = Dot(point=[x, -0.6, 0], radius=0.35, color=ACCENT)
            ring = Circle(radius=0.55, color=INK, stroke_width=4).move_to([x, -0.6, 0])
            lab = Text(m, font_size=32, color=INK).move_to([x, -1.7, 0])
            self.play(Create(ring), FadeIn(dot), Write(lab))
        self.wait(1.2)


class M06_B04(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=7.6, height=2.2,
                                fill_color=BLUE, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, 2.0, 0])
        title = Text("Muse Glimmer", font_size=52, color=CARD).move_to(card.get_center())
        self.play(FadeIn(card), Write(title))
        halo = Circle(radius=1.0, color=BLUE, stroke_width=5).move_to([-3.6, -0.8, 0])
        big = Text("30B", font_size=72, color=INK).move_to([-3.6, -0.8, 0])
        self.play(Create(halo), Write(big))
        chip = RoundedRectangle(corner_radius=0.35, width=3.4, height=1.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0.4, -0.8, 0])
        chip_lab = Text("one GPU", font_size=36, color=INK).move_to(chip.get_center())
        self.play(Create(chip), Write(chip_lab))
        tag = Rectangle(width=3.4, height=1.0, stroke_color=GREEN, stroke_width=4,
                        fill_color=CARD, fill_opacity=1).move_to([4.2, -0.8, 0])
        tag_lab = Text("open weights", font_size=32, color=GREEN).move_to(tag.get_center())
        self.play(Create(tag), Write(tag_lab))
        foot = Text("one graphics card \u00b7 100+ languages", font_size=30, color=GREY).move_to([0, -2.4, 0])
        foot_dot = bullet([-5.2, -2.4, 0], color=BLUE)
        self.play(FadeIn(foot_dot), Write(foot))
        self.wait(1.2)


class M07_B05(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.3, width=12.0, height=5.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        card = RoundedRectangle(corner_radius=0.2, width=5.2, height=2.2,
                                fill_color="#E4E1D8", fill_opacity=1,
                                stroke_color=GREY, stroke_width=3).move_to([-2.6, 0.4, 0])
        name = Text("Llama", font_size=52, color=GREY).move_to(card.get_center())
        self.play(Create(card), Write(name))
        gloss = Text("the famous sibling", font_size=36, color=INK).move_to([2.6, 0.4, 0])
        dot = bullet([0.4, 0.4, 0], color=GREY)
        self.play(FadeIn(dot), Write(gloss))
        self.wait(1.2)


class M08_B06(Scene):
    def construct(self):
        base = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=4).move_to([0, -2.2, 0])
        self.play(Create(base))
        heights = [1.2, 2.0, 2.6, 3.4, 1.6]
        for i, h in enumerate(heights):
            x = -4.4 + i * 2.2
            bar = Rectangle(width=1.2, height=h, fill_color=GREY, fill_opacity=1,
                            stroke_color=INK, stroke_width=2)
            bar.move_to([x, -2.2 + h / 2, 0])
            self.play(GrowFromEdge(bar, DOWN))
        hl_bar = Rectangle(width=1.2, height=3.4, fill_color=ACCENT, fill_opacity=1,
                           stroke_color=INK, stroke_width=3)
        hl_bar.move_to([-4.4 + 3 * 2.2, -2.2 + 3.4 / 2, 0])
        self.play(FadeIn(hl_bar))
        lab1 = Text("upper-middle", font_size=38, color=ACCENT).move_to([2.2, 2.0, 0])
        lab2 = Text("the instructor's Goldilocks reading", font_size=30, color=INK).move_to([2.2, 1.2, 0])
        pointer = Arrow([2.2, 0.9, 0], [2.2, -0.3, 0], color=ACCENT, stroke_width=6)
        self.play(Create(pointer), Write(lab1), Write(lab2))
        self.wait(1.2)


class M09_B07(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=8.6, height=2.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, 1.8, 0])
        t = Text("no subscription", font_size=52, color=INK).move_to(card.get_center())
        self.play(FadeIn(card), Write(t))
        strike = Line(LEFT * 3.6, RIGHT * 3.6, color=ACCENT, stroke_width=10).move_to(card.get_center())
        self.play(Create(strike))
        meter_bg = RoundedRectangle(corner_radius=0.3, width=9.0, height=1.1,
                                    fill_color="#E4E1D8", fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([0, -0.9, 0])
        self.play(Create(meter_bg))
        meter_fill = RoundedRectangle(corner_radius=0.3, width=6.2, height=0.8,
                                      fill_color=ACCENT, fill_opacity=1,
                                      stroke_color=ACCENT, stroke_width=2).move_to([-1.2, -0.9, 0])
        cap = Text("pay per token, not per month", font_size=36, color=INK).move_to([0, -2.3, 0])
        self.play(GrowFromEdge(meter_fill, LEFT), Write(cap))
        self.wait(1.2)


class M10_B08(Scene):
    def construct(self):
        head_std = Text("Standard", font_size=44, color=INK).move_to([-3.2, 2.4, 0])
        head_con = Text("Contributor", font_size=44, color=BLUE).move_to([3.2, 2.4, 0])
        self.play(Write(head_std))
        self.play(Write(head_con))
        price_lab = Text("price", font_size=32, color=GREY).move_to([-5.6, 1.2, 0])
        price_std = Rectangle(width=3.4, height=0.7, fill_color=GREY, fill_opacity=1,
                              stroke_color=INK, stroke_width=2).move_to([-3.2, 1.2, 0])
        self.play(Write(price_lab), Create(price_std))
        price_con = Rectangle(width=1.4, height=0.7, fill_color=BLUE, fill_opacity=1,
                              stroke_color=INK, stroke_width=2).move_to([2.2, 1.2, 0])
        self.play(Create(price_con))
        rate_lab = Text("rate limit", font_size=32, color=GREY).move_to([-5.6, -0.4, 0])
        rate_std = Rectangle(width=3.4, height=0.7, fill_color=GREY, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to([-3.2, -0.4, 0])
        self.play(Write(rate_lab), Create(rate_std))
        rate_con = Rectangle(width=0.8, height=0.7, fill_color=ACCENT, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to([1.9, -0.4, 0])
        self.play(Create(rate_con))
        verdict = Text("cheap and slow, or standard and fast", font_size=32, color=INK).move_to([0, -2.2, 0])
        vdot = bullet([-4.6, -2.2, 0])
        self.play(FadeIn(vdot), Write(verdict))
        self.wait(1.2)


class M11_B09(Scene):
    def construct(self):
        chips = [
            ("$1.25 in", -4.2),
            ("$4.25 out", 0.0),
            ("$0.10 in / $0.20 out", 4.2),
        ]
        for label, x in chips:
            chip = RoundedRectangle(corner_radius=0.35, width=3.6, height=1.3,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 1.2, 0])
            t = Text(label, font_size=36, color=INK).move_to(chip.get_center())
            self.play(Create(chip), Write(t))
        cap = Text("$20\u201350 a month, heavy use", font_size=36, color=INK).move_to([0, -1.2, 0])
        coin = Circle(radius=0.35, fill_color="#E8B93C", fill_opacity=1,
                      stroke_color=INK, stroke_width=3).move_to([-4.4, -1.2, 0])
        self.play(Create(coin), Write(cap))
        note = Text("at launch: no batch pricing", font_size=30, color=GREY).move_to([0, -2.4, 0])
        ndot = bullet([-3.6, -2.4, 0], color=GREY)
        self.play(FadeIn(ndot), Write(note))
        self.wait(1.2)


class M12_B10(Scene):
    def construct(self):
        b_want = labeled_box("you want", [-4.2, 0.6, 0], w=3.0, h=1.5)
        self.play(Create(b_want[0]), Write(b_want[1]))
        a1 = Arrow([-2.4, 0.6, 0], [-1.2, 0.6, 0], color=INK, stroke_width=8)
        self.play(GrowArrow(a1))
        b_agent = labeled_box("the agent", [0, 0.6, 0], w=3.0, h=1.5, box_color=ACCENT)
        self.play(Create(b_agent[0]), Write(b_agent[1]))
        a2 = Arrow([1.8, 0.6, 0], [3.0, 0.6, 0], color=INK, stroke_width=8)
        self.play(GrowArrow(a2))
        b_merch = labeled_box("merchant", [4.6, 0.6, 0], w=3.0, h=1.5, box_color=BLUE)
        self.play(Create(b_merch[0]), Write(b_merch[1]))
        coin = Circle(radius=0.4, fill_color="#E8B93C", fill_opacity=1,
                      stroke_color=INK, stroke_width=3).move_to([4.6, -0.9, 0])
        meta_lab = Text("Meta", font_size=40, color=INK).move_to([4.6, -1.9, 0])
        drop = Arrow([4.6, -0.2, 0], [4.6, -0.6, 0], color=ACCENT, stroke_width=6)
        self.play(Create(drop), Create(coin), Write(meta_lab))
        layer = Text("the intent layer", font_size=34, color=GREY).move_to([0, -2.6, 0])
        ldot = bullet([-2.6, -2.6, 0])
        self.play(FadeIn(ldot), Write(layer))
        self.wait(1.2)


class M13_B11(Scene):
    def construct(self):
        col_l = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=GREEN, stroke_width=4).move_to([-3.1, 0.6, 0])
        t_l1 = Text("for: cheap and fast,", font_size=32, color=INK).move_to([-3.1, 1.2, 0])
        t_l2 = Text("good enough", font_size=32, color=INK).move_to([-3.1, 0.4, 0])
        self.play(Create(col_l), Write(t_l1), Write(t_l2))
        col_r = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to([3.1, 0.6, 0])
        t_r1 = Text("limit: in Nik's experience,", font_size=28, color=INK).move_to([3.1, 1.2, 0])
        t_r2 = Text("less capable than the top models", font_size=28, color=INK).move_to([3.1, 0.4, 0])
        self.play(Create(col_r), Write(t_r1), Write(t_r2))
        stamp = Rectangle(width=2.6, height=1.1, stroke_color=ACCENT, stroke_width=6,
                          fill_opacity=0).move_to([0, -2.3, 0]).rotate(8 * DEGREES)
        stamp_t = Text("honest", font_size=44, color=ACCENT).move_to(stamp.get_center()).rotate(8 * DEGREES)
        self.play(Create(stamp), Write(stamp_t))
        self.wait(1.2)


class M14_BvdtHtfOut(Scene):
    def construct(self):
        # --- recap: four lines, one per act ---
        plate = RoundedRectangle(corner_radius=0.25, width=12.2, height=6.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        recap_lines = [
            "Act 1: vertical integration \u2014 Meta builds the models and the tools",
            "Act 2: Spark, managed and multimodal; Glimmer, open weights, one graphics card",
            "Act 3: pay per token, not per month; sharing data buys a deep discount",
            "Act 4: Meta bets on transaction fees, within honest limits",
        ]
        recap_mobs = []
        for i, ln in enumerate(recap_lines):
            y = 1.9 - i * 1.15
            d = bullet([-5.5, y, 0])
            t = Text(ln, font_size=27, color=INK).move_to([-4.9, y, 0])
            # left-align: shift so text starts near the bullet
            t.shift(RIGHT * (t.width / 2 - 0.2))
            recap_mobs.extend([d, t])
            self.play(FadeIn(d), Write(t))
        # --- your turn ---
        self.play(*[FadeOut(m) for m in recap_mobs], FadeOut(plate))
        yt_card = RoundedRectangle(corner_radius=0.25, width=11.6, height=4.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=ACCENT, stroke_width=4).move_to(ORIGIN)
        yt_head = Text("Your turn.", font_size=48, color=ACCENT).move_to([0, 1.5, 0])
        self.play(FadeIn(yt_card), Write(yt_head))
        steps = [
            "Open the playground. Set a spend limit. Run one prompt.",
            "Did it answer? What did it cost?",
        ]
        step_mobs = []
        for i, s in enumerate(steps):
            y = 0.3 - i * 1.0
            cm = check_mark([-5.0, y, 0], scale=0.8)
            t = Text(s, font_size=32, color=INK).move_to([-4.2, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            step_mobs.extend([cm, t])
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        # --- outro ---
        self.play(*[FadeOut(m) for m in step_mobs], FadeOut(yt_card), FadeOut(yt_head))
        out = title_card("What Muse Is", "@NikBearBrown")
        self.play(FadeIn(out[0]), Write(out[1]), Write(out[2]))
        nxt = Text("Next: Your First Prompts", font_size=36, color=GREY).move_to([0, -2.6, 0])
        ndot = bullet([-3.4, -2.6, 0], color=ACCENT)
        self.play(FadeIn(ndot), Write(nxt))
        self.wait(1.2)
