import math
import random
import time
import turtle

SLOW = 0 
FAST = SLOW / 2 
JITTER = 0.25 
STEP = 5 
SC = 0.6 
W, H = 752, 1344
CX, CY = W / 2, 670
BG = "#14081a"
GOLD = "#d9b45a"
GOLD_D = "#8a6420"
PINK = "#f2a0ae"
random.seed()

screen = turtle.Screen()
screen.setup(int(W * SC) + 30, int(H * SC) + 30)
screen.bgcolor(BG)
screen.title("Geometry Heart")
screen.tracer(0,0)
pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()

def to_t(x, y):
    return ((x - CX) * SC, (CY - y) * SC)

def lerp_col(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def resample(pts, step=STEP):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        k = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(1, k + 1):
            t = i / k
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    return out

def split_runs(pts, clip):
    if clip is None:
        return [pts]
    runs, cur = [], []
    for p in pts:
        if clip(*p):
            cur.append(p)
        else:
            if len(cur) > 1:
                runs.append(cur)
            cur = []
    if len(cur) > 1:
        runs.append(cur)
    return runs

def stroke(pts, color, w=1.0, clip=None, delay=None, every=2):
    delay = SLOW if delay is None else delay
    for run in split_runs(resample(pts), clip):
        pen.color(color)
        pen.pensize(max(1, w * SC * 1.3))
        pen.penup()
        pen.goto(*to_t(*run[0]))
        pen.pendown()
        for i, (x, y) in enumerate(run[1:], 1):
            tx, ty = to_t(x, y)
            pen.goto(tx + random.uniform(-JITTER, JITTER),
                     ty + random.uniform(-JITTER, JITTER))
            if i % every == 0:
                screen.update()
                time.sleep(delay)
        pen.penup()
    screen.update()

def fill_poly(pts, color):
    pen.penup()
    pen.color(color)
    pen.fillcolor(color)
    pen.goto(*to_t(*pts[0]))
    pen.begin_fill()
    for p in pts[1:]:
        pen.goto(*to_t(*p))
    pen.end_fill()

def ellipse(cx, cy, rx, ry, n=64, rot=0):
    r = math.radians(rot)
    out = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * math.cos(r) - y * math.sin(r),
                    cy + x * math.sin(r) + y * math.cos(r)))
    return out

def poly(n, r, cx, cy, rot=-90):
    pts = [(cx + r * math.cos(math.radians(rot + 360 * i / n)),
            cy + r * math.sin(math.radians(rot + 360 * i / n))) for i in range(n)]
    return pts

def heart_pts(cx, cy, k, n=140):
    out = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        out.append((cx + k * x, cy - k * (y + 2.5)))
    return out

def pip(x, y, poly_pts):
    inside = False
    j = len(poly_pts) - 1
    for i in range(len(poly_pts)):
        xi, yi = poly_pts[i]
        xj, yj = poly_pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi + 1e-9) + xi:
            inside = not inside
        j = i
    return inside

def catmull(pts, n=10):
    P = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for j in range(n):
            t = j / n
            t2, t3 = t * t, t * t * t
            x = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(pts[-1])
    return out

def flower_lattice(cx, cy, r, rings, color, w, clip, delay):
    centers = []
    for i in range(-rings, rings + 1):
        for j in range(-rings, rings + 1):
            x = cx + r * (i + j * 0.5)
            y = cy + r * (j * math.sqrt(3) / 2)
            centers.append((math.hypot(x - cx, y - cy), x, y))
    centers.sort()
    for _, x, y in centers:
        c = ellipse(x, y, r, r, 48)
        if any(clip(*p) for p in c):
            stroke(c, color, w, clip=clip, delay=delay, every=3)

HEART_GLOW = heart_pts(376, 685, 19.5)
HEART_IN = heart_pts(376, 685, 14.4)
HEART_INNER = heart_pts(376, 672, 7.0)

def outside_heart(x, y):
    return not pip(x, y, HEART_GLOW)

def big_circle(x, y):
    return math.hypot(x - CX, y - CY) <= 332 and outside_heart(x, y)

def in_heart(x, y):
    return pip(x, y, HEART_IN)

def in_inner(x, y):
    return pip(x, y, HEART_INNER)

def spiral(cx, cy, r0, r1, turns, theta_end, direction=1, n=90):
    pts = []
    for i in range(n + 1):
        t = i / n
        r = r0 * (r1 / r0) ** t
        th = math.radians(theta_end - direction * turns * 360 * (1 - t))
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    return pts


