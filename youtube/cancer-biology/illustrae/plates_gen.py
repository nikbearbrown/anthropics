# -*- coding: utf-8 -*-
# cancer-biology blank-plate generator — ONE geometry, THREE outputs:
#   (1) blank Okabe-Ito SVG plates   (2) a contact-sheet HTML   (3) an animated
#   Manim scene per plate (auto-built from the SAME shape records, so they never drift).
# House rule: a plates pass ALWAYS emits all three. No baked text on the plates.
import os, math

ORANGE="#E69F00"; SKY="#56B4E9"; GREEN="#009E73"; BLUE="#0072B2"
VERM="#D55E00"; PURPLE="#CC79A7"; GRAY="#7c7c7c"; INK="#333333"
PALETTE=[ORANGE,SKY,GREEN,BLUE,VERM,PURPLE,GRAY,INK]
SW=2.6; THIN=1.8

# ---------- shape records (backend-agnostic) ----------
def rect(x,y,w,h,color=INK,fill=None,sw=SW,rx=12,fo=0.16,dash=None):
    return {"t":"rect","x":x,"y":y,"w":w,"h":h,"color":color,"fill":fill,"sw":sw,"rx":rx,"fo":fo,"dash":dash}
def node(cx,cy,w,h,color,fo=0.16,sw=SW,rx=14):
    return rect(cx-w/2,cy-h/2,w,h,color=color,fill=color,fo=fo,sw=sw,rx=rx)
def circ(cx,cy,r,color=INK,fill=None,sw=SW,fo=0.16,dash=None):
    return {"t":"circ","cx":cx,"cy":cy,"r":r,"color":color,"fill":fill,"sw":sw,"fo":fo,"dash":dash}
def dot(cx,cy,r,color):
    return {"t":"dot","cx":cx,"cy":cy,"r":r,"color":color}
def ln(x1,y1,x2,y2,color=GRAY,sw=SW,dash=None,arrow=True):
    return {"t":"line","x1":x1,"y1":y1,"x2":x2,"y2":y2,"color":color,"sw":sw,"dash":dash,"arrow":arrow}
def poly(pts,color=INK,fill=None,sw=SW,fo=0.16,closed=True):
    return {"t":"poly","pts":list(pts),"color":color,"fill":fill,"sw":sw,"fo":fo,"closed":closed}
def white(x,y,w,h):
    return {"t":"white","x":x,"y":y,"w":w,"h":h}

def ngon(cx,cy,r,n,rot=0):
    return [(cx+r*math.cos(rot+2*math.pi*k/n), cy+r*math.sin(rot+2*math.pi*k/n)) for k in range(n)]
def star(cx,cy,ro,ri,n=5,rot=-math.pi/2):
    pts=[]
    for k in range(2*n):
        rr=ro if k%2==0 else ri; a=rot+math.pi*k/n
        pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
    return pts
def xmark(cx,cy,s,color=VERM,sw=5.5):
    return [ln(cx-s,cy-s,cx+s,cy+s,color=color,sw=sw,arrow=False),
            ln(cx-s,cy+s,cx+s,cy-s,color=color,sw=sw,arrow=False)]
def burst(cx,cy,r,color=VERM,sw=2.2):
    return poly(star(cx,cy,r,r*0.42,n=8),color=color,fill=color,fo=0.25,sw=sw)
def cluster(cx,cy,n,r,color,cols=3,gap=None,fo=0.9):
    gap=gap or r*2.4; rows=math.ceil(n/cols); out=[]; k=0
    x0=cx-(cols-1)*gap/2; y0=cy-(rows-1)*gap/2
    for ry in range(rows):
        for cxi in range(cols):
            if k>=n: break
            out.append(circ(x0+cxi*gap,y0+ry*gap,r,color=color,fill=color,fo=fo,sw=1.6)); k+=1
    return out
def vstack(x,ytop,n,w,h,color,gap=3):
    return [rect(x,ytop+i*(h+gap),w,h,color=color,fill=color,fo=0.85,sw=1.4,rx=3) for i in range(n)]

# ---------- SVG backend ----------
def _mid(c): return "a_"+c.lstrip("#")
def _svg_rec(r):
    t=r["t"]
    if t=="white":
        return f'<rect x="{r["x"]}" y="{r["y"]}" width="{r["w"]}" height="{r["h"]}" fill="#ffffff"/>'
    if t=="rect":
        fill=r["fill"]; f="none" if fill in (None,"none") else ("url(#hatch)" if fill=="hatch" else fill)
        fop="" if fill in (None,"none") else f' fill-opacity="{r["fo"]}"'
        d=f' stroke-dasharray="{r["dash"]}"' if r["dash"] else ""
        return (f'<rect x="{r["x"]}" y="{r["y"]}" width="{r["w"]}" height="{r["h"]}" rx="{r["rx"]}" ry="{r["rx"]}" '
                f'fill="{f}"{fop} stroke="{r["color"]}" stroke-width="{r["sw"]}"{d}/>')
    if t=="circ":
        fill=r["fill"]; f="none" if fill in (None,"none") else ("url(#hatch)" if fill=="hatch" else fill)
        fop="" if fill in (None,"none") else f' fill-opacity="{r["fo"]}"'
        d=f' stroke-dasharray="{r["dash"]}"' if r["dash"] else ""
        return f'<circle cx="{r["cx"]}" cy="{r["cy"]}" r="{r["r"]}" fill="{f}"{fop} stroke="{r["color"]}" stroke-width="{r["sw"]}"{d}/>'
    if t=="dot":
        return f'<circle cx="{r["cx"]}" cy="{r["cy"]}" r="{r["r"]}" fill="{r["color"]}"/>'
    if t=="line":
        d=f' stroke-dasharray="{r["dash"]}"' if r["dash"] else ""
        m=f' marker-end="url(#{_mid(r["color"])})"' if r["arrow"] else ""
        return (f'<line x1="{r["x1"]}" y1="{r["y1"]}" x2="{r["x2"]}" y2="{r["y2"]}" stroke="{r["color"]}" '
                f'stroke-width="{r["sw"]}" stroke-linecap="round"{d}{m}/>')
    if t=="poly":
        fill=r["fill"]; f="none" if fill in (None,"none") else fill
        fop="" if fill in (None,"none") else f' fill-opacity="{r["fo"]}"'
        p=" ".join(f"{x:.1f},{y:.1f}" for x,y in r["pts"])
        tag="polygon" if r["closed"] else "polyline"
        return f'<{tag} points="{p}" fill="{f}"{fop} stroke="{r["color"]}" stroke-width="{r["sw"]}" stroke-linejoin="round"/>'
    return ""
