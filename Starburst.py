import turtle
import colorsys

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#050505")
screen.title("Starburst")
screen.tracer(5)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

def draw_starburst():
    hue = 0
    for i in range(400):
        color = colorsys.hsv_to_rgb(hue, 0.8, 1)
        t.pencolor(color)
        hue += 0.008
        t.forward(i)
        t.right(137.5)
        t.forward(i / 2)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.circle(i, 30)

        if i % 5 == 0:
            screen.update()
draw_starburst()
screen.exitonclick()