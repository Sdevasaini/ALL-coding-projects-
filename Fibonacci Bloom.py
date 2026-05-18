import turtle
import colorsys
import math

def setup():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1000, height=1000)
    screen.tracer(100)
    return screen

def draw_galactic_bloom():  
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    iterations = 240
    spin = 137.508 
    
    for i in range(iterations):
        hue = (0.68 - (i / iterations) * 0.75) % 1.0
        t.pencolor(colorsys.hsv_to_rgb(hue, 0.8, 1))
        t.penup()
        t.goto(0, 0)
        t.setheading(i * spin)
        offset = i * 0.6
        t.forward(offset)
        t.pendown()
        t.width(max(1, i / 60))
    
        for _ in range(2):
            t.circle(i * 0.8, 70)
            t.left(110)
            t.circle(i * 0.3, 70)
            t.left(110)
            
        if i % 8 == 0:
            turtle.update()

    turtle.update()

def main():
    screen = setup()
    draw_galactic_bloom()
    print("Galactic Bloom Rendered")
    screen.exitonclick()

if __name__ == "__main__":
    main()