def svg(W,H,records):
    defs=('<defs>'+"".join(
            f'<marker id="{_mid(c)}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" '
            f'orient="auto-start-reverse"><path d="M0.5,0.7 L9.3,5 L0.5,9.3 L3,5 z" fill="{c}"/></marker>' for c in PALETTE)
          +'<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
          f'<line x1="0" y1="0" x2="0" y2="8" stroke="{SKY}" stroke-width="2"/></pattern></defs>')
    body="".join(_svg_rec(r) for r in records)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<rect width="{W}" height="{H}" fill="#ffffff"/>'+defs+body+'</svg>')

# ---------- Manim backend (same records → animated scene) ----------
def make_construct(records,W,H):
    def construct(self):
        from manim import (RoundedRectangle, Circle, Dot, Line, Arrow, Polygon, VMobject,
                           FadeIn, GrowArrow, LaggedStart, config)
        import numpy as np
        config.background_color="#FFFFFF"
        scale=min(11.6/W, 6.7/H)
        def P(x,y): return np.array([(x-W/2)*scale, -(y-H/2)*scale, 0.0])
        def SWm(sw): return max(1.2, sw*1.55)
        shapes=[]; arrows=[]
        for r in records:
            t=r["t"]
            if t=="white": continue
            if t=="rect":
                fill=r["fill"]; has=fill not in (None,"none"); col=r["color"]
                fcol=col if fill in (None,"none","hatch") else fill
                w=r["w"]*scale; h=r["h"]*scale; cr=min(r["rx"]*scale, w*0.45, h*0.45)
                shapes.append(RoundedRectangle(width=max(0.05,w),height=max(0.05,h),corner_radius=max(0.001,cr),
                    stroke_color=col,stroke_width=SWm(r["sw"]),fill_color=fcol,
                    fill_opacity=(r["fo"] if has else 0)).move_to(P(r["x"]+r["w"]/2,r["y"]+r["h"]/2)))
            elif t=="circ":
                fill=r["fill"]; has=fill not in (None,"none"); col=r["color"]
                fcol=col if fill in (None,"none","hatch") else fill
                shapes.append(Circle(radius=max(0.03,r["r"]*scale),stroke_color=col,stroke_width=SWm(r["sw"]),
                    fill_color=fcol,fill_opacity=(r["fo"] if has else 0)).move_to(P(r["cx"],r["cy"])))
            elif t=="dot":
                shapes.append(Dot(P(r["cx"],r["cy"]),radius=max(0.02,r["r"]*scale),color=r["color"]))
            elif t=="line":
                a,b2=P(r["x1"],r["y1"]),P(r["x2"],r["y2"])
                if r["arrow"]:
                    arrows.append(Arrow(a,b2,buff=0,color=r["color"],stroke_width=SWm(r["sw"]),
                        max_tip_length_to_length_ratio=0.14,max_stroke_width_to_length_ratio=14))
                else:
                    shapes.append(Line(a,b2,color=r["color"],stroke_width=SWm(r["sw"])))
            elif t=="poly":
                fill=r["fill"]; has=fill not in (None,"none"); col=r["color"]; pts=[P(x,y) for (x,y) in r["pts"]]
                if r["closed"]:
                    shapes.append(Polygon(*pts,stroke_color=col,stroke_width=SWm(r["sw"]),
                        fill_color=(fill if has else col),fill_opacity=(r["fo"] if has else 0)))
                else:
                    m=VMobject(stroke_color=col,stroke_width=SWm(r["sw"])); m.set_points_as_corners(pts); shapes.append(m)
        if shapes:
            self.play(LaggedStart(*[FadeIn(s,scale=0.96) for s in shapes],lag_ratio=0.07,run_time=2.4))
        if arrows:
            self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=0.06,run_time=1.6))
        self.wait(0.9)
    return construct

# ===================== PLATES (records) =====================
def p01():
    W,H=1300,430; b=[]; cy=205
    cx=[110,320,545,770,980,1175]; w=150; hw=185; h=92; hh=118
    cols=[SKY,SKY,BLUE,GREEN,VERM,VERM]; edges=[]
    for i,x in enumerate(cx):
        ww=hw if i==2 else w; hh2=hh if i==2 else h
        b.append(node(x,cy,ww,hh2,cols[i],sw=(3.4 if i==2 else SW))); edges.append((x-ww/2,x+ww/2))
    for i in range(5): b.append(ln(edges[i][1]+4,cy,edges[i+1][0]-6,cy))
    return W,H,b
