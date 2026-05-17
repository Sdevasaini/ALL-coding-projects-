import turtle
import colorsys
import math

def setup():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=900, height=900)
    screen.tracer(5)
    return screen

def draw_phyllotaxis_neon():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    phi = 137.508 * (math.pi / 180) 
    c = 4
    
    for n in range(600):
        r = c * math.sqrt(n)
        theta = n * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        hue = (n % 255) / 255
        t.pencolor(colorsys.hsv_to_rgb(hue, 0.9, 1))
        t.width(math.sin(n * 0.1) * 3 + 4)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(n * 137.5)
        t.forward(n / 10)

    turtle.update()

def draw_radial_web():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    points = 120
    radius = 350
    coords = []
    for i in range(points):
        angle = math.radians(i * (360/points))
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        coords.append((x, y))
    for i in range(points):
        hue = i / points
        t.pencolor(colorsys.hsv_to_rgb(hue, 0.8, 1))
        target_index = (i * 3) % points 
        t.penup()
        t.goto(coords[i])
        t.pendown()
        t.goto(coords[target_index])
        
    turtle.update()

def main():
    screen = setup()
    draw_phyllotaxis_neon()
    screen.exitonclick()

if __name__ == "__main__":
    main()