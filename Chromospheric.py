import turtle
import colorsys
import math

def draw_vortex_effect():

    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Chromospheric")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(2, 0) 
    hue = 0.0
    iterations = 400
    magic_angle = 121 

    try:
        for i in range(iterations):
            color = colorsys.hsv_to_rgb(hue, 0.9, 1)
            t.pencolor(color)
            hue += 1/iterations 
            width = (math.sin(i * 0.05) * 2) + 3
            t.width(width)
            t.forward(i * 1.5)
            t.left(magic_angle)
            t.circle(i, 90)
            t.right(45) 
            if i % 2 == 0:
                screen.update()

    except turtle.Terminator:
        pass

    print("Pattern complete.")
    screen.exitonclick()

if __name__ == "__main__":
    draw_vortex_effect() 