def p02():
    W,H=1060,540; b=[]
    def xchrom(cx,cy,arm,capr,line=BLUE,cap=GREEN):
        s=[ln(cx-arm,cy-arm,cx+arm,cy+arm,color=line,arrow=False),
           ln(cx-arm,cy+arm,cx+arm,cy-arm,color=line,arrow=False)]
        for (dx,dy) in [(-1,-1),(1,-1),(-1,1),(1,1)]:
            if capr>0.5: s.append(dot(cx+dx*arm,cy+dy*arm,capr,cap))
        return s
    xs=[95,235,375,515]; caps=[16,11,6,2]; cy=275
    for i,x in enumerate(xs):
        b+=xchrom(x,cy,44,caps[i],line=BLUE,cap=(GREEN if i<3 else VERM))
        if i<3: b.append(ln(x+52,cy,xs[i+1]-52,cy,sw=THIN))
    b.append(ln(567,cy,660,cy)); b.append(ln(675,cy,780,155,sw=THIN)); b.append(ln(675,cy,780,395,sw=THIN))
    b+=xchrom(850,155,40,0,line=GREEN)
    for (dx,dy),cr in zip([(-1,-1),(1,-1),(-1,1),(1,1)],[13,7,15,5]): b.append(dot(850+dx*40,155+dy*40,cr,GREEN))
    b.append(poly([(905,120),(915,135),(905,150),(917,165)],color=VERM,fill="none",sw=3,closed=False))
    b.append(ln(815,395,885,395,color=VERM,sw=3,arrow=False)); b+=xmark(895,395,16,color=VERM)
    return W,H,b
def p03():
    W,H=1240,600; b=[]; hx,hy=120,300
    b.append(poly(ngon(hx,hy,60,6,rot=math.pi/6),color=BLUE,fill=BLUE,fo=0.18,sw=3.2))
    uty=150; b.append(ln(hx+55,hy-30,250,uty+10,sw=THIN)); ux=[300,470,640]
    for i,x in enumerate(ux):
        b.append(node(x,uty,90,64,VERM))
        if i<2: b.append(ln(x+46,uty,ux[i+1]-46,uty))
    b.append(ln(ux[-1]+46,uty,760,uty)); b+=cluster(830,uty,6,11,ORANGE,cols=3)
    b.append(rect(905,uty-45,86,90,color=ORANGE,fill=ORANGE,fo=0.8,sw=2,rx=8))
    lty=450; b.append(ln(hx+55,hy+30,250,lty-10,sw=THIN)); lx=[300,470,640]
    for i,x in enumerate(lx):
        b.append(node(x,lty,90,64,GREEN))
        if i<2: b.append(ln(x+46,lty,lx[i+1]-46,lty))
    b.append(ln(lx[-1]+46,lty,760,lty))
    b.append(poly([(810,lty-18),(840,lty+22),(780,lty+22)],color=SKY,fill=SKY,fo=0.7,sw=2))
    b.append(rect(852,lty-16,44,32,color=SKY,fill=SKY,fo=0.7,sw=2,rx=4))
    b.append(rect(905,lty-6,58,14,color=SKY,fill=SKY,fo=0.7,sw=2,rx=7))
    b.append(rect(978,lty-20,40,40,color=ORANGE,fill=ORANGE,fo=0.8,sw=2,rx=6))
    return W,H,b
def p04():
    W,H=760,760; b=[]; cx,cy,R=380,380,250
    b.append(circ(cx,cy,R,color=GRAY,fill="none",sw=SW+0.4))
    ang=math.radians(-35); ax,ay=cx+R*math.cos(ang),cy+R*math.sin(ang)
    b.append(ln(ax-2,ay-14,ax+10,ay+8,color=GRAY))
    ga=math.radians(210); gx,gy=cx+R*math.cos(ga),cy+R*math.sin(ga)
    b.append(rect(gx-13,gy-13,26,26,color=VERM,fill=VERM,fo=0.5,sw=3,rx=4))
    for a_deg in (234,186):
        a=math.radians(a_deg); px,py=cx+R*math.cos(a),cy+R*math.sin(a)
        b.append(circ(px,py,26,color=BLUE,fill=BLUE,fo=0.2,sw=3))
        ox,oy=cx+(R+70)*math.cos(a),cy+(R+70)*math.sin(a)
        b.append(ln(px+26*math.cos(a),py+26*math.sin(a),ox,oy,color=GRAY))
    return W,H,b
def p05():
    W,H=1120,560; b=[]; inx=150; iny=[110,250,390,530]; gx,gy=640,320; fx=970
    b.append(node(gx,gy,150,150,BLUE,sw=3.4)); b.append(node(fx,gy,140,96,GREEN))
    for y in iny:
        b.append(node(inx,y,150,86,SKY)); b.append(ln(inx+78,y,gx-82,gy+(y-gy)*0.12))
    b.append(ln(gx+78,gy,fx-72,gy)); return W,H,b
