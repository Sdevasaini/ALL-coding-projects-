import math
import random
import time
import turtle

SLOW = 0.004 
JITTER = 0.35 
STEP = 3 
SC = 1.3  
SIZE = 560  
PURPLE = "#9b2a8c"
PURPLE_D = "#46103f"
GREEN = "#5b8a3c"
BLUE = "#1f8fcf"
INK = "#1a1a1a"

random.seed(5)
screen = turtle.Screen()
screen.setup(int(SIZE * SC) + 30, int(SIZE * SC) + 30)
screen.bgcolor("white")
screen.title("Mandala")
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()

def T(p):
    return (p[0] * SC, p[1] * SC)

def P(r, a_deg):
    a = math.radians(a_deg)
    return (r * math.cos(a), r * math.sin(a))

def resample(pts, step=STEP):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        k = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(1, k + 1):
            t = i / k
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    return out

def stroke(pts, color=INK, w=1.2, delay=None, every=2):
    delay = SLOW if delay is None else delay
    pts = resample(pts)
    pen.color(color)
    pen.pensize(max(1, w * SC * 0.9))
    pen.penup()
    pen.goto(*T(pts[0]))
    pen.pendown()
    for i, p in enumerate(pts[1:], 1):
        x, y = T(p)
        pen.goto(x + random.uniform(-JITTER, JITTER), y + random.uniform(-JITTER, JITTER))
        if i % every == 0:
            screen.update()
            time.sleep(delay)
    pen.penup()
    screen.update()

def fill_poly(pts, color):
    pen.penup()
    pen.color(color)
    pen.fillcolor(color)
    pen.goto(*T(pts[0]))
    pen.begin_fill()
    for p in pts[1:]:
        pen.goto(*T(p))
    pen.end_fill()

def circle(r, n=120, cx=0, cy=0):
    return [(cx + r * math.cos(2 * math.pi * i / n),
             cy + r * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]

def arc(r, a0, a1, n=20):
    return [P(r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]

def ellipse(cx, cy, rx, ry, rot_deg, n=30):
    r = math.radians(rot_deg)
    out = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * math.cos(r) - y * math.sin(r),
                    cy + x * math.sin(r) + y * math.cos(r)))
    return out

def star_pts(cx, cy, R, r, n, rot):
    pts = []
    for i in range(2 * n + 1):
        rad = R if i % 2 == 0 else r
        a = math.radians(rot + 180 * i / n)
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts

def center():
    fill_poly(circle(52), GREEN)
    stroke(circle(52), INK, 1.4)
    for i in range(72): 
        a = i * 5
        stroke([P(18, a), P(52, a)], "#0e2a44", 1, delay=0.001, every=3)
    fill_poly(circle(18), BLUE)
    for r in (18, 14, 10, 6, 3): 
        stroke(circle(r, 60), "#0b3a5c", 1.1, delay=0.002)

def green_ring():
    n = 40
    spikes = []
    for i in range(2 * n + 1):
        r = 102 if i % 2 == 0 else 80
        spikes.append(P(r, 90 + 180 * i / n))
    fill_poly(spikes, GREEN)
    fill_poly(circle(76), GREEN)
    stroke(spikes, INK, 1.2, delay=0.002)
    stroke(circle(76), INK, 1.2)
    for k in range(12):
        a0 = k * 30 + 4
        a1 = a0 + 22
        band = arc(70, a0, a1) + arc(58, a1, a0)
        band.append(band[0])
        fill_poly(band, PURPLE)
        stroke(band, PURPLE_D, 1.4, delay=0.002)

def slats():
    stroke(circle(108), INK, 1.2)
    stroke(circle(138), INK, 1.2)
    n = 48
    for i in range(n):
        a = i * 360 / n
        w = 3.1
        quad = [P(108, a - w), P(138, a - w * 0.9), P(138, a + w * 0.9),
                P(108, a + w), P(108, a - w)]
        stroke(quad, INK, 1, delay=0.002, every=2)

def dotted_ring(r, n, size=2):
    for i in range(n):
        x, y = T(P(r, i * 360 / n))
        pen.goto(x, y)
        pen.dot(size * SC, INK)
        if i % 4 == 0:
            screen.update()
            time.sleep(0.01)

def ovals():
    dotted_ring(146, 90)
    for i in range(24):
        a = i * 15 + 7.5
        cx, cy = P(158, a)
        stroke(ellipse(cx, cy, 4, 9, a), INK, 1, delay=0.002)

def zigzag():
    n = 36
    pts = []
    for i in range(2 * n + 1):
        r = 190 if i % 2 == 0 else 168
        pts.append(P(r, 180 * i / n))
    stroke(pts, INK, 1.3, delay=0.003)
    stroke(circle(168), INK, 1)
    for i in range(n):  
        a = i * 360 / n + 5
        tri = [P(172, a - 3), P(184, a), P(172, a + 3), P(172, a - 3)]
        stroke(tri, INK, 0.8, delay=0.002)

def outer_rings():
    for r in (194, 201, 214):
        stroke(circle(r, 180), INK, 1.2)
    for k in range(60):
        a0 = k * 6
        stroke(arc(207.5, a0, a0 + 3.2, 6), INK, 1.1, delay=0.002, every=1)

def stars():
    n_stars = 20
    for k in range(n_stars):
        a = 90 + k * 360 / n_stars
        cx, cy = P(238, a)
        pts = star_pts(cx, cy, 39, 21, 9, a)
        fill_poly(pts, PURPLE)
        stroke(pts, PURPLE_D, 2.4, delay=0.003)

def main():
    center()
    green_ring()
    slats()
    ovals()
    zigzag()
    outer_rings()
    stars()
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()