"""scenes.py — claude-constitution-three-principals

PrincipalHierarchy: animated 3-tier authority stack.
Anthropic (hardcoded) → Operator (system prompt) → User (conversation).
Each tier reveals top-to-bottom; arrows draw in between them.
"""
from manim import *

CREAM    = "#FAF9F5"
INK      = "#3D3929"
TERRA    = "#D97757"
CHARCOAL = "#2A2720"

TIER_W = 6.5
TIER_H = 1.05
GAP    = 0.55

TIERS = [
    ("ANTHROPIC",    "Training rules — hardcoded"),
    ("OPERATOR",     "System prompt"),
    ("USER",         "Conversation"),
]


class PrincipalHierarchy(Scene):
    def construct(self):
        self.camera.background_color = CHARCOAL

        # Build tier boxes (top → bottom, centred)
        total_h = len(TIERS) * TIER_H + (len(TIERS) - 1) * GAP
        top_y   = total_h / 2 - TIER_H / 2

        boxes, labels = [], []
        for i, (title, sub) in enumerate(TIERS):
            y = top_y - i * (TIER_H + GAP)
            rect = RoundedRectangle(
                width=TIER_W, height=TIER_H,
                corner_radius=0.08, color=CREAM,
                fill_opacity=0.0, stroke_width=1.5,
            ).move_to([0, y, 0])

            t = Text(title, font="EB Garamond", font_size=22,
                     color=TERRA if i == 0 else CREAM, weight=BOLD)
            s = Text(sub,   font="EB Garamond", font_size=14, color=CREAM)
            grp = VGroup(t, s).arrange(DOWN, buff=0.12).move_to(rect)
            boxes.append(rect)
            labels.append(grp)

        # Arrows between tiers
        arrows = []
        for i in range(len(TIERS) - 1):
            start = boxes[i].get_bottom()
            end   = boxes[i + 1].get_top()
            mid   = (start + end) / 2
            arr   = Arrow(
                start + DOWN * 0.02, end - DOWN * 0.02,
                buff=0, stroke_width=1.2,
                color=CREAM, tip_length=0.15, max_stroke_width_to_length_ratio=90,
            ).set_opacity(0.5)
            arrows.append(arr)

        cap = Text("can restrict", font="EB Garamond",
                   font_size=11, color=CREAM).set_opacity(0.45)

        # ── Animation ───────────────────────────────────────────────────────
        self.wait(0.3)

        # Tier 1: Anthropic
        self.play(Create(boxes[0], run_time=0.5))
        self.play(FadeIn(labels[0], shift=UP * 0.1, run_time=0.4))
        self.wait(0.5)

        # Arrow 1 + "can restrict" label
        cap.next_to(arrows[0], RIGHT, buff=0.15)
        self.play(GrowArrow(arrows[0], run_time=0.5))
        self.play(FadeIn(cap.copy().next_to(arrows[0], RIGHT, buff=0.1), run_time=0.3))
        self.wait(0.2)

        # Tier 2: Operator
        self.play(Create(boxes[1], run_time=0.5))
        self.play(FadeIn(labels[1], shift=UP * 0.1, run_time=0.4))
        self.wait(0.5)

        # Arrow 2
        cap2 = Text("can restrict", font="EB Garamond",
                    font_size=11, color=CREAM).set_opacity(0.45)
        cap2.next_to(arrows[1], RIGHT, buff=0.10)
        self.play(GrowArrow(arrows[1], run_time=0.5))
        self.play(FadeIn(cap2, run_time=0.3))
        self.wait(0.2)

        # Tier 3: User
        self.play(Create(boxes[2], run_time=0.5))
        self.play(FadeIn(labels[2], shift=UP * 0.1, run_time=0.4))
        self.wait(1.5)

        # Pulse the Anthropic box (hardcoded = special)
        self.play(boxes[0].animate.set_stroke(TERRA, width=2.5), run_time=0.6)
        self.wait(1.0)

        # Fade to hold
        self.wait(2.0)
