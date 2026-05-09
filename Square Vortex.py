import turtle
import colorsys

def draw_vortex():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Square Vortex")
    screen.tracer(5)
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()

    for i in range(500):
        color = colorsys.hsv_to_rgb(i/60, 0.8, 1.0)
        t.pencolor(color)
        t.forward(i) 
        t.left(91)
        for _ in range(4):
            t.forward(i)
            t.left(90)
        if i % 5 == 0:
            screen.update()

    screen.update()
    print("Vortex complete! Click to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    draw_vortex()