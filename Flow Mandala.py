import turtle
import math

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("#0F172A")
screen.title("Flow Mandala")
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
turtle.colormode(255)

palette = [
    (129, 140, 248),
    (192, 132, 252),
    (244, 114, 182), 
    (56, 189, 248),
    (45, 212, 191),
    (251, 191, 36)
]

def draw_flowing_petals():
    layers = 24
    for l in range(layers):
        t.color(palette[l % len(palette)])
        t.pensize(1.5)
        petals = 12
        angle_step = 360 / petals
        radius = 80 + l * 10
        
        for i in range(petals):
            t.penup()
            t.goto(0, 0)
            t.setheading(i * angle_step + (l * 3))
            t.forward(radius * 0.4)
            t.pendown()
            t.circle(radius * 0.6, 120)
            t.left(120)
            t.circle(radius * 0.6, 120)

def draw_zen_ripples():
    rings = 18
    for r in range(rings):
        t.color(palette[(r + 3) % len(palette)])
        t.pensize(1)
        t.penup()
        t.goto(0, -(35 + r * 18))
        t.pendown()
        t.circle(35 + r * 18)

def draw_inner_mandala_core():
    t.pensize(2)
    spokes = 30
    angle_step = 360 / spokes
    for i in range(spokes):
        t.color(palette[i % len(palette)])
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle_step)
        t.pendown()
        t.forward(60)
        t.circle(20, 180)

try:
    draw_zen_ripples()
    draw_flowing_petals()
    draw_inner_mandala_core()
    screen.update()
    t.penup()
    t.goto(0, -420)
    t.color("#94A3B8")
    t.write("", align="center", font=("Courier", 13, "italic"))
    
except Exception as e:
    print(f"An error occurred during drawing: {e}")
screen.mainloop()