def ornament(mirror):
    X = (lambda x: W - x) if mirror else (lambda x: x)
    d = -1 if mirror else 1

    def sp(cx, cy, r1, turns, th_end, w):
        th = 180 - th_end if mirror else th_end
        pts = spiral(X(cx), cy, 2.5, r1, turns, th, d)
        stroke(pts, GOLD_D, w + 2.5, delay=FAST)
        stroke(pts, GOLD, w, delay=FAST)
        stroke([(x - 0.8, y - 0.8) for x, y in pts], "#fff0b8", 1, delay=FAST)

    path = [(198, 541), (160, 572), (148, 612), (165, 652),
            (190, 692), (220, 730), (255, 765), (292, 782)]
    pts = catmull([(X(x), y) for x, y in path], 10)
    stroke(pts, GOLD_D, 10, delay=SLOW)
    stroke(pts, GOLD, 6.5, delay=SLOW)
    stroke([(x - 1.2, y - 1.2) for x, y in pts], "#fff0b8", 1.5, delay=SLOW)
    for i in range(2, len(pts) - 2, 4): 
        (x0, y0), (x1, y1) = pts[i - 1], pts[i + 1]
        L = math.hypot(x1 - x0, y1 - y0) + 1e-6
        nx, ny = -(y1 - y0) / L, (x1 - x0) / L
        x, y = pts[i]
        stroke([(x - nx * 5.5, y - ny * 5.5), (x + nx * 5.5, y + ny * 5.5)],
               GOLD_D, 1.2, delay=0.001, every=1)
    sp(230, 530, 34, 2.3, 160, 5)
    sp(192, 608, 19, 2.0, 40, 3.5)
    sp(212, 676, 17, 2.0, 40, 3.5)
    sp(243, 736, 18, 2.0, 40, 3.5)
    sp(296, 777, 16, 2.0, 70, 3.5)

def icon(kind, cx, cy, s=20):
    if kind == "tri":
        a = poly(3, s, cx, cy + 3)
        b = poly(3, s * 0.5, cx, cy + 3, 90)
        for p in (a, b):
            stroke(p + [p[0]], GOLD, 1.2, delay=0.002, every=1)
        for v in a:
            stroke([v, (cx, cy + 3)], GOLD, 0.8, delay=0.002, every=1)
    elif kind == "pent":
        a = poly(5, s, cx, cy)
        stroke(a + [a[0]], GOLD, 1.2, delay=0.002, every=1)
        star = [a[(2 * i) % 5] for i in range(6)]
        stroke(star, GOLD, 0.9, delay=0.002, every=1)
    elif kind == "hex":
        a = poly(6, s, cx, cy)
        stroke(a + [a[0]], GOLD, 1.2, delay=0.002, every=1)
        b = poly(6, s * 0.5, cx, cy)
        stroke(b + [b[0]], GOLD, 0.8, delay=0.002, every=1)
        for i in (0, 2, 4):
            stroke([a[i], (cx, cy)], GOLD, 0.8, delay=0.002, every=1)
    elif kind == "circ":
        stroke(ellipse(cx, cy, s, s, 40), GOLD, 1.3, delay=0.002, every=1)
        stroke(ellipse(cx, cy, s * 0.65, s * 0.65, 32), GOLD, 0.9, delay=0.002, every=1)
        t = poly(3, s * 0.35, cx, cy)
        stroke(t + [t[0]], GOLD, 0.9, delay=0.002, every=1)
    else:
        a = poly(4, s, cx, cy, -45)
        b = poly(4, s * 0.55, cx + 2, cy - 2, -45)
        stroke(a + [a[0]], GOLD, 1.2, delay=0.002, every=1)
        stroke(b + [b[0]], GOLD, 0.9, delay=0.002, every=1)
        for p, q in zip(a, b):
            stroke([p, q], GOLD, 0.8, delay=0.002, every=1)

ICONS = [("tri", 375, 108, 20), ("circ", 376, 215, 26), ("pent", 251, 227, 22),
         ("hex", 506, 228, 22), ("circ", 153, 296, 20), ("hex", 597, 296, 20),
         ("tri", 57, 408, 20), ("cube", 692, 410, 20), ("cube", 58, 884, 20),
         ("circ", 693, 886, 20), ("pent", 150, 988, 22), ("pent", 603, 990, 22),
         ("hex", 252, 1062, 22), ("cube", 377, 1058, 22), ("circ", 503, 1058, 14)]

def dotted(x, y0, y1):
    n = int(abs(y1 - y0) / 7)
    for i in range(n + 1):
        y = y0 + (y1 - y0) * i / max(1, n)
        pen.goto(*to_t(x, y))
        pen.dot(2, "#e8c0c8")
    screen.update()

def star4(x, y, s, color="#ffffff"):
    stroke([(x - s, y), (x + s, y)], color, 1, delay=0.001, every=1)
    stroke([(x, y - s * 1.6), (x, y + s * 1.6)], color, 1, delay=0.001, every=1)
    stroke([(x - s * .5, y - s * .5), (x + s * .5, y + s * .5)], color, 0.7, delay=0.001, every=1)
    stroke([(x - s * .5, y + s * .5), (x + s * .5, y - s * .5)], color, 0.7, delay=0.001, every=1)

