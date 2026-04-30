import turtle
import colorsys
import math

def draw_muralidhar_mandala():
    screen = turtle.Screen()
    screen.bgcolor("#000814")
    screen.title("Muralidhar")
    screen.setup(width=800, height=800)
    screen.tracer(2)
    t = turtle.Turtle()
    t.speed(0)
    t.width(1)
    t.hideturtle()
    iterations = 360
    for i in range(iterations):

        hue = (i / iterations) * 0.7 
        if i > 250:
            color = colorsys.hsv_to_rgb(0.12, 0.8, 1)
        else:
            color = colorsys.hsv_to_rgb(0.5 + (hue * 0.5), 0.9, 1)
        t.pencolor(color)
        
        angle = i * 137.508
        dist = i * 0.8
        
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(dist)
        t.pendown()
        arc_size = 20 + math.sin(i * 0.1) * 30
        t.circle(arc_size, 180)
        
        if i % 20 == 0:
            t.dot(5, "#FFD700")

    t.width(2)
    for j in range(8):
        t.penup()
        t.goto(0, 0)
        t.setheading(j * 45)
        t.pencolor("#FFD700")
        for k in range(10):
            t.pendown()
            t.forward(30)
            t.penup()
            t.forward(10)
            t.dot(8, "#B22222")
    t.penup()
    for m in range(72):
        t.goto(0, 0)
        t.setheading(m * 5)
        t.forward(350)
        t.pendown()
        
        color = colorsys.hsv_to_rgb(0.5 + (math.sin(m)*0.1), 0.8, 1)
        t.pencolor(color)
        t.circle(15, steps=3) 
        
    screen.update()
    print("Muralidhar Mandala complete. Click to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    try:
        draw_muralidhar_mandala()
    except (turtle.Terminator, Exception):
        pass