import turtle
import colorsys
import math

def draw_vortex():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Vortex")
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(10, 0)
    iterations = 360
    cycles = 6 
    
    for i in range(iterations):
        hue = i / iterations
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(color)
        t.pensize(abs(math.sin(i * 0.05)) * 2 + 1)
        angle = i * (360 / cycles) + (i * 0.5)
        distance = math.sqrt(i) * 16 
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(distance)
        t.pendown()
        t.begin_fill()
        t.fillcolor(colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 0.8, 0.3))
        
        for _ in range(5):
            t.forward(i * 0.15)
            t.right(144)
            t.forward(i * 0.15)
            t.left(72)
        t.end_fill()
        if i % 10 == 0:
            
            screen.update()
    screen.update()
    t.penup()
    t.goto(0, -350)
    t.pencolor("white")
    t.write(" ", align="center", font=("Arial", 16, "bold"))
    screen.mainloop()

if __name__ == "__main__":
    draw_vortex()