def p06():
    W,H=1300,470; b=[]; fx,fy=150,300
    b.append(poly([(fx-16,fy+70),(fx+16,fy+70),(fx,fy+30)],color=GRAY,fill=GRAY,fo=0.4,sw=2))
    lx,ly=fx-95,fy+8; rx,ry=fx+95,fy+45
    b.append(ln(lx,ly,rx,ry,color=INK,sw=3.4,arrow=False))
    b+=vstack(fx-118,ly-40,2,46,16,SKY); b+=vstack(fx+72,ry-70,3,46,16,VERM)
    b.append(ln(285,fy,360,fy))
    mx,my=470,300
    b.append(rect(mx-55,my-95,110,190,color=BLUE,fill=BLUE,fo=0.16,sw=3.2,rx=54))
    b.append(white(mx+40,my-22,30,44))
    for (dx,dy) in [(78,-40),(96,-8),(88,26),(112,6),(104,42)]: b.append(dot(mx+dx,my+dy,10,ORANGE))
    b.append(ln(mx+130,my,690,my))
    wx,wy=850,300; b.append(circ(wx,wy,26,color=GREEN,fill=GREEN,fo=0.25,sw=2.6))
    for k in range(7):
        a=2*math.pi*k/7-math.pi/2
        b.append(poly([(wx+26*math.cos(a),wy+26*math.sin(a)),(wx+70*math.cos(a-0.16),wy+70*math.sin(a-0.16)),
                       (wx+70*math.cos(a+0.16),wy+70*math.sin(a+0.16))],color=GREEN,fill=GREEN,fo=0.5,sw=2))
    return W,H,b
def p07():
    W,H=1120,720; b=[]
    def state(cy,all_att,gate_open):
        s=[]; x0,x1=150,600; pL=(120,cy); pR=(630,cy)
        s.append(ln(x0,cy,x1,cy,color=GRAY,sw=SW,dash="2 8",arrow=False))
        s.append(dot(*pL,7,GREEN)); s.append(dot(*pR,7,GREEN))
        for i,px in enumerate([230,330,430,530]):
            un=(not all_att) and i==2
            s.append(circ(px-9,cy,15,color=BLUE,fill=BLUE,fo=0.25,sw=2.2))
            s.append(circ(px+9,cy,15,color=BLUE,fill=BLUE,fo=0.25,sw=2.2))
            if not un:
                s.append(ln(px,cy,pL[0]+8,cy,color=GRAY,sw=1.4,arrow=False))
                s.append(ln(px,cy,pR[0]-8,cy,color=GRAY,sw=1.4,arrow=False))
            else:
                s.append(ln(px,cy,px-40,cy-30,color=GRAY,sw=1.4,arrow=False)); s.append(burst(px-52,cy-40,20,color=VERM))
        if gate_open:
            s.append(ln(690,cy,760,cy)); s+=cluster(830,cy-30,3,13,BLUE,cols=1); s+=cluster(830,cy+30,3,13,BLUE,cols=1)
            s.append(ln(690,cy-40,600,cy-40,color=GRAY,sw=1.2))
        else:
            s.append(ln(690,cy,745,cy)); s.append(rect(752,cy-42,16,84,color=ORANGE,fill=ORANGE,fo=0.6,sw=3,rx=5))
        return s
    b+=state(200,False,False); b.append(ln(560,360,560,300,color=GRAY,sw=1.4,arrow=False,dash="2 7")); b+=state(520,True,True)
    return W,H,b
def p08():
    W,H=1240,560; b=[]; sx,sy=140,280
    b.append(poly(ngon(sx,sy,52,7,rot=-math.pi/2),color=PURPLE,fill=PURPLE,fo=0.22,sw=3.2))
    conv=(1080,280); b+=cluster(conv[0],conv[1],6,17,GREEN,cols=3)
    for (bx,by) in [(540,150),(540,410)]:
        b.append(ln(sx+52,sy+(by-sy)*0.14,bx-70,by))
        b.append(poly(ngon(bx,by,44,8,rot=math.pi/8),color=BLUE,fill=BLUE,fo=0.18,sw=3)); b+=xmark(bx,by,26,color=VERM)
        b.append(ln(bx+58,by,conv[0]-70,conv[1]+(by-conv[1])*0.14))
    return W,H,b
def p09():
    W,H=1240,600; b=[]
    def ladder(x0,blocked):
        s=[]; steps=5; pts=[(x0+i*70,470-i*80) for i in range(steps)]
        s.append(circ(pts[0][0],pts[0][1],26,color=SKY,fill=SKY,fo=0.3,sw=2.6))
        for i in range(steps-1):
            s.append(ln(pts[i][0]+18,pts[i][1]-14,pts[i+1][0]-18,pts[i+1][1]+14,color=(GREEN if not blocked else GRAY)))
        mx,my=pts[-1]; s.append(poly(star(mx,my,30,13,n=6),color=BLUE,fill=BLUE,fo=0.35,sw=2.4))
        if blocked:
            bx,by=(pts[1][0]+pts[2][0])/2,(pts[1][1]+pts[2][1])/2
            s.append(ln(bx-46,by-46,bx+46,by+46,color=VERM,sw=6,arrow=False))
            for dx,dy in [(-30,60),(6,64),(40,58),(-8,92),(28,90),(60,80),(-40,96),(14,120)]:
                s.append(circ(pts[1][0]+dx,pts[1][1]+dy,15,color=SKY,fill=SKY,fo=0.45,sw=1.6))
        else:
            s.append(ln(pts[0][0]+22,pts[0][1]-4,mx-14,my+18,color=GREEN,sw=3.4))
        return s
    b+=ladder(120,True); b+=ladder(720,False); return W,H,b
