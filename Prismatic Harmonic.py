import turtle
import colorsys
import math

def draw_prismatic_web():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Prismatic Harmonic")
    screen.tracer(11)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    iterations = 1200
    hue = 0.0
    
    try:
        for i in range(iterations):
            color = colorsys.hsv_to_rgb(hue, 0.95, 1)
            t.pencolor(color)
            width = (math.sin(i * 0.05) * 1.5) + 2.5 
            t.width(width)
            angle = i * 20
            radius = i * 0.4
            x = math.cos(math.radians(angle)) * radius
            y = math.sin(math.radians(angle)) * radius
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.circle(i * 0.05, 180)
    
            hue += 0.0015
            if i % 3 == 0:
                screen.update()
                
    except turtle.Terminator:
        pass
    
    print(" ")
    screen.exitonclick()

if __name__ == "__main__":
    draw_prismatic_web() 