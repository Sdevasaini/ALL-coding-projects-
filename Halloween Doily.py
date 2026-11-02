import math
import random
import time
import turtle

SLOW = 0 
STEP = 3
JITTER = 0.7 
PASSES = 2
N = 12 
BG = "#1b1b1b"

random.seed(7)
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor(BG)
screen.title("Halloween Doily")
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()
pen.hideturtle()
SHADES = ["#f2f2f2", "#d9d9d9", "#e8e8e8", "#c8c8c8", "#fafafa"]

def resample(pts, step=STEP):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        d = math.hypot(x1 - x0, y1 - y0)
        k = max(1, int(d / step))
        for i in range(1, k + 1):
            t = i / k
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    return out

def stroke(pts, width=1.2):
    pts = resample(pts)
    for _ in range(PASSES):
        pen.color(random.choice(SHADES))
        pen.pensize(max(1, width + random.uniform(-0.3, 0.4)))
        ox, oy = random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6)
        pen.penup()
        pen.goto(pts[0][0] + ox, pts[0][1] + oy)
        pen.pendown()
        for i, (x, y) in enumerate(pts[1:], 1):
            pen.goto(x + ox + random.uniform(-JITTER, JITTER),
                     y + oy + random.uniform(-JITTER, JITTER))
            if i % 2 == 0:
                screen.update()
                time.sleep(SLOW)
        pen.penup()
    screen.update()

def pol(r, a_deg):
    a = math.radians(a_deg)
    return (r * math.cos(a), r * math.sin(a))

def ellipse(cx, cy, rx, ry, t0=0, t1=360, n=48):
    return [(cx + rx * math.cos(math.radians(t0 + (t1 - t0) * i / n)),
             cy + ry * math.sin(math.radians(t0 + (t1 - t0) * i / n)))
            for i in range(n + 1)]

def place(local_pts, origin, a_deg, scale=1.0):
    a = math.radians(a_deg)
    ux, uy = math.cos(a), math.sin(a) 
    tx, ty = -math.sin(a), math.cos(a)
    ox, oy = origin
    return [(ox + scale * (x * tx + y * ux), oy + scale * (x * ty + y * uy))
            for x, y in local_pts]

def draw_local(shapes, origin, a_deg, scale=1.0, width=1.2):
    for s in shapes:
        stroke(place(s, origin, a_deg, scale), width)

def pumpkin_shapes():
    s = []
    s.append(ellipse(0, 0, 40, 30)) 
    s.append(ellipse(0, 0, 27, 29, 0, 360)) 
    s.append(ellipse(0, 0, 14, 29, 0, 360))
    s.append([(-4, 29), (-2, 38), (4, 40), (6, 30)]) 
    s.append([(-20, 6), (-8, 6), (-14, 17), (-20, 6)]) 
    s.append([(8, 6), (20, 6), (14, 17), (8, 6)]) 
    s.append([(-18, -8), (-10, -14), (-5, -9), (0, -15),
              (5, -9), (10, -14), (18, -8)])
    return s

def skull_shapes():
    s = []
    s.append(ellipse(0, 4, 14, 15, 0, 360, 36)) 
    s.append([(-9, -8), (-9, -15), (9, -15), (9, -8)]) 
    s.append(ellipse(-6, 4, 4, 4.5, 0, 360, 16)) 
    s.append(ellipse(6, 4, 4, 4.5, 0, 360, 16))
    s.append([(0, -3), (-2, -7), (2, -7), (0, -3)]) 
    for x in (-4.5, 0, 4.5):  
        s.append([(x, -9), (x, -15)])
    return s

def spider_shapes():
    s = []
    s.append(ellipse(0, -6, 8, 13, 0, 360, 30)) 
    s.append(ellipse(0, 10, 6, 7, 0, 360, 24)) 
    s.append([(-3, -14), (0, -6), (3, -14)]) 
    for side in (-1, 1):
        for i, y in enumerate((12, 6, 0, -6)): 
            spread = 22 + i * 3
            s.append([(side * 6, y),
                      (side * (spread * 0.55), y + 12 - i * 4),
                      (side * spread, y + 2 - i * 7),
                      (side * (spread + 4), y - 12 - i * 5)])
    return s

def web_ring(r, sag, a1, a2, width=0.9):
    pts = []
    n = 14
    for i in range(n + 1):
        t = i / n
        rr = r - sag * math.sin(math.pi * t)
        pts.append(pol(rr, a1 + (a2 - a1) * t))
    stroke(pts, width)

def center_rosette():
    for r in (6, 14, 24, 34, 46):
        stroke(ellipse(0, 0, r, r, 0, 360, 60), 1.1)
    for k in range(N * 2): 
        a = k * 360 / (N * 2)
        stroke([pol(46, a), pol(58, a + 6), pol(46, a + 12)], 1)

def draw_web():
    step = 360 / N
    for k in range(N):
        stroke([pol(46, k * step), pol(345, k * step)], 1)
        stroke([pol(46, k * step + step / 2), pol(300, k * step + step / 2)], 0.8)
    for r in range(80, 340, 26):
        for k in range(N):
            web_ring(r, 9, k * step, (k + 1) * step)


def outer_edge():
    step = 360 / N
    for k in range(N):
        a = k * step
        tip = pol(375, a)
        left = pol(338, a - step / 2)
        right = pol(338, a + step / 2)
        stroke([left, pol(352, a - step / 4), tip], 1.3)
        stroke([tip, pol(352, a + step / 4), right], 1.3)
        stroke([pol(345, a), tip], 1)
    for k in range(N):
        web_ring(338, 14, k * step - step / 2, k * step + step / 2, 1.1)

def main():
    step = 360 / N
    center_rosette()
    draw_web()

    for k in range(N):
        a = k * step + step / 2
        draw_local(skull_shapes(), pol(120, a), a - 90 + 90, 1.0)
        a2 = k * step
        draw_local(skull_shapes(), pol(160, a2), a2, 0.9)

    for k in range(N):
        a = k * step + step / 2
        draw_local(spider_shapes(), pol(215, a), a, 1.0)

    for k in range(N):
        a = k * step
        draw_local(pumpkin_shapes(), pol(285, a), a, 1.05, 1.4)

    outer_edge()
    draw_local(spider_shapes(), (0, 0), 90, 0.6)

    pen.penup()
    pen.goto(0, -420)
    pen.color("#888888")
    pen.write("",
              align="center", font=("Arial", 10, "normal"))
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()