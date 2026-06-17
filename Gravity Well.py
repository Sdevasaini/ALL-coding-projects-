import turtle
import math
import colorsys
import time

WIDTH, HEIGHT = 900, 900
orbit_speed = 30.0
gravity_pull = 1.0
palette_mode = 0
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("#030208")
screen.title("Hypnotic Gravity Well")
screen.tracer(0)
orbiters = []

for _ in range(4):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    orbiters.append(t)
center = turtle.Turtle()
center.hideturtle()
center.speed(0)
center.penup()
center.goto(0, -15)
center.dot(35, "#221144")
center.dot(18, "white")
angles = [0, 90, 180, 270]

for i, t in enumerate(orbiters):
    radius = 120 + i * 70
    a = math.radians(angles[i])
    x = radius * math.cos(a)
    y = radius * math.sin(a)
    t.goto(x, y)
    t.pendown()

step = 0

try:
    while True:
        step += 1
        for i, t in enumerate(orbiters):
            base_radius = 100 + i * 65
            angles[i] += (0.35 / (1 + i * 0.5)) * orbit_speed
            a = math.radians(angles[i])
            warp = 1 + (
                0.35
                * gravity_pull
                * math.sin(a * 3.5 + step * 0.005)
            )
            radius = base_radius * warp
            x = radius * math.cos(a)
            y = radius * math.sin(a)
            if palette_mode == 0:
                hue = (
                    i * 0.08
                    + math.sin(step * 0.002) * 0.05
                )
            elif palette_mode == 1:
                hue = (
                    0.5
                    + i * 0.1
                    + math.cos(step * 0.001) * 0.08
                )
            else:
                hue = (
                    0.8
                    + i * 0.05
                    + math.sin(step * 0.003) * 0.04
                )
            r, g, b = colorsys.hsv_to_rgb(
                hue % 1.0,
                0.9,
                1.0
            )
            t.pencolor(r, g, b)
            t.pensize(
                1.5 + abs(math.sin(a * 2)) * 3
            )
            t.goto(x, y)

        screen.update()
        time.sleep(0.005)
except turtle.Terminator:
    pass