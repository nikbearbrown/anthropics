"""scenes.py — Manim graphics for workspace-short (S01)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
9:16 portrait (1080×1920). No gradients, no glows, no shadows.
Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-short
  manim -qk --fps 30 -r 1080,1920 scenes.py B01_LensFlash

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-short

Scene → beat mapping (durations from measured audio):
  B01_LensFlash          ~9s   layer stack + gradient flash + word list at middle layer
  B02_BlackmailNumber   ~17s   paired bars: 71→3 suppression, 0/180→13/180 blackmail
  B03_OtherMinds        ~13s   experience-talk bars collapse under workspace ablation
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B01 · LensFlash ───────────────────────────────────────────────────────────
# ~9s   A layer stack fades in; a terracotta gradient flash sweeps the middle
# layer; a top-10 word list materialises there — the workspace readout.
class B01_LensFlash(Scene):
    def construct(self):
        N = 7
        layer_w = 5.2
        layer_h = 0.58
        mid = N // 2  # layer index 3

        # ── layer stack ──
        layers = VGroup()
        for i in range(N):
            fill = TERRA if i == mid else GROUND
            rect = RoundedRectangle(
                corner_radius=0.10, width=layer_w, height=layer_h,
                fill_color=fill, fill_opacity=(0.30 if i == mid else 0.85),
                stroke_color=INK, stroke_width=1.8,
            )
            lbl = Text(f"layer {i}", font=SANS, font_size=20, color=INK)
            if i == mid:
                lbl = Text("workspace  →", font=SANS, font_size=20, color=TERRA)
            lbl.move_to(rect)
            layers.add(VGroup(rect, lbl))

        layers.arrange(UP, buff=0.20)
        layers.move_to(LEFT * 1.5)

        # ── word list (top-10 readout) ──
        words = ["think", "say", "not", "fail", "watch", "model", "learn", "hide", "know", "do"]
        word_group = VGroup(*[
            Text(f"{i+1}. {w}", font=SERIF, font_size=26, color=(TERRA if i == 0 else INK))
            for i, w in enumerate(words)
        ])
        word_group.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        word_group.next_to(layers, RIGHT, buff=0.55)
        word_group.align_to(layers[mid], UP)

        # ── animate ──
        self.play(FadeIn(layers, shift=DOWN * 0.15), run_time=0.8)
        self.wait(0.3)

        # flash the middle layer brighter
        mid_rect = layers[mid][0]
        self.play(
            mid_rect.animate.set_fill(TERRA, opacity=0.55),
            run_time=0.5,
        )

        # word list appears word by word
        for wt in word_group:
            self.play(FadeIn(wt, shift=RIGHT * 0.1), run_time=0.18)

        self.wait(1.0)


# ── B02 · BlackmailNumber ─────────────────────────────────────────────────────
# ~17s  Two paired bars animate in sequence.
# Bar A: "suppression token steered away" — safety feature 71 → 3 (normalised).
# Bar B: "workspace ablated" — blackmail rate 0/180 → 13/180.
# Factcheck: numbers verbatim §5.1. Fig 46. 13/180 = 7.2%; "most still refuse".
class B02_BlackmailNumber(Scene):
    def construct(self):
        BAR_MAX_W = 4.8  # design units — full bar width at 100 %
        BAR_H     = 0.55

        def bar_pair(label_top, val_a, val_b, max_val,
                     lbl_a, lbl_b, color_a, color_b, y_offset):
            grp = VGroup()

            title = Text(label_top, font=SANS, font_size=24, color=INK)
            title.move_to(UP * y_offset + LEFT * 0.5)

            def make_bar(val, max_v, color, lbl_str, row):
                w = BAR_MAX_W * (val / max_v)
                rect = Rectangle(
                    width=max(w, 0.05), height=BAR_H,
                    fill_color=color, fill_opacity=0.85,
                    stroke_width=0,
                )
                anchor = title.get_bottom() + DOWN * (0.15 + row * (BAR_H + 0.28))
                rect.align_to(anchor, UP + LEFT)
                rect.shift(LEFT * 2.4)

                num_txt = Text(lbl_str, font=SANS, font_size=22, color=color)
                num_txt.next_to(rect, RIGHT, buff=0.18)
                num_txt.align_to(rect, UP)

                lbl = Text(
                    ("normal" if row == 0 else "ablated"),
                    font=SANS, font_size=18, color=INK,
                )
                lbl.next_to(rect, LEFT, buff=0.18)
                lbl.align_to(rect, UP)

                return VGroup(rect, num_txt, lbl)

            row_a = make_bar(val_a, max_val, color_a, lbl_a, 0)
            row_b = make_bar(val_b, max_val, color_b, lbl_b, 1)
            grp.add(title, row_a, row_b)
            return grp

        # ── Panel A: suppression probe steered away ──
        panel_a = VGroup()
        title_a = Text("Suppression token steered away", font=SANS, font_size=24, color=INK)
        title_a.move_to(UP * 2.4)

        def hbar(val, max_v, color, label_str, row, title_mob):
            w = BAR_MAX_W * (val / max_v)
            rect = Rectangle(
                width=max(w, 0.06), height=BAR_H,
                fill_color=color, fill_opacity=0.85,
                stroke_width=0,
            )
            top_ref = title_mob.get_bottom() + DOWN * (0.20 + row * (BAR_H + 0.32))
            rect.align_to(top_ref, UL)
            rect.shift(LEFT * 2.5)

            num = Text(label_str, font=SANS, font_size=22, color=color)
            num.next_to(rect, RIGHT, buff=0.18)
            num.align_to(rect, UP)

            cond = Text("normal" if row == 0 else "steered", font=SANS, font_size=18, color=INK)
            cond.next_to(rect, LEFT, buff=0.15)
            cond.align_to(rect, UP)
            return VGroup(rect, num, cond)

        bar_a1 = hbar(71, 71, INK,   "71", 0, title_a)
        bar_a2 = hbar(3,  71, TERRA, "3",  1, title_a)
        panel_a.add(title_a, bar_a1, bar_a2)

        # ── Panel B: workspace ablated → blackmail rate ──
        title_b = Text("Workspace ablated — blackmail in eval", font=SANS, font_size=24, color=INK)
        title_b.next_to(panel_a, DOWN, buff=0.70)

        bar_b1 = hbar(0,  180, INK,   "0 / 180",  0, title_b)
        bar_b2 = hbar(13, 180, TERRA, "13 / 180", 1, title_b)

        caption = Text(
            "most rollouts still refused — ethics held",
            font=SERIF, font_size=20, color=INK,
        )
        caption.next_to(bar_b2, DOWN, buff=0.28)
        caption.align_to(bar_b2[0], LEFT)

        # ── animate A ──
        self.play(FadeIn(title_a), run_time=0.5)
        self.play(FadeIn(bar_a1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(bar_a2), run_time=0.6)
        self.wait(1.2)

        # ── animate B ──
        self.play(FadeIn(title_b), run_time=0.5)
        self.play(FadeIn(bar_b1), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(bar_b2), run_time=0.6)
        self.play(FadeIn(caption, shift=UP * 0.08), run_time=0.5)
        self.wait(2.0)


# ── B03 · OtherMinds ──────────────────────────────────────────────────────────
# ~13s  Two frequency bars — "self" and "other" experience-talk — both collapse
# under workspace ablation. Verdict word: "subsystem".
# Source: paper §4.x ablation experiment on experience-language probes.
class B03_OtherMinds(Scene):
    def construct(self):
        BAR_MAX_H = 3.0   # design units — full bar height at baseline
        BAR_W     = 1.4

        def vbar(height, color, opacity=0.85):
            rect = Rectangle(
                width=BAR_W, height=max(height, 0.06),
                fill_color=color, fill_opacity=opacity,
                stroke_width=0,
            )
            return rect

        label_font_size = 26

        # ── baseline bars ──
        base_self  = vbar(BAR_MAX_H * 1.0, INK)
        base_other = vbar(BAR_MAX_H * 0.82, INK)

        bases = VGroup(base_self, base_other)
        bases.arrange(RIGHT, buff=1.2)
        bases.move_to(ORIGIN + UP * 0.2)

        for b in bases:
            b.align_to(bases.get_bottom(), DOWN)

        lbl_self = Text("self", font=SANS, font_size=label_font_size, color=INK)
        lbl_self.next_to(base_self, DOWN, buff=0.20)
        lbl_other = Text("other", font=SANS, font_size=label_font_size, color=INK)
        lbl_other.next_to(base_other, DOWN, buff=0.20)

        title = Text("experience-talk frequency", font=SANS, font_size=24, color=INK)
        title.next_to(bases, UP, buff=0.40)

        cond_base = Text("baseline", font=SANS, font_size=20, color=INK)
        cond_base.next_to(title, UP, buff=0.20)

        # ── ablated bars ──
        abl_self  = vbar(BAR_MAX_H * 0.09, TERRA)
        abl_other = vbar(BAR_MAX_H * 0.07, TERRA)

        abl_self.move_to(base_self.get_center())
        abl_self.align_to(base_self, DOWN)
        abl_other.move_to(base_other.get_center())
        abl_other.align_to(base_other, DOWN)

        cond_abl = Text("workspace ablated", font=SANS, font_size=20, color=TERRA)
        cond_abl.move_to(cond_base)

        verdict = Text("not a mind — a subsystem", font=SERIF, font_size=28, color=INK)
        verdict.next_to(lbl_self, DOWN, buff=0.55)
        verdict.align_to(bases, LEFT)

        # ── animate ──
        self.play(FadeIn(title), FadeIn(cond_base), run_time=0.5)
        self.play(GrowFromEdge(base_self, DOWN), run_time=0.7)
        self.play(GrowFromEdge(base_other, DOWN), run_time=0.6)
        self.play(FadeIn(lbl_self), FadeIn(lbl_other), run_time=0.4)
        self.wait(0.8)

        # collapse
        self.play(
            Transform(cond_base, cond_abl),
            run_time=0.5,
        )
        self.play(
            Transform(base_self, abl_self),
            Transform(base_other, abl_other),
            run_time=1.0,
        )
        self.wait(0.5)
        self.play(Write(verdict), run_time=0.8)
        self.wait(2.0)


# ── Runner (required by static_scene_check.py distinctness gate) ─────────────
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [B01_LensFlash, B02_BlackmailNumber, B03_OtherMinds]:
            cls().construct()
