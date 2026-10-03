from manim import *

INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"


def _boxed(text_mob, pad_w=0.20, pad_h=0.12, fill=CREAM):
    """Place a cream background under a text mobject wider than the text itself."""
    w = text_mob.width + pad_w
    h = text_mob.height + pad_h
    bg = Rectangle(width=w, height=h,
                   fill_color=ManimColor(fill), fill_opacity=1.0,
                   stroke_width=0, stroke_opacity=0).move_to(text_mob.get_center())
    return VGroup(bg, text_mob)


class B04_LNPEscape(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title = Text("LNP ENDOSOMAL ESCAPE: 1-2% SUCCESS RATE", font="Georgia",
                     font_size=22, color=ManimColor(INK), weight=BOLD).move_to([0, 3.2, 0])

        lnp = Circle(radius=0.35, fill_color=ManimColor(GOLD), fill_opacity=0.9,
                     stroke_width=2, stroke_color=ManimColor(INK)).move_to([-0.9, 2.2, 0])
        lnp_t = Text("LNP (mRNA)", font="Georgia", font_size=14,
                     color=ManimColor(INK)).move_to([0.4, 2.2, 0])
        lnp_group = VGroup(lnp, _boxed(lnp_t))

        arr1 = Arrow([-0.9, 1.75, 0], [-0.9, 1.2, 0], stroke_width=2,
                     color=ManimColor(INK), buff=0.0, max_tip_length_to_length_ratio=0.25)

        end_box = Rectangle(width=3.2, height=0.9,
                            fill_color=ManimColor(SLATE), fill_opacity=0.3,
                            stroke_width=2, stroke_color=ManimColor(INK),
                            stroke_opacity=1.0).move_to([-0.9, 0.6, 0])
        end_t = Text("ENDOSOME", font="Georgia", font_size=16,
                     color=ManimColor(INK)).move_to([-0.9, 0.85, 0])
        end_boxed = _boxed(end_t, pad_w=0.35)
        ph_t = Text("pH 7.4 -> 5.5 · lipid ionizes", font="Georgia", font_size=12,
                    color=ManimColor(CRIMSON)).move_to([-0.9, 0.35, 0])
        ph_boxed = _boxed(ph_t, pad_w=0.30)
        endosome = VGroup(end_box, end_boxed, ph_boxed)

        ionize_t = Text("ALC-0315 / SM-102", font="Georgia", font_size=12,
                        color=ManimColor(CRIMSON)).move_to([2.5, 1.0, 0])
        ionize_sub = Text("(ionizable lipid)", font="Georgia", font_size=10,
                          color=ManimColor(CRIMSON)).move_to([2.5, 0.7, 0])
        ionize_label = VGroup(_boxed(ionize_t, pad_w=0.30), _boxed(ionize_sub, pad_w=0.30))

        arr_lys = Arrow([-1.6, 0.1, 0], [-3.2, -0.9, 0], stroke_width=2,
                        color=ManimColor(CRIMSON), buff=0.05,
                        max_tip_length_to_length_ratio=0.25)
        lys_box = Rectangle(width=3.4, height=0.9,
                            fill_color=ManimColor(CRIMSON), fill_opacity=0.8,
                            stroke_width=0, stroke_opacity=0).move_to([-3.6, -1.6, 0])
        lys_t = Text("LYSOSOME", font="Georgia", font_size=16,
                     color=ManimColor(CREAM), weight=BOLD).move_to([-3.6, -1.4, 0])
        lys_sub = Text("98-99% DEGRADED", font="Georgia", font_size=13,
                       color=ManimColor(CREAM)).move_to([-3.6, -1.8, 0])
        lysosome = VGroup(lys_box, lys_t, lys_sub)

        arr_cyt = Arrow([-0.2, 0.1, 0], [1.6, -0.9, 0], stroke_width=2,
                        color=ManimColor("#B48A00"), buff=0.05,
                        max_tip_length_to_length_ratio=0.25)
        cyt_box = Rectangle(width=3.4, height=0.9,
                            fill_color=ManimColor(GOLD), fill_opacity=0.9,
                            stroke_width=0, stroke_opacity=0).move_to([2.0, -1.6, 0])
        cyt_t = Text("CYTOPLASM", font="Georgia", font_size=16,
                     color=ManimColor(INK), weight=BOLD).move_to([2.0, -1.4, 0])
        cyt_sub = Text("1-2% escape -> protein", font="Georgia", font_size=13,
                       color=ManimColor(INK)).move_to([2.0, -1.8, 0])
        cytoplasm = VGroup(cyt_box, cyt_t, cyt_sub)

        imp_t = Text("10x escape gain -> 10x mRNA potency", font="Georgia",
                     font_size=15, color=ManimColor(INK),
                     weight=BOLD).move_to([-0.9, -2.7, 0])
        implication = _boxed(imp_t, pad_w=0.40)

        self.play(FadeIn(title), FadeIn(lnp_group), run_time=1.2)
        self.wait(2.0)
        self.play(FadeIn(arr1), FadeIn(end_box), FadeIn(end_boxed), run_time=1.2)
        self.wait(2.0)
        self.play(FadeIn(ph_boxed), FadeIn(ionize_label), run_time=1.2)
        self.wait(3.0)
        self.play(FadeIn(arr_lys), FadeIn(lysosome), run_time=1.4)
        self.wait(2.5)
        self.play(FadeIn(arr_cyt), FadeIn(cytoplasm), run_time=1.4)
        self.wait(3.0)
        self.play(FadeIn(implication), run_time=1.2)
        self.wait(4.0)