def main():
    for a in range(0, 360, 10):
        r = math.radians(a)
        stroke([(CX + 300 * math.cos(r), CY + 300 * math.sin(r)),
                (CX + 900 * math.cos(r), CY + 900 * math.sin(r))],
               "#3a1a2c", 1, delay=0.0005, every=4,
               clip=lambda x, y: 0 <= x <= W and 0 <= y <= H)
    for i in range(10):
        t = i / 9
        fill_poly(ellipse(CX, 655, 376 - 226 * t, 130 - 90 * t, 60),
                  lerp_col(BG, "#7e3048", t * 0.9))

    for A, ph, col in [(40, 0.0, "#a8586c"), (55, 1.4, "#c77c86"), (30, 2.8, "#7d3f55"),
                       (48, 4.2, "#d38d98")]:
        pts = [(CX + A * math.sin(y / 90 + ph) * (0.4 + 0.6 * math.sin(math.pi * y / H)), y)
               for y in range(0, H + 1, 6)]
        stroke(pts, col, 1, clip=outside_heart, delay=0.001, every=3)
    for rx in (150, 100):
        stroke(ellipse(CX, CY, rx, 650, 120), "#8a4658", 1, clip=outside_heart,
               delay=0.001, every=3)
    for i in range(7):
        amp = 22 - i * 2
        pts = [(x, 655 + amp * math.sin(x / 38 + i * 0.7) * math.exp(-((x - CX) / 300) ** 2))
               for x in range(0, W + 1, 4)]
        stroke(pts, "#ffe9ec" if i % 2 == 0 else PINK, 1, clip=outside_heart,
               delay=0.001, every=3)

    for r in (332, 344, 300):
        stroke(ellipse(CX, CY, r, r, 160), PINK, 1.1, clip=outside_heart, delay=0.002, every=2)
    flower_lattice(CX, CY, 41, 9, "#d98a98", 0.8, big_circle, FAST)

    for i in range(9):
        fill_poly(heart_pts(376, 685, 19.5 - i * 0.3),
                  lerp_col(BG, "#ff7d96", (i + 1) / 9 * 0.65))
    fill_poly(heart_pts(376, 685, 16.4), "#fff0f2")
    fill_poly(heart_pts(376, 685, 16.0), "#f07a8c")
    fill_poly(heart_pts(376, 685, 14.7), "#ffd9dc")
    fill_poly(heart_pts(376, 685, 14.4), "#2b0a1f")

    flower_lattice(376, 685, 28, 12, "#b08a36", 0.9, in_heart, FAST)

    fill_poly(heart_pts(376, 672, 8.0), "#f3d2a0")
    fill_poly(heart_pts(376, 672, 7.6), "#e8c882")
    fill_poly(heart_pts(376, 672, 7.3), "#8a1232")
    fill_poly(heart_pts(376, 672, 7.0), "#7a0f2e")
    mc = [(376, 668)] + [(376 + 46 * math.cos(math.radians(60 * i - 90)),
                          668 + 46 * math.sin(math.radians(60 * i - 90))) for i in range(6)]
    mc += [(376 + 92 * math.cos(math.radians(60 * i - 90)),
            668 + 92 * math.sin(math.radians(60 * i - 90))) for i in range(6)]
    for (x, y) in mc:
        stroke(ellipse(x, y, 46, 46, 48), "#f4b6c0", 0.9, clip=in_inner, delay=FAST, every=3)
    for i in range(len(mc)):
        for j in range(i + 1, len(mc)):
            stroke([mc[i], mc[j]], "#ffd9de", 0.7, clip=in_inner, delay=0.001, every=3)
    for rot, rr in ((0, 62), (180, 62)):
        t = poly(3, rr, 376, 668, -90 + rot)
        stroke(t + [t[0]], "#ffffff", 1.2, clip=in_inner, delay=FAST)
    stroke(ellipse(376, 668, 8, 8, 24), "#ffffff", 1.5, delay=FAST)
    ornament(False)
    ornament(True)
    stroke(heart_pts(376, 685, 16.4), "#ffffff", 1.6, delay=0.002, every=2)

    for kind, x, y, s in ICONS:
        icon(kind, x, y, s)
        if abs(x - CX) > 20:
            if y < CY:
                dotted(x, y + s + 6, y + s + 90)
            else:
                dotted(x, y - s - 6, y - s - 90)

    pal = ["#ffffff", "#ffd5dc", "#f2a0ae", "#ffe9b0"]
    for n in range(650):
        if n % 3 == 0:
            x, y = CX + random.gauss(0, 45), random.uniform(0, H)
        else:
            a = random.uniform(0, 2 * math.pi)
            r = min(abs(random.gauss(0, 190)), 360)
            x, y = CX + r * math.cos(a), CY + r * math.sin(a)
        pen.goto(*to_t(x, y))
        pen.dot(random.choice([1.5, 2, 2.5, 3.5]), random.choice(pal))
        if n % 12 == 0:
            screen.update()
            time.sleep(0.01)
    for x, y, s in [(376, 75, 18), (376, 430, 12), (376, 1135, 18), (376, 905, 10),
                    (240, 460, 9), (512, 880, 9), (120, 650, 8), (640, 690, 8)]:
        star4(x, y, s)
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()