def p10():
    W,H=1300,620; b=[]; r=15; founder=(90,310)
    b.append(circ(*founder,20,color=GRAY,fill=GRAY,fo=0.5,sw=2))
    def sub(cx,cy,t):
        if t==0: return circ(cx,cy,r,color=SKY,fill=SKY,fo=0.85,sw=1.6)
        if t==1: return circ(cx,cy,r,color=ORANGE,fill="#ffffff",sw=2.4)
        return circ(cx,cy,r,color=GREEN,fill="hatch",sw=2,fo=1)
    edges=[(founder,(250,180)),(founder,(250,440)),((250,180),(430,110)),((250,180),(430,240)),
           ((250,440),(430,370)),((250,440),(430,520)),((430,240),(600,240))]
    for a,c in edges: b.append(ln(a[0]+r,a[1],c[0]-r,c[1],color=GRAY,sw=1.6,arrow=False))
    for (cx,cy),t in [((250,180),2),((250,440),0),((430,110),1),((430,240),0),((430,370),2),((430,520),1),((600,240),0)]:
        b.append(sub(cx,cy,t))
    b.append(ln(430,60,430,95,color=VERM,sw=3.2))
    for (sx,sy),(ex,ey) in [((430,110),(520,80)),((430,370),(520,400)),((430,520),(520,560))]:
        b.append(ln(sx+r,sy,ex,ey,color=GRAY,sw=1.6,arrow=False)); b+=xmark(ex+8,ey,12,color=VERM,sw=4)
    b.append(ln(618,240,700,240,color=GRAY,sw=2)); b+=cluster(880,300,8,20,BLUE,cols=4,fo=0.85)
    return W,H,b
def p11():
    W,H=1120,640; b=[]; gy=[130,320,510]; gx=280
    for i,y in enumerate(gy):
        b.append(rect(gx-110,y-70,190,140,color=BLUE,fill=BLUE,fo=0.16,sw=3,rx=22))
        b.append(white(gx+80-34,y-24,40,48))
        if i!=1: b.append(poly([(gx+58,y-18),(gx+58,y+18),(gx+30,y)],color=SKY,fill=SKY,fo=0.8,sw=2))
    b.append(ln(720,320,560,320)); b.append(poly([(760,296),(760,344),(726,320)],color=ORANGE,fill=ORANGE,fo=0.8,sw=2.4))
    b.append(poly([(430,300),(430,336),(402,318)],color=VERM,fill=VERM,fo=0.85,sw=2))
    b.append(ln(452,332,560,470,color=VERM,sw=2.4)); b.append(circ(610,500,30,color=GREEN,fill=GREEN,fo=0.3,sw=2.6))
    return W,H,b
def p12():
    W,H=1120,640; b=[]
    def panel(cy,both):
        s=[]; start=(140,cy); surv=(900,cy)
        up=[(start[0]+20,cy),(360,cy-90),(640,cy-90),(surv[0]-24,cy)]
        lo=[(start[0]+20,cy),(360,cy+90),(640,cy+90),(surv[0]-24,cy)]
        s.append(circ(*start,26,color=GRAY,fill=GRAY,fo=0.35,sw=2.4))
        s.append(poly(up,color=GRAY,fill="none",sw=SW,closed=False)); s.append(poly(lo,color=GRAY,fill="none",sw=SW,closed=False))
        s+=xmark(430,cy-90,17,color=VERM)
        if both:
            s+=xmark(430,cy+90,17,color=VERM)
            s.append(poly([(surv[0]-24,cy-24),(surv[0]+4,cy-6),(surv[0]-14,cy+8),(surv[0]+18,cy+26),(surv[0]-8,cy+24)],
                          color=ORANGE,fill=ORANGE,fo=0.5,sw=2.4))
        else:
            s.append(circ(*surv,28,color=GREEN,fill=GREEN,fo=0.3,sw=3))
            s.append(ln(surv[0]-42,cy,surv[0]-26,cy,color=GRAY,sw=SW))
        return s
    b+=panel(190,False); b+=panel(470,True); return W,H,b
def p13():
    W,H=1300,600; b=[]; bx0,bx1,bary=120,1180,150
    b.append(rect(bx0,bary-22,bx1-bx0,44,color=GRAY,fill=GRAY,fo=0.18,sw=2.6,rx=22))
    for x in [250,470,690,910,1090]:
        if x in (470,690): continue
        b.append(ln(x,bary-18,x,bary+18,color=INK,sw=3,arrow=False))
    b.append(poly([(440,90),(440,70),(720,70),(720,90)],color=VERM,fill="none",sw=3,closed=False))
    b.append(rect(470-24,230-24,48,48,color=BLUE,fill=BLUE,fo=0.7,sw=2.4,rx=6))
    b.append(circ(690,230,26,color=ORANGE,fill="#ffffff",sw=3))
    b.append(ln(470,bary+20,470,205,color=GRAY,sw=1.6,arrow=False,dash="2 7"))
    b.append(ln(690,bary+20,690,205,color=GRAY,sw=1.6,arrow=False,dash="2 7"))
    b.append(ln(690,258,690,380)); b.append(circ(690,440,52,color=SKY,fill=SKY,fo=0.16,sw=3)); b+=cluster(690,440,5,10,SKY,cols=3)
    b.append(ln(900,440,760,440,color=GRAY,sw=SW)); b.append(poly([(940,416),(940,464),(906,440)],color=VERM,fill=VERM,fo=0.8,sw=2.4))
    return W,H,b
def p14():
    W,H=1240,560; b=[]; rx,ry=560,270
    b.append(rect(rx-90,ry-150,180,300,color=ORANGE,fill="none",sw=3.4,rx=26))
    for (dx,dy) in [(-40,120),(0,128),(40,118),(-18,150),(22,150)]: b.append(dot(rx+dx,ry+dy,11,ORANGE))
    b.append(ln(rx-90,ry-40,240,ry-40,color=GRAY,sw=22,arrow=False)); b+=cluster(150,ry-40,7,22,BLUE,cols=3,fo=0.8)
    for i in range(3): b.append(dot(rx-160-i*60,ry-40,7,ORANGE))
    b.append(ln(rx+90,ry-40,1000,ry-40,color=GRAY,sw=5,arrow=False))
    b.append(circ(1060,ry-40,26,color=VERM,fill=SKY,fo=0.18,sw=3,dash="4 5"))
    return W,H,b
