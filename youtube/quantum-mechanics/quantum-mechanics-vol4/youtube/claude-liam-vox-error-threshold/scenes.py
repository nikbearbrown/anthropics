import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.4):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.82).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=24).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_EncodedLogical(Scene):
 def construct(self):
  logical=chip("LOGICAL QUBIT",CRIMSON,3.4);phys=VGroup(*[chip(f"q{i}",TEAL,1.1) for i in range(1,8)]).arrange(RIGHT,buff=.2);arr=Arrow(logical.get_bottom(),phys.get_top(),color=INK,buff=.25);g=VGroup(logical,arr,phys).arrange(DOWN,buff=.65);self.play(FadeIn(logical),run_time=.4);self.play(GrowArrow(arr),LaggedStart(*[FadeIn(q) for q in phys],lag_ratio=.1),run_time=1);self.wait(max(.5,D["B02"]-1.4))
class B03_Distance(Scene):
 def construct(self):
  g=VGroup(*[VGroup(chip(f"distance {d}",SLATE,3),VGroup(*[Dot(color=CRIMSON,radius=.13) for _ in range((d+1)//2)]).arrange(RIGHT,buff=.25)).arrange(RIGHT,buff=.7) for d in [3,5,7]]).arrange(DOWN,buff=.5);lab=Text("minimum damaging pattern grows",font=SERIF,color=TEAL,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.55);self.play(LaggedStart(*[FadeIn(r) for r in g],lag_ratio=.2),FadeIn(lab),run_time=1.3);self.wait(max(.5,D["B03"]-1.3))
class B04_LowNoiseWins(Scene):
 def construct(self):
  rare=VGroup(*[Dot(color=CRIMSON,radius=.14).move_to([i*.8-2.4,0,0]) for i in range(7)]);cross=VGroup(*[Line(d.get_center()+UP*.18,d.get_center()+DOWN*.18,color=SLATE) for d in rare]);lab=title("LOW PHYSICAL ERROR","high-weight chains become rare",TEAL).to_edge(UP,buff=.7);self.play(FadeIn(lab),FadeIn(rare),run_time=.6);self.play(LaggedStart(*[Create(x) for x in cross],lag_ratio=.12),run_time=.8);self.wait(max(.5,D["B04"]-1.4))
def threshold_plot(scene):
 ax=Axes(x_range=[0,1,.2],y_range=[0,1,.2],x_length=8.5,y_length=4.6,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.2);curves=VGroup();cols=[SLATE,TEAL,CRIMSON]
 for i,(k,c) in enumerate(zip([.35,.7,1.0],cols)):
  curves.add(ax.plot(lambda x,kk=k:.45+kk*(x-.5),x_range=[.08,.92],color=c))
 mark=DashedLine(ax.c2p(.5,0),ax.c2p(.5,1),color=CRIMSON);lab=Text("threshold region",font=SERIF,color=CRIMSON,font_size=27,slant=ITALIC).next_to(mark,UP,buff=.2);return ax,curves,mark,lab
class B05_CrossingCurves(Scene):
 def construct(self):
  ax,curves,mark,lab=threshold_plot(self);self.play(Create(ax),run_time=.5);self.play(LaggedStart(*[Create(c) for c in curves],lag_ratio=.2),Create(mark),FadeIn(lab),run_time=1.2);self.wait(max(.5,D["B05"]-1.7))
class B06_AboveThreshold(Scene):
 def construct(self):
  ax,curves,mark,lab=threshold_plot(self);zone=Rectangle(width=3.7,height=4.6).set_fill(CRIMSON,.08).set_stroke(width=0).move_to(ax.c2p(.72,.5));cap=Text("larger code no longer suppresses failure",font=SERIF,color=CRIMSON,font_size=27,slant=ITALIC).move_to(DOWN*2.65);self.play(FadeIn(ax),FadeIn(curves),FadeIn(mark),FadeIn(zone),FadeIn(cap),run_time=1);self.wait(max(.5,D["B06"]-1))
class B07_NotUniversal(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.4) for t,c in [("code",TEAL),("decoder",CRIMSON),("gates",SLATE),("geometry",TEAL),("schedule",CRIMSON),("noise model",SLATE)]]).arrange_in_grid(rows=2,cols=3,buff=.5);lab=Text("no universal threshold percentage",font=DISPLAY,color=INK,font_size=40,weight=BOLD).next_to(g,DOWN,buff=.7);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.12),FadeIn(lab),run_time=1.2);self.wait(max(.5,D["B07"]-1.2))
class B08_Assumptions(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.8) for t,c in [("correlation",CRIMSON),("leakage",CRIMSON),("drift",CRIMSON),("crosstalk",CRIMSON)]]).arrange(RIGHT,buff=.35);head=title("CHECK THE NOISE MODEL","a component number alone is not enough",TEAL).to_edge(UP,buff=.7);self.play(FadeIn(head),LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.15),run_time=1.2);self.wait(max(.5,D["B08"]-1.2))
class B09_ExperimentalSignature(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(chip(f"distance {d}",SLATE,3),chip(v,c,2.5)).arrange(RIGHT,buff=.6) for d,v,c in [("3","error 1.0",CRIMSON),("5","error 0.6",TEAL),("7","error 0.3",TEAL)]]).arrange(DOWN,buff=.4);cap=Text("matched conditions · systematic suppression",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(rows,DOWN,buff=.6);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.2),FadeIn(cap),run_time=1.3);self.wait(max(.5,D["B09"]-1.3))
class B10_Overhead(Scene):
 def construct(self):
  g=VGroup(*[chip(t,c,2.7) for t,c in [("physical qubits",TEAL),("syndrome cycles",CRIMSON),("decoder",SLATE),("logical gates",TEAL)]]).arrange(RIGHT,buff=.35);head=title("BELOW THRESHOLD","overhead still matters",CRIMSON).to_edge(UP,buff=.7);self.play(FadeIn(head),LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.15),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Bigger Code, Fewer Errors",font=DISPLAY,color=WHITE,font_size=47,weight=BOLD);b=Text("The Threshold",font=SERIF,color="#D7C8FF",font_size=41,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Code distance measures how large an unde'))
  stmt=Text('Code distance measures how large an undetectable logica',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Increasing distance raises the minimum weight of that d',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Above that region, increasing distance d'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Above that region, increasing distance does not suppres',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Extra faulty components and correction circuitry can ou',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('The threshold is not a universal percent'))
  stmt=Text('The threshold is not a universal percentage',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It depends on the code, decoder, gate set, measurement ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.0
  self.add(bg(),ttl('Correlated faults, leakage, drift, and l'))
  stmt=Text('Correlated faults, leakage, drift, and long-range cross',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A reported component error below some number is not by ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Experiments can test below-threshold beh'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Experiments can test below-threshold behavior by compar',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The signature is systematic suppression as distance gro',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Even below threshold, useful logical err'))
  stmt=Text('Even below threshold, useful logical error rates requir',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('More physical qubits, repeated syndrome cycles, decodin',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('Bigger code, fewer errors — below a'))
  stmt=Text('Bigger code, fewer errors — below a conditional thresho',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
