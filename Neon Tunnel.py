import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.tracer(5)

for i in range(300):
    color = colorsys.hsv_to_rgb(i/300, 1.0, 1.0)
    t.pencolor(color)
    for _ in range(4):
        t.forward(i)
        t.left(90)
    
    t.left(5)
    t.width(2)

turtle.done()