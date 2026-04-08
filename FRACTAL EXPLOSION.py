import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("ULTRA FRACTAL EXPLOSION")
screen.tracer(120)
t = turtle.Turtle()
t.speed(0)
t.width(1)

hue = 0
def draw_fractal(x, y, angle, depth, length):
    global hue
    
    if depth == 0:
        return
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    color = colorsys.hsv_to_rgb(hue % 1, 1, 1)
    t.pencolor(color)
    hue += 0.002

    t.forward(length)

    new_x, new_y = t.position()
    for a in [-45, -20, 0, 20, 45]:
        draw_fractal(new_x, new_y, angle + a, depth - 1, length * 0.75)

# MULTI-SYMMETRY (ULTRA EFFECT)
for i in range(12):
    draw_fractal(0, 0, i * 30, 6, 120)

screen.update()
t.hideturtle()
turtle.done()