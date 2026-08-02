import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def card(h,s,c=TEAL):
 a=Text(h,font=DISPLAY,color=INK,font_size=44,weight=BOLD);b=Text(s,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if a.width>11.5:a.scale_to_fit_width(11.5)
 if b.width>11:b.scale_to_fit_width(11)
 return VGroup(a,b).arrange(DOWN,buff=.45)
def chip(t,c=SLATE,w=2.2):
 r=Rectangle(width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=26).move_to(r)
 if x.width>w*.86:x.scale_to_fit_width(w*.86)
 return VGroup(r,x)
def axis(angle,label,c):
 v=np.array([np.cos(angle),np.sin(angle),0]);line=Arrow(ORIGIN,v*2.35,color=c,stroke_width=4,buff=0,tip_length=.2);txt=Text(label,font=MONO,color=c,font_size=23).next_to(line.get_end(),v,buff=.15);return VGroup(line,txt)
class B02_FourSettings(Scene):
 def construct(self):
  alice=VGroup(chip("A1",TEAL),chip("A2",TEAL)).arrange(DOWN,buff=.4).move_to(LEFT*4);bob=VGroup(chip("B1",SLATE),chip("B2",SLATE)).arrange(DOWN,buff=.4).move_to(RIGHT*4);out=Text("each run: +1 or -1",font=MONO,color=CRIMSON,font_size=34);self.play(FadeIn(alice),FadeIn(bob),run_time=.7);self.play(FadeIn(out),run_time=.5);self.wait(max(.5,DUR["B02"]-1.2))
class B03_CHSHScore(Scene):
 def construct(self):
  terms=[]
  for i,(t,c) in enumerate([("E11",TEAL),("+ E12",TEAL),("+ E21",TEAL),("- E22",CRIMSON)]):terms.append(chip(t,c,2.0))
  g=VGroup(*terms).arrange(RIGHT,buff=.35);h=Text("S =",font=DISPLAY,color=INK,font_size=48,weight=BOLD).next_to(g,LEFT,buff=.5);self.play(FadeIn(h),LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.18),run_time=1.1);self.wait(max(.5,DUR["B03"]-1.1))
class B04_ClassicalCeiling(Scene):
 def construct(self):
  line=Line(LEFT*5,RIGHT*5,color=INK,stroke_width=4);x2=LEFT*1.5;mark=Line(x2+DOWN*.5,x2+UP*.5,color=CRIMSON,stroke_width=6);lab=Text("2",font=MONO,color=CRIMSON,font_size=48).next_to(mark,UP,buff=.25);zone=Rectangle(width=3.5,height=.7).set_fill(TEAL,.25).set_stroke(TEAL,2).move_to(LEFT*3.25);caption=card("Local hidden-variable ceiling","|S| <= 2 with independent settings",CRIMSON).scale(.78).to_edge(UP,buff=.55);self.play(FadeIn(caption),Create(line),FadeIn(zone),Create(mark),FadeIn(lab),run_time=1);self.wait(max(.5,DUR["B04"]-1))
class B05_AliceAxes(Scene):
 def construct(self):
  c=Circle(radius=2.5).set_stroke(SLATE,2);a1=axis(0,"A1 0°",TEAL);a2=axis(np.pi/2,"A2 90°",TEAL);eq=Text("E = cos(angle difference)",font=MONO,color=INK,font_size=32).to_edge(DOWN,buff=.65);self.play(Create(c),run_time=.5);self.play(Create(a1),Create(a2),FadeIn(eq),run_time=.9);self.wait(max(.5,DUR["B05"]-1.4))
class B06_BobAxes(Scene):
 def construct(self):
  c=Circle(radius=2.5).set_stroke(SLATE,2);axes=VGroup(axis(0,"A1",TEAL),axis(np.pi/2,"A2",TEAL),axis(np.pi/4,"B1 45°",CRIMSON),axis(-np.pi/4,"B2 -45°",CRIMSON));self.play(Create(c),run_time=.4);self.play(LaggedStart(*[Create(x) for x in axes],lag_ratio=.18),run_time=1.4);self.wait(max(.5,DUR["B06"]-1.8))
class B07_FourCorrelations(Scene):
 def construct(self):
  rows=VGroup()
  for t,v,c in [("E11","+1/sqrt(2)",TEAL),("E12","+1/sqrt(2)",TEAL),("E21","+1/sqrt(2)",TEAL),("E22","-1/sqrt(2)",CRIMSON)]:rows.add(VGroup(chip(t,SLATE,1.6),chip(v,c,3.2)).arrange(RIGHT,buff=.4))
  rows.arrange(DOWN,buff=.28);self.play(LaggedStart(*[FadeIn(r,shift=RIGHT*.15) for r in rows],lag_ratio=.16),run_time=1.2);self.wait(max(.5,DUR["B07"]-1.2))
