"""scenes.py — Manim graphics for workspace-anatomy (E03)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-anatomy
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_ThreeRegions

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-anatomy

Scene → beat mapping (durations from estimated audio; update after audio lock):
  B02_ThreeRegions     ~19s   layer stack: sensory / workspace / motor + CKA strip
  B03_BandSignatures   ~17s   band boundary curve with elbows at L38 and L92
  B04_Ignition         ~20s   ambiguous input bimodal snap at workspace entry
  B06_Occupancy        ~25s   two-panel: occupancy plateau ~25 + variance < 10%
  B07_ListOverflow     ~24s   80-word animal list: dashed unread animals in readout
  B08_Displacement     ~12s   25-slot grid: unrelated words displace each other
  B09_BroadcastHubs    ~25s   MLP bars + broadcast heads highlighted + ablation
  B10_Multitask        ~12s   two concepts time-sharing across tokens
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
MUTE   = "#8A8570"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B02 · Three Regions ───────────────────────────────────────────────────────
# ~19s  Layer stack split into sensory / workspace / motor; CKA heat strip beside
class B02_ThreeRegions(Scene):
    def construct(self):
        N_LAYERS = 12
        layer_h = 0.42
        layer_w = 2.8

        # build layers bottom-to-top (early = sensory at bottom)
        layers = VGroup()
        for i in range(N_LAYERS):
            rect = Rectangle(
                width=layer_w, height=layer_h,
                fill_color=GROUND, fill_opacity=1.0,
                stroke_color=INK, stroke_width=1.5,
            )
            layers.add(rect)
        layers.arrange(UP, buff=0.06)
        layers.move_to(ORIGIN + LEFT * 2.2)

        # darker fills so gate-V contrast threshold is met
        region_colors = {
            "sensory":   "#BDBAA8",   # medium warm-gray   lum≈0.49
            "workspace": "#C8A080",   # warm terracotta    lum≈0.39
            "motor":     "#BDBAA8",   # same as sensory
        }
        boundary_low  = N_LAYERS // 3        # sensory / workspace boundary
        boundary_high = 2 * N_LAYERS // 3    # workspace / motor boundary

        for i, rect in enumerate(layers):
            if i < boundary_low:
                rect.set_fill(region_colors["sensory"],   opacity=1.0)
            elif i < boundary_high:
                rect.set_fill(region_colors["workspace"], opacity=1.0)
            else:
                rect.set_fill(region_colors["motor"],     opacity=1.0)

        # region bracket labels
        sensory_mid   = layers[boundary_low // 2].get_center()
        workspace_mid = layers[(boundary_low + boundary_high) // 2].get_center()
        motor_mid     = layers[(boundary_high + N_LAYERS) // 2].get_center()

        lbl_s = Text("SENSORY",   font=SANS, font_size=20, color=INK)
        lbl_w = Text("WORKSPACE", font=SANS, font_size=20, color=INK)
        lbl_m = Text("MOTOR",     font=SANS, font_size=20, color=INK)
        lbl_s.move_to(sensory_mid   + LEFT * 3.0)
        lbl_w.move_to(workspace_mid + LEFT * 3.0)
        lbl_m.move_to(motor_mid     + LEFT * 3.0)

        # layer index ticks — font_size≥20 to clear §8.1 floor
        tick_L0  = Text("L 0",  font=SANS, font_size=20, color=INK)
        tick_Lmid = Text(f"L {boundary_low}", font=SANS, font_size=20, color=INK)
        tick_Lhi  = Text(f"L {boundary_high}", font=SANS, font_size=20, color=INK)
        tick_Lend = Text(f"L {N_LAYERS}", font=SANS, font_size=20, color=INK)
        for tick, layer_i in [(tick_L0, 0), (tick_Lmid, boundary_low),
                              (tick_Lhi, boundary_high), (tick_Lend, N_LAYERS - 1)]:
            tick.next_to(layers[min(layer_i, N_LAYERS - 1)], RIGHT, buff=0.18)

        # CKA strip (a thin heat strip beside the stack)
        strip_w = 0.38
        strip = VGroup()
        for i in range(N_LAYERS):
            if i in (boundary_low - 1, boundary_low, boundary_high - 1, boundary_high):
                shade = "#D9C8A8"   # boundary — low similarity
            else:
                shade = TERRA
            s = Rectangle(
                width=strip_w, height=layer_h,
                fill_color=shade, fill_opacity=0.90,
                stroke_width=0,
            )
            strip.add(s)
        strip.arrange(UP, buff=0.06)
        strip.next_to(layers, RIGHT, buff=0.22)

        cka_lbl = Text("CKA", font=SANS, font_size=20, color=INK)
        cka_lbl.rotate(PI / 2)
        cka_lbl.next_to(strip, RIGHT, buff=0.14)

        # boundary dashed lines — explicit horizontal endpoints (same y both sides)
        y_low  = layers[boundary_low].get_top()[1]
        y_high = layers[boundary_high].get_top()[1]
        x_l    = layers.get_left()[0] - 0.1
        x_r    = strip.get_right()[0]  + 0.1
        dash_low  = DashedLine(
            [x_l, y_low,  0],
            [x_r, y_low,  0],
            dash_length=0.12, color=INK, stroke_width=1.2,
        )
        dash_high = DashedLine(
            [x_l, y_high, 0],
            [x_r, y_high, 0],
            dash_length=0.12, color=INK, stroke_width=1.2,
        )

        # right-side annotation cards — fill the empty right half of the scene
        title_lbl = Text("THREE MODEL REGIONS", font=SANS, font_size=20, color=INK)
        title_lbl.to_edge(UP, buff=0.65)

        ann_cards = VGroup()
        for mid, fill_col, label_col, heading, subtext in [
            (sensory_mid,   "#BDBAA8", INK,  "SENSORY",   "token features / position"),
            (workspace_mid, "#C8A080", INK,  "WORKSPACE", "abstract state / planning"),
            (motor_mid,     "#BDBAA8", INK,  "MOTOR",     "output / prediction"),
        ]:
            card = Rectangle(
                width=4.5, height=1.6,
                fill_color=fill_col, fill_opacity=1.0,
                stroke_color=label_col, stroke_width=1.5,
            )
            card.move_to([3.9, mid[1], 0])
            card_h = Text(heading, font=SANS, font_size=22, color=label_col)
            card_h.move_to(card.get_center() + UP * 0.35)
            card_sub = Text(subtext.upper(), font=SANS, font_size=20, color=label_col)
            card_sub.move_to(card.get_center() + DOWN * 0.28)
            ann_cards.add(VGroup(card, card_h, card_sub))

        # animate
        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in layers], lag_ratio=0.04),
            FadeIn(title_lbl),
            run_time=1.8,
        )
        self.play(FadeIn(strip, shift=RIGHT * 0.1), run_time=0.6)
        self.play(
            FadeIn(lbl_s), FadeIn(lbl_w), FadeIn(lbl_m),
            FadeIn(tick_L0), FadeIn(tick_Lmid), FadeIn(tick_Lhi), FadeIn(tick_Lend),
            FadeIn(cka_lbl),
            run_time=0.8,
        )
        self.play(Create(dash_low), Create(dash_high), run_time=0.7)

        ws_highlight = SurroundingRectangle(
            VGroup(*layers[boundary_low:boundary_high]),
            color=TERRA, stroke_width=2.5, buff=0.06,
        )
        self.play(Create(ws_highlight), run_time=0.5)
        self.play(FadeIn(ann_cards), run_time=0.7)
        self.wait(11.8)


# ── B03 · Band Signatures ─────────────────────────────────────────────────────
# ~17s  Curve rising from zero; two dashed verticals mark L38 and L92 for Sonnet
class B03_BandSignatures(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 120, 20],
            y_range=[0, 1.0, 0.25],
            x_length=9.5,
            y_length=5.0,
            axis_config={"color": INK, "stroke_width": 1.8,
                         "include_tip": False, "numbers_to_include": []},
        )
        ax.move_to(ORIGIN + DOWN * 0.3)

        x_lbl = Text("layer", font=SANS, font_size=22, color=INK)
        x_lbl.next_to(ax.x_axis, DOWN, buff=0.18)
        y_lbl = Text("signal", font=SANS, font_size=22, color=INK)
        y_lbl.rotate(PI / 2)
        y_lbl.next_to(ax.y_axis, LEFT, buff=0.3)

        # x-axis tick labels
        for val, lbl in [(0, "0"), (38, "38"), (92, "92"), (120, "120")]:
            t = Text(lbl, font=SANS, font_size=20, color=MUTE if val in (0, 120) else INK)
            t.next_to(ax.c2p(val, 0), DOWN, buff=0.22)
            self.add(t)

        # curve: near-zero 0–38, sigmoid rise 38–55, plateau 55–92, fall 92–120
        def curve_y(x):
            if x < 38:
                return 0.04 + 0.01 * x / 38
            elif x < 55:
                t = (x - 38) / 17
                return 0.05 + 0.75 * (3 * t**2 - 2 * t**3)
            elif x < 92:
                return 0.80
            else:
                t = (x - 92) / 28
                return 0.80 * (1 - 0.55 * t)

        curve = ax.plot(curve_y, x_range=[0, 120, 0.5],
                        color=TERRA, stroke_width=3)

        # band dashed verticals
        y_top = ax.c2p(0, 1.0)[1]
        y_bot = ax.c2p(0, 0.0)[1]
        d38 = DashedLine(
            ax.c2p(38, 0), ax.c2p(38, 0.9),
            dash_length=0.14, color=INK, stroke_width=1.8,
        )
        d92 = DashedLine(
            ax.c2p(92, 0), ax.c2p(92, 0.9),
            dash_length=0.14, color=INK, stroke_width=1.8,
        )
        lbl_38 = Text("L38", font=SANS, font_size=20, color=INK)
        lbl_92 = Text("L92", font=SANS, font_size=20, color=INK)
        lbl_38.next_to(ax.c2p(38, 0.93), UP, buff=0.08)
        lbl_92.next_to(ax.c2p(92, 0.93), UP, buff=0.08)

        band_label = Text("workspace band", font=SANS, font_size=22, color=INK)
        band_label.move_to(ax.c2p(65, 0.88))

        note_lo = Text("reads static", font=SERIF, font_size=22, color=MUTE)
        note_hi = Text("reads the answer", font=SERIF, font_size=22, color=MUTE)
        note_lo.move_to(ax.c2p(19, 0.18))
        # placed below the falling tail (curve ≈0.55 at x=108); clear vertical gap
        note_hi.move_to(ax.c2p(108, 0.24))

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.7)
        self.play(Create(curve), run_time=2.2)
        self.play(Create(d38), Create(d92), run_time=0.7)
        self.play(
            FadeIn(lbl_38), FadeIn(lbl_92),
            FadeIn(band_label),
            run_time=0.6,
        )
        self.play(FadeIn(note_lo), FadeIn(note_hi), run_time=0.6)
        self.wait(12.2)


# ── B04 · Ignition ────────────────────────────────────────────────────────────
# ~20s  Ambiguous token; early layers hold mixture; middle layers snap bimodal
class B04_Ignition(Scene):
    def construct(self):
        # early-layer panel (left): mixture of two concept labels
        panel_w, panel_h = 3.6, 4.2
        early_box = Rectangle(
            width=panel_w, height=panel_h,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=MUTE, stroke_width=1.5,
        ).move_to(LEFT * 3.8)
        early_title = Text("early layers", font=SANS, font_size=20, color=MUTE)
        early_title.next_to(early_box, UP, buff=0.18)

        concept_a = Text("CONCEPT A", font=SANS, font_size=26, color=INK)
        concept_b = Text("CONCEPT B", font=SANS, font_size=26, color=MUTE)
        concept_a.move_to(early_box.get_center() + UP * 0.45)
        concept_b.move_to(early_box.get_center() + DOWN * 0.45)
        mix_arrow = DoubleArrow(
            concept_a.get_bottom() + DOWN * 0.08,
            concept_b.get_top()    + UP * 0.08,
            color=MUTE, stroke_width=1.5, buff=0,
        )
        mix_lbl = Text("mixture", font=SERIF, font_size=22, color=MUTE)
        mix_lbl.next_to(mix_arrow, RIGHT, buff=0.12)

        # workspace entry dashed line (center)
        entry_line = DashedLine(
            UP * 2.5, DOWN * 2.5,
            dash_length=0.16, color=INK, stroke_width=2.0,
        )
        entry_lbl = Text("workspace\nentry", font=SANS, font_size=22, color=INK)
        entry_lbl.next_to(entry_line, UP, buff=0.14)

        # middle-layer panel (right): two separate outcomes
        mid_box_a = Rectangle(
            width=3.0, height=1.8,
            fill_color="#F5ECE5", fill_opacity=1.0,
            stroke_color=TERRA, stroke_width=2.0,
        ).move_to(RIGHT * 3.5 + UP * 1.0)
        mid_box_b = Rectangle(
            width=3.0, height=1.8,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=MUTE, stroke_width=1.5,
        ).move_to(RIGHT * 3.5 + DOWN * 1.2)

        mid_label_a = Text("CONCEPT A", font=SANS, font_size=24, color=INK)
        mid_label_b = Text("CONCEPT B", font=SANS, font_size=24, color=MUTE)
        mid_label_a.move_to(mid_box_a)
        mid_label_b.move_to(mid_box_b)

        prompt_a = Text("prompt 1", font=SERIF, font_size=22, color=MUTE)
        prompt_b = Text("prompt 2", font=SERIF, font_size=22, color=MUTE)
        prompt_a.next_to(mid_box_a, UP, buff=0.1)
        prompt_b.next_to(mid_box_b, DOWN, buff=0.1)

        snap_lbl = Text("SNAP", font=SANS, font_size=22, color=INK)
        snap_lbl.next_to(entry_line, DOWN, buff=0.16)

        # animate
        self.play(
            FadeIn(early_box), FadeIn(early_title),
            run_time=0.5,
        )
        self.play(
            FadeIn(concept_a), FadeIn(concept_b),
            Create(mix_arrow), FadeIn(mix_lbl),
            run_time=0.8,
        )
        self.play(Create(entry_line), FadeIn(entry_lbl), run_time=0.6)
        self.play(
            FadeIn(mid_box_a), FadeIn(mid_box_b),
            FadeIn(mid_label_a), FadeIn(mid_label_b),
            FadeIn(prompt_a), FadeIn(prompt_b),
            run_time=0.9,
        )
        self.play(FadeIn(snap_lbl, scale=1.15), run_time=0.4)
        self.wait(15.8)


# ── B06 · Occupancy ───────────────────────────────────────────────────────────
# ~25s  Two-panel: occupancy plateau ~25 | excess variance < 10%
class B06_Occupancy(Scene):
    def construct(self):
        # LEFT panel — occupancy curve
        ax_l = Axes(
            x_range=[0, 120, 40],
            y_range=[0, 50, 10],
            x_length=5.0,
            y_length=3.8,
            axis_config={"color": INK, "stroke_width": 1.8,
                         "include_tip": False, "numbers_to_include": []},
        ).move_to(LEFT * 3.3 + DOWN * 0.3)

        for val, lbl in [(0, "0"), (40, "40"), (80, "80"), (120, "120")]:
            t = Text(lbl, font=SANS, font_size=20, color=MUTE)
            t.next_to(ax_l.c2p(val, 0), DOWN, buff=0.18)
            self.add(t)
        for val, lbl in [(0, "0"), (50, "50")]:
            t = Text(lbl, font=SANS, font_size=20, color=MUTE)
            t.next_to(ax_l.c2p(0, val), LEFT, buff=0.18)
            self.add(t)

        ax_l_xlabel = Text("layer", font=SANS, font_size=22, color=INK)
        ax_l_xlabel.next_to(ax_l.x_axis, DOWN, buff=0.3)
        ax_l_ylabel = Text("occupancy", font=SANS, font_size=22, color=INK)
        ax_l_ylabel.rotate(PI / 2)
        ax_l_ylabel.next_to(ax_l.y_axis, LEFT, buff=0.15)

        def occ_y(x):
            if x < 38:
                return 1.5 + 0.5 * x / 38
            elif x < 55:
                t = (x - 38) / 17
                return 2.0 + 23.0 * (3 * t**2 - 2 * t**3)
            elif x < 92:
                return 25.0
            else:
                t = (x - 92) / 28
                return 25.0 - 8.0 * t

        curve_l = ax_l.plot(occ_y, x_range=[0, 120, 0.5],
                            color=TERRA, stroke_width=3)
        plateau_lbl = Text("~25 median", font=SANS, font_size=20, color=MUTE)
        plateau_lbl.next_to(ax_l.c2p(65, 26.5), UP, buff=0.04)

        # RIGHT panel — excess variance bar
        ax_r = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 25, 5],
            x_length=2.4,
            y_length=3.8,
            axis_config={"color": INK, "stroke_width": 1.8,
                         "include_tip": False, "numbers_to_include": []},
        ).move_to(RIGHT * 2.8 + DOWN * 0.3)

        ax_r_ylabel = Text("% variance", font=SANS, font_size=22, color=INK)
        ax_r_ylabel.rotate(PI / 2)
        ax_r_ylabel.next_to(ax_r.y_axis, LEFT, buff=0.3)
        for val, lbl in [(0, "0%"), (20, "20%")]:
            t = Text(lbl, font=SANS, font_size=20, color=MUTE)
            t.next_to(ax_r.c2p(0, val), LEFT, buff=0.18)
            self.add(t)

        # bar to ~9% (just below 10%)
        bar = ax_r.get_area(
            ax_r.plot(lambda x: 9.1, x_range=[0.1, 0.9]),
            x_range=[0.1, 0.9], color=TERRA, opacity=0.75,
        )
        cap_line = DashedLine(
            ax_r.c2p(0, 10), ax_r.c2p(1.0, 10),
            dash_length=0.12, color=INK, stroke_width=1.8,
        )
        cap_lbl = Text("<10%", font=SANS, font_size=20, color=INK)
        cap_lbl.next_to(ax_r.c2p(1.05, 10), RIGHT, buff=0.08)

        title = Text("Workspace capacity", font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.65)

        # animate
        self.play(FadeIn(title), run_time=0.4)
        self.play(
            Create(ax_l), FadeIn(ax_l_xlabel), FadeIn(ax_l_ylabel),
            run_time=0.6,
        )
        self.play(Create(curve_l), run_time=1.8)
        self.play(FadeIn(plateau_lbl), run_time=0.4)
        self.play(
            Create(ax_r), FadeIn(ax_r_ylabel),
            run_time=0.5,
        )
        self.play(FadeIn(bar), run_time=0.6)
        self.play(Create(cap_line), FadeIn(cap_lbl), run_time=0.5)
        self.wait(18.2)


# ── B07 · List Overflow ───────────────────────────────────────────────────────
# ~24s  80-word animal list streams in; readout shows dashed "unread" animals
class B07_ListOverflow(Scene):
    def construct(self):
        ANIMALS_READ = ["cat", "dog", "bear", "wolf", "hawk",
                        "deer", "fox", "owl", "crow", "elk"]
        ANIMALS_PRED = ["eagle", "raven", "lynx", "moose"]

        # list panel (left)
        list_title = Text("input list", font=SANS, font_size=22, color=MUTE)
        list_title.move_to(LEFT * 4.2 + UP * 2.9)

        list_items = VGroup()
        for i, animal in enumerate(ANIMALS_READ):
            item = Text(animal.upper(), font=SANS, font_size=22, color=INK)
            item.move_to(LEFT * 4.2 + UP * (2.3 - i * 0.44))
            list_items.add(item)
        ellipsis = Text("… (80 total)", font=SERIF, font_size=22, color=MUTE)
        ellipsis.next_to(list_items[-1], DOWN, buff=0.22)

        read_brace = Brace(list_items, direction=LEFT, color=MUTE)
        read_lbl = Text("read so far", font=SANS, font_size=20, color=MUTE)
        read_lbl.rotate(PI / 2)
        read_lbl.next_to(read_brace, LEFT, buff=0.1)

        # readout panel (right)
        readout_title = Text("workspace readout", font=SANS, font_size=22, color=INK)
        readout_title.move_to(RIGHT * 2.6 + UP * 2.9)

        readout_solid = VGroup()
        for i, animal in enumerate(ANIMALS_READ[:6]):
            item = Text(animal.upper(), font=SANS, font_size=22, color=INK)
            item.move_to(RIGHT * 2.6 + UP * (2.3 - i * 0.44))
            readout_solid.add(item)

        readout_dashed = VGroup()
        for i, animal in enumerate(ANIMALS_PRED):
            item = Text(animal, font=SERIF, font_size=22, color=MUTE)
            # underline anchored to actual bottom edge so it clears the text bounding box
            dash_under = DashedLine(
                item.get_corner(DL) + DOWN * 0.06,
                item.get_corner(DR) + DOWN * 0.06,
                dash_length=0.10, color=MUTE, stroke_width=1.4,
            )
            grp = VGroup(item, dash_under)
            grp.move_to(RIGHT * 2.6 + UP * (2.3 - (i + 6) * 0.44))
            readout_dashed.add(grp)

        pred_lbl = Text("category prediction", font=SANS, font_size=20, color=MUTE)
        pred_lbl.next_to(readout_dashed, RIGHT, buff=0.22)

        capacity_bar_bg = Rectangle(
            width=0.5, height=3.5,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=MUTE, stroke_width=1.2,
        ).move_to(RIGHT * 5.8)
        capacity_fill = Rectangle(
            width=0.5, height=3.5 * (10 / 25),
            fill_color=TERRA, fill_opacity=0.8,
            stroke_width=0,
        )
        capacity_fill.align_to(capacity_bar_bg, DOWN)
        cap_lbl2 = Text("~25\nslots", font=SANS, font_size=24, color=INK)
        cap_lbl2.next_to(capacity_bar_bg, UP, buff=0.12)

        # skeptic caption
        skep = Text("'~25 slots' measures sparse reconstruction — not remembered items.",
                    font=SERIF, font_size=22, color=MUTE)
        skep.to_edge(DOWN, buff=0.80)

        # animate
        self.play(FadeIn(list_title), FadeIn(readout_title), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(item, shift=DOWN * 0.08) for item in list_items],
                        lag_ratio=0.08),
            run_time=1.4,
        )
        self.play(FadeIn(ellipsis), run_time=0.3)
        self.play(
            FadeIn(read_brace), FadeIn(read_lbl),
            run_time=0.4,
        )
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.08) for item in readout_solid],
                        lag_ratio=0.07),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[FadeIn(grp) for grp in readout_dashed],
                        lag_ratio=0.12),
            run_time=0.8,
        )
        self.play(FadeIn(pred_lbl), run_time=0.3)
        self.play(
            FadeIn(capacity_bar_bg), FadeIn(capacity_fill), FadeIn(cap_lbl2),
            run_time=0.5,
        )
        self.play(FadeIn(skep, shift=UP * 0.06), run_time=0.4)
        self.wait(17.5)


# ── B08 · Displacement ────────────────────────────────────────────────────────
# ~12s  25-slot grid: unrelated words stream in, displacing older entries
class B08_Displacement(Scene):
    def construct(self):
        COLS, ROWS = 5, 5
        CELL_W, CELL_H = 1.72, 0.72
        WORDS = ["table", "seven", "bridge", "clay",
                 "epoch", "lever", "marble", "prism",
                 "forge", "delta"]

        grid_group = VGroup()
        cells = []
        for row in range(ROWS):
            for col in range(COLS):
                rect = Rectangle(
                    width=CELL_W, height=CELL_H,
                    fill_color=GROUND, fill_opacity=1.0,
                    stroke_color=MUTE, stroke_width=1.2,
                )
                rect.move_to(
                    RIGHT * (col - 2) * (CELL_W + 0.1) +
                    UP    * (row - 2) * (CELL_H + 0.1)
                )
                cells.append(rect)
                grid_group.add(rect)

        title = Text("unrelated list — genuine displacement",
                     font=SANS, font_size=22, color=INK)
        title.to_edge(UP, buff=0.65)
        slot_lbl = Text("25 slots", font=SANS, font_size=22, color=MUTE)
        slot_lbl.next_to(grid_group, RIGHT, buff=0.4)

        self.play(FadeIn(title), FadeIn(grid_group), FadeIn(slot_lbl),
                  run_time=0.7)

        # fill first 6 slots with placeholder words
        placeholders = ["cat", "dog", "bear", "wolf", "hawk", "deer"]
        slot_texts = []
        for i, word in enumerate(placeholders):
            t = Text(word.upper(), font=SANS, font_size=22, color=INK)
            t.move_to(cells[i].get_center())
            slot_texts.append(t)
        self.play(LaggedStart(*[FadeIn(t) for t in slot_texts], lag_ratio=0.1),
                  run_time=0.7)

        # displace: each new unrelated word overwrites an existing slot
        disp_counter_val = 0
        disp_counter_box = Rectangle(
            width=1.4, height=0.55,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=INK, stroke_width=1.5,
        ).next_to(grid_group, LEFT, buff=0.2).shift(UP * 0.5)
        disp_label = Text("displaced:", font=SANS, font_size=20, color=MUTE)
        disp_label.next_to(disp_counter_box, UP, buff=0.08)
        disp_num = Text("0", font=SANS, font_size=24, color=INK)
        disp_num.move_to(disp_counter_box)
        self.play(FadeIn(disp_counter_box), FadeIn(disp_label), FadeIn(disp_num),
                  run_time=0.4)

        for i, word in enumerate(WORDS):
            slot_i = i % len(placeholders)
            new_text = Text(word.upper(), font=SANS, font_size=22, color=INK)
            new_text.move_to(cells[slot_i].get_center())
            old_text = slot_texts[slot_i]
            disp_counter_val += 1
            new_num = Text(str(disp_counter_val), font=SANS, font_size=24, color=INK)
            new_num.move_to(disp_counter_box)
            self.play(
                FadeOut(old_text, shift=LEFT * 0.2),
                FadeIn(new_text,  shift=RIGHT * 0.2),
                Transform(disp_num, new_num),
                run_time=0.38,
            )
            slot_texts[slot_i] = new_text

        self.wait(6.0)


# ── B09 · Broadcast Hubs ──────────────────────────────────────────────────────
# ~25s  MLP amplification bars + top-1% heads highlighted + ablation comparison
# Manual bar chart (no Axes c2p arithmetic) — same pattern as B07_LensBakeoff.
class B09_BroadcastHubs(Scene):
    def construct(self):
        Y_BOT  = -2.4    # common y baseline for both charts
        BAR_W  = 0.82

        # ── PART 1 — MLP amplification (left) ────────────────────────────────
        # scale: 1.0 unit → 2.0 Manim units
        mlp_cx = -4.0
        mlp_scale = 2.0

        mlp_axis = Line([mlp_cx - 0.4, Y_BOT, 0], [mlp_cx + 2.2, Y_BOT, 0],
                        color=INK, stroke_width=1.8)
        mlp_yaxis = Line([mlp_cx - 0.4, Y_BOT, 0], [mlp_cx - 0.4, Y_BOT + 2.8, 0],
                         color=INK, stroke_width=1.8)

        # control bar  (value 0.55)
        h_ctrl = 0.55 * mlp_scale
        bar_ctrl = Rectangle(
            width=BAR_W, height=h_ctrl,
            fill_color=MUTE, fill_opacity=0.65, stroke_width=0,
        ).move_to([mlp_cx, Y_BOT + h_ctrl / 2, 0])

        # J-space bar  (value 1.15)
        h_jspace = 1.15 * mlp_scale
        bar_jspace = Rectangle(
            width=BAR_W, height=h_jspace,
            fill_color=TERRA, fill_opacity=0.80, stroke_width=0,
        ).move_to([mlp_cx + 1.1, Y_BOT + h_jspace / 2, 0])

        lbl_ctrl   = Text("control",  font=SANS, font_size=14, color=MUTE)
        lbl_jspace = Text("J-space",  font=SANS, font_size=14, color=INK)
        lbl_ctrl.move_to([mlp_cx,       Y_BOT - 0.32, 0])
        lbl_jspace.move_to([mlp_cx + 1.1, Y_BOT - 0.32, 0])
        mlp_title = Text("MLP amplification", font=SANS, font_size=17, color=INK)
        mlp_title.move_to([mlp_cx + 0.55, Y_BOT + 3.0, 0])

        # ── PART 2 — layer stack with top-1% broadcast heads ─────────────────
        N = 10
        stack = VGroup()
        for i in range(N):
            r = Rectangle(
                width=2.0, height=0.36,
                fill_color=GROUND, fill_opacity=1.0,
                stroke_color=MUTE, stroke_width=1.2,
            )
            stack.add(r)
        stack.arrange(UP, buff=0.06).move_to([0.0, 0.2, 0])

        broadcast_heads = VGroup()
        for i in [3, 5, 6, 7]:
            dot = Dot(radius=0.13, color=TERRA)
            dot.move_to(stack[i].get_center() + RIGHT * 0.7)
            broadcast_heads.add(dot)

        stack_title = Text("broadcast heads (top 1%)", font=SANS, font_size=17, color=INK)
        stack_title.next_to(stack, UP, buff=0.14)

        # ── PART 3 — ablation bar chart (right) ──────────────────────────────
        # scale: 1.0 unit → 2.5 Manim units
        abl_cx    = 3.8
        abl_scale = 2.5

        abl_axis  = Line([abl_cx - 0.7, Y_BOT, 0], [abl_cx + 2.5, Y_BOT, 0],
                         color=INK, stroke_width=1.8)
        abl_yaxis = Line([abl_cx - 0.7, Y_BOT, 0], [abl_cx - 0.7, Y_BOT + 2.8, 0],
                         color=INK, stroke_width=1.8)

        # intact (0.82), broadcast-ablated (0.38), random-control (0.79)
        h_base = 0.82 * abl_scale
        h_abl  = 0.38 * abl_scale
        h_rand = 0.79 * abl_scale

        bar_base = Rectangle(
            width=BAR_W, height=h_base,
            fill_color=MUTE, fill_opacity=0.65, stroke_width=0,
        ).move_to([abl_cx - 0.05, Y_BOT + h_base / 2, 0])
        bar_abl = Rectangle(
            width=BAR_W, height=h_abl,
            fill_color=TERRA, fill_opacity=0.80, stroke_width=0,
        ).move_to([abl_cx + 0.95, Y_BOT + h_abl / 2, 0])
        bar_rand = Rectangle(
            width=BAR_W, height=h_rand,
            fill_color=MUTE, fill_opacity=0.42, stroke_width=0,
        ).move_to([abl_cx + 1.85, Y_BOT + h_rand / 2, 0])

        lbl_base = Text("intact",   font=SANS, font_size=13, color=MUTE)
        lbl_abl  = Text("ablated",  font=SANS, font_size=13, color=INK)
        lbl_rand = Text("random\n(5 seeds)", font=SANS, font_size=12, color=MUTE)
        lbl_base.move_to([abl_cx - 0.05, Y_BOT - 0.35, 0])
        lbl_abl.move_to( [abl_cx + 0.95, Y_BOT - 0.35, 0])
        lbl_rand.move_to([abl_cx + 1.85, Y_BOT - 0.42, 0])
        abl_title = Text("workspace function after ablation",
                         font=SANS, font_size=17, color=INK)
        abl_title.move_to([abl_cx + 0.5, Y_BOT + 3.0, 0])

        # animate in three parts
        self.play(
            Create(mlp_axis), Create(mlp_yaxis), FadeIn(mlp_title),
            run_time=0.5,
        )
        self.play(
            FadeIn(bar_ctrl),   FadeIn(lbl_ctrl),
            FadeIn(bar_jspace), FadeIn(lbl_jspace),
            run_time=0.8,
        )
        self.play(
            FadeIn(stack), FadeIn(stack_title),
            run_time=0.5,
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=1.2) for d in broadcast_heads],
                        lag_ratio=0.15),
            run_time=0.7,
        )
        self.play(
            Create(abl_axis), Create(abl_yaxis), FadeIn(abl_title),
            run_time=0.5,
        )
        self.play(
            FadeIn(bar_base), FadeIn(lbl_base),
            FadeIn(bar_abl),  FadeIn(lbl_abl),
            FadeIn(bar_rand), FadeIn(lbl_rand),
            run_time=0.9,
        )
        self.wait(19.1)


# ── B10 · Multitask ───────────────────────────────────────────────────────────
# ~12s  Two concepts time-sharing across tokens in the workspace band.
# Each token gets a colored slot rectangle (INK=A, TERRA=B) — these are the
# non-text shapes that change state per step for the distinctness gate.
class B10_Multitask(Scene):
    def construct(self):
        TOKENS   = ["T1", "T2", "T3", "T4", "T5", "T6"]
        SCHEDULE = [0,    1,    0,    1,    0,    1   ]  # 0=A, 1=B
        COLORS   = [INK, TERRA]
        CONCEPTS = ["A", "B"]

        # workspace band
        band = Rectangle(
            width=10.5, height=1.6,
            fill_color="#F5ECE5", fill_opacity=0.65,
            stroke_color=TERRA, stroke_width=2.0,
        ).move_to(UP * 0.7)
        band_lbl = Text("workspace band", font=SANS, font_size=22, color=INK)
        band_lbl.next_to(band, UP, buff=0.14)

        bx0    = band.get_left()[0] + 0.9
        by     = band.get_center()[1]
        step   = 1.56
        slot_w = 1.22
        slot_h = 1.08

        self.play(FadeIn(band), FadeIn(band_lbl), run_time=0.5)

        # build tick labels below band
        for i, tok in enumerate(TOKENS):
            t = Text(tok, font=SANS, font_size=20, color=MUTE)
            t.move_to([bx0 + i * step, by - 1.15, 0])
            self.add(t)

        # add slot rectangles one by one (each is a distinct shape change)
        slots = []
        for i, sched in enumerate(SCHEDULE):
            color = COLORS[sched]
            slot = Rectangle(
                width=slot_w, height=slot_h,
                fill_color=color, fill_opacity=0.55,
                stroke_color=color, stroke_width=2.0,
            ).move_to([bx0 + i * step, by, 0])
            concept_lbl = Text(f"C{CONCEPTS[sched]}",
                               font=SANS, font_size=20, color=INK)
            concept_lbl.move_to(slot.get_center())
            slots.append(VGroup(slot, concept_lbl))
            self.play(FadeIn(slots[-1], shift=DOWN * 0.08), run_time=0.32)

        # legend
        swatch_a = Rectangle(width=0.32, height=0.32,
                              fill_color=INK, fill_opacity=0.55,
                              stroke_color=INK, stroke_width=1.5)
        swatch_b = Rectangle(width=0.32, height=0.32,
                              fill_color=TERRA, fill_opacity=0.55,
                              stroke_color=TERRA, stroke_width=1.5)
        leg_a = VGroup(swatch_a,
                       Text("CONCEPT A — active", font=SANS, font_size=20, color=INK)
                       ).arrange(RIGHT, buff=0.14)
        leg_b = VGroup(swatch_b,
                       Text("CONCEPT B — active", font=SANS, font_size=20, color=INK)
                       ).arrange(RIGHT, buff=0.14)
        legend = VGroup(leg_a, leg_b).arrange(RIGHT, buff=0.6)
        legend.move_to(DOWN * 2.55)

        caption = Text("Held concepts coexist · Active computation evicts",
                       font=SERIF, font_size=20, color=INK)
        caption.to_edge(DOWN, buff=0.70)

        self.play(FadeIn(legend), run_time=0.4)
        self.play(FadeIn(caption, shift=UP * 0.06), run_time=0.4)
        self.wait(6.8)


# ── BearsDoodlesVideo ─────────────────────────────────────────────────────────
# Static-check entry point: runs all per-beat scenes sequentially so the
# distinctness gate can count shape states across the whole reel.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_ThreeRegions,
            B03_BandSignatures,
            B04_Ignition,
            B06_Occupancy,
            B07_ListOverflow,
            B08_Displacement,
            B09_BroadcastHubs,
            B10_Multitask,
        ]:
            cls().construct()
