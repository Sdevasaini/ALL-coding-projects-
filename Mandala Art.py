import turtle
import math
import random

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#0b0f19")
screen.title("Mandala Art")
screen.tracer(2)
artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)
artist.pensize(1.5)

colors = [
    "#ff2a6d", "#05d9e8", "#ff007f", "#39ff14", 
    "#ffe600", "#9d00ff", "#00ffcc", "#ff5500"
]

def draw_mandala():
    num_petals = 12
    layers = 8
    
    for layer in range(1, layers + 1):
        radius = layer * 35
        color_choice = colors[(layer - 1) % len(colors)]
        artist.pencolor(color_choice)
        
        for i in range(num_petals):
            angle = (i * 360 / num_petals)
            rad = math.radians(angle)
            x = radius * math.cos(rad)
            y = radius * math.sin(rad)
            artist.penup()
            artist.goto(x, y)
            artist.pendown()
            artist.setheading(angle + 90)
            for j in range(4):
                artist.circle(radius * 0.4, 90)
                artist.left(90)

def draw_stars(num_stars=100):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    
    for _ in range(num_stars):
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        size = random.randint(1, 3)
        star.penup()
        star.goto(x, y)
        star.pendown()
        star.dot(size, random.choice(colors))

draw_stars()
draw_mandala()
screen.update()
turtle.done()