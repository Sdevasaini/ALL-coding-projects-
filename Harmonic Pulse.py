import turtle
import math
import colorsys

def setup_environment():
    screen = turtle.Screen()
    screen.title("Harmonic Pulse")
    screen.bgcolor("#050505")
    screen.tracer(100)
    return screen

def heart_curve(t, scale):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x * scale, y * scale

def draw_animation():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    for t in [t1, t2]:
        t.hideturtle()
        t.speed(0)
        t.width(2)
        t.pensize(2)
    for i in range(500):
        hue = i / 150.0
        color = colorsys.hsv_to_rgb(hue % 1.0, 0.8, 1.0)
        t1.pencolor(color)
        t2.pencolor(color)
        pulse = 0.2 + 0.15 * math.sin(i * 0.1)
        angle = i * 12
        radius = i * 0.6
        x_pos = radius * math.cos(math.radians(angle))
        y_pos = radius * math.sin(math.radians(angle))
        
        for t, x_offset, y_offset in [(t1, x_pos, y_pos), (t2, -x_pos, -y_pos)]:
            t.penup()
            t.goto(x_offset, y_offset)
            t.pendown()
            for j in range(0, 70):
                hx, hy = heart_curve(j / 10, pulse)
                t.goto(x_offset + hx, y_offset + hy)
        
        if i % 2 == 0:
            turtle.update()
    turtle.done()
if __name__ == "__main__":
    screen = setup_environment()
    try:
        draw_animation()
    except turtle.Terminator:
        print("Animation finished.")