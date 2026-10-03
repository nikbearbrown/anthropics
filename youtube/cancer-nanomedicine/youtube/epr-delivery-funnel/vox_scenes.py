import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_DeliveryFunnel(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("EPR EFFECT DELIVERY FUNNEL",font="Helvetica",
                   font_size=42,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # 5 funnel stages (visual, not to scale)
        stages=[
            ("INJECTED DOSE",     "100 PERCENT",   6.2, 2.0,  SLATE,  0.5),
            ("BLOOD CIRCULATION", "60 PERCENT",    4.8, 1.1,  SLATE,  0.45),
            ("TUMOR VASCULATURE", "10 PERCENT",    3.4, 0.2,  SLATE,  0.4),
            ("INTERSTITIAL SPACE","3 PERCENT",     2.1,-0.7,  SLATE,  0.35),
            ("CELLULAR UPTAKE",   "0 POINT 7",     1.2,-1.6, CRIMSON,0.9),
        ]
        BOX_H=0.60
        boxes=[]; stage_labels=[]; pct_labels=[]; connectors=[]
        for label,pct,width,cy,clr,op in stages:
            box=Rectangle(width=width,height=BOX_H,fill_color=ManimColor(clr),
                          fill_opacity=op,stroke_width=0,stroke_opacity=0)
            box.move_to([0,cy,0])
            boxes.append(box)
            lbl_t=Text(label,font="Helvetica",font_size=36,weight=BOLD,color=ManimColor(INK)).move_to([-4.4,cy,0])
            stage_labels.append(lbl_t)
            pct_t=Text(pct,font="Helvetica",font_size=36,weight=BOLD,
                       color=ManimColor(CRIMSON if clr==CRIMSON else INK)).move_to([4.4,cy,0])
            pct_labels.append(pct_t)
        # Connectors between stages (tapered lines on sides)
        for i in range(len(stages)-1):
            w1=stages[i][2]/2; w2=stages[i+1][2]/2
            y1=stages[i][3]-BOX_H/2; y2=stages[i+1][3]+BOX_H/2
            l_conn=Line([-w1,y1,0],[-w2,y2,0],stroke_width=4,color=ManimColor(SLATE))
            r_conn=Line([ w1,y1,0],[ w2,y2,0],stroke_width=4,color=ManimColor(SLATE))
            connectors.append(VGroup(l_conn,r_conn))
        ann_t=Text("WILHELM 2016 META-ANALYSIS 117 STUDIES",font="Helvetica",font_size=32,weight=BOLD,color=ManimColor(CRIMSON)).move_to([0,-2.7,0])
        self.add(title, ann_t)
        for b in boxes: self.add(b)
        for l in stage_labels: self.add(l)
        for p in pct_labels: self.add(p)
        for c in connectors: self.add(c)
        self.wait(2.0)
