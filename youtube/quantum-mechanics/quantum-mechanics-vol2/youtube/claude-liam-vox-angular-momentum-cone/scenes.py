import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def cone(theta=35,scale=1):
 a=np.deg2rad(theta); o=DOWN*1.6; top=o+UP*5*scale
 axis=Arrow(o,top,color=SLATE,buff=0,stroke_width=3)
 tip=o+np.array([5*scale*np.sin(a),5*scale*np.cos(a),0])
 vec=Arrow(o,tip,color=CRIMSON,buff=0,stroke_width=7)
 shadow=Arrow(o,o+UP*5*scale*np.cos(a),color=TEAL,buff=0,stroke_width=7)
 arc=Arc(radius=1.15,start_angle=np.pi/2-a,angle=a,color=INK).move_arc_center_to(o)
 return VGroup(axis,vec,shadow,arc)
class B02_Cone(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('MAXIMUM Lz STILL LEAVES A LEAN')); c=cone(); labs=VGroup(Text('|L|',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*3+UP*1.3),Text('Lz max',font=MONO,font_size=28,color=TEAL).move_to(LEFT*1.3+UP*.8),Text('z',font=MONO,font_size=26,color=SLATE).move_to(UP*3)); self.play(Create(c),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B03_Lengths(Scene):
 def construct(self):
  d=DUR.get('B03',10); self.add(bg(),ttl('THE MAGNITUDE OUTGROWS ITS BIGGEST SHADOW')); rows=VGroup(Text('|L| = hbar sqrt(l(l+1))',font=MONO,font_size=40,color=CRIMSON),Text('Lz,max = l hbar',font=MONO,font_size=40,color=TEAL),Text('sqrt(l(l+1)) > l   for every l > 0',font=MONO,font_size=34,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B04_Classical(Scene):
 def construct(self):
  d=DUR.get('B04',10); self.add(bg(),ttl('CLASSICALLY, THE ARROW MAY ALIGN')); a=Arrow(DOWN*2,UP*2.4,color=TEAL,buff=0,stroke_width=8); axis=DashedLine(DOWN*2.5,UP*2.8,color=SLATE); lab=Text('exact alignment allowed',font=SERIF,font_size=34,color=TEAL).move_to(DOWN*3); self.play(Create(axis),GrowArrow(a),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B05_SharpZ(Scene):
 def construct(self):
  d=DUR.get('B05',8); self.add(bg(),ttl('A SHARP PROJECTION IS NOT A SHARP DIRECTION')); meter=NumberLine(x_range=[-2,2,1],length=9,color=SLATE); dot=Dot(meter.n2p(2),radius=.2,color=TEAL); labs=VGroup(Text('measurement: Lz = l hbar',font=MONO,font_size=35,color=INK).move_to(UP*2),Text('definite z-shadow',font=SERIF,font_size=32,color=TEAL).move_to(DOWN*2)); self.play(Create(meter),FadeIn(dot,labs),run_time=1); self.wait(max(.1,d-1))
class B06_Budget(Scene):
 def construct(self):
  d=DUR.get('B06',11); self.add(bg(),ttl('THE SQUARED-COMPONENT BUDGET')); eq=Text('L^2 = Lx^2 + Ly^2 + Lz^2',font=MONO,font_size=45,color=INK); boxes=VGroup(*[RoundedRectangle(width=2.5,height=1.2,corner_radius=.15,color=c).set_fill(c,.12) for c in [CRIMSON,CRIMSON,TEAL]]).arrange(RIGHT,buff=.45).move_to(DOWN*1.7); labs=VGroup(*[Text(s,font=MONO,font_size=29,color=c).move_to(b) for s,c,b in zip(['Lx^2 >= 0','Ly^2 >= 0','Lz^2 >= 0'],[CRIMSON,CRIMSON,TEAL],boxes)]); self.play(FadeIn(eq),Create(boxes),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B07_Transverse(Scene):
 def construct(self):
  d=DUR.get('B07',13); self.add(bg(),ttl('THE TOP STATE HAS UNAVOIDABLE SIDEWAYS SPREAD')); cross=VGroup(Line(LEFT*4,RIGHT*4,color=SLATE),Line(DOWN*2.5,UP*2.5,color=SLATE)); cloud=VGroup(*[Dot(np.array([2*np.cos(t),1.25*np.sin(t),0]),radius=.08,color=CRIMSON) for t in np.linspace(0,2*np.pi,36)]); eq=Text('Delta Lx^2 + Delta Ly^2 = l hbar^2',font=MONO,font_size=37,color=INK).move_to(UP*2.8); lab=Text('not zero',font=SERIF,font_size=34,color=CRIMSON).move_to(DOWN*2.8); self.play(Create(cross),FadeIn(cloud,eq,lab),run_time=1.2); self.wait(max(.1,d-1.2))
class B08_Gap(Scene):
 def construct(self):
  d=DUR.get('B08',10); self.add(bg(),ttl('THE MISSING LENGTH IS TRANSVERSE RMS')); tri=Polygon(LEFT*3+DOWN*2,LEFT*3+UP*2,RIGHT*2+DOWN*2,color=INK); labs=VGroup(Text('l hbar',font=MONO,font_size=27,color=TEAL).move_to(LEFT*3.8),Text('hbar sqrt(l)',font=MONO,font_size=27,color=CRIMSON).move_to(DOWN*2.7),Text('hbar sqrt(l(l+1))',font=MONO,font_size=27,color=INK).move_to(RIGHT*.2+UP*.5)); self.play(Create(tri),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Angle(Scene):
 def construct(self):
  d=DUR.get('B09',11); self.add(bg(),ttl('THE CONE ANGLE IS FIXED BY THE RATIO')); c=cone(35,.72).shift(LEFT*3); eqs=VGroup(Text('cos(theta) = l / sqrt(l(l+1))',font=MONO,font_size=33,color=INK),Text('l = 2  ->  theta = 35.3 deg',font=MONO,font_size=33,color=CRIMSON)).arrange(DOWN,buff=.7).move_to(RIGHT*2.6); self.play(Create(c),FadeIn(eqs),run_time=1.2); self.wait(max(.1,d-1.2))
class B10_LargeL(Scene):
 def construct(self):
  d=DUR.get('B10',10); self.add(bg(),ttl('LARGE l NARROWS THE CONE')); cs=VGroup(cone(35,.43).move_to(LEFT*4),cone(17.5,.43),cone(5,.43).move_to(RIGHT*4)); labs=VGroup(Text('l = 2',font=MONO,font_size=24,color=CRIMSON).move_to(LEFT*4+DOWN*2.8),Text('l = 10',font=MONO,font_size=24,color=INK).move_to(DOWN*2.8),Text('l very large',font=MONO,font_size=24,color=TEAL).move_to(RIGHT*4+DOWN*2.8)); self.play(*[Create(x) for x in cs],FadeIn(labs),run_time=1.3); self.wait(max(.1,d-1.3))
class B11_Caveat(Scene):
 def construct(self):
  d=DUR.get('B11',10); self.add(bg(),ttl('VECTOR MODEL — NOT A HIDDEN TRAJECTORY')); left=cone(35,.55).shift(LEFT*3); right=VGroup(Text('sharp:',font=SERIF,font_size=31,color=TEAL),Text('L^2 and Lz',font=MONO,font_size=35,color=TEAL),Text('not sharp:',font=SERIF,font_size=31,color=CRIMSON),Text('Lx and Ly',font=MONO,font_size=35,color=CRIMSON)).arrange(DOWN,buff=.35).move_to(RIGHT*3); self.play(Create(left),FadeIn(right),run_time=1); self.wait(max(.1,d-1))
class B12_Worked(Scene):
 def construct(self):
  d=DUR.get('B12',14); self.add(bg(),ttl('WORKED EXAMPLE: l = 2')); eqs=VGroup(Text('|L| = hbar sqrt(6) = 2.45 hbar',font=MONO,font_size=34,color=INK),Text('Lz,max = 2 hbar',font=MONO,font_size=34,color=TEAL),Text('theta = arccos(2/sqrt(6)) = 35.3 deg',font=MONO,font_size=31,color=CRIMSON)).arrange(DOWN,buff=.65); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN')); q=VGroup(Text('Set l = 10',font=DISPLAY,font_size=39,color=TEAL),Text('theta = arccos(10 / sqrt(110))',font=MONO,font_size=35,color=INK),Text('Estimate first — then calculate.',font=SERIF,font_size=31,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(q),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',10); self.add(bg(),Text('WHY ANGULAR MOMENTUM',font=DISPLAY,font_size=35,color=INK).move_to(UP*2.4),Text('CAN NEVER POINT STRAIGHT UP',font=DISPLAY,font_size=38,color=CRIMSON).move_to(UP*1.5),Text('|L| > Lz,max',font=MONO,font_size=46,color=TEAL).move_to(DOWN*.1),Text('unavoidable transverse spread',font=SERIF,font_size=32,color=INK).move_to(DOWN*1.6)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.49
  self.add(bg(),ttl('Set it to the maximum allowed orientatio'))
  stmt=Text('Set it to the maximum allowed orientation',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The z-component reaches its ceiling',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.71
  self.add(bg(),ttl('But here is the constraint the algebra'))
  stmt=Text('But here is the constraint the algebra enforces',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The total squared magnitude equals L-x squared plus L-y',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.29
  self.add(bg(),ttl('For the vector to point straight up,'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('For the vector to point straight up, both sideways comp',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('But in any state with a definite z-component, the sidew',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.47
  self.add(bg(),ttl('So the total length is always strictly'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('So the total length is always strictly bigger than the ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The gap is hbar times root-ell — that is the mandatory ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.07
  self.add(bg(),ttl('The cone half-angle — the lean off'))
  stmt=Text('The cone half-angle — the lean off the axis — is the ar',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('For ell equals two, that is about 35 degrees',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.09
  self.add(bg(),ttl('Take ell very large — a thousand,'))
  stmt=Text('Take ell very large — a thousand, a million',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The angle collapses nearly to zero',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=9.71
  self.add(bg(),ttl('This is not a measurement disturbance. T'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('This is not a measurement disturbance',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The x and y components have no definite value — the ang',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=14.23
  self.add(bg(),ttl('A student works out the ell-equals-two t'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('A student works out the ell-equals-two top state',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Total length is hbar root-six — about 2',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B13_SDT(Scene):
 # B13 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.05
  self.add(bg(),ttl('She tries ell equals ten. Cone half-angl'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('She tries ell equals ten',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Cone half-angle drops to about 18 degrees',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
