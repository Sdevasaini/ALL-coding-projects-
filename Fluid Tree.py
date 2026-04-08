import turtle
import random

def setup_canvas():
    screen = turtle.Screen()
    screen.bgcolor("#F5F5F0") 
    screen.setup(width=900, height=900)
    screen.title("Fluid Recursive Growth (Biological Ink)")
    screen.tracer(10)
    return screen

def grow(t, length, thickness, angle, wind):
    if length < 5:
        return
    t.pensize(thickness)
    
    color_val = int(255 - (thickness * 15))
    color_val = max(min(color_val, 200), 20)
    color_hex = f'#{color_val:02x}{color_val:02x}{color_val:02x}'
    t.pencolor(color_hex)
    t.forward(length)
    
    new_length = length * random.uniform(0.7, 0.8)
    new_thickness = thickness * 0.7
    pos = t.pos()
    head = t.heading()

    t.right(angle + random.uniform(-10, 20) + wind)
    grow(t, new_length, new_thickness, angle, wind)
    t.penup()
    t.goto(pos)
    t.setheading(head)
    t.pendown()
    t.left(angle + random.uniform(-10, 20) - wind)
    grow(t, new_length, new_thickness, angle, wind)
    t.penup()
    t.goto(pos)
    t.setheading(head)
    t.pendown()  
def main():
    screen = setup_canvas()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, -350)
    t.left(90)
    t.pendown()
    grow(t, 120, 15, 25, 5)

    print("Ink growth complete. Click to exit.")
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    turtle.colormode(255)
    main()