def p15():
    W,H=1260,560; b=[]; hub=(680,300); out=(1080,300)
    b.append(node(*hub,120,120,GRAY,fo=0.18,sw=3.2,rx=20)); b+=cluster(out[0],out[1],6,17,GREEN,cols=3)
    b.append(ln(hub[0]+70,hub[1],out[0]-70,out[1]))
    ax,ay=170,150; b.append(node(ax,ay,150,84,BLUE)); b.append(ln(ax+70,ay+20,hub[0]-70,hub[1]-40))
    b.append(rect(410,205,16,64,color=VERM,fill=VERM,fo=0.6,sw=3,rx=5)); b+=xmark(418,237,15,color=VERM,sw=5)
    bx,by=170,450; b.append(node(bx,by,150,84,ORANGE)); b.append(ln(bx+70,by-20,hub[0]-70,hub[1]+40,color=ORANGE))
    return W,H,b
def p16():
    W,H=1320,540; b=[]; y=360; xs=[130,320,510,700,890,1080]
    import random; rnd=random.Random(7)
    for i,x in enumerate(xs):
        col=ORANGE if i==5 else SKY
        b.append(rect(x-78,y-70,156,140,color=col,fill=col,fo=0.14,sw=2.8,rx=16))
        n=4+i*3
        for k in range(n):
            j=i*3.0; px=x-52+(k%4)*34+rnd.uniform(-j,j); py=y-40+(k//4)*34+rnd.uniform(-j,j)
            px=max(x-70,min(x+70,px)); py=max(y-58,min(y+58,py)); b.append(dot(px,py,6.5,BLUE if i<5 else ORANGE))
        if i<5: b.append(ln(x+80,y,xs[i+1]-80,y,sw=THIN))
    bxx,byy=430,110
    b.append(poly([(bxx-46,byy+14),(bxx-16,byy-18),(bxx+14,byy+10),(bxx+44,byy-18),(bxx+74,byy+6)],color=VERM,fill="none",sw=8,closed=False))
    for tx in (xs[0],xs[1],xs[2]): b.append(ln(bxx+8,byy+26,tx,y-78,color=VERM,sw=1.8))
    return W,H,b
def p17():
    W,H=1160,640; b=[]
    def state(cy,sil):
        s=[]; x0,x1=150,650; s.append(ln(x0,cy,x1,cy,color=BLUE,sw=5,arrow=False))
        if sil:
            mx=400; s.append(poly([(mx-34,cy),(mx-30,cy-46),(mx,cy-58),(mx+30,cy-46),(mx+34,cy)],color=GREEN,fill="none",sw=5,closed=False))
        else:
            s+=xmark(400,cy-40,16,color=VERM)
        s.append(ln(x1-40,cy,x1-40,cy+70,color=GRAY,sw=SW,arrow=(not sil)))
        if sil:
            s.append(ln(x1-58,cy+58,x1-22,cy+58,color=GRAY,sw=3,arrow=False)); s.append(dot(x1-40,cy+96,10,ORANGE))
        else:
            s+=cluster(x1+120,cy+40,9,12,ORANGE,cols=3)
        return s
    b+=state(170,True); b.append(ln(360,360,360,300,color=GRAY,sw=1.4,arrow=False,dash="2 7")); b+=state(470,False)
    return W,H,b
def p18():
    W,H=1300,520; b=[]; y=230
    b.append(rect(70,y-20,120,40,color=GRAY,fill=GRAY,fo=0.18,sw=2.4,rx=10)); b.append(ln(130,y-16,130,y+16,color=INK,sw=3,arrow=False))
    b.append(ln(196,y,300,y))
    b.append(poly([(310,y),(330,y-22),(350,y),(370,y+22),(390,y)],color=BLUE,fill="none",sw=5,closed=False))
    b.append(ln(396,y,500,y)); pxx,pyy=560,y; b.append(circ(pxx,pyy,40,color=SKY,fill=SKY,fo=0.3,sw=3))
    for (dx,dy) in [(-30,-34),(2,-46),(34,-32)]: b.append(dot(pxx+dx,pyy+dy,9,VERM))
    b.append(ln(pxx,pyy+42,pxx,pyy+120,color=VERM,sw=SW))
    b.append(poly([(pxx-52,pyy+130),(pxx+52,pyy+130),(pxx+20,pyy+210),(pxx-20,pyy+210)],color=VERM,fill=VERM,fo=0.22,sw=3))
    for k in range(3): b.append(ln(pxx-52+k*34,pyy+150,pxx-34+k*34,pyy+150,color=VERM,sw=3,arrow=False))
    b.append(ln(602,y,760,y,dash="3 8")); b.append(rect(820,y-60,150,120,color=GRAY,fill="none",sw=3,rx=18,dash="7 8"))
    return W,H,b
def p19():
    W,H=1320,600; b=[]; lx,ly=150,300
    b.append(ln(70,ly,240,ly,color=GRAY,sw=5,arrow=False))
    b.append(poly([(lx,ly-16),(lx+16,ly),(lx,ly+16),(lx-16,ly)],color=VERM,fill=VERM,fo=0.85,sw=2))
    b.append(ln(250,ly,330,170,sw=THIN)); b.append(ln(250,ly,330,430,sw=THIN))
    uy=150; b.append(ln(360,uy,520,uy,color=GRAY,sw=5,arrow=False))
    b.append(circ(474,uy,22,color=GREEN,fill="none",sw=5)); b.append(white(474,uy-6,26,12))
    b.append(ln(560,uy,680,uy)); b.append(ln(700,uy,840,uy,color=GRAY,sw=5,arrow=False)); b.append(circ(950,uy,34,color=SKY,fill=SKY,fo=0.28,sw=3))
    lyy=440; b.append(rect(360,lyy-26,150,52,color=BLUE,fill=BLUE,fo=0.16,sw=2.6,rx=10))
    for k in range(4):
        px=378+k*34; b.append(ln(px,lyy+26,px,lyy+46,color=BLUE,sw=2.4,arrow=False)); b.append(dot(px,lyy+52,7,BLUE))
    b.append(ln(520,lyy,660,lyy)); b.append(ln(690,lyy,830,lyy,color=GRAY,sw=5,arrow=False))
    b.append(poly([(760,lyy-16),(776,lyy),(760,lyy+16),(744,lyy)],color=VERM,fill=VERM,fo=0.85,sw=2))
    b.append(ln(846,lyy-14,878,lyy+14,color=VERM,sw=4,arrow=False))
    b.append(poly([(930,lyy-26),(958,lyy-8),(940,lyy+6),(970,lyy+26),(944,lyy+24),(922,lyy+6)],color=ORANGE,fill=ORANGE,fo=0.5,sw=2.4))
    return W,H,b
def p20():
    W,H=1240,600; b=[]
    def meter(cx,frac,clamp,over):
        s=[]; top,bot,w=110,470,110
        s.append(rect(cx-w/2,top,w,bot-top,color=GRAY,fill="none",sw=3.2,rx=18))
        thr=top+70; s.append(ln(cx-w/2-24,thr,cx+w/2+24,thr,color=GRAY,sw=2.4,dash="7 7",arrow=False))
        ft=bot-(bot-top)*frac; col=VERM if over else SKY
        s.append(rect(cx-w/2+6,ft,w-12,bot-ft-4,color=col,fill=col,fo=0.55,sw=0.8,rx=10))
        if clamp: s.append(rect(cx-w/2-6,top-6,w+12,40,color=BLUE,fill=BLUE,fo=0.6,sw=3,rx=8))
        return s
    b+=meter(360,0.72,True,False)
    b.append(ln(150,150,300,150)); b.append(poly([(150,126),(150,174),(116,150)],color=ORANGE,fill=ORANGE,fo=0.8,sw=2.4))
    b.append(ln(470,300,650,300)); b+=meter(820,0.96,False,True)
    b.append(ln(880,150,1000,150))
    b.append(poly([(1050,124),(1078,142),(1060,156),(1090,176),(1064,174),(1042,156)],color=VERM,fill=VERM,fo=0.5,sw=2.4))
    return W,H,b

PLATES=[("01","p53-circuit",p01),("02","telomere-crisis",p02),("03","warburg-carbon",p03),
    ("04","restriction-point",p04),("05","rb-convergence",p05),("06","apoptosis-momp",p06),
    ("07","spindle-checkpoint",p07),("08","hpv-dual-hit",p08),("09","differentiation-block",p09),
    ("10","clonal-evolution",p10),("11","bcl-selectivity",p11),("12","synthetic-lethality",p12),
    ("13","mtap-passenger",p13),("14","immune-starvation",p14),("15","bypass-track",p15),
    ("16","hpylori-cancer",p16),("17","mir-deletion",p17),("18","protein-level-loss",p18),
    ("19","mgmt-methylation-paradox",p19),("20","venetoclax-priming",p20)]

META={
 "01":("the damage→p53→effector relay","relay chain","Critical"),"02":("erosion → crisis → scarred survivor","sequence + bottleneck","Important"),
 "03":("glucose: build vs burn","two-path comparison","Critical"),"04":("commitment before vs after the R point","before/after cycle","Important"),
 "05":("many signals funnel onto one gate","convergence / fan-in","Important"),"06":("balance tips → leak → apoptosome","switch → release → assembly","Critical"),
 "07":("anaphase waits for the last attachment","gate / all-clear","Important"),"08":("one virus, two brakes cut","two-track convergence","Important"),
 "09":("maturation stalls, therapy releases","arrested ladder → release","Important"),"10":("founder → subclones → resistant sweep","branching selection tree","Important"),
 "11":("which lock the drug fits","lock-and-key displacement","Important"),"12":("two roads, the double cut kills","redundancy → double-hit","Critical"),
 "13":("bystander deletion → vulnerability","co-deletion","Important"),"14":("one fuel pool, the T-cell starves","shared-resource competition","Important"),
 "15":("block the door, find a side door","reroute to shared node","Important"),"16":("irritant marches the lining stage by stage","irritant-driven stages","Important"),
 "17":("lose the silencer, the oncogene shouts","repressor removal → de-repression","Important"),"18":("blueprint fine, product destroyed","product destroyed → loss","Important"),
 "19":("silence repair, the poison works","gene-silencing fork","Important"),"20":("cell at the cliff edge, tipped over","near-threshold tip-over","Important"),
}
def build_board(outdir,htmlpath,with_video=True):
    import re as _re
    cards=[]
    for num,slug,fn in PLATES:
        title,pat,pri=META[num]; s=open(os.path.join(outdir,f"{num}-{slug}.svg")).read()
        s=_re.sub(r'(<svg[^>]*?)\swidth="[^"]*"',r'\1',s,count=1); s=_re.sub(r'(<svg[^>]*?)\sheight="[^"]*"',r'\1',s,count=1)
        badge="crit" if pri=="Critical" else "imp"
        mp4=f"manim/{num}-{slug}.mp4"; has_mp4=os.path.exists(os.path.join(outdir,mp4))
        vid=(f'<video class="viz" src="{mp4}" poster="{num}-{slug}.png" autoplay loop muted playsinline></video>' if (with_video and has_mp4) else "")
        media=(f'<div class="media"><div class="still">{s}</div>'+(f'<div class="anim">{vid}</div>' if vid else "")+'</div>')
        cards.append(f'<figure class="card">{media}<figcaption>'
            f'<div class="row"><span class="num">{num}</span><span class="slug">{slug}</span><span class="badge {badge}">{pri}</span></div>'
            f'<div class="title">{title}</div><div class="pat">{pat}</div></figcaption></figure>')
    html=('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
      '<title>cancer-biology — 20 plates (contact sheet)</title><style>'
      ':root{--bg:#FAF9F5;--ink:#3D3929;--mut:#7c766b;--line:#e7e3da;--terra:#D97757;--slate:#5b6b7a;}'
      '*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}'
      'header{padding:34px 40px 14px;border-bottom:1px solid var(--line)}h1{margin:0 0 4px;font-size:24px;letter-spacing:-.01em}'
      '.sub{color:var(--mut);font-size:14.5px;max-width:74ch}.legend{margin-top:12px;font-size:13px;color:var(--mut);display:flex;gap:18px;flex-wrap:wrap}.legend b{color:var(--ink);font-weight:600}'
      'main{padding:26px 40px 60px;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:22px}'
      '.card{margin:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.03)}'
      '.media{display:grid;grid-template-columns:1fr 1fr;gap:0}.media .still,.media .anim{padding:14px;display:flex;align-items:center;justify-content:center;min-height:170px}'
      '.media .anim{border-left:1px solid var(--line);background:#fff}.still svg,.anim .viz{width:100%;height:auto;max-height:210px}'
      '.anim .viz{border-radius:6px}figcaption{padding:10px 16px 16px;border-top:1px solid var(--line)}'
      '.row{display:flex;align-items:center;gap:9px}.num{font-variant-numeric:tabular-nums;font-weight:700;color:var(--mut);font-size:13px}'
      '.slug{font-weight:650;font-size:15px;letter-spacing:-.01em}.badge{margin-left:auto;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;padding:3px 8px;border-radius:999px}'
      '.badge.crit{background:rgba(217,119,87,.14);color:var(--terra)}.badge.imp{background:rgba(91,107,122,.12);color:var(--slate)}'
      '.title{margin-top:6px;font-size:14px}.pat{margin-top:3px;font-size:12.5px;color:var(--mut);font-style:italic}'
      'footer{padding:20px 40px 46px;color:var(--mut);font-size:12.5px;border-top:1px solid var(--line)}'
      '</style></head><body><header><h1>cancer-biology — 20 plates <span style="color:var(--mut);font-weight:400">· contact sheet</span></h1>'
      '<div class="sub">Each plate is one geometry rendered two ways: the blank Okabe-Ito <b>still</b> (SVG, labels added at previz) and its <b>Manim animation</b> (auto-built from the same shapes). Colorblind-safe, no baked text, no red/green pairing.</div>'
      '<div class="legend"><span><b>20</b> plates</span><span><b>4</b> Critical · <b>16</b> Important</span><span>still + motion, one source</span></div></header><main>'
      +''.join(cards)+'</main><footer>Blank plates + Manim viz for the cancer-biology tile worklist · <code>illustrae/plates/</code> · <code>illustrae/plates/manim/</code> · regen <code>illustrae/plates_gen.py</code>.</footer></body></html>')
    open(htmlpath,"w").write(html); return len(html)

if __name__=="__main__":
    import subprocess, shutil
    outdir=os.environ.get("PLATES_OUT") or os.path.join(os.path.dirname(os.path.abspath(__file__)),"plates")
    os.makedirs(outdir,exist_ok=True)
    try: import cairosvg; _png=True
    except Exception: _png=False
    for num,slug,fn in PLATES:
        W,H,recs=fn(); s=svg(W,H,recs)
        open(os.path.join(outdir,f"{num}-{slug}.svg"),"w").write(s)
        if _png: cairosvg.svg2png(bytestring=s.encode(),write_to=os.path.join(outdir,f"{num}-{slug}.png"),output_width=760)
    mdir=os.path.join(outdir,"manim"); os.makedirs(mdir,exist_ok=True)
    scene_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"manim_plates.py")
    rendered=0
    if shutil.which("manim") and os.path.exists(scene_file):
        for num,slug,fn in PLATES:
            cls=f"Plate{num}"
            try:
                subprocess.run(["manim","-ql","--format=mp4","--media_dir",os.path.join(mdir,"_mm"),
                                scene_file,cls],check=True,capture_output=True)
                src=os.path.join(mdir,"_mm","videos","manim_plates","480p15",f"{cls}.mp4")
                if os.path.exists(src): shutil.copy(src,os.path.join(mdir,f"{num}-{slug}.mp4")); rendered+=1
            except Exception as e:
                print("manim FAIL",num,slug,str(e)[:120])
    htmlpath=os.path.join(outdir,"contact-sheet.html")  # inside plates/ so manim/ + png paths resolve
    n=build_board(outdir,htmlpath)
    print(f"OK: 20 svgs (png={_png}) · manim rendered={rendered} · contact sheet {n}b -> {htmlpath}")
