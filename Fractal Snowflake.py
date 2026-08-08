import turtle
import colorsys

def setup_environment():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Fractal Snowflake")
    screen.tracer(5)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return screen, t

def draw_fractal(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_fractal(t, order - 1, size / 3)
            t.left(angle)

def run_art():
    screen, t = setup_environment()
    h = 0
    for i in range(12):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        t.pencolor(color)
        h += 0.08
        
        for _ in range(6):
            draw_fractal(t, 3, 100)
            t.left(60)
        t.right(30)

    t.penup()
    t.goto(0, -250)
    t.color("white")
    t.write("", align="center", font=("Arial", 16, "bold"))
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    try:
        run_art()
    except turtle.Terminator:
        pass