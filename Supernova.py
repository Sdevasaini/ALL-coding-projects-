import turtle
import math

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.tracer(0)
turtles = [turtle.Turtle() for _ in range(8)]
colors = ["#FF1493", "#00FFFF", "#FFD700",
           "#7FFF00", "#FF4500", "#9932CC", 
           "#FFFFFF", "#FF69B4"]

for i, t in enumerate(turtles):
    t.speed(0)
    t.color(colors[i])
    t.width(2)
    t.hideturtle()

for angle in range(0, 360, 2):
    for i, t in enumerate(turtles):
        radius = angle * 0.8
        t.penup()
        x = radius * math.cos(math.radians(angle + i * 45))
        y = radius * math.sin(math.radians(angle + i * 45))
        t.goto(x, y)
        t.pendown()
        t.circle(radius / 10, 60)
        
    screen.update()
turtle.done()