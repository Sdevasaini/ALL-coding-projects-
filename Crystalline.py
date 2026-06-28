import turtle
import random

def draw_branch(t, length, depth):
    if depth == 0:
        return
    t.pencolor(0.2, 0.5 + (depth * 0.05), 0.8)
    t.width(depth * 0.5)
    t.forward(length)
    for i in range(3):
        t.right(120)
        draw_branch(t, length * 0.5, depth - 1)  
    t.penup()
    t.backward(length)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("#020205")
    screen.tracer(80)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i in range(8):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * 45)
        draw_branch(t, 150, 7)
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()