import turtle
import math
import random
import colorsys

screen = turtle.Screen()
screen.setup(width=1000, height=850)
screen.bgcolor("#03020c") 
screen.title("Cosmic Tree")
screen.colormode(1.0)
screen.tracer(5)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def refresh(step, interval=4):
    if step % interval == 0:
        screen.update()

def get_hsv(h, s=0.85, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)

random.seed(42)
num_stars = 200
star_hues = [0.55, 0.75, 0.90, 0.12, 0.0]

for i in range(num_stars):
    angle = random.uniform(0, 2 * math.pi)
    radius = random.uniform(20, 500)
    sx = radius * math.cos(angle)
    sy = radius * math.sin(angle) + 50
    size = random.uniform(0.8, 3.0)
    hue = random.choice(star_hues)
    t.penup()
    t.goto(sx, sy)
    t.pendown()
    t.dot(size, get_hsv(hue, 0.3 if hue != 0 else 0, random.uniform(0.7, 1.0)))
    refresh(i, interval=10)

screen.update()
base_y = -260

for idx, r in enumerate([320, 260, 200, 140]):
    t.penup()
    t.goto(0, base_y - (r * 0.25))
    t.pendown()
    t.pencolor(get_hsv(0.1 + idx * 0.12, 0.8, 0.5))
    t.pensize(2)
    steps = 100
    for i in range(steps + 1):
        a = (i / steps) * 2 * math.pi
        x = r * math.cos(a)
        y = base_y + (r * 0.25) * math.sin(a)
        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
        refresh(i, interval=10)

screen.update()

num_roots = 14
for r in range(num_roots):
    angle = 180 + (180 / (num_roots + 1)) * (r + 1)
    rad = math.radians(angle)
    t.penup()
    t.goto(0, base_y)
    t.pendown()
    curr_x, curr_y = 0, base_y
    root_len = random.uniform(80, 160)
    steps = 25
    
    for s in range(steps):
        frac = s / steps
        curr_x += (root_len / steps) * math.cos(rad) + random.uniform(-2, 2)
        curr_y += (root_len / steps) * math.sin(rad) + random.uniform(-2, 2)
        hue = 0.08 + frac * 0.15
        t.pencolor(get_hsv(hue, 0.9, 0.8 - frac * 0.4))
        t.pensize(max(1, int(6 * (1 - frac))))
        t.goto(curr_x, curr_y)
    refresh(r, interval=1)

screen.update()
branch_counter = [0]

def draw_blossom(x, y, size):
    num_petals = 5
    petal_len = random.uniform(8, 14)
    hue = random.choice([0.88, 0.92, 0.96, 0.05, 0.52]) 
    
    for i in range(num_petals):
        a = (360 / num_petals) * i + random.uniform(-10, 10)
        rad = math.radians(a)
        px = x + petal_len * math.cos(rad)
        py = y + petal_len * math.sin(rad)
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor(get_hsv(hue, 0.75, 0.95))
        t.pensize(2)
        t.goto(px, py)
        t.dot(random.uniform(4, 7), get_hsv(hue, 0.4, 1.0))
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5, "#ffffff")

def grow_tree(x, y, angle, length, thickness, depth):
    if depth == 0 or length < 5:
        draw_blossom(x, y, length)
        return
    
    rad = math.radians(angle)
    x_end = x + length * math.cos(rad)
    y_end = y + length * math.sin(rad)
    hue = 0.08 + (7 - depth) * 0.07
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(max(1, int(thickness)))
    t.pencolor(get_hsv(hue, 0.85, 0.85))
    t.goto(x_end, y_end)
    branch_counter[0] += 1
    if branch_counter[0] % 4 == 0:
        screen.update()

    new_len = length * random.uniform(0.72, 0.82)
    new_thick = thickness * 0.70
    spread = random.uniform(20, 32)
    grow_tree(x_end, y_end, angle - spread, new_len, new_thick, depth - 1)
    grow_tree(x_end, y_end, angle + spread, new_len, new_thick, depth - 1)
    if depth > 3 and random.random() < 0.45:
        grow_tree(x_end, y_end, angle + random.uniform(-10, 10), new_len * 0.65, new_thick * 0.60, depth - 2)

grow_tree(x=0, y=base_y, angle=90, length=125, thickness=16, depth=7)

screen.update()
num_particles = 90
for p in range(num_particles):
    px = random.uniform(-380, 380)
    py = random.uniform(base_y, 320)
    p_size = random.uniform(2.0, 5.5)
    hue = random.choice([0.14, 0.88, 0.52, 0.05])
    
    t.penup()
    t.goto(px, py)
    t.pendown()
    t.dot(p_size, get_hsv(hue, 0.3, 1.0))
    t.pencolor(get_hsv(hue, 0.6, 0.8))
    t.pensize(1)
    t.setheading(random.uniform(220, 320))
    t.forward(random.uniform(4, 12))
    refresh(p, interval=3)

screen.update()
pen.penup()
pen.goto(0, -340)
pen.pencolor("#ffffff")
pen.goto(0, -370)
pen.pencolor("#ff77c8")
screen.update()
screen.exitonclick()