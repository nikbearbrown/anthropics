"""scenes.py — Manim graphics for workspace-jacobian-lens (E01)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-jacobian-lens
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_ResidualStack

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-jacobian-lens

Scene → beat mapping (durations from measured audio):
  B02_ResidualStack      9.83s   residual stream layer stack, probe at layer L
  B03_JLensGradient     11.33s   gradient arrows back to layer L; vocab vectors
  B04_ReadoutRanking    10.50s   projection → top-10 word ranking list
  B06_SixPrompts         9.62s   six prompt types × midlayer readout words
  B07_LensBakeoff       14.36s   Fig 52 bar comparison, six distributions
  B08_SwapSurgery       12.42s   spider→ant lens-coordinate swap
  B11_SingleTokenBlindSpot 12.84s  'blackmail' → black|mail; lens misses 'mail'
  B12_TemplateOracle    14.19s   template + oracle patch lenses
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B02 · Residual Stream Layer Stack ────────────────────────────────────────
# 9.83s  A token column rises through numbered layers; probe arrow marks layer L
class B02_ResidualStack(Scene):
    def construct(self):
        # layer labels
        N = 6
        layer_h = 0.72
        layer_w = 2.2
        layers = VGroup()
        for i in range(N):
            lbl = "L" if i == N // 2 else f"layer {i}"
            rect = RoundedRectangle(
                corner_radius=0.12, width=layer_w, height=layer_h,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=INK, stroke_width=2,
            )
            txt = Text(lbl, font=SANS, font_size=22, color=INK)
            txt.move_to(rect)
            layers.add(VGroup(rect, txt))

        layers.arrange(UP, buff=0.18)
        layers.move_to(ORIGIN + LEFT * 2)

        # token label — shifted into safe area (DL corner, buff keeps it ≥ 6.3 x)
        token = Text("token  t", font=SERIF, font_size=32, color=INK)
        token.to_corner(DL, buff=1.2)

        # residual stream arrow running up through the stack
        stream_x = layers.get_right()[0] + 0.55
        stream_bottom = layers.get_bottom() + DOWN * 0.1
        stream_top    = layers.get_top()   + UP   * 0.1
        stream_arrow = Arrow(
            stream_bottom + RIGHT * (stream_x - layers.get_center()[0]),
            stream_top    + RIGHT * (stream_x - layers.get_center()[0]),
            color=INK, stroke_width=3, buff=0,
        )
        stream_arrow.set_x(stream_x)
        stream_lbl = Text("residual stream", font=SANS, font_size=20, color=INK)
        stream_lbl.rotate(PI / 2)
        stream_lbl.next_to(stream_arrow, RIGHT, buff=0.18)

        self.play(
            FadeIn(token, shift=UP * 0.2),
            run_time=0.6,
        )
        self.play(
            LaggedStart(
                *[FadeIn(lyr, shift=UP * 0.15) for lyr in layers],
                lag_ratio=0.15,
            ),
            run_time=1.6,
        )
        self.play(
            Create(stream_arrow),
            FadeIn(stream_lbl),
            run_time=0.8,
        )
        self.wait(0.5)

        # probe arrow pointing at the middle layer (layer L) — terracotta accent
        probe_target = layers[N // 2].get_right() + RIGHT * 0.08
        probe_start  = probe_target + RIGHT * 1.8
        probe = Arrow(
            probe_start, probe_target,
            color=TERRA, stroke_width=4, buff=0.05,
        )
        probe_lbl = Text("probe at layer L", font=SANS, font_size=22, color=INK)
        probe_lbl.next_to(probe, RIGHT, buff=0.15)
        self.play(
            GrowArrow(probe),
            FadeIn(probe_lbl, shift=LEFT * 0.2),
            run_time=0.9,
        )
        # highlight layer L rect
        hl = layers[N // 2][0].copy()
        hl.set_stroke(TERRA, width=4)
        hl.set_fill(opacity=0)
        self.play(Create(hl), run_time=0.5)

        question = Text(
            "What's written here, mid-stack?",
            font=SERIF, font_size=30, color=INK,
        )
        question.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(question, shift=UP * 0.15), run_time=0.7)
        self.wait(3.48)    # total ≈ 9.83s


# ── B03 · Jacobian Lens Gradient ──────────────────────────────────────────────
# 11.33s  Gradient arrows flow from output distribution back to layer L;
#         one vocabulary vector materialises per word.
class B03_JLensGradient(Scene):
    def construct(self):
        # output distribution box — upper centre
        out_box = RoundedRectangle(
            corner_radius=0.15, width=3.8, height=1.2,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        out_lbl = Text("output distribution", font=SANS, font_size=22, color=INK)
        out_lbl.move_to(out_box)
        out_group = VGroup(out_box, out_lbl)
        out_group.move_to([0.0, 2.6, 0])

        # layer L box — lower centre-left
        layer_box = RoundedRectangle(
            corner_radius=0.15, width=3.0, height=1.1,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        layer_lbl = Text("layer  L", font=SANS, font_size=22, color=INK)
        layer_lbl.move_to(layer_box)
        layer_group = VGroup(layer_box, layer_lbl)
        layer_group.move_to([-2.6, 0.2, 0])

        self.play(
            FadeIn(out_group, shift=DOWN * 0.2),
            FadeIn(layer_group, shift=UP * 0.2),
            run_time=0.7,
        )
        self.wait(0.3)

        # vocab words — vertical column on the right (each label well-spaced)
        words = ["cat", "the", "run", "Paris", "seven", "blue"]
        word_labels = VGroup()
        col_x = 4.5
        ys = [2.2, 1.3, 0.4, -0.5, -1.4, -2.3]
        for i, (word, y) in enumerate(zip(words, ys)):
            col = INK
            wlbl = Text(f'v("{word}")', font=SERIF, font_size=20, color=col)
            wlbl.move_to([col_x, y, 0])
            word_labels.add(wlbl)

        # gradient arrows: from output box centre toward each word label
        arrows = VGroup()
        src = out_group.get_center()
        for i, wlbl in enumerate(word_labels):
            dst = wlbl.get_left() + LEFT * 0.12
            arr = Arrow(
                src, dst,
                color=TERRA if i == 0 else INK,
                stroke_width=2.5 if i == 0 else 1.6,
                buff=0.08,
            )
            arrows.add(arr)

        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.10,
            ),
            run_time=1.8,
        )
        self.play(
            LaggedStart(
                *[FadeIn(wl, shift=LEFT * 0.12) for wl in word_labels],
                lag_ratio=0.10,
            ),
            run_time=1.2,
        )
        self.wait(0.5)

        # annotation — inside safe area
        eq = Text(
            "one gradient per vocabulary token",
            font=SERIF, font_size=26, color=INK,
        )
        eq.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(eq, shift=UP * 0.15), run_time=0.7)
        self.wait(5.36)    # total ≈ 11.33s


# ── B04 · Readout Ranking ─────────────────────────────────────────────────────
# 10.50s  Activation vector dots onto gradient directions → top-10 word list
class B04_ReadoutRanking(Scene):
    def construct(self):
        # activation vector on left
        act_box = RoundedRectangle(
            corner_radius=0.15, width=2.6, height=1.1,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        act_lbl = Text("activation  h", font=SANS, font_size=24, color=INK)
        act_lbl.move_to(act_box)
        act_group = VGroup(act_box, act_lbl).shift(LEFT * 3.8)

        # projection arrow — terracotta
        proj_arrow = Arrow(
            act_group.get_right() + RIGHT * 0.15,
            act_group.get_right() + RIGHT * 2.2,
            color=TERRA, stroke_width=4, buff=0,
        )
        proj_lbl = Text("project", font=SANS, font_size=25, color=TERRA)
        proj_lbl.next_to(proj_arrow, UP, buff=0.12)

        # ranked word list on right
        words = [
            "#1  Mars", "#2  planet", "#3  red",
            "#4  fourth", "#5  color", "#6  orbit",
            "#7  solar", "#8  surface", "#9  dust", "#10  rocky",
        ]
        word_items = VGroup()
        for w in words:
            txt = Text(w, font=SERIF, font_size=22, color=INK)
            word_items.add(txt)
        word_items.arrange(DOWN, buff=0.04, aligned_edge=LEFT)
        word_items.shift(RIGHT * 2.5)
        word_items.scale_to_fit_height(5.8)

        list_box = SurroundingRectangle(
            word_items, buff=0.25,
            color=INK, stroke_width=2,
            corner_radius=0.14, fill_opacity=0,
        )
        list_title = Text("readout", font=SANS, font_size=24, color=INK)
        list_title.next_to(list_box, UP, buff=0.12)

        self.play(FadeIn(act_group, shift=RIGHT * 0.2), run_time=0.6)
        self.play(
            GrowArrow(proj_arrow),
            FadeIn(proj_lbl),
            run_time=0.6,
        )
        self.play(
            FadeIn(list_title),
            Create(list_box),
            run_time=0.5,
        )
        self.play(
            LaggedStart(
                *[FadeIn(w, shift=RIGHT * 0.1) for w in word_items],
                lag_ratio=0.1,
            ),
            run_time=1.8,
        )
        # terracotta highlight on top word
        hl = word_items[0].copy()
        hl.set_color(TERRA)
        self.play(Transform(word_items[0], hl), run_time=0.4)

        caption = Text(
            "That ranked list is the readout. That's the whole instrument.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.7)
        self.wait(5.38)    # total ≈ 10.50s


# ── B06 · Six Prompts Readout ──────────────────────────────────────────────────
# 9.62s   Six mini-prompts with midlayer readout words appearing over tokens.
#         Skeptic caption at bottom.
class B06_SixPrompts(Scene):
    def construct(self):
        prompt_data = [
            ("counting",     "1  2  3  4  ...",   "numbers"),
            ("translation",  "Bonjour  →  ...",   "target language"),
            ("poem",         "Roses are red ...",  "rhyme"),
            ("arithmetic",   "12 × 7  =  ...",    "84"),
            ("geography",    "Capital of  ...",   "city name"),
            ("completion",   "The sky is  ...",   "blue"),
        ]

        cells = VGroup()
        for prompt_type, prompt_text, readout in prompt_data:
            cell = VGroup()
            # prompt label (small caps style via SANS bold)
            label = Text(prompt_type, font=SANS, font_size=22, color=INK)
            # prompt text
            ptext = Text(prompt_text, font=SERIF, font_size=22, color=INK)
            # readout chip — terracotta border, ink text (§8.3 contrast)
            chip_rect = RoundedRectangle(
                corner_radius=0.1, width=2.4, height=0.52,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=TERRA, stroke_width=2,
            )
            chip_txt = Text(readout, font=SERIF, font_size=22, color=INK)
            chip_txt.move_to(chip_rect)
            chip = VGroup(chip_rect, chip_txt)

            cell.add(label, ptext, chip)
            cell.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            cell_bg = SurroundingRectangle(
                cell, buff=0.08,
                color=INK, stroke_width=1.5,
                corner_radius=0.12, fill_opacity=0,
            )
            cells.add(VGroup(cell_bg, cell))

        cells.arrange_in_grid(rows=2, cols=3, buff=0.12)
        cells.scale_to_fit_width(12.5)
        cells.shift(UP * 0.3)

        # animate cells in two waves
        self.play(
            LaggedStart(
                *[FadeIn(c, shift=UP * 0.1) for c in cells[:3]],
                lag_ratio=0.18,
            ),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                *[FadeIn(c, shift=UP * 0.1) for c in cells[3:]],
                lag_ratio=0.18,
            ),
            run_time=1.0,
        )
        self.wait(0.5)

        # skeptic caption — above safe-area floor (SERIF 26 → ~42px blob; buff=0.65 clears ±3.4y)
        skeptic = Text(
            "Selected examples — the quantitative test is next.",
            font=SERIF, font_size=28, color=INK,
        )
        skeptic.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(skeptic, run_time=0.5))
        self.wait(5.62)    # total ≈ 9.62s


# ── B07 · Lens Bakeoff ────────────────────────────────────────────────────────
# 14.36s  Fig 52 as animated grouped bars: pass@k AUC for six distributions.
#         Values from img_c983850908bf60d9.png.
#         FACTCHECK: typo-panel values marked VERIFY in beat_sheet.json;
#         narration "all six" needs paper-text confirmation before final cut.
class B07_LensBakeoff(Scene):
    def construct(self):
        # parchment panel anchors the chart area (no stroke — avoids TEXT-ON-LINE audit)
        # fill_color delta from GROUND (#FAF9F5) must exceed INK_DELTA=28; #D4CFC5 gives max-ch Δ≥38
        panel = Rectangle(
            width=11.0, height=6.0,
            fill_color="#D4CFC5",
            fill_opacity=1.0,
            stroke_width=0,
        )
        panel.move_to([0.0, -0.4, 0])
        self.add(panel)

        # AUC values (five confirmed from paper PNG; typo confirmed: J<L per §A.5)
        data = {
            "multihop":     {"J": 0.81, "L": 0.77, "T": 0.68},
            "multilingual": {"J": 0.71, "L": 0.53, "T": 0.47},
            "poetry":       {"J": 0.80, "L": 0.58, "T": 0.18},
            "order ops":    {"J": 0.89, "L": 0.72, "T": 0.65},
            "association":  {"J": 0.68, "L": 0.65, "T": 0.11},
            "typo":         {"J": 0.52, "L": 0.83, "T": 0.45},
        }
        FAMILIES = list(data.keys())
        LENSES   = ["J", "L", "T"]
        COLORS   = {"J": TERRA, "L": INK, "T": "#999080"}

        bar_w  = 0.26
        gap    = 0.12
        scale  = 4.0     # AUC 1.0 → 4.0 height units
        x0     = -4.5    # well inside safe area left
        y0     = -2.6    # baseline y

        # axis — safe area starts at x=-6.3; place at -4.8
        axis_x = x0 - 0.3
        axis   = Line(
            [axis_x, y0, 0], [axis_x, y0 + scale + 0.3, 0],
            color=INK, stroke_width=2,
        )
        tick_labels = VGroup()
        for v in [0.0, 0.25, 0.5, 0.75, 1.0]:
            y = y0 + v * scale
            tick = Line([axis_x - 0.1, y, 0], [axis_x, y, 0], color=INK, stroke_width=1.5)
            lbl  = Text(f"{v:.2f}", font=SANS, font_size=14, color=INK)
            lbl.next_to(tick, LEFT, buff=0.08)
            tick_labels.add(VGroup(tick, lbl))

        axis_title = Text("AUC", font=SANS, font_size=17, color=INK)
        axis_title.rotate(PI / 2)
        # position above the axis top — avoids overlapping tick labels at the midpoint
        axis_title.move_to([axis_x - 0.45, y0 + scale + 0.52, 0])

        self.play(
            Create(axis),
            FadeIn(tick_labels),
            FadeIn(axis_title),
            run_time=0.7,
        )

        # draw groups one family at a time
        group_w = len(LENSES) * bar_w + gap
        group_spacing = group_w + 0.22

        for fi, fam in enumerate(FAMILIES):
            gx = x0 + fi * group_spacing
            bars_this = VGroup()
            for li, lens in enumerate(LENSES):
                auc = data[fam][lens]
                bx  = gx + li * (bar_w + 0.04)
                bar_h = auc * scale
                bar = Rectangle(
                    width=bar_w, height=bar_h,
                    fill_color=COLORS[lens], fill_opacity=0.88,
                    stroke_color=COLORS[lens], stroke_width=1,
                )
                bar.move_to([bx, y0 + bar_h / 2, 0])
                val_txt = Text(f"{auc:.2f}", font=SANS, font_size=12, color=COLORS[lens])
                val_txt.move_to(bar.get_top() + UP * 0.16)
                bars_this.add(VGroup(bar, val_txt))

            cx = gx + (len(LENSES) * bar_w + (len(LENSES)-1)*0.04) / 2 - bar_w * 0.5
            flbl = Text(fam, font=SANS, font_size=14, color=INK)
            flbl.move_to([cx, y0 - 0.28, 0])

            self.play(
                LaggedStart(
                    *[GrowFromEdge(b[0], DOWN) for b in bars_this],
                    lag_ratio=0.15,
                ),
                FadeIn(flbl),
                run_time=0.80,
            )
            self.play(
                *[FadeIn(b[1]) for b in bars_this],
                run_time=0.28,
            )

        # legend — upper right, compact
        legend = VGroup()
        for lens, name, col in [("J", "Jacobian", TERRA), ("L", "Logit", INK), ("T", "Tuned", "#999080")]:
            swatch = Rectangle(
                width=0.24, height=0.24,
                fill_color=col, fill_opacity=0.88,
                stroke_width=0,
            )
            lbl = Text(name, font=SANS, font_size=15, color=INK)
            pair = VGroup(swatch, lbl).arrange(RIGHT, buff=0.10)
            legend.add(pair)
        legend.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        legend.move_to([4.8, 2.0, 0])
        self.play(FadeIn(legend), run_time=0.4)

        # title — short, within safe area
        title = Text("Six families · three lenses  (Fig 52)", font=SERIF, font_size=22, color=INK)
        title.to_edge(UP, buff=0.65)   # buff=0.65 keeps top at 4.0-0.65=3.35, within safe area
        self.play(FadeIn(title), run_time=0.4)
        self.wait(3.36)    # total ≈ 14.36s


# ── B08 · Swap Surgery ────────────────────────────────────────────────────────
# 12.42s  'spider' lifted from readout; 'ant' inserted; output word flips.
class B08_SwapSurgery(Scene):
    def construct(self):
        # riddle prompt banner
        prompt_txt = Text(
            '"How many legs does it have?"',
            font=SERIF, font_size=30, color=INK,
        )
        prompt_txt.to_edge(UP, buff=0.55)
        hidden = Text(
            "(hidden step: spider)",
            font=SERIF, font_size=22, color=INK,
        )
        hidden.next_to(prompt_txt, DOWN, buff=0.15)
        self.play(
            FadeIn(prompt_txt, shift=DOWN * 0.15),
            FadeIn(hidden, shift=DOWN * 0.1),
            run_time=0.8,
        )
        self.wait(0.3)

        # readout list with 'spider' highlighted
        readout_words = ["spider", "insect", "web", "legs", "arachnid", "venom"]
        items = VGroup()
        for w in readout_words:
            col = TERRA if w == "spider" else INK
            txt = Text(w, font=SERIF, font_size=28, color=col)
            items.add(txt)
        items.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        items.shift(LEFT * 3.5 + DOWN * 0.3)
        # RoundedRectangle with no VGroup arg so static check tracks it as a shape
        box = RoundedRectangle(
            corner_radius=0.14, width=4.2, height=5.8,
            fill_opacity=0, stroke_color=INK, stroke_width=2,
        )
        box.move_to(items)
        box_lbl = Text("readout", font=SANS, font_size=20, color=INK)
        box_lbl.next_to(box, UP, buff=0.1)

        self.play(
            Create(box),
            FadeIn(box_lbl),
            LaggedStart(
                *[FadeIn(it, shift=RIGHT * 0.1) for it in items],
                lag_ratio=0.12,
            ),
            run_time=1.2,
        )
        self.wait(0.4)

        # lift 'spider' out — terracotta lift
        spider_item = items[0]
        spider_copy = spider_item.copy()
        spider_item.set_color(TERRA)
        self.play(
            spider_item.animate.shift(RIGHT * 0.6 + UP * 0.2),
            run_time=0.6,
        )

        # insert 'ant'
        ant = Text("ant", font=SERIF, font_size=28, color=TERRA)
        ant.move_to(spider_item.get_center() + RIGHT * 0.1)
        arrow_in = Arrow(
            ant.get_top() + UP * 0.8, ant.get_top(),
            color=TERRA, stroke_width=3, buff=0.05,
        )
        self.play(
            FadeOut(spider_item),
            GrowArrow(arrow_in),
            FadeIn(ant, shift=DOWN * 0.3),
            run_time=0.8,
        )
        self.wait(0.3)

        # output flips: 8 legs → 6 legs
        out_label = Text("output:", font=SANS, font_size=22, color=INK)
        out_label.shift(RIGHT * 1.8 + DOWN * 1.4)
        out_before = Text("8  legs", font=SERIF, font_size=40, color=INK)
        out_before.next_to(out_label, RIGHT, buff=0.3)
        out_after  = Text("6  legs", font=SERIF, font_size=40, color=TERRA)
        out_after.move_to(out_before)

        self.play(
            FadeIn(out_label),
            FadeIn(out_before, shift=LEFT * 0.2),
            run_time=0.6,
        )
        self.wait(0.4)
        self.play(
            FadeOut(out_before, shift=UP * 0.3),
            FadeIn(out_after, shift=UP * 0.3),
            run_time=0.6,
        )
        caption = Text(
            "The lens finds directions the model actually uses.",
            font=SERIF, font_size=26, color=INK,
        )
        caption.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.6)
        self.wait(5.37)    # total ≈ 12.42s


# ── B11 · Single-Token Blind Spot ──────────────────────────────────────────────
# 12.84s  'blackmail' splits into black|mail; lens vector attaches only to 'black'
class B11_SingleTokenBlindSpot(Scene):
    def construct(self):
        # header fills the empty upper frame
        title = Text("Single-token limit", font=SANS, font_size=32, color=INK)
        title.to_edge(UP, buff=0.55)
        subtitle = Text(
            "The J-lens decodes one token at a time",
            font=SERIF, font_size=22, color=INK,
        )
        subtitle.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.5)

        # word at y=1.0 — below the header, above the split band
        word = Text("blackmail", font=SERIF, font_size=72, color=INK)
        word.move_to(UP * 1.0)
        self.play(FadeIn(word, shift=UP * 0.2), run_time=0.7)
        self.wait(0.6)

        # split parts at y=-0.4, x=±2.5 — separated from word bbox by ≥0.45 units
        black_part = Text("black", font=SERIF, font_size=72, color=INK)
        mail_part  = Text("mail",  font=SERIF, font_size=72, color=INK)
        black_part.move_to(DOWN * 0.4 + LEFT * 2.5)
        mail_part.move_to(DOWN * 0.4 + RIGHT * 2.5)

        # divider between the two split tokens
        divider = DashedLine(
            UP * 0.15, DOWN * 0.95,
            color=INK, stroke_width=2,
        )

        self.play(
            FadeOut(word),
            FadeIn(black_part),
            FadeIn(mail_part),
            Create(divider),
            run_time=0.8,
        )
        self.wait(0.4)

        # token chips below split parts
        def chip(txt, col):
            r = RoundedRectangle(
                corner_radius=0.1, width=2.6, height=0.6,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=col, stroke_width=2,
            )
            t = Text(txt, font=SANS, font_size=22, color=INK)
            t.move_to(r)
            return VGroup(r, t)

        chip_black = chip("token: 'black'",  TERRA)
        chip_mail  = chip("token: 'mail'",   INK)
        chip_black.next_to(black_part, DOWN, buff=0.3)
        chip_mail.next_to(mail_part,  DOWN, buff=0.3)

        self.play(
            FadeIn(chip_black, shift=DOWN * 0.15),
            FadeIn(chip_mail,  shift=DOWN * 0.15),
            run_time=0.7,
        )
        self.wait(0.3)

        # lens vector arrow points only to 'black'
        lens_arrow = Arrow(
            chip_black.get_bottom() + DOWN * 0.5,
            chip_black.get_bottom(),
            color=TERRA, stroke_width=4, buff=0.05,
        )
        lens_lbl = Text("J-lens vector", font=SANS, font_size=22, color=INK)
        lens_lbl.next_to(lens_arrow, DOWN, buff=0.12)

        # fade mail token to show it's missed
        self.play(
            GrowArrow(lens_arrow),
            FadeIn(lens_lbl),
            mail_part.animate.set_opacity(0.30),
            chip_mail.animate.set_opacity(0.30),
            run_time=0.9,
        )

        verdict = Text(
            "'blackmail' → registers only as 'black'",
            font=SERIF, font_size=28, color=INK,
        )
        verdict.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(verdict, shift=UP * 0.15), run_time=0.6)
        self.wait(6.77)    # total ≈ 12.84s


# ── B12 · Template & Oracle Lenses ────────────────────────────────────────────
# 14.19s  Two patch-lenses appear; template decodes 'blackmail' whole;
#         oracle emits phrase 'blackmail him by revealing'.
class B12_TemplateOracle(Scene):
    def construct(self):
        # header: J-lens baseline
        header = Text(
            "J-lens: 'black'  —  single-token limit",
            font=SERIF, font_size=28, color=INK,
        )
        header.to_edge(UP, buff=0.65)
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.6)
        self.wait(0.4)

        # two patch cards
        def patch_card(title, output_lines, col):
            outer = RoundedRectangle(
                corner_radius=0.18, width=5.4, height=3.4,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=col, stroke_width=2.5,
            )
            lbl = Text(title, font=SANS, font_size=24, color=col)
            lbl.move_to(outer.get_top() + DOWN * 0.38)
            divline = Line(
                outer.get_left() + RIGHT * 0.2 + DOWN * 0.0,
                outer.get_right() + LEFT * 0.2 + DOWN * 0.0,
                color=col, stroke_width=1,
            )
            divline.shift(DOWN * 0.55)
            lines_grp = VGroup()
            for ol in output_lines:
                t = Text(ol, font=SERIF, font_size=28, color=INK)
                lines_grp.add(t)
            lines_grp.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            lines_grp.move_to(outer.get_center() + DOWN * 0.45)
            return VGroup(outer, lbl, divline, lines_grp)

        template_card = patch_card(
            "Template Lens",
            ['"blackmail"  ✓', "decodes multi-token phrase", "if enumerated in advance"],
            INK,
        )
        oracle_card = patch_card(
            "Oracle Lens",
            ['"blackmail him by revealing"', "whole-phrase decode at", "email sign-off token"],
            TERRA,
        )
        template_card.shift(LEFT * 3.1 + DOWN * 0.4)
        oracle_card.shift(RIGHT * 3.1  + DOWN * 0.4)

        self.play(
            FadeIn(template_card, shift=UP * 0.2),
            run_time=0.9,
        )
        self.wait(0.4)
        self.play(
            FadeIn(oracle_card, shift=UP * 0.2),
            run_time=0.9,
        )
        self.wait(0.5)

        # skeptic caption
        skeptic = Text(
            "If the patches see more, the J-space is a slice — not the whole workspace.",
            font=SERIF, font_size=28, color=INK,
        )
        skeptic.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(skeptic), run_time=0.5)
        self.wait(7.97)    # total ≈ 14.19s


# ── BearsDoodlesVideo ─────────────────────────────────────────────────────────
# Static-check entry point: runs all per-beat scenes sequentially so the
# distinctness gate can count shape states across the whole reel.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_ResidualStack,
            B03_JLensGradient,
            B04_ReadoutRanking,
            B06_SixPrompts,
            B07_LensBakeoff,
            B08_SwapSurgery,
            B11_SingleTokenBlindSpot,
            B12_TemplateOracle,
        ]:
            cls().construct()