class B08_SubtractNegative(Scene):
 def construct(self):
  e=Text("S = 1/sqrt(2) + 1/sqrt(2) + 1/sqrt(2) - (-1/sqrt(2))",font=MONO,color=INK,font_size=31);e2=Text("S = 4/sqrt(2)",font=MONO,color=CRIMSON,font_size=54);g=VGroup(e,e2).arrange(DOWN,buff=.75);self.play(FadeIn(e),run_time=.6);self.play(FadeIn(e2,shift=UP*.15),run_time=.7);self.wait(max(.5,DUR["B08"]-1.3))
class B09_BellNumber(Scene):
 def construct(self):
  a=Text("4/sqrt(2)",font=MONO,color=INK,font_size=58);b=Text("2 sqrt(2)",font=MONO,color=CRIMSON,font_size=66);c=Text("≈ 2.828  ·  41% above 2",font=SERIF,color=TEAL,font_size=32,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.38);self.play(FadeIn(a),run_time=.5);self.play(ReplacementTransform(a.copy(),b),run_time=.7);self.play(FadeIn(c),run_time=.5);self.wait(max(.5,DUR["B09"]-1.7))
class B10_PatternNotOnePair(Scene):
 def construct(self):
  left=card("One perfect correlation","classical models can reproduce it",SLATE).scale(.7);right=card("Four-setting pattern","cannot share one local answer table",CRIMSON).scale(.7);g=VGroup(left,right).arrange(RIGHT,buff=1.3);arrow=Arrow(left.get_right(),right.get_left(),color=TEAL,buff=.2);self.play(FadeIn(left),run_time=.5);self.play(GrowArrow(arrow),FadeIn(right),run_time=.8);self.wait(max(.5,DUR["B10"]-1.3))
class B11_CarefulConclusion(Scene):
 def construct(self):
  bad=Text("NOT: faster-than-light messages",font=DISPLAY,color=CRIMSON,font_size=35,weight=BOLD);good=Text("YES: local hidden-variable models fail the tested bound",font=DISPLAY,color=TEAL,font_size=35,weight=BOLD);assume=Text("under locality + setting-independence assumptions",font=SERIF,color=SLATE,font_size=27,slant=ITALIC);g=VGroup(bad,good,assume).arrange(DOWN,buff=.5);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.2),run_time=1.2);self.wait(max(.5,DUR["B11"]-1.2))
class B12_Verdict(Scene):
 def construct(self):
  lines=VGroup(Text("LOCAL CEILING: 2",font=DISPLAY,color=INK,font_size=44,weight=BOLD),Text("QUANTUM GEOMETRY: 2 sqrt(2)",font=DISPLAY,color=CRIMSON,font_size=44,weight=BOLD),Text("four angles turn philosophy into a test",font=SERIF,color=TEAL,font_size=32,slant=ITALIC)).arrange(DOWN,buff=.5);self.play(LaggedStart(*[FadeIn(x,shift=UP*.12) for x in lines],lag_ratio=.2),run_time=1.3);self.wait(max(.5,DUR["B12"]-1.3))
class B14_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Where 2 Becomes 2 Root 2",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Bell's Number",font=SERIF,color="#D7C8FF",font_size=38,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,DUR["B14"]-.7))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.71
  self.add(bg(),ttl('CHSH combines them as E eleven plus'))
  stmt=Text('CHSH combines them as E eleven plus E twelve plus E twe',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The minus sign is the hinge that makes four settings te',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.48
  self.add(bg(),ttl('If outcomes are fixed by local hidden'))
  stmt=Text('If outcomes are fixed by local hidden variables, the ab',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('That is the Bell-CHSH bound, not a limit on one correla',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.39
  self.add(bg(),ttl('Cosine forty-five degrees is one over ro'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Cosine forty-five degrees is one over root two',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('So the first three correlations are plus one over root ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.27
  self.add(bg(),ttl('The violation is not perfect correlation'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The violation is not perfect correlation by itself',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('classical models can do that',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.76
  self.add(bg(),ttl('Bell tests have repeatedly observed CHSH'))
  stmt=Text('Bell tests have repeatedly observed CHSH violations',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The careful conclusion is that local hidden-variable mo',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.62
  self.add(bg(),ttl('The verdict: 2 is the local hidden-varia'))
  stmt=Text('The verdict: 2 is the local hidden-variable ceiling',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The four-angle cosine pattern reaches 2 root 2',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B14_SDT(Scene):
 # B14 SDT retrofit: generic reveal with underline
 def construct(self):
  d=4.12
  self.add(bg(),ttl('Where 2 Becomes 2 Root 2: Bell\'s'))
  stmt=Text('Where 2 Becomes 2 Root 2: Bell\'s Number',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Liam, in for Bear',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
