from manim import *

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY  = "#56B4E9"
BLUE = "#0072B2"
GREEN= "#009E73"
VERM = "#D55E00"
GRAY = "#7c7c7c"

COLS = [SKY, SKY, BLUE, GREEN, VERM, VERM]

HUB = 2          # index of the hub node (p53)

# Standard node: w=1.85, h=1.05   Hub: 25% larger → w=2.3125, h=1.3125
# Edge-gap-based placement keeps all nodes within the ±7.11 half-width.
NODE_W = 1.85
NODE_H = 1.05
HUB_SCALE = 1.25

# Gap between adjacent node EDGES = 0.40 units (uniform).
# Total span outer edges: ±6.78 — safely inside the 7.11 Manim half-width.
_GAP = 0.40

def _node_widths():
    return [NODE_W * (HUB_SCALE if i == HUB else 1.0) for i in range(6)]

def _compute_xs():
    """Place node centres so edge-gaps are uniform; then shift to centre the group."""
    ws = _node_widths()
    xs = [0.0]
    for i in range(1, 6):
        xs.append(xs[-1] + ws[i - 1] / 2 + _GAP + ws[i] / 2)
    # Centre: total span midpoint
    mid = (xs[0] + xs[-1]) / 2
    return [x - mid for x in xs]

XS = _compute_xs()  # recomputed at import time; centred, no overlaps


def make_nodes():
    nodes = VGroup()
    for i, x in enumerate(XS):
        is_hub = (i == HUB)
        w = NODE_W * (HUB_SCALE if is_hub else 1.0)
        h = NODE_H * (HUB_SCALE if is_hub else 1.0)
        sw = 4.2 if is_hub else 3.2
        n = RoundedRectangle(
            width=w, height=h, corner_radius=0.18,
            color=COLS[i],
            fill_color=COLS[i], fill_opacity=0.16,
            stroke_width=sw,
        ).move_to([x, 0, 0])
        nodes.add(n)
    return nodes


def make_arrows(nodes):
    arrows = VGroup()
    for i in range(5):
        a = Arrow(
            start=nodes[i].get_right(),
            end=nodes[i + 1].get_left(),
            buff=0.10,
            color=GRAY,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.12,
            max_stroke_width_to_length_ratio=6,
        )
        arrows.add(a)
    return arrows


# ============================================================
# B05_P53Circuit — initial animation
#   LaggedStart node reveal → LaggedStart arrow grow → Flash hub
# ============================================================
class B05_P53Circuit(Scene):
    def construct(self):
        nodes  = make_nodes()
        arrows = make_arrows(nodes)
        hub    = nodes[HUB]

        # 1. LaggedStart node reveal left → right
        self.play(
            LaggedStart(
                *[FadeIn(n, shift=RIGHT * 0.3) for n in nodes],
                lag_ratio=0.18,
                run_time=1.6,
            )
        )

        # 2. LaggedStart arrow grow
        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.14,
                run_time=1.4,
            )
        )

        # 3. Flash the hub — shows it is the control pivot
        self.play(
            Flash(
                hub.get_center(),
                color=BLUE,
                line_length=0.40,
                num_lines=16,
                flash_radius=1.40,
            ),
            hub.animate.scale(1.12),
            run_time=0.5,
        )
        self.play(hub.animate.scale(1 / 1.12), run_time=0.35)
        self.wait(0.8)


# ============================================================
# B07_P53CircuitBroken — stagger reveal + hub collapse
#   node0 → arrow0 → node1 → arrow1 → … (tight stagger)
#   then Flash → collapse (hub dims, X-mark, downstream fade)
# ============================================================
class B07_P53CircuitBroken(Scene):
    def construct(self):
        nodes  = make_nodes()
        arrows = make_arrows(nodes)
        hub    = nodes[HUB]

        # 1. Stagger: node → arrow → node → arrow …
        self.play(FadeIn(nodes[0], shift=RIGHT * 0.3), run_time=0.35)
        for i in range(5):
            self.play(GrowArrow(arrows[i]), run_time=0.38)
            self.play(FadeIn(nodes[i + 1], shift=RIGHT * 0.3), run_time=0.35)

        self.wait(0.25)

        # 2. Flash the hub — pivot moment
        self.play(
            Flash(
                hub.get_center(),
                color=BLUE,
                line_length=0.40,
                num_lines=16,
                flash_radius=1.40,
            ),
            hub.animate.scale(1.12),
            run_time=0.5,
        )
        self.play(hub.animate.scale(1 / 1.12), run_time=0.35)
        self.wait(0.40)

        # 3. Collapse sequence — p53 loss breaks the chain
        # X-mark at hub centre
        xmark = VGroup(
            Line(
                hub.get_center() + UP * 0.22 + LEFT * 0.22,
                hub.get_center() + DOWN * 0.22 + RIGHT * 0.22,
                color=VERM, stroke_width=8,
            ),
            Line(
                hub.get_center() + DOWN * 0.22 + LEFT * 0.22,
                hub.get_center() + UP * 0.22 + RIGHT * 0.22,
                color=VERM, stroke_width=8,
            ),
        )

        # Dim hub, show X-mark, fade downstream arrows
        self.play(
            hub.animate.set_fill(BLUE, opacity=0.07).set_stroke(opacity=0.30),
            FadeIn(xmark),
            arrows[2].animate.set_opacity(0.15),
            arrows[3].animate.set_opacity(0.15),
            arrows[4].animate.set_opacity(0.15),
            run_time=0.8,
        )
        # Also dim downstream nodes
        self.play(
            nodes[3].animate.set_fill(GREEN, opacity=0.06).set_stroke(opacity=0.25),
            nodes[4].animate.set_fill(VERM, opacity=0.06).set_stroke(opacity=0.25),
            nodes[5].animate.set_fill(VERM, opacity=0.06).set_stroke(opacity=0.25),
            run_time=0.5,
        )
        self.wait